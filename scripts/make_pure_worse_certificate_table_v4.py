#!/usr/bin/env python3
"""
Generate final v4 certificate table for the pure worse-only branch.

v4 extends v3 by adding equality tie-break coverage from:

    logs/summary_equality_tie_break_ranks_p17.json
    logs/summary_equality_tie_break_ranks_p23.json

Final status meanings:

    zero_sum_routed       -> target obstruction classified and routed
    equality_tiebroken    -> D_short-neutral but q_tail_span_gap decreases
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
    "B_tail+q=A_complement": "q_tail_span_gap",
    "B_prefix=q": "q_tail_span_gap",
}


def load(path: str | None) -> dict[str, Any]:
    if not path:
        return {}
    return json.loads(Path(path).read_text(encoding="utf-8"))


def hist_count(d: dict[str, Any], hist: str, key: str) -> int:
    return int(((d.get(hist, {}) or {}).get(key, 0)) or 0)


def nested_count(d: dict[str, Any], outer: str, fam: str, key: str) -> int:
    return int(((((d.get(outer, {}) or {}).get(fam, {}) or {}).get(key, 0)) or 0))


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


def target_coverage(p: str, fam: str, count: int, genuine: dict[str, Any], bqy_gap_p23: dict[str, Any], tie: dict[str, Any]) -> str:
    if count == 0:
        return "-"
    target = TARGET[fam]
    if target == "q_tail_span_gap":
        got = nested_count(tie, "improve_key_coverage_by_family", fam, "q_tail_span_gap")
        return f"{got}/{count}"
    if p == "23" and fam == "B_tail+q+Y_prefix" and bqy_gap_p23:
        got = int(bqy_gap_p23.get("records_with_target_class", 0) or 0)
        total = int(bqy_gap_p23.get("target_records", count) or count)
        return f"{got}/{total}"
    cov = nested_count(genuine, "genuine_record_coverage_by_class", fam, target)
    return f"{cov}/{count}"


def route_coverage(fam: str, count: int, route: dict[str, Any]) -> str:
    if TARGET[fam] == "q_tail_span_gap":
        return "not_applicable"
    got = nested_count(route, "route_success_by_family", fam, "yes")
    return f"{got}/{count}"


def status_for(fam: str, target_cov: str, route_cov: str) -> str:
    target = TARGET[fam]
    if target == "q_tail_span_gap":
        a, b = target_cov.split("/")
        return "equality_tiebroken" if a == b else "equality_tie_break_gap"
    a, b = target_cov.split("/")
    c, d = route_cov.split("/")
    if a == b and c == d:
        return "zero_sum_routed"
    if a == b:
        return "target_classified_route_gap"
    return "target_coverage_gap"


def build_rows(p: str, extract: dict[str, Any], bridge: dict[str, Any], genuine: dict[str, Any], route: dict[str, Any], tie: dict[str, Any], bqy_gap_p23: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for fam in FAMILIES:
        count = family_count(extract, fam)
        if count == 0:
            continue
        target_cov = target_coverage(p, fam, count, genuine, bqy_gap_p23, tie)
        route_cov = route_coverage(fam, count, route)
        target = TARGET[fam]
        rows.append(
            {
                "p": p,
                "family": fam,
                "records": count,
                "mode": "equality" if target == "q_tail_span_gap" else "zero_sum",
                "verified_total": verified_total(bridge),
                "best_bridge_class": best_bridge_class(bridge, fam),
                "target": target,
                "target_coverage": target_cov,
                "route_coverage": route_cov,
                "status": status_for(fam, target_cov, route_cov),
            }
        )
    return rows


def markdown_table(rows: list[dict[str, Any]]) -> str:
    headers = [
        "p",
        "family",
        "records",
        "mode",
        "verified_total",
        "best_bridge_class",
        "target",
        "target_coverage",
        "route_coverage",
        "status",
    ]
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
    ap.add_argument("--route-p17", required=True)
    ap.add_argument("--route-p23", required=True)
    ap.add_argument("--tie-p17", required=True)
    ap.add_argument("--tie-p23", required=True)
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
    route17 = load(args.route_p17)
    route23 = load(args.route_p23)
    tie17 = load(args.tie_p17)
    tie23 = load(args.tie_p23)
    gap23 = load(args.bqy_gap_p23)

    rows = []
    rows.extend(build_rows("17", extract17, bridge17, genuine17, route17, tie17, gap23))
    rows.extend(build_rows("23", extract23, bridge23, genuine23, route23, tie23, gap23))

    md = markdown_table(rows)
    summary = {
        "rows": rows,
        "interpretation": "zero_sum rows are routed; equality rows are D_short-neutral but q_tail_span_gap decreasing",
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
