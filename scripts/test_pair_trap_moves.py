#!/usr/bin/env python3
"""
Low-compute tester for pair-trap block moves in the Erdős 475 analytic sprint.

This script does not attempt to prove Erdős 475.  It searches small prime examples
for zero intervals Z containing equal-interval-sum pair traps, classifies the trap
geometry, applies the natural block move, and reports whether the working short-
defect D_short improves or whether failures are accompanied by external collisions.

Important mode distinction:

  --order-mode best
      tries to find a low-defect / possibly collision-free ordering.  This is good
      for theorem search but often produces no obstruction records.

  --order-mode defective
      deliberately keeps sampled defective orderings.  This is better for mining
      obstruction patterns and is the recommended mode for this script.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
from collections import Counter
from typing import Iterator, List, Optional, Sequence, Tuple

INF = 10**9
SUPPORTED_TYPES = {"disjoint", "crossing", "nested"}


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
    i, j, k, l = trap["i"], trap["j"], trap["k"], trap["l"]
    typ = trap["type"]

    if k < i:
        i, j, k, l = k, l, i, j

    z0 = z_start

    if typ == "disjoint":
        A = order[z0 + i : z0 + j]
        M = order[z0 + j : z0 + k]
        B = order[z0 + k : z0 + l]
        return replace_block(order, z0 + i, z0 + l, tuple(B) + tuple(M) + tuple(A))

    if typ == "crossing":
        A = order[z0 + i : z0 + k]
        Bmid = order[z0 + k : z0 + j]
        C = order[z0 + j : z0 + l]
        return replace_block(order, z0 + i, z0 + l, tuple(C) + tuple(Bmid) + tuple(A))

    if typ == "nested":
        A = order[z0 + i : z0 + k]
        Bmid = order[z0 + k : z0 + l]
        C = order[z0 + l : z0 + j]
        return replace_block(order, z0 + i, z0 + j, tuple(A) + tuple(C) + tuple(Bmid))

    return None


def changed_indices(old: Sequence[int], new: Sequence[int]) -> Tuple[int, int]:
    n = len(old)
    lo = 0
    while lo < n and old[lo] == new[lo]:
        lo += 1
    hi = n
    while hi > lo and old[hi - 1] == new[hi - 1]:
        hi -= 1
    return lo, hi


def has_external_collision_change(p: int, old: Sequence[int], new: Sequence[int]) -> bool:
    lo_atom, hi_atom = changed_indices(old, new)
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


def result_kind(result: dict) -> str:
    if result.get("move") is None:
        return "unsupported"
    if result.get("improved") is True:
        return "improved"
    if result.get("external_collision_change") is True:
        return "external_only"
    return "danger"


def summarize_results(results: Sequence[dict]) -> dict:
    counts = Counter(result_kind(r) for r in results)
    supported = sum(1 for r in results if r.get("trap", {}).get("type") in SUPPORTED_TYPES)
    trap_types = Counter(r.get("trap", {}).get("type", "unknown") for r in results)
    return {
        "supported_results": supported,
        "improved": counts.get("improved", 0),
        "external_only": counts.get("external_only", 0),
        "danger": counts.get("danger", 0),
        "unsupported": counts.get("unsupported", 0),
        "trap_result_type_counts": dict(trap_types),
    }


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


def sample_defective_orders(p: int, S: Sequence[int], samples: int, rng: random.Random, limit: int) -> List[Tuple[int, ...]]:
    arr = list(S)
    scored: list[tuple[tuple[int, int, int], Tuple[int, ...]]] = []
    seen = set()
    for _ in range(samples):
        rng.shuffle(arr)
        cand = tuple(arr)
        if cand in seen:
            continue
        seen.add(cand)
        zis = zero_intervals(p, cand)
        if not zis:
            continue
        D = defect_short(p, cand)
        E, L, N, _M = D
        score = (-E, -L, -N)
        scored.append((score, cand))
    scored.sort()
    return [cand for _score, cand in scored[:limit]]


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


def analyze_order(p: int, S: Sequence[int], order: Sequence[int], max_traps: int, *, active_mode: str) -> Optional[dict]:
    zis = zero_intervals(p, order)
    if not zis:
        return None

    if active_mode == "shortest":
        target_len = min(length for _, _, length in zis)
    elif active_mode == "longest":
        target_len = max(length for _, _, length in zis)
    else:
        raise ValueError(f"unknown active_mode: {active_mode}")

    active_candidates = [z for z in zis if z[2] == target_len]

    best_record = None
    best_trap_count = 0
    for active in active_candidates:
        i, j, m = active
        Z = tuple(order[i:j])
        traps = pair_traps_inside_Z(p, Z)
        if len(traps) > best_trap_count:
            best_trap_count = len(traps)
            best_record = (i, j, m, Z, traps)

    if best_record is None or best_trap_count == 0:
        return None

    i, j, m, Z, traps = best_record
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
                "new_zero_intervals_first10": [list(z) for z in zero_intervals(p, moved)[:10]],
            }
        )

    summary = summarize_results(results)

    return {
        "p": p,
        "S": list(S),
        "sigma": sum(S) % p,
        "order": list(order),
        "partial_sums": partial_sums_extended(p, order),
        "defect": oldD,
        "active_mode": active_mode,
        "active_zero_interval": {"i": i, "j": j, "length": m, "Z": list(Z)},
        "trap_count": len(traps),
        "trap_type_counts": dict(Counter(t["type"] for t in traps)),
        "summary": summary,
        "results": results,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, default=13)
    ap.add_argument("--size", type=int, default=7)
    ap.add_argument("--max-sets", type=int, default=100)
    ap.add_argument("--order-samples", type=int, default=300)
    ap.add_argument("--orders-per-set", type=int, default=5)
    ap.add_argument("--max-traps", type=int, default=20)
    ap.add_argument("--random-sets", action="store_true")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", default="-")
    ap.add_argument("--order-mode", choices=["best", "defective"], default="defective")
    ap.add_argument("--active-mode", choices=["shortest", "longest"], default="longest")
    args = ap.parse_args()

    if not is_prime(args.p):
        raise SystemExit(f"ERROR: p must be prime, got {args.p}")
    if not (1 <= args.size <= args.p - 1):
        raise SystemExit("ERROR: size must be in [1,p-1]")

    rng = random.Random(args.seed)
    records = []
    sets_seen = 0
    orders_tested = 0
    aggregate = Counter()
    for S in iter_sets(args.p, args.size, args.max_sets, rng, args.random_sets):
        sets_seen += 1
        if sum(S) % args.p == 0:
            continue

        if args.order_mode == "best":
            candidate_orders = [find_best_sample_order(args.p, S, args.order_samples, rng)]
        else:
            candidate_orders = sample_defective_orders(args.p, S, args.order_samples, rng, args.orders_per_set)

        for order in candidate_orders:
            orders_tested += 1
            rec = analyze_order(args.p, S, order, args.max_traps, active_mode=args.active_mode)
            if rec is not None:
                records.append(rec)
                aggregate.update({k: v for k, v in rec["summary"].items() if isinstance(v, int)})

    if args.out == "-":
        for rec in records:
            print(json.dumps(rec, separators=(",", ":")))
    else:
        with open(args.out, "w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec, separators=(",", ":")) + "\n")

    print(f"sets_seen={sets_seen}", flush=True)
    print(f"orders_tested={orders_tested}", flush=True)
    print(f"pair_trap_records={len(records)}", flush=True)
    print("aggregate=" + json.dumps(dict(aggregate), sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
