#!/usr/bin/env python3
"""
Base finite checker for Erdős 475 / Graham's rearrangement problem.

This is intentionally weaker than endpoint avoidance.  It checks only the original
Graham-valid ordering condition:

  For A subset F_p^*, find an ordering whose nonempty partial sums are pairwise
  distinct mod p.

The checker can be used in two modes:

  1. Exhaustive canonical-complement search over declared finite domains.
  2. Witness verification from JSONL records.

JSONL witness format:

  {"p":29,"B":[1,2,5],"final_order":[...]}

where B = F_p^* \ A.
"""

from __future__ import annotations

import argparse
import itertools
import json
from functools import lru_cache
from typing import Dict, Iterable, Iterator, List, Optional, Sequence, Tuple


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


def parse_domain(text: str) -> Tuple[int, int, int]:
    left, right = text.split(":", 1)
    p = int(left)
    if "-" in right:
        lo, hi = right.split("-", 1)
        return p, int(lo), int(hi)
    r = int(right)
    return p, r, r


def canonical_scale_subset(p: int, subset: Sequence[int]) -> Tuple[int, ...]:
    vals = tuple(sorted(x % p for x in subset))
    best: Optional[Tuple[int, ...]] = None
    for lam in range(1, p):
        scaled = tuple(sorted((lam * x) % p for x in vals))
        if best is None or scaled < best:
            best = scaled
    assert best is not None
    return best


def canonical_complements(p: int, b_size: int) -> Iterator[Tuple[int, ...]]:
    seen = set()
    for comb in itertools.combinations(range(1, p), b_size):
        can = canonical_scale_subset(p, comb)
        if can in seen:
            continue
        seen.add(can)
        yield can


def partial_sums(p: int, order: Iterable[int]) -> List[int]:
    s = 0
    out: List[int] = []
    for x in order:
        s = (s + x) % p
        out.append(s)
    return out


def is_graham_valid_order(p: int, A: Sequence[int], order: Sequence[int]) -> bool:
    if sorted(x % p for x in order) != sorted(x % p for x in A):
        return False
    sums = partial_sums(p, order)
    return len(sums) == len(set(sums))


def find_graham_order(p: int, A: Sequence[int]) -> Optional[Tuple[int, ...]]:
    elems = tuple(sorted(x % p for x in A))
    n = len(elems)
    elem_to_bit = {x: 1 << i for i, x in enumerate(elems)}
    full = (1 << n) - 1

    # Try larger atoms first only as a mild heuristic.  The validity condition is exact.
    ordered_elems = tuple(sorted(elems, reverse=True))

    @lru_cache(maxsize=None)
    def dfs(used: int, current: int, seen: int) -> Optional[Tuple[int, ...]]:
        if used == full:
            return tuple()
        for x in ordered_elems:
            bit = elem_to_bit[x]
            if used & bit:
                continue
            nxt = (current + x) % p
            if seen & (1 << nxt):
                continue
            suffix = dfs(used | bit, nxt, seen | (1 << nxt))
            if suffix is not None:
                return (x,) + suffix
        return None

    return dfs(0, 0, 0)


def complement_to_A(p: int, B: Sequence[int]) -> Tuple[int, ...]:
    bset = {x % p for x in B}
    return tuple(x for x in range(1, p) if x not in bset)


def verify_witness_file(path: str, require_canonical: bool) -> int:
    ok = 0
    fail = 0
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            if not line.strip():
                continue
            rec = json.loads(line)
            p = int(rec["p"])
            B = tuple(int(x) for x in rec["B"])
            order = tuple(int(x) for x in rec["final_order"])
            if not is_prime(p):
                print(f"FAIL line={lineno}: p is not prime: {p}")
                fail += 1
                continue
            if require_canonical and tuple(sorted(B)) != canonical_scale_subset(p, B):
                print(f"FAIL line={lineno}: B is not canonical: {B}")
                fail += 1
                continue
            A = complement_to_A(p, B)
            if is_graham_valid_order(p, A, order):
                ok += 1
            else:
                print(f"FAIL line={lineno}: invalid witness p={p} B={B}")
                fail += 1
    print(f"witness_ok={ok}")
    print(f"witness_fail={fail}")
    return 0 if fail == 0 else 1


def exhaustive_domains(domains: Sequence[Tuple[int, int, int]], emit_witnesses: str | None) -> int:
    out = open(emit_witnesses, "w", encoding="utf-8") if emit_witnesses else None
    total = 0
    fail = 0
    try:
        for p, b_min, b_max in domains:
            if not is_prime(p):
                raise ValueError(f"p is not prime: {p}")
            for b_size in range(b_min, b_max + 1):
                for B in canonical_complements(p, b_size):
                    total += 1
                    A = complement_to_A(p, B)
                    order = find_graham_order(p, A)
                    if order is None:
                        print(f"FAIL p={p} B={B} |B|={b_size}")
                        fail += 1
                        continue
                    if out is not None:
                        out.write(json.dumps({"p": p, "B": list(B), "final_order": list(order)}, separators=(",", ":")) + "\n")
            print(f"p={p} b={b_min}-{b_max}: cumulative_total={total} cumulative_fail={fail}")
    finally:
        if out is not None:
            out.close()

    print(f"total_canonical_complements={total}")
    print(f"failures={fail}")
    print("VERDICT: PASS" if fail == 0 else "VERDICT: FAIL")
    return 0 if fail == 0 else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", action="append", default=[], help="Complement domain p:bmin-bmax, e.g. 29:3-7")
    ap.add_argument("--witness-jsonl", help="Verify an existing JSONL witness file")
    ap.add_argument("--emit-witnesses", help="Write witnesses found by exhaustive domain search")
    ap.add_argument("--require-canonical", action="store_true")
    args = ap.parse_args()

    if args.witness_jsonl:
        return verify_witness_file(args.witness_jsonl, require_canonical=args.require_canonical)

    domains = [parse_domain(x) for x in args.domain]
    if not domains:
        raise SystemExit("ERROR: provide --domain or --witness-jsonl")
    return exhaustive_domains(domains, emit_witnesses=args.emit_witnesses)


if __name__ == "__main__":
    raise SystemExit(main())
