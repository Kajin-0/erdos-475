#!/usr/bin/env python3
"""Empirical verification of Template T1 external cancellation reduction.

Template T1: right blocker D = (z, J) with sum(D) = -a, |D| >= 2.
Move: (a, b, z, J) -> (z, a, b, J).

Tests:
  1. How often does T1 produce a valid (non-blocking) ordering?
  2. When it fails, which failure mode occurs:
     - affine/singleton (z = a+b or z = b-a)
     - proper prefix of J (prefix sum = -a-b or a-b)
     - external collision at new value z or z+a
  3. What does the external collision structure look like?

Output: JSONL with per-case results.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from multiprocessing import Pool, cpu_count
from pathlib import Path
from typing import Any, Sequence


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
    """Return the standard obstruction structure for inserting x into order."""
    n = len(order)
    s = [0]
    acc = 0
    for v in order:
        acc = (acc + v) % p
        s.append(acc)

    blocked = set()
    zero_partial = any(v == 0 for v in s[1:])
    if zero_partial:
        blocked.add(0)

    endpoint_cuts = set()
    for i in range(1, n + 1):
        if (s[i] + x) % p in set(s[1:i+1]):
            endpoint_cuts.add(i)
            blocked.add(i)

    target = (-x) % p
    for k in range(1, n + 1):
        for j in range(k, n + 1):
            if (s[j] - s[k]) % p == target and k < j:
                for i in range(k, j):
                    blocked.add(i)

    blocked |= endpoint_cuts
    unblocked = [i for i in range(n + 1) if i not in blocked]
    return {
        "blocked": len(blocked),
        "unblocked": len(unblocked),
        "unblocked_cuts": unblocked,
        "zero_partial": zero_partial,
    }


def find_right_blockers(order: list[int], x: int, p: int) -> list[dict]:
    """Find right-blocker patterns (a, b, D) with sum(D) = -a in the ordering
    for the purpose of inserting x.

    In the endpoint-avoidance framework, the right blocker occurs when:
    - adjacent_swap at position h-1 fails (where h is the first-hit index)
    - The result is a right blocker: a, b, D with sum(D) = -a

    For empirical verification, we scan the ordering for any adjacent pair
    (a, b) followed by a nonempty D with sum(D) = -a (mod p).
    """
    n = len(order)
    blockers = []
    for i in range(n - 2):
        a = order[i]
        b = order[i + 1]
        # D must be nonempty and follow b
        for j in range(i + 2, n + 1):
            D = order[i + 2:j]
            if not D:
                continue
            sD = sum(D) % p
            if sD == (-a) % p and len(D) >= 2:
                z = D[0]
                J = D[1:]
                blockers.append({
                    "i": i,
                    "a": a,
                    "b": b,
                    "z": z,
                    "J": J,
                    "D": D,
                    "len_D": len(D),
                    "len_J": len(J),
                    "sum_D": sD,
                    "sum_J": sum(J) % p if J else 0,
                })
    return blockers


def test_t1_move(order: list[int], x: int, blk: dict, p: int) -> dict:
    """Test the T1 move: (a, b, z, J) -> (z, a, b, J).

    Records whether the result is valid, and if not, which failure mode.
    """
    a, b, z = blk["a"], blk["b"], blk["z"]
    J = blk["J"]
    i = blk["i"]

    # Extract the full ordering elements before and after
    prefix = order[:i]
    suffix = order[i + 2 + len(blk["D"]):]  # skip past a,b,D

    # Build T1 result: prefix + (z, a, b, J) + suffix
    t1_order = prefix + [z, a, b] + J + suffix

    baseline_obs = compute_obstruction(order, x, p)
    t1_valid = is_graham_valid(t1_order, p)

    if t1_valid:
        t1_obs = compute_obstruction(t1_order, x, p)
        return {
            "t1_valid": True,
            "t1_has_unblocked": t1_obs["unblocked"] > 0,
            "t1_unblocked_cuts": t1_obs["unblocked_cuts"],
            "failure_mode": None,
        }

    # Classify failure
    failure = []

    # Affine/singleton: z = a+b or z = b-a
    if z == (a + b) % p:
        failure.append("z_eq_a+b")
    if z == (b - a) % p:
        failure.append("z_eq_b-a")

    # Proper prefix of J
    ps = 0
    for idx, val in enumerate(J):
        ps = (ps + val) % p
        if ps == (-a - b) % p:
            failure.append(f"prefix_J_eq_-a-b@{idx+1}")
        if ps == (a - b) % p:
            failure.append(f"prefix_J_eq_a-b@{idx+1}")

    # Check if t1_order is Graham-invalid due to collision
    # Compute what the new partial sums would be
    t1_obs = compute_obstruction(t1_order, x, p)

    # We can check if external collision occurred by examining
    # whether the new values z and z+a appear in the partial sums
    # But the obstruction analysis only tells us about blocked cuts for x,
    # not about collisions in the ordering itself.
    # For ordering validity, we already checked is_graham_valid above.
    if not t1_valid:
        # The T1 move produces an invalid ordering - classify by computing
        # which partial sum repeats
        sums = [0]
        acc = 0
        seen = {0}
        coll_pos = None
        for pos, v in enumerate(t1_order, 1):
            acc = (acc + v) % p
            if acc in seen:
                coll_pos = pos
                break
            seen.add(acc)

        # Determine if the collision involves z or z+a
        # by checking if the collision happens at a position where the
        # new sum would be z or z+a (relative to prefix start)
        # In T1, the new sums start after the prefix
        new_start_idx = i  # position in t1_order where z appears
        if coll_pos is not None:
            if coll_pos == new_start_idx:
                failure.append(f"external_collision_at_z")
            elif coll_pos == new_start_idx + 1:
                failure.append(f"external_collision_at_z+a")

    return {
        "t1_valid": t1_valid,
        "t1_has_unblocked": t1_obs["unblocked"] > 0 if not t1_valid else None,
        "failure_mode": failure if failure else "other_collision",
        "t1_collision_position": coll_pos if not t1_valid else None,
    }


def process_row(rec: dict) -> list[dict]:
    p = rec["p"]
    order = rec["final_order"]
    B = rec.get("B", [])
    results = []

    for idx, x in enumerate(order):
        elements = [*order[:idx], *order[idx+1:]]
        if len(elements) <= 3 or len(elements) > 30:
            continue
        if any(not (1 <= v <= p - 1) for v in elements):
            continue
        if not is_graham_valid(elements, p):
            continue

        # Find right-blocker patterns
        blockers = find_right_blockers(elements, x, p)
        for blk in blockers:
            t1 = test_t1_move(elements, x, blk, p)
            results.append({
                "p": p,
                "B": B,
                "x": x,
                "k": len(elements),
                "a": blk["a"],
                "b": blk["b"],
                "z": blk["z"],
                "len_D": blk["len_D"],
                "len_J": blk["len_J"],
                "t1_valid": t1["t1_valid"],
                "t1_has_unblocked": t1.get("t1_has_unblocked"),
                "failure_mode": t1.get("failure_mode"),
            })

    return results


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

        sample = rows[:200]
        print(f"  Processing {len(sample)} rows...", file=sys.stderr)

        with Pool(cpu_count()) as pool:
            batch = pool.map(process_row, sample)

        for br in batch:
            all_records.extend(br)

    total = len(all_records)
    if total == 0:
        print("No right-blocker patterns found.", file=sys.stderr)
        # Try direct search across more rows
        print("Running direct search on larger sample...", file=sys.stderr)
        for wp in witness_paths:
            if not wp.exists():
                continue
            with wp.open() as f:
                rows = [json.loads(line) for line in f if line.strip()]
            rows = rows[:500]
            for rec in rows:
                all_records.extend(process_row(rec))
        total = len(all_records)
        if total == 0:
            print("Still no right-blocker patterns found.", file=sys.stderr)
            return 1

    valid = sum(1 for r in all_records if r["t1_valid"])
    has_unblocked = sum(1 for r in all_records if r["t1_has_unblocked"])

    # Failure mode breakdown
    failures = [r for r in all_records if not r["t1_valid"]]
    fm_counter = Counter()
    for r in failures:
        fm = r["failure_mode"]
        if isinstance(fm, list):
            for f in fm:
                fm_counter[f] += 1
        else:
            fm_counter[str(fm)] += 1

    print("=" * 60)
    print("Template T1 Verification Results")
    print("=" * 60)
    print(f"Right-blocker patterns found: {total}")
    print(f"T1 move produces valid ordering: {valid}/{total} ({100*valid/total:.1f}%)")
    print(f"T1 move creates unblocked cut: {has_unblocked}/{valid if valid else 1} ({100*has_unblocked/max(valid,1):.1f}% of valid)")
    print()
    print(f"Failure modes ({total - valid} cases):")
    for fm, cnt in fm_counter.most_common():
        print(f"  {fm}: {cnt} ({100*cnt/max(total-valid,1):.1f}%)")

    out_path = Path("logs/template_t1_verification.jsonl")
    with out_path.open("w") as f:
        for r in all_records:
            f.write(json.dumps(r, sort_keys=True, separators=(",", ":")) + "\n")
    print(f"\nOutput: {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
