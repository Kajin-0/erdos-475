#!/usr/bin/env python3
"""Surgery on fully blocked orderings found via perturbation search.

Uses the same perturbation strategy as systematic_insertion_search.py to find
fully blocked valid orderings for large k, then applies surgery operations.

This addresses the limitation of surgery_simulation.py which could only find
fully blocked orderings for small k via random sampling.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import time
from collections import Counter
from multiprocessing import Pool, cpu_count
from pathlib import Path
from typing import Any, Iterable, Sequence

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

    return {
        "blocked_count": len(blocked),
        "unblocked_count": len(unblocked),
        "unblocked_cuts": unblocked,
        "zero_partial": zero_partial,
        "endpoint_count": len(endpoint_cuts),
        "crossing_count": len(crossing),
        "first_cross_k": first_cross_k,
        "last_cross_j": last_cross_j,
        "prefix_gap": first_cross_k - 1,
        "suffix_gap": n - last_cross_j,
    }


# ── perturbation search for fully blocked ordering ────────────────────────

def find_fully_blocked_perturbation(start: list[int], x: int, p: int, iters: int = 50000) -> list[int] | None:
    """Use perturbation search to find a fully blocked valid ordering."""
    current = list(start)
    cur_blocked = compute_obstruction(current, x, p)["blocked_count"]
    best = (cur_blocked, list(current))

    for _ in range(iters):
        idx = random.randrange(len(current))
        val = current.pop(idx)
        pos = random.randrange(len(current) + 1)
        current.insert(pos, val)
        if not is_graham_valid(current, p):
            # undo
            val2 = current.pop(pos)
            current.insert(idx, val2)
            continue
        obs = compute_obstruction(current, x, p)
        bc = obs["blocked_count"]
        if bc > best[0]:
            best = (bc, list(current))
        if obs["unblocked_count"] == 0:
            return current
        if bc >= cur_blocked:
            cur_blocked = bc
        else:
            # revert
            val2 = current.pop(pos)
            current.insert(idx, val2)

    return best[1] if best[0] >= len(start) else None


# ── surgery operations ────────────────────────────────────────────────────

def adjacent_swap(order: list[int], i: int) -> list[int]:
    n = len(order)
    if i < 0 or i >= n - 1:
        return order
    r = list(order)
    r[i], r[i + 1] = r[i + 1], r[i]
    return r

def block_reverse(order: list[int], i: int, j: int) -> list[int]:
    n = len(order)
    i = max(0, i)
    j = min(n, j)
    if j - i < 2:
        return order
    r = list(order)
    r[i:j] = reversed(r[i:j])
    return r

def element_move(order: list[int], src: int, dst: int) -> list[int]:
    n = len(order)
    src = max(0, min(n - 1, src))
    dst = max(0, min(n, dst))
    r = list(order)
    val = r.pop(src)
    r.insert(dst, val)
    return r

def prefix_rotate(order: list[int], dst: int) -> list[int]:
    return element_move(order, 0, dst)

def suffix_rotate(order: list[int], src: int) -> list[int]:
    return element_move(order, src, len(order))


# ── surgery attempts ──────────────────────────────────────────────────────

def try_surgeries(order: list[int], x: int, p: int) -> dict:
    n = len(order)
    baseline = compute_obstruction(order, x, p)

    results_list: list[dict] = []
    target_reduction = 1

    # adjacent swaps
    for i in range(n - 1):
        r = adjacent_swap(order, i)
        if not is_graham_valid(r, p):
            continue
        obs = compute_obstruction(r, x, p)
        red = baseline["blocked_count"] - obs["blocked_count"]
        if red >= target_reduction:
            results_list.append({
                "op": "adjacent_swap", "param": i, "reduction": red,
                "unblocked": obs["unblocked_count"],
                "zero_partial": obs["zero_partial"],
                "prefix_gap": obs["prefix_gap"],
                "suffix_gap": obs["suffix_gap"],
            })

    # block reverse (len 2-4)
    for length in range(2, min(5, n + 1)):
        for i in range(n - length + 1):
            r = block_reverse(order, i, i + length)
            if not is_graham_valid(r, p):
                continue
            obs = compute_obstruction(r, x, p)
            red = baseline["blocked_count"] - obs["blocked_count"]
            if red >= target_reduction:
                results_list.append({
                    "op": f"block_reverse_{length}", "param": i, "reduction": red,
                    "unblocked": obs["unblocked_count"],
                    "zero_partial": obs["zero_partial"],
                    "prefix_gap": obs["prefix_gap"],
                    "suffix_gap": obs["suffix_gap"],
                })

    # element moves (sampled)
    pairs = set()
    for _ in range(200):
        src = random.randrange(n)
        dst = random.randrange(n + 1)
        if dst != src and dst != src + 1:
            pairs.add((src, dst))
    for src, dst in pairs:
        r = element_move(order, src, dst)
        if not is_graham_valid(r, p):
            continue
        obs = compute_obstruction(r, x, p)
        red = baseline["blocked_count"] - obs["blocked_count"]
        if red >= target_reduction:
            results_list.append({
                "op": "element_move", "param": f"{src}->{dst}", "reduction": red,
                "unblocked": obs["unblocked_count"],
                "zero_partial": obs["zero_partial"],
                "prefix_gap": obs["prefix_gap"],
                "suffix_gap": obs["suffix_gap"],
            })

    # prefix/suffix rotates
    for dst in range(1, min(n, 6)):
        r = prefix_rotate(order, dst)
        if not is_graham_valid(r, p):
            continue
        obs = compute_obstruction(r, x, p)
        red = baseline["blocked_count"] - obs["blocked_count"]
        if red >= target_reduction:
            results_list.append({
                "op": "prefix_rotate", "param": dst, "reduction": red,
                "unblocked": obs["unblocked_count"],
                "zero_partial": obs["zero_partial"],
                "prefix_gap": obs["prefix_gap"],
                "suffix_gap": obs["suffix_gap"],
            })

    for src in range(max(0, n - 6), n - 1):
        r = suffix_rotate(order, src)
        if not is_graham_valid(r, p):
            continue
        obs = compute_obstruction(r, x, p)
        red = baseline["blocked_count"] - obs["blocked_count"]
        if red >= target_reduction:
            results_list.append({
                "op": "suffix_rotate", "param": src, "reduction": red,
                "unblocked": obs["unblocked_count"],
                "zero_partial": obs["zero_partial"],
                "prefix_gap": obs["prefix_gap"],
                "suffix_gap": obs["suffix_gap"],
            })

    # summarize
    op_counts: dict[str, int] = Counter()
    max_red: dict[str, int] = {}
    unblocked_achieved = False
    best_red = 0
    for s in results_list:
        op_family = s["op"].rsplit("_", 1)[0] if s["op"].startswith("block_reverse") else s["op"].split("_")[0]
        op_counts[op_family] += 1
        if s["reduction"] > max_red.get(op_family, 0):
            max_red[op_family] = s["reduction"]
        if s["reduction"] > best_red:
            best_red = s["reduction"]
        if s["unblocked"] > 0:
            unblocked_achieved = True

    return {
        "total_surgeries": len(results_list),
        "unblocked_achieved": unblocked_achieved,
        "best_reduction": best_red,
        "op_breakdown": dict(op_counts),
        "max_reduction_by_op": max_red,
        "baseline_obstruction": baseline,
    }


# ── worker ────────────────────────────────────────────────────────────────

def process_record(record: dict) -> list[dict]:
    p = int(record["p"])
    order = record["final_order"]
    B = record.get("B", [])
    results: list[dict] = []

    for idx, x in enumerate(order):
        s = [*order[:idx], *order[idx+1:]]
        n = len(s)
        if n <= 2 or n > 30:
            continue
        # check valid elements
        if any(not (1 <= v <= p - 1) for v in s):
            continue
        if not is_graham_valid(s, p):
            continue

        fb = find_fully_blocked_perturbation(s, x, p, iters=30000)
        if fb is None:
            continue

        # Check it's actually fully blocked
        obs = compute_obstruction(fb, x, p)
        if obs["unblocked_count"] > 0:
            continue

        surgery = try_surgeries(fb, x, p)
        results.append({
            "p": p,
            "B": B,
            "x": x,
            "k": n,
            "src_line": record.get("_source_line", 0),
            **surgery,
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
    ap.add_argument("--jsonl-out", type=str, default="logs/surgery_large_k.jsonl")
    args = ap.parse_args()

    path = Path(args.witness_jsonl)
    records = list(witness_rows(path))[:args.limit]
    print(f"Records: {len(records)}", file=sys.stderr)

    start = time.monotonic()
    with Pool(args.workers) as pool:
        results = pool.map(process_record, records)
    elapsed = time.monotonic() - start

    flat = [r for rec in results for r in rec]
    print(f"Fully blocked with surgeries: {len(flat)}", file=sys.stderr)
    print(f"Time: {elapsed:.1f}s", file=sys.stderr)

    if not flat:
        print("No fully blocked orderings found.")
        return 0

    unblocked = sum(1 for r in flat if r["unblocked_achieved"])
    print(f"\n=== Surgery Results (Large k via Perturbation) ===")
    print(f"Fully blocked cases: {len(flat)}")
    print(f"Unblocked achieved: {unblocked}/{len(flat)} ({100*unblocked/len(flat):.1f}%)")

    for op_family in ["adjacent", "block", "element", "prefix", "suffix"]:
        count = sum(1 for r in flat if r["op_breakdown"].get(op_family, 0) > 0)
        if count:
            reds = [r["max_reduction_by_op"][op_family] for r in flat if op_family in r.get("max_reduction_by_op", {})]
            avg = sum(reds) / len(reds) if reds else 0
            mx = max(reds) if reds else 0
            print(f"  {op_family}: {count}/{len(flat)} ({100*count/len(flat):.1f}%)  max_red={mx} avg_red={avg:.2f}")

    avg_best = sum(r["best_reduction"] for r in flat) / len(flat)
    print(f"\nAvg best reduction: {avg_best:.2f}")

    by_k: dict[int, int] = Counter()
    by_k_u: dict[int, int] = Counter()
    for r in flat:
        by_k[r["k"]] += 1
        if r["unblocked_achieved"]:
            by_k_u[r["k"]] += 1
    print(f"\nBy k = |S|:")
    for k in sorted(by_k):
        u = by_k_u.get(k, 0)
        print(f"  k={k:3d}: {by_k[k]:4d}  unblocked={u:4d} ({100*u//by_k[k]}%)")

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
