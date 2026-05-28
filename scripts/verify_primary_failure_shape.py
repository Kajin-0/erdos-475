#!/usr/bin/env python3
"""
Verify the corrected primary-failure shape for equality fallback rows.

Input is produced by scripts/taxonomize_fallback_local_intervals.py:

    logs/fallback_local_interval_taxonomy.jsonl

For every primary-failure row, this script checks that every primary-new
shortest block has zone class P+q, i.e. symbolic form P_suffix + q.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

TARGET_ZONE = "P+q"


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


def analyze(row: dict[str, Any]) -> dict[str, Any]:
    blocks = row.get("primary_new_short_blocks", []) or []
    zones = [b.get("zone_class") for b in blocks]
    symbols = [b.get("symbolic_block") for b in blocks]
    only_pq = bool(blocks) and all(z == TARGET_ZONE for z in zones)
    return {
        "p": row.get("p"),
        "record_index": row.get("record_index"),
        "family": row.get("family"),
        "reduced_equation": row.get("reduced_equation"),
        "primary_new_short_count": len(blocks),
        "primary_new_short_zone_classes": zones,
        "primary_new_short_symbols": symbols,
        "only_Pq_new_short": only_pq,
        "primary_new_short_blocks": blocks,
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    zone_hist = Counter()
    symbol_hist = Counter()
    for r in rows:
        zone_hist.update(r.get("primary_new_short_zone_classes", []))
        symbol_hist.update(r.get("primary_new_short_symbols", []))
    failures = [r for r in rows if not r.get("only_Pq_new_short")]
    return {
        "primary_failure_rows": len(rows),
        "rows_with_only_Pq_new_short": sum(1 for r in rows if r.get("only_Pq_new_short")),
        "rows_with_non_Pq_new_short": len(failures),
        "failure_indices": [r.get("record_index") for r in failures],
        "zone_class_histogram": dict(zone_hist.most_common()),
        "symbolic_block_histogram": dict(symbol_hist.most_common()),
        "record_indices": [r.get("record_index") for r in rows],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input fallback local interval taxonomy JSONL files")
    ap.add_argument("--out", default="-")
    ap.add_argument("--summary-out", default=None)
    args = ap.parse_args()

    rows = []
    for name in args.jsonl:
        for row in iter_jsonl(Path(name)):
            rows.append(analyze(row))

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
