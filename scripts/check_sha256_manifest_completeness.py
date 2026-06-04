#!/usr/bin/env python3
"""Check MANIFEST.sha256 completeness and consistency.

Validates:
  - MANIFEST.sha256 exists
  - every referenced file exists
  - no duplicate entries
  - every trusted release file is included
  - every included hash matches current content
  - trusted certificate artifacts are included
  - trusted scripts are included
  - trusted docs are included
  - tests are included
  - CI workflow is included
  - MANIFEST.required is included
  - certificates/verified_domains.json is included

Trusted release files list is maintained at the top of this script.

Usage:
    check_sha256_manifest_completeness.py [MANIFEST.sha256]
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

TRUSTED_RELEASE_FILES = [
    "README.md",
    "MANIFEST.required",
    ".github/workflows/verify.yml",
    "certificates/verified_domains.json",
    "certificates/minimal_witnesses.jsonl",
    "certificates/witnesses_p29_b08.jsonl",
    "scripts/run_all_verification.sh",
    "scripts/verify_minimal_witnesses.py",
    "scripts/validate_certificate_schema.py",
    "scripts/audit_canonical_counts.py",
    "scripts/check_required_artifacts.py",
    "scripts/check_manifest_completeness.py",
    "scripts/check_sha256_manifest_completeness.py",
    "scripts/check_claim_boundary_consistency.py",
    "scripts/check_no_overclaiming.py",
    "scripts/ci_classify.sh",
    "scripts/reduction_residue_audit.py",
    "scripts/sweep_coverage_sandwich.py",
    "rust-verifier/Cargo.toml",
    "rust-verifier/src/main.rs",
    "tests/__init__.py",
    "tests/test_verify_minimal_witnesses.py",
    "tests/test_validate_certificate_schema.py",
    "tests/test_audit_canonical_counts.py",
    "docs/CLAIM_BOUNDARY.md",
    "docs/VERIFIED_DOMAIN.md",
    "docs/TRUST_MODEL.md",
    "docs/AI_PROVENANCE.md",
    "docs/EFFECTIVE_FINITE_COMPLETION_THEOREM.md",
    "docs/COVERAGE_SANDWICH_LEMMA.md",
    "docs/SOURCE_EXTRACTION_PRIME_FIELD.md",
    "docs/EXTERNAL_REVIEW_PACKET.md",
    "docs/EXTERNAL_ARTIFACT_LEDGER.md",
    "docs/EXTERNAL_ARTIFACT_VERIFICATION_MODEL.md",
    "docs/FINITE_FRONTIER_STATUS.md",
    "docs/RELEASE_AUDIT_REPORT.md",
    "docs/RELEASE_HARDENING_CHECKLIST.md",
    "data/literature_coverage.json",
]


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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manifest", nargs="?", default="MANIFEST.sha256")
    args = ap.parse_args()

    manifest = Path(args.manifest)
    if not manifest.exists():
        print(f"ERROR missing manifest: {manifest}")
        return 2

    entries = parse_sha256_manifest(manifest)
    failures: list[str] = []

    # Check every referenced file exists
    for filepath in entries:
        if not Path(filepath).exists():
            failures.append(f"missing file referenced in manifest: {filepath}")

    # Check trusted release files are included
    for trusted in TRUSTED_RELEASE_FILES:
        if trusted not in entries:
            failures.append(f"trusted release file missing from manifest: {trusted}")

    # Verify hashes (skip MANIFEST.sha256 — self-referential hash)
    for filepath, expected_hex in entries.items():
        if filepath == "MANIFEST.sha256":
            continue
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

    print(f"PASS SHA256 manifest completeness: {len(entries)} entries, {len(TRUSTED_RELEASE_FILES)} trusted files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
