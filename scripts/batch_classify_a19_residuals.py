#!/usr/bin/env python3
"""
Batch classifier for A19/A22 residual rows under branch-valid index ranges.

This script enumerates symbolic index configurations for the singleton-prefix
residual families and classifies their equal-interval geometry using

    scripts/classify_a19_residual_row.py

It is a proof-audit tool, not a proof.  It answers questions such as:

    Which A20 geometry classes actually occur under the FIRST branch
    constraints h < alpha <= t?

    Which classes survive in the SECOND branch away from beta=h?

The enumeration is purely positional.  It does not use field values, primality,
or the actual sequence entries.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from types import SimpleNamespace
from typing import Dict, Iterable, Iterator, List, Tuple

from classify_a19_residual_row import classify_row


FIRST_FAMILIES = ["F1r", "F3r", "F4r", "F5r", "F6r"]
SECOND_FAMILIES = ["S1r", "S2r", "S3r", "S4r", "S5r"]


def local_j_values(t: int, h: int) -> Iterator[int]:
    """A5 blocker index j is an old nonempty partial-sum index, j != h.

    The case j=h-1 would force b=0 because S_{h-1}+b=S_{h-1}, so it is
    skipped as an immediate impossibility.
    """
    for j in range(1, t + 1):
        if j in (h, h - 1):
            continue
        yield j


def first_rows(t: int, h: int, alpha: int) -> Iterator[Tuple[str, Dict[str, int]]]:
    """Enumerate FIRST-branch residual row parameters.

    FIRST setup:
        R = L U V
        L=(1..h)
        U=(h+1..alpha)
        V=(alpha+1..t)
        singleton-prefix move requires |U| >= 2, i.e. alpha >= h+2.
    """
    u_len = alpha - h
    v_len = t - alpha
    if u_len < 2:
        return

    # F1r: 1 <= i <= h-2
    for i in range(1, max(0, h - 2) + 1):
        yield "F1r", {"i": i}

    # F3r: 2 <= s <= |U|
    for s in range(2, u_len + 1):
        yield "F3r", {"s": s}

    # F4r: 1 <= m <= |V|
    for m in range(1, v_len + 1):
        yield "F4r", {"alpha": alpha, "m": m}

    # F5r: 2 <= s <= |U|, 1 <= i <= h-1
    for s in range(2, u_len + 1):
        for i in range(1, h):
            yield "F5r", {"i": i, "s": s}

    # F6r: 1 <= m <= |V|, 1 <= i <= h
    for m in range(1, v_len + 1):
        for i in range(1, h + 1):
            yield "F6r", {"i": i, "alpha": alpha, "m": m}


def second_rows(t: int, h: int, beta: int) -> Iterator[Tuple[str, Dict[str, int]]]:
    """Enumerate SECOND-branch residual row parameters away from beta=h.

    SECOND setup:
        R = A B C
        A=(1..beta)
        B=(beta+1..h)
        C=(h+1..t)
        singleton-prefix move requires |C| >= 2, i.e. t-h >= 2.
        A18/A22 exclude the boundary pair-trap beta=h here.
    """
    if beta >= h:
        return
    b_len = h - beta
    c_len = t - h
    if c_len < 2:
        return

    # S1r: 1 <= k < |B|
    for k in range(1, b_len):
        yield "S1r", {"beta": beta, "k": k}

    # S2r: 1 <= i < beta
    for i in range(1, beta):
        yield "S2r", {"beta": beta, "i": i}

    # S3r: 1 <= i < beta, 1 <= k <= |B|
    for i in range(1, beta):
        for k in range(1, b_len + 1):
            yield "S3r", {"beta": beta, "i": i, "k": k}

    # S4r: 2 <= s <= |C|
    for s in range(2, c_len + 1):
        yield "S4r", {"beta": beta, "s": s}

    # S5r: 2 <= s <= |C|, 1 <= k <= |B|
    for s in range(2, c_len + 1):
        for k in range(1, b_len + 1):
            yield "S5r", {"beta": beta, "k": k, "s": s}


def classify_config(t: int, h: int, j: int, family: str, params: Dict[str, int]) -> Dict[str, object]:
    ns = SimpleNamespace(
        family=family,
        t=t,
        h=h,
        j=j,
        i=params.get("i"),
        s=params.get("s"),
        alpha=params.get("alpha"),
        m=params.get("m"),
        beta=params.get("beta"),
        k=params.get("k"),
        json=False,
    )
    out = classify_row(ns)
    out["params"] = dict(params)
    return out


def summarize(results: Iterable[Dict[str, object]]) -> Dict[str, object]:
    by_class: Counter[str] = Counter()
    by_family_class: Dict[str, Counter[str]] = defaultdict(Counter)
    examples: Dict[str, Dict[str, object]] = {}
    total = 0

    for row in results:
        total += 1
        cls = str(row["geometry_class"])
        fam = str(row["family"])
        by_class[cls] += 1
        by_family_class[fam][cls] += 1
        examples.setdefault(cls, row)

    return {
        "total_rows": total,
        "by_class": dict(sorted(by_class.items())),
        "by_family_class": {
            fam: dict(sorted(counter.items()))
            for fam, counter in sorted(by_family_class.items())
        },
        "example_by_class": examples,
    }


def run_first(t: int, h: int, alpha: int) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for family, params in first_rows(t, h, alpha):
        for j in local_j_values(t, h):
            try:
                rows.append(classify_config(t, h, j, family, params))
            except ValueError as exc:
                rows.append({
                    "family": family,
                    "params": dict(params),
                    "t": t,
                    "h": h,
                    "j": j,
                    "geometry_class": "invalid_or_immediate",
                    "reason": str(exc),
                })
    return rows


def run_second(t: int, h: int, beta: int) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for family, params in second_rows(t, h, beta):
        for j in local_j_values(t, h):
            try:
                rows.append(classify_config(t, h, j, family, params))
            except ValueError as exc:
                rows.append({
                    "family": family,
                    "params": dict(params),
                    "t": t,
                    "h": h,
                    "j": j,
                    "geometry_class": "invalid_or_immediate",
                    "reason": str(exc),
                })
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--branch", choices=["first", "second"], required=True)
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--h", type=int, required=True)
    ap.add_argument("--alpha", type=int, help="FIRST branch alpha")
    ap.add_argument("--beta", type=int, help="SECOND branch beta")
    ap.add_argument("--show-examples", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.branch == "first":
        if args.alpha is None:
            ap.error("--alpha is required for --branch first")
        rows = run_first(args.t, args.h, args.alpha)
    else:
        if args.beta is None:
            ap.error("--beta is required for --branch second")
        rows = run_second(args.t, args.h, args.beta)

    summary = summarize(rows)

    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
        return 0

    print(f"branch: {args.branch}")
    print(f"t: {args.t}")
    print(f"h: {args.h}")
    if args.branch == "first":
        print(f"alpha: {args.alpha}")
    else:
        print(f"beta: {args.beta}")
    print(f"total_rows: {summary['total_rows']}")
    print()
    print("by_class:")
    for cls, count in summary["by_class"].items():
        print(f"  {cls}: {count}")
    print()
    print("by_family_class:")
    for fam, counter in summary["by_family_class"].items():
        print(f"  {fam}:")
        for cls, count in counter.items():
            print(f"    {cls}: {count}")

    if args.show_examples:
        print()
        print("examples:")
        for cls, row in summary["example_by_class"].items():
            print(f"  {cls}: {json.dumps(row, sort_keys=True)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
