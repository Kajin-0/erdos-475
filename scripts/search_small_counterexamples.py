#!/usr/bin/env python3
"""Exhaustive small-prime counterexample search for Erdős 475.

For each prime p up to --max-prime, this script enumerates subsets
A subset F_p^* subject to size/complement filters and searches for a
Graham-valid ordering by backtracking.

This is intended as a small-prime sanity check and disproof detector.  It is not
intended to replace the certificate machinery for large finite domains.
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(frozen=True)
class SearchResult:
    p: int
    A: tuple[int, ...]
    found: bool
    ordering: tuple[int, ...] | None
    nodes: int

    @property
    def b_size(self) -> int:
        return self.p - 1 - len(self.A)


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


def primes_upto(n: int) -> list[int]:
    return [p for p in range(2, n + 1) if is_prime(p)]


def parse_range(text: str | None, default_min: int, default_max: int) -> tuple[int, int]:
    if text is None:
        return default_min, default_max
    text = text.strip()
    if ".." in text:
        a, b = text.split("..", 1)
        return int(a), int(b)
    v = int(text)
    return v, v


def canonical_scale_subset(A: Sequence[int], p: int) -> tuple[int, ...]:
    values = tuple(sorted(x % p for x in A))
    if not values:
        return values
    candidates = []
    for lam in range(1, p):
        candidates.append(tuple(sorted((lam * x) % p for x in values)))
    return min(candidates)


def valid_order_backtrack(A: Sequence[int], p: int, node_limit: int | None = None) -> tuple[tuple[int, ...] | None, int]:
    values = tuple(sorted(A))
    used = [False] * len(values)
    order: list[int] = []
    seen_sums: set[int] = set()
    nodes = 0

    # Simple deterministic heuristic: try larger elements after smaller ones alternate by residue.
    indices = list(range(len(values)))

    def dfs(current_sum: int) -> tuple[int, ...] | None:
        nonlocal nodes
        if node_limit is not None and nodes >= node_limit:
            return None
        nodes += 1
        if len(order) == len(values):
            return tuple(order)

        for idx in indices:
            if used[idx]:
                continue
            x = values[idx]
            new_sum = (current_sum + x) % p
            if new_sum in seen_sums:
                continue
            used[idx] = True
            order.append(x)
            seen_sums.add(new_sum)
            out = dfs(new_sum)
            if out is not None:
                return out
            seen_sums.remove(new_sum)
            order.pop()
            used[idx] = False
        return None

    return dfs(0), nodes


def subset_iterator(p: int, t_min: int, t_max: int, b_min: int | None, b_max: int | None, canonical_only: bool) -> Iterable[tuple[int, ...]]:
    universe = tuple(range(1, p))
    seen: set[tuple[int, ...]] = set()
    for t in range(t_min, t_max + 1):
        if t < 0 or t > p - 1:
            continue
        b = p - 1 - t
        if b_min is not None and b < b_min:
            continue
        if b_max is not None and b > b_max:
            continue
        for A in itertools.combinations(universe, t):
            if canonical_only:
                key = canonical_scale_subset(A, p)
                if key in seen:
                    continue
                seen.add(key)
            yield tuple(A)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-prime", type=int, default=13)
    ap.add_argument("--t-range", default=None, help="Subset-size range, e.g. 1..8")
    ap.add_argument("--b-range", default=None, help="Complement-size range, e.g. 3..7")
    ap.add_argument("--canonical-only", action="store_true", help="Only test one multiplicative-scaling representative")
    ap.add_argument("--node-limit", type=int, default=None)
    ap.add_argument("--stop-on-counterexample", action="store_true")
    ap.add_argument("--jsonl-out", default=None)
    args = ap.parse_args()

    out_fh = None
    if args.jsonl_out:
        out_path = Path(args.jsonl_out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_fh = out_path.open("w", encoding="utf-8")

    total = 0
    solved = 0
    failed = 0
    timed_out_or_limited = 0
    counterexamples: list[SearchResult] = []

    for p in primes_upto(args.max_prime):
        t_min, t_max = parse_range(args.t_range, 1, p - 1)
        b_min = b_max = None
        if args.b_range:
            b_min, b_max = parse_range(args.b_range, 0, p - 1)
        for A in subset_iterator(p, t_min, t_max, b_min, b_max, args.canonical_only):
            total += 1
            ordering, nodes = valid_order_backtrack(A, p, node_limit=args.node_limit)
            limited = args.node_limit is not None and ordering is None and nodes >= args.node_limit
            if ordering is not None:
                solved += 1
            elif limited:
                timed_out_or_limited += 1
            else:
                failed += 1
                counterexamples.append(SearchResult(p=p, A=A, found=False, ordering=None, nodes=nodes))

            row = {
                "p": p,
                "A": list(A),
                "t": len(A),
                "b": p - 1 - len(A),
                "found": ordering is not None,
                "ordering": list(ordering) if ordering is not None else None,
                "nodes": nodes,
                "node_limited": limited,
            }
            if out_fh:
                out_fh.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")

            if failed and args.stop_on_counterexample:
                break
        if failed and args.stop_on_counterexample:
            break

    if out_fh:
        out_fh.close()

    print("=== Small-prime counterexample search ===")
    print(f"max_prime={args.max_prime}")
    print(f"total={total}")
    print(f"solved={solved}")
    print(f"failed={failed}")
    print(f"node_limited={timed_out_or_limited}")
    if counterexamples:
        print("COUNTEREXAMPLE_CANDIDATES")
        for r in counterexamples[:20]:
            print(json.dumps({"p": r.p, "A": list(r.A), "t": len(r.A), "b": r.b_size, "nodes": r.nodes}, sort_keys=True))
        print("VERDICT: counterexample candidates found or search incomplete")
    elif timed_out_or_limited:
        print("VERDICT: no counterexamples found, but some searches hit the node limit")
    else:
        print("VERDICT: no counterexamples found in searched domain")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
