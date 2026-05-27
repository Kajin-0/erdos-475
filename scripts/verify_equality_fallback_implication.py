#!/usr/bin/env python3
"""
Verify the equality fallback implication:

    P_q_T_M worse -> q_T_P_M neutral with q_tail_span_gap = 0.

Input is produced by scripts/test_equality_three_localizations.py:

    logs/equality_three_localizations_p17.jsonl
    logs/equality_three_localizations_p23.jsonl

Typical use:

    python3 scripts/verify_equality_fallback_implication.py \
      logs/equality_three_localizations_p17.jsonl \
      --out logs/equality_fallback_implication_p17.jsonl \
      --summary-out logs/summary_equality_fallback_implication_p17.json
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


def candidate_map(row: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {c.get("name"): c for c in row.get("candidates", [])}


def analyze(row: dict[str, Any]) -> dict[str, Any]:
    cmap = candidate_map(row)
    primary = cmap.get(PRIMARY, {})
    fallback = cmap.get(FALLBACK, {})
    primary_worse = primary.get("class_vs_old") == "worse"
    fallback_ok = fallback.get("class_vs_old") == "neutral" and fallback.get("q_tail_span_gap") == 0
    implication_holds = (not primary_worse) or fallback_ok
    return {
        "p": row.get("p"),
        "record_index": row.get("record_index"),
        "family": row.get("family"),
        "reduced_equation": row.get("reduced_equation"),
        "primary_class": primary.get("class_vs_old"),
        "primary_gap": primary.get("q_tail_span_gap"),
        "fallback_class": fallback.get("class_vs_old"),
        "fallback_gap": fallback.get("q_tail_span_gap"),
        "primary_worse": primary_worse,
        "fallback_ok": fallback_ok,
        "implication_holds": implication_holds,
        "primary_active_symbolic": primary.get("active_symbolic"),
        "fallback_active_symbolic": fallback.get("active_symbolic"),
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    primary_worse_rows = [r for r in rows if r["primary_worse"]]
    failures = [r for r in rows if not r["implication_holds"]]
    by_family: dict[str, Counter[str]] = defaultdict(Counter)
    for r in rows:
        fam = r.get("family")
        by_family[fam]["records"] += 1
        if r["primary_worse"]:
            by_family[fam]["primary_worse"] += 1
        if r["primary_worse"] and r["fallback_ok"]:
            by_family[fam]["fallback_rescues"] += 1
        if not r["implication_holds"]:
            by_family[fam]["failures"] += 1
    return {
        "records": len(rows),
        "primary": PRIMARY,
        "fallback": FALLBACK,
        "primary_worse_records": len(primary_worse_rows),
        "implication_holds_on_primary_worse": sum(1 for r in primary_worse_rows if r["implication_holds"]),
        "implication_failures": len(failures),
        "failure_indices": [r["record_index"] for r in failures],
        "by_family": {k: dict(v) for k, v in by_family.items()},
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input equality_three_localizations JSONL files")
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
