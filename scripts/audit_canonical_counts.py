#!/usr/bin/env python3
"""Audit canonical B counts against combinatorial expectations.

Usage:
    audit_canonical_counts.py <file.jsonl> [file2.jsonl ...] --domain 17:3 --domain 19:3-5
"""

from __future__ import annotations

import argparse
import functools
import itertools
import json
from collections import defaultdict
from pathlib import Path


@functools.lru_cache(maxsize=None)
def canonical_scale(B: tuple[int, ...], p: int) -> tuple[int, ...]:
    if not B:
        return tuple()
    reps = []
    for lam in range(1, p):
        reps.append(tuple(sorted((lam * x) % p for x in B)))
    return min(reps)


@functools.lru_cache(maxsize=None)
def all_canonical_B(p: int, k: int) -> frozenset[tuple[int, ...]]:
    universe = list(range(1, p))
    out: set[tuple[int, ...]] = set()
    for comb in itertools.combinations(universe, k):
        out.add(canonical_scale(tuple(comb), p))
    return frozenset(out)


def parse_domain(text: str) -> tuple[int, range]:
    left, right = text.split(":", 1)
    p = int(left)
    if "-" in right:
        a, b = right.split("-", 1)
        return p, range(int(a), int(b) + 1)
    k = int(right)
    return p, range(k, k + 1)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("certificates", nargs="+", help="Minimal witness JSONL file(s)")
    ap.add_argument("--domain", action="append", default=[], help="Expected domain, e.g. 29:3-7. May repeat.")
    args = ap.parse_args()

    by_pk: dict[tuple[int, int], set[tuple[int, ...]]] = defaultdict(set)
    rows = 0

    for path_str in args.certificates:
        path = Path(path_str)
        if not path.exists():
            print(f"ERROR file not found: {path}")
            return 1
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rows += 1
                obj = json.loads(line)
                p = int(obj["p"])
                B = tuple(sorted(obj["B"]))
                can = canonical_scale(B, p)
                by_pk[(p, len(B))].add(can)

    print(f"total_rows={rows}")
    print()
    total_failures = 0

    for domain_text in args.domain:
        p, k_range = parse_domain(domain_text)
        for k in k_range:
            observed = by_pk.get((p, k), set())
            expected = set(all_canonical_B(p, k))
            missing = expected - observed
            extra = observed - expected
            status = "PASS" if not missing and not extra else "FAIL"
            if status == "FAIL":
                total_failures += 1
            print(f"domain p={p} |B|={k} expected={len(expected)} observed={len(observed)} "
                  f"missing={len(missing)} extra={len(extra)} {status}")

    print()
    if total_failures > 0:
        print(f"FAIL canonical count audit: {total_failures} domains with mismatches")
        return 1
    print("PASS canonical count audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
