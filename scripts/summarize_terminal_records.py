#!/usr/bin/env python3
"""
Summarize terminal-bridge structure in external-bridge JSONL logs.

Input is produced by:

    scripts/test_external_bridge_overlap.py

The intended input is usually a hard-record file such as:

    logs/external_bridge_hard_terminal_lengths_p17.jsonl

where records have no CLEAN_DESCENT attempts.  The script reports record-level
rather than attempt-level structure:

    - left/right terminal presence
    - short/long terminal presence
    - terminal + distributed
    - terminal + signed
    - one-sided vs two-sided terminal
    - terminal support-length histograms

This is diagnostic infrastructure for the analytic sprint, not a proof engine.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from statistics import median
from typing import Any, Iterable


TERMINAL_FLAGS = {"LEFT_TERMINAL_BRIDGE", "RIGHT_TERMINAL_BRIDGE"}


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


def all_attempts(record: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for interval in record.get("interval_records", []):
        for side_key in ("right_q", "left_q"):
            side = interval.get(side_key)
            if not side:
                continue
            out.extend(side.get("attempts", []))
    return out


def terminal_support_entries(attempt: dict[str, Any]) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for bridge in attempt.get("external", []):
        if bridge.get("b") is None:
            continue
        for meta in bridge.get("terminal_support", []) or []:
            entries.append(meta)
    return entries


def classify_record(record: dict[str, Any]) -> dict[str, Any]:
    attempts = all_attempts(record)
    flags = Counter()
    labels = Counter()
    support_lengths: list[int] = []
    terminal_total_lengths: list[int] = []
    terminal_meta_count = 0

    for attempt in attempts:
        labels.update([attempt.get("label", "UNKNOWN")])
        flags.update(attempt.get("branch_flags", []))
        for meta in terminal_support_entries(attempt):
            terminal_meta_count += 1
            if meta.get("valid_support_length"):
                support_lengths.append(int(meta["support_length"]))
                terminal_total_lengths.append(int(meta["terminal_total_length"]))

    has_left = flags["LEFT_TERMINAL_BRIDGE"] > 0
    has_right = flags["RIGHT_TERMINAL_BRIDGE"] > 0
    has_terminal = has_left or has_right
    has_short = flags["SHORT_TERMINAL_BRIDGE"] > 0
    has_long = flags["LONG_TERMINAL_BRIDGE"] > 0
    has_distributed = flags["DISTRIBUTED_BRIDGE"] > 0
    has_signed = flags["SIGNED_INTERVAL"] > 0
    has_external = flags["EXTERNAL_BRIDGE"] > 0
    has_clean = flags["CLEAN_DESCENT"] > 0

    if has_left and has_right:
        terminal_sidedness = "both_left_right"
    elif has_right:
        terminal_sidedness = "right_only"
    elif has_left:
        terminal_sidedness = "left_only"
    else:
        terminal_sidedness = "none"

    if has_short and has_long:
        terminal_length_class = "both_short_and_long"
    elif has_long:
        terminal_length_class = "long_only"
    elif has_short:
        terminal_length_class = "short_only"
    else:
        terminal_length_class = "none"

    return {
        "has_clean": has_clean,
        "has_terminal": has_terminal,
        "has_left": has_left,
        "has_right": has_right,
        "has_short": has_short,
        "has_long": has_long,
        "has_distributed": has_distributed,
        "has_signed": has_signed,
        "has_external": has_external,
        "terminal_sidedness": terminal_sidedness,
        "terminal_length_class": terminal_length_class,
        "flags": dict(flags),
        "labels": dict(labels),
        "support_lengths": support_lengths,
        "terminal_total_lengths": terminal_total_lengths,
        "terminal_meta_count": terminal_meta_count,
    }


def update_bool_count(counter: Counter[str], name: str, value: bool) -> None:
    if value:
        counter[name] += 1


def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    record_counts: Counter[str] = Counter()
    aggregate_flags: Counter[str] = Counter()
    aggregate_labels: Counter[str] = Counter()
    sidedness: Counter[str] = Counter()
    length_class: Counter[str] = Counter()
    support_hist: Counter[str] = Counter()
    terminal_total_hist: Counter[str] = Counter()
    support_lengths_all: list[int] = []
    terminal_total_all: list[int] = []

    for record in records:
        cls = classify_record(record)
        aggregate_flags.update(cls["flags"])
        aggregate_labels.update(cls["labels"])
        sidedness.update([cls["terminal_sidedness"]])
        length_class.update([cls["terminal_length_class"]])

        update_bool_count(record_counts, "records_with_clean_descent", cls["has_clean"])
        update_bool_count(record_counts, "records_with_terminal", cls["has_terminal"])
        update_bool_count(record_counts, "records_with_left_terminal", cls["has_left"])
        update_bool_count(record_counts, "records_with_right_terminal", cls["has_right"])
        update_bool_count(record_counts, "records_with_both_left_right_terminal", cls["has_left"] and cls["has_right"])
        update_bool_count(record_counts, "records_with_right_only_terminal", cls["has_right"] and not cls["has_left"])
        update_bool_count(record_counts, "records_with_left_only_terminal", cls["has_left"] and not cls["has_right"])
        update_bool_count(record_counts, "records_with_short_terminal", cls["has_short"])
        update_bool_count(record_counts, "records_with_long_terminal", cls["has_long"])
        update_bool_count(record_counts, "records_with_both_short_and_long_terminal", cls["has_short"] and cls["has_long"])
        update_bool_count(record_counts, "records_with_long_only_terminal", cls["has_long"] and not cls["has_short"])
        update_bool_count(record_counts, "records_with_short_only_terminal", cls["has_short"] and not cls["has_long"])
        update_bool_count(record_counts, "records_with_terminal_and_distributed", cls["has_terminal"] and cls["has_distributed"])
        update_bool_count(record_counts, "records_with_terminal_and_signed", cls["has_terminal"] and cls["has_signed"])
        update_bool_count(record_counts, "records_with_terminal_and_external", cls["has_terminal"] and cls["has_external"])
        update_bool_count(record_counts, "records_with_distributed_no_terminal", cls["has_distributed"] and not cls["has_terminal"])
        update_bool_count(record_counts, "records_with_signed_no_terminal", cls["has_signed"] and not cls["has_terminal"])

        for s in cls["support_lengths"]:
            support_hist[str(s)] += 1
            support_lengths_all.append(s)
        for t in cls["terminal_total_lengths"]:
            terminal_total_hist[str(t)] += 1
            terminal_total_all.append(t)

    support_stats: dict[str, Any]
    if support_lengths_all:
        support_stats = {
            "count": len(support_lengths_all),
            "min": min(support_lengths_all),
            "median": median(support_lengths_all),
            "max": max(support_lengths_all),
        }
    else:
        support_stats = {"count": 0, "min": None, "median": None, "max": None}

    terminal_total_stats: dict[str, Any]
    if terminal_total_all:
        terminal_total_stats = {
            "count": len(terminal_total_all),
            "min": min(terminal_total_all),
            "median": median(terminal_total_all),
            "max": max(terminal_total_all),
        }
    else:
        terminal_total_stats = {"count": 0, "min": None, "median": None, "max": None}

    return {
        "records": len(records),
        "record_counts": dict(record_counts),
        "terminal_sidedness": dict(sidedness),
        "terminal_length_class": dict(length_class),
        "aggregate_flags": dict(aggregate_flags),
        "aggregate_labels": dict(aggregate_labels),
        "support_length_stats": support_stats,
        "terminal_total_length_stats": terminal_total_stats,
        "support_length_histogram": dict(sorted(support_hist.items(), key=lambda kv: int(kv[0]))),
        "terminal_total_length_histogram": dict(sorted(terminal_total_hist.items(), key=lambda kv: int(kv[0]))),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input JSONL log files.")
    ap.add_argument("--out", default="-", help="Output JSON summary path, or '-' for stdout.")
    ap.add_argument("--pretty", action="store_true", help="Pretty-print JSON.")
    args = ap.parse_args()

    all_records: list[dict[str, Any]] = []
    input_counts = {}
    for name in args.jsonl:
        path = Path(name)
        records = list(iter_jsonl(path))
        input_counts[str(path)] = len(records)
        all_records.extend(records)

    summary = summarize(all_records)
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
