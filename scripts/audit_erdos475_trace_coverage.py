#!/usr/bin/env python3
"""
Coverage audit for Erdos 475 repair-trace universes.

Purpose
-------
The certificate verifier proves that every state PRESENT in the trace/certificate
universe has a valid descent/escape certificate. The remaining mathematical gap is
coverage:

    Do the trace files cover all B-sets/configurations required by the theorem?

This script audits trace coverage at the B-set level. It does not assume that the
trace generator is exhaustive. It compares the B-sets appearing in JSONL traces
against an explicitly generated universe of normalized B-sets.

Supported normalization modes
-----------------------------

1. contains_one
   Universe = all k-subsets of F_p^* containing 1.

   This is the simplest audit if your generator explicitly normalizes every B so
   that 1 in B but does NOT quotient by all multiplicative symmetries.

2. canonical_scaling
   Universe = one canonical representative for each multiplicative scaling orbit
   of k-subsets of F_p^*. The canonical representative is the lexicographically
   smallest sorted tuple among all aB, a in F_p^*.

   Use this if your generator quotients by nonzero scalar multiplication.

3. trace_mode
   Infer likely mode from trace data:
       - if every B contains 1, run contains_one;
       - always also report canonical_scaling counts for comparison.

Validity testing for missing B-sets
-----------------------------------
By default, the script only reports coverage gaps.

With --test-missing, it attempts to determine whether missing B-sets are already
valid by brute-forcing permutations of B up to --exact-max-k. For k<=7 this can
be feasible for small missing sets but may be expensive for large gaps.

Definitions
-----------
Given an ordering R=(r_1,...,r_k), partial sums are

    S_i = r_1 + ... + r_i mod p, i=1..k.

Following the existing analyzers, collisions are checked among S_1,...,S_k.
An ordering is valid if these partial sums are all distinct.

Usage
-----

Basic audit:

    python audit_erdos475_trace_coverage.py p29_r3_to_r7_repair_traces_strict.jsonl p31_r3_to_r6_repair_traces_strict.jsonl

Explicit ranges:

    python audit_erdos475_trace_coverage.py p29_r3_to_r7_repair_traces_strict.jsonl --p 29 --r-min 3 --r-max 7 --mode contains_one

Canonical scaling audit:

    python audit_erdos475_trace_coverage.py p31_r3_to_r6_repair_traces_strict.jsonl --p 31 --r-min 3 --r-max 6 --mode canonical_scaling

Test missing sets exactly up to k=6:

    python audit_erdos475_trace_coverage.py p31_r3_to_r6_repair_traces_strict.jsonl --mode contains_one --test-missing --exact-max-k 6 --missing-csv p31_missing_audit.csv

Outputs
-------
- coverage by p and |B|;
- missing counts;
- duplicate trace B counts;
- optional CSV of missing B-sets and exact validity status.
"""

from __future__ import annotations

import argparse
import collections
import csv
import itertools
import json
import math
import os
import random
from typing import Dict, Iterable, List, Tuple, Set, Optional, Any


BSet = Tuple[int, ...]


def mod_tuple(xs: Iterable[int], p: int) -> BSet:
    return tuple(sorted({int(x) % p for x in xs if int(x) % p != 0}))


def scale_B(B: BSet, a: int, p: int) -> BSet:
    return tuple(sorted((a * x) % p for x in B))


def canonical_scaling(B: BSet, p: int) -> BSet:
    reps = [scale_B(B, a, p) for a in range(1, p)]
    return min(reps)


def contains_one_key(B: BSet, p: int) -> BSet:
    return tuple(sorted(B))


def key_B(B: BSet, p: int, mode: str) -> BSet:
    if mode == "contains_one":
        return contains_one_key(B, p)
    if mode == "canonical_scaling":
        return canonical_scaling(B, p)
    raise ValueError(mode)


def load_trace_Bs(paths: List[str]) -> Tuple[Dict[Tuple[int, int], collections.Counter], Dict[str, Any]]:
    by_pk: Dict[Tuple[int, int], collections.Counter] = collections.defaultdict(collections.Counter)
    meta = {
        "files": [],
        "all_contain_one": True,
        "total_lines": 0,
        "p_values": set(),
        "k_values": set(),
    }

    for path in paths:
        n = 0
        with open(path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                if not line.strip():
                    continue
                rec = json.loads(line)
                p = int(rec["p"])
                B = mod_tuple(rec["B"], p)
                k = len(B)
                by_pk[(p, k)][B] += 1
                meta["all_contain_one"] = meta["all_contain_one"] and (1 in B)
                meta["p_values"].add(p)
                meta["k_values"].add(k)
                n += 1
        meta["files"].append({"path": path, "lines": n})
        meta["total_lines"] += n

    meta["p_values"] = sorted(meta["p_values"])
    meta["k_values"] = sorted(meta["k_values"])
    return by_pk, meta


def universe_contains_one(p: int, k: int) -> Iterable[BSet]:
    for rest in itertools.combinations(range(2, p), k - 1):
        yield (1,) + tuple(rest)


def universe_canonical_scaling(p: int, k: int) -> Iterable[BSet]:
    seen: Set[BSet] = set()
    for B in itertools.combinations(range(1, p), k):
        c = canonical_scaling(tuple(B), p)
        if c not in seen:
            seen.add(c)
            yield c


def partial_sums(p: int, order: Tuple[int, ...]) -> List[int]:
    s = 0
    out = []
    for x in order:
        s = (s + x) % p
        out.append(s)
    return out


def is_valid_ordering(p: int, order: Tuple[int, ...]) -> bool:
    S = partial_sums(p, order)
    return len(S) == len(set(S))


def find_valid_ordering_exact(p: int, B: BSet, max_perms: Optional[int] = None) -> Optional[Tuple[int, ...]]:
    count = 0
    for perm in itertools.permutations(B):
        count += 1
        if is_valid_ordering(p, perm):
            return perm
        if max_perms is not None and count >= max_perms:
            break
    return None


def find_valid_ordering_random(p: int, B: BSet, trials: int, seed: int = 1) -> Optional[Tuple[int, ...]]:
    rng = random.Random(seed)
    arr = list(B)
    for _ in range(trials):
        rng.shuffle(arr)
        perm = tuple(arr)
        if is_valid_ordering(p, perm):
            return perm
    return None


def infer_ranges(by_pk: Dict[Tuple[int, int], collections.Counter], args) -> List[Tuple[int, int]]:
    pairs = sorted(by_pk.keys())
    if args.p is not None:
        pairs = [x for x in pairs if x[0] == args.p]
    if args.r_min is not None:
        pairs = [x for x in pairs if x[1] >= args.r_min]
    if args.r_max is not None:
        pairs = [x for x in pairs if x[1] <= args.r_max]
    return pairs


def expected_universe_set(p: int, k: int, mode: str) -> Set[BSet]:
    if mode == "contains_one":
        return set(universe_contains_one(p, k))
    if mode == "canonical_scaling":
        return set(universe_canonical_scaling(p, k))
    raise ValueError(mode)


def project_trace_keys(counter: collections.Counter, p: int, mode: str) -> collections.Counter:
    out = collections.Counter()
    for B, n in counter.items():
        out[key_B(B, p, mode)] += n
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("trace_jsonl", nargs="+")
    ap.add_argument("--p", type=int, default=None)
    ap.add_argument("--r-min", type=int, default=None)
    ap.add_argument("--r-max", type=int, default=None)
    ap.add_argument("--mode", choices=["trace_mode", "contains_one", "canonical_scaling"], default="trace_mode")
    ap.add_argument("--test-missing", action="store_true")
    ap.add_argument("--exact-max-k", type=int, default=7)
    ap.add_argument("--max-exact-perms", type=int, default=None)
    ap.add_argument("--random-trials", type=int, default=0)
    ap.add_argument("--max-missing-test", type=int, default=None)
    ap.add_argument("--missing-csv", default=None)
    ap.add_argument("--summary-csv", default=None)
    ap.add_argument("--show-missing", type=int, default=20)
    args = ap.parse_args()

    by_pk, meta = load_trace_Bs(args.trace_jsonl)
    pairs = infer_ranges(by_pk, args)

    modes = ["contains_one", "canonical_scaling"] if args.mode == "trace_mode" else [args.mode]

    print("=== Erdos 475 trace coverage audit ===")
    print(f"files={len(args.trace_jsonl)}")
    print(f"total_trace_lines={meta['total_lines']}")
    print(f"p_values={meta['p_values']}")
    print(f"k_values={meta['k_values']}")
    print(f"all_trace_B_contain_1={meta['all_contain_one']}")
    print(f"modes={','.join(modes)}")
    print()

    summary_rows = []
    missing_rows = []

    for mode in modes:
        print(f"--- Mode: {mode} ---")
        for p, k in pairs:
            trace_counter_raw = by_pk[(p, k)]
            trace_counter = project_trace_keys(trace_counter_raw, p, mode)

            universe = expected_universe_set(p, k, mode)
            trace_keys = set(trace_counter.keys())
            present = trace_keys & universe
            extra = trace_keys - universe
            missing = sorted(universe - trace_keys)

            duplicate_lines = sum(n - 1 for n in trace_counter.values() if n > 1)

            row = {
                "mode": mode,
                "p": p,
                "k": k,
                "universe_count": len(universe),
                "trace_unique_projected": len(trace_keys),
                "present": len(present),
                "missing": len(missing),
                "extra": len(extra),
                "trace_raw_unique": len(trace_counter_raw),
                "trace_lines": sum(trace_counter_raw.values()),
                "duplicate_projected_lines": duplicate_lines,
                "coverage_fraction": f"{len(present)/len(universe):.8f}" if universe else "0",
            }
            summary_rows.append(row)

            print(
                f"p={p:2d} |B|={k}: universe={len(universe):7d} "
                f"present={len(present):7d} missing={len(missing):7d} "
                f"extra={len(extra):5d} raw_unique={len(trace_counter_raw):7d} "
                f"lines={sum(trace_counter_raw.values()):7d} coverage={100*len(present)/len(universe) if universe else 0:6.2f}%"
            )

            if missing:
                print("  missing examples:", " ".join(str(m) for m in missing[:args.show_missing]))

            if args.test_missing and missing:
                to_test = missing
                if args.max_missing_test is not None:
                    to_test = to_test[:args.max_missing_test]

                for B in to_test:
                    status = "not_tested"
                    witness = ""

                    if k <= args.exact_max_k:
                        w = find_valid_ordering_exact(p, B, args.max_exact_perms)
                        if w is not None:
                            status = "valid_exact"
                            witness = " ".join(map(str, w))
                        else:
                            status = "no_valid_found_exact"
                    elif args.random_trials > 0:
                        w = find_valid_ordering_random(p, B, args.random_trials)
                        if w is not None:
                            status = "valid_random"
                            witness = " ".join(map(str, w))
                        else:
                            status = "no_valid_found_random"

                    missing_rows.append({
                        "mode": mode,
                        "p": p,
                        "k": k,
                        "B": " ".join(map(str, B)),
                        "status": status,
                        "witness_order": witness,
                    })

        print()

    if args.summary_csv:
        with open(args.summary_csv, "w", encoding="utf-8", newline="") as f:
            fields = list(summary_rows[0].keys()) if summary_rows else []
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(summary_rows)
        print(f"Wrote {args.summary_csv}")

    if args.missing_csv and missing_rows:
        with open(args.missing_csv, "w", encoding="utf-8", newline="") as f:
            fields = list(missing_rows[0].keys())
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(missing_rows)
        print(f"Wrote {args.missing_csv}")

    print("Interpretation:")
    print("  - present/universe=100% means the trace file covers every B-set under that normalization.")
    print("  - missing B-sets may be harmless if they are already valid and therefore never needed repair.")
    print("  - if missing B-sets are invalid and not trace-covered, the trace universe is not exhaustive.")
    print("  - use --test-missing for exact/rand validity checks on missing B-sets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
