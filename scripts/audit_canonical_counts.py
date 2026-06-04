#!/usr/bin/env python3
"""Audit canonical B counts against combinatorial expectations.

Independently validates each row:
  - root value must be a JSON object
  - p must be a strict integer (not bool)
  - p must be prime
  - B must be a list of strict integers
  - B must be a subset of F_p^* (no 0, no p)
  - B must not contain duplicates

Tracks:
  - total rows
  - malformed rows
  - noncanonical B (if --require-canonical)
  - duplicate canonical representatives
  - per-domain expected vs observed

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
from math import isqrt
from pathlib import Path
from typing import Any


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    r = isqrt(n)
    f = 3
    while f <= r:
        if n % f == 0:
            return False
        f += 2
    return True


def is_strict_int(val: Any) -> bool:
    return isinstance(val, int) and not isinstance(val, bool)


def is_strict_int_list(val: Any) -> bool:
    if not isinstance(val, list):
        return False
    return all(is_strict_int(x) for x in val)


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
    try:
        left, right = text.split(":", 1)
        p = int(left)
        if "-" in right:
            a, b = right.split("-", 1)
            return p, range(int(a), int(b) + 1)
        k = int(right)
        return p, range(k, k + 1)
    except (ValueError, TypeError) as exc:
        raise SystemExit(f"ERROR: malformed domain argument {text!r}: {exc}")


def validate_row(obj: dict[str, Any], line_id: str) -> tuple[int, tuple[int, ...]] | None:
    """Validate a single row. Returns (p, canonical_B) or None if malformed."""
    if not isinstance(obj, dict):
        return None

    p_raw = obj.get("p")
    if p_raw is None:
        return None
    if not is_strict_int(p_raw):
        return None
    p = p_raw
    if p < 2:
        return None
    if not is_prime(p):
        return None

    B_raw = obj.get("B")
    if B_raw is None:
        return None
    if not isinstance(B_raw, list):
        return None
    if not is_strict_int_list(B_raw):
        return None

    B = tuple(sorted(B_raw))
    universe = set(range(1, p))
    if len(B) != len(set(B)):
        return None
    if not set(B) <= universe:
        return None

    return p, B


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("certificates", nargs="+", help="Minimal witness JSONL file(s)")
    ap.add_argument("--domain", action="append", default=[], help="Expected domain, e.g. 29:3-7. May repeat.")
    ap.add_argument("--require-canonical", action="store_true", help="Reject noncanonical B entries")
    ap.add_argument("--fail-extra-domains", action="store_true", help="Fail if unexpected domains appear")
    ap.add_argument("--json", action="store_true", help="Output results as JSON")
    args = ap.parse_args()

    by_pk: dict[tuple[int, int], set[tuple[int, ...]]] = defaultdict(set)
    total_rows = 0
    noncanonical_rows = 0
    malformed_rows = 0
    duplicate_canonical_count = 0
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
            for lineno, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                total_rows += 1
                line_id = f"{path}:{lineno}"
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    malformed_rows += 1
                    continue

                result = validate_row(obj, line_id)
                if result is None:
                    malformed_rows += 1
                    continue

                p, B = result
                can = canonical_scale(B, p)

                if args.require_canonical and B != can:
                    noncanonical_rows += 1
                    continue

                key = (p, can)
                canonical_seen[key] += 1
                if canonical_seen[key] > 1:
                    duplicate_canonical_count += 1

                by_pk[(p, len(B))].add(can)

    requested_domains: set[tuple[int, int]] = set()
    failures: list[str] = []
    domains_output: list[dict] = []

    for domain_text in args.domain:
        p, k_range = parse_domain(domain_text)
        for k in k_range:
            requested_domains.add((p, k))
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

    if args.fail_extra_domains:
        extra_domains = [d for d in by_pk if d not in requested_domains]
        if extra_domains:
            for d in extra_domains:
                failures.append(f"Unexpected domain p={d[0]} |B|={d[1]} (not requested)")
            extra_domain_count = len(extra_domains)
        else:
            extra_domain_count = 0
    else:
        extra_domain_count = 0

    if args.json:
        print(json.dumps({
            "pass": len(failures) == 0 and malformed_rows == 0,
            "total_rows": total_rows,
            "noncanonical_rows": noncanonical_rows,
            "malformed_rows": malformed_rows,
            "duplicate_canonical_count": duplicate_canonical_count,
            "extra_domain_count": extra_domain_count,
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
