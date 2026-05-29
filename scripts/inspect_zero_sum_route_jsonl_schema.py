#!/usr/bin/env python3
"""
Inspect schema of detailed zero-sum route JSONL files.

This is used when extract_zero_sum_route_examples.py picks up an incorrect
label field, e.g. "worse" instead of true route labels like CLEAN_DESCENT.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

LIKELY_KEYS = [
    "class",
    "route_label",
    "route_class",
    "label",
    "result_class",
    "best_class",
    "best_route_label",
    "result_counts",
    "route_label_counts",
    "route_class_counts",
    "attempt_label_counts",
    "attempt_flag_counts",
    "move_class_counts",
    "candidate_best_counts",
    "results",
    "routes",
    "attempts",
    "witnesses",
    "route_witness",
]


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


def typ(v: Any) -> str:
    if isinstance(v, dict):
        return "dict"
    if isinstance(v, list):
        return "list"
    if isinstance(v, str):
        return "str"
    if isinstance(v, bool):
        return "bool"
    if isinstance(v, int):
        return "int"
    if isinstance(v, float):
        return "float"
    if v is None:
        return "null"
    return type(v).__name__


def compact(v: Any, limit: int = 240) -> str:
    s = json.dumps(v, sort_keys=True) if isinstance(v, (dict, list)) else str(v)
    return s if len(s) <= limit else s[:limit] + "..."


def nested_key_sample(v: Any) -> dict[str, Any]:
    if isinstance(v, dict):
        return {"type": "dict", "keys": sorted(list(v.keys()))[:30]}
    if isinstance(v, list):
        sample = next((x for x in v if isinstance(x, dict)), None)
        if sample is not None:
            return {"type": "list[dict]", "len": len(v), "keys": sorted(list(sample.keys()))[:30], "sample": sample}
        return {"type": "list", "len": len(v), "sample": v[:5]}
    return {"type": typ(v), "sample": v}


def inspect_file(path: Path, max_rows: int, sample_rows: int) -> dict[str, Any]:
    top_keys = Counter()
    key_types: dict[str, Counter[str]] = defaultdict(Counter)
    likely_values: dict[str, Counter[str]] = defaultdict(Counter)
    nested_samples: dict[str, Any] = {}
    rows = []
    count = 0
    for row in iter_jsonl(path):
        count += 1
        if len(rows) < sample_rows:
            rows.append(row)
        for k, v in row.items():
            top_keys[k] += 1
            key_types[k][typ(v)] += 1
            if k in LIKELY_KEYS:
                if isinstance(v, str):
                    likely_values[k][v] += 1
                elif isinstance(v, dict):
                    for kk, vv in v.items():
                        likely_values[k][f"{kk}:{vv}"] += 1
                elif isinstance(v, list):
                    likely_values[k][f"list_len={len(v)}"] += 1
                if k not in nested_samples:
                    nested_samples[k] = nested_key_sample(v)
        if max_rows and count >= max_rows:
            break
    return {
        "path": str(path),
        "rows_inspected": count,
        "top_keys": dict(top_keys.most_common()),
        "key_types": {k: dict(v.most_common()) for k, v in sorted(key_types.items())},
        "likely_values": {k: dict(v.most_common(30)) for k, v in sorted(likely_values.items())},
        "nested_samples": nested_samples,
        "sample_rows": rows,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Route JSONL files to inspect")
    ap.add_argument("--max-rows", type=int, default=0, help="0 means all rows")
    ap.add_argument("--sample-rows", type=int, default=3)
    ap.add_argument("--out", default="-")
    args = ap.parse_args()

    reports = []
    for name in args.jsonl:
        p = Path(name)
        if not p.exists():
            reports.append({"path": name, "missing": True})
            continue
        reports.append(inspect_file(p, args.max_rows, args.sample_rows))

    result = {"files": reports}
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.out == "-":
        print(text)
    else:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
