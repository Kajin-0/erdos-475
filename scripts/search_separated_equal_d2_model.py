#!/usr/bin/env python3
"""
Finite search for the stronger A44 separated-equal D2 model.

A43 showed that the local A41 balanced-transfer difference-walk residual is
not impossible by itself.  This script strengthens the model by including
blocks

    X A G C Y

with

    sum(A)=sum(C),

and requiring a D2 obstruction for the direct exchange

    X A G C Y -> X C G A Y

while simultaneously excluding the other direct-exchange collision branches
D1, D3, D4, and D5 from A36.

A36 direct-exchange collision equations:

    D1: C_k = a + G_j
    D2: C_k = 2a + g + Y_m
    D3: A_i = G_j - g
    D4: A_i = a + Y_m
    D5: C_k = a + g + A_i

This is still a local algebraic model.  It does not enforce all global
Graham-validity or endpoint-avoidance constraints.
"""

from __future__ import annotations

import argparse
import itertools
import json
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


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


def ps(block: Sequence[int], p: int) -> List[int]:
    out: List[int] = []
    s = 0
    for x in block:
        s = (s + x) % p
        out.append(s)
    return out


def ssum(block: Sequence[int], p: int) -> int:
    return sum(block) % p


def valid_atoms(blocks: Sequence[Sequence[int]], p: int) -> bool:
    atoms = [x % p for block in blocks for x in block]
    return all(x != 0 for x in atoms) and len(set(atoms)) == len(atoms)


def d2_hits(A: Sequence[int], G: Sequence[int], C: Sequence[int], Y: Sequence[int], p: int) -> List[Tuple[int, int]]:
    """Return all (k,m) with C_k = 2a+g+Y_m."""
    a = ssum(A, p)
    g = ssum(G, p)
    Cp = ps(C, p)
    Yp = ps(Y, p)
    hits: List[Tuple[int, int]] = []
    for k, ck in enumerate(Cp, start=1):
        for m, ym in enumerate(Yp, start=1):
            if ck == (2 * a + g + ym) % p:
                hits.append((k, m))
    return hits


def other_obstructions_absent(A: Sequence[int], G: Sequence[int], C: Sequence[int], Y: Sequence[int], p: int) -> bool:
    """Check absence of D1, D3, D4, D5 over all valid internal prefix indices."""
    a = ssum(A, p)
    g = ssum(G, p)
    Ap = ps(A, p)
    Gp = ps(G, p)
    Cp = ps(C, p)
    Yp = ps(Y, p)

    # D1: C_k = a + G_j
    for ck in Cp:
        for gj in Gp:
            if ck == (a + gj) % p:
                return False

    # D3: A_i = G_j - g
    for ai in Ap:
        for gj in Gp:
            if ai == (gj - g) % p:
                return False

    # D4: A_i = a + Y_m
    for ai in Ap:
        for ym in Yp:
            if ai == (a + ym) % p:
                return False

    # D5: C_k = a + g + A_i
    for ck in Cp:
        for ai in Ap:
            if ck == (a + g + ai) % p:
                return False

    return True


def graham_valid_local(blocks: Sequence[Sequence[int]], p: int) -> bool:
    """Optional local Graham distinctness for the concatenated A,G,C,Y segment.

    This is not the full theorem's global condition because X and external
    blocks are omitted.  It simply rejects repeated nonempty partial sums within
    the modeled segment.
    """
    seq = [x for block in blocks for x in block]
    vals: List[int] = []
    s = 0
    for x in seq:
        s = (s + x) % p
        vals.append(s)
    return len(vals) == len(set(vals))


def balanced_walk_residual(C: Sequence[int], Y: Sequence[int], p: int, k: int, target: int) -> bool:
    """A41 residual check for K=prefix_k(C), M=prefix_k(Y)."""
    K = C[:k]
    M = Y[:k]
    D = [0]
    s = 0
    for c, y in zip(K, M):
        inc = (c - y) % p
        if inc == 0:
            return False
        s = (s + inc) % p
        D.append(s)
    if D[-1] != target % p:
        return False
    if len(set(D)) != len(D):
        return False
    for d in D[1:-1]:
        if d == 0 or d == target % p:
            return False
    return True


def search(p: int, len_a: int, len_g: int, len_c: int, len_y: int, limit: int, require_balanced: bool, require_local_graham: bool) -> List[Dict[str, object]]:
    if not is_prime(p):
        raise ValueError("p must be prime")
    total_len = len_a + len_g + len_c + len_y
    if total_len > p - 1:
        return []

    vals = list(range(1, p))
    out: List[Dict[str, object]] = []

    # Brute force permutations for small p only.
    for seq in itertools.permutations(vals, total_len):
        A = seq[:len_a]
        G = seq[len_a:len_a + len_g]
        C = seq[len_a + len_g:len_a + len_g + len_c]
        Y = seq[len_a + len_g + len_c:]

        a = ssum(A, p)
        if a != ssum(C, p):
            continue
        if require_local_graham and not graham_valid_local([A, G, C, Y], p):
            continue
        if not other_obstructions_absent(A, G, C, Y, p):
            continue

        hits = d2_hits(A, G, C, Y, p)
        if not hits:
            continue

        g = ssum(G, p)
        for k, m in hits:
            if require_balanced and m != k:
                continue
            target = (2 * a + g) % p
            if require_balanced and not balanced_walk_residual(C, Y, p, k, target):
                continue
            out.append({
                "p": p,
                "lengths": {"A": len_a, "G": len_g, "C": len_c, "Y": len_y},
                "A": list(A),
                "G": list(G),
                "C": list(C),
                "Y": list(Y),
                "a": a,
                "g": g,
                "target_2a_plus_g": target,
                "d2_hit": {"k": k, "m": m, "balanced": k == m},
                "prefixes": {"A": ps(A, p), "G": ps(G, p), "C": ps(C, p), "Y": ps(Y, p)},
            })
            if len(out) >= limit:
                return out
    return out


def sweep(max_p: int, max_len: int, limit_per_case: int, require_balanced: bool, require_local_graham: bool) -> Dict[str, object]:
    rows: List[Dict[str, object]] = []
    for p in range(5, max_p + 1):
        if not is_prime(p):
            continue
        for len_a in range(1, max_len + 1):
            for len_g in range(1, max_len + 1):
                for len_c in range(1, max_len + 1):
                    for len_y in range(1, max_len + 1):
                        if len_a + len_g + len_c + len_y > p - 1:
                            continue
                        examples = search(p, len_a, len_g, len_c, len_y, limit_per_case, require_balanced, require_local_graham)
                        if examples:
                            rows.append({
                                "p": p,
                                "lengths": {"A": len_a, "G": len_g, "C": len_c, "Y": len_y},
                                "found": len(examples),
                                "examples": examples,
                            })
    return {
        "max_p": max_p,
        "max_len": max_len,
        "limit_per_case": limit_per_case,
        "require_balanced": require_balanced,
        "require_local_graham": require_local_graham,
        "rows": rows,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--single", action="store_true")
    mode.add_argument("--sweep", action="store_true")
    ap.add_argument("--p", type=int)
    ap.add_argument("--A", type=int)
    ap.add_argument("--G", type=int)
    ap.add_argument("--C", type=int)
    ap.add_argument("--Y", type=int)
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--max-p", type=int, default=11)
    ap.add_argument("--max-len", type=int, default=3)
    ap.add_argument("--require-balanced", action="store_true")
    ap.add_argument("--require-local-graham", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.single:
        for name in ["p", "A", "G", "C", "Y"]:
            if getattr(args, name) is None:
                ap.error(f"--single requires --{name}")
        result: object = {
            "examples": search(args.p, args.A, args.G, args.C, args.Y, args.limit, args.require_balanced, args.require_local_graham)
        }
    else:
        result = sweep(args.max_p, args.max_len, args.limit, args.require_balanced, args.require_local_graham)

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
