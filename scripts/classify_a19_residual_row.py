#!/usr/bin/env python3
"""
Row-specific classifier for A19 residual singleton-prefix traps.

This script corrects an orientation subtlety from the informal A19 summary:

    b = S_j - S_{h-1}

is a forward interval only when j > h-1.  If j < h-1, it is the negative of
the forward interval (j,h-1].

The script maps each residual family F1r--F6r and S1r--S5r to an oriented
interval expression for b, compares it with the oriented local blocker
expression, and then calls the A21 interval-geometry classifier.

It is a symbolic bookkeeping tool, not a proof of the theorem.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from typing import Dict, Optional, Tuple

# Allow importing sibling script when executed from repo root or scripts/.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from classify_interval_traps import Interval, classify  # type: ignore


@dataclass(frozen=True)
class OrientedInterval:
    sign: int  # +1 or -1
    interval: Interval
    expression: str

    def as_text(self) -> str:
        s = "+" if self.sign == 1 else "-"
        return f"{s}sum{self.interval.as_text()}"


def diff_expr(right_endpoint: int, left_endpoint: int, label: str) -> OrientedInterval:
    """Represent S_right - S_left as ± sum(min,max]."""
    if right_endpoint == left_endpoint:
        raise ValueError(f"{label}: zero difference S_{right_endpoint}-S_{left_endpoint}")
    if right_endpoint > left_endpoint:
        return OrientedInterval(
            +1,
            Interval(left_endpoint, right_endpoint),
            f"{label}: S_{right_endpoint}-S_{left_endpoint}",
        )
    return OrientedInterval(
        -1,
        Interval(right_endpoint, left_endpoint),
        f"{label}: S_{right_endpoint}-S_{left_endpoint}",
    )


def local_expr(h: int, j: int) -> OrientedInterval:
    if j == h:
        raise ValueError("local blocker has j=h, excluded by A5")
    if j == h - 1:
        raise ValueError("local blocker has j=h-1, forcing b=0")
    return diff_expr(j, h - 1, "local b=S_j-S_{h-1}")


def residual_expr(family: str, args: argparse.Namespace) -> OrientedInterval:
    h = args.h

    if family == "F1r":
        if args.i is None:
            raise ValueError("F1r requires --i")
        return diff_expr(h, args.i, "F1r b=S_h-S_i")

    if family == "F2r":
        raise ValueError("F2r is prefix-zero S_i=0, not an atom-equals-interval row")

    if family == "F3r":
        if args.s is None:
            raise ValueError("F3r requires --s")
        return diff_expr(h + args.s, 0, "F3r b=S_{h+s}-S_0")

    if family == "F4r":
        if args.alpha is None or args.m is None:
            raise ValueError("F4r requires --alpha --m")
        return diff_expr(args.alpha + args.m, 0, "F4r b=S_{alpha+m}-S_0")

    if family == "F5r":
        if args.i is None or args.s is None:
            raise ValueError("F5r requires --i --s")
        return diff_expr(h + args.s, args.i, "F5r b=S_{h+s}-S_i")

    if family == "F6r":
        if args.i is None or args.alpha is None or args.m is None:
            raise ValueError("F6r requires --i --alpha --m")
        return diff_expr(args.alpha + args.m, args.i, "F6r b=S_{alpha+m}-S_i")

    if family == "S1r":
        if args.beta is None or args.k is None:
            raise ValueError("S1r requires --beta --k")
        return diff_expr(h, args.beta + args.k, "S1r b=S_h-S_{beta+k}")

    if family == "S2r":
        if args.beta is None or args.i is None:
            raise ValueError("S2r requires --beta --i")
        return diff_expr(args.i, args.beta, "S2r b=S_i-S_beta")

    if family == "S3r":
        if args.beta is None or args.i is None or args.k is None:
            raise ValueError("S3r requires --beta --i --k")
        return diff_expr(args.i, args.beta + args.k, "S3r b=S_i-S_{beta+k}")

    if family == "S4r":
        if args.beta is None or args.s is None:
            raise ValueError("S4r requires --beta --s")
        return diff_expr(h + args.s, args.beta, "S4r b=S_{h+s}-S_beta")

    if family == "S5r":
        if args.beta is None or args.k is None or args.s is None:
            raise ValueError("S5r requires --beta --k --s")
        return diff_expr(h + args.s, args.beta + args.k, "S5r b=S_{h+s}-S_{beta+k}")

    raise ValueError(f"unknown residual family: {family}")


def classify_row(args: argparse.Namespace) -> Dict[str, object]:
    loc = local_expr(args.h, args.j)
    res = residual_expr(args.family, args)

    # loc.sign*sum(loc.interval) = res.sign*sum(res.interval)
    # hence sum(loc.interval) = (loc.sign*res.sign)*sum(res.interval).
    relation_sign = loc.sign * res.sign

    geom = classify(args.t, loc.interval, res.interval, relation_sign)

    return {
        "family": args.family,
        "t": args.t,
        "h": args.h,
        "j": args.j,
        "local_expression": loc.expression,
        "local_oriented_interval": loc.as_text(),
        "residual_expression": res.expression,
        "residual_oriented_interval": res.as_text(),
        "relation_sign": relation_sign,
        "normalized_relation": (
            f"sum{loc.interval.as_text()} "
            f"={' ' if relation_sign == 1 else ' -'}sum{res.interval.as_text()}"
        ),
        "geometry_class": geom["class"],
        "derived": geom["derived"],
        "reason": geom["reason"],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True, choices=[
        "F1r", "F2r", "F3r", "F4r", "F5r", "F6r",
        "S1r", "S2r", "S3r", "S4r", "S5r",
    ])
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--h", type=int, required=True)
    ap.add_argument("--j", type=int, required=True)

    # Optional row parameters.  Each row validates what it needs.
    ap.add_argument("--i", type=int)
    ap.add_argument("--s", type=int)
    ap.add_argument("--alpha", type=int)
    ap.add_argument("--m", type=int)
    ap.add_argument("--beta", type=int)
    ap.add_argument("--k", type=int)
    ap.add_argument("--json", action="store_true")

    args = ap.parse_args()
    result = classify_row(args)

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        for key, value in result.items():
            print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
