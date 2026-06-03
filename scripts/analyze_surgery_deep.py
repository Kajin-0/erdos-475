#!/usr/bin/env python3
"""Deep surgery analysis: record exact positions and condition changes.

For each successful surgery on a fully blocked ordering, record:
1. Which position(s) were modified
2. Which of the three necessary conditions was broken
3. What the resulting gap structure looks like
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

    first_cross_k = min((k for k, j in crossing), default=n + 1)
    last_cross_j = max((j for k, j in crossing), default=0)

    # Determine which conditions hold
    cond_a = zero_partial  # cut 0 blocked
    # cond b: cut 1 blocked by crossing (1,j)
    cond_b = any(k == 1 for k, j in crossing)
    # cond c: cut n blocked by endpoint
    cond_c = n in endpoint_cuts

    return {
        "blocked_count": len(blocked),
        "unblocked_count": len(unblocked),
        "unblocked_cuts": unblocked,
        "zero_partial": zero_partial,
        "cond_a": cond_a,
        "cond_b": cond_b,
        "cond_c": cond_c,
        "endpoint_cuts": sorted(endpoint_cuts),
        "crossing_count": len(crossing),
        "first_cross_k": first_cross_k,
        "last_cross_j": last_cross_j,
        "prefix_gap": first_cross_k - 1,
        "suffix_gap": len(order) - last_cross_j,
    }


# ── surgery with detailed outcome ─────────────────────────────────────────

def try_surgeries_detailed(order: list[int], x: int, p: int) -> list[dict]:
    n = len(order)
    baseline = compute_obstruction(order, x, p)
    results: list[dict] = []

    # adjacent swaps
    for i in range(n - 1):
        r = list(order)
        r[i], r[i + 1] = r[i + 1], r[i]
        if not is_graham_valid(r, p):
            continue
        obs = compute_obstruction(r, x, p)
        results.append({
            "op": "adjacent_swap", "pos": i, "pos2": i + 1,
            "reduction": baseline["blocked_count"] - obs["blocked_count"],
            "unblocked": obs["unblocked_count"],
            "cond_a_broken": baseline["cond_a"] and not obs["cond_a"],
            "cond_b_broken": baseline["cond_b"] and not obs["cond_b"],
            "cond_c_broken": baseline["cond_c"] and not obs["cond_c"],
            "prefix_gap_created": obs["prefix_gap"] > 0,
            "suffix_gap_created": obs["suffix_gap"] > 0,
            "result_unblocked_cuts": obs["unblocked_cuts"],
        })

    # block reverses (len 2-4)
    for length in range(2, min(5, n + 1)):
        for i in range(n - length + 1):
            r = list(order)
            r[i:i+length] = reversed(r[i:i+length])
            if not is_graham_valid(r, p):
                continue
            obs = compute_obstruction(r, x, p)
            results.append({
                "op": f"block_reverse_{length}", "pos": i, "pos2": i + length - 1,
                "reduction": baseline["blocked_count"] - obs["blocked_count"],
                "unblocked": obs["unblocked_count"],
                "cond_a_broken": baseline["cond_a"] and not obs["cond_a"],
                "cond_b_broken": baseline["cond_b"] and not obs["cond_b"],
                "cond_c_broken": baseline["cond_c"] and not obs["cond_c"],
                "prefix_gap_created": obs["prefix_gap"] > 0,
                "suffix_gap_created": obs["suffix_gap"] > 0,
                "result_unblocked_cuts": obs["unblocked_cuts"],
            })

    # element moves (sampled)
    pairs = set()
    for _ in range(100):
        src = random.randrange(n)
        dst = random.randrange(n + 1)
        if dst != src and dst != src + 1:
            pairs.add((src, dst))
    for src, dst in pairs:
        r = list(order)
        val = r.pop(src)
        r.insert(dst, val)
        if not is_graham_valid(r, p):
            continue
        obs = compute_obstruction(r, x, p)
        results.append({
            "op": "element_move", "pos": src, "pos2": dst,
            "reduction": baseline["blocked_count"] - obs["blocked_count"],
            "unblocked": obs["unblocked_count"],
            "cond_a_broken": baseline["cond_a"] and not obs["cond_a"],
            "cond_b_broken": baseline["cond_b"] and not obs["cond_b"],
            "cond_c_broken": baseline["cond_c"] and not obs["cond_c"],
            "prefix_gap_created": obs["prefix_gap"] > 0,
            "suffix_gap_created": obs["suffix_gap"] > 0,
            "result_unblocked_cuts": obs["unblocked_cuts"],
        })

    return results


def find_fully_blocked_perturbation(start: list[int], x: int, p: int, iters: int = 30000) -> list[int] | None:
    current = list(start)
    cur_blocked = compute_obstruction(current, x, p)["blocked_count"]
    best = (cur_blocked, list(current))

    for _ in range(iters):
        idx = random.randrange(len(current))
        val = current.pop(idx)
        pos = random.randrange(len(current) + 1)
        current.insert(pos, val)
        if not is_graham_valid(current, p):
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
            val2 = current.pop(pos)
            current.insert(idx, val2)

    return best[1] if best[0] >= len(start) else None


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
        if any(not (1 <= v <= p - 1) for v in s):
            continue
        if not is_graham_valid(s, p):
            continue

        fb = find_fully_blocked_perturbation(s, x, p, iters=30000)
        if fb is None:
            continue

        obs = compute_obstruction(fb, x, p)
        if obs["unblocked_count"] > 0:
            continue

        surgeries = try_surgeries_detailed(fb, x, p)
        # Only record successful ones
        successful = [s for s in surgeries if s["unblocked"] > 0]
        if not successful:
            continue

        # Summarize which conditions broke and how
        a_broken = sum(1 for s in successful if s["cond_a_broken"])
        b_broken = sum(1 for s in successful if s["cond_b_broken"])
        c_broken = sum(1 for s in successful if s["cond_c_broken"])
        prefix_gap = sum(1 for s in successful if s["prefix_gap_created"])
        suffix_gap = sum(1 for s in successful if s["suffix_gap_created"])

        # Best surgery detail
        best = max(successful, key=lambda s: s["reduction"])

        results.append({
            "p": p,
            "B": B,
            "x": x,
            "k": n,
            "src_line": record.get("_source_line", 0),
            "baseline": baseline_summary(baseline := compute_obstruction(fb, x, p)),
            "num_successful_surgeries": len(successful),
            "cond_a_broken_count": a_broken,
            "cond_b_broken_count": b_broken,
            "cond_c_broken_count": c_broken,
            "prefix_gap_created_count": prefix_gap,
            "suffix_gap_created_count": suffix_gap,
            "best_op": best["op"],
            "best_reduction": best["reduction"],
            "best_pos": best["pos"],
            "best_pos2": best["pos2"],
            "best_broke_a": best["cond_a_broken"],
            "best_broke_b": best["cond_b_broken"],
            "best_broke_c": best["cond_c_broken"],
            "best_prefix_gap": best["prefix_gap_created"],
            "best_suffix_gap": best["suffix_gap_created"],
            "best_unblocked_cuts": best["result_unblocked_cuts"],
        })

    return results


def baseline_summary(b: dict) -> dict:
    return {
        "blocked": b["blocked_count"],
        "cond_a": b["cond_a"],
        "cond_b": b["cond_b"],
        "cond_c": b["cond_c"],
        "prefix_gap": b["prefix_gap"],
        "suffix_gap": b["suffix_gap"],
    }


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
    ap.add_argument("--limit", type=int, default=300)
    ap.add_argument("--workers", type=int, default=cpu_count())
    ap.add_argument("--jsonl-out", type=str, default="logs/surgery_deep_analysis.jsonl")
    args = ap.parse_args()

    path = Path(args.witness_jsonl)
    records = list(witness_rows(path))[:args.limit]
    print(f"Records: {len(records)}", file=sys.stderr)

    start = time.monotonic()
    with Pool(args.workers) as pool:
        results = pool.map(process_record, records)
    elapsed = time.monotonic() - start

    flat = [r for rec in results for r in rec]
    print(f"Cases with successful surgery: {len(flat)}", file=sys.stderr)
    print(f"Time: {elapsed:.1f}s", file=sys.stderr)

    if not flat:
        print("No results.")
        return 0

    # What conditions break?
    a_count = sum(1 for r in flat if r["cond_a_broken_count"] > 0)
    b_count = sum(1 for r in flat if r["cond_b_broken_count"] > 0)
    c_count = sum(1 for r in flat if r["cond_c_broken_count"] > 0)
    print(f"\n=== Conditions Broken by Surgery ===")
    print(f"Condition A (zero partial sum) broken:  {a_count}/{len(flat)} ({100*a_count/len(flat):.1f}%)")
    print(f"Condition B (prefix crossing) broken:   {b_count}/{len(flat)} ({100*b_count/len(flat):.1f}%)")
    print(f"Condition C (suffix endpoint) broken:   {c_count}/{len(flat)} ({100*c_count/len(flat):.1f}%)")

    pg = sum(1 for r in flat if r["prefix_gap_created_count"] > 0)
    sg = sum(1 for r in flat if r["suffix_gap_created_count"] > 0)
    print(f"Prefix gap created: {pg}/{len(flat)} ({100*pg/len(flat):.1f}%)")
    print(f"Suffix gap created: {sg}/{len(flat)} ({100*sg/len(flat):.1f}%)")

    # What does the BEST surgery break?
    ba = sum(1 for r in flat if r["best_broke_a"])
    bb = sum(1 for r in flat if r["best_broke_b"])
    bc = sum(1 for r in flat if r["best_broke_c"])
    print(f"\nBest surgery breaks:")
    print(f"  Only A: {sum(1 for r in flat if r['best_broke_a'] and not r['best_broke_b'] and not r['best_broke_c'])}")
    print(f"  Only B: {sum(1 for r in flat if not r['best_broke_a'] and r['best_broke_b'] and not r['best_broke_c'])}")
    print(f"  Only C: {sum(1 for r in flat if not r['best_broke_a'] and not r['best_broke_b'] and r['best_broke_c'])}")
    print(f"  A+B:    {sum(1 for r in flat if r['best_broke_a'] and r['best_broke_b'] and not r['best_broke_c'])}")
    print(f"  A+C:    {sum(1 for r in flat if r['best_broke_a'] and not r['best_broke_b'] and r['best_broke_c'])}")
    print(f"  B+C:    {sum(1 for r in flat if not r['best_broke_a'] and r['best_broke_b'] and r['best_broke_c'])}")
    print(f"  A+B+C:  {sum(1 for r in flat if r['best_broke_a'] and r['best_broke_b'] and r['best_broke_c'])}")
    print(f"  None:   {sum(1 for r in flat if not r['best_broke_a'] and not r['best_broke_b'] and not r['best_broke_c'])}")

    # Which operation was best?
    op_dist = Counter(r["best_op"].split("_")[0] for r in flat)
    print(f"\nBest operation distribution: {dict(sorted(op_dist.items()))}")

    # Position analysis for best surgery
    positions = Counter()
    for r in flat:
        op = r["best_op"]
        pos = r["best_pos"]
        positions[f"{op}@{pos}"] += 1
    print(f"\nTop 20 best surgery positions:")
    for k, v in positions.most_common(20):
        print(f"  {k}: {v}")

    # Unblocked cut distribution
    all_uc: list[int] = []
    for r in flat:
        all_uc.extend(r["best_unblocked_cuts"])
    uc_dist = Counter(all_uc)
    print(f"\nUnblocked cut positions (top 10):")
    for cut, cnt in uc_dist.most_common(10):
        names = {0: "cut 0", 1: "cut 1", "n": "cut n"}
        label = names.get(cut, f"cut {cut}")
        print(f"  {label}: {cnt}")

    # by k
    by_k: dict[int, dict] = {}
    for r in flat:
        k = r["k"]
        if k not in by_k:
            by_k[k] = {"total": 0, "a": 0, "b": 0, "c": 0}
        by_k[k]["total"] += 1
        if r["best_broke_a"]:
            by_k[k]["a"] += 1
        if r["best_broke_b"]:
            by_k[k]["b"] += 1
        if r["best_broke_c"]:
            by_k[k]["c"] += 1
    print(f"\nBy k:")
    for k in sorted(by_k):
        d = by_k[k]
        print(f"  k={k:3d}: n={d['total']:4d}  A={100*d['a']//d['total']}%  B={100*d['b']//d['total']}%  C={100*d['c']//d['total']}%")

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
