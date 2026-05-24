#!/usr/bin/env python3
"""
Low-compute obstruction miner for the Erdős 475 analytic sprint.

This script is not a proof engine.  It generates small examples and records the
algebraic equations produced when simple one-atom insertion moves fail.

Output is intended for AI/human inspection:

  q = P_u - P_v mod p

where q is the moved outside atom, P_u is an affected old partial sum, and P_v is
an old unaffected partial sum causing a collision.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
from dataclasses import dataclass
from typing import Iterable, Iterator, List, Optional, Sequence, Tuple


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


def primes_upto(n: int) -> List[int]:
    return [p for p in range(2, n + 1) if is_prime(p)]


def partial_sums_extended(p: int, order: Sequence[int]) -> List[int]:
    s = 0
    out = [0]
    for x in order:
        s = (s + x) % p
        out.append(s)
    return out


def zero_intervals(p: int, order: Sequence[int]) -> List[Tuple[int, int, int]]:
    """Return zero intervals as (i,j,length) with P_i=P_j and 0<=i<j<=t."""
    P = partial_sums_extended(p, order)
    out: List[Tuple[int, int, int]] = []
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            if P[i] == P[j]:
                out.append((i, j, j - i))
    return out


def collision_excess(p: int, order: Sequence[int]) -> int:
    P = partial_sums_extended(p, order)
    return len(P) - len(set(P))


def defect_tuple(p: int, order: Sequence[int]) -> Tuple[int, Tuple[int, ...], int, int]:
    P = partial_sums_extended(p, order)
    counts = {}
    for x in P:
        counts[x] = counts.get(x, 0) + 1
    excess = len(P) - len(counts)
    profile = tuple(sorted((c for c in counts.values() if c > 1), reverse=True))
    zis = zero_intervals(p, order)
    if not zis:
        k_min = 0
        n_min = 0
    else:
        l_min = min(z[2] for z in zis)
        k_min = len(order) + 1 - l_min
        n_min = sum(1 for z in zis if z[2] == l_min)
    return (excess, profile, k_min, n_min)


def one_atom_insert(order: Sequence[int], src: int, dst_before: int) -> Tuple[int, ...]:
    """Remove atom at index src and insert it before index dst_before in the shortened list.

    Indices are 0-based atom indices.  dst_before is interpreted in the original
    coordinate if src < dst_before by the usual remove-then-insert convention.
    """
    arr = list(order)
    q = arr.pop(src)
    if src < dst_before:
        dst_before -= 1
    arr.insert(dst_before, q)
    return tuple(arr)


def changed_partial_indices_for_right_move(src: int, dst_before: int) -> range:
    """Partial-sum indices affected by moving src right before dst_before.

    Atom index src moves across atoms src+1 ... dst_before-1.  Extended partial
    sums with indices src+1 ... dst_before-1 are shifted by -q.  The endpoint
    dst_before is unchanged.
    """
    return range(src + 1, dst_before)


def changed_partial_indices_for_left_move(src: int, dst_before: int) -> range:
    """Partial-sum indices affected by moving src left before dst_before.

    Atom index src moves left across atoms dst_before ... src-1. Extended partial
    sums with indices dst_before ... src are shifted by +q.
    """
    return range(dst_before, src + 1)


def collision_equations_for_move(p: int, order: Sequence[int], src: int, dst_before: int) -> List[dict]:
    oldP = partial_sums_extended(p, order)
    q = order[src]
    new_order = one_atom_insert(order, src, dst_before)
    newP = partial_sums_extended(p, new_order)

    old_value_to_indices = {}
    for idx, val in enumerate(oldP):
        old_value_to_indices.setdefault(val, []).append(idx)

    equations: List[dict] = []

    # Identify changed extended partial-sum positions in old coordinates.
    if dst_before > src:
        changed = set(changed_partial_indices_for_right_move(src, dst_before))
        shift = -q % p
    elif dst_before < src:
        changed = set(changed_partial_indices_for_left_move(src, dst_before))
        shift = q % p
    else:
        return []

    unchanged = set(range(len(oldP))) - changed

    # For each shifted old partial sum, detect collisions with old unchanged values.
    for u in sorted(changed):
        shifted = (oldP[u] + shift) % p
        for v in sorted(unchanged):
            if shifted == oldP[v]:
                equations.append(
                    {
                        "q": q,
                        "u": u,
                        "v": v,
                        "P_u": oldP[u],
                        "P_v": oldP[v],
                        "equation": f"{q} = P_{u} - P_{v} mod {p}" if dst_before > src else f"{q} = P_{v} - P_{u} mod {p}",
                        "direction": "right" if dst_before > src else "left",
                    }
                )

    # Sanity: report whether the new order improved the defect.
    oldD = defect_tuple(p, order)
    newD = defect_tuple(p, new_order)
    for e in equations:
        e["old_defect"] = oldD
        e["new_defect"] = newD
        e["improved"] = newD < oldD
    return equations


def find_best_sample_order(p: int, S: Sequence[int], samples: int, rng: random.Random) -> Tuple[int, ...]:
    best = tuple(S)
    bestD = defect_tuple(p, best)
    arr = list(S)
    for _ in range(samples):
        rng.shuffle(arr)
        cand = tuple(arr)
        d = defect_tuple(p, cand)
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
        while len(seen) < max_sets and attempts < max_sets * 20:
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


def mine_for_set(p: int, S: Sequence[int], order_samples: int, rng: random.Random) -> Optional[dict]:
    if sum(S) % p == 0:
        return None
    order = find_best_sample_order(p, S, order_samples, rng)
    zis = zero_intervals(p, order)
    if not zis:
        return None
    min_len = min(z[2] for z in zis)
    active = [z for z in zis if z[2] == min_len][0]
    i, j, ell = active

    moves = []

    # Atom immediately before active interval: atom index i-1, move right into/through interval.
    if i > 0:
        src = i - 1
        for dst_before in range(i + 1, j + 1):
            eqs = collision_equations_for_move(p, order, src, dst_before)
            new_order = one_atom_insert(order, src, dst_before)
            moves.append(
                {
                    "src": src,
                    "dst_before": dst_before,
                    "q": order[src],
                    "direction": "right_into_Z",
                    "old_defect": defect_tuple(p, order),
                    "new_defect": defect_tuple(p, new_order),
                    "equations": eqs,
                }
            )

    # Atom immediately after active interval: atom index j, move left into interval.
    if j < len(order):
        src = j
        for dst_before in range(i + 1, j + 1):
            eqs = collision_equations_for_move(p, order, src, dst_before)
            new_order = one_atom_insert(order, src, dst_before)
            moves.append(
                {
                    "src": src,
                    "dst_before": dst_before,
                    "q": order[src],
                    "direction": "left_into_Z",
                    "old_defect": defect_tuple(p, order),
                    "new_defect": defect_tuple(p, new_order),
                    "equations": eqs,
                }
            )

    return {
        "p": p,
        "S": list(S),
        "sigma": sum(S) % p,
        "order": list(order),
        "partial_sums": partial_sums_extended(p, order),
        "defect": defect_tuple(p, order),
        "active_zero_interval": {"i": i, "j": j, "length": ell, "block": list(order[i:j])},
        "moves": moves,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, default=11)
    ap.add_argument("--size", type=int, default=6)
    ap.add_argument("--max-sets", type=int, default=50)
    ap.add_argument("--order-samples", type=int, default=200)
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
        rec = mine_for_set(args.p, S, args.order_samples, rng)
        if rec is not None:
            records.append(rec)

    if args.out == "-":
        for rec in records:
            print(json.dumps(rec, separators=(",", ":")))
    else:
        with open(args.out, "w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec, separators=(",", ":")) + "\n")

    print(f"mined_records={len(records)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
