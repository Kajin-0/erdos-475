#!/usr/bin/env python3
"""
Exhaustive small-prime checker for the single-forbidden endpoint-avoidance
strengthening used in the analytic proof notes.

Statement checked for primes p <= max_p:

For every A subset F_p^* and every f in F_p with f != sigma(A), there exists
an ordering of A such that:
  1. the nonempty partial sums are pairwise distinct;
  2. f is not one of the nonempty partial sums.

This is stronger than Graham's original rearrangement conjecture.
The checker is only a finite sanity/backtest tool; it is not a proof.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from typing import Iterable, List, Optional, Tuple


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


def subset_mask_to_tuple(p: int, mask: int) -> Tuple[int, ...]:
    return tuple(i for i in range(1, p) if mask & (1 << (i - 1)))


def find_endpoint_avoiding_order(
    p: int,
    A: Tuple[int, ...],
    forbidden: int,
) -> Optional[Tuple[int, ...]]:
    """Backtracking search for an endpoint-avoiding Graham ordering."""
    A = tuple(sorted(A))
    n = len(A)
    if n == 0:
        return tuple()

    elems = A
    elem_to_bit = {x: 1 << k for k, x in enumerate(elems)}
    full_mask = (1 << n) - 1

    @lru_cache(maxsize=None)
    def dfs(used_mask: int, current_sum: int, seen_mask: int) -> Optional[Tuple[int, ...]]:
        if used_mask == full_mask:
            return tuple()

        for x in elems:
            bit = elem_to_bit[x]
            if used_mask & bit:
                continue

            nxt = (current_sum + x) % p

            if nxt == forbidden:
                continue
            if seen_mask & (1 << nxt):
                continue

            suffix = dfs(used_mask | bit, nxt, seen_mask | (1 << nxt))
            if suffix is not None:
                return (x,) + suffix

        return None

    return dfs(0, 0, 0)


def partial_sums(p: int, order: Iterable[int]) -> List[int]:
    s = 0
    out = []
    for x in order:
        s = (s + x) % p
        out.append(s)
    return out


def check_order(p: int, A: Tuple[int, ...], forbidden: int, order: Tuple[int, ...]) -> bool:
    if sorted(order) != sorted(A):
        return False
    ps = partial_sums(p, order)
    return len(ps) == len(set(ps)) and forbidden not in ps


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-p", type=int, default=13)
    ap.add_argument("--stop-on-first-failure", action="store_true")
    ap.add_argument("--show-witnesses", action="store_true")
    args = ap.parse_args()

    total_instances = 0
    failures = []

    print("=== Endpoint-avoidance backtest ===")
    print(f"max_p={args.max_p}")
    print("Statement: for every A subset F_p^* and f != sigma(A),")
    print("there is a Graham-valid ordering avoiding f.")
    print()

    for p in primes_upto(args.max_p):
        prime_instances = 0
        prime_failures = 0
        nonempty_masks = range(1, 1 << (p - 1))

        for mask in nonempty_masks:
            A = subset_mask_to_tuple(p, mask)
            sigma = sum(A) % p

            for f in range(p):
                if f == sigma:
                    continue

                total_instances += 1
                prime_instances += 1

                order = find_endpoint_avoiding_order(p, A, f)
                if order is None or not check_order(p, A, f, order):
                    prime_failures += 1
                    failure = {
                        "p": p,
                        "A": A,
                        "sigma": sigma,
                        "forbidden": f,
                    }
                    failures.append(failure)
                    print(
                        "FAIL "
                        f"p={p} A={A} sigma={sigma} forbidden={f}"
                    )
                    if args.stop_on_first_failure:
                        print("VERDICT: FAIL")
                        return 1
                elif args.show_witnesses:
                    print(
                        f"PASS p={p} A={A} sigma={sigma} forbidden={f} "
                        f"order={order} partial_sums={partial_sums(p, order)}"
                    )

        print(
            f"p={p}: instances={prime_instances} "
            f"failures={prime_failures} status={'PASS' if prime_failures == 0 else 'FAIL'}"
        )

    print()
    print(f"total_instances={total_instances}")
    print(f"failures={len(failures)}")
    print("VERDICT: PASS" if not failures else "VERDICT: FAIL")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
