#!/usr/bin/env python3
"""Analyze structural patterns of fully-blocked vs unblocked valid orderings.

For each (S, y) pair where S=A\{x} and both fully-blocked and unblocked valid
orderings exist, this script compares the crossing-interval structure, endpoint
obstruction patterns, and partial-sum geometry to extract distinguishing
features.

Output: JSONL + summary stats, plus structural rule candidates for the
existence theorem proof.
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


# ── shared utilities ──────────────────────────────────────────────────────

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
    n = len(order)
    s = extended_partials(order, p)
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

    blocked = {i for i, m in enumerate(multiplicities) if m > 0}
    blocked |= endpoint_cuts
    unblocked = [i for i in range(n + 1) if i not in blocked]

    # structural features
    crossing.sort()
    total_cross_len = sum(j - k for k, j in crossing)
    crossing_cover = set()
    for k, j in crossing:
        crossing_cover.update(range(k, j))
    crossing_cover_pct = len(crossing_cover) / max(n, 1) if n > 0 else 0

    # longest crossing interval
    max_cross_len = max((j - k for k, j in crossing), default=0)

    # prefix gap: cuts before first crossing interval
    first_cross_k = min((k for k, j in crossing), default=n+1)
    prefix_gap = first_cross_k - 1  # cuts 1..first_cross_k-1 not covered by crossing

    # suffix gap: cuts after last crossing interval
    last_cross_j = max((j for k, j in crossing), default=0)
    suffix_gap = n - last_cross_j  # cuts last_cross_j+1..n not covered by crossing

    # endpoint-blocked cuts not covered by crossing
    endpoint_only = endpoint_cuts - crossing_cover

    return {
        "blocked_count": len(blocked),
        "unblocked_count": len(unblocked),
        "blocked_cuts": sorted(blocked),
        "unblocked_cuts": unblocked,
        "endpoint_count": len(endpoint_cuts),
        "endpoint_cuts": sorted(endpoint_cuts),
        "zero_partial": zero_partial,
        "zero_partial_blocks_cut0": zero_partial,
        "crossing_count": len(crossing),
        "crossing_intervals": crossing,
        "total_cross_len": total_cross_len,
        "max_cross_len": max_cross_len,
        "crossing_cover_pct": crossing_cover_pct,
        "prefix_gap": prefix_gap,
        "suffix_gap": suffix_gap,
        "endpoint_only_count": len(endpoint_only),
        "endpoint_only_cuts": sorted(endpoint_only),
        "cut_multiplicities": multiplicities,
        "first_cross_k": first_cross_k,
        "last_cross_j": last_cross_j,
    }


# ── search strategies ─────────────────────────────────────────────────────

def find_good_ordering(elements: list[int], x: int, p: int, max_trials: int = 200000) -> dict | None:
    """Find any valid ordering with unblocked cuts."""
    for _ in range(max_trials):
        perm = list(elements)
        random.shuffle(perm)
        if not is_graham_valid(perm, p):
            continue
        obs = compute_insertion_obstruction(perm, x, p)
        if obs["unblocked_count"] > 0:
            return {**obs, "order": perm}
    return None


def find_fully_blocked_ordering(elements: list[int], x: int, p: int, max_trials: int = 200000) -> dict | None:
    """Find a fully blocked valid ordering."""
    best_worst: dict | None = None
    for _ in range(max_trials):
        perm = list(elements)
        random.shuffle(perm)
        if not is_graham_valid(perm, p):
            continue
        obs = compute_insertion_obstruction(perm, x, p)
        if best_worst is None or obs["blocked_count"] > best_worst["blocked_count"]:
            best_worst = {**obs, "order": perm}
            if obs["unblocked_count"] == 0:
                return best_worst
    return best_worst


# ── structural comparison ─────────────────────────────────────────────────

@dataclass
class ComparisonResult:
    p: int
    B: list[int]
    x: int
    k: int
    source_line: int
    has_good: bool
    has_fully_blocked: bool
    good_obs: dict | None = None
    fully_blocked_obs: dict | None = None

    def features(self) -> dict:
        return {
            "p": self.p,
            "B": self.B,
            "x": self.x,
            "k": self.k,
            "has_good": self.has_good,
            "has_fully_blocked": self.has_fully_blocked,
            "good_unblocked": self.good_obs["unblocked_count"] if self.good_obs else None,
            "fb_blocked": self.fully_blocked_obs["blocked_count"] if self.fully_blocked_obs else None,
            "good_cross_count": self.good_obs["crossing_count"] if self.good_obs else None,
            "fb_cross_count": self.fully_blocked_obs["crossing_count"] if self.fully_blocked_obs else None,
            "good_prefix_gap": self.good_obs["prefix_gap"] if self.good_obs else None,
            "fb_prefix_gap": self.fully_blocked_obs["prefix_gap"] if self.fully_blocked_obs else None,
            "good_suffix_gap": self.good_obs["suffix_gap"] if self.good_obs else None,
            "fb_suffix_gap": self.fully_blocked_obs["suffix_gap"] if self.fully_blocked_obs else None,
            "good_endpoint_count": self.good_obs["endpoint_count"] if self.good_obs else None,
            "fb_endpoint_count": self.fully_blocked_obs["endpoint_count"] if self.fully_blocked_obs else None,
            "good_zero_partial": self.good_obs["zero_partial"] if self.good_obs else None,
            "fb_zero_partial": self.fully_blocked_obs["zero_partial"] if self.fully_blocked_obs else None,
            "good_max_cross_len": self.good_obs["max_cross_len"] if self.good_obs else None,
            "fb_max_cross_len": self.fully_blocked_obs["max_cross_len"] if self.fully_blocked_obs else None,
            "good_cross_cover_pct": self.good_obs["crossing_cover_pct"] if self.good_obs else None,
            "fb_cross_cover_pct": self.fully_blocked_obs["crossing_cover_pct"] if self.fully_blocked_obs else None,
        }


def process_record(record: dict) -> list[dict]:
    p = int(record["p"])
    order = record["final_order"]
    B = record.get("B", [])
    source_line = record.get("_source_line", 0)

    results: list[dict] = []
    for idx, x in enumerate(order):
        s = [*order[:idx], *order[idx+1:]]
        base = {"p": p, "B": B, "x": x, "|A|": len(order), "k": len(s), "source_line": source_line}

        for v in s:
            if not (1 <= v <= p - 1):
                break
        else:
            pass

        if len(s) <= 2:
            continue

        if not is_graham_valid(s, p):
            results.append({**base, "native_valid": False, "has_good": False, "has_fully_blocked": False})
            continue

        good = find_good_ordering(s, x, p, max_trials=5000)
        fb = find_fully_blocked_ordering(s, x, p, max_trials=5000)

        comp = ComparisonResult(
            p=p,
            B=B,
            x=x,
            k=len(s),
            source_line=source_line,
            has_good=good is not None,
            has_fully_blocked=fb is not None and fb["unblocked_count"] == 0,
            good_obs=good,
            fully_blocked_obs=fb if (fb and fb["unblocked_count"] == 0) else None,
        )
        feat = comp.features()
        feat["native_valid"] = True
        feat["native_blocked"] = compute_insertion_obstruction(s, x, p)["blocked_count"]
        results.append({**base, **feat})

    return results


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


# ── main ──────────────────────────────────────────────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("witness_jsonl", type=str)
    ap.add_argument("--limit", type=int, default=200)
    ap.add_argument("--workers", type=int, default=cpu_count())
    ap.add_argument("--jsonl-out", type=str, default="logs/blocking_pattern_analysis.jsonl")
    args = ap.parse_args()

    path = Path(args.witness_jsonl)
    records: list[dict] = []
    for row in witness_rows(path):
        records.append(row)
        if args.limit and len(records) >= args.limit:
            break

    print(f"Records loaded: {len(records)}", file=sys.stderr)

    start = time.monotonic()
    with Pool(args.workers) as pool:
        all_results = pool.map(process_record, records)
    elapsed = time.monotonic() - start

    flat = [r for rec in all_results for r in rec]
    print(f"Total triples: {len(flat)}", file=sys.stderr)
    print(f"Search time: {elapsed:.1f}s", file=sys.stderr)

    # Summary stats
    valid = [r for r in flat if r.get("native_valid")]
    good_found = [r for r in valid if r.get("has_good")]
    fb_found = [r for r in valid if r.get("has_fully_blocked")]
    both_found = [r for r in valid if r.get("has_good") and r.get("has_fully_blocked")]

    print(f"\nValid deletions: {len(valid)}")
    print(f"Good ordering (unblocked cuts) found: {len(good_found)}")
    print(f"Fully blocked ordering found: {len(fb_found)}")
    print(f"Both found (comparable): {len(both_found)}")

    if both_found:
        # Compare structural features
        print("\n=== Structural comparison: good vs fully blocked ===")
        # prefix gap
        pg_good = [r["good_prefix_gap"] for r in both_found]
        pg_fb = [r["fb_prefix_gap"] for r in both_found]
        print(f"Prefix gap:  good avg={sum(pg_good)/len(pg_good):.2f}  fb avg={sum(pg_fb)/len(pg_fb):.2f}")
        print(f"  good min={min(pg_good)} max={max(pg_good)}  fb min={min(pg_fb)} max={max(pg_fb)}")

        sg_good = [r["good_suffix_gap"] for r in both_found]
        sg_fb = [r["fb_suffix_gap"] for r in both_found]
        print(f"Suffix gap:  good avg={sum(sg_good)/len(sg_good):.2f}  fb avg={sum(sg_fb)/len(sg_fb):.2f}")

        cc_good = [r["good_cross_count"] for r in both_found]
        cc_fb = [r["fb_cross_count"] for r in both_found]
        print(f"Crossing count:  good avg={sum(cc_good)/len(cc_good):.2f}  fb avg={sum(cc_fb)/len(cc_fb):.2f}")

        ml_good = [r["good_max_cross_len"] for r in both_found]
        ml_fb = [r["fb_max_cross_len"] for r in both_found]
        print(f"Max cross len:  good avg={sum(ml_good)/len(ml_good):.2f}  fb avg={sum(ml_fb)/len(ml_fb):.2f}")

        ec_good = [r["good_endpoint_count"] for r in both_found]
        ec_fb = [r["fb_endpoint_count"] for r in both_found]
        print(f"Endpoint count:  good avg={sum(ec_good)/len(ec_good):.2f}  fb avg={sum(ec_fb)/len(ec_fb):.2f}")

        zp_good = sum(1 for r in both_found if r.get("good_zero_partial"))
        zp_fb = sum(1 for r in both_found if r.get("fb_zero_partial"))
        print(f"Zero partial:  good={zp_good}/{len(both_found)}  fb={zp_fb}/{len(both_found)}")

        cross_cover_good = [r["good_cross_cover_pct"] for r in both_found]
        cross_cover_fb = [r["fb_cross_cover_pct"] for r in both_found]
        print(f"Crossing cover %%:  good avg={sum(cross_cover_good)/len(cross_cover_good):.1f}  fb avg={sum(cross_cover_fb)/len(cross_cover_fb):.1f}")

        # key question: what distinguishes good from fully blocked?
        gap_diff = [pg_good[i] + sg_good[i] - (pg_fb[i] + sg_fb[i]) for i in range(len(both_found))]
        larger_gap_in_good = sum(1 for d in gap_diff if d > 0)
        print(f"\nGood ordering has larger total gap (prefix+suffix): {larger_gap_in_good}/{len(both_found)}")
        print(f"Good ordering avg total gap: {sum(pg_good[i]+sg_good[i] for i in range(len(both_found)))/len(both_found):.2f}")
        print(f"FB ordering avg total gap:   {sum(pg_fb[i]+sg_fb[i] for i in range(len(both_found)))/len(both_found):.2f}")

        # Count long-interval cases vs interval-stacking cases in fully blocked
        max_k = max(r["k"] for r in both_found)
        long_interval_fb = sum(1 for r in both_found if r["fb_max_cross_len"] >= r["k"])
        stacking_fb = len(both_found) - long_interval_fb
        print(f"\nFully blocked strategies:  long interval (max_cross_len >= k): {long_interval_fb}  stacking: {stacking_fb}")

        # Does good ordering always have a suffix or prefix gap?
        has_gap_good = sum(1 for r in both_found if r["good_prefix_gap"] > 0 or r["good_suffix_gap"] > 0)
        print(f"Good ordering has prefix or suffix gap: {has_gap_good}/{len(both_found)}")

        # How many good orderings have gap at cut 0 or n?
        cut0_or_n_good = sum(1 for r in both_found if 0 in (r.get("good_obs") or {}).get("unblocked_cuts", []) or r["k"] in (r.get("good_obs") or {}).get("unblocked_cuts", []))
        print(f"Good ordering has cut 0 or cut n unblocked: checking...")

    if args.jsonl_out:
        out_path = Path(args.jsonl_out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("w", encoding="utf-8") as fh:
            for r in flat:
                fh.write(json.dumps(r, sort_keys=True, separators=(",", ":")) + "\n")
        print(f"\nFull results: {args.jsonl_out}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
