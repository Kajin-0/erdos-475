#!/usr/bin/env python3
"""Schema check for docs/source_theorems.yaml.

This script is intentionally lightweight and uses the minimal YAML parser from
reduction_residue_audit.py to avoid adding dependencies.

It checks that the source theorem ledger is machine-actionable and that proof
status fields are explicit. It does not certify any theorem.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Dict, List

# Allow running from repository root without installing as a package.
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from reduction_residue_audit import load_source_theorems  # noqa: E402


REQUIRED_FIELDS = {
    "source_id",
    "authors",
    "title",
    "arxiv_or_publication",
    "theorem_number",
    "exact_statement",
    "prime_hypotheses",
    "set_size_hypotheses",
    "constants_or_thresholds",
    "effective_status",
    "translation_to_p_t",
    "translation_to_p_b",
    "audit_rule_status",
    "citation",
    "notes",
}

VALID_EFFECTIVE_STATUS = {"effective", "non_effective", "pending_extraction"}


def fail(msg: str) -> int:
    print(f"ERROR: {msg}", file=sys.stderr)
    return 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "path",
        nargs="?",
        default="docs/source_theorems.yaml",
        help="Path to source theorem ledger.",
    )
    args = ap.parse_args()

    path = Path(args.path)
    entries = load_source_theorems(path)
    if not entries:
        return fail(f"no source theorem entries found in {path}")

    seen = set()
    errors: List[str] = []
    for i, entry in enumerate(entries, start=1):
        sid = entry.get("source_id", f"<missing-{i}>")
        if sid in seen:
            errors.append(f"duplicate source_id: {sid}")
        seen.add(sid)

        missing = sorted(REQUIRED_FIELDS - set(entry))
        if missing:
            errors.append(f"{sid}: missing required fields: {missing}")

        status = entry.get("effective_status")
        if status not in VALID_EFFECTIVE_STATUS:
            errors.append(f"{sid}: invalid effective_status={status!r}")

        for field in ("translation_to_p_t", "translation_to_p_b"):
            val = str(entry.get(field, "")).strip()
            if not val:
                errors.append(f"{sid}: empty {field}")
            if val.lower() in {"todo", "tbd", "pending", "unknown"}:
                errors.append(f"{sid}: non-actionable {field}={val!r}")

        if status == "effective":
            # Effective sources must not describe their core constants as pending.
            joined = " ".join(str(entry.get(k, "")) for k in ("constants_or_thresholds", "notes", "audit_rule_status"))
            lowered = joined.lower()
            bad_markers = ["pending_extraction", "non-effective", "non_effective", "not extracted"]
            if any(marker in lowered for marker in bad_markers):
                errors.append(
                    f"{sid}: effective_status='effective' but constants/notes contain pending/non-effective markers"
                )

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    by_status: Dict[str, int] = {k: 0 for k in sorted(VALID_EFFECTIVE_STATUS)}
    for entry in entries:
        by_status[str(entry["effective_status"])] += 1

    print(f"source_theorems_schema_ok entries={len(entries)}")
    for status, count in sorted(by_status.items()):
        print(f"  {status}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
