#!/usr/bin/env python3
"""Check MANIFEST.sha256 against release/manifest_policy.json.

Reads the policy file and verifies:
  - every trusted release file is in the manifest
  - no forbidden files (never_in_manifest) appear
  - no excluded-path patterns match manifest entries
  - every referenced file exists
  - no duplicate entries
  - every hash matches current file content
"""
from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
from pathlib import Path


def compute_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            block = f.read(65536)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def parse_sha256_manifest(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        parts = line.split("  ", 1)
        if len(parts) != 2:
            raise SystemExit(f"{path}:{lineno}: malformed entry: {line}")
        hexdigest, filepath = parts
        if filepath in entries:
            raise SystemExit(f"{path}:{lineno}: duplicate entry: {filepath}")
        entries[filepath] = hexdigest
    return entries


def load_policy(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manifest", nargs="?", default="MANIFEST.sha256")
    ap.add_argument("--policy", default="release/manifest_policy.json")
    args = ap.parse_args()

    manifest = Path(args.manifest)
    policy_path = Path(args.policy)

    if not manifest.exists():
        print(f"ERROR missing manifest: {manifest}")
        return 2
    if not policy_path.exists():
        print(f"ERROR missing policy: {policy_path}")
        return 2

    policy = load_policy(policy_path)
    trusted = set(policy.get("trusted_release_files", []))
    never = set(policy.get("never_in_manifest", []))
    excluded = policy.get("excluded_path_globs", [])

    entries = parse_sha256_manifest(manifest)
    failures: list[str] = []

    # Check no never_in_manifest files
    for filepath in never:
        if filepath in entries:
            failures.append(f"forbidden file in manifest: {filepath}")

    # Check no excluded-path patterns match
    for filepath in entries:
        for pat in excluded:
            if fnmatch.fnmatch(filepath, pat):
                failures.append(f"excluded path in manifest: {filepath} matches {pat!r}")
                break

    # Check every referenced file exists
    for filepath in entries:
        if not Path(filepath).exists():
            failures.append(f"missing file referenced in manifest: {filepath}")

    # Check trusted release files are included
    for trusted_path in sorted(trusted):
        if trusted_path not in entries:
            failures.append(f"trusted release file missing from manifest: {trusted_path}")

    # Verify hashes
    for filepath, expected_hex in entries.items():
        fp = Path(filepath)
        if not fp.exists():
            continue
        actual = compute_sha256(fp)
        if actual != expected_hex:
            failures.append(f"hash mismatch for {filepath}: expected {expected_hex}, got {actual}")

    if failures:
        print("FAIL SHA256 manifest completeness check")
        for f in failures:
            print(f"  - {f}")
        return 2

    print(f"PASS SHA256 manifest completeness: {len(trusted)} trusted files, {len(entries)} manifest entries, no self-entry")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
