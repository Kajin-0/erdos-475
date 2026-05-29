#!/usr/bin/env python3
"""
Route Bq/BqY secondary obstructions and preserve per-label attempt witnesses.

This is a witness-rich companion to scripts/route_bq_bqy_obstructions.py.  It
uses the same classifier functions, but stores representative attempts by route
label and by branch flag so downstream witness extraction is not limited by
attempts_first5/first10 truncation.

Typical use:

    python3 scripts/route_bq_bqy_obstructions_with_attempts.py \
      logs/hidden_support_bridge_moves_p23_v5.jsonl \
      --out logs/route_bq_bqy_obstructions_p23_with_attempts.jsonl \
      --summary-out logs/summary_route_bq_bqy_obstructions_p23_with_attempts.json
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "route_bq_bqy_obstructions.py"

spec = importlib.util.spec_from_file_location("route_bq_bqy_obstructions_base", BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not import base route script from {BASE_PATH}")
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)


def attempts_by_label(attempts: list[dict[str, Any]], max_per_label: int) -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for attempt in attempts:
        label = str(attempt.get("label", "UNKNOWN"))
        if len(out[label]) < max_per_label:
            out[label].append(attempt)
    return dict(out)


def attempts_by_flag(attempts: list[dict[str, Any]], max_per_flag: int) -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for attempt in attempts:
        for flag in attempt.get("branch_flags", []) or []:
            flag = str(flag)
            if len(out[flag]) < max_per_flag:
                out[flag].append(attempt)
    return dict(out)


def analyze_order_rich(p: int, order: list[int], max_intervals: int = 6, max_per_label: int = 3, max_per_flag: int = 3) -> dict[str, Any] | None:
    zis = base.zero_intervals(p, order)
    if not zis:
        return None
    L_min = min(length for _, _, length in zis)
    active_intervals = [(i, j, length) for i, j, length in zis if length == L_min]
    attempts: list[dict[str, Any]] = []
    for z_i, z_j, m in active_intervals[:max_intervals]:
        if m < 2:
            continue
        if z_j < len(order):
            attempts.extend(base.classify_right_insertion(p, order, z_i, z_j, k) for k in range(1, m))
        if z_i > 0:
            attempts.extend(base.classify_left_by_reversal(p, order, z_i, z_j, k) for k in range(1, m))
    if not attempts:
        return None
    return {
        "active_shortest_length": L_min,
        "attempt_label_counts": dict(Counter(a.get("label", "UNKNOWN") for a in attempts).most_common()),
        "attempt_flag_counts": dict(Counter(flag for a in attempts for flag in (a.get("branch_flags", []) or [])).most_common()),
        "attempts_first10": attempts[:10],
        "attempts_by_label": attempts_by_label(attempts, max_per_label=max_per_label),
        "attempts_by_flag": attempts_by_flag(attempts, max_per_flag=max_per_flag),
        "attempts_total": len(attempts),
    }


def best_moves(row: dict[str, Any]) -> list[dict[str, Any]]:
    return base.best_moves(row)


def route_record(row: dict[str, Any], max_per_label: int, max_per_flag: int) -> dict[str, Any]:
    p = int(row["p"])
    family = row.get("reduced_family")
    move_routes = []
    route_flags = Counter()
    route_labels = Counter()
    for move in best_moves(row):
        new_order = [int(x) for x in move.get("new_order", [])]
        if not new_order:
            continue
        routed = analyze_order_rich(p, new_order, max_per_label=max_per_label, max_per_flag=max_per_flag)
        if routed is None:
            move_routes.append({"move": move.get("move"), "bridge_class": move.get("class"), "routed": False})
            continue
        flags = routed.get("attempt_flag_counts", {})
        labels = routed.get("attempt_label_counts", {})
        route_flags.update(flags)
        route_labels.update(labels)
        move_routes.append(
            {
                "move": move.get("move"),
                "bridge_class": move.get("class"),
                "routed": True,
                "attempt_flag_counts": flags,
                "attempt_label_counts": labels,
                "active_shortest_length": routed.get("active_shortest_length"),
                "attempts_first10": routed.get("attempts_first10", []),
                "attempts_by_label": routed.get("attempts_by_label", {}),
                "attempts_by_flag": routed.get("attempts_by_flag", {}),
                "attempts_total": routed.get("attempts_total", 0),
            }
        )
    useful_flags = sorted(set(route_flags) & base.ROUTE_FLAGS)
    return {
        "p": p,
        "record_index": row.get("record_index"),
        "reduced_family": family,
        "hidden_equation": row.get("hidden_equation", {}).get("reduced_equation"),
        "best_class": row.get("best_class"),
        "route_success": bool(useful_flags),
        "useful_route_flags": useful_flags,
        "route_flag_counts": dict(route_flags.most_common()),
        "route_label_counts": dict(route_labels.most_common()),
        "move_routes": move_routes,
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return base.summarize(rows)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Bridge move JSONL files from test_hidden_support_bridge_moves.py")
    ap.add_argument("--out", default="-", help="Output JSONL path, or '-' for stdout")
    ap.add_argument("--summary-out", default=None, help="Optional summary JSON path")
    ap.add_argument("--max-per-label", type=int, default=3)
    ap.add_argument("--max-per-flag", type=int, default=3)
    args = ap.parse_args()

    rows = []
    for name in args.jsonl:
        for row in base.iter_jsonl(Path(name)):
            if row.get("reduced_family") not in base.TARGET_FAMILIES:
                continue
            rows.append(route_record(row, max_per_label=args.max_per_label, max_per_flag=args.max_per_flag))

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
