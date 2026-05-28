#!/usr/bin/env python3
"""
Build a compact proof-facing witness table from zero_sum_route_examples.jsonl.

Input is produced by scripts/extract_zero_sum_route_examples.py.
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


def compact(value: Any, limit: int = 160) -> str:
    if value is None:
        return "-"
    if isinstance(value, (dict, list)):
        text = json.dumps(value, sort_keys=True, separators=(",", ":"))
    else:
        text = str(value)
    text = text.replace("\n", " ")
    if len(text) > limit:
        return text[: max(0, limit - 3)] + "..."
    return text or "-"


def move_route_summary(move_routes: Any, route_label: str, limit: int = 220) -> str:
    if not move_routes:
        return "-"
    matches = []
    if isinstance(move_routes, list):
        for item in move_routes:
            if not isinstance(item, dict):
                continue
            labels = item.get("labels") or item.get("route_labels") or item.get("label") or item.get("route_label")
            if isinstance(labels, list) and route_label in labels:
                matches.append(item)
            elif isinstance(labels, str) and labels == route_label:
                matches.append(item)
            elif route_label in json.dumps(item, sort_keys=True):
                matches.append(item)
    elif isinstance(move_routes, dict):
        for key, val in move_routes.items():
            if key == route_label or route_label in json.dumps(val, sort_keys=True):
                matches.append({key: val})
    if not matches:
        return compact(move_routes, limit)
    return compact(matches[:2], limit)


def useful_flags_for_label(example: dict[str, Any]) -> str:
    witness = example.get("witness", {}) or {}
    label = example.get("route_label")
    flags = witness.get("useful_route_flags")
    if isinstance(flags, dict):
        val = flags.get(label)
        if val is not None:
            return compact(val, 140)
    if isinstance(flags, list):
        vals = [x for x in flags if label in compact(x, 1000)]
        if vals:
            return compact(vals[:3], 140)
    return compact(flags, 140)


def route_flag_counts_for_label(example: dict[str, Any]) -> str:
    witness = example.get("witness", {}) or {}
    label = example.get("route_label")
    counts = witness.get("route_flag_counts")
    if isinstance(counts, dict):
        if label in counts:
            return compact({label: counts[label]}, 100)
        return compact(counts, 140)
    return compact(counts, 140)


def normalize_row(example: dict[str, Any]) -> dict[str, Any]:
    witness = example.get("witness", {}) or {}
    return {
        "family": example.get("family", "-"),
        "target": example.get("target", "-"),
        "route_label": example.get("route_label", "-"),
        "p": example.get("p", "-"),
        "record_index": example.get("record_index", "-"),
        "reduced_equation": example.get("reduced_equation", "-"),
        "active_symbolic_order": example.get("active_symbolic_order", "-"),
        "hidden_equation": compact(witness.get("hidden_equation"), 140),
        "useful_route_flags": useful_flags_for_label(example),
        "route_flag_counts": route_flag_counts_for_label(example),
        "route_label_count": example.get("route_label_count", "-"),
        "representative_move_routes": move_route_summary(witness.get("move_routes"), str(example.get("route_label", ""))),
    }


def markdown_table(rows: list[dict[str, Any]]) -> str:
    headers = [
        "family",
        "target",
        "route_label",
        "p",
        "record_index",
        "reduced_equation",
        "active_symbolic_order",
        "hidden_equation",
        "useful_route_flags",
        "route_flag_counts",
        "route_label_count",
        "representative_move_routes",
    ]
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        out.append("| " + " | ".join(compact(r.get(h), 180).replace("|", "\\|") for h in headers) + " |")
    return "\n".join(out)


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "rows": len(rows),
        "by_family": dict(Counter(r["family"] for r in rows).most_common()),
        "by_route_label": dict(Counter(r["route_label"] for r in rows).most_common()),
        "by_family_route": dict(Counter(f"{r['family']}::{r['route_label']}" for r in rows).most_common()),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input_jsonl")
    ap.add_argument("--out-md", default="-")
    ap.add_argument("--out-json", default=None)
    args = ap.parse_args()

    rows = [normalize_row(r) for r in iter_jsonl(Path(args.input_jsonl))]
    rows.sort(key=lambda r: (str(r["family"]), str(r["route_label"]), int(r["p"]), int(r["record_index"])))
    md = markdown_table(rows)
    payload = {"summary": summarize(rows), "rows": rows}

    if args.out_md == "-":
        print(md)
    else:
        Path(args.out_md).write_text(md + "\n", encoding="utf-8")
        print(f"wrote {args.out_md}")
    if args.out_json:
        Path(args.out_json).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.out_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
