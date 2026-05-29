#!/usr/bin/env python3
"""
Summarize residual neutral/worse records from one-sided terminal block-permutation tests.

Input is produced by:

    scripts/test_one_sided_terminal_exchange.py

Typical inputs:

    logs/one_sided_terminal_block_perms_p17.jsonl
    logs/one_sided_terminal_block_perms_p23.jsonl

This script isolates records with record_best_class in {neutral,worse} by default
and reports:

    - old D_short histogram
    - active m histogram from candidate windows
    - support length histogram
    - terminal total length histogram
    - record_best_class counts
    - candidate_best_class counts
    - best neutral permutation histogram
    - best worse permutation histogram
    - delta histogram old_defect -> new_defect for best moves
    - compact examples of residual classes

This is diagnostic infrastructure for the S20/S21 m=3 residual attack.
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


def tuple_key(x: Any) -> str:
    if isinstance(x, (list, tuple)):
        return "(" + ",".join(tuple_key(v) if isinstance(v, (list, tuple)) else str(v) for v in x) + ")"
    return str(x)


def perm_key(perm: list[str] | tuple[str, ...]) -> str:
    return " ".join(str(x) for x in perm)


def defect_delta_key(oldD: list[Any] | tuple[Any, ...], newD: list[Any] | tuple[Any, ...]) -> str:
    if oldD is None or newD is None:
        return "missing"
    try:
        e0, l0, n0, m0 = oldD
        e1, l1, n1, m1 = newD
        return f"dE={int(e1)-int(e0)},dL={int(l1)-int(l0)},dN={int(n1)-int(n0)},M:{tuple_key(m0)}->{tuple_key(m1)}"
    except Exception:
        return f"{tuple_key(oldD)}->{tuple_key(newD)}"


def best_moves_for_candidate(candidate_result: dict[str, Any]) -> list[dict[str, Any]]:
    moves = candidate_result.get("moves", [])
    if not moves:
        return []
    best_rank = min(CLASS_RANK.get(m.get("class", "none"), 99) for m in moves)
    return [m for m in moves if CLASS_RANK.get(m.get("class", "none"), 99) == best_rank]


def candidate_defect(candidate_result: dict[str, Any], record: dict[str, Any]) -> Any:
    for move in candidate_result.get("moves", []):
        if move.get("old_defect") is not None:
            return move["old_defect"]
    return record.get("defect")


def compact_example(record: dict[str, Any], record_index: int) -> dict[str, Any]:
    cands = record.get("candidate_results", [])
    compact_cands = []
    for cand_res in cands[:3]:
        cand = cand_res.get("candidate", {})
        bests = best_moves_for_candidate(cand_res)
        compact_cands.append(
            {
                "candidate": {
                    "m": cand.get("m"),
                    "support_length": cand.get("support_length"),
                    "terminal_total_length": cand.get("terminal_total_length"),
                    "A": cand.get("A"),
                    "z": cand.get("z"),
                    "q": cand.get("q"),
                    "B": cand.get("B"),
                    "valid_equal_sum": cand.get("valid_equal_sum"),
                    "valid_terminal": cand.get("valid_terminal"),
                },
                "best_classes": [m.get("class") for m in bests],
                "best_perms": [m.get("perm") for m in bests[:5]],
                "best_new_defects": [m.get("new_defect") for m in bests[:5]],
            }
        )
    return {
        "record_index": record_index,
        "p": record.get("p"),
        "S": record.get("S"),
        "sigma": record.get("sigma"),
        "order": record.get("order"),
        "defect": record.get("defect"),
        "attempt_flag_counts": record.get("attempt_flag_counts"),
        "record_best_class": record.get("record_best_class"),
        "candidate_best_counts": record.get("candidate_best_counts"),
        "candidates": compact_cands,
    }


def summarize(records: list[dict[str, Any]], classes: set[str], example_limit: int) -> dict[str, Any]:
    selected = [r for r in records if r.get("record_best_class") in classes]

    record_best_counts = Counter(r.get("record_best_class", "none") for r in selected)
    candidate_best_counts: Counter[str] = Counter()
    old_defect_hist: Counter[str] = Counter()
    m_hist: Counter[str] = Counter()
    support_hist: Counter[str] = Counter()
    terminal_total_hist: Counter[str] = Counter()
    best_perm_hist: Counter[str] = Counter()
    best_neutral_perm_hist: Counter[str] = Counter()
    best_worse_perm_hist: Counter[str] = Counter()
    best_delta_hist: Counter[str] = Counter()
    best_delta_by_perm: dict[str, Counter[str]] = defaultdict(Counter)
    attempt_flag_hist: Counter[str] = Counter()
    candidate_validity: Counter[str] = Counter()
    m3_defect_special = 0
    all_candidates_m3 = 0
    all_records_defect_1_3_1 = 0

    examples_by_class: dict[str, list[dict[str, Any]]] = {c: [] for c in sorted(classes)}

    for global_idx, rec in enumerate(records):
        if rec.get("record_best_class") not in classes:
            continue
        rclass = rec.get("record_best_class", "none")
        attempt_flag_hist.update(rec.get("attempt_flag_counts", {}))
        candidate_best_counts.update(rec.get("candidate_best_counts", {}))

        defect = rec.get("defect")
        old_defect_hist[tuple_key(defect)] += 1
        if defect == [1, 3, 1, [2]]:
            all_records_defect_1_3_1 += 1

        cands = rec.get("candidate_results", [])
        if cands and all((cr.get("candidate", {}).get("m") == 3) for cr in cands):
            all_candidates_m3 += 1
        if defect == [1, 3, 1, [2]] and cands and all((cr.get("candidate", {}).get("m") == 3) for cr in cands):
            m3_defect_special += 1

        for cand_res in cands:
            cand = cand_res.get("candidate", {})
            m = cand.get("m")
            support = cand.get("support_length")
            terminal_total = cand.get("terminal_total_length")
            if m is not None:
                m_hist[str(m)] += 1
            if support is not None:
                support_hist[str(support)] += 1
            if terminal_total is not None:
                terminal_total_hist[str(terminal_total)] += 1
            if cand.get("valid_equal_sum") and cand.get("valid_terminal"):
                candidate_validity["valid"] += 1
            else:
                candidate_validity["invalid"] += 1

            oldD = candidate_defect(cand_res, rec)
            for bm in best_moves_for_candidate(cand_res):
                cls = bm.get("class", "none")
                pk = perm_key(bm.get("perm", []))
                best_perm_hist[pk] += 1
                if cls == "neutral":
                    best_neutral_perm_hist[pk] += 1
                elif cls == "worse":
                    best_worse_perm_hist[pk] += 1
                delta = defect_delta_key(oldD, bm.get("new_defect"))
                best_delta_hist[delta] += 1
                best_delta_by_perm[pk][delta] += 1

        if len(examples_by_class.get(rclass, [])) < example_limit:
            examples_by_class[rclass].append(compact_example(rec, global_idx))

    def sort_numeric_counter(c: Counter[str]) -> dict[str, int]:
        def keyfn(item: tuple[str, int]) -> tuple[int, str]:
            k, _v = item
            try:
                return (int(k), k)
            except Exception:
                return (10**9, k)
        return dict(sorted(c.items(), key=keyfn))

    return {
        "input_records": len(records),
        "selected_records": len(selected),
        "selected_classes": sorted(classes),
        "record_best_counts": dict(record_best_counts),
        "candidate_best_counts": dict(candidate_best_counts),
        "old_defect_histogram": dict(old_defect_hist.most_common()),
        "m_histogram": sort_numeric_counter(m_hist),
        "support_length_histogram": sort_numeric_counter(support_hist),
        "terminal_total_length_histogram": sort_numeric_counter(terminal_total_hist),
        "attempt_flag_histogram": dict(attempt_flag_hist.most_common()),
        "candidate_validity": dict(candidate_validity),
        "all_records_defect_1_3_1_count": all_records_defect_1_3_1,
        "all_candidates_m3_count": all_candidates_m3,
        "m3_and_defect_1_3_1_count": m3_defect_special,
        "m3_and_defect_1_3_1_fraction": (m3_defect_special / len(selected)) if selected else None,
        "best_perm_histogram": dict(best_perm_hist.most_common()),
        "best_neutral_perm_histogram": dict(best_neutral_perm_hist.most_common()),
        "best_worse_perm_histogram": dict(best_worse_perm_hist.most_common()),
        "best_delta_histogram": dict(best_delta_hist.most_common()),
        "best_delta_by_perm": {k: dict(v.most_common()) for k, v in best_delta_by_perm.items()},
        "examples_by_class": examples_by_class,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input terminal block-permutation JSONL logs.")
    ap.add_argument("--classes", default="neutral,worse", help="Comma-separated record_best_class values to include.")
    ap.add_argument("--out", default="-", help="Output JSON path, or '-' for stdout.")
    ap.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    ap.add_argument("--example-limit", type=int, default=5)
    args = ap.parse_args()

    classes = {x.strip() for x in args.classes.split(",") if x.strip()}
    records: list[dict[str, Any]] = []
    input_counts = {}
    for name in args.jsonl:
        path = Path(name)
        loaded = list(iter_jsonl(path))
        input_counts[str(path)] = len(loaded)
        records.extend(loaded)

    summary = summarize(records, classes, args.example_limit)
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
