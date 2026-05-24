#!/usr/bin/env python3
"""
Low-compute classifier for external-bridge obstruction in the Erdős 475 analytic sprint.

This script is not a proof engine. It mines proof-relevant shortest-zero-interval
examples and classifies q-through-Z insertion attempts.

For an ordering R and a shortest zero interval

    Z = z_1 ... z_m

with adjacent outside atom q on the right or left, the script tries useful
insertions of q into Z and classifies the obstruction pattern.

Right-adjacent model:

    R = X Z q Y

with internal prefixes T_0=0, T_b=z_1+...+z_b, T_m=0. Inserting q after z_k
has local endpoints

    {T_0,...,T_k} union {q+T_k,...,q+T_m}.

Obstruction classes:

    CLEAN_DESCENT              new D_short is smaller
    CLEAN_NO_DESCENT           no detected local/external blocker but no descent
    SIGNED_INTERVAL            local cross-side collision T_a = q+T_b
    RIGHT_TERMINAL_BRIDGE      only/primary bridge at b=m-1 to the side of q
    LEFT_TERMINAL_BRIDGE       terminal-like bridge to the opposite side
    DISTRIBUTED_BRIDGE         two or more non-boundary bridge indices
    EXTERNAL_BRIDGE            one nonterminal external bridge index
    MIXED                      multiple branches appear simultaneously

Important filter:

    --min-active-length 3

skips examples whose shortest zero interval has length 2. Length-2 intervals are
inverse pairs and form a special terminal-bridge branch, not the true distributed
overlap hard case.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
from collections import Counter, defaultdict
from typing import Iterator, List, Sequence, Tuple

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
    out = []
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


def prefix_sums_block(p: int, block: Sequence[int]) -> List[int]:
    s = 0
    T = [0]
    for x in block:
        s = (s + x) % p
        T.append(s)
    return T


def insert_atom(order: Sequence[int], src: int, dst_before: int) -> Tuple[int, ...]:
    arr = list(order)
    q = arr.pop(src)
    if src < dst_before:
        dst_before -= 1
    arr.insert(dst_before, q)
    return tuple(arr)


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
        E, L, N, _M = defect_short(p, cand)
        score = (E, L, N)
        scored.append((score, cand))
    scored.sort()
    return [cand for _score, cand in scored[:limit]]


def external_indices_for_window(n_atoms: int, z_i: int, z_j: int, q_index: int) -> set[int]:
    local = set(range(z_i, z_j + 1))
    local.add(q_index + 1)
    return set(range(n_atoms + 1)) - local


def classify_right_insertion(p: int, order: Sequence[int], z_i: int, z_j: int, k: int) -> dict:
    n = len(order)
    m = z_j - z_i
    q_index = z_j
    q = order[q_index]
    Z = order[z_i:z_j]
    T = prefix_sums_block(p, Z)
    P = partial_sums_extended(p, order)
    base = P[z_i]

    new_order = insert_atom(order, q_index, z_i + k)
    oldD = defect_short(p, order)
    newD = defect_short(p, new_order)

    signed = []
    external = []
    ext_indices = external_indices_for_window(n, z_i, z_j, q_index)
    ext_value_to_indices = defaultdict(list)
    for idx in ext_indices:
        ext_value_to_indices[P[idx]].append(idx)

    for a in range(0, k + 1):
        for b in range(k, m):
            if T[a] % p == (q + T[b]) % p:
                signed.append({"a": a, "b": b, "value": (base + T[a]) % p})

    for b in range(k, m):
        val = (base + q + T[b]) % p
        if val in ext_value_to_indices:
            side_counts = Counter("left" if idx < z_i else "right" for idx in ext_value_to_indices[val])
            external.append({"b": b, "value": val, "indices": ext_value_to_indices[val], "side_counts": dict(side_counts)})

    bset = sorted({e["b"] for e in external})
    terminal = [e for e in external if e["b"] == m - 1]
    nonterminal = [e for e in external if e["b"] != m - 1]

    branch_flags = []
    if newD < oldD:
        branch_flags.append("CLEAN_DESCENT")
    if signed:
        branch_flags.append("SIGNED_INTERVAL")
    if len(bset) >= 2:
        branch_flags.append("DISTRIBUTED_BRIDGE")
    elif nonterminal:
        branch_flags.append("EXTERNAL_BRIDGE")
    elif terminal:
        side_counts = Counter()
        for e in terminal:
            side_counts.update(e["side_counts"])
        if side_counts.get("right", 0) and not side_counts.get("left", 0):
            branch_flags.append("RIGHT_TERMINAL_BRIDGE")
        elif side_counts.get("left", 0) and not side_counts.get("right", 0):
            branch_flags.append("LEFT_TERMINAL_BRIDGE")
        else:
            branch_flags.append("MIXED_TERMINAL_BRIDGE")

    if not branch_flags:
        if newD == oldD:
            branch_flags.append("CLEAN_NO_DESCENT")
        else:
            branch_flags.append("WORSE_UNCLASSIFIED")

    if "CLEAN_DESCENT" in branch_flags and len(branch_flags) == 1:
        label = "CLEAN_DESCENT"
    elif len(branch_flags) == 1:
        label = branch_flags[0]
    else:
        label = "MIXED"

    return {
        "side": "right",
        "k": k,
        "q": q,
        "old_defect": oldD,
        "new_defect": newD,
        "label": label,
        "branch_flags": branch_flags,
        "signed": signed,
        "external": external,
        "bridge_indices": bset,
        "new_order": list(new_order),
    }


def classify_left_by_reversal(p: int, order: Sequence[int], z_i: int, z_j: int, k: int) -> dict:
    n = len(order)
    rev = tuple(reversed(order))
    rz_i = n - z_j
    rz_j = n - z_i
    rec = classify_right_insertion(p, rev, rz_i, rz_j, k)
    rec["side"] = "left_via_reversal"
    rec["new_order_reversed_back"] = list(reversed(rec["new_order"]))
    return rec


def analyze_order(p: int, S: Sequence[int], order: Sequence[int], max_intervals: int, min_active_length: int) -> dict | None:
    zis = zero_intervals(p, order)
    if not zis:
        return None
    L_min = min(length for _, _, length in zis)
    if L_min < min_active_length:
        return None

    active_intervals = [(i, j, length) for i, j, length in zis if length == L_min]
    records = []

    for z_i, z_j, m in active_intervals[:max_intervals]:
        Z = order[z_i:z_j]
        interval_rec = {
            "i": z_i,
            "j": z_j,
            "length": m,
            "Z": list(Z),
            "right_q": None,
            "left_q": None,
        }
        if z_j < len(order):
            attempts = [classify_right_insertion(p, order, z_i, z_j, k) for k in range(1, m)]
            interval_rec["right_q"] = {
                "q": order[z_j],
                "attempts": attempts,
                "label_counts": dict(Counter(a["label"] for a in attempts)),
                "flag_counts": dict(Counter(flag for a in attempts for flag in a["branch_flags"])),
            }
        if z_i > 0:
            attempts = [classify_left_by_reversal(p, order, z_i, z_j, k) for k in range(1, m)]
            interval_rec["left_q"] = {
                "q": order[z_i - 1],
                "attempts": attempts,
                "label_counts": dict(Counter(a["label"] for a in attempts)),
                "flag_counts": dict(Counter(flag for a in attempts for flag in a["branch_flags"])),
            }
        records.append(interval_rec)

    all_attempts = []
    for r in records:
        for side_key in ("right_q", "left_q"):
            if r[side_key] is not None:
                all_attempts.extend(r[side_key]["attempts"])

    if not all_attempts:
        return None

    return {
        "p": p,
        "S": list(S),
        "sigma": sum(S) % p,
        "order": list(order),
        "partial_sums": partial_sums_extended(p, order),
        "defect": defect_short(p, order),
        "active_shortest_length": L_min,
        "interval_records": records,
        "attempt_label_counts": dict(Counter(a["label"] for a in all_attempts)),
        "attempt_flag_counts": dict(Counter(flag for a in all_attempts for flag in a["branch_flags"])),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=int, default=17)
    ap.add_argument("--size", type=int, default=9)
    ap.add_argument("--max-sets", type=int, default=200)
    ap.add_argument("--order-samples", type=int, default=1000)
    ap.add_argument("--orders-per-set", type=int, default=10)
    ap.add_argument("--max-intervals", type=int, default=5)
    ap.add_argument("--min-active-length", type=int, default=2)
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
    sets_seen = 0
    orders_tested = 0
    skipped_short_active = 0
    aggregate_labels = Counter()
    aggregate_flags = Counter()

    for S in iter_sets(args.p, args.size, args.max_sets, rng, args.random_sets):
        sets_seen += 1
        if sum(S) % args.p == 0:
            continue
        for order in sample_defective_orders(args.p, S, args.order_samples, rng, args.orders_per_set):
            orders_tested += 1
            rec = analyze_order(args.p, S, order, args.max_intervals, args.min_active_length)
            if rec is None:
                zis = zero_intervals(args.p, order)
                if zis and min(length for _, _, length in zis) < args.min_active_length:
                    skipped_short_active += 1
                continue
            records.append(rec)
            aggregate_labels.update(rec["attempt_label_counts"])
            aggregate_flags.update(rec["attempt_flag_counts"])

    if args.out == "-":
        for rec in records:
            print(json.dumps(rec, separators=(",", ":")))
    else:
        with open(args.out, "w", encoding="utf-8") as f:
            for rec in records:
                f.write(json.dumps(rec, separators=(",", ":")) + "\n")

    print(f"sets_seen={sets_seen}", flush=True)
    print(f"orders_tested={orders_tested}", flush=True)
    print(f"skipped_short_active={skipped_short_active}", flush=True)
    print(f"external_bridge_records={len(records)}", flush=True)
    print("aggregate_labels=" + json.dumps(dict(aggregate_labels), sort_keys=True), flush=True)
    print("aggregate_flags=" + json.dumps(dict(aggregate_flags), sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
