#!/usr/bin/env python3
"""Deeper analysis: cut-n obstruction patterns and structural invariants.

Key questions:
1. For fully blocked orderings, how is cut n blocked? (endpoint vs crossing)
2. Is zero_partial necessary for full blockage? (100% in sample)
3. What is the minimal crossing configuration for full blockage?
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

def extended_partials(order: Sequence[int], p: int) -> list[int]:
    return [0, *nonempty_partials(order, p)]

def is_graham_valid(order: Sequence[int], p: int) -> bool:
    sums = nonempty_partials(order, p)
    return len(sums) == len(set(sums))

def analyze_deep(order: Sequence[int], x: int, p: int) -> dict:
    n = len(order)
    s = extended_partials(order, p)
    multiplicities = [0] * (n + 1)
    endpoint_cuts: set[int] = set()
    endpoint_pairs: list[tuple[int, int]] = []

    zero_partial = any(v == 0 for v in s[1:])
    if zero_partial:
        multiplicities[0] += 1

    for i in range(1, n + 1):
        inserted_sum = (s[i] + x) % p
        for k in range(1, i + 1):
            if inserted_sum == s[k]:
                endpoint_cuts.add(i)
                multiplicities[i] += 1
                endpoint_pairs.append((k, i))
                break

    target = (-x) % p
    crossing: list[tuple[int, int]] = []
    for k in range(1, n + 1):
        for j in range(k, n + 1):
            if (s[j] - s[k]) % p == target:
                if k < j:
                    crossing.append((k, j))
                    for i in range(k, j):
                        multiplicities[i] += 1

    blocked = {i for i, m in enumerate(multiplicities) if m > 0}
    blocked |= endpoint_cuts
    unblocked = [i for i in range(n + 1) if i not in blocked]

    crossing_cover = set()
    for k, j in crossing:
        crossing_cover.update(range(k, j))

    endpoint_only = endpoint_cuts - crossing_cover

    first_cross_k = min((k for k, j in crossing), default=n + 1)
    last_cross_j = max((j for k, j in crossing), default=0)
    prefix_gap = first_cross_k - 1
    suffix_gap = n - last_cross_j

    # cut n analysis: is it blocked by endpoint or crossing?
    cut_n_blocked = n in blocked
    cut_n_endpoint = n in endpoint_cuts
    cut_n_crossing_cover = n in crossing_cover  # Should be False by construction
    # Check if there's a crossing pair (k, n) that contributes
    cross_to_n = [c for c in crossing if c[1] == n]

    # cut 0 analysis
    cut_0_blocked = 0 in blocked
    cut_0_zero = zero_partial

    # what's the first crossing interval and last?
    first_ci = crossing[0] if crossing else None
    last_ci = crossing[-1] if crossing else None

    return {
        "n": n,
        "blocked_count": len(blocked),
        "unblocked_count": len(unblocked),
        "unblocked_cuts": unblocked,
        "zero_partial": zero_partial,
        "cut_0_blocked": cut_0_blocked,
        "cut_0_zero": cut_0_zero,
        "cut_n_blocked": cut_n_blocked,
        "cut_n_endpoint": cut_n_endpoint,
        "cross_to_n_count": len(cross_to_n),
        "crossing_count": len(crossing),
        "first_cross_k": first_cross_k,
        "last_cross_j": last_cross_j,
        "prefix_gap": prefix_gap,
        "suffix_gap": suffix_gap,
        "endpoint_only_count": len(endpoint_only),
        "endpoint_only_cuts": sorted(endpoint_only),
        "crossing": crossing,
        "prefix_sum_has_zero": zero_partial,
    }


def find_fully_blocked(elements: list[int], x: int, p: int, max_trials: int = 100000) -> dict | None:
    best: dict | None = None
    for _ in range(max_trials):
        perm = list(elements)
        random.shuffle(perm)
        if not is_graham_valid(perm, p):
            continue
        obs = analyze_deep(perm, x, p)
        if best is None or obs["blocked_count"] > best["blocked_count"]:
            best = {**obs, "order": perm}
            if obs["unblocked_count"] == 0:
                return best
    return best


def find_good(elements: list[int], x: int, p: int, max_trials: int = 100000) -> dict | None:
    for _ in range(max_trials):
        perm = list(elements)
        random.shuffle(perm)
        if not is_graham_valid(perm, p):
            continue
        obs = analyze_deep(perm, x, p)
        if obs["unblocked_count"] > 0:
            return {**obs, "order": perm}
    return None


def process(record: dict) -> list[dict]:
    p = int(record["p"])
    order = record["final_order"]
    B = record.get("B", [])
    src = record.get("_source_line", 0)
    results = []

    for idx, x in enumerate(order):
        s = [*order[:idx], *order[idx+1:]]
        if len(s) <= 2:
            continue
        if not is_graham_valid(s, p):
            continue

        base = {"p": p, "B": B, "x": x, "k": len(s), "src": src}

        fb = find_fully_blocked(s, x, p, max_trials=20000)
        good = find_good(s, x, p, max_trials=20000)

        fb_data = fb if fb and fb["unblocked_count"] == 0 else None
        good_data = good if good and good["unblocked_count"] > 0 else None

        if fb_data:
            fb_row = {**base, "type": "fully_blocked",
                      "zero_partial": fb_data["zero_partial"],
                      "cut_n_endpoint": fb_data["cut_n_endpoint"],
                      "cross_to_n": fb_data["cross_to_n_count"],
                      "crossing_count": fb_data["crossing_count"],
                      "prefix_gap": fb_data["prefix_gap"],
                      "suffix_gap": fb_data["suffix_gap"],
                      "endpoint_only": fb_data["endpoint_only_count"],
                      "first_cross_k": fb_data["first_cross_k"],
                      "last_cross_j": fb_data["last_cross_j"],
                      "has_order": True}
            results.append(fb_row)

        if good_data:
            good_row = {**base, "type": "good",
                        "zero_partial": good_data["zero_partial"],
                        "cut_n_endpoint": good_data["cut_n_endpoint"],
                        "cross_to_n": good_data["cross_to_n_count"],
                        "crossing_count": good_data["crossing_count"],
                        "prefix_gap": good_data["prefix_gap"],
                        "suffix_gap": good_data["suffix_gap"],
                        "endpoint_only": good_data["endpoint_only_count"],
                        "first_cross_k": good_data["first_cross_k"],
                        "last_cross_j": good_data["last_cross_j"],
                        "unblocked_cuts": good_data["unblocked_cuts"],
                        "has_order": True}
            results.append(good_row)

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
    ap = argparse.ArgumentParser()
    ap.add_argument("witness_jsonl", type=str)
    ap.add_argument("--limit", type=int, default=300)
    ap.add_argument("--workers", type=int, default=cpu_count())
    ap.add_argument("--jsonl-out", type=str, default="logs/cut_n_analysis.jsonl")
    args = ap.parse_args()

    path = Path(args.witness_jsonl)
    records = list(witness_rows(path))[:args.limit]
    print(f"Records: {len(records)}", file=sys.stderr)

    start = time.monotonic()
    with Pool(args.workers) as pool:
        results = pool.map(process, records)
    elapsed = time.monotonic() - start
    print(f"Time: {elapsed:.1f}s", file=sys.stderr)

    flat = [r for rec in results for r in rec]

    fb = [r for r in flat if r["type"] == "fully_blocked"]
    good = [r for r in flat if r["type"] == "good"]

    print(f"\nFully blocked found: {len(fb)}")
    print(f"Good found: {len(good)}")

    if fb:
        zp = sum(1 for r in fb if r["zero_partial"])
        print(f"Cut 0 blocked by zero partial: {zp}/{len(fb)}")
        cn = sum(1 for r in fb if r["cut_n_endpoint"])
        ctn = sum(1 for r in fb if r["cross_to_n"] > 0)
        both_n = sum(1 for r in fb if r["cut_n_endpoint"] and r["cross_to_n"] > 0)
        print(f"Cut n blocked by endpoint:  {cn}/{len(fb)}")
        print(f"Cut n covered by cross (k,n): {ctn}/{len(fb)}")
        print(f"Both: {both_n}/{len(fb)}")
        only_n_endpoint = sum(1 for r in fb if r["cut_n_endpoint"] and r["cross_to_n"] == 0)
        print(f"Cut n endpoint-only (no crossing): {only_n_endpoint}/{len(fb)}")

        # What blocks cut 0 in fully blocked?
        zpc = Counter(r["zero_partial"] for r in fb)
        print(f"\nZero partial distribution: {dict(sorted(zpc.items()))}")

        # prefix/suffix gaps
        pg = [r["prefix_gap"] for r in fb]
        sg = [r["suffix_gap"] for r in fb]
        print(f"\nPrefix gaps: min={min(pg)} max={max(pg)} avg={sum(pg)/len(pg):.2f}")
        print(f"Suffix gaps: min={min(sg)} max={max(sg)} avg={sum(sg)/len(sg):.2f}")
        print(f"All zero prefix gap: {sum(1 for g in pg if g==0)}/{len(pg)}")
        print(f"All zero suffix gap: {sum(1 for g in sg if g==0)}/{len(sg)}")
        # first_cross_k and last_cross_j
        fck = [r["first_cross_k"] for r in fb]
        lcj = [r["last_cross_j"] for r in fb]
        print(f"first_cross_k = 1: {sum(1 for v in fck if v==1)}/{len(fck)}")
        print(f"last_cross_j = n (=k): {sum(1 for i,v in enumerate(lcj) if v==fb[i]['k'])}/{len(lcj)}")

    if good:
        ug = [r["unblocked_cuts"] for r in good]
        cut0_unblocked = sum(1 for u in ug if 0 in u)
        cut_n_unblocked = sum(1 for i, u in enumerate(ug) if good[i]["k"] in u)
        internal_unblocked = sum(1 for u in ug if any(1 <= c < len(u)-1 for c in u))
        print(f"\nGood orderings: cut 0 unblocked: {cut0_unblocked}/{len(good)}")
        print(f"Good orderings: cut n unblocked: {cut_n_unblocked}/{len(good)}")
        print(f"Good orderings: internal cut unblocked: {internal_unblocked}/{len(good)}")

        first_unblocked = Counter()
        for u in ug:
            first_unblocked[min(u)] += 1
        print(f"\nFirst unblocked cut distribution: {dict(sorted(first_unblocked.items()))}")

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
