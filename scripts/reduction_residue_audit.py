#!/usr/bin/env python3
"""
Reduction residue audit utility for Erdos 475.

This script does not prove any analytic theorem. It is a bookkeeping tool.
Given explicit coverage rules, it computes which (p,t) cases remain and
compares them with the certified complement domain in this repository.

Notation:
  p = prime
  t = |A|
  B = F_p^* \ A
  |B| = p - 1 - t

Default built-in known ranges:
  small_set: t <= 12
  very_large: p - 3 <= t <= p - 1, equivalently |B| <= 2

The missing analytic input is the published medium/large/sufficiently-large
prime reduction. Add those rules through --range once they are known.

Examples:
  python scripts/reduction_residue_audit.py --max-prime 31

  python scripts/reduction_residue_audit.py --max-prime 31 \
    --range p=29,t=13..20,name=example_p29_mid \
    --range p=31,t=13..23,name=example_p31_mid

Range syntax:
  p=29,t=13..20,name=label
  p=29..31,t=13..20,name=label
  p=all,t=13..20,name=label
  p>=37,t=all,name=sufficiently_large_primes
  p=all,b=3..7,name=small_complement
"""

from __future__ import annotations

import argparse
import dataclasses
import re
from typing import Iterable, List, Optional, Set, Tuple


@dataclasses.dataclass(frozen=True)
class Case:
    p: int
    t: int

    @property
    def b(self) -> int:
        return self.p - 1 - self.t


@dataclasses.dataclass
class Rule:
    name: str
    p_min: Optional[int] = None
    p_max: Optional[int] = None
    t_min: Optional[int] = None
    t_max: Optional[int] = None
    b_min: Optional[int] = None
    b_max: Optional[int] = None

    def covers(self, case: Case) -> bool:
        if self.p_min is not None and case.p < self.p_min:
            return False
        if self.p_max is not None and case.p > self.p_max:
            return False
        if self.t_min is not None and case.t < self.t_min:
            return False
        if self.t_max is not None and case.t > self.t_max:
            return False
        if self.b_min is not None and case.b < self.b_min:
            return False
        if self.b_max is not None and case.b > self.b_max:
            return False
        return True


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def primes_upto(n: int) -> List[int]:
    return [p for p in range(2, n + 1) if is_prime(p)]


def parse_range_piece(text: str) -> Tuple[Optional[int], Optional[int]]:
    text = text.strip()
    if text in {"all", "*"}:
        return None, None
    if text.startswith(">="):
        return int(text[2:]), None
    if text.startswith("<="):
        return None, int(text[2:])
    if ".." in text:
        a, b = text.split("..", 1)
        return int(a), int(b)
    v = int(text)
    return v, v


def parse_rule(spec: str) -> Rule:
    parts = {}
    for token in spec.split(","):
        token = token.strip()
        if not token:
            continue
        if "=" not in token:
            raise ValueError(f"Bad token in rule: {token}")
        k, v = token.split("=", 1)
        parts[k.strip()] = v.strip()

    name = parts.get("name", spec)
    rule = Rule(name=name)

    if "p" in parts:
        rule.p_min, rule.p_max = parse_range_piece(parts["p"])
    if "t" in parts:
        rule.t_min, rule.t_max = parse_range_piece(parts["t"])
    if "b" in parts:
        rule.b_min, rule.b_max = parse_range_piece(parts["b"])

    return rule


def certified_cases() -> Set[Case]:
    out = set()
    for p, b_min, b_max in [(29, 3, 7), (31, 3, 6)]:
        for b in range(b_min, b_max + 1):
            t = p - 1 - b
            out.add(Case(p, t))
    return out


def default_rules() -> List[Rule]:
    return [
        Rule(name="small_set_t_le_12", t_min=None, t_max=12),
        Rule(name="very_large_b_le_2", b_min=None, b_max=2),
    ]


def format_case(c: Case) -> str:
    return f"p={c.p}, t={c.t}, |B|={c.b}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-prime", type=int, default=31)
    ap.add_argument("--range", action="append", default=[], help="Additional coverage rule")
    ap.add_argument("--no-default-rules", action="store_true")
    args = ap.parse_args()

    cases = [Case(p, t) for p in primes_upto(args.max_prime) for t in range(1, p)]

    rules = [] if args.no_default_rules else default_rules()
    rules.extend(parse_rule(x) for x in args.range)

    covered = set()
    coverage_by_rule = {r.name: 0 for r in rules}
    for c in cases:
        for r in rules:
            if r.covers(c):
                covered.add(c)
                coverage_by_rule[r.name] += 1
                break

    residue = sorted(set(cases) - covered, key=lambda c: (c.p, c.t))
    cert = certified_cases()
    residue_set = set(residue)

    certified_in_residue = sorted(residue_set & cert, key=lambda c: (c.p, c.t))
    residue_not_certified = sorted(residue_set - cert, key=lambda c: (c.p, c.t))
    certified_not_residue = sorted(cert - residue_set, key=lambda c: (c.p, c.t))

    print("=== Erdos 475 reduction residue audit ===")
    print(f"max_prime={args.max_prime}")
    print(f"total_cases={len(cases)}")
    print(f"coverage_rules={len(rules)}")
    for r in rules:
        print(f"  {r.name}: covered_first={coverage_by_rule[r.name]}")
    print(f"covered_cases={len(covered)}")
    print(f"residue_cases={len(residue)}")
    print()

    by_p = {}
    for c in residue:
        by_p.setdefault(c.p, []).append(c)

    print("Residue by prime")
    print("----------------")
    for p in sorted(by_p):
        ts = [c.t for c in by_p[p]]
        bs = [c.b for c in by_p[p]]
        print(f"p={p}: t={min(ts)}..{max(ts)} count={len(ts)} |B| values={sorted(set(bs))}")

    print()
    print("Comparison to certified domain")
    print("------------------------------")
    print(f"certified_cases={len(cert)}")
    print(f"certified_in_residue={len(certified_in_residue)}")
    print(f"residue_not_certified={len(residue_not_certified)}")
    print(f"certified_not_residue={len(certified_not_residue)}")

    if residue_not_certified:
        print()
        print("First residue cases not certified")
        print("----------------------------------")
        for c in residue_not_certified[:80]:
            print(format_case(c))

    if certified_not_residue:
        print()
        print("Certified cases already covered by supplied rules")
        print("--------------------------------------------------")
        for c in certified_not_residue:
            print(format_case(c))

    print()
    if residue_set == cert:
        print("VERDICT: residue equals certified domain")
    else:
        print("VERDICT: residue does not yet equal certified domain")
        print("This is expected until all published analytic ranges are encoded.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
