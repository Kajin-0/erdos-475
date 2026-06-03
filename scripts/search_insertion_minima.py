#!/usr/bin/env python3
"""Search for worst-case (max blocked cuts) valid orderings of A\{x}.

For each witness record and each x in final_order, this script:
  1. Computes the native deletion ordering C_native = A\{x}.
  2. Searches for valid orderings C' of A\{x} with MORE blocked cuts.
  3. Records the max blocked count found.
  4. If any valid ordering ever has all cuts blocked (fully blocked), flags it.

Search strategies (tried in order of increasing set size k = |A\{x}|):
  - k ≤ 8: enumerate ALL permutations, check each for validity.
  - k ≤ 12: enumerate 200K random permutations, keep valid ones.
  - k > 12: start from C_native, perform random element-move perturbations.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import sys
import time
from collections import Counter
from dataclasses import dataclass, field
from multiprocessing import Pool, cpu_count
from pathlib import Path
from typing import Any, Iterable, Sequence

random.seed(20260603)


# ── imported from analyze_insertion_blocks.py ──────────────────────────────

def nonempty_partials(order: Sequence[int], p: int) -> list[int]:
    out: list[int] = []
    s = 0
    for v in order:
        s = (s + v) % p
        out.append(s)
    return out

def extended_partials(order: Sequence[int], p: int) -> list[int]:
    return [0, *nonempty_partials(order, p)]

def is_graham_valid(order: Sequence[int], p: int) -> bool:
    sums = nonempty_partials(order, p)
    return len(sums) == len(set(sums))

def compute_insertion_obstruction(order: Sequence[int], x: int, p: int) -> dict:
    """Return blocked/unblocked cut data for inserting x into order."""
    n = len(order)
    s = extended_partials(order, p)
    multiplicities = [0] * (n + 1)
    endpoint_cuts: set[int] = set()

    zero_partial_blocks_cut_zero = any(v == 0 for v in s[1:])
    if zero_partial_blocks_cut_zero:
        multiplicities[0] += 1

    for i in range(1, n + 1):
        inserted_sum = (s[i] + x) % p
        if inserted_sum in set(s[1:i+1]):
            endpoint_cuts.add(i)
            multiplicities[i] += 1

    target = (-x) % p
    for k in range(1, n + 1):
        for j in range(k, n + 1):
            if (s[j] - s[k]) % p == target:
                if k < j:
                    for i in range(k, j):
                        multiplicities[i] += 1

    blocked = {i for i, m in enumerate(multiplicities) if m > 0}
    blocked |= endpoint_cuts
    unblocked = [i for i in range(n + 1) if i not in blocked]

    return {
        "blocked_count": len(blocked),
        "unblocked_count": len(unblocked),
        "blocked_cuts": sorted(blocked),
        "unblocked_cuts": unblocked,
        "endpoint_count": len(endpoint_cuts),
        "zero_partial_blocked_cut_zero": zero_partial_blocks_cut_zero,
        "max_multiplicity": max(multiplicities) if multiplicities else 0,
    }


# ── search strategies ─────────────────────────────────────────────────────

def search_exhaustive(elements: list[int], x: int, p: int) -> tuple[dict | None, dict | None]:
    """Enumerate all valid permutations for small sets (k ≤ 8)."""
    best_worst: dict | None = None  # has most blocked cuts
    best_native: dict | None = None  # first valid ordering found
    for perm in itertools.permutations(elements):
        if not is_graham_valid(perm, p):
            continue
        obs = compute_insertion_obstruction(perm, x, p)
        if best_native is None:
            best_native = {**obs, "order": list(perm)}
        if best_worst is None or obs["blocked_count"] > best_worst["blocked_count"]:
            best_worst = {**obs, "order": list(perm)}
            if obs["unblocked_count"] == 0:
                break  # fully blocked, can't get worse
    return best_native, best_worst


def search_random_sample(elements: list[int], x: int, p: int, max_trials: int = 200_000, max_valid: int = 500) -> tuple[dict | None, dict | None]:
    """Sample random permutations for medium sets (9 ≤ k ≤ 12)."""
    best_worst: dict | None = None
    best_native: dict | None = None
    valid_found = 0

    for _ in range(max_trials):
        perm = list(elements)
        random.shuffle(perm)
        if not is_graham_valid(perm, p):
            continue
        valid_found += 1
        obs = compute_insertion_obstruction(perm, x, p)
        if best_native is None:
            best_native = {**obs, "order": perm}
        if best_worst is None or obs["blocked_count"] > best_worst["blocked_count"]:
            best_worst = {**obs, "order": perm}
            if obs["unblocked_count"] == 0:
                break
        if valid_found >= max_valid:
            break

    return best_native, best_worst


def search_perturbation(start_order: list[int], x: int, p: int, iterations: int = 50_000) -> tuple[dict, dict]:
    """Perturb starting ordering to find worse (more blocked) configurations.

    Strategy: repeatedly remove a random element and reinsert at a random
    position. If the result is valid and at least as bad (blocked_count >=
    current), keep it.  Otherwise revert.
    """
    def perturb(seq: list[int]) -> list[int]:
        idx = random.randrange(len(seq))
        val = seq.pop(idx)
        pos = random.randrange(len(seq) + 1)
        seq.insert(pos, val)
        return seq

    baseline = compute_insertion_obstruction(start_order, x, p)
    baseline["order"] = start_order
    best_worst: dict = {**baseline}
    current = list(start_order)
    current_blocked = baseline["blocked_count"]

    for _ in range(iterations):
        candidate = perturb(list(current))
        if not is_graham_valid(candidate, p):
            continue
        obs = compute_insertion_obstruction(candidate, x, p)
        if obs["blocked_count"] >= current_blocked:
            current = candidate
            current_blocked = obs["blocked_count"]
            if obs["blocked_count"] > best_worst["blocked_count"]:
                best_worst = {**obs, "order": list(candidate)}
                if obs["unblocked_count"] == 0:
                    break

    return baseline, best_worst


def search_worst(elements: list[int], x: int, p: int, native_order: list[int] | None = None) -> dict:
    """Dispatch to appropriate search strategy based on set size."""
    k = len(elements)
    start_ord = native_order if native_order else list(elements)

    start = time.monotonic()
    if k <= 8:
        native, worst = search_exhaustive(elements, x, p)
    elif k <= 12:
        native, worst = search_random_sample(elements, x, p, max_trials=200_000, max_valid=500)
    else:
        native, worst = search_perturbation(start_ord, x, p, iterations=50_000)
    elapsed = time.monotonic() - start

    if worst is None or worst["blocked_count"] == -1:
        # No valid ordering found at all
        return {
            "k": k,
            "native_valid": False,
            "search_time_s": elapsed,
        }

    return {
        "k": k,
        "native_valid": True,
        "native_blocked": native["blocked_count"],
        "native_unblocked": native["unblocked_count"],
        "worst_blocked": worst["blocked_count"],
        "worst_unblocked": worst["unblocked_count"],
        "fully_blocked_found": worst["unblocked_count"] == 0,
        "worst_improved": worst["blocked_count"] > native["blocked_count"],
        "search_time_s": elapsed,
    }


# ── worker ────────────────────────────────────────────────────────────────

@dataclass
class Record:
    p: int
    B: list[int]
    final_order: list[int]
    source_line: int


def process_record(record: Record) -> list[dict]:
    """Process one witness record: search all x in final_order."""
    p = record.p
    order = record.final_order
    b = record.B
    results: list[dict] = []

    for idx, x in enumerate(order):
        s = [*order[:idx], *order[idx+1:]]
        base = {"p": p, "B": b, "x": x, "|A|": len(order), "source_line": record.source_line}

        if len(s) == 0:
            results.append({**base, "k": 0, "native_valid": True,
                            "native_blocked": 1, "native_unblocked": 0,
                            "worst_blocked": 1, "worst_unblocked": 0,
                            "fully_blocked_found": True})
            continue

        if not is_graham_valid(s, p):
            results.append({**base, "k": len(s), "native_valid": False})
            continue

        sr = search_worst(s, x, p, native_order=s)
        results.append({**base, **sr})

    return results


# ── I/O ───────────────────────────────────────────────────────────────────

def witness_rows(path: Path) -> Iterable[dict]:
    with path.open("r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            row["_source_line"] = line_no
            yield row


# ── main ───────────────────────────────────────────────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("witness_jsonl", type=str, help="Path to witness JSONL file")
    ap.add_argument("--limit", type=int, default=None, help="Limit records processed")
    ap.add_argument("--workers", type=int, default=cpu_count(), help="Parallel workers")
    ap.add_argument("--jsonl-out", type=str, help="Per-instance output")
    ap.add_argument("--sample-first", action="store_true", help="Before full run, sample first N to calibrate")
    ap.add_argument("--sample-n", type=int, default=200, help="Calibration sample size")
    args = ap.parse_args()

    path = Path(args.witness_jsonl)
    records: list[Record] = []
    for row in witness_rows(path):
        records.append(Record(
            p=int(row["p"]),
            B=[int(v) for v in row.get("B", [])],
            final_order=[int(v) for v in row["final_order"]],
            source_line=row["_source_line"],
        ))
        if args.limit and len(records) >= args.limit:
            break

    total = len(records)
    print(f"Records loaded: {total}", file=sys.stderr)

    if args.sample_first:
        sample = records[:min(args.sample_n, total)]
        print(f"Calibration sample: {len(sample)} records", file=sys.stderr)
        with Pool(args.workers) as pool:
            sample_results = pool.map(process_record, sample)
        # flatten
        flat = [r for rec in sample_results for r in rec]
        samples_with_valid = sum(1 for r in flat if r.get("native_valid"))
        samples_fully_blocked = sum(1 for r in flat if r.get("fully_blocked_found"))
        samples_worst_improved = sum(1 for r in flat if r.get("worst_improved"))
        print(f"Sample valid deletions: {samples_with_valid}")
        print(f"Sample fully blocked found: {samples_fully_blocked}")
        print(f"Sample worst improved over native: {samples_worst_improved}")
        if args.jsonl_out:
            with open(args.jsonl_out, "w") as fh:
                for r in flat:
                    fh.write(json.dumps(r, sort_keys=True) + "\n")
        return 0

    start = time.monotonic()
    with Pool(args.workers) as pool:
        all_results = pool.map(process_record, records)
    elapsed = time.monotonic() - start

    flat = [r for rec in all_results for r in rec]
    total_triples = len(flat)
    valid_deletions = sum(1 for r in flat if r.get("native_valid"))
    invalid_deletions = total_triples - valid_deletions
    fully_blocked = sum(1 for r in flat if r.get("fully_blocked_found"))
    worst_improved = sum(1 for r in flat if r.get("worst_improved"))

    print("=" * 60)
    print("INSERTION MINIMUM SEARCH — FULL RESULTS")
    print("=" * 60)
    print(f"Witness records analyzed: {total}")
    print(f"Total (p, A, x) triples:  {total_triples}")
    print(f"Valid deletions:          {valid_deletions}")
    print(f"Invalid deletions (C not Graham-valid): {invalid_deletions}")
    print(f"Fully blocked found:      {fully_blocked}")
    print(f"Worst > native:           {worst_improved}")
    print(f"Search wall time:         {elapsed:.1f}s")

    if fully_blocked:
        print("\nWARNING: fully blocked configurations FOUND:")
        for r in flat:
            if r.get("fully_blocked_found"):
                print(json.dumps(r, sort_keys=True))

    # Distribution of native unblocked counts
    native_unblocked_counts = Counter(r["native_unblocked"] for r in flat if r.get("native_valid"))
    print(f"\nNative unblocked count distribution:")
    for cnt in sorted(native_unblocked_counts.keys()):
        print(f"  unblocked={cnt}: {native_unblocked_counts[cnt]}")

    # Distribution by set size k
    by_k: dict[int, Counter] = {}
    for r in flat:
        if r.get("native_valid"):
            k = r["k"]
            if k not in by_k:
                by_k[k] = Counter()
            by_k[k][r["native_unblocked"]] += 1

    print(f"\nBy set size k = |A| - 1:")
    for k in sorted(by_k.keys()):
        c = by_k[k]
        min_ub = min(c.keys())
        max_ub = max(c.keys())
        worst_counts = sum(1 for r in flat if r.get("k") == k and r.get("native_valid") and r.get("worst_improved"))
        print(f"  k={k:3d}:  records={sum(c.values()):5d}  unblocked=[{min_ub}..{max_ub}]  worst_improved={worst_counts}")

    if args.jsonl_out:
        out_path = Path(args.jsonl_out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("w", encoding="utf-8") as fh:
            for r in flat:
                fh.write(json.dumps(r, sort_keys=True, separators=(",", ":")) + "\n")
        print(f"\nFull diagnostics written to: {args.jsonl_out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
