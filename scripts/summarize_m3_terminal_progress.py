#!/usr/bin/env python3
"""
Summarize progress of neutral moves in the m=3 one-sided terminal residual.

Input is produced by:

    scripts/test_one_sided_terminal_exchange.py

Typical inputs:

    logs/one_sided_terminal_block_perms_p17.jsonl
    logs/one_sided_terminal_block_perms_p23.jsonl

This script focuses on records with:

    record_best_class == neutral
    defect == (1,3,1,[2])
    candidate m == 3

For every best neutral move it computes:

    - old unique zero interval
    - new unique zero interval
    - left/right boundary distances before and after
    - shift direction of the zero interval
    - whether the zero triple atom multiset is preserved
    - whether the zero interval moves toward a boundary
    - whether it makes right-terminal-direction progress
    - permutation histograms by progress class

This is diagnostic infrastructure for defining the refined terminal-progress
tie-break needed after S21.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
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


def perm_key(perm: list[str] | tuple[str, ...]) -> str:
    return " ".join(str(x) for x in perm)


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
        "nearest_boundary_distance": min(i, n - j),
        "center2": i + j,
    }


def progress_relation(old_payload: dict[str, Any], new_payload: dict[str, Any]) -> dict[str, Any]:
    old_left = int(old_payload["left_distance"])
    old_right = int(old_payload["right_distance"])
    old_near = int(old_payload["nearest_boundary_distance"])
    new_left = int(new_payload["left_distance"])
    new_right = int(new_payload["right_distance"])
    new_near = int(new_payload["nearest_boundary_distance"])
    old_center2 = int(old_payload["center2"])
    new_center2 = int(new_payload["center2"])

    if new_near < old_near:
        boundary_progress = "toward_boundary"
    elif new_near > old_near:
        boundary_progress = "away_from_boundary"
    else:
        boundary_progress = "same_boundary_distance"

    if new_left < old_left:
        left_progress = "left"
    elif new_left > old_left:
        left_progress = "right"
    else:
        left_progress = "same_left_index"

    if new_right < old_right:
        right_distance_progress = "toward_right_terminal"
    elif new_right > old_right:
        right_distance_progress = "away_from_right_terminal"
    else:
        right_distance_progress = "same_right_distance"

    if new_center2 < old_center2:
        center_shift = "left"
    elif new_center2 > old_center2:
        center_shift = "right"
    else:
        center_shift = "same_center"

    if new_center2 > old_center2:
        terminal_direction_progress = "rightward_progress"
    elif new_center2 < old_center2:
        terminal_direction_progress = "leftward_regress"
    else:
        terminal_direction_progress = "same_position"

    same_atoms_ordered = old_payload["block"] == new_payload["block"]
    same_atoms_multiset = old_payload["block_sorted"] == new_payload["block_sorted"]

    return {
        "delta_left_distance": new_left - old_left,
        "delta_right_distance": new_right - old_right,
        "delta_nearest_boundary_distance": new_near - old_near,
        "delta_center2": new_center2 - old_center2,
        "boundary_progress": boundary_progress,
        "right_distance_progress": right_distance_progress,
        "terminal_direction_progress": terminal_direction_progress,
        "left_index_shift": left_progress,
        "center_shift": center_shift,
        "same_atoms_ordered": same_atoms_ordered,
        "same_atoms_multiset": same_atoms_multiset,
        "old_block": old_payload["block"],
        "new_block": new_payload["block"],
    }


def candidate_is_m3(cand_res: dict[str, Any]) -> bool:
    return cand_res.get("candidate", {}).get("m") == 3


def analyze_record(record: dict[str, Any], record_index: int) -> list[dict[str, Any]]:
    if record.get("record_best_class") != "neutral":
        return []
    if record.get("defect") != SPECIAL_DEFECT:
        return []

    p = int(record["p"])
    old_order = [int(x) for x in record["order"]]
    old_interval = unique_zero_interval_of_length(p, old_order, 3)
    old_payload = interval_payload(old_order, old_interval)
    if old_payload is None:
        return []

    analyses: list[dict[str, Any]] = []
    for cand_idx, cand_res in enumerate(record.get("candidate_results", [])):
        if not candidate_is_m3(cand_res):
            continue
        bests = [m for m in best_moves_for_candidate(cand_res) if m.get("class") == "neutral"]
        for move_idx, move in enumerate(bests):
            new_order = [int(x) for x in move.get("new_order", [])]
            if not new_order:
                continue
            newD = defect_short(p, new_order)
            if list(newD[:3]) != [1, 3, 1] or tuple(newD[3]) != (2,):
                continue
            new_interval = unique_zero_interval_of_length(p, new_order, 3)
            new_payload = interval_payload(new_order, new_interval)
            if new_payload is None:
                continue
            rel = progress_relation(old_payload, new_payload)
            cand = cand_res.get("candidate", {})
            analyses.append(
                {
                    "record_index": record_index,
                    "candidate_index": cand_idx,
                    "move_index": move_idx,
                    "p": p,
                    "perm": move.get("perm"),
                    "perm_key": perm_key(move.get("perm", [])),
                    "old_defect": record.get("defect"),
                    "new_defect": list(newD),
                    "old_interval": old_payload,
                    "new_interval": new_payload,
                    "progress": rel,
                    "candidate": {
                        "m": cand.get("m"),
                        "support_length": cand.get("support_length"),
                        "terminal_total_length": cand.get("terminal_total_length"),
                        "A": cand.get("A"),
                        "z": cand.get("z"),
                        "q": cand.get("q"),
                        "B": cand.get("B"),
                    },
                    "order": old_order,
                    "new_order": new_order,
                }
            )
    return analyses


def summarize(analyses: list[dict[str, Any]], example_limit: int) -> dict[str, Any]:
    perm_hist: Counter[str] = Counter()
    boundary_progress_hist: Counter[str] = Counter()
    right_distance_progress_hist: Counter[str] = Counter()
    terminal_direction_hist: Counter[str] = Counter()
    center_shift_hist: Counter[str] = Counter()
    left_index_shift_hist: Counter[str] = Counter()
    same_atoms_hist: Counter[str] = Counter()
    delta_near_hist: Counter[str] = Counter()
    delta_left_hist: Counter[str] = Counter()
    delta_right_hist: Counter[str] = Counter()
    delta_center_hist: Counter[str] = Counter()
    support_hist: Counter[str] = Counter()
    perm_by_boundary: dict[str, Counter[str]] = defaultdict(Counter)
    perm_by_terminal_direction: dict[str, Counter[str]] = defaultdict(Counter)
    perm_by_right_distance: dict[str, Counter[str]] = defaultdict(Counter)
    perm_by_same_atoms: dict[str, Counter[str]] = defaultdict(Counter)

    best_record_boundary: dict[int, str] = {}
    best_record_boundary_perm: dict[int, str] = {}
    best_record_terminal: dict[int, str] = {}
    best_record_terminal_perm: dict[int, str] = {}
    best_record_right_distance: dict[int, str] = {}
    best_record_right_distance_perm: dict[int, str] = {}

    boundary_rank = {"toward_boundary": 0, "same_boundary_distance": 1, "away_from_boundary": 2}
    terminal_rank = {"rightward_progress": 0, "same_position": 1, "leftward_regress": 2}
    right_distance_rank = {"toward_right_terminal": 0, "same_right_distance": 1, "away_from_right_terminal": 2}

    for a in analyses:
        pk = a["perm_key"]
        rel = a["progress"]
        perm_hist[pk] += 1
        boundary_progress_hist[rel["boundary_progress"]] += 1
        right_distance_progress_hist[rel["right_distance_progress"]] += 1
        terminal_direction_hist[rel["terminal_direction_progress"]] += 1
        center_shift_hist[rel["center_shift"]] += 1
        left_index_shift_hist[rel["left_index_shift"]] += 1
        same_atoms_hist["same_multiset" if rel["same_atoms_multiset"] else "changed_multiset"] += 1
        same_atoms_hist["same_ordered" if rel["same_atoms_ordered"] else "changed_ordered"] += 1
        delta_near_hist[str(rel["delta_nearest_boundary_distance"])] += 1
        delta_left_hist[str(rel["delta_left_distance"])] += 1
        delta_right_hist[str(rel["delta_right_distance"])] += 1
        delta_center_hist[str(rel["delta_center2"])] += 1
        support_hist[str(a["candidate"].get("support_length"))] += 1
        perm_by_boundary[pk][rel["boundary_progress"]] += 1
        perm_by_terminal_direction[pk][rel["terminal_direction_progress"]] += 1
        perm_by_right_distance[pk][rel["right_distance_progress"]] += 1
        perm_by_same_atoms[pk]["same_multiset" if rel["same_atoms_multiset"] else "changed_multiset"] += 1

        rid = int(a["record_index"])
        bcur = best_record_boundary.get(rid)
        if bcur is None or boundary_rank[rel["boundary_progress"]] < boundary_rank[bcur]:
            best_record_boundary[rid] = rel["boundary_progress"]
            best_record_boundary_perm[rid] = pk

        tcur = best_record_terminal.get(rid)
        if tcur is None or terminal_rank[rel["terminal_direction_progress"]] < terminal_rank[tcur]:
            best_record_terminal[rid] = rel["terminal_direction_progress"]
            best_record_terminal_perm[rid] = pk

        rcur = best_record_right_distance.get(rid)
        if rcur is None or right_distance_rank[rel["right_distance_progress"]] < right_distance_rank[rcur]:
            best_record_right_distance[rid] = rel["right_distance_progress"]
            best_record_right_distance_perm[rid] = pk

    def sort_numeric_counter(c: Counter[str]) -> dict[str, int]:
        def keyfn(item: tuple[str, int]) -> tuple[int, str]:
            k, _v = item
            try:
                return (int(k), k)
            except Exception:
                return (10**9, k)
        return dict(sorted(c.items(), key=keyfn))

    return {
        "neutral_move_analyses": len(analyses),
        "records_with_neutral_analyses": len({a["record_index"] for a in analyses}),
        "perm_histogram": dict(perm_hist.most_common()),
        "boundary_progress_histogram": dict(boundary_progress_hist),
        "right_distance_progress_histogram": dict(right_distance_progress_hist),
        "terminal_direction_progress_histogram": dict(terminal_direction_hist),
        "record_best_boundary_progress_histogram": dict(Counter(best_record_boundary.values())),
        "record_best_boundary_perm_histogram": dict(Counter(best_record_boundary_perm.values()).most_common()),
        "record_best_terminal_direction_histogram": dict(Counter(best_record_terminal.values())),
        "record_best_terminal_direction_perm_histogram": dict(Counter(best_record_terminal_perm.values()).most_common()),
        "record_best_right_distance_progress_histogram": dict(Counter(best_record_right_distance.values())),
        "record_best_right_distance_perm_histogram": dict(Counter(best_record_right_distance_perm.values()).most_common()),
        "center_shift_histogram": dict(center_shift_hist),
        "left_index_shift_histogram": dict(left_index_shift_hist),
        "same_atoms_histogram": dict(same_atoms_hist),
        "delta_nearest_boundary_histogram": sort_numeric_counter(delta_near_hist),
        "delta_left_distance_histogram": sort_numeric_counter(delta_left_hist),
        "delta_right_distance_histogram": sort_numeric_counter(delta_right_hist),
        "delta_center2_histogram": sort_numeric_counter(delta_center_hist),
        "support_length_histogram": sort_numeric_counter(support_hist),
        "perm_by_boundary_progress": {k: dict(v) for k, v in perm_by_boundary.items()},
        "perm_by_terminal_direction_progress": {k: dict(v) for k, v in perm_by_terminal_direction.items()},
        "perm_by_right_distance_progress": {k: dict(v) for k, v in perm_by_right_distance.items()},
        "perm_by_same_atoms": {k: dict(v) for k, v in perm_by_same_atoms.items()},
        "rightward_progress_examples": [a for a in analyses if a["progress"]["terminal_direction_progress"] == "rightward_progress"][:example_limit],
        "same_position_examples": [a for a in analyses if a["progress"]["terminal_direction_progress"] == "same_position"][:example_limit],
        "leftward_regress_examples": [a for a in analyses if a["progress"]["terminal_direction_progress"] == "leftward_regress"][:example_limit],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input terminal block-permutation JSONL files.")
    ap.add_argument("--out", default="-", help="Output JSON path, or '-' for stdout.")
    ap.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    ap.add_argument("--example-limit", type=int, default=3)
    args = ap.parse_args()

    records: list[dict[str, Any]] = []
    input_counts = {}
    for name in args.jsonl:
        path = Path(name)
        loaded = list(iter_jsonl(path))
        input_counts[str(path)] = len(loaded)
        records.extend(loaded)

    analyses: list[dict[str, Any]] = []
    for idx, rec in enumerate(records):
        analyses.extend(analyze_record(rec, idx))

    summary = summarize(analyses, args.example_limit)
    summary["input_records"] = len(records)
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
