#!/usr/bin/env python3
"""
Finite search for A41 balanced-transfer difference walks.

A41 reduced the balanced D2 branch to a paired-difference walk

    D_r = sum(c_1..c_r) - sum(y_1..y_r)

with

    D_0 = 0,
    D_k = target,

and the residual case requires:

    D_1,...,D_{k-1} avoid 0 and target,
    D_0,...,D_k are pairwise distinct,
    increments c_r-y_r are nonzero,
    c_r and y_r are disjoint atoms from F_p^*.

This script searches for such residual walks over small prime fields.

Important limitation:
    This is a local model for the balanced-transfer obstruction only.  It does
    not enforce all global Graham-validity constraints of the original theorem.
    A found example is therefore only a local residual witness, not a
    counterexample to the theorem.
"""

from __future__ import annotations

import argparse
import itertools
import json
from typing import Dict, Iterator, List, Optional, Sequence, Tuple


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def residues(p: int) -> List[int]:
    return list(range(1, p))


def diff_walk(C: Sequence[int], Y: Sequence[int], p: int) -> List[int]:
    D = [0]
    s = 0
    for c, y in zip(C, Y):
        s = (s + c - y) % p
        D.append(s)
    return D


def is_residual_walk(C: Sequence[int], Y: Sequence[int], p: int, target: int) -> bool:
    if len(C) != len(Y):
        return False
    if target % p == 0:
        return False
    target %= p
    # Atoms must be nonzero and disjoint as a local model of disjoint blocks.
    atoms = list(C) + list(Y)
    if any(a % p == 0 for a in atoms):
        return False
    if len(set(atoms)) != len(atoms):
        return False
    # Increments must be nonzero.
    if any((c - y) % p == 0 for c, y in zip(C, Y)):
        return False
    D = diff_walk(C, Y, p)
    if D[-1] != target:
        return False
    if len(set(D)) != len(D):
        return False
    for d in D[1:-1]:
        if d == 0 or d == target:
            return False
    return True


def search_residual_walks(p: int, k: int, target: Optional[int], limit: int) -> List[Dict[str, object]]:
    if not is_prime(p):
        raise ValueError("p must be prime")
    if k <= 0:
        raise ValueError("k must be positive")
    if 2 * k > p - 1:
        # Cannot choose 2k disjoint nonzero atoms from F_p^*.
        return []

    targets = [target % p] if target is not None else list(range(1, p))
    out: List[Dict[str, object]] = []
    vals = residues(p)

    # Brute force over ordered disjoint C and Y blocks.  This is factorial-scale;
    # intended only for small p,k.
    for C in itertools.permutations(vals, k):
        remaining = [v for v in vals if v not in C]
        for Y in itertools.permutations(remaining, k):
            for T in targets:
                if is_residual_walk(C, Y, p, T):
                    out.append({
                        "p": p,
                        "k": k,
                        "target": T,
                        "C": list(C),
                        "Y": list(Y),
                        "D": diff_walk(C, Y, p),
                        "increments": [((c - y) % p) for c, y in zip(C, Y)],
                    })
                    if len(out) >= limit:
                        return out
    return out


def summarize(max_p: int, max_k: int, limit_per_case: int) -> Dict[str, object]:
    rows: List[Dict[str, object]] = []
    for p in range(3, max_p + 1):
        if not is_prime(p):
            continue
        for k in range(1, max_k + 1):
            if 2 * k > p - 1:
                continue
            examples = search_residual_walks(p, k, None, limit_per_case)
            rows.append({
                "p": p,
                "k": k,
                "found": len(examples),
                "examples": examples,
            })
    return {
        "max_p": max_p,
        "max_k": max_k,
        "limit_per_case": limit_per_case,
        "rows": rows,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--single", action="store_true", help="Search one p,k,target case")
    mode.add_argument("--sweep", action="store_true", help="Sweep p<=max-p and k<=max-k")
    ap.add_argument("--p", type=int)
    ap.add_argument("--k", type=int)
    ap.add_argument("--target", type=int)
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--max-p", type=int, default=17)
    ap.add_argument("--max-k", type=int, default=4)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.single:
        if args.p is None or args.k is None:
            ap.error("--single requires --p and --k")
        result: object = {
            "examples": search_residual_walks(args.p, args.k, args.target, args.limit)
        }
    else:
        result = summarize(args.max_p, args.max_k, args.limit)

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
