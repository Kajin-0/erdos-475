#!/usr/bin/env python3
"""
Normalize interval relations from the A19--A26 proof program.

This tool is deliberately symbolic.  It does not use finite-field values.
It applies the controlled reductions proved in

    docs/analytic_composite_interval_surgery_a26.md

especially:

    equal proper-overlap descent:
        sum(x,y] = sum(u,v], x<u<y<v
        -> sum(x,u] = sum(y,v]

The tool iterates such reductions until a terminal geometry class is reached.
For signed relations, it classifies the geometry but does not try to eliminate
weighted signed overlap/nesting branches.

Input relation:

    sign = +1: sum(x,y] =  sum(u,v]
    sign = -1: sum(x,y] = -sum(u,v]

Output:

    a normalization trace and terminal class.

This is a proof-audit tool, not a proof of endpoint avoidance.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, asdict
from typing import Dict, List, Tuple

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from classify_interval_traps import Interval, classify  # type: ignore


@dataclass(frozen=True)
class Relation:
    I: Interval
    J: Interval
    sign: int

    def validate(self, t: int) -> None:
        self.I.validate(t)
        self.J.validate(t)
        if self.sign not in (1, -1):
            raise ValueError("sign must be +1 or -1")

    def span(self) -> int:
        return (self.I.right - self.I.left) + (self.J.right - self.J.left)

    def as_text(self) -> str:
        rhs_sign = "" if self.sign == 1 else "-"
        return f"sum{self.I.as_text()} = {rhs_sign}sum{self.J.as_text()}"


def equal_proper_overlap_reduce(rel: Relation) -> Tuple[Relation, str] | None:
    """Apply A26.1 if the relation is an equal proper-overlap relation."""
    if rel.sign != 1:
        return None

    x, y = rel.I.left, rel.I.right
    u, v = rel.J.left, rel.J.right

    # Equality is symmetric; normalize order by left endpoint.
    swapped = False
    if u < x:
        x, y, u, v = u, v, x, y
        swapped = True

    if x < u < y < v:
        new_rel = Relation(Interval(x, u), Interval(y, v), 1)
        reason = (
            "A26.1 proper-overlap equal-interval descent: "
            f"sum({x},{y}]=sum({u},{v}] -> sum({x},{u}]=sum({y},{v}]"
        )
        return new_rel, reason

    return None


def normalize(t: int, rel: Relation, max_steps: int = 100) -> Dict[str, object]:
    rel.validate(t)
    trace: List[Dict[str, object]] = []
    current = rel
    seen = set()

    for step in range(max_steps + 1):
        geom = classify(t, current.I, current.J, current.sign)
        trace.append({
            "step": step,
            "relation": current.as_text(),
            "span": current.span(),
            "geometry_class": geom["class"],
            "derived": geom["derived"],
            "reason": geom["reason"],
        })

        key = (current.I.left, current.I.right, current.J.left, current.J.right, current.sign)
        if key in seen:
            return {
                "status": "cycle_detected",
                "terminal_relation": current.as_text(),
                "terminal_class": geom["class"],
                "trace": trace,
            }
        seen.add(key)

        reduction = equal_proper_overlap_reduce(current)
        if reduction is None:
            return {
                "status": "terminal",
                "terminal_relation": current.as_text(),
                "terminal_class": geom["class"],
                "trace": trace,
            }

        new_rel, reduction_reason = reduction
        if new_rel.span() >= current.span():
            return {
                "status": "non_descent_error",
                "terminal_relation": current.as_text(),
                "terminal_class": geom["class"],
                "trace": trace,
                "attempted_reduction": reduction_reason,
            }

        trace[-1]["applied_reduction"] = reduction_reason
        current = new_rel

    return {
        "status": "max_steps_exceeded",
        "terminal_relation": current.as_text(),
        "terminal_class": "unknown",
        "trace": trace,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--x", type=int, required=True)
    ap.add_argument("--y", type=int, required=True)
    ap.add_argument("--u", type=int, required=True)
    ap.add_argument("--v", type=int, required=True)
    ap.add_argument("--sign", type=int, choices=[1, -1], required=True)
    ap.add_argument("--max-steps", type=int, default=100)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rel = Relation(Interval(args.x, args.y), Interval(args.u, args.v), args.sign)
    out = normalize(args.t, rel, max_steps=args.max_steps)

    if args.json:
        print(json.dumps(out, indent=2, sort_keys=True))
        return 0

    print(f"status: {out['status']}")
    print(f"terminal_relation: {out['terminal_relation']}")
    print(f"terminal_class: {out['terminal_class']}")
    print("trace:")
    for row in out["trace"]:
        print(f"  step {row['step']}: {row['relation']}")
        print(f"    span: {row['span']}")
        print(f"    class: {row['geometry_class']}")
        print(f"    derived: {row['derived']}")
        if "applied_reduction" in row:
            print(f"    reduction: {row['applied_reduction']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
