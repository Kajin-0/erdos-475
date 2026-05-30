import csv
import hashlib
import json
import os
import re
import time
from pathlib import Path

ROOT = Path(r"C:\Users\User1\Downloads\erdos")
OUTDIR = Path(r"C:\Users\User1\Documents\erdos-475\local_artifacts\batch_manifest")
OUTDIR.mkdir(parents=True, exist_ok=True)

EXPECTED = {
    (29, 8): 111041,
    (29, 9): 246675,
    (29, 10): 468754,
    (29, 11): 766935,
    (29, 12): 1086601,
    (29, 13): 1337220,
    (29, 14): 1432860,
    (29, 15): 1337220,

    (31, 7): 67860,
    (31, 8): 195143,
    (31, 9): 476913,
    (31, 10): 1001603,
    (31, 11): 1820910,
    (31, 12): 2883289,
    (31, 13): 3991995,
    (31, 14): 4847637,
    (31, 15): 5170604,
    (31, 16): 4847637,
    (31, 17): 3991995,
}

PAT = re.compile(r"p(?P<p>\d+)_b(?P<b>\d+).*\.jsonl$", re.IGNORECASE)

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

rows = []
files = sorted(ROOT.glob("*.jsonl"))

print(f"root={ROOT}")
print(f"jsonl_files_found={len(files)}")
print()

t0 = time.time()

for i, path in enumerate(files, start=1):
    m = PAT.search(path.name)
    if not m:
        print(f"[skip] could not parse p,b from filename: {path.name}")
        continue

    p = int(m.group("p"))
    b = int(m.group("b"))
    expected = EXPECTED.get((p, b))

    print(f"[{i}/{len(files)}] hashing/counting p={p} b={b} file={path.name}")
    sha, lines, size = hash_and_count(path)

    status = "UNKNOWN_EXPECTED"
    if expected is not None:
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

with json_path.open("w", encoding="utf-8") as f:
    json.dump(
        {
            "schema": "erdos475.local_jsonl_artifact_manifest.v1",
            "root": str(ROOT),
            "generated_at_unix": int(time.time()),
            "elapsed_seconds": round(time.time() - t0, 3),
            "artifacts": rows,
        },
        f,
        indent=2,
    )

with md_path.open("w", encoding="utf-8") as f:
    f.write("# Local JSONL artifact manifest\n\n")
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
