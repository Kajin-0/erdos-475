#!/usr/bin/env python3
"""
Generate a proof-focused v2 certificate table for the pure worse-only branch.

Compared with make_pure_worse_certificate_table.py, this script suppresses noisy
secondary-class lists and reports only the proof-relevant target coverage:

    B_tail+q              -> Bq_zero
    B_tail+q+Y_prefix     -> BqY_zero
    B_tail+q=A_complement -> equality_tie_break
    B_prefix=q            -> equality_tie_break

The p=23 BqY coverage is read from the direct gap diagnostic so it is recorded
as 32/32 rather than the restricted shortest-view count.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

FAMILIES = [
    "B_tail+q",
    "B_tail+q+Y_prefix",
    "B_tail+q=A_complement",
    "B_prefix=q",
]

TARGET = {
    "B_tail+q": "Bq_zero",
    "B_tail+q+Y_prefix": "BqY_zero",
    "B_tail+q=A_complement": "equality_tie_break",
    "B_prefix=q": "equality_tie_break",
}


def load(path: str | None) -> dict[str, Any]:
    if not path:
        return {}
    return json.loads(Path(path).read_text(encoding="utf-8"))


def hist_count(d: dict[str, Any], hist: str, key: str) -> int:
    return int(((d.get(hist, {}) or {}).get(key, 0)) or 0)


def family_count(extract: dict[str, Any], fam: str) -> int:
    return hist_count(extract, "reduced_family_histogram", fam)


def verified_total(bridge: dict[str, Any]) -> str:
    true_count = hist_count(bridge, "hidden_equation_holds", "True")
    total = int(bridge.get("records", 0) or 0)
    return f"{true_count}/{total}"


def best_bridge_class(bridge: dict[str, Any], fam: str) -> str:
    obj = ((bridge.get("best_class_by_family", {}) or {}).get(fam, {}) or {})
    if not obj:
        return "-"
    return ", ".join(f"{k}:{v}" for k, v in obj.items())


def target_coverage(p: str, fam: str, count: int, genuine: dict[str, Any], bqy_gap_p23: dict[str, Any]) -> str:
    if count == 0:
        return "-"
    target = TARGET[fam]
    if target == "equality_tie_break":
        return f"neutral {count}/{count}"
    if p == "23" and fam == "B_tail+q+Y_prefix" and bqy_gap_p23:
        got = int(bqy_gap_p23.get("records_with_target_class", 0) or 0)
        total = int(bqy_gap_p23.get("target_records", count) or count)
        return f"{got}/{total}"
    cov = (((genuine.get("genuine_record_coverage_by_class", {}) or {}).get(fam, {}) or {}).get(target, 0))
    return f"{int(cov)}/{count}"


def status_for(fam: str, count: int, coverage: str) -> str:
    if count == 0:
        return "absent"
    if TARGET[fam] == "equality_tie_break":
        return "tie_break_needed"
    lhs, rhs = coverage.split("/")
    return "zero_sum_classified" if lhs == rhs else "coverage_gap"


def build_rows(p: str, extract: dict[str, Any], bridge: dict[str, Any], genuine: dict[str, Any], bqy_gap_p23: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for fam in FAMILIES:
        count = family_count(extract, fam)
        if count == 0:
            continue
        cov = target_coverage(p, fam, count, genuine, bqy_gap_p23)
        rows.append(
            {
                "p": p,
                "family": fam,
                "records": count,
                "mode": "zero_sum" if TARGET[fam] != "equality_tie_break" else "equality",
                "verified_total": verified_total(bridge),
                "best_bridge_class": best_bridge_class(bridge, fam),
                "target_obstruction": TARGET[fam],
                "target_coverage": cov,
                "status": status_for(fam, count, cov),
            }
        )
    return rows


def markdown_table(rows: list[dict[str, Any]]) -> str:
    headers = ["p", "family", "records", "mode", "verified_total", "best_bridge_class", "target_obstruction", "target_coverage", "status"]
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        out.append("| " + " | ".join(str(r.get(h, "")) for h in headers) + " |")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--extract-p17", required=True)
    ap.add_argument("--extract-p23", required=True)
    ap.add_argument("--bridge-p17", required=True)
    ap.add_argument("--bridge-p23", required=True)
    ap.add_argument("--genuine-p17", required=True)
    ap.add_argument("--genuine-p23", required=True)
    ap.add_argument("--bqy-gap-p23", required=True)
    ap.add_argument("--out-md", default="-")
    ap.add_argument("--out-json", default=None)
    args = ap.parse_args()

    extract17 = load(args.extract_p17)
    extract23 = load(args.extract_p23)
    bridge17 = load(args.bridge_p17)
    bridge23 = load(args.bridge_p23)
    genuine17 = load(args.genuine_p17)
    genuine23 = load(args.genuine_p23)
    gap23 = load(args.bqy_gap_p23)

    rows = []
    rows.extend(build_rows("17", extract17, bridge17, genuine17, gap23))
    rows.extend(build_rows("23", extract23, bridge23, genuine23, gap23))

    md = markdown_table(rows)
    summary = {
        "rows": rows,
        "interpretation": "zero_sum rows are fully classified by target Bq/BqY obstructions; equality rows are isolated tie-break obligations",
    }

    if args.out_md == "-":
        print(md)
    else:
        Path(args.out_md).write_text(md + "\n", encoding="utf-8")
        print(f"wrote {args.out_md}")
    if args.out_json:
        Path(args.out_json).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.out_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
