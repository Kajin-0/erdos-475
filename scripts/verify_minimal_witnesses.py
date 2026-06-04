#!/usr/bin/env python3
"""Verify minimal witness certificates for finite Erdős 475 complement domains.

Certificate JSONL schema:

    {"p": 29, "B": [1,2,5], "final_order": [...]}

The checker recomputes all trusted properties from scratch.
Uses strict type checking: no bool-as-int, no string coercion, no floats.

One or more JSONL files may be supplied. Duplicate `(p,B)` witnesses are
rejected across all input files unless `--allow-duplicates` is passed.
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


def is_strict_int(val: Any) -> bool:
    return isinstance(val, int) and not isinstance(val, bool)


def is_strict_int_list(val: Any) -> bool:
    if not isinstance(val, list):
        return False
    return all(is_strict_int(x) for x in val)


def parse_domain(text: str) -> tuple[int, range]:
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


def verify_record(raw: dict[str, Any], line_id: str, require_canonical: bool) -> tuple[int, tuple[int, ...]]:
    p_raw = raw.get("p")
    if p_raw is None:
        raise ValueError(f"{line_id}: missing p")
    if not is_strict_int(p_raw):
        raise ValueError(f"{line_id}: p must be an integer (not bool, string, or float), got {type(p_raw).__name__}")
    p = p_raw
    if p < 2:
        raise ValueError(f"{line_id}: p={p} must be >= 2")
    if not is_prime(p):
        raise ValueError(f"{line_id}: p={p} is not prime")

    B_raw = raw.get("B")
    if B_raw is None:
        raise ValueError(f"{line_id}: missing B")
    if not isinstance(B_raw, list):
        raise ValueError(f"{line_id}: B must be a list, got {type(B_raw).__name__}")
    if not is_strict_int_list(B_raw):
        raise ValueError(f"{line_id}: B must contain only integers (not bools, strings, or floats)")
    B = tuple(sorted(B_raw))

    order_raw = raw.get("final_order")
    if order_raw is None:
        raise ValueError(f"{line_id}: missing final_order")
    if not isinstance(order_raw, list):
        raise ValueError(f"{line_id}: final_order must be a list, got {type(order_raw).__name__}")
    if not is_strict_int_list(order_raw):
        raise ValueError(f"{line_id}: final_order must contain only integers (not bools, strings, or floats)")

    universe = set(range(1, p))
    B_set = set(B)
    if len(B) != len(B_set):
        raise ValueError(f"{line_id}: B has duplicates: {B}")
    if not B_set <= universe:
        raise ValueError(f"{line_id}: B is not a subset of F_p^*: {B}")

    if require_canonical and B != canonical_scale(B, p):
        raise ValueError(f"{line_id}: B is not canonical under scaling: {B}")

    A = universe - B_set
    if Counter(order_raw) != Counter(A):
        missing = sorted(A - set(order_raw))
        extra = sorted(set(order_raw) - A)
        raise ValueError(
            f"{line_id}: final_order is not permutation of F_p^*\\B; "
            f"missing={missing} extra={extra}"
        )

    partials: list[int] = []
    s = 0
    for x in order_raw:
        s = (s + x) % p
        partials.append(s)
    if len(partials) != len(set(partials)):
        counts = Counter(partials)
        dupes = sorted(v for v, c in counts.items() if c > 1)
        raise ValueError(f"{line_id}: repeated nonempty partial sums: {dupes}")

    return p, B


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificates", nargs="+", help="Minimal witness JSONL file(s)")
    parser.add_argument("--domain", action="append", default=[], help="Expected domain, e.g. 29:3-7. May repeat.")
    parser.add_argument("--require-canonical", action="store_true", help="Require every B to be canonical under scaling")
    parser.add_argument("--require-coverage", action="store_true", help="Require complete canonical B coverage for declared domains")
    parser.add_argument("--allow-duplicates", action="store_true", help="Allow duplicate B rows if all rows verify")
    args = parser.parse_args()

    cert_paths = [Path(x) for x in args.certificates]
    for cert_path in cert_paths:
        if not cert_path.exists():
            raise FileNotFoundError(f"certificate file not found: {cert_path}")

    seen: dict[tuple[int, tuple[int, ...]], str] = {}
    by_p_k: dict[tuple[int, int], set[tuple[int, ...]]] = defaultdict(set)
    rows = 0

    for cert_path in cert_paths:
        file_rows = 0
        with cert_path.open("r", encoding="utf-8") as fh:
            for line_no, line in enumerate(fh, start=1):
                line = line.strip()
                if not line:
                    continue
                rows += 1
                file_rows += 1
                line_id = f"{cert_path}:{line_no}"
                try:
                    raw = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"{line_id}: invalid JSON: {exc}") from exc
                if not isinstance(raw, dict):
                    raise ValueError(f"{line_id}: root JSON value is not an object")
                key = verify_record(raw, line_id, args.require_canonical)
                if key in seen and not args.allow_duplicates:
                    raise ValueError(
                        f"{line_id}: duplicate witness for p={key[0]} B={list(key[1])}; first at {seen[key]}"
                    )
                seen.setdefault(key, line_id)
                p, B = key
                by_p_k[(p, len(B))].add(B)
        print(f"certificate_file={cert_path} verified_rows={file_rows}")

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
