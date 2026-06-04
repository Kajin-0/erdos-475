#!/usr/bin/env python3
"""Parse summary-only artifact logs and produce a structured manifest.

Usage:
    parse_summary_only_artifacts.py --root <repo_root>
"""

import argparse
import csv
import json
import re
from pathlib import Path

EXPECTED = {
    (31, 17): 3991995,
}


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
    ap.add_argument("--summary-dir", default="local_artifacts/summary_only",
                    help="Directory containing summary-only pass log files (relative to root)")
    ap.add_argument("--outdir", default="local_artifacts/batch_manifest",
                    help="Output directory for manifest files (relative to root)")
    args = ap.parse_args()

    ROOT = Path(args.root).resolve()
    SUMMARY_DIR = ROOT / args.summary_dir
    OUTDIR = ROOT / args.outdir
    OUTDIR.mkdir(parents=True, exist_ok=True)

    rows: list[dict] = []

    for path in sorted(SUMMARY_DIR.glob("*summary_only*pass*.txt")):
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
        expected = EXPECTED.get((p, b))

        status = "UNKNOWN_EXPECTED"
        if expected is not None:
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

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "schema": "erdos475.summary_only_artifact_manifest.v1",
                "artifacts": rows,
            },
            f,
            indent=2,
        )

    with md_path.open("w", encoding="utf-8") as f:
        f.write("# Summary-only artifact manifest\n\n")
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
