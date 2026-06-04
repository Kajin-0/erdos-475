#!/usr/bin/env python3
"""Scan local JSONL witness files and produce a structured manifest.

Expected-count file format (JSON, passed via --expected):
  [{"p": 29, "b": 8, "count": 111041}, ...]

Usage:
    batch_local_jsonl_manifest.py --root <dir> --expected <file> --outdir <dir>
"""

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

PAT = re.compile(r"p(?P<p>\d+)_b(?P<b>\d+).*\.jsonl$", re.IGNORECASE)


def load_expected(path: str) -> dict:
    with open(path) as f:
        entries = json.load(f)
    if isinstance(entries, dict):
        return {(int(k.split(":")[0]), int(k.split(":")[1])): v for k, v in entries.items()}
    return {(e["p"], e["b"]): e["count"] for e in entries}


def hash_and_count(path: Path):
    h = hashlib.sha256()
    line_count = 0
    size = path.stat().st_size
    with path.open("rb") as f:
        while True:
            block = f.read(8 * 1024 * 1024)
            if not block:
                break
            h.update(block)
            line_count += block.count(b"\n")
    return h.hexdigest(), line_count, size


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", required=True, help="Directory containing JSONL witness files")
    ap.add_argument("--expected", required=True, help="Path to JSON file with expected counts")
    ap.add_argument("--outdir", required=True, help="Output directory for manifest files")
    ap.add_argument("--allow-empty", action="store_true", help="Do not fail when no matching files are found")
    ap.add_argument("--allow-unknown", action="store_true", help="Do not fail on domains not in expected counts")
    args = ap.parse_args()

    ROOT = Path(args.root)
    if not ROOT.is_dir():
        raise SystemExit(f"Input root directory does not exist: {ROOT}")

    OUTDIR = Path(args.outdir)
    OUTDIR.mkdir(parents=True, exist_ok=True)

    expected_counts = load_expected(args.expected)

    files = sorted(ROOT.glob("*.jsonl"))
    if not files:
        msg = f"No JSONL files found in {ROOT}"
        if args.allow_empty:
            print(msg)
            return 0
        raise SystemExit(msg)

    rows: list[dict] = []
    t0 = time.time()

    for i, path in enumerate(files, start=1):
        m = PAT.search(path.name)
        if not m:
            print(f"[skip] could not parse p,b from filename: {path.name}")
            continue

        p = int(m.group("p"))
        b = int(m.group("b"))
        expected = expected_counts.get((p, b))

        print(f"[{i}/{len(files)}] hashing/counting p={p} b={b} file={path.name}")
        sha, lines, size = hash_and_count(path)

        if expected is None:
            if not args.allow_unknown:
                raise SystemExit(f"Unknown domain p={p} b={b} in file {path.name}. Use --allow-unknown to skip this check.")
            status = "UNKNOWN_EXPECTED"
        else:
            status = "PASS_LINE_COUNT" if lines == expected else "FAIL_LINE_COUNT"

        row = {
            "p": p,
            "b": b,
            "domain": f"{p}:{b}",
            "filename": path.name,
            "full_path": str(path),
            "size_bytes": size,
            "size_mib": round(size / (1024 * 1024), 3),
            "sha256": sha,
            "line_count": lines,
            "expected_canonical": expected if expected is not None else "",
            "line_count_status": status,
            "artifact_availability": "local_pc",
            "verification_status": "previously_generated_and_verified_by_local_workflow",
        }
        rows.append(row)
        print(f"    lines={lines} expected={expected} size_mib={row['size_mib']} sha256={sha[:16]}... status={status}")

    rows.sort(key=lambda r: (r["p"], r["b"], r["filename"]))

    csv_path = OUTDIR / "local_jsonl_artifact_manifest.csv"
    json_path = OUTDIR / "local_jsonl_artifact_manifest.json"
    md_path = OUTDIR / "local_jsonl_artifact_manifest.md"

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [])
        writer.writeheader()
        writer.writerows(rows)

    gen_time = int(time.time())
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "schema": "erdos475.local_jsonl_artifact_manifest.v1",
                "root": str(ROOT),
                "generated_at_unix": gen_time,
                "elapsed_seconds": round(time.time() - t0, 3),
                "artifacts": rows,
            },
            f,
            indent=2,
        )

    with md_path.open("w", encoding="utf-8") as f:
        f.write("# Local JSONL artifact manifest\n\n")
        f.write(f"Generated at UNIX timestamp: {gen_time}\n\n")
        f.write("This manifest records local witness JSONL artifacts that may be too large to commit directly.\n\n")
        f.write("| p | b | lines | expected | status | size MiB | sha256 | filename |\n")
        f.write("|---:|---:|---:|---:|---|---:|---|---|\n")
        for r in rows:
            f.write(
                f"| {r['p']} | {r['b']} | {r['line_count']} | {r['expected_canonical']} | "
                f"{r['line_count_status']} | {r['size_mib']} | `{r['sha256']}` | `{r['filename']}` |\n"
            )

    print()
    print(f"wrote={csv_path}")
    print(f"wrote={json_path}")
    print(f"wrote={md_path}")
    print(f"elapsed_seconds={time.time() - t0:.2f}")

    bad = [r for r in rows if r["line_count_status"].startswith("FAIL")]
    unknown = [r for r in rows if r["line_count_status"] == "UNKNOWN_EXPECTED"]

    print()
    print(f"artifacts_recorded={len(rows)}")
    print(f"line_count_failures={len(bad)}")
    print(f"unknown_expected={len(unknown)}")

    if bad:
        print("FAILURES:")
        for r in bad:
            print(r)

    if unknown:
        print("UNKNOWN EXPECTED:")
        for r in unknown:
            print(r["filename"], r["domain"], r["line_count"])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
