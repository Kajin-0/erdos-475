#!/usr/bin/env python3
"""Verify minimal witness certificates for finite Erdős 475 complement domains.

Certificate JSONL schema:

    {"p": 29, "B": [1,2,5], "final_order": [...]}

The checker recomputes all trusted properties from scratch.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict
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


def parse_domain(text: str) -> tuple[int, range]:
    # Format: 29:3-7 or 31:6
    left, right = text.split(":", 1)
    p = int(left)
    if "-" in right:
        a, b = right.split("-", 1)
        return p, range(int(a), int(b) + 1)
    k = int(right)
    return p, range(k, k + 1)


def canonical_scale(B: tuple[int, ...], p: int) -> tuple[int, ...]:
    if not B:
        return tuple()
    reps = []
    for lam in range(1, p):
        reps.append(tuple(sorted((lam * x) % p for x in B)))
    return min(reps)


def all_canonical_B(p: int, k: int) -> set[tuple[int, ...]]:
    universe = list(range(1, p))
    out: set[tuple[int, ...]] = set()
    for comb in itertools.combinations(universe, k):
        out.add(canonical_scale(tuple(comb), p))
    return out


def as_int_list(value: Any, field: str, line_no: int) -> list[int]:
    if not isinstance(value, list):
        raise ValueError(f"line {line_no}: field {field!r} must be a list")
    try:
        return [int(x) for x in value]
    except (TypeError, ValueError) as exc:
        raise ValueError(f"line {line_no}: field {field!r} contains non-integers") from exc


def verify_record(raw: dict[str, Any], line_no: int, require_canonical: bool) -> tuple[int, tuple[int, ...]]:
    try:
        p = int(raw["p"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"line {line_no}: missing/invalid p") from exc
    if not is_prime(p):
        raise ValueError(f"line {line_no}: p={p} is not prime")

    B = tuple(sorted(as_int_list(raw.get("B"), "B", line_no)))
    order = as_int_list(raw.get("final_order"), "final_order", line_no)

    universe = set(range(1, p))
    B_set = set(B)
    if len(B) != len(B_set):
        raise ValueError(f"line {line_no}: B has duplicates: {B}")
    if not B_set <= universe:
        raise ValueError(f"line {line_no}: B is not a subset of F_p^*: {B}")

    if require_canonical and B != canonical_scale(B, p):
        raise ValueError(f"line {line_no}: B is not canonical under scaling: {B}")

    A = universe - B_set
    if Counter(order) != Counter(A):
        missing = sorted(A - set(order))
        extra = sorted(set(order) - A)
        raise ValueError(
            f"line {line_no}: final_order is not permutation of F_p^*\\B; "
            f"missing={missing} extra={extra}"
        )

    partials: list[int] = []
    s = 0
    for x in order:
        s = (s + x) % p
        partials.append(s)
    if len(partials) != len(set(partials)):
        counts = Counter(partials)
        dupes = sorted(v for v, c in counts.items() if c > 1)
        raise ValueError(f"line {line_no}: repeated nonempty partial sums: {dupes}")

    return p, B


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", help="Minimal witness JSONL file")
    parser.add_argument("--domain", action="append", default=[], help="Expected domain, e.g. 29:3-7. May repeat.")
    parser.add_argument("--require-canonical", action="store_true", help="Require every B to be canonical under scaling")
    parser.add_argument("--require-coverage", action="store_true", help="Require complete canonical B coverage for declared domains")
    parser.add_argument("--allow-duplicates", action="store_true", help="Allow duplicate B rows if all rows verify")
    args = parser.parse_args()

    cert_path = Path(args.certificate)
    if not cert_path.exists():
        raise FileNotFoundError(f"certificate file not found: {cert_path}")

    seen: dict[tuple[int, tuple[int, ...]], int] = {}
    by_p_k: dict[tuple[int, int], set[tuple[int, ...]]] = defaultdict(set)
    rows = 0

    with cert_path.open("r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            rows += 1
            try:
                raw = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"line {line_no}: invalid JSON: {exc}") from exc
            key = verify_record(raw, line_no, args.require_canonical)
            if key in seen and not args.allow_duplicates:
                raise ValueError(f"line {line_no}: duplicate witness for p={key[0]} B={list(key[1])}; first at line {seen[key]}")
            seen.setdefault(key, line_no)
            p, B = key
            by_p_k[(p, len(B))].add(B)

    for domain_text in args.domain:
        p, k_range = parse_domain(domain_text)
        for k in k_range:
            observed = by_p_k[(p, k)]
            print(f"domain p={p} |B|={k} observed={len(observed)}")
            if args.require_coverage:
                expected = all_canonical_B(p, k)
                missing = expected - observed
                extra = observed - expected
                print(f"domain p={p} |B|={k} expected_canonical={len(expected)} missing={len(missing)} extra={len(extra)}")
                if missing or extra:
                    sample_missing = sorted(missing)[:5]
                    sample_extra = sorted(extra)[:5]
                    raise ValueError(
                        f"coverage failure for p={p} |B|={k}: "
                        f"missing={len(missing)} sample_missing={sample_missing} "
                        f"extra={len(extra)} sample_extra={sample_extra}"
                    )

    print(f"verified_rows={rows}")
    print(f"unique_instances={len(seen)}")
    print("PASS minimal witness verification")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
