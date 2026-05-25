#!/usr/bin/env python3
"""
Test local block moves exposed by one-sided long terminal bridges.

Input is a JSONL log produced by scripts/test_external_bridge_overlap.py, usually
filtered to hard records with no CLEAN_DESCENT, for example:

    logs/external_bridge_hard_terminal_lengths_p17.jsonl

This script focuses first on the right-sided orientation:

    R = X A z q B Y_r
    Z = A z
    z + sum(B) = 0
    sum(A) = sum(B)

where z is the last atom of the active shortest zero interval and B is the
terminal right external support.

The first tested move was only:

    A z q B -> B z q A

Empirically that was mostly worse.  This version tests the full block-permutation
family over the four blocks:

    A, z, q, B

preserving the internal order of A and B.  This is still low-compute, but it is a
much better diagnostic for the one-sided long terminal branch.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Sequence, Tuple

INF = 10**9
BLOCK_NAMES = ("A", "z", "q", "B")
ORIGINAL_PERM = ("A", "z", "q", "B")


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


def flags(record: dict[str, Any]) -> Counter[str]:
    return Counter(record.get("attempt_flag_counts", {}))


def is_right_one_sided_long(record: dict[str, Any]) -> bool:
    f = flags(record)
    return (
        f.get("RIGHT_TERMINAL_BRIDGE", 0) > 0
        and f.get("LEFT_TERMINAL_BRIDGE", 0) == 0
        and f.get("LONG_TERMINAL_BRIDGE", 0) > 0
    )


def right_long_terminal_candidates(record: dict[str, Any]) -> list[dict[str, Any]]:
    """Return candidate terminal windows.

    Candidate contains enough indices to test block permutations over:

        A, z, q, B

    with A = order[z_i:z_j-1], z = order[z_j-1], q=order[z_j],
    B = order[z_j+1:external_index].
    """
    out: list[dict[str, Any]] = []
    order = record["order"]
    p = int(record["p"])
    seen = set()
    for interval in record.get("interval_records", []):
        z_i = int(interval["i"])
        z_j = int(interval["j"])
        m = int(interval["length"])
        rq = interval.get("right_q")
        if not rq:
            continue
        for attempt in rq.get("attempts", []):
            if "RIGHT_TERMINAL_BRIDGE" not in attempt.get("branch_flags", []):
                continue
            for bridge in attempt.get("external", []):
                if bridge.get("b") != m - 1:
                    continue
                for meta in bridge.get("terminal_support", []) or []:
                    if meta.get("side") != "right":
                        continue
                    if not meta.get("long_terminal"):
                        continue
                    ext_index = int(meta["external_index"])
                    support_length = int(meta["support_length"])
                    key = (z_i, z_j, ext_index)
                    if key in seen:
                        continue
                    seen.add(key)
                    if support_length <= 0:
                        continue
                    if z_j - z_i < 3:
                        continue
                    if ext_index <= z_j + 1 or ext_index > len(order):
                        continue
                    A = [int(x) for x in order[z_i : z_j - 1]]
                    z = int(order[z_j - 1])
                    q = int(order[z_j])
                    B = [int(x) for x in order[z_j + 1 : ext_index]]
                    if not A or not B:
                        continue
                    valid_equal_sum = (sum(A) % p == sum(B) % p)
                    valid_terminal = ((z + sum(B)) % p == 0)
                    out.append(
                        {
                            "z_i": z_i,
                            "z_j": z_j,
                            "m": m,
                            "k": attempt.get("k"),
                            "external_index": ext_index,
                            "support_length": support_length,
                            "terminal_total_length": meta.get("terminal_total_length"),
                            "A": A,
                            "z": z,
                            "q": q,
                            "B": B,
                            "valid_equal_sum": valid_equal_sum,
                            "valid_terminal": valid_terminal,
                        }
                    )
    return out


def block_map(cand: dict[str, Any]) -> dict[str, tuple[int, ...]]:
    return {
        "A": tuple(int(x) for x in cand["A"]),
        "z": (int(cand["z"]),),
        "q": (int(cand["q"]),),
        "B": tuple(int(x) for x in cand["B"]),
    }


def apply_perm(order: Sequence[int], cand: dict[str, Any], perm: tuple[str, ...]) -> tuple[int, ...]:
    z_i = int(cand["z_i"])
    ext = int(cand["external_index"])
    blocks = block_map(cand)
    new_window: tuple[int, ...] = tuple()
    for name in perm:
        new_window += blocks[name]
    return tuple(order[:z_i]) + new_window + tuple(order[ext:])


def classify_move(oldD: tuple, newD: tuple, cand: dict[str, Any]) -> str:
    if not cand.get("valid_equal_sum") or not cand.get("valid_terminal"):
        return "bad_indexing"
    if newD < oldD:
        return "improved"
    if newD == oldD:
        return "neutral"
    return "worse"


def zero_block_flags(p: int, cand: dict[str, Any], perm: tuple[str, ...]) -> list[str]:
    """Record whether the perm makes known zero blocks contiguous."""
    flags: list[str] = []
    # z+B or B+z is zero by terminal relation.
    for a, b in zip(perm, perm[1:]):
        if {a, b} == {"z", "B"}:
            flags.append("terminal_zero_contiguous")
        if a == "A" and b == "z":
            flags.append("old_Z_contiguous")
    return flags


def analyze_record(record: dict[str, Any], *, max_candidates: int) -> dict[str, Any] | None:
    if not is_right_one_sided_long(record):
        return None
    p = int(record["p"])
    order = tuple(int(x) for x in record["order"])
    oldD = defect_short(p, order)
    cands = right_long_terminal_candidates(record)
    candidate_results = []
    record_best_class = "none"
    class_rank = {"improved": 0, "neutral": 1, "worse": 2, "bad_indexing": 3, "none": 4}

    perms = [perm for perm in itertools.permutations(BLOCK_NAMES) if perm != ORIGINAL_PERM]

    for cand in cands[:max_candidates]:
        moves = []
        for perm in perms:
            new_order = apply_perm(order, cand, perm)
            newD = defect_short(p, new_order)
            cls = classify_move(oldD, newD, cand)
            if class_rank[cls] < class_rank[record_best_class]:
                record_best_class = cls
            moves.append(
                {
                    "perm": list(perm),
                    "old_defect": oldD,
                    "new_defect": newD,
                    "class": cls,
                    "zero_block_flags": zero_block_flags(p, cand, perm),
                    "new_order": list(new_order),
                    "new_zero_intervals_first10": [list(z) for z in zero_intervals(p, new_order)[:10]],
                }
            )
        candidate_results.append(
            {
                "candidate": cand,
                "move_counts": dict(Counter(m["class"] for m in moves)),
                "best_class": min((m["class"] for m in moves), key=lambda c: class_rank[c]),
                "moves": moves,
            }
        )
    if not candidate_results:
        return None

    return {
        "p": p,
        "S": record.get("S"),
        "sigma": record.get("sigma"),
        "order": list(order),
        "defect": oldD,
        "attempt_flag_counts": record.get("attempt_flag_counts", {}),
        "record_best_class": record_best_class,
        "candidate_results": candidate_results,
        "candidate_best_counts": dict(Counter(c["best_class"] for c in candidate_results)),
        "move_class_counts": dict(Counter(m["class"] for c in candidate_results for m in c["moves"])),
        "perm_class_counts": {
            " ".join(perm): dict(
                Counter(
                    m["class"]
                    for c in candidate_results
                    for m in c["moves"]
                    if tuple(m["perm"]) == perm
                )
            )
            for perm in perms
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input external-bridge hard JSONL logs.")
    ap.add_argument("--out", default="-", help="Output JSONL path, or '-' for stdout.")
    ap.add_argument("--max-candidates", type=int, default=20)
    args = ap.parse_args()

    records_out = []
    input_records = 0
    eligible_records = 0
    aggregate_best = Counter()
    aggregate_candidate_best = Counter()
    aggregate_move = Counter()

    for name in args.jsonl:
        for rec in iter_jsonl(Path(name)):
            input_records += 1
            analyzed = analyze_record(rec, max_candidates=args.max_candidates)
            if analyzed is None:
                continue
            eligible_records += 1
            aggregate_best.update([analyzed["record_best_class"]])
            aggregate_candidate_best.update(analyzed["candidate_best_counts"])
            aggregate_move.update(analyzed["move_class_counts"])
            records_out.append(analyzed)

    if args.out == "-":
        for rec in records_out:
            print(json.dumps(rec, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for rec in records_out:
                fh.write(json.dumps(rec, separators=(",", ":")) + "\n")

    print(f"input_records={input_records}")
    print(f"eligible_right_one_sided_long_records={eligible_records}")
    print("aggregate_record_best=" + json.dumps(dict(aggregate_best), sort_keys=True))
    print("aggregate_candidate_best=" + json.dumps(dict(aggregate_candidate_best), sort_keys=True))
    print("aggregate_move=" + json.dumps(dict(aggregate_move), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
