#!/usr/bin/env python3
"""
Print a compact coverage table from summary_pure_worse_nontautological_core_*.json.

This avoids huge terminal output from jq when examples/top signatures are large.

Usage:

    python3 scripts/print_pure_worse_nontaut_coverage.py \
      logs/summary_pure_worse_nontautological_core_p17.json \
      logs/summary_pure_worse_nontautological_core_p23.json

Output columns:

    file, pure_worse_records, perm, records, records_with_nont, all_have_nont, coverage
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("summary_json", nargs="+", help="Summary JSON files from summarize_pure_worse_nontautological_core.py")
    ap.add_argument("--tsv", action="store_true", help="Emit TSV instead of aligned text")
    args = ap.parse_args()

    rows: list[tuple[str, int, str, int, int, bool, float]] = []
    for name in args.summary_json:
        path = Path(name)
        data = load(path)
        total = int(data.get("pure_worse_records", 0))
        coverage = data.get("separated_perm_nontautological_record_coverage", {})
        for perm, rec in sorted(coverage.items()):
            records = int(rec.get("records", 0))
            with_nont = int(rec.get("records_with_nont", 0))
            all_have = bool(rec.get("all_have_nont", False))
            frac = (with_nont / records) if records else 0.0
            rows.append((path.name, total, perm, records, with_nont, all_have, frac))

    if args.tsv:
        print("file\tpure_worse_records\tperm\trecords\trecords_with_nont\tall_have_nont\tcoverage")
        for row in rows:
            print("\t".join([str(row[0]), str(row[1]), row[2], str(row[3]), str(row[4]), str(row[5]).lower(), f"{row[6]:.6f}"]))
        return 0

    header = f"{'file':52} {'N':>4} {'perm':11} {'hit':>5} {'tot':>5} {'all':>5} {'coverage':>9}"
    print(header)
    print("-" * len(header))
    for file_name, total, perm, records, with_nont, all_have, frac in rows:
        print(f"{file_name:52} {total:4d} {perm:11} {with_nont:5d} {records:5d} {str(all_have):>5} {frac:9.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
