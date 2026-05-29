#!/usr/bin/env python3
"""
Print compact diagnostics for rows where test_hidden_support_bridge_moves.py says
hidden_equation.holds == false.

Input is produced by:

    scripts/test_hidden_support_bridge_moves.py

Typical use:

    python3 scripts/diagnose_hidden_equation_false_rows.py \
      logs/hidden_support_bridge_moves_p17_v2.jsonl \
      logs/hidden_support_bridge_moves_p23_v2.jsonl \
      --out logs/hidden_equation_false_rows.jsonl \
      --summary-out logs/summary_hidden_equation_false_rows.json

This is intended to distinguish:

    1. stale equation JSONL files generated before the extractor patch;
    2. bad reduced_equation token evaluation;
    3. an extractor reduction rule that is algebraically too aggressive.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


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


def compact(row: dict[str, Any], source: str) -> dict[str, Any]:
    he = row.get("hidden_equation", {}) or {}
    return {
        "source": source,
        "p": row.get("p"),
        "record_index": row.get("record_index"),
        "support_length": row.get("support_length"),
        "reduced_family": row.get("reduced_family"),
        "extraction_kind": row.get("extraction_kind"),
        "hidden_equation": he,
        "best_class": row.get("best_class"),
        "result_counts": row.get("result_counts"),
        "terminal_progress_counts": row.get("terminal_progress_counts"),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Bridge-move JSONL files from test_hidden_support_bridge_moves.py")
    ap.add_argument("--out", default="-", help="Output JSONL path, or '-' for stdout")
    ap.add_argument("--summary-out", default=None, help="Optional summary JSON path")
    args = ap.parse_args()

    rows: list[dict[str, Any]] = []
    total = 0
    for name in args.jsonl:
        for row in iter_jsonl(Path(name)):
            total += 1
            he = row.get("hidden_equation", {}) or {}
            if he.get("holds") is False:
                rows.append(compact(row, Path(name).name))

    fam = Counter(str(r.get("reduced_family")) for r in rows)
    pcounts = Counter(str(r.get("p")) for r in rows)
    source_counts = Counter(r.get("source") for r in rows)
    zero_sums = Counter(str((r.get("hidden_equation") or {}).get("zero_block_sum")) for r in rows)
    red_eq = Counter(str((r.get("hidden_equation") or {}).get("reduced_equation")) for r in rows)

    if args.out == "-":
        for r in rows:
            print(json.dumps(r, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, separators=(",", ":")) + "\n")

    summary = {
        "input_rows": total,
        "false_rows": len(rows),
        "false_by_p": dict(pcounts.most_common()),
        "false_by_source": dict(source_counts.most_common()),
        "false_by_reduced_family": dict(fam.most_common()),
        "zero_block_sum_histogram": dict(zero_sums.most_common()),
        "top_reduced_equations": dict(red_eq.most_common(25)),
    }
    print("summary=" + json.dumps(summary, sort_keys=True))
    if args.summary_out:
        Path(args.summary_out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
