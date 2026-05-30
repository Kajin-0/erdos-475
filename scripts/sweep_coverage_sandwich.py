#!/usr/bin/env python3
"""Sweep candidate coverage-sandwich constants for Erdős 475.

This script is exploratory bookkeeping, not proof logic.  It answers:

    Given candidate constants for small, medium, and large analytic ranges,
    does the resulting residue through --max-prime lie inside the verified
    finite domain?

It is designed for rapid testing after extracting constants from source papers.
Do not treat a successful sweep as a proof unless every encoded rule is backed
by a source theorem with matching hypotheses.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, Sequence

import reduction_residue_audit as audit


def parse_float_list(text: str) -> list[float]:
    if not text.strip():
        return []
    return [float(x) for x in text.split(",")]


def parse_int_list(text: str) -> list[int]:
    if not text.strip():
        return []
    return [int(x) for x in text.split(",")]


def residue_not_verified_count(
    *,
    max_prime: int,
    rules: Sequence[audit.CoverageRule],
    verified_rules: Sequence[audit.CoverageRule],
) -> tuple[int, int]:
    cases = [audit.Case(p, t) for p in audit.primes_upto(max_prime) for t in range(1, p)]
    covered = set()
    for case in cases:
        if any(rule.covers(case) for rule in rules):
            covered.add(case)

    residue = set(cases) - covered
    verified = audit.verified_cases(max_prime, list(verified_rules))
    residue_not_verified = residue - verified
    return len(residue), len(residue_not_verified)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-prime", type=int, default=31)
    ap.add_argument("--verified-domain-file", default="certificates/verified_domains.json")
    ap.add_argument(
        "--include-verified-domain",
        action="store_true",
        help="Treat verified finite domains as covered by finite verification.",
    )
    ap.add_argument(
        "--include-default-rules",
        action="store_true",
        help="Include default t<=12 and |B|<=2 rules.",
    )
    ap.add_argument(
        "--include-small-exp-quarter",
        action="store_true",
        help="Include t <= floor(exp((log p)^(1/4))).",
    )
    ap.add_argument(
        "--small-exp-quarter-threshold",
        type=int,
        default=2,
    )
    ap.add_argument(
        "--alphas",
        default="0.05,0.10,0.15,0.20,0.25,0.30",
        help="Comma-separated alpha values for medium rules.",
    )
    ap.add_argument(
        "--n-mins",
        default="13,20,50,100",
        help="Comma-separated N_alpha lower thresholds for medium rules.",
    )
    ap.add_argument(
        "--p-mins",
        default="37,101,1009",
        help="Comma-separated P_alpha lower prime thresholds for medium rules.",
    )
    ap.add_argument(
        "--cs",
        default="0.01,0.02,0.05,0.10,0.15,0.20",
        help="Comma-separated c values for large-set rules.",
    )
    ap.add_argument(
        "--large-p-mins",
        default="37,101,1009",
        help="Comma-separated prime thresholds for large-set rules.",
    )
    ap.add_argument(
        "--show-all",
        action="store_true",
        help="Print every parameter combination instead of only successful closures.",
    )
    args = ap.parse_args()

    verified_rules = audit.load_verified_domain_rules(Path(args.verified_domain_file))
    base_rules: list[audit.CoverageRule] = []
    if args.include_default_rules:
        base_rules.extend(audit.default_rules())
    if args.include_verified_domain:
        base_rules.extend(verified_rules)
    if args.include_small_exp_quarter:
        base_rules.append(audit.SmallExpQuarterRule(p_min=args.small_exp_quarter_threshold))

    alphas = parse_float_list(args.alphas)
    n_mins = parse_int_list(args.n_mins)
    p_mins = parse_int_list(args.p_mins)
    cs = parse_float_list(args.cs)
    large_p_mins = parse_int_list(args.large_p_mins)

    print("=== Coverage sandwich sweep ===")
    print(f"max_prime={args.max_prime}")
    print(f"verified_domain_file={args.verified_domain_file}")
    print(f"base_rules={[rule.name for rule in base_rules]}")
    print()

    successes = 0
    tested = 0
    for alpha in alphas:
        for n_min in n_mins:
            for p_min in p_mins:
                medium = audit.MediumAlphaRule(
                    name=f"medium_alpha_{alpha:g}_N{n_min}_P{p_min}",
                    alpha=alpha,
                    n_min=n_min,
                    p_min=p_min,
                )
                for c in cs:
                    for large_p_min in large_p_mins:
                        large = audit.LargePowerRule(
                            name=f"large_power_c_{c:g}_P{large_p_min}",
                            c=c,
                            p_min=large_p_min,
                        )
                        tested += 1
                        rules = [*base_rules, medium, large]
                        residue_count, rnv = residue_not_verified_count(
                            max_prime=args.max_prime,
                            rules=rules,
                            verified_rules=verified_rules,
                        )
                        ok = rnv == 0
                        if ok:
                            successes += 1
                        if ok or args.show_all:
                            status = "CLOSES" if ok else "open"
                            print(
                                f"{status}: alpha={alpha:g} N={n_min} Pm={p_min} "
                                f"c={c:g} Pl={large_p_min} residue={residue_count} "
                                f"residue_not_verified={rnv}"
                            )

    print()
    print(f"tested={tested}")
    print(f"successful_closures={successes}")
    if successes == 0:
        print("VERDICT: no tested parameter combination closed the residue.")
    else:
        print("VERDICT: at least one tested parameter combination closed the residue.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
