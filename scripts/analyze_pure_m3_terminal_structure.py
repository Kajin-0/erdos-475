#!/usr/bin/env python3
"""
Analyze the unresolved pure m=3 right-terminal residual using the full block-permutation logs.

Input is produced by:

    scripts/test_one_sided_terminal_exchange.py

Typical inputs:

    logs/one_sided_terminal_block_perms_p17.jsonl
    logs/one_sided_terminal_block_perms_p23.jsonl

Default filter: the true unresolved pure local bottleneck:

    defect = (1,3,1,[2])
    no SIGNED_INTERVAL flag
    no DISTRIBUTED_BRIDGE flag
    every candidate has m=3
    record_best_class == worse
        OR
    record_best_class == neutral with no best neutral move shifting the unique zero triple rightward

Use --include-rightward-neutral to restore the broader diagnostic mode that also includes
handled neutral-rightward records.

For each pure record it extracts:

    - X/Y boundary lengths around the terminal window
    - A,z,q,B structure
    - support length |B|
    - old unique zero triple
    - new zero intervals produced by each local block permutation
    - which new collisions touch moved block-boundary endpoints
    - permutation-level collision signatures

The goal is to expose the hidden equations behind the pure worse-only and no-rightward branches.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Sequence, Tuple

SPECIAL_DEFECT = [1, 3, 1, [2]]
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


def defect_short(p: int, order: Sequence[int]) -> tuple[Any, ...]:
    P = partial_sums_extended(p, order)
    counts = Counter(P)
    E = len(P) - len(counts)
    if E == 0:
        return (0, 10**9, 0, tuple())
    zis = zero_intervals(p, order)
    L_min = min(length for _, _, length in zis)
    N_min = sum(1 for _, _, length in zis if length == L_min)
    M = tuple(sorted((c for c in counts.values() if c > 1), reverse=True))
    return (E, L_min, N_min, M)


def tuple_key(x: Any) -> str:
    if isinstance(x, (list, tuple)):
        return "(" + ",".join(tuple_key(v) if isinstance(v, (list, tuple)) else str(v) for v in x) + ")"
    return str(x)


def perm_key(perm: Sequence[str]) -> str:
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
    n = len(order)
    block = [int(x) for x in order[i:j]]
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


def neutral_progress_classes(record: dict[str, Any]) -> Counter[str]:
    """Classify best neutral moves by terminal-direction movement of unique zero triple."""
    if record.get("record_best_class") != "neutral":
        return Counter()
    p = int(record["p"])
    old_order = [int(x) for x in record["order"]]
    old_payload = interval_payload(old_order, unique_zero_interval_of_length(p, old_order, 3))
    if old_payload is None:
        return Counter({"unknown": 1})

    counts: Counter[str] = Counter()
    for cand_res in record.get("candidate_results", []):
        for move in best_moves_for_candidate(cand_res):
            if move.get("class") != "neutral":
                continue
            new_order = [int(x) for x in move.get("new_order", [])]
            if not new_order:
                continue
            new_payload = interval_payload(new_order, unique_zero_interval_of_length(p, new_order, 3))
            if new_payload is None:
                counts["unknown"] += 1
                continue
            dc = int(new_payload["center2"]) - int(old_payload["center2"])
            if dc > 0:
                counts["rightward_progress"] += 1
            elif dc < 0:
                counts["leftward_regress"] += 1
            else:
                counts["same_position"] += 1
    return counts


def has_rightward_neutral_progress(record: dict[str, Any]) -> bool:
    return neutral_progress_classes(record).get("rightward_progress", 0) > 0


def is_basic_pure_record(record: dict[str, Any]) -> bool:
    if record.get("defect") != SPECIAL_DEFECT:
        return False
    if record.get("record_best_class") not in {"neutral", "worse"}:
        return False
    flags = record.get("attempt_flag_counts", {}) or {}
    if flags.get("SIGNED_INTERVAL", 0) > 0 or flags.get("DISTRIBUTED_BRIDGE", 0) > 0:
        return False
    cands = record.get("candidate_results", [])
    if not cands:
        return False
    if not all(c.get("candidate", {}).get("m") == 3 for c in cands):
        return False
    return True


def is_pure_record(record: dict[str, Any], include_rightward_neutral: bool) -> bool:
    if not is_basic_pure_record(record):
        return False
    if record.get("record_best_class") == "worse":
        return True
    if include_rightward_neutral:
        return True
    return not has_rightward_neutral_progress(record)


def pure_label(record: dict[str, Any]) -> str:
    if record.get("record_best_class") == "worse":
        return "pure_worse_only"
    progress = neutral_progress_classes(record)
    if progress.get("rightward_progress", 0) > 0:
        return "pure_neutral_rightward_progress"
    if progress.get("leftward_regress", 0) > 0:
        return "pure_neutral_leftward_regress"
    if progress.get("same_position", 0) > 0:
        return "pure_neutral_same_position"
    return "pure_neutral_other"


def block_lengths(cand: dict[str, Any]) -> dict[str, int]:
    return {
        "A": len(cand.get("A", [])),
        "z": 1,
        "q": 1,
        "B": len(cand.get("B", [])),
    }


def boundary_label_map(cand: dict[str, Any], perm: Sequence[str]) -> dict[int, str]:
    z_i = int(cand["z_i"])
    lens = block_lengths(cand)
    out = {z_i: "window_start"}
    pos = z_i
    prefix: list[str] = []
    for name in perm:
        pos += lens[name]
        prefix.append(name)
        out[pos] = "after_" + "".join(prefix)
    return out


def collision_payload(p: int, order: Sequence[int], zint: tuple[int, int, int], boundary_map: dict[int, str], window_start: int, window_end: int) -> dict[str, Any]:
    i, j, length = zint
    P = partial_sums_extended(p, order)
    i_lab = boundary_map.get(i)
    j_lab = boundary_map.get(j)
    touches_boundary = i_lab is not None or j_lab is not None
    if i < window_start and j < window_start:
        span_type = "left_external"
    elif i > window_end and j > window_end:
        span_type = "right_external"
    elif window_start <= i <= window_end and window_start <= j <= window_end:
        span_type = "internal_window"
    else:
        span_type = "cross_window_external"
    return {
        "i": i,
        "j": j,
        "length": length,
        "value": int(P[i]),
        "left_label": i_lab,
        "right_label": j_lab,
        "touches_moved_boundary": touches_boundary,
        "span_type": span_type,
        "block": [int(x) for x in order[i:j]],
    }


def analyze_move(p: int, cand: dict[str, Any], move: dict[str, Any]) -> dict[str, Any]:
    perm = move.get("perm", [])
    new_order = [int(x) for x in move.get("new_order", [])]
    if not new_order:
        return {"perm": perm, "class": move.get("class"), "error": "missing_new_order"}
    z_i = int(cand["z_i"])
    ext = int(cand["external_index"])
    bmap = boundary_label_map(cand, perm)
    new_zis = zero_intervals(p, new_order)
    collisions = [collision_payload(p, new_order, z, bmap, z_i, ext) for z in new_zis]
    touching = [c for c in collisions if c["touches_moved_boundary"]]
    signatures = []
    for c in touching:
        signatures.append(
            f"{c.get('left_label') or 'ext'}={c.get('right_label') or 'ext'}:L{c['length']}:{c['span_type']}"
        )
    return {
        "perm": perm,
        "perm_key": perm_key(perm),
        "class": move.get("class"),
        "old_defect": move.get("old_defect"),
        "new_defect": move.get("new_defect"),
        "zero_block_flags": move.get("zero_block_flags", []),
        "boundary_map": bmap,
        "new_zero_interval_count": len(new_zis),
        "new_zero_intervals": collisions,
        "touching_collision_count": len(touching),
        "touching_collision_signatures": signatures,
    }


def analyze_candidate(p: int, order: Sequence[int], cand_res: dict[str, Any], include_all_moves: bool) -> dict[str, Any]:
    cand = cand_res.get("candidate", {})
    z_i = int(cand["z_i"])
    z_j = int(cand["z_j"])
    ext = int(cand["external_index"])
    A = [int(x) for x in cand.get("A", [])]
    B = [int(x) for x in cand.get("B", [])]
    z = int(cand["z"])
    q = int(cand["q"])
    moves = cand_res.get("moves", []) if include_all_moves else best_moves_for_candidate(cand_res)
    return {
        "candidate": {
            "z_i": z_i,
            "z_j": z_j,
            "external_index": ext,
            "X_length": z_i,
            "Y_length": len(order) - ext,
            "m": cand.get("m"),
            "support_length": cand.get("support_length"),
            "terminal_total_length": cand.get("terminal_total_length"),
            "A": A,
            "z": z,
            "q": q,
            "B": B,
            "sum_A": sum(A) % p,
            "sum_B": sum(B) % p,
            "z_plus_B": (z + sum(B)) % p,
            "valid_equal_sum": cand.get("valid_equal_sum"),
            "valid_terminal": cand.get("valid_terminal"),
        },
        "move_counts": cand_res.get("move_counts"),
        "best_class": cand_res.get("best_class"),
        "moves_analyzed": [analyze_move(p, cand, m) for m in moves],
    }


def analyze_record(record: dict[str, Any], record_index: int, include_all_moves: bool, include_rightward_neutral: bool) -> dict[str, Any] | None:
    if not is_pure_record(record, include_rightward_neutral):
        return None
    p = int(record["p"])
    order = [int(x) for x in record["order"]]
    old_interval = interval_payload(order, unique_zero_interval_of_length(p, order, 3))
    cands = [analyze_candidate(p, order, c, include_all_moves) for c in record.get("candidate_results", [])]
    return {
        "record_index": record_index,
        "p": p,
        "pure_label": pure_label(record),
        "neutral_progress_classes": dict(neutral_progress_classes(record)),
        "S": record.get("S"),
        "sigma": record.get("sigma"),
        "order": order,
        "defect": record.get("defect"),
        "record_best_class": record.get("record_best_class"),
        "candidate_best_counts": record.get("candidate_best_counts"),
        "attempt_flag_counts": record.get("attempt_flag_counts"),
        "old_unique_zero_triple": old_interval,
        "candidate_analyses": cands,
    }


def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    label_counts = Counter(r["pure_label"] for r in records)
    neutral_progress_counts: Counter[str] = Counter()
    support_hist = Counter()
    x_len_hist = Counter()
    y_len_hist = Counter()
    perm_class_counts: dict[str, Counter[str]] = defaultdict(Counter)
    signature_counts: Counter[str] = Counter()
    signature_by_label: dict[str, Counter[str]] = defaultdict(Counter)
    new_defect_by_label: dict[str, Counter[str]] = defaultdict(Counter)
    zero_block_by_label: dict[str, Counter[str]] = defaultdict(Counter)

    for r in records:
        label = r["pure_label"]
        neutral_progress_counts.update(r.get("neutral_progress_classes", {}))
        for ca in r.get("candidate_analyses", []):
            c = ca["candidate"]
            support_hist[str(c.get("support_length"))] += 1
            x_len_hist[str(c.get("X_length"))] += 1
            y_len_hist[str(c.get("Y_length"))] += 1
            for ma in ca.get("moves_analyzed", []):
                pk = ma.get("perm_key")
                cls = ma.get("class")
                perm_class_counts[pk][cls] += 1
                new_defect_by_label[label][tuple_key(ma.get("new_defect"))] += 1
                for zbf in ma.get("zero_block_flags", []) or []:
                    zero_block_by_label[label][zbf] += 1
                for sig in ma.get("touching_collision_signatures", []) or []:
                    signature_counts[sig] += 1
                    signature_by_label[label][sig] += 1

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
        "pure_label_counts": dict(label_counts),
        "neutral_progress_counts": dict(neutral_progress_counts.most_common()),
        "support_length_histogram": sort_numeric(support_hist),
        "X_length_histogram": sort_numeric(x_len_hist),
        "Y_length_histogram": sort_numeric(y_len_hist),
        "perm_class_counts": {k: dict(v.most_common()) for k, v in perm_class_counts.items()},
        "top_touching_collision_signatures": dict(signature_counts.most_common(25)),
        "touching_collision_signatures_by_label": {k: dict(v.most_common(25)) for k, v in signature_by_label.items()},
        "new_defects_by_label": {k: dict(v.most_common(25)) for k, v in new_defect_by_label.items()},
        "zero_block_flags_by_label": {k: dict(v.most_common()) for k, v in zero_block_by_label.items()},
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input full terminal block-permutation JSONL logs.")
    ap.add_argument("--out", default="-", help="Output analyzed pure residual JSONL path, or '-' for stdout.")
    ap.add_argument("--summary-out", default=None, help="Optional summary JSON path.")
    ap.add_argument("--include-all-moves", action="store_true", help="Analyze all moves, not only best moves.")
    ap.add_argument("--include-rightward-neutral", action="store_true", help="Include handled neutral records that already have rightward terminal progress.")
    args = ap.parse_args()

    analyzed: list[dict[str, Any]] = []
    input_records = 0
    for name in args.jsonl:
        for idx, rec in enumerate(iter_jsonl(Path(name))):
            input_records += 1
            ar = analyze_record(rec, idx, args.include_all_moves, args.include_rightward_neutral)
            if ar is not None:
                analyzed.append(ar)

    if args.out == "-":
        for rec in analyzed:
            print(json.dumps(rec, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for rec in analyzed:
                fh.write(json.dumps(rec, separators=(",", ":")) + "\n")

    summary = summarize(analyzed)
    summary["input_records"] = input_records
    summary["include_rightward_neutral"] = bool(args.include_rightward_neutral)
    print("summary=" + json.dumps(summary, sort_keys=True))
    if args.summary_out:
        Path(args.summary_out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
