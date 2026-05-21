#!/usr/bin/env python3
"""
Sweep A23 residual histograms over many symbolic branch configurations.

A23 classifies one fixed FIRST or SECOND branch instance.  This script sweeps
over many positional parameters and aggregates the A20/A21 geometry classes.

It remains purely symbolic/positional.  It does not assert that each positional
configuration is algebraically realizable over a finite field.  Its purpose is
to show which residual geometry classes survive the known index inequalities.

Examples:

  python3 scripts/sweep_a23_residual_histograms.py --branch first --max-t 30

  python3 scripts/sweep_a23_residual_histograms.py --branch first --max-t 30 \
    --use-secondary-constraints

  python3 scripts/sweep_a23_residual_histograms.py --branch second --max-t 30 \
    --use-secondary-constraints --json
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from typing import Dict, Iterable, Iterator, List, Tuple

from batch_classify_a19_residuals import run_first, run_second


def first_configs(max_t: int, use_secondary: bool) -> Iterator[Tuple[int, int, int]]:
    """Yield (t,h,alpha) for FIRST equal-sum branch.

    Basic constraints:
      2 <= t
      1 <= h < alpha <= t
      singleton-prefix move requires alpha-h >= 2

    Secondary A8/A13 minimality constraint for a valid direct exchange:
      alpha >= 2h

    The secondary constraint is optional because in the full obstruction tree the
    cyclic cut may fail Graham-validity before the special-hit branch is used.
    """
    for t in range(2, max_t + 1):
        for h in range(1, t):
            for alpha in range(h + 2, t + 1):
                if use_secondary and alpha < 2 * h:
                    continue
                yield t, h, alpha


def second_configs(max_t: int, use_secondary: bool) -> Iterator[Tuple[int, int, int]]:
    """Yield (t,h,beta) for SECOND equal-sum branch away from beta=h.

    Basic constraints:
      3 <= t
      1 <= beta < h < t
      singleton-prefix move requires t-h >= 2

    Secondary A8/A13 minimality constraint for a valid direct exchange:
      beta >= 2h-t

    Boundary beta=h is excluded because it is the pair-trap branch.
    """
    for t in range(3, max_t + 1):
        for h in range(2, t - 1):
            for beta in range(1, h):
                if t - h < 2:
                    continue
                if use_secondary and beta < 2 * h - t:
                    continue
                yield t, h, beta


def aggregate_rows(rows: Iterable[Dict[str, object]], accum: Dict[str, object]) -> None:
    by_class: Counter[str] = accum["by_class"]  # type: ignore[assignment]
    by_family_class: Dict[str, Counter[str]] = accum["by_family_class"]  # type: ignore[assignment]
    examples: Dict[str, Dict[str, object]] = accum["examples"]  # type: ignore[assignment]

    for row in rows:
        accum["total_rows"] = int(accum["total_rows"]) + 1
        cls = str(row.get("geometry_class"))
        fam = str(row.get("family"))
        by_class[cls] += 1
        by_family_class[fam][cls] += 1
        examples.setdefault(cls, row)


def new_accum() -> Dict[str, object]:
    return {
        "total_rows": 0,
        "by_class": Counter(),
        "by_family_class": defaultdict(Counter),
        "examples": {},
    }


def serialize_accum(accum: Dict[str, object]) -> Dict[str, object]:
    by_class: Counter[str] = accum["by_class"]  # type: ignore[assignment]
    by_family_class: Dict[str, Counter[str]] = accum["by_family_class"]  # type: ignore[assignment]
    return {
        "total_rows": accum["total_rows"],
        "by_class": dict(sorted(by_class.items())),
        "by_family_class": {
            fam: dict(sorted(counter.items()))
            for fam, counter in sorted(by_family_class.items())
        },
        "examples": accum["examples"],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--branch", choices=["first", "second", "both"], required=True)
    ap.add_argument("--max-t", type=int, default=30)
    ap.add_argument("--use-secondary-constraints", action="store_true")
    ap.add_argument("--show-examples", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    branches = ["first", "second"] if args.branch == "both" else [args.branch]
    output: Dict[str, object] = {
        "max_t": args.max_t,
        "use_secondary_constraints": args.use_secondary_constraints,
        "branches": {},
    }

    for branch in branches:
        accum = new_accum()
        config_count = 0

        if branch == "first":
            for t, h, alpha in first_configs(args.max_t, args.use_secondary_constraints):
                config_count += 1
                aggregate_rows(run_first(t, h, alpha), accum)
        else:
            for t, h, beta in second_configs(args.max_t, args.use_secondary_constraints):
                config_count += 1
                aggregate_rows(run_second(t, h, beta), accum)

        serial = serialize_accum(accum)
        serial["config_count"] = config_count
        if not args.show_examples:
            serial.pop("examples", None)
        output["branches"][branch] = serial  # type: ignore[index]

    if args.json:
        print(json.dumps(output, indent=2, sort_keys=True))
        return 0

    print(f"max_t: {args.max_t}")
    print(f"use_secondary_constraints: {args.use_secondary_constraints}")
    print()

    for branch, data in output["branches"].items():  # type: ignore[union-attr]
        print(f"branch: {branch}")
        print(f"  config_count: {data['config_count']}")
        print(f"  total_rows: {data['total_rows']}")
        print("  by_class:")
        for cls, count in data["by_class"].items():
            print(f"    {cls}: {count}")
        print("  by_family_class:")
        for fam, counter in data["by_family_class"].items():
            print(f"    {fam}:")
            for cls, count in counter.items():
                print(f"      {cls}: {count}")
        if args.show_examples:
            print("  examples:")
            for cls, row in data["examples"].items():
                print(f"    {cls}: {json.dumps(row, sort_keys=True)}")
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
