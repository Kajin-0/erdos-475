#!/usr/bin/env python3
"""
Extract the remaining m=3 one-sided terminal progress residuals.

Input is produced by:

    scripts/test_one_sided_terminal_exchange.py

Typical inputs:

    logs/one_sided_terminal_block_perms_p17.jsonl
    logs/one_sided_terminal_block_perms_p23.jsonl

This script labels records as:

    neutral_with_rightward_progress
    neutral_no_rightward_progress
    worse_only
    other

for records in the special residual class:

    D_short = (1,3,1,[2])
    candidate m = 3

The main output should be filtered to:

    neutral_no_rightward_progress
    worse_only

These are the small residuals after S23.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Sequence, Tuple

INF = 10**9
CLASS_RANK = {"improved": 0, "neutral": 1, "worse": 2, "bad_indexing": 3, "none": 4}
SPECIAL_DEFECT = [1, 3, 1, [2]]


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


def partial_sums_extended(p: int, order: Sequence[int]) -> list[int]:
    s = 0
    out = [0]
    for x in order:
        s = (s + int(x)) % p
        out.append(s)
    return out


def zero_intervals(p: int, order: Sequence[int]) -> list[Tuple[int, int, int]]:
    P = partial_sums_extended(p, order)
    out: list[Tuple[int, int, int]] = []
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            if P[i] == P[j]:
                out.append((i, j, j - i))
    return out


def defect_short(p: int, order: Sequence[int]) -> Tuple[int, int, int, Tuple[int, ...]]:
    P = partial_sums_extended(p, order)
    counts = Counter(P)
    E = len(P) - len(counts)
    if E == 0:
        return (0, INF, 0, tuple())
    zis = zero_intervals(p, order)
    L_min = min(length for _, _, length in zis)
    N_min = sum(1 for _, _, length in zis if length == L_min)
    M = tuple(sorted((c for c in counts.values() if c > 1), reverse=True))
    return (E, L_min, N_min, M)


def best_moves_for_candidate(candidate_result: dict[str, Any]) -> list[dict[str, Any]]:
    moves = candidate_result.get("moves", [])
    if not moves:
        return []
    best_rank = min(CLASS_RANK.get(m.get("class", "none"), 99) for m in moves)
    return [m for m in moves if CLASS_RANK.get(m.get("class", "none"), 99) == best_rank]


def unique_zero_interval_of_length(p: int, order: Sequence[int], length: int) -> tuple[int, int, int] | None:
    matches = [z for z in zero_intervals(p, order) if z[2] == length]
    if len(matches) == 1:
        return matches[0]
    return None


def interval_payload(order: Sequence[int], interval: tuple[int, int, int] | None) -> dict[str, Any] | None:
    if interval is None:
        return None
    i, j, length = interval
    block = [int(x) for x in order[i:j]]
    n = len(order)
    return {
        "i": i,
        "j": j,
        "length": length,
        "block": block,
        "block_sorted": sorted(block),
        "left_distance": i,
        "right_distance": n - j,
        "center2": i + j,
    }


def move_progress(p: int, old_order: list[int], new_order: list[int]) -> dict[str, Any] | None:
    old_interval = unique_zero_interval_of_length(p, old_order, 3)
    new_interval = unique_zero_interval_of_length(p, new_order, 3)
    old_payload = interval_payload(old_order, old_interval)
    new_payload = interval_payload(new_order, new_interval)
    if old_payload is None or new_payload is None:
        return None
    delta_right = int(new_payload["right_distance"]) - int(old_payload["right_distance"])
    delta_center2 = int(new_payload["center2"]) - int(old_payload["center2"])
    if delta_right < 0:
        terminal_progress = "rightward_progress"
    elif delta_right == 0:
        terminal_progress = "same_position"
    else:
        terminal_progress = "leftward_regress"
    return {
        "terminal_progress": terminal_progress,
        "delta_right_distance": delta_right,
        "delta_center2": delta_center2,
        "old_interval": old_payload,
        "new_interval": new_payload,
        "same_atoms_multiset": old_payload["block_sorted"] == new_payload["block_sorted"],
        "same_atoms_ordered": old_payload["block"] == new_payload["block"],
    }


def record_is_special_m3(record: dict[str, Any]) -> bool:
    if record.get("defect") != SPECIAL_DEFECT:
        return False
    cands = record.get("candidate_results", [])
    return bool(cands) and all(c.get("candidate", {}).get("m") == 3 for c in cands)


def classify_record(record: dict[str, Any]) -> dict[str, Any] | None:
    if not record_is_special_m3(record):
        return None
    p = int(record["p"])
    old_order = [int(x) for x in record["order"]]
    rbest = record.get("record_best_class")

    neutral_progresses = []
    worse_best_moves = []
    support_lengths = []
    terminal_totals = []
    best_perm_counts = Counter()

    for cand_idx, cand_res in enumerate(record.get("candidate_results", [])):
        cand = cand_res.get("candidate", {})
        if cand.get("support_length") is not None:
            support_lengths.append(int(cand["support_length"]))
        if cand.get("terminal_total_length") is not None:
            terminal_totals.append(int(cand["terminal_total_length"]))
        for move in best_moves_for_candidate(cand_res):
            cls = move.get("class")
            perm = " ".join(move.get("perm", []))
            best_perm_counts[perm] += 1
            new_order = [int(x) for x in move.get("new_order", [])]
            if cls == "neutral" and new_order:
                progress = move_progress(p, old_order, new_order)
                if progress is not None:
                    neutral_progresses.append({"candidate_index": cand_idx, "perm": perm, **progress})
            elif cls == "worse":
                worse_best_moves.append({"candidate_index": cand_idx, "perm": perm, "new_defect": move.get("new_defect")})

    has_rightward = any(x["terminal_progress"] == "rightward_progress" for x in neutral_progresses)
    has_same = any(x["terminal_progress"] == "same_position" for x in neutral_progresses)
    has_leftward = any(x["terminal_progress"] == "leftward_regress" for x in neutral_progresses)

    if rbest == "neutral":
        if has_rightward:
            residual_label = "neutral_with_rightward_progress"
        else:
            residual_label = "neutral_no_rightward_progress"
    elif rbest == "worse":
        residual_label = "worse_only"
    else:
        residual_label = "other"

    return {
        "residual_label": residual_label,
        "p": p,
        "S": record.get("S"),
        "sigma": record.get("sigma"),
        "order": old_order,
        "defect": record.get("defect"),
        "attempt_flag_counts": record.get("attempt_flag_counts"),
        "record_best_class": rbest,
        "candidate_best_counts": record.get("candidate_best_counts"),
        "support_lengths": support_lengths,
        "terminal_total_lengths": terminal_totals,
        "min_support_length": min(support_lengths) if support_lengths else None,
        "max_support_length": max(support_lengths) if support_lengths else None,
        "best_perm_counts": dict(best_perm_counts),
        "neutral_progress_counts": dict(Counter(x["terminal_progress"] for x in neutral_progresses)),
        "has_rightward_progress": has_rightward,
        "has_same_position": has_same,
        "has_leftward_regress": has_leftward,
        "neutral_progresses": neutral_progresses[:20],
        "worse_best_moves": worse_best_moves[:20],
    }


def summarize(extracted: list[dict[str, Any]]) -> dict[str, Any]:
    label_counts = Counter(x["residual_label"] for x in extracted)
    support_hist = Counter()
    min_support_hist = Counter()
    max_support_hist = Counter()
    attempt_flags = Counter()
    best_perms = Counter()
    neutral_progress = Counter()
    p_counts = Counter(str(x["p"]) for x in extracted)

    for x in extracted:
        attempt_flags.update(x.get("attempt_flag_counts", {}))
        best_perms.update(x.get("best_perm_counts", {}))
        neutral_progress.update(x.get("neutral_progress_counts", {}))
        for s in x.get("support_lengths", []):
            support_hist[str(s)] += 1
        if x.get("min_support_length") is not None:
            min_support_hist[str(x["min_support_length"])] += 1
        if x.get("max_support_length") is not None:
            max_support_hist[str(x["max_support_length"])] += 1

    def sort_numeric(c: Counter[str]) -> dict[str, int]:
        def keyfn(item: tuple[str, int]) -> tuple[int, str]:
            k, _v = item
            try:
                return (int(k), k)
            except Exception:
                return (10**9, k)
        return dict(sorted(c.items(), key=keyfn))

    return {
        "records": len(extracted),
        "p_counts": dict(p_counts),
        "label_counts": dict(label_counts),
        "attempt_flag_counts": dict(attempt_flags.most_common()),
        "best_perm_counts": dict(best_perms.most_common()),
        "neutral_progress_counts": dict(neutral_progress),
        "support_length_histogram": sort_numeric(support_hist),
        "min_support_length_histogram": sort_numeric(min_support_hist),
        "max_support_length_histogram": sort_numeric(max_support_hist),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input terminal block-permutation JSONL files.")
    ap.add_argument("--out", default="-", help="Output JSONL path, or '-' for stdout.")
    ap.add_argument("--summary-out", default=None, help="Optional JSON summary path.")
    ap.add_argument("--keep", default="neutral_no_rightward_progress,worse_only", help="Comma-separated residual labels to write.")
    args = ap.parse_args()

    keep = {x.strip() for x in args.keep.split(",") if x.strip()}
    extracted_all = []
    input_records = 0
    for name in args.jsonl:
        for rec in iter_jsonl(Path(name)):
            input_records += 1
            classified = classify_record(rec)
            if classified is not None:
                extracted_all.append(classified)

    kept = [x for x in extracted_all if x["residual_label"] in keep]

    if args.out == "-":
        for rec in kept:
            print(json.dumps(rec, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for rec in kept:
                fh.write(json.dumps(rec, separators=(",", ":")) + "\n")

    summary = summarize(extracted_all)
    summary["input_records"] = input_records
    summary["kept_records"] = len(kept)
    summary["keep_labels"] = sorted(keep)

    print("summary=" + json.dumps(summary, sort_keys=True))
    if args.summary_out:
        Path(args.summary_out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
