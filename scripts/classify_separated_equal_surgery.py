#!/usr/bin/env python3
"""
Classifier for separated equal-interval surgery branches D1--D5.

This script encodes the routing from:

  docs/analytic_separated_equal_interval_surgery_a36.md
  docs/analytic_d1_d5_span_descent_a37.md
  docs/analytic_weighted_transported_prefix_a38.md

Setup:

  X A G C Y
  sum(A)=sum(C)=a

Direct exchange:

  X A G C Y -> X C G A Y

Collision branches from A36:

  D1: C_k = a + G_j
  D2: C_k = 2a + g + Y_m
  D3: A_i = G_j - g
  D4: A_i = a + Y_m
  D5: C_k = a + g + A_i

The classifier is positional.  It does not test field realizability.
It returns the routed obstruction class and the branch-specific descent/collapse
status.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class Lengths:
    A: int
    G: int
    C: int
    Y: int

    def validate(self) -> None:
        if self.A <= 0:
            raise ValueError("|A| must be positive")
        if self.G < 0:
            raise ValueError("|G| must be nonnegative")
        if self.C <= 0:
            raise ValueError("|C| must be positive")
        if self.Y < 0:
            raise ValueError("|Y| must be nonnegative")


@dataclass(frozen=True)
class Indices:
    i: Optional[int] = None
    j: Optional[int] = None
    k: Optional[int] = None
    m: Optional[int] = None


def require(name: str, value: Optional[int]) -> int:
    if value is None:
        raise ValueError(f"missing required index --{name}")
    return value


def classify_d1(L: Lengths, I: Indices) -> Dict[str, object]:
    j = require("j", I.j)
    k = require("k", I.k)
    if not (1 <= j <= L.G):
        raise ValueError("D1 requires 1 <= j <= |G|")
    if not (1 <= k <= L.C):
        raise ValueError("D1 requires 1 <= k <= |C|")

    if k == L.C:
        return {
            "class": "zero_collapse",
            "status": "closed_or_prefix_zero",
            "derived": "G_j=0",
            "reason": "D1 with k=|C| gives a=a+G_j, hence G_j=0.",
        }

    return {
        "class": "equal_interval_descent",
        "status": "controlled_descent",
        "derived": "sum(A + prefix_j(G)) = sum(prefix_k(C))",
        "new_support": L.A + j + k,
        "old_enclosing_span": L.A + L.G + L.C,
        "reason": "D1 with k<|C| gives a shorter/span-controlled equal-interval relation.",
    }


def classify_d2(L: Lengths, I: Indices) -> Dict[str, object]:
    k = require("k", I.k)
    m = require("m", I.m)
    if not (1 <= k <= L.C):
        raise ValueError("D2 requires 1 <= k <= |C|")
    if not (1 <= m <= L.Y):
        raise ValueError("D2 requires 1 <= m <= |Y|")

    if k == L.C:
        return {
            "class": "two_piece_zero",
            "status": "controlled_composite_zero",
            "derived": "sum(A G)+Y_m=0",
            "new_support": L.A + L.G + m,
            "reason": "D2 endpoint k=|C| removes tail(C), leaving a two-piece zero composite.",
        }

    return {
        "class": "three_piece_zero",
        "status": "composite_zero_descent_accounting_needed",
        "derived": "sum(A G)+sum(tail_k(C))+Y_m=0",
        "new_support": L.A + L.G + (L.C - k) + m,
        "old_enclosing_span": L.A + L.G + L.C,
        "reason": "A38 routes D2 to a three-piece zero composite. Whether it is strict descent depends on the Y-prefix length m.",
    }


def classify_d3(L: Lengths, I: Indices) -> Dict[str, object]:
    i = require("i", I.i)
    j = require("j", I.j)
    if not (1 <= i <= L.A):
        raise ValueError("D3 requires 1 <= i <= |A|")
    if not (1 <= j <= L.G):
        raise ValueError("D3 requires 1 <= j <= |G|")

    if j == L.G:
        return {
            "class": "zero_collapse",
            "status": "closed_or_prefix_zero",
            "derived": "A_i=0",
            "reason": "D3 with j=|G| gives tail_j(G)=0, hence A_i=0.",
        }

    return {
        "class": "two_piece_zero",
        "status": "controlled_composite_zero",
        "derived": "A_i + tail_j(G)=0",
        "new_support": i + (L.G - j),
        "old_enclosing_span": L.A + L.G + L.C,
        "reason": "A36 routes D3 to a two-piece zero composite using a proper G-tail.",
    }


def classify_d4(L: Lengths, I: Indices) -> Dict[str, object]:
    i = require("i", I.i)
    m = require("m", I.m)
    if not (1 <= i <= L.A):
        raise ValueError("D4 requires 1 <= i <= |A|")
    if not (1 <= m <= L.Y):
        raise ValueError("D4 requires 1 <= m <= |Y|")

    if i == L.A:
        return {
            "class": "zero_collapse",
            "status": "closed_or_prefix_zero",
            "derived": "Y_m=0",
            "reason": "D4 with i=|A| gives tail_i(A)=0, hence Y_m=0.",
        }

    return {
        "class": "two_piece_zero",
        "status": "controlled_composite_zero",
        "derived": "tail_i(A)+Y_m=0",
        "new_support": (L.A - i) + m,
        "old_enclosing_span": L.A + L.G + L.C,
        "reason": "A36 routes D4 to a two-piece zero composite using a proper A-tail.",
    }


def classify_d5(L: Lengths, I: Indices) -> Dict[str, object]:
    i = require("i", I.i)
    k = require("k", I.k)
    if not (1 <= i <= L.A):
        raise ValueError("D5 requires 1 <= i <= |A|")
    if not (1 <= k <= L.C):
        raise ValueError("D5 requires 1 <= k <= |C|")

    if i == L.A and k == L.C:
        return {
            "class": "two_piece_zero",
            "status": "controlled_composite_zero",
            "derived": "sum(A G)=0",
            "new_support": L.A + L.G,
            "reason": "D5 double endpoint gives a+g=0, so AG is zero.",
        }

    if i == L.A:
        return {
            "class": "two_piece_zero",
            "status": "controlled_composite_zero",
            "derived": "sum(A G)+tail_k(C)=0",
            "new_support": L.A + L.G + (L.C - k),
            "reason": "A37 endpoint i=|A| routes to a two-piece zero/composite branch.",
        }

    if k == L.C:
        return {
            "class": "two_piece_zero",
            "status": "controlled_composite_zero",
            "derived": "prefix_i(A)+sum(G)=0",
            "new_support": i + L.G,
            "reason": "A37 endpoint k=|C| routes to a two-piece zero branch.",
        }

    return {
        "class": "three_piece_zero_strict_span",
        "status": "controlled_descent",
        "derived": "prefix_i(A)+sum(G)+tail_k(C)=0",
        "new_support": i + L.G + (L.C - k),
        "old_enclosing_span": L.A + L.G + L.C,
        "span_drop": (L.A - i) + k,
        "reason": "A38 proves D5 proper-interior is a strict-span three-piece zero composite.",
    }


def classify(branch: str, L: Lengths, I: Indices) -> Dict[str, object]:
    L.validate()
    branch = branch.upper()
    if branch == "D1":
        out = classify_d1(L, I)
    elif branch == "D2":
        out = classify_d2(L, I)
    elif branch == "D3":
        out = classify_d3(L, I)
    elif branch == "D4":
        out = classify_d4(L, I)
    elif branch == "D5":
        out = classify_d5(L, I)
    else:
        raise ValueError("branch must be D1, D2, D3, D4, or D5")

    out = dict(out)
    out.update({
        "branch": branch,
        "lengths": {"A": L.A, "G": L.G, "C": L.C, "Y": L.Y},
        "indices": {"i": I.i, "j": I.j, "k": I.k, "m": I.m},
    })
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--branch", required=True, choices=["D1", "D2", "D3", "D4", "D5", "d1", "d2", "d3", "d4", "d5"])
    ap.add_argument("--A", type=int, required=True, help="Length |A|")
    ap.add_argument("--G", type=int, required=True, help="Length |G|; may be 0 for midpoint boundary, though D1/D3 need positive G")
    ap.add_argument("--C", type=int, required=True, help="Length |C|")
    ap.add_argument("--Y", type=int, default=0, help="Length |Y|")
    ap.add_argument("--i", type=int)
    ap.add_argument("--j", type=int)
    ap.add_argument("--k", type=int)
    ap.add_argument("--m", type=int)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    result = classify(args.branch, Lengths(args.A, args.G, args.C, args.Y), Indices(args.i, args.j, args.k, args.m))
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        for key, value in result.items():
            print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
