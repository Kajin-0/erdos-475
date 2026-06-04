#!/usr/bin/env python3
"""Audit canonical B counts against combinatorial expectations.

Tracks:
  - total rows
  - raw B rows
  - canonical representatives
  - duplicate canonical representatives
  - noncanonical B (if --require-canonical)
  - malformed rows

Reports:
  - expected canonical count
  - observed canonical count
  - duplicate canonical count
  - noncanonical row count
  - missing canonical representatives
  - extra canonical representatives

Usage:
    audit_canonical_counts.py <file.jsonl> [file2.jsonl ...] --domain 17:3 --domain 19:3-5
"""

from __future__ import annotations

import argparse
import functools
import itertools
import json
import sys
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
    ap.add_argument("--require-canonical", action="store_true", help="Reject noncanonical B entries")
    ap.add_argument("--json", action="store_true", help="Output results as JSON")
    args = ap.parse_args()

    # (p, k) -> set of canonical representatives
    by_pk: dict[tuple[int, int], set[tuple[int, ...]]] = defaultdict(set)
    # Track raw counts
    total_rows = 0
    noncanonical_rows = 0
    malformed_rows = 0
    duplicate_canonical_count = 0
    # Track raw B keys per (p, B_canonical)
    canonical_seen: dict[tuple[int, tuple[int, ...]], int] = defaultdict(int)

    for path_str in args.certificates:
        path = Path(path_str)
        if not path.exists():
            msg = f"ERROR file not found: {path}"
            if args.json:
                print(json.dumps({"pass": False, "error": msg}))
            else:
                print(msg)
            return 1
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                total_rows += 1
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    malformed_rows += 1
                    continue

                try:
                    p = int(obj["p"])
                    B = tuple(sorted(obj["B"]))
                except (KeyError, TypeError, ValueError):
                    malformed_rows += 1
                    continue

                if len(B) != len(set(B)):
                    malformed_rows += 1
                    continue

                can = canonical_scale(B, p)

                if args.require_canonical and B != can:
                    noncanonical_rows += 1
                    continue

                key = (p, can)
                canonical_seen[key] += 1
                if canonical_seen[key] > 1:
                    duplicate_canonical_count += 1

                by_pk[(p, len(B))].add(can)

    failures = []
    domains_output: list[dict] = []

    for domain_text in args.domain:
        p, k_range = parse_domain(domain_text)
        for k in k_range:
            observed = by_pk.get((p, k), set())
            expected_can = all_canonical_B(p, k)
            missing = expected_can - observed
            extra = observed - expected_can
            n_expected = len(expected_can)
            n_observed = len(observed)
            status = "PASS" if not missing and not extra else "FAIL"
            if status == "FAIL":
                failures.append(f"p={p} |B|={k}")
            entry = {
                "p": p,
                "k": k,
                "expected": n_expected,
                "observed": n_observed,
                "missing": len(missing),
                "extra": len(extra),
                "status": status,
            }
            domains_output.append(entry)
            if not args.json:
                print(f"domain p={p} |B|={k} "
                      f"expected={n_expected} observed={n_observed} "
                      f"missing={len(missing)} extra={len(extra)} {status}")

    if args.json:
        print(json.dumps({
            "pass": len(failures) == 0 and malformed_rows == 0,
            "total_rows": total_rows,
            "noncanonical_rows": noncanonical_rows,
            "malformed_rows": malformed_rows,
            "duplicate_canonical_count": duplicate_canonical_count,
            "domains": domains_output,
            "failures": failures,
        }))
    else:
        print()
        print(f"total_rows={total_rows}")
        print(f"noncanonical_rows={noncanonical_rows}")
        print(f"malformed_rows={malformed_rows}")
        print(f"duplicate_canonical_count={duplicate_canonical_count}")

    if malformed_rows > 0:
        if not args.json:
            print(f"FAIL: {malformed_rows} malformed row(s)")
        return 1

    if args.require_canonical and noncanonical_rows > 0:
        if not args.json:
            print(f"FAIL: {noncanonical_rows} noncanonical row(s)")
        return 1

    if duplicate_canonical_count > 0:
        if not args.json:
            print(f"FAIL: {duplicate_canonical_count} duplicate canonical representatives")
        return 1

    if failures:
        if not args.json:
            print(f"FAIL canonical count audit: {len(failures)} domain(s) with mismatches: {failures}")
        return 1

    if not args.json:
        print("PASS canonical count audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
