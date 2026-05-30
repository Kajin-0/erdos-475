import hashlib
from pathlib import Path

out_path = Path("jsonl_manifest_sha256.txt")

with out_path.open("w", encoding="utf-8") as out:
    count = 0

    for path in sorted(Path(".").glob("*.jsonl")):
        h = hashlib.sha256()

        with path.open("rb") as f:
            for block in iter(lambda: f.read(1024 * 1024), b""):
                h.update(block)

        digest = h.hexdigest()
        size = path.stat().st_size

        out.write(f"{digest}  {size}  {path.name}\n")
        print(f"{digest}  {size}  {path.name}")
        count += 1

print(f"\nwrote {out_path} with {count} JSONL files")
