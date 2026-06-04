#!/usr/bin/env python3
"""Scan high-risk documentation files for unsafe overclaims.

Unsafe phrases (in non-claim/non-blocker contexts):
  - complete proof
  - solved
  - final proof
  - theorem proved
  - proof completed
  - residue contained
  - full theorem follows
  - unconditional proof
  - standalone proof

Usage:
    check_no_overclaiming.py [file ...]
    check_no_overclaiming.py  # scans all high-risk files by default
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HIGH_RISK_FILES = [
    "README.md",
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
]

# Phrases that suggest overclaiming (case-insensitive)
UNSAFE_PATTERNS: list[tuple[str, re.Pattern]] = [
    ("complete proof", re.compile(r"complete\s+proof", re.IGNORECASE)),
    ("solved", re.compile(r"(?<!\w)solved(?!\w)", re.IGNORECASE)),
    ("final proof", re.compile(r"final\s+proof", re.IGNORECASE)),
    ("theorem proved", re.compile(r"theorem\s+proved", re.IGNORECASE)),
    ("proof completed", re.compile(r"proof\s+completed", re.IGNORECASE)),
    ("residue contained", re.compile(r"residue\s+contained", re.IGNORECASE)),
    ("full theorem follows", re.compile(r"full\s+theorem\s+follows", re.IGNORECASE)),
    ("unconditional proof", re.compile(r"unconditional\s+proof", re.IGNORECASE)),
    ("standalone proof", re.compile(r"standalone\s+proof", re.IGNORECASE)),
]

# Contexts where unsafe phrases are acceptable (non-claim, limitation, blocker)
SAFE_CONTEXTS = [
    "not claim", "not proved", "not a complete proof", "not yet",
    "not currently", "do not claim", "does not claim", "does not prove",
    "would require", "remains conditional", "currently missing",
    "safe current claim", "unsafe claims", "unsafe claim",
    "explicit non-claims", "forbidden claims",
    "not claimed here", "not claimed",
    "avoid language such as", "do not use", "should not",
    "does not currently claim", "does not prove",
    "is not a complete proof", "not an unconditional proof",
    "not the same as", "not as a complete proof",
    "should not be presented as", "not release-grade",
    "do not claim the full", "the full theorem would require",
    "the full theorem is not claimed", "not a full proof",
    "repository must not currently claim",
    "no document claims",
    # Technical field names in summary-only artifact contexts
    "processed", "solved_count", "total_solved",
    # Checklist items describing unsafe phrases (not claiming them)
    "unsafe phrases", "such as", "like",
]


def is_safe_context(lines: list[str]) -> bool:
    lower = " ".join(l.lower() for l in lines)
    return any(ctx in lower for ctx in SAFE_CONTEXTS)


def scan_file(path: Path) -> list[str]:
    findings: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"ERROR reading {path}: {e}"]

    raw = text.splitlines()
    for lineno, line in enumerate(raw, start=1):
        # Check current line plus up to 5 previous lines for safe context
        ctx_lines = raw[max(0, lineno - 6):lineno]
        if is_safe_context(ctx_lines):
            continue
        for name, pattern in UNSAFE_PATTERNS:
            if pattern.search(line):
                findings.append(f"{path}:{lineno}: possible overclaim '{name}' in: {line.strip()[:120]}")
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*", default=HIGH_RISK_FILES, help="Files to scan")
    args = ap.parse_args()

    all_findings: list[str] = []
    for filepath in args.files:
        path = Path(filepath)
        if not path.exists():
            print(f"SKIP {filepath}: not found")
            continue
        findings = scan_file(path)
        all_findings.extend(findings)
        for f in findings:
            print(f)

    if all_findings:
        print(f"\nFAIL overclaim scan: {len(all_findings)} finding(s)")
        return 2
    else:
        print(f"PASS overclaim scan: {len(args.files)} files scanned, no unsafe overclaims found")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
