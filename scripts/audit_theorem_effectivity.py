#!/usr/bin/env python3
"""Effectivity audit summary for source theorem ledger.

This script reports which theorem entries are proof-mode usable and why other
entries remain blocked. It does not prove theorem statements.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from reduction_residue_audit import load_source_theorems  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "path",
        nargs="?",
        default="docs/source_theorems.yaml",
        help="Path to source theorem ledger.",
    )
    args = ap.parse_args()

    entries = load_source_theorems(Path(args.path))
    if not entries:
        print(f"ERROR: no entries found in {args.path}", file=sys.stderr)
        return 1

    print("=== Source theorem effectivity audit ===")
    print(f"ledger={args.path}")
    print(f"entries={len(entries)}")
    print()

    proof_usable = []
    blocked = []
    for entry in entries:
        sid = entry.get("source_id", "<missing>")
        status = entry.get("effective_status", "<missing>")
        if status == "effective":
            proof_usable.append(entry)
        else:
            blocked.append(entry)
        print(f"{sid}: effective_status={status}")
        print(f"  theorem={entry.get('theorem_number', '?')}")
        print(f"  audit_rule_status={entry.get('audit_rule_status', '?')}")
        print(f"  constants_or_thresholds={entry.get('constants_or_thresholds', '?')}")
        print(f"  proof_mode_usable={'yes' if status == 'effective' else 'no'}")
        print()

    print("Summary")
    print("-------")
    print(f"proof_mode_usable={len(proof_usable)}")
    print(f"blocked_or_exploratory={len(blocked)}")
    if blocked:
        print("blocked_source_ids=" + ",".join(str(e.get("source_id")) for e in blocked))
    print()

    if blocked:
        print("VERDICT: bridge is not currently source-effective for all listed analytic rules")
    else:
        print("VERDICT: all listed theorem entries are proof-mode usable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
