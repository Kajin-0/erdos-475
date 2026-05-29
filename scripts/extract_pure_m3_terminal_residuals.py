#!/usr/bin/env python3
"""
Extract pure-terminal m=3 residuals from m3 progress residual JSONL logs.

Input is produced by:

    scripts/extract_m3_progress_residuals.py

Typical inputs:

    logs/m3_progress_residuals_p17.jsonl
    logs/m3_progress_residuals_p23.jsonl

This script removes records that already have SIGNED_INTERVAL or DISTRIBUTED_BRIDGE
flags and keeps only the genuinely new pure terminal local residue:

    pure_neutral_same_position
    pure_worse_only

These are the cases that should feed the S26 pure m=3 terminal residual attack.
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


def has_signed_or_distributed(record: dict[str, Any]) -> bool:
    flags = record.get("attempt_flag_counts", {}) or {}
    return (flags.get("SIGNED_INTERVAL", 0) > 0) or (flags.get("DISTRIBUTED_BRIDGE", 0) > 0)


def classify_pure(record: dict[str, Any]) -> str | None:
    if has_signed_or_distributed(record):
        return None
    label = record.get("residual_label")
    if label == "neutral_no_rightward_progress":
        # In current data these are same-position neutral moves, but preserve the label
        # if future data includes leftward regressions.
        progress = Counter(record.get("neutral_progress_counts", {}))
        if progress.get("same_position", 0) > 0 and progress.get("leftward_regress", 0) == 0:
            return "pure_neutral_same_position"
        if progress.get("leftward_regress", 0) > 0:
            return "pure_neutral_leftward_regress"
        return "pure_neutral_no_rightward"
    if label == "worse_only":
        return "pure_worse_only"
    return None


def compact_summary(records: list[dict[str, Any]]) -> dict[str, Any]:
    label_counts = Counter()
    residual_label_counts = Counter()
    p_counts = Counter()
    support_hist = Counter()
    best_perm_counts = Counter()
    neutral_progress_counts = Counter()
    attempt_flags = Counter()
    candidate_best_counts = Counter()

    for rec in records:
        label_counts[rec.get("pure_label", "unknown")] += 1
        residual_label_counts[rec.get("residual_label", "unknown")] += 1
        p_counts[str(rec.get("p"))] += 1
        attempt_flags.update(rec.get("attempt_flag_counts", {}) or {})
        best_perm_counts.update(rec.get("best_perm_counts", {}) or {})
        neutral_progress_counts.update(rec.get("neutral_progress_counts", {}) or {})
        candidate_best_counts.update(rec.get("candidate_best_counts", {}) or {})
        for s in rec.get("support_lengths", []) or []:
            support_hist[str(s)] += 1

    def sort_numeric(c: Counter[str]) -> dict[str, int]:
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
        "pure_label_counts": dict(label_counts),
        "source_residual_label_counts": dict(residual_label_counts),
        "support_length_histogram": sort_numeric(support_hist),
        "attempt_flag_counts": dict(attempt_flags.most_common()),
        "candidate_best_counts": dict(candidate_best_counts.most_common()),
        "best_perm_counts": dict(best_perm_counts.most_common()),
        "neutral_progress_counts": dict(neutral_progress_counts.most_common()),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input m3 progress residual JSONL files.")
    ap.add_argument("--out", default="-", help="Output pure residual JSONL path, or '-' for stdout.")
    ap.add_argument("--summary-out", default=None, help="Optional summary JSON path.")
    args = ap.parse_args()

    input_records = 0
    pure_records: list[dict[str, Any]] = []
    skipped_signed_distributed = 0
    skipped_other = 0

    for name in args.jsonl:
        for rec in iter_jsonl(Path(name)):
            input_records += 1
            if has_signed_or_distributed(rec):
                skipped_signed_distributed += 1
                continue
            pure_label = classify_pure(rec)
            if pure_label is None:
                skipped_other += 1
                continue
            out = dict(rec)
            out["pure_label"] = pure_label
            pure_records.append(out)

    if args.out == "-":
        for rec in pure_records:
            print(json.dumps(rec, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for rec in pure_records:
                fh.write(json.dumps(rec, separators=(",", ":")) + "\n")

    summary = compact_summary(pure_records)
    summary["input_records"] = input_records
    summary["skipped_signed_distributed"] = skipped_signed_distributed
    summary["skipped_other"] = skipped_other
    print("summary=" + json.dumps(summary, sort_keys=True))
    if args.summary_out:
        Path(args.summary_out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
