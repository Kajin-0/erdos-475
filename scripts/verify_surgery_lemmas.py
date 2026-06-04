#!/usr/bin/env python3
"""Comprehensive surgery lemma verification with ordering storage.

Stores the actual fully blocked ordering and tests all short block_reverse
operations to identify which positions reliably break full blockage.
"""

from __future__ import annotations

import json
import random
import sys
from collections import Counter
from multiprocessing import Pool, cpu_count
from pathlib import Path
from typing import Any, Sequence

random.seed(20260603)


def nonempty_partials(order: Sequence[int], p: int) -> list[int]:
    out: list[int] = []
    s = 0
    for v in order:
        s = (s + v) % p
        out.append(s)
    return out

def is_graham_valid(order: Sequence[int], p: int) -> bool:
    sums = nonempty_partials(order, p)
    return len(sums) == len(set(sums))

def compute_obstruction(order: Sequence[int], x: int, p: int) -> dict:
    n = len(order)
    s = [0]
    acc = 0
    for v in order:
        acc = (acc + v) % p
        s.append(acc)
    multiplicities = [0] * (n + 1)
    endpoint_cuts: set[int] = set()
    zero_partial = any(v == 0 for v in s[1:])
    if zero_partial:
        multiplicities[0] += 1
    for i in range(1, n + 1):
        inserted_sum = (s[i] + x) % p
        if inserted_sum in set(s[1:i+1]):
            endpoint_cuts.add(i)
            multiplicities[i] += 1
    target = (-x) % p
    for k in range(1, n + 1):
        for j in range(k, n + 1):
            if (s[j] - s[k]) % p == target and k < j:
                for i in range(k, j):
                    multiplicities[i] += 1
    blocked = {i for i, m in enumerate(multiplicities) if m > 0} | endpoint_cuts
    unblocked = [i for i in range(n + 1) if i not in blocked]
    first_cross_k = n + 1
    last_cross_j = 0
    for k in range(1, n + 1):
        for j in range(k, n + 1):
            if (s[j] - s[k]) % p == target and k < j:
                first_cross_k = min(first_cross_k, k)
                last_cross_j = max(last_cross_j, j)
    return {
        "blocked_count": len(blocked),
        "unblocked_count": len(unblocked),
        "unblocked_cuts": unblocked,
        "zero_partial": zero_partial,
        "prefix_gap": first_cross_k - 1,
        "suffix_gap": n - last_cross_j,
    }

def block_reverse(order: list[int], i: int, j: int) -> list[int]:
    r = list(order)
    i = max(0, i)
    j = min(len(r), j)
    if j - i >= 2:
        r[i:j] = reversed(r[i:j])
    return r

def adjacent_swap(order: list[int], i: int) -> list[int]:
    r = list(order)
    if 0 <= i < len(r) - 1:
        r[i], r[i + 1] = r[i + 1], r[i]
    return r


def find_fully_blocked(elements: list[int], x: int, p: int, max_trials: int = 20000) -> list[int] | None:
    best: list[int] | None = None
    best_blocked = 0
    for _ in range(max_trials):
        perm = list(elements)
        random.shuffle(perm)
        if not is_graham_valid(perm, p):
            continue
        obs = compute_obstruction(perm, x, p)
        if obs["blocked_count"] > best_blocked:
            best_blocked = obs["blocked_count"]
            best = perm
            if obs["unblocked_count"] == 0:
                return best
    return best


def test_operations(order: list[int], x: int, p: int) -> dict:
    """Test ALL short surgery operations, return results."""
    n = len(order)
    baseline = compute_obstruction(order, x, p)
    results: list[dict] = []

    # 1) All block_reverse len 2-3
    for length in [2, 3]:
        for start in range(n - length + 1):
            end = start + length
            r = block_reverse(order, start, end)
            if not is_graham_valid(r, p):
                continue
            obs = compute_obstruction(r, x, p)
            reduction = baseline["blocked_count"] - obs["blocked_count"]
            if reduction > 0 or obs["unblocked_count"] > 0:
                results.append({
                    "op": f"br_{length}@{start}",
                    "reduction": reduction,
                    "unblocked": obs["unblocked_count"],
                    "broke_a": not obs["zero_partial"] and baseline["zero_partial"],
                    "broke_b": obs["prefix_gap"] > 0 and baseline["prefix_gap"] == 0,
                    "broke_c": obs["suffix_gap"] > 0 and baseline["suffix_gap"] == 0,
                })

    # 2) Adjacent swaps
    for i in range(n - 1):
        r = adjacent_swap(order, i)
        if not is_graham_valid(r, p):
            continue
        obs = compute_obstruction(r, x, p)
        reduction = baseline["blocked_count"] - obs["blocked_count"]
        if reduction > 0 or obs["unblocked_count"] > 0:
            results.append({
                "op": f"as@{i}",
                "reduction": reduction,
                "unblocked": obs["unblocked_count"],
                "broke_a": not obs["zero_partial"] and baseline["zero_partial"],
                "broke_b": obs["prefix_gap"] > 0 and baseline["prefix_gap"] == 0,
                "broke_c": obs["suffix_gap"] > 0 and baseline["suffix_gap"] == 0,
            })

    best = max(results, key=lambda r: r["reduction"]) if results else None
    br_results = [r for r in results if r["op"].startswith("br_")]

    return {
        "baseline": baseline,
        "has_surgery": best is not None,
        "best": best,
        "n_block_reverse": len(br_results),
        "has_block_reverse": len(br_results) > 0,
        "has_adjacent_swap": any(r["op"].startswith("as@") for r in results),
    }


def process_row(rec: dict) -> list[dict]:
    p = rec["p"]
    order = rec["final_order"]
    B = rec.get("B", [])
    out = []
    for idx, x in enumerate(order):
        elements = [*order[:idx], *order[idx+1:]]
        if len(elements) <= 2 or len(elements) > 26:
            continue
        if any(not (1 <= v <= p - 1) for v in elements):
            continue
        fb = find_fully_blocked(elements, x, p, max_trials=8000)
        if fb is None:
            continue
        ops = test_operations(fb, x, p)
        if not ops["has_surgery"]:
            continue
        out.append({
            "p": p,
            "B": B,
            "x": x,
            "k": len(elements),
            "C": fb,
            "baseline": {"blocked": ops["baseline"]["blocked_count"]},
            "has_block_reverse": ops["has_block_reverse"],
            "has_adjacent_swap": ops["has_adjacent_swap"],
            "best": ops["best"],
        })
    return out


def main() -> int:
    witness_paths = [
        Path("certificates/minimal_witnesses.jsonl"),
        Path("certificates/witnesses_p29_b08.jsonl"),
    ]

    all_records = []
    for wp in witness_paths:
        if not wp.exists():
            continue
        print(f"Loading {wp}...", file=sys.stderr)
        with wp.open() as f:
            rows = [json.loads(line) for line in f if line.strip()]

        sample = rows[:150]
        print(f"  Processing {len(sample)} rows...", file=sys.stderr)

        with Pool(cpu_count()) as pool:
            batch = pool.map(process_row, sample)

        for br in batch:
            all_records.extend(br)

    total = len(all_records)
    if total == 0:
        print("No fully blocked orderings found.", file=sys.stderr)
        return 1

    br_ok = sum(1 for r in all_records if r["has_block_reverse"])
    as_ok = sum(1 for r in all_records if r["has_adjacent_swap"])
    any_ok = sum(1 for r in all_records if r["best"] is not None)

    print("=" * 60)
    print("Surgery Lemma Verification (Comprehensive)")
    print("=" * 60)
    print(f"Fully blocked orderings tested: {total}")
    print(f"Has block_reverse solution:  {br_ok}/{total} ({100*br_ok/total:.1f}%)")
    print(f"Has adjacent_swap solution:  {as_ok}/{total} ({100*as_ok/total:.1f}%)")
    print(f"Has any surgery solution:    {any_ok}/{total} ({100*any_ok/total:.1f}%)")
    print()

    # Best reduction distribution
    reds = Counter()
    for r in all_records:
        if r["best"]:
            reds[r["best"]["reduction"]] += 1
    print(f"Best reduction distribution:")
    for red in sorted(reds):
        print(f"  {red}: {reds[red]} ({100*reds[red]/total:.1f}%)")

    # Output with ordering data
    out_path = Path("logs/surgery_lemma_deep.jsonl")
    with out_path.open("w") as f:
        for r in all_records:
            f.write(json.dumps(r, sort_keys=True, separators=(",", ":")) + "\n")
    print(f"\nDetailed results: {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
