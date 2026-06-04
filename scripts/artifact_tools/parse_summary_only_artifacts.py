#!/usr/bin/env python3
"""Parse summary-only artifact logs and produce a structured manifest.

Expected-count file format (JSON, passed via --expected):
  [{"p": 31, "b": 17, "count": 3991995}, ...]

Usage:
    parse_summary_only_artifacts.py --root <repo_root> --expected <file>
"""

import argparse
import csv
import json
import re
import sys
import time
from pathlib import Path


def load_expected(path: str) -> dict:
    with open(path) as f:
        entries = json.load(f)
    if isinstance(entries, dict):
        return {(int(k.split(":")[0]), int(k.split(":")[1])): v for k, v in entries.items()}
    return {(e["p"], e["b"]): e["count"] for e in entries}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def grab(pattern: str, text: str, default=None, cast=str):
    m = re.search(pattern, text, re.MULTILINE)
    if not m:
        return default
    return cast(m.group(1))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=".", help="Repository root directory (default: current dir)")
    ap.add_argument("--expected", required=True, help="Path to JSON file with expected counts")
    ap.add_argument("--summary-dir", default="local_artifacts/summary_only",
                    help="Directory containing summary-only pass log files (relative to root)")
    ap.add_argument("--outdir", default="local_artifacts/batch_manifest",
                    help="Output directory for manifest files (relative to root)")
    ap.add_argument("--allow-empty", action="store_true", help="Do not fail when no matching files are found")
    ap.add_argument("--allow-unknown", action="store_true", help="Do not fail on domains not in expected counts")
    args = ap.parse_args()

    ROOT = Path(args.root).resolve()
    SUMMARY_DIR = ROOT / args.summary_dir
    if not SUMMARY_DIR.is_dir():
        raise SystemExit(f"Summary directory does not exist: {SUMMARY_DIR}")

    OUTDIR = ROOT / args.outdir
    OUTDIR.mkdir(parents=True, exist_ok=True)

    expected_counts = load_expected(args.expected)

    paths = sorted(SUMMARY_DIR.glob("*summary_only*pass*.txt"))
    if not paths:
        msg = f"No summary-only pass files found in {SUMMARY_DIR}"
        if args.allow_empty:
            print(msg)
            return 0
        raise SystemExit(msg)

    rows: list[dict] = []
    t0 = time.time()

    for path in paths:
        text = read_text(path)

        cases = grab(r"^cases=(\S+)", text)
        seed = grab(r"^seed=(\d+)", text, cast=int)
        max_nodes = grab(r"^max_nodes=(\d+)", text, cast=int)
        restarts = grab(r"^restarts=(\d+)", text, cast=int)
        greedy_restarts = grab(r"^greedy_restarts=(\d+)", text, cast=int)
        total_processed = grab(r"^total_processed=(\d+)", text, cast=int)
        total_solved = grab(r"^total_solved=(\d+)", text, cast=int)
        failed = grab(r"^failed=(\d+)", text, cast=int)
        aggregate_sha256 = grab(r"^aggregate_sha256=([0-9a-fA-F]+)", text)
        elapsed_seconds = grab(r"^elapsed_seconds=([0-9.]+)", text, cast=float)
        verdict = grab(r"^VERDICT:\s*(\S+)", text)

        if not cases:
            raise SystemExit(f"Could not parse cases= from {path}")

        p_str, b_str = cases.split(":")
        p = int(p_str)
        b = int(b_str)
        expected = expected_counts.get((p, b))

        if expected is None:
            if not args.allow_unknown:
                raise SystemExit(f"Unknown domain p={p} b={b} in file {path.name}. Use --allow-unknown to skip this check.")
            status = "UNKNOWN_EXPECTED"
        else:
            status = "PASS_SUMMARY_COUNT" if total_processed == expected and total_solved == expected and failed == 0 else "FAIL_SUMMARY_COUNT"

        rows.append({
            "p": p,
            "b": b,
            "domain": f"{p}:{b}",
            "artifact_type": "summary_only_digest",
            "filename": path.name,
            "full_path": str(path),
            "cases": cases,
            "seed": seed,
            "max_nodes": max_nodes,
            "restarts": restarts,
            "greedy_restarts": greedy_restarts,
            "processed": total_processed,
            "solved": total_solved,
            "failed": failed,
            "expected_canonical": expected if expected is not None else "",
            "status": status,
            "aggregate_sha256": aggregate_sha256,
            "elapsed_seconds": elapsed_seconds,
            "verdict": verdict,
            "artifact_availability": "summary_only_log",
            "verification_status": "summary_only_deterministic_generation_pass",
        })

    rows.sort(key=lambda r: (r["p"], r["b"], r["filename"]))

    csv_path = OUTDIR / "summary_only_artifact_manifest.csv"
    json_path = OUTDIR / "summary_only_artifact_manifest.json"
    md_path = OUTDIR / "summary_only_artifact_manifest.md"

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [])
        writer.writeheader()
        writer.writerows(rows)

    gen_time = int(time.time())
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "schema": "erdos475.summary_only_artifact_manifest.v1",
                "generated_at_unix": gen_time,
                "elapsed_seconds": round(time.time() - t0, 3),
                "artifacts": rows,
            },
            f,
            indent=2,
        )

    with md_path.open("w", encoding="utf-8") as f:
        f.write("# Summary-only artifact manifest\n\n")
        f.write(f"Generated at UNIX timestamp: {gen_time}\n\n")
        f.write("| p | b | processed | solved | failed | expected | status | aggregate_sha256 | verdict | filename |\n")
        f.write("|---:|---:|---:|---:|---:|---:|---|---|---|---|\n")
        for r in rows:
            f.write(
                f"| {r['p']} | {r['b']} | {r['processed']} | {r['solved']} | {r['failed']} | "
                f"{r['expected_canonical']} | {r['status']} | `{r['aggregate_sha256']}` | "
                f"{r['verdict']} | `{r['filename']}` |\n"
            )

    print(f"wrote={csv_path}")
    print(f"wrote={json_path}")
    print(f"wrote={md_path}")
    print(f"records={len(rows)}")

    bad = [r for r in rows if str(r["status"]).startswith("FAIL") or r["verdict"] != "PASS"]
    print(f"bad_records={len(bad)}")
    if bad:
        raise SystemExit(bad)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
