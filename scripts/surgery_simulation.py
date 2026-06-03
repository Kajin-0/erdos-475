#!/usr/bin/env python3
"""Surgery simulation: break fully blocked valid orderings via local modifications.

Given a fully blocked valid ordering C for inserting x into S, try local
surgery operations and check if the result:
  (a) remains Graham-valid, and
  (b) has fewer blocked cuts (ideally, at least one unblocked cut).

Operations:
  - adjacent_swap: swap C[i] and C[i+1]
  - block_reverse: reverse C[i:j] for small blocks (len 2-4)
  - element_move: remove C[i] and reinsert at position j
  - prefix_rotate: move C[0] to position j
  - suffix_rotate: move C[n-1] to position i

Goal: identify which operations reliably reduce blocked counts and what
structural features make a fully blocked ordering "surgically accessible."
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
import time
from collections import Counter
from multiprocessing import Pool, cpu_count
from pathlib import Path
from typing import Any, Iterable, Sequence

random.seed(20260603)


# ── shared utilities ──────────────────────────────────────────────────────

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
    crossing: list[tuple[int, int]] = []
    for k in range(1, n + 1):
        for j in range(k, n + 1):
            if (s[j] - s[k]) % p == target:
                if k < j:
                    crossing.append((k, j))
                    for i in range(k, j):
                        multiplicities[i] += 1

    blocked = {i for i, m in enumerate(multiplicities) if m > 0} | endpoint_cuts
    unblocked = [i for i in range(n + 1) if i not in blocked]
    crossing_cover = set()
    for k, j in crossing:
        crossing_cover.update(range(k, j))

    first_cross_k = min((k for k, j in crossing), default=n + 1)
    last_cross_j = max((j for k, j in crossing), default=0)
    endpoint_only = endpoint_cuts - crossing_cover

    return {
        "blocked_count": len(blocked),
        "unblocked_count": len(unblocked),
        "blocked_cuts": sorted(blocked),
        "unblocked_cuts": unblocked,
        "zero_partial": zero_partial,
        "endpoint_count": len(endpoint_cuts),
        "crossing_count": len(crossing),
        "first_cross_k": first_cross_k,
        "last_cross_j": last_cross_j,
        "prefix_gap": first_cross_k - 1,
        "suffix_gap": n - last_cross_j,
        "endpoint_only_count": len(endpoint_only),
    }


# ── surgery operations ────────────────────────────────────────────────────

def adjacent_swap(order: list[int], i: int) -> list[int]:
    """Swap order[i] and order[i+1]."""
    n = len(order)
    if i < 0 or i >= n - 1:
        return order
    r = list(order)
    r[i], r[i + 1] = r[i + 1], r[i]
    return r

def block_reverse(order: list[int], i: int, j: int) -> list[int]:
    """Reverse order[i:j] (exclusive of j)."""
    n = len(order)
    i = max(0, i)
    j = min(n, j)
    if j - i < 2:
        return order
    r = list(order)
    r[i:j] = reversed(r[i:j])
    return r

def element_move(order: list[int], src: int, dst: int) -> list[int]:
    """Remove order[src], insert at position dst."""
    n = len(order)
    src = max(0, min(n - 1, src))
    dst = max(0, min(n, dst))
    r = list(order)
    val = r.pop(src)
    r.insert(dst, val)
    return r

def prefix_rotate(order: list[int], dst: int) -> list[int]:
    """Move first element to position dst."""
    return element_move(order, 0, dst)

def suffix_rotate(order: list[int], src: int) -> list[int]:
    """Move element at src to end."""
    return element_move(order, src, len(order))


# ── try all surgeries on one ordering ─────────────────────────────────────

def surgery_attempts(order: list[int], x: int, p: int, target_reduction: int = 1) -> list[dict]:
    """Try all surgeries on a fully-blocked ordering, return successful ones.

    target_reduction: minimum reduction in blocked_count to record.
    """
    n = len(order)
    baseline = compute_obstruction(order, x, p)
    if baseline["unblocked_count"] > 0:
        return []  # not fully blocked

    results: list[dict] = []

    # 1. adjacent swaps
    for i in range(n - 1):
        r = adjacent_swap(order, i)
        if not is_graham_valid(r, p):
            continue
        obs = compute_obstruction(r, x, p)
        reduction = baseline["blocked_count"] - obs["blocked_count"]
        if reduction >= target_reduction:
            results.append({
                "op": "adjacent_swap",
                "param": i,
                "reduction": reduction,
                "result_unblocked": obs["unblocked_count"],
                "result_zero_partial": obs["zero_partial"],
                "result_prefix_gap": obs["prefix_gap"],
                "result_suffix_gap": obs["suffix_gap"],
                "result_first_cross_k": obs["first_cross_k"],
                "result_last_cross_j": obs["last_cross_j"],
            })

    # 2. block reverse (len 2-4)
    for length in range(2, min(5, n + 1)):
        for i in range(n - length + 1):
            r = block_reverse(order, i, i + length)
            if not is_graham_valid(r, p):
                continue
            obs = compute_obstruction(r, x, p)
            reduction = baseline["blocked_count"] - obs["blocked_count"]
            if reduction >= target_reduction:
                results.append({
                    "op": f"block_reverse_{length}",
                    "param": i,
                    "reduction": reduction,
                    "result_unblocked": obs["unblocked_count"],
                    "result_zero_partial": obs["zero_partial"],
                    "result_prefix_gap": obs["prefix_gap"],
                    "result_suffix_gap": obs["suffix_gap"],
                })

    # 3. element moves (sample if n > 12)
    move_pairs = []
    if n <= 12:
        for src in range(n):
            for dst in range(n + 1):
                if dst != src and dst != src + 1:
                    move_pairs.append((src, dst))
    else:
        # sample
        for _ in range(100):
            src = random.randrange(n)
            dst = random.randrange(n + 1)
            if dst != src and dst != src + 1:
                move_pairs.append((src, dst))

    for src, dst in move_pairs:
        r = element_move(order, src, dst)
        if not is_graham_valid(r, p):
            continue
        obs = compute_obstruction(r, x, p)
        reduction = baseline["blocked_count"] - obs["blocked_count"]
        if reduction >= target_reduction:
            results.append({
                "op": "element_move",
                "param": f"{src}->{dst}",
                "reduction": reduction,
                "result_unblocked": obs["unblocked_count"],
                "result_zero_partial": obs["zero_partial"],
                "result_prefix_gap": obs["prefix_gap"],
                "result_suffix_gap": obs["suffix_gap"],
            })

    # 4. prefix rotate
    for dst in range(1, min(n, 6)):
        r = prefix_rotate(order, dst)
        if not is_graham_valid(r, p):
            continue
        obs = compute_obstruction(r, x, p)
        reduction = baseline["blocked_count"] - obs["blocked_count"]
        if reduction >= target_reduction:
            results.append({
                "op": "prefix_rotate",
                "param": dst,
                "reduction": reduction,
                "result_unblocked": obs["unblocked_count"],
                "result_zero_partial": obs["zero_partial"],
                "result_prefix_gap": obs["prefix_gap"],
                "result_suffix_gap": obs["suffix_gap"],
            })

    # 5. suffix rotate
    for src in range(max(0, n - 6), n - 1):
        r = suffix_rotate(order, src)
        if not is_graham_valid(r, p):
            continue
        obs = compute_obstruction(r, x, p)
        reduction = baseline["blocked_count"] - obs["blocked_count"]
        if reduction >= target_reduction:
            results.append({
                "op": "suffix_rotate",
                "param": src,
                "reduction": reduction,
                "result_unblocked": obs["unblocked_count"],
                "result_zero_partial": obs["zero_partial"],
                "result_prefix_gap": obs["prefix_gap"],
                "result_suffix_gap": obs["suffix_gap"],
            })

    return results


def find_fully_blocked_ordering(elements: list[int], x: int, p: int, max_trials: int = 50000) -> list[int] | None:
    """Find a fully blocked valid ordering."""
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


def process_record(record: dict) -> list[dict]:
    p = int(record["p"])
    order = record["final_order"]
    B = record.get("B", [])
    src = record.get("_source_line", 0)
    results: list[dict] = []

    for idx, x in enumerate(order):
        s = [*order[:idx], *order[idx+1:]]
        if len(s) <= 2 or len(s) > 30:
            continue
        for v in s:
            if not (1 <= v <= p - 1):
                break
        else:
            # valid elements
            fb_order = find_fully_blocked_ordering(s, x, p, max_trials=20000)
            if fb_order is None:
                continue

            surgeries = surgery_attempts(fb_order, x, p, target_reduction=1)
            if surgeries:
                # summarize which ops succeeded
                op_counts: dict[str, int] = Counter()
                max_reduction: dict[str, int] = {}
                unblocked_achieved = False
                for s in surgeries:
                    op_counts[s["op"]] += 1
                    op_name = s["op"].split("_")[0]
                    if s["reduction"] > max_reduction.get(op_name, 0):
                        max_reduction[op_name] = s["reduction"]
                    if s["result_unblocked"] > 0:
                        unblocked_achieved = True

                results.append({
                    "p": p,
                    "B": B,
                    "x": x,
                    "k": len(s),
                    "src_line": src,
                    "total_surgeries": len(surgeries),
                    "unblocked_achieved": unblocked_achieved,
                    "best_reduction": max(s["reduction"] for s in surgeries) if surgeries else 0,
                    "op_breakdown": dict(op_counts),
                    "max_reduction_by_op": max_reduction,
                    "has_adjacent_swap": op_counts.get("adjacent_swap", 0) > 0,
                    "has_block_reverse": any(k.startswith("block_reverse") for k in op_counts),
                    "has_element_move": op_counts.get("element_move", 0) > 0,
                    "has_prefix_rotate": op_counts.get("prefix_rotate", 0) > 0,
                    "has_suffix_rotate": op_counts.get("suffix_rotate", 0) > 0,
                })

    return results


def witness_rows(path: Path) -> Iterable[dict]:
    with path.open("r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("witness_jsonl", type=str)
    ap.add_argument("--limit", type=int, default=200)
    ap.add_argument("--workers", type=int, default=cpu_count())
    ap.add_argument("--jsonl-out", type=str, default="logs/surgery_results.jsonl")
    args = ap.parse_args()

    path = Path(args.witness_jsonl)
    records = list(witness_rows(path))[:args.limit]
    print(f"Records: {len(records)}", file=sys.stderr)

    start = time.monotonic()
    with Pool(args.workers) as pool:
        results = pool.map(process_record, records)
    elapsed = time.monotonic() - start

    flat = [r for rec in results for r in rec]
    print(f"Fully blocked with successful surgeries: {len(flat)}", file=sys.stderr)
    print(f"Time: {elapsed:.1f}s", file=sys.stderr)

    if not flat:
        print("No fully blocked orderings with successful surgeries found.")
        return 0

    unblocked = sum(1 for r in flat if r["unblocked_achieved"])
    print(f"\n=== Surgery Simulation Results ===")
    print(f"Fully blocked cases with successful surgeries: {len(flat)}")
    print(f"Unblocked achieved: {unblocked}/{len(flat)} ({100*unblocked/len(flat):.1f}%)")

    # Which ops work?
    for op_name in ["has_adjacent_swap", "has_block_reverse", "has_element_move", "has_prefix_rotate", "has_suffix_rotate"]:
        count = sum(1 for r in flat if r.get(op_name))
        print(f"  {op_name}: {count}/{len(flat)} ({100*count/len(flat):.1f}%)")

    # Best reduction by each op
    best_by_op: dict[str, list[int]] = {}
    for r in flat:
        for op, red in r.get("max_reduction_by_op", {}).items():
            best_by_op.setdefault(op, []).append(red)

    print(f"\nBest reduction by operation type:")
    for op, reds in sorted(best_by_op.items()):
        avg = sum(reds) / len(reds)
        mx = max(reds)
        print(f"  {op}: max={mx} avg={avg:.2f} n={len(reds)}")

    # Average best reduction
    avg_best = sum(r["best_reduction"] for r in flat) / len(flat)
    print(f"\nAverage best reduction: {avg_best:.2f}")
    print(f"Max reduction: {max(r['best_reduction'] for r in flat)}")

    # Distribution by set size
    by_k: dict[int, int] = Counter()
    by_k_unblocked: dict[int, int] = Counter()
    for r in flat:
        by_k[r["k"]] += 1
        if r["unblocked_achieved"]:
            by_k_unblocked[r["k"]] += 1

    print(f"\nBy set k = |S|:")
    for k in sorted(by_k.keys()):
        u = by_k_unblocked.get(k, 0)
        print(f"  k={k:3d}: {by_k[k]:4d} cases, unblocked={u:4d} ({100*u/by_k[k]:.0f}%)")

    if args.jsonl_out:
        out_path = Path(args.jsonl_out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("w") as fh:
            for r in flat:
                fh.write(json.dumps(r, sort_keys=True, separators=(",", ":")) + "\n")
        print(f"\nOutput: {args.jsonl_out}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
