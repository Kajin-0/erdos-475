#!/usr/bin/env python3
"""Fetch and unpack an arXiv TeX source bundle.

This helper is for theorem-effectivity extraction. It downloads the arXiv e-print
source bundle, detects whether it is a tar archive, gzip-compressed tar archive,
or single TeX file, and writes the contents into an output directory.

Example:
  python scripts/fetch_arxiv_source_bundle.py 2602.15797 \
    --out-dir data/theorem_extraction/pham_sauermann_2026_source

Notes:
  - This script requires network access.
  - It does not certify any theorem statement.
  - Use it to recover displayed equations that arXiv HTML strips.
"""

from __future__ import annotations

import argparse
import gzip
import io
import tarfile
import urllib.request
from pathlib import Path


ARXIV_EPRINT_URL = "https://arxiv.org/e-print/{arxiv_id}"


def safe_member_path(out_dir: Path, member_name: str) -> Path:
    target = (out_dir / member_name).resolve()
    root = out_dir.resolve()
    if not str(target).startswith(str(root) + "/") and target != root:
        raise ValueError(f"unsafe tar member path: {member_name!r}")
    return target


def try_extract_tar(data: bytes, out_dir: Path) -> bool:
    for mode in ("r:gz", "r:"):
        try:
            with tarfile.open(fileobj=io.BytesIO(data), mode=mode) as tf:
                for member in tf.getmembers():
                    if not member.isfile():
                        continue
                    target = safe_member_path(out_dir, member.name)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    src = tf.extractfile(member)
                    if src is None:
                        continue
                    target.write_bytes(src.read())
            return True
        except tarfile.TarError:
            continue
    return False


def maybe_gunzip(data: bytes) -> bytes:
    if data[:2] == b"\x1f\x8b":
        try:
            return gzip.decompress(data)
        except OSError:
            return data
    return data


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("arxiv_id", help="arXiv id, e.g. 2602.15797")
    ap.add_argument("--out-dir", required=True, help="Directory to write source files")
    args = ap.parse_args()

    url = ARXIV_EPRINT_URL.format(arxiv_id=args.arxiv_id)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    req = urllib.request.Request(url, headers={"User-Agent": "erdos-475-source-extraction/0.1"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()

    raw_path = out_dir / f"{args.arxiv_id.replace('/', '_')}.eprint"
    raw_path.write_bytes(data)

    if try_extract_tar(data, out_dir):
        print(f"downloaded and extracted tar source from {url} -> {out_dir}")
        return 0

    decompressed = maybe_gunzip(data)
    if decompressed != data and try_extract_tar(decompressed, out_dir):
        print(f"downloaded, gunzipped, and extracted tar source from {url} -> {out_dir}")
        return 0

    # Fall back to a single TeX/plain file.
    tex_path = out_dir / f"{args.arxiv_id.replace('/', '_')}.tex"
    tex_path.write_bytes(decompressed)
    print(f"downloaded source from {url}; wrote fallback single file {tex_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
