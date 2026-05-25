#!/usr/bin/env python3
"""
Generate a compact certificate table for the pure worse-only branch.

Inputs are summary JSON files already generated in the analytic sprint:

    --extract-p17 logs/summary_bzqa_hidden_support_equations_p17_v3.json
    --extract-p23 logs/summary_bzqa_hidden_support_equations_p23_v3.json
    --bridge-p17  logs/summary_hidden_support_bridge_moves_p17_v5.json
    --bridge-p23  logs/summary_hidden_support_bridge_moves_p23_v5.json
    --genuine-p17 logs/summary_hidden_bridge_genuine_obstructions_p17.json
    --genuine-p23 logs/summary_hidden_bridge_genuine_obstructions_p23.json
    --bqy-gap-p23 logs/summary_gaps_Btail_q_Yprefix_missing_BqY_p23.json

Output is a compact Markdown table plus a JSON summary.
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


def load(path: str | None) -> dict[str, Any]:
    if not path:
        return {}
    return json.loads(Path(path).read_text(encoding="utf-8"))


def get_count(d: dict[str, Any], key: str, sub: str | None = None) -> int:
    obj = d.get(key, {}) or {}
    if sub is None:
        return int(obj) if isinstance(obj, int) else 0
    return int((obj.get(sub, 0) if isinstance(obj, dict) else 0) or 0)


def family_count_extract(extract: dict[str, Any], fam: str) -> int:
    return get_count(extract, "reduced_family_histogram", fam)


def verification_count(bridge: dict[str, Any]) -> int:
    return get_count(bridge, "hidden_equation_holds", "True")


def best_class(bridge: dict[str, Any], fam: str) -> str:
    obj = ((bridge.get("best_class_by_family", {}) or {}).get(fam, {}) or {})
    if not obj:
        return "-"
    return ", ".join(f"{k}:{v}" for k, v in obj.items())


def genuine_class(genuine: dict[str, Any], fam: str) -> str:
    obj = ((genuine.get("genuine_record_coverage_by_class", {}) or {}).get(fam, {}) or {})
    if not obj:
        return "-"
    return ", ".join(f"{k}:{v}" for k, v in obj.items())


def has_genuine(genuine: dict[str, Any], fam: str) -> str:
    obj = ((genuine.get("record_has_genuine_by_family", {}) or {}).get(fam, {}) or {})
    if not obj:
        return "-"
    return ", ".join(f"{k}:{v}" for k, v in obj.items())


def mode_for_family(bridge: dict[str, Any], fam: str) -> str:
    if fam in {"B_tail+q", "B_tail+q+Y_prefix"}:
        return "zero_sum"
    if fam in {"B_tail+q=A_complement", "B_prefix=q"}:
        return "equality"
    return "unknown"


def build_rows(p: str, extract: dict[str, Any], bridge: dict[str, Any], genuine: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    verified = verification_count(bridge)
    total = int(bridge.get("records", 0) or extract.get("input_records", 0) or 0)
    for fam in FAMILIES:
        count = family_count_extract(extract, fam)
        if count == 0:
            continue
        rows.append(
            {
                "p": p,
                "family": fam,
                "records": count,
                "mode": mode_for_family(bridge, fam),
                "verified_total": f"{verified}/{total}",
                "best_bridge_class": best_class(bridge, fam),
                "has_genuine": has_genuine(genuine, fam),
                "genuine_record_classes": genuine_class(genuine, fam),
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
        "has_genuine",
        "genuine_record_classes",
    ]
    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join("---" for _ in headers) + " |")
    for r in rows:
        lines.append("| " + " | ".join(str(r.get(h, "")) for h in headers) + " |")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--extract-p17", required=True)
    ap.add_argument("--extract-p23", required=True)
    ap.add_argument("--bridge-p17", required=True)
    ap.add_argument("--bridge-p23", required=True)
    ap.add_argument("--genuine-p17", required=True)
    ap.add_argument("--genuine-p23", required=True)
    ap.add_argument("--bqy-gap-p23", default=None)
    ap.add_argument("--out-md", default="-")
    ap.add_argument("--out-json", default=None)
    args = ap.parse_args()

    extract17 = load(args.extract_p17)
    extract23 = load(args.extract_p23)
    bridge17 = load(args.bridge_p17)
    bridge23 = load(args.bridge_p23)
    genuine17 = load(args.genuine_p17)
    genuine23 = load(args.genuine_p23)
    bqy_gap23 = load(args.bqy_gap_p23)

    rows = []
    rows.extend(build_rows("17", extract17, bridge17, genuine17))
    rows.extend(build_rows("23", extract23, bridge23, genuine23))

    summary = {
        "rows": rows,
        "notes": {
            "p23_B_tail+q+Y_prefix_BqY_gap": bqy_gap23,
            "interpretation": "zero_sum families have universal genuine Bq/BqY obstruction; equality families are neutral and require tie-break refinement",
        },
    }

    md = markdown_table(rows)
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
