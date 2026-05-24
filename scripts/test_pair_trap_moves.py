#!/usr/bin/env python3
"""
Low-compute tester for pair-trap block moves in the Erdős 475 analytic sprint.

This script does not attempt to prove Erdős 475.  It searches small prime examples
for shortest zero intervals Z containing equal-interval-sum pair traps, classifies
the trap geometry, applies the natural block move, and reports whether the working
short-defect D_short improves or whether failures are accompanied by external
collisions.

Definitions:

  Extended partial sums: P_0=0, P_i=r_1+...+r_i mod p.
  Zero interval: P_i=P_j, i<j.
  D_short(R)=(E,L_min,N_min,M), where:
    E     = collision excess of extended partial sums;
    L_min = shortest zero-interval length, inf if E=0;
    N_min = number of shortest zero intervals;
    M     = descending multiplicity profile >1.

Pair trap inside Z:

  U(i,j)=U(k,l), where U(a,b)=T_b-T_a and T are Z-internal prefixes.

Trap types:

  disjoint: i<j<k<l
  crossing: i<k<j<l, equivalent to equal flank sums U(i,k)=U(j,l)
  nested:   i<k<l<j, equivalent to zero flank sum U(i,k)+U(l,j)=0
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import random
from collections import Counter
from typing import Iterable, Iterator, List, Optional, Sequence, Tuple

INF = 10**9


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def partial_sums_extended(p: int, order: Sequence[int]) -> List[int]:
    s = 0
    out = [0]
    for x in order:
        s = (s + x) % p
        out.append(s)
    return out


def zero_intervals(p: int, order: Sequence[int]) -> List[Tuple[int, int, int]]:
    P = partial_sums_extended(p, order)
    out: List[Tuple[int, int, int]] = []
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


def z_internal_prefixes(p: int, Z: Sequence[int]) -> List[int]:
    s = 0
    T = [0]
    for z in Z:
        s = (s + z) % p
        T.append(s)
    return T


def interval_sum(T: Sequence[int], i: int, j: int, p: int) -> int:
    return (T[j] - T[i]) % p


def classify_pair(i: int, j: int, k: int, l: int) -> Optional[str]:
    if (i, j) == (k, l):
        return None
    if i == k or j == l:
        return "shared_endpoint"
    # Normalize by leftmost interval start for named types.
    if k < i:
        return classify_pair(k, l, i, j)
    if i < j < k < l:
        return "disjoint"
    if i < k < j < l:
        return "crossing"
    if i < k < l < j:
        return "nested"
    return "other"


def pair_traps_inside_Z(p: int, Z: Sequence[int]) -> List[dict]:
    T = z_internal_prefixes(p, Z)
    m = len(Z)
    intervals = []
    for i in range(m + 1):
        for j in range(i + 1, m + 1):
            # Exclude the whole Z interval when possible; it is the active zero block.
            intervals.append((i, j, interval_sum(T, i, j, p)))

    traps = []
    for idx1 in range(len(intervals)):
        i, j, s1 = intervals[idx1]
        for idx2 in range(idx1 + 1, len(intervals)):
            k, l, s2 = intervals[idx2]
            if s1 != s2:
                continue
            typ = classify_pair(i, j, k, l)
            if typ is None:
                continue
            traps.append({"i": i, "j": j, "k": k, "l": l, "sum": s1, "type": typ})
    return traps


def replace_block(order: Sequence[int], start: int, end: int, new_block: Sequence[int]) -> Tuple[int, ...]:
    return tuple(order[:start]) + tuple(new_block) + tuple(order[end:])


def move_for_trap(order: Sequence[int], z_start: int, trap: dict) -> Optional[Tuple[int, ...]]:
    """Apply the natural pair-trap block move in global coordinates.

    z_start is the atom index where active Z begins in order.
    Trap indices are prefix indices relative to Z.
    """
    i, j, k, l = trap["i"], trap["j"], trap["k"], trap["l"]
    typ = trap["type"]

    # Ensure i<... by swapping interval labels when needed.
    if k < i:
        i, j, k, l = k, l, i, j

    Z_window_start = z_start

    if typ == "disjoint":
        # A M B -> B M A
        A = order[Z_window_start + i : Z_window_start + j]
        M = order[Z_window_start + j : Z_window_start + k]
        B = order[Z_window_start + k : Z_window_start + l]
        new_block = tuple(B) + tuple(M) + tuple(A)
        return replace_block(order, Z_window_start + i, Z_window_start + l, new_block)

    if typ == "crossing":
        # i<k<j<l gives equal flank sums U(i,k)=U(j,l). Swap flank blocks A and C in A B C -> C B A.
        A = order[Z_window_start + i : Z_window_start + k]
        Bmid = order[Z_window_start + k : Z_window_start + j]
        C = order[Z_window_start + j : Z_window_start + l]
        new_block = tuple(C) + tuple(Bmid) + tuple(A)
        return replace_block(order, Z_window_start + i, Z_window_start + l, new_block)

    if typ == "nested":
        # i<k<l<j gives zero flanks U(i,k)+U(l,j)=0. Bring flanks together: A B C -> A C B.
        A = order[Z_window_start + i : Z_window_start + k]
        Bmid = order[Z_window_start + k : Z_window_start + l]
        C = order[Z_window_start + l : Z_window_start + j]
        new_block = tuple(A) + tuple(C) + tuple(Bmid)
        return replace_block(order, Z_window_start + i, Z_window_start + j, new_block)

    return None


def changed_indices(old: Sequence[int], new: Sequence[int]) -> Tuple[int, int]:
    """Return a coarse changed atom index window [lo,hi)."""
    n = len(old)
    lo = 0
    while lo < n and old[lo] == new[lo]:
        lo += 1
    hi = n
    while hi > lo and old[hi - 1] == new[hi - 1]:
        hi -= 1
    return lo, hi


def has_external_collision_change(p: int, old: Sequence[int], new: Sequence[int]) -> bool:
    """Heuristic external-collision detector for a block move.

    A changed collision is considered external if a repeated partial-sum value in the
    new ordering involves one partial-sum index outside the changed atom window.
    """
    lo_atom, hi_atom = changed_indices(old, new)
    # Partial-sum indices affected by atom window [lo,hi) are roughly lo+1 through hi.
    aff_lo = lo_atom + 1
    aff_hi = hi_atom
    P_new = partial_sums_extended(p, new)
    locs = {}
    for idx, val in enumerate(P_new):
        locs.setdefault(val, []).append(idx)
    for indices in locs.values():
        if len(indices) < 2:
            continue
        has_inside = any(aff_lo <= idx <= aff_hi for idx in indices)
        has_outside = any(idx < aff_lo or idx > aff_hi for idx in indices)
        if has_inside and has_outside:
            return True
    return False


def find_best_sample_order(p: int, S: Sequence[int], samples: int, rng: random.Random) -> Tuple[int, ...]:
    arr = list(S)
    best = tuple(arr)
    bestD = defect_short(p, best)
    for _ in range(samples):
        rng.shuffle(arr)
        cand = tuple(arr)
        d = defect_short(p, cand)
        if d < bestD:
            best = cand
            bestD = d
            if d[0] == 0:
                break
    return best


def iter_sets(p: int, size: int, max_sets: int, rng: random.Random, random_sets: bool) -> Iterator[Tuple[int, ...]]:
    universe = list(range(1, p))
    if random_sets:
        seen = set()
        attempts = 0
        while len(seen) < max_sets and attempts < 20 * max_sets:
            attempts += 1
            S = tuple(sorted(rng.sample(universe, size)))
            if S in seen:
                continue
            seen.add(S)
            yield S
    else:
        for idx, comb in enumerate(itertools.combinations(universe, size)):
            if idx >= max_sets:
                break
            yield comb


def analyze_order(p: int, S: Sequence[int], order: Sequence[int], max_traps: int) -> Optional[dict]:
    zis = zero_intervals(p, order)
    if not zis:
        return None
    min_len = min(length for _, _, length in zis)
    active = next(z for z in zis if z[2] == min_len)
    i, j, m = active
    Z = tuple(order[i:j])
    traps = pair_traps_inside_Z(p, Z)
    if not traps:
        return None

    oldD = defect_short(p, order)
    results = []
    for trap in traps[:max_traps]:
        moved = move_for_trap(order, i, trap)
        if moved is None:
            results.append({"trap": trap, "move": None})
            continue
        newD = defect_short(p, moved)
        results.append(
            {
                "trap": trap,
                "old_defect": oldD,
                "new_defect": newD,
                "improved": newD < oldD,
                "external_collision_change": has_external_collision_change(p, order, moved),
                "new_order": list(moved),
                "new_zero_intervals_min": [list(z) for z in zero_intervals(p, moved)[:10]],
            }
        )

    return {
        "p": p,
        "S": list(S),
        "sigma": sum(S) % p,
        "order": list(order),
        "partial_sums": partial_sums_extended(p, order),
        "defect": oldD,
        "active_zero_interval": {"i": i, "j": j, "length": m, "Z": list(Z)},
        "trap_count": len(traps),
        "results": results,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, default=13)
    ap.add_argument("--size", type=int, default=7)
    ap.add_argument("--max-sets", type=int, default=100)
    ap.add_argument("--order-samples", type=int, default=300)
    ap.add_argument("--max-traps", type=int, default=20)
    ap.add_argument("--random-sets", action="store_true")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", default="-")
    args = ap.parse_args()

    if not is_prime(args.p):
        raise SystemExit(f"ERROR: p must be prime, got {args.p}")
    if not (1 <= args.size <= args.p - 1):
        raise SystemExit("ERROR: size must be in [1,p-1]")

    rng = random.Random(args.seed)
    records = []
    for S in iter_sets(args.p, args.size, args.max_sets, rng, args.random_sets):
        if sum(S) % args.p == 0:
            continue
        order = find_best_sample_order(args.p, S, args.order_samples, rng)
        rec = analyze_order(args.p, S, order, args.max_traps)
        if rec is not None:
            records.append(rec)

    if args.out == "-":
        for rec in records:
            print(json.dumps(rec, separators=(",", ":")))
    else:
        with open(args.out, "w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec, separators=(",", ":")) + "\n")

    print(f"pair_trap_records={len(records)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
