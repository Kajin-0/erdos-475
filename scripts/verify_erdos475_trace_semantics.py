#!/usr/bin/env python3
"""
Verify trace semantics for the Erdos 475 complement-domain certificate.

This script checks the crucial interpretation:

    B is not the original Erdos set A.
    B is the complement/defect set.
    The ordering being repaired is A = F_p^* \\ B.

For every JSONL trace record it verifies:

1. Q_p is a permutation of F_p^* = {1,...,p-1}.
2. B is a subset of Q_p.
3. initial_order is exactly Q_p \\ B.
4. final_order is a permutation of initial_order.
5. final_partial_sums are exactly the partial sums of final_order.
6. final_partial_sums are pairwise distinct.

Usage:

    python verify_erdos475_trace_semantics.py \
        traces/p29_r3_to_r7_repair_traces_strict.jsonl \
        traces/p31_r3_to_r6_repair_traces_strict.jsonl

Expected:

    VERDICT: PASS
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import sys
from typing import Dict, List, Tuple


def partial_sums(p: int, order: List[int]) -> List[int]:
    s = 0
    out = []
    for x in order:
        s = (s + int(x)) % p
        out.append(s)
    return out


def verify_file(path: str, max_fail_examples: int = 20):
    counts = collections.Counter()
    failures = []
    total = 0

    with open(path, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            if not line.strip():
                continue

            total += 1
            rec = json.loads(line)

            p = int(rec["p"])
            B = [int(x) for x in rec["B"]]
            Q = [int(x) for x in rec["Q_p"]]
            initial = [int(x) for x in rec["initial_order"]]
            final = [int(x) for x in rec["final_order"]]
            final_partial_sums = [int(x) for x in rec["final_partial_sums"]]

            Bset = set(B)
            Qset = set(Q)
            initial_set = set(initial)
            final_set = set(final)
            Fpx = set(range(1, p))

            kB = len(B)
            kA = p - 1 - kB
            counts[(p, kB, kA)] += 1

            def fail(reason: str):
                if len(failures) < max_fail_examples:
                    failures.append({
                        "file": os.path.basename(path),
                        "line": line_no,
                        "p": p,
                        "|B|": kB,
                        "|A|": kA,
                        "reason": reason,
                    })

            if len(Q) != p - 1 or Qset != Fpx:
                fail("Q_p is not a permutation of F_p^*")

            if len(B) != len(Bset):
                fail("B has duplicate entries")

            if not Bset <= Qset:
                fail("B is not a subset of Q_p")

            if len(initial) != kA or initial_set != Qset - Bset or initial_set & Bset:
                fail("initial_order is not exactly Q_p \\ B")

            if len(final) != len(initial) or final_set != initial_set:
                fail("final_order is not a permutation of initial_order")

            computed_ps = partial_sums(p, final)
            if computed_ps != final_partial_sums:
                fail("final_partial_sums do not match final_order")

            if len(final_partial_sums) != len(set(final_partial_sums)):
                fail("final_partial_sums are not pairwise distinct")

    return total, counts, failures


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("trace_jsonl", nargs="+")
    ap.add_argument("--max-fail-examples", type=int, default=20)
    args = ap.parse_args()

    grand_total = 0
    grand_counts = collections.Counter()
    all_failures = []

    print("=== Erdos 475 trace-semantics verifier ===")
    print("Claim checked: initial_order = Q_p \\ B, so B is the complement/defect set.")
    print()

    for path in args.trace_jsonl:
        total, counts, failures = verify_file(path, args.max_fail_examples)
        grand_total += total
        grand_counts.update(counts)
        all_failures.extend(failures)

        print(f"file={path}")
        print(f"records={total}")
        for (p, kB, kA), n in sorted(counts.items()):
            print(f"  p={p} |B|={kB} |A|=p-1-|B|={kA}: {n}")
        print()

    print("Combined complement-domain counts:")
    for (p, kB, kA), n in sorted(grand_counts.items()):
        print(f"  p={p} |B|={kB} |A|={kA}: {n}")
    print()

    print(f"total_records={grand_total}")
    print(f"failures={len(all_failures)}")

    if all_failures:
        print()
        print("Failure examples:")
        for x in all_failures[:args.max_fail_examples]:
            print(
                f"  file={x['file']} line={x['line']} p={x['p']} "
                f"|B|={x['|B|']} |A|={x['|A|']} reason={x['reason']}"
            )
        print()
        print("VERDICT: FAIL")
        return 1

    print("VERDICT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
