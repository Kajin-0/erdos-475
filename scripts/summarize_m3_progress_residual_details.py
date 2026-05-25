#!/usr/bin/env python3
"""
Summarize the kept m=3 terminal-progress residuals.

Input is produced by:

    scripts/extract_m3_progress_residuals.py

Typical inputs:

    logs/m3_progress_residuals_p17.jsonl
    logs/m3_progress_residuals_p23.jsonl

The kept records are usually:

    neutral_no_rightward_progress
    worse_only

This script splits those records by mechanism:

    - support length by label
    - attempt flags by label
    - best permutation counts by label
    - neutral progress type counts
    - worse new_defect histogram
    - records already containing distributed/signed flags
    - compact examples by residual label
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
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


def tuple_key(x: Any) -> str:
    if isinstance(x, (list, tuple)):
        return "(" + ",".join(tuple_key(v) if isinstance(v, (list, tuple)) else str(v) for v in x) + ")"
    return str(x)


def compact_record(rec: dict[str, Any]) -> dict[str, Any]:
    return {
        "residual_label": rec.get("residual_label"),
        "p": rec.get("p"),
        "S": rec.get("S"),
        "sigma": rec.get("sigma"),
        "order": rec.get("order"),
        "defect": rec.get("defect"),
        "attempt_flag_counts": rec.get("attempt_flag_counts"),
        "record_best_class": rec.get("record_best_class"),
        "candidate_best_counts": rec.get("candidate_best_counts"),
        "support_lengths": rec.get("support_lengths"),
        "terminal_total_lengths": rec.get("terminal_total_lengths"),
        "best_perm_counts": rec.get("best_perm_counts"),
        "neutral_progress_counts": rec.get("neutral_progress_counts"),
        "neutral_progresses_first5": (rec.get("neutral_progresses") or [])[:5],
        "worse_best_moves_first5": (rec.get("worse_best_moves") or [])[:5],
    }


def summarize(records: list[dict[str, Any]], example_limit: int) -> dict[str, Any]:
    label_counts: Counter[str] = Counter()
    p_counts: Counter[str] = Counter()
    support_by_label: dict[str, Counter[str]] = defaultdict(Counter)
    min_support_by_label: dict[str, Counter[str]] = defaultdict(Counter)
    max_support_by_label: dict[str, Counter[str]] = defaultdict(Counter)
    flags_by_label: dict[str, Counter[str]] = defaultdict(Counter)
    perms_by_label: dict[str, Counter[str]] = defaultdict(Counter)
    neutral_progress_by_label: dict[str, Counter[str]] = defaultdict(Counter)
    worse_new_defects_by_label: dict[str, Counter[str]] = defaultdict(Counter)
    candidate_best_by_label: dict[str, Counter[str]] = defaultdict(Counter)
    signed_distributed_by_label: dict[str, Counter[str]] = defaultdict(Counter)
    examples: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for rec in records:
        label = rec.get("residual_label", "unknown")
        label_counts[label] += 1
        p_counts[str(rec.get("p"))] += 1
        flags = Counter(rec.get("attempt_flag_counts", {}))
        flags_by_label[label].update(flags)
        perms_by_label[label].update(rec.get("best_perm_counts", {}))
        neutral_progress_by_label[label].update(rec.get("neutral_progress_counts", {}))
        candidate_best_by_label[label].update(rec.get("candidate_best_counts", {}))

        if flags.get("DISTRIBUTED_BRIDGE", 0) > 0:
            signed_distributed_by_label[label]["has_distributed"] += 1
        else:
            signed_distributed_by_label[label]["no_distributed"] += 1
        if flags.get("SIGNED_INTERVAL", 0) > 0:
            signed_distributed_by_label[label]["has_signed"] += 1
        else:
            signed_distributed_by_label[label]["no_signed"] += 1
        if flags.get("DISTRIBUTED_BRIDGE", 0) > 0 or flags.get("SIGNED_INTERVAL", 0) > 0:
            signed_distributed_by_label[label]["has_signed_or_distributed"] += 1
        else:
            signed_distributed_by_label[label]["pure_terminal_local"] += 1

        for s in rec.get("support_lengths", []) or []:
            support_by_label[label][str(s)] += 1
        if rec.get("min_support_length") is not None:
            min_support_by_label[label][str(rec["min_support_length"])] += 1
        if rec.get("max_support_length") is not None:
            max_support_by_label[label][str(rec["max_support_length"])] += 1

        for move in rec.get("worse_best_moves", []) or []:
            worse_new_defects_by_label[label][tuple_key(move.get("new_defect"))] += 1

        if len(examples[label]) < example_limit:
            examples[label].append(compact_record(rec))

    def sorted_numeric_counter(c: Counter[str]) -> dict[str, int]:
        def keyfn(item: tuple[str, int]) -> tuple[int, str]:
            k, _v = item
            try:
                return (int(k), k)
            except Exception:
                return (10**9, k)
        return dict(sorted(c.items(), key=keyfn))

    return {
        "records": len(records),
        "p_counts": dict(p_counts),
        "label_counts": dict(label_counts),
        "support_length_by_label": {k: sorted_numeric_counter(v) for k, v in support_by_label.items()},
        "min_support_length_by_label": {k: sorted_numeric_counter(v) for k, v in min_support_by_label.items()},
        "max_support_length_by_label": {k: sorted_numeric_counter(v) for k, v in max_support_by_label.items()},
        "attempt_flags_by_label": {k: dict(v.most_common()) for k, v in flags_by_label.items()},
        "best_perms_by_label": {k: dict(v.most_common()) for k, v in perms_by_label.items()},
        "neutral_progress_by_label": {k: dict(v.most_common()) for k, v in neutral_progress_by_label.items()},
        "candidate_best_by_label": {k: dict(v.most_common()) for k, v in candidate_best_by_label.items()},
        "signed_distributed_by_label": {k: dict(v.most_common()) for k, v in signed_distributed_by_label.items()},
        "worse_new_defects_by_label": {k: dict(v.most_common()) for k, v in worse_new_defects_by_label.items()},
        "examples_by_label": dict(examples),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input m3 progress residual JSONL files.")
    ap.add_argument("--out", default="-", help="Output JSON path, or '-' for stdout.")
    ap.add_argument("--pretty", action="store_true")
    ap.add_argument("--example-limit", type=int, default=3)
    args = ap.parse_args()

    records: list[dict[str, Any]] = []
    input_counts = {}
    for name in args.jsonl:
        path = Path(name)
        loaded = list(iter_jsonl(path))
        input_counts[str(path)] = len(loaded)
        records.extend(loaded)

    summary = summarize(records, args.example_limit)
    summary["input_files"] = input_counts

    text = json.dumps(summary, indent=2 if args.pretty else None, sort_keys=True)
    if args.out == "-":
        print(text)
    else:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
