#!/usr/bin/env python3
"""
Extract attempt-level witnesses from zero_sum_route_examples.jsonl.

Input is produced by scripts/extract_zero_sum_route_examples.py and contains a
witness.move_routes field copied from detailed route JSONL rows.

The schema is intentionally handled flexibly because attempt payloads evolved
through the sprint.
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


def compact(value: Any, limit: int = 500) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        text = json.dumps(value, sort_keys=True, separators=(",", ":"))
    else:
        text = str(value)
    return text if len(text) <= limit else text[: max(0, limit - 3)] + "..."


def flatten_attempts(obj: Any) -> list[dict[str, Any]]:
    """Return plausible attempt dictionaries from a route/move object."""
    out: list[dict[str, Any]] = []
    if isinstance(obj, dict):
        # The object itself may be an attempt.
        if any(k in obj for k in ["branch_flags", "bridge_interval", "old_defect", "new_defect", "class", "route_label", "label"]):
            out.append(obj)
        for key in ["attempts", "attempts_first5", "routes", "results", "moves", "move_routes"]:
            val = obj.get(key)
            if isinstance(val, list):
                for item in val:
                    out.extend(flatten_attempts(item))
            elif isinstance(val, dict):
                out.extend(flatten_attempts(val))
    elif isinstance(obj, list):
        for item in obj:
            out.extend(flatten_attempts(item))
    return out


def route_objects(example: dict[str, Any]) -> list[Any]:
    witness = example.get("witness", {}) or {}
    mr = witness.get("move_routes")
    if isinstance(mr, list):
        return mr
    if isinstance(mr, dict):
        return [mr]
    return []


def object_mentions_label(obj: Any, label: str) -> bool:
    return label in compact(obj, 10000)


def select_route_object(example: dict[str, Any]) -> tuple[Any, bool]:
    label = str(example.get("route_label", ""))
    objs = route_objects(example)
    for obj in objs:
        if object_mentions_label(obj, label):
            return obj, True
    if objs:
        return objs[0], False
    return {}, False


def select_attempt(route_obj: Any, label: str) -> tuple[dict[str, Any], bool]:
    attempts = flatten_attempts(route_obj)
    for att in attempts:
        flags = att.get("branch_flags") or att.get("route_flags") or att.get("labels") or att.get("route_labels")
        if isinstance(flags, list) and label in flags:
            return att, True
        if isinstance(flags, str) and flags == label:
            return att, True
        if object_mentions_label(att, label):
            return att, True
    if attempts:
        return attempts[0], False
    return {}, False


def pick(obj: dict[str, Any], keys: list[str]) -> Any:
    for key in keys:
        if key in obj and obj[key] not in (None, ""):
            return obj[key]
    return None


def normalize(example: dict[str, Any]) -> dict[str, Any]:
    label = str(example.get("route_label", ""))
    route_obj, matched_route = select_route_object(example)
    attempt, matched_attempt = select_attempt(route_obj, label)
    witness = example.get("witness", {}) or {}

    branch_flags = pick(attempt, ["branch_flags", "route_flags", "labels", "route_labels"])
    bridge_interval = pick(attempt, ["bridge_interval", "interval", "zero_interval", "new_zero_interval"])
    bridge_sum = pick(attempt, ["bridge_sum", "sum", "interval_sum", "symbolic_sum", "partial_sum_equality"])
    symbolic_block = pick(attempt, ["symbolic_block", "block", "new_zero_block", "zero_block"])
    old_defect = pick(attempt, ["old_defect", "before_defect", "active_old_defect"])
    new_defect = pick(attempt, ["new_defect", "after_defect", "candidate_defect"])

    return {
        "family": example.get("family"),
        "target": example.get("target"),
        "route_label": label,
        "p": example.get("p"),
        "record_index": example.get("record_index"),
        "reduced_equation": example.get("reduced_equation"),
        "hidden_equation": witness.get("hidden_equation"),
        "active_symbolic_order": example.get("active_symbolic_order"),
        "route_label_count": example.get("route_label_count"),
        "matched_route_object": matched_route,
        "matched_attempt": matched_attempt,
        "branch_flags": branch_flags,
        "bridge_interval": bridge_interval,
        "bridge_sum": bridge_sum,
        "symbolic_block": symbolic_block,
        "old_defect": old_defect,
        "new_defect": new_defect,
        "attempt_label_counts": route_obj.get("attempt_label_counts") if isinstance(route_obj, dict) else None,
        "attempt_flag_counts": route_obj.get("attempt_flag_counts") if isinstance(route_obj, dict) else None,
        "active_shortest_length": route_obj.get("active_shortest_length") if isinstance(route_obj, dict) else None,
        "selected_attempt_compact": compact(attempt, 800),
        "selected_route_compact": compact(route_obj, 1000),
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "rows": len(rows),
        "matched_route_object_rows": sum(1 for r in rows if r.get("matched_route_object")),
        "matched_attempt_rows": sum(1 for r in rows if r.get("matched_attempt")),
        "by_family": dict(Counter(r.get("family") for r in rows).most_common()),
        "by_route_label": dict(Counter(r.get("route_label") for r in rows).most_common()),
        "by_family_route": dict(Counter(f"{r.get('family')}::{r.get('route_label')}" for r in rows).most_common()),
        "branch_flag_histogram": dict(Counter(flag for r in rows for flag in (r.get("branch_flags") or [])).most_common()),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input_jsonl")
    ap.add_argument("--out", default="-")
    ap.add_argument("--summary-out", default=None)
    args = ap.parse_args()

    rows = [normalize(r) for r in iter_jsonl(Path(args.input_jsonl))]
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
