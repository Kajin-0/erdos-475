#!/usr/bin/env python3
"""
Classifier for weighted signed normal forms from A56.

The target relation is

    sum(A) + 2 sum(B) + sum(C) = 0.

A56 separates coefficient-2 branches into:

    transported-prefix/tail artifacts,
    zero collapse,
    adjacent-pair zero reductions,
    equal-outer reductions,
    genuine weighted cores.

This script is a symbolic/status classifier.  It does not evaluate finite-field
sums or prove realizability.  It records which normal-form test applies given
metadata about the branch.
"""

from __future__ import annotations

import argparse
import json
from typing import Dict


def classify(
    *,
    transported_prefix: bool,
    transported_tail: bool,
    b_zero: bool,
    ab_zero: bool,
    bc_zero: bool,
    outer_equal: bool,
    odd_prime: bool,
) -> Dict[str, object]:
    tests = []

    if transported_prefix:
        tests.append("W1_prefix")
        return {
            "class": "transported_prefix_artifact",
            "status": "controlled_composite_zero",
            "tests": tests,
            "normal_form": "2P+R+U=0 -> P+B+U=0",
            "reason": "A56.1 removes the coefficient 2 because the complementary tail of the containing block is present.",
        }

    if transported_tail:
        tests.append("W1_tail")
        return {
            "class": "transported_tail_artifact",
            "status": "controlled_composite_zero",
            "tests": tests,
            "normal_form": "P+2R+U=0 -> B+R+U=0",
            "reason": "A56.2 removes the coefficient 2 because the complementary prefix of the containing block is present.",
        }

    if b_zero:
        tests.append("W2")
        return {
            "class": "zero_doubled_block_collapse",
            "status": "zero_collapse_or_two_piece_zero",
            "tests": tests,
            "normal_form": "B=0 -> A+C=0",
            "reason": "A56.4 collapses the weighted relation when the doubled block is zero.",
        }

    if ab_zero:
        tests.append("W3_left")
        return {
            "class": "adjacent_pair_zero_left",
            "status": "two_piece_zero",
            "tests": tests,
            "normal_form": "A+B=0 -> B+C=0",
            "reason": "A56.5 reduces the weighted relation to a two-piece zero composite.",
        }

    if bc_zero:
        tests.append("W3_right")
        return {
            "class": "adjacent_pair_zero_right",
            "status": "two_piece_zero",
            "tests": tests,
            "normal_form": "B+C=0 -> A+B=0",
            "reason": "A56.5 reduces the weighted relation to a two-piece zero composite.",
        }

    if outer_equal:
        tests.append("W4")
        if odd_prime:
            return {
                "class": "equal_outer_reduction",
                "status": "two_piece_zero_or_midpoint_boundary",
                "tests": tests,
                "normal_form": "A=C -> A+B=0 over odd prime fields",
                "reason": "A56.6 divides by 2 and reduces the weighted relation to a two-piece zero composite.",
            }
        return {
            "class": "equal_outer_needs_characteristic_check",
            "status": "requires_odd_prime_or_finite_verification",
            "tests": tests,
            "normal_form": "2(A+B)=0",
            "reason": "The equal-outer reduction requires division by 2; odd-prime cases are controlled, characteristic 2 must be handled separately.",
        }

    return {
        "class": "genuine_weighted_core",
        "status": "hard_residual",
        "tests": tests,
        "normal_form": "A+2B+C=0 with no transported-prefix rewrite and no zero/equal endpoint collapse",
        "reason": "None of W1--W4 applies. This is the genuine weighted signed core isolated in A56.",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--transported-prefix", action="store_true", help="Doubled piece is a prefix and its complementary tail is present")
    ap.add_argument("--transported-tail", action="store_true", help="Doubled piece is a tail and its complementary prefix is present")
    ap.add_argument("--b-zero", action="store_true", help="sum(B)=0")
    ap.add_argument("--ab-zero", action="store_true", help="sum(A)+sum(B)=0")
    ap.add_argument("--bc-zero", action="store_true", help="sum(B)+sum(C)=0")
    ap.add_argument("--outer-equal", action="store_true", help="sum(A)=sum(C)")
    ap.add_argument("--odd-prime", action="store_true", help="Field has odd prime characteristic, so division by 2 is valid")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    result = classify(
        transported_prefix=args.transported_prefix,
        transported_tail=args.transported_tail,
        b_zero=args.b_zero,
        ab_zero=args.ab_zero,
        bc_zero=args.bc_zero,
        outer_equal=args.outer_equal,
        odd_prime=args.odd_prime,
    )

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        for key, value in result.items():
            print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
