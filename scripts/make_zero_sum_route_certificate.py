#!/usr/bin/env python3
"""
Build a focused route certificate table for the zero-sum hidden-support families:

    B_tail+q          -> Bq_zero
    B_tail+q+Y_prefix -> BqY_zero

This is a zero-sum-only companion to make_pure_worse_certificate_table_v4.py.
It consumes the same summary JSON files used by the v4 certificate table and
optionally emits a Markdown table plus JSON summary.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ZERO_SUM_FAMILIES = ["B_tail+q", "B_tail+q+Y_prefix"]
TARGET = {
    "B_tail+q": "Bq_zero",
    "B_tail+q+Y_prefix": "BqY_zero",
}


def load(path: str | None) -> dict[str, Any]:
    if not path:
        return {}
    p = Path(path)
    if not p.exists():
        return {"_missing": str(path)}
    return json.loads(p.read_text(encoding="utf-8"))


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


def target_coverage(p: str, fam: str, count: int, genuine: dict[str, Any], bqy_gap_p23: dict[str, Any]) -> str:
    target = TARGET[fam]
    if count == 0:
        return "-"
    # B_tail+q+Y_prefix in p=23 has a focused gap diagnostic in the existing sprint.
    if p == "23" and fam == "B_tail+q+Y_prefix" and bqy_gap_p23 and not bqy_gap_p23.get("_missing"):
        got = int(bqy_gap_p23.get("records_with_target_class", 0) or 0)
        total = int(bqy_gap_p23.get("target_records", count) or count)
        return f"{got}/{total}"
    got = nested_count(genuine, "genuine_record_coverage_by_class", fam, target)
    return f"{got}/{count}"


def route_coverage(fam: str, count: int, route: dict[str, Any]) -> str:
    got = nested_count(route, "route_success_by_family", fam, "yes")
    return f"{got}/{count}"


def dominant_route_labels(route: dict[str, Any], fam: str) -> str:
    """Return any available route-label/class histogram for a family.

    The exact route summary format has evolved, so this intentionally checks a
    few likely keys and degrades to '-'.
    """
    candidates = [
        "route_label_by_family",
        "route_labels_by_family",
        "route_class_by_family",
        "route_classes_by_family",
        "route_success_label_by_family",
        "route_success_classes_by_family",
    ]
    for key in candidates:
        obj = ((route.get(key, {}) or {}).get(fam, {}) or {})
        if obj:
            return ", ".join(f"{k}:{v}" for k, v in obj.items())
    return "-"


def status_for(target_cov: str, route_cov: str) -> str:
    try:
        a, b = target_cov.split("/")
        c, d = route_cov.split("/")
    except ValueError:
        return "unknown"
    if a == b and c == d:
        return "zero_sum_routed"
    if a == b:
        return "target_classified_route_gap"
    return "target_coverage_gap"


def build_rows(p: str, extract: dict[str, Any], bridge: dict[str, Any], genuine: dict[str, Any], route: dict[str, Any], bqy_gap_p23: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for fam in ZERO_SUM_FAMILIES:
        count = family_count(extract, fam)
        if count == 0:
            continue
        t_cov = target_coverage(p, fam, count, genuine, bqy_gap_p23)
        r_cov = route_coverage(fam, count, route)
        rows.append({
            "p": p,
            "family": fam,
            "target": TARGET[fam],
            "records": count,
            "verified_total": verified_total(bridge),
            "best_bridge_class": best_bridge_class(bridge, fam),
            "target_coverage": t_cov,
            "route_coverage": r_cov,
            "dominant_route_labels": dominant_route_labels(route, fam),
            "status": status_for(t_cov, r_cov),
        })
    return rows


def markdown_table(rows: list[dict[str, Any]]) -> str:
    headers = [
        "p",
        "family",
        "target",
        "records",
        "verified_total",
        "best_bridge_class",
        "target_coverage",
        "route_coverage",
        "dominant_route_labels",
        "status",
    ]
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        out.append("| " + " | ".join(str(r.get(h, "")) for h in headers) + " |")
    return "\n".join(out)


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    total_records = sum(int(r.get("records", 0) or 0) for r in rows)
    routed = 0
    target_classified = 0
    for r in rows:
        tc = str(r.get("target_coverage", "0/0"))
        rc = str(r.get("route_coverage", "0/0"))
        try:
            a, _b = tc.split("/")
            c, _d = rc.split("/")
            target_classified += int(a)
            routed += int(c)
        except Exception:
            pass
    return {
        "zero_sum_rows": len(rows),
        "zero_sum_records": total_records,
        "target_classified_records": target_classified,
        "routed_records": routed,
        "all_rows_routed": all(r.get("status") == "zero_sum_routed" for r in rows),
    }


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
    gap23 = load(args.bqy_gap_p23)

    rows = []
    rows.extend(build_rows("17", extract17, bridge17, genuine17, route17, gap23))
    rows.extend(build_rows("23", extract23, bridge23, genuine23, route23, gap23))

    md = markdown_table(rows)
    summary = {
        "rows": rows,
        "aggregate": aggregate(rows),
        "interpretation": "zero-sum hidden-support families Bq_zero and BqY_zero are routed when target_coverage and route_coverage are complete",
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
