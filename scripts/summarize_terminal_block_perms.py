#!/usr/bin/env python3
"""
Summarize block-permutation tests for one-sided long terminal bridges.

Input is produced by:

    scripts/test_one_sided_terminal_exchange.py

Typical inputs:

    logs/one_sided_terminal_block_perms_p17.jsonl
    logs/one_sided_terminal_block_perms_p23.jsonl

The script reports:

    - record_best_class counts
    - candidate_best_class counts
    - move class counts
    - permutation-level class counts
    - improving permutation histogram
    - neutral permutation histogram
    - worse-only residual examples
    - neutral-best residual examples

This helps decide whether the proof should use a canonical permutation,
a finite menu of permutations, or a terminal-progress tie-break coordinate.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

CLASS_RANK = {"improved": 0, "neutral": 1, "worse": 2, "bad_indexing": 3, "none": 4}


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


def perm_key(perm: list[str] | tuple[str, ...]) -> str:
    return " ".join(str(x) for x in perm)


def best_moves_for_candidate(candidate_result: dict[str, Any]) -> list[dict[str, Any]]:
    moves = candidate_result.get("moves", [])
    if not moves:
        return []
    best_rank = min(CLASS_RANK.get(m.get("class", "none"), 99) for m in moves)
    return [m for m in moves if CLASS_RANK.get(m.get("class", "none"), 99) == best_rank]


def summarize_records(records: list[dict[str, Any]], residual_limit: int) -> dict[str, Any]:
    record_best_counts: Counter[str] = Counter()
    candidate_best_counts: Counter[str] = Counter()
    move_class_counts: Counter[str] = Counter()
    perm_class_counts: dict[str, Counter[str]] = defaultdict(Counter)
    improving_perm_hist: Counter[str] = Counter()
    neutral_perm_hist: Counter[str] = Counter()
    worse_perm_hist: Counter[str] = Counter()
    zero_flag_counts: Counter[str] = Counter()
    perm_zero_flags: dict[str, Counter[str]] = defaultdict(Counter)

    worse_only_examples: list[dict[str, Any]] = []
    neutral_best_examples: list[dict[str, Any]] = []
    improved_examples: list[dict[str, Any]] = []

    for rec_idx, rec in enumerate(records):
        rbest = rec.get("record_best_class", "none")
        record_best_counts[rbest] += 1
        candidate_best_counts.update(rec.get("candidate_best_counts", {}))
        move_class_counts.update(rec.get("move_class_counts", {}))

        for cand_idx, cand_res in enumerate(rec.get("candidate_results", [])):
            bests = best_moves_for_candidate(cand_res)
            for m in cand_res.get("moves", []):
                cls = m.get("class", "none")
                pk = perm_key(m.get("perm", []))
                perm_class_counts[pk][cls] += 1
                for zf in m.get("zero_block_flags", []) or []:
                    zero_flag_counts[zf] += 1
                    perm_zero_flags[pk][zf] += 1
            for bm in bests:
                pk = perm_key(bm.get("perm", []))
                cls = bm.get("class", "none")
                if cls == "improved":
                    improving_perm_hist[pk] += 1
                elif cls == "neutral":
                    neutral_perm_hist[pk] += 1
                elif cls == "worse":
                    worse_perm_hist[pk] += 1

        compact = {
            "record_index": rec_idx,
            "p": rec.get("p"),
            "S": rec.get("S"),
            "sigma": rec.get("sigma"),
            "order": rec.get("order"),
            "defect": rec.get("defect"),
            "attempt_flag_counts": rec.get("attempt_flag_counts"),
            "record_best_class": rbest,
            "candidate_best_counts": rec.get("candidate_best_counts"),
        }
        if rbest == "worse" and len(worse_only_examples) < residual_limit:
            worse_only_examples.append(compact)
        elif rbest == "neutral" and len(neutral_best_examples) < residual_limit:
            neutral_best_examples.append(compact)
        elif rbest == "improved" and len(improved_examples) < residual_limit:
            improved_examples.append(compact)

    # Sort permutation summaries by useful priority: improved count desc, neutral count desc, worse asc.
    perm_summary = {}
    for pk, counts in perm_class_counts.items():
        total = sum(counts.values())
        perm_summary[pk] = {
            "total": total,
            "improved": counts.get("improved", 0),
            "neutral": counts.get("neutral", 0),
            "worse": counts.get("worse", 0),
            "bad_indexing": counts.get("bad_indexing", 0),
            "improved_rate": counts.get("improved", 0) / total if total else 0.0,
            "non_worse_rate": (counts.get("improved", 0) + counts.get("neutral", 0)) / total if total else 0.0,
            "zero_block_flags": dict(perm_zero_flags.get(pk, Counter())),
        }

    top_improving_perms = sorted(
        perm_summary.items(),
        key=lambda kv: (kv[1]["improved"], kv[1]["non_worse_rate"], -kv[1]["worse"]),
        reverse=True,
    )
    top_non_worse_perms = sorted(
        perm_summary.items(),
        key=lambda kv: (kv[1]["non_worse_rate"], kv[1]["improved"], -kv[1]["worse"]),
        reverse=True,
    )

    return {
        "records": len(records),
        "record_best_counts": dict(record_best_counts),
        "candidate_best_counts": dict(candidate_best_counts),
        "move_class_counts": dict(move_class_counts),
        "improving_perm_histogram": dict(improving_perm_hist.most_common()),
        "neutral_perm_histogram": dict(neutral_perm_hist.most_common()),
        "worse_perm_histogram": dict(worse_perm_hist.most_common()),
        "zero_block_flag_counts": dict(zero_flag_counts),
        "top_improving_perms": [{"perm": k, **v} for k, v in top_improving_perms[:10]],
        "top_non_worse_perms": [{"perm": k, **v} for k, v in top_non_worse_perms[:10]],
        "perm_summary": perm_summary,
        "worse_only_examples": worse_only_examples,
        "neutral_best_examples": neutral_best_examples,
        "improved_examples": improved_examples,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input block-permutation JSONL files.")
    ap.add_argument("--out", default="-", help="Output JSON path, or '-' for stdout.")
    ap.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    ap.add_argument("--residual-limit", type=int, default=5, help="Number of compact residual examples to keep.")
    args = ap.parse_args()

    records: list[dict[str, Any]] = []
    input_counts = {}
    for name in args.jsonl:
        path = Path(name)
        loaded = list(iter_jsonl(path))
        input_counts[str(path)] = len(loaded)
        records.extend(loaded)

    summary = summarize_records(records, args.residual_limit)
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
