#!/usr/bin/env python3
"""
Symbolic classifier for equal-interval and signed-equal-interval traps.

This script implements the geometry table from

    docs/analytic_equal_interval_uncrossing_a20.md

It does not prove the remaining theorem.  Its purpose is to make the A19/A20
residual case split reproducible and unambiguous.

An interval is encoded as (x, y] with 0 <= x < y <= t.

A relation has sign:

    +1:  sum(x,y] =  sum(u,v]
    -1:  sum(x,y] = -sum(u,v]

The classifier returns one of the following broad classes:

    identical
    collapse_old_collision
    collapse_prefix_zero
    collapse_interior_zero
    reduction_equal_outer_pieces
    residual_two_piece_zero
    residual_midpoint
    residual_separated_equal
    residual_separated_signed
    residual_signed_overlap_weighted
    residual_signed_nested_weighted
    invalid_geometry

This is intentionally syntactic.  It does not use additional branch-specific
facts such as h, alpha, beta, or whether a residual interval arose from F1/S3.
Those facts should be layered on top by a later row-specific classifier.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass(frozen=True)
class Interval:
    left: int
    right: int

    def validate(self, t: int) -> None:
        if not (0 <= self.left < self.right <= t):
            raise ValueError(f"invalid interval ({self.left},{self.right}] for t={t}")

    def as_text(self) -> str:
        return f"({self.left},{self.right}]"


def classify_equal(I: Interval, J: Interval) -> Dict[str, str]:
    x, y = I.left, I.right
    u, v = J.left, J.right

    if (x, y) == (u, v):
        return {
            "class": "identical",
            "reason": "The two intervals are identical; the equality is tautological.",
            "derived": "none",
        }

    if x == u:
        return {
            "class": "collapse_old_collision",
            "reason": "Shared left endpoint gives S_y=S_v; distinct right endpoints contradict Graham-validity.",
            "derived": f"S_{y}=S_{v}",
        }

    if y == v:
        if x == 0 or u == 0:
            w = u if x == 0 else x
            return {
                "class": "collapse_prefix_zero",
                "reason": "Shared right endpoint with one left endpoint 0 gives a prefix-zero branch.",
                "derived": f"S_{w}=0",
            }
        return {
            "class": "collapse_old_collision",
            "reason": "Shared right endpoint gives S_x=S_u; distinct nonzero left endpoints contradict Graham-validity.",
            "derived": f"S_{x}=S_{u}",
        }

    # Normalize order labels without swapping relation semantics; equality is symmetric.
    if u < x:
        return classify_equal(J, I)

    # Now x < u or disjoint x<y<=u<v or proper/nested.
    if x < y < u < v:
        return {
            "class": "residual_separated_equal",
            "reason": "Separated equal intervals do not collapse syntactically.",
            "derived": f"sum{I.as_text()}=sum{J.as_text()}",
        }

    if x < y == u < v:
        return {
            "class": "residual_midpoint",
            "reason": "Adjacent equal intervals give midpoint relation 2S_y=S_x+S_v.",
            "derived": f"2*S_{y}=S_{x}+S_{v}",
        }

    if x < u < y < v:
        return {
            "class": "reduction_equal_outer_pieces",
            "reason": "Proper overlap cancels the common middle piece and gives equal outer pieces.",
            "derived": f"sum({x},{u}]=sum({y},{v}]",
        }

    if x < u < v < y:
        return {
            "class": "residual_two_piece_zero",
            "reason": "Nested equal intervals give a two-piece zero composite.",
            "derived": f"sum({x},{u}]+sum({v},{y}]=0",
        }

    # Remaining cases include u < v <= x < y after failed normalization or boundary weirdness.
    return {
        "class": "invalid_geometry",
        "reason": "Geometry not matched by the current equal-interval classifier.",
        "derived": "none",
    }


def classify_signed(I: Interval, J: Interval) -> Dict[str, str]:
    x, y = I.left, I.right
    u, v = J.left, J.right

    # Signed relation is symmetric in the two intervals: A=-B iff B=-A.
    if u < x:
        return classify_signed(J, I)

    if (x, y) == (u, v):
        # sum(I)=-sum(I), so 2 sum(I)=0. For odd p this implies sum(I)=0.
        return {
            "class": "residual_signed_self",
            "reason": "Self-signed relation gives 2*sum(I)=0; over odd characteristic this is zero-sum, but p=2 must be handled separately.",
            "derived": f"2*sum{I.as_text()}=0",
        }

    if y == u:
        if x == 0:
            return {
                "class": "collapse_prefix_zero",
                "reason": "Adjacent signed intervals join to a prefix zero-sum interval.",
                "derived": f"S_{v}=0",
            }
        return {
            "class": "collapse_interior_zero",
            "reason": "Adjacent signed intervals join to an interior zero-sum interval, contradicting Graham-validity.",
            "derived": f"sum({x},{v}]=0",
        }

    if y < u:
        return {
            "class": "residual_separated_signed",
            "reason": "Separated signed intervals form a two-piece zero composite.",
            "derived": f"sum{I.as_text()}+sum{J.as_text()}=0",
        }

    if x < u < y < v:
        return {
            "class": "residual_signed_overlap_weighted",
            "reason": "Proper signed overlap gives weighted relation A+2B+C=0.",
            "derived": f"sum({x},{u}]+2*sum({u},{y}]+sum({y},{v}]=0",
        }

    if x < u < v < y:
        return {
            "class": "residual_signed_nested_weighted",
            "reason": "Nested signed relation gives weighted composite L+2M+R=0.",
            "derived": f"sum({x},{u}]+2*sum({u},{v}]+sum({v},{y}]=0",
        }

    if x == u:
        return {
            "class": "residual_shared_left_signed",
            "reason": "Shared-left signed relation gives 2S_common=S_y+S_v; midpoint-type branch.",
            "derived": f"2*S_{x}=S_{y}+S_{v}",
        }

    if y == v:
        return {
            "class": "residual_shared_right_signed",
            "reason": "Shared-right signed relation gives 2S_common=S_x+S_u; midpoint-type branch.",
            "derived": f"2*S_{y}=S_{x}+S_{u}",
        }

    return {
        "class": "invalid_geometry",
        "reason": "Geometry not matched by the current signed-interval classifier.",
        "derived": "none",
    }


def classify(t: int, I: Interval, J: Interval, sign: int) -> Dict[str, str]:
    I.validate(t)
    J.validate(t)
    if sign == 1:
        out = classify_equal(I, J)
    elif sign == -1:
        out = classify_signed(I, J)
    else:
        raise ValueError("sign must be +1 or -1")

    out = dict(out)
    out["interval_1"] = I.as_text()
    out["interval_2"] = J.as_text()
    out["relation"] = "equal" if sign == 1 else "signed_equal"
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True, help="Maximum endpoint index t")
    ap.add_argument("--x", type=int, required=True)
    ap.add_argument("--y", type=int, required=True)
    ap.add_argument("--u", type=int, required=True)
    ap.add_argument("--v", type=int, required=True)
    ap.add_argument("--sign", type=int, choices=[1, -1], required=True)
    args = ap.parse_args()

    result = classify(args.t, Interval(args.x, args.y), Interval(args.u, args.v), args.sign)
    for k in ["relation", "interval_1", "interval_2", "class", "derived", "reason"]:
        print(f"{k}: {result[k]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
