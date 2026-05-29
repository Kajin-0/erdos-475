#!/usr/bin/env python3
"""
Inspect shortest-block accounting for equality fallback rows.

Input is produced by scripts/diagnose_three_localization_worse_conditions.py:

    logs/three_localization_worse_conditions_p17.jsonl
    logs/three_localization_worse_conditions_p23.jsonl

The script filters rows where the primary localization P_q_T_M is worse and
compares old, primary, and fallback q_T_P_M shortest zero blocks.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

PRIMARY = "P_q_T_M"
FALLBACK = "q_T_P_M"


def iter_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSON in {path}:{line_no}: {exc}") from exc


def cand(row: dict[str, Any], name: str) -> dict[str, Any]:
    for c in row.get("candidates", []) or []:
        if c.get("name") == name:
            return c
    return {}


def block_symbols(blocks: list[dict[str, Any]]) -> list[str]:
    return [str(b.get("symbolic_block")) for b in blocks]


def inspect(row: dict[str, Any]) -> dict[str, Any] | None:
    primary = cand(row, PRIMARY)
    if primary.get("class_vs_old") != "worse":
        return None
    fallback = cand(row, FALLBACK)
    old_short = row.get("old_shortest_blocks_first10", []) or []
    primary_new = primary.get("new_short_blocks_first10", []) or []
    fallback_new = fallback.get("new_short_blocks_first10", []) or []
    return {
        "p": row.get("p"),
        "record_index": row.get("record_index"),
        "family": row.get("family"),
        "reduced_equation": row.get("reduced_equation"),
        "old_defect": row.get("old_defect"),
        "old_active_symbolic": row.get("old_active_symbolic"),
        "old_shortest_blocks": old_short,
        "primary_name": PRIMARY,
        "primary_class": primary.get("class_vs_old"),
        "primary_defect": primary.get("defect"),
        "primary_active_symbolic": primary.get("active_symbolic"),
        "primary_new_short_blocks": primary_new,
        "fallback_name": FALLBACK,
        "fallback_class": fallback.get("class_vs_old"),
        "fallback_defect": fallback.get("defect"),
        "fallback_active_symbolic": fallback.get("active_symbolic"),
        "fallback_new_short_blocks": fallback_new,
        "fallback_new_short_symbols": block_symbols(fallback_new),
        "fallback_has_new_short_blocks": bool(fallback_new),
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_family: dict[str, Counter[str]] = defaultdict(Counter)
    fallback_new_symbols = Counter()
    primary_new_symbols = Counter()
    for r in rows:
        fam = str(r.get("family"))
        by_family[fam]["primary_failure_rows"] += 1
        by_family[fam][f"fallback_{r.get('fallback_class')}"] += 1
        by_family[fam]["fallback_has_new_short" if r.get("fallback_has_new_short_blocks") else "fallback_no_new_short"] += 1
        for b in r.get("fallback_new_short_blocks", []) or []:
            fallback_new_symbols[str(b.get("symbolic_block"))] += 1
        for b in r.get("primary_new_short_blocks", []) or []:
            primary_new_symbols[str(b.get("symbolic_block"))] += 1
    return {
        "primary_failure_rows": len(rows),
        "fallback_class_counts": dict(Counter(r.get("fallback_class") for r in rows).most_common()),
        "fallback_new_short_presence": dict(Counter("yes" if r.get("fallback_has_new_short_blocks") else "no" for r in rows).most_common()),
        "by_family": {k: dict(v) for k, v in by_family.items()},
        "primary_new_short_symbols": dict(primary_new_symbols.most_common()),
        "fallback_new_short_symbols": dict(fallback_new_symbols.most_common()),
        "record_indices": [r.get("record_index") for r in rows],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input worse-condition JSONL files")
    ap.add_argument("--out", default="-")
    ap.add_argument("--summary-out", default=None)
    args = ap.parse_args()

    rows = []
    for name in args.jsonl:
        for row in iter_jsonl(Path(name)):
            out = inspect(row)
            if out is not None:
                rows.append(out)

    if args.out == "-":
        for r in rows:
            print(json.dumps(r, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, separators=(",", ":")) + "\n")

    summary = summarize(rows)
    print("summary=" + json.dumps(summary, sort_keys=True))
    if args.summary_out:
        Path(args.summary_out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
