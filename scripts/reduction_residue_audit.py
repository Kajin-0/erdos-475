#!/usr/bin/env python3
r"""
Reduction residue audit utility for Erdos 475.

This script does not prove any analytic theorem. It is a bookkeeping tool.
Given explicit coverage rules, it computes which (p,t) cases remain and
compares them with the verified finite complement domain in this repository.

Notation:
  p = prime
  t = |A|
  B = F_p^* \ A
  |B| = p - 1 - t

Default built-in known ranges:
  small_set: t <= 12
  very_large: p - 3 <= t <= p - 1, equivalently |B| <= 2

The verified finite domain is data-driven by default:
  certificates/verified_domains.json

The missing analytic input is the published medium/large/sufficiently-large
prime reduction. Add those rules through --range or the p-dependent rule flags
once they are source-certified.

Examples:
  python scripts/reduction_residue_audit.py --max-prime 31

  python scripts/reduction_residue_audit.py --max-prime 31 \
    --cover-verified-domain

  python scripts/reduction_residue_audit.py --max-prime 31 \
    --range p>=37,t=all,name=sufficiently_large_prime_theorem

  python scripts/reduction_residue_audit.py --max-prime 1000 \
    --cover-small-exp-quarter \
    --cover-medium-alpha 0.10:20:37:pham_sauermann_alpha_010 \
    --cover-large-power-c 0.05 \
    --cover-large-power-threshold 37

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
import json
import math
from pathlib import Path
from typing import List, Optional, Protocol, Set, Tuple


@dataclasses.dataclass(frozen=True)
class Case:
    p: int
    t: int

    @property
    def b(self) -> int:
        return self.p - 1 - self.t


class CoverageRule(Protocol):
    name: str

    def covers(self, case: Case) -> bool:
        ...


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


@dataclasses.dataclass
class SmallExpQuarterRule:
    name: str = "small_exp_log_quarter"
    p_min: int = 2

    def covers(self, case: Case) -> bool:
        if case.p < self.p_min:
            return False
        endpoint = math.floor(math.exp(math.log(case.p) ** 0.25))
        return case.t <= endpoint


@dataclasses.dataclass
class MediumAlphaRule:
    name: str
    alpha: float
    n_min: int
    p_min: int

    def covers(self, case: Case) -> bool:
        if case.p < self.p_min:
            return False
        if case.t < self.n_min:
            return False
        endpoint = math.floor(case.p ** (1.0 - self.alpha))
        return case.t <= endpoint


@dataclasses.dataclass
class LargePowerRule:
    name: str
    c: float
    p_min: int

    def covers(self, case: Case) -> bool:
        if case.p < self.p_min:
            return False
        endpoint = math.ceil(case.p ** (1.0 - self.c))
        return case.t >= endpoint


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


def parse_medium_alpha_rule(spec: str) -> MediumAlphaRule:
    """Parse alpha:N:P[:name] into a p-dependent medium coverage rule."""
    parts = spec.split(":")
    if len(parts) not in {3, 4}:
        raise ValueError(
            "--cover-medium-alpha expects alpha:N_min:P_min[:name], "
            f"got {spec!r}"
        )
    alpha = float(parts[0])
    n_min = int(parts[1])
    p_min = int(parts[2])
    name = parts[3] if len(parts) == 4 else f"medium_alpha_{alpha:g}_N{n_min}_P{p_min}"
    if not (0.0 < alpha < 1.0):
        raise ValueError(f"alpha must lie in (0,1), got {alpha}")
    if n_min < 1:
        raise ValueError(f"N_min must be positive, got {n_min}")
    if p_min < 2:
        raise ValueError(f"P_min must be at least 2, got {p_min}")
    return MediumAlphaRule(name=name, alpha=alpha, n_min=n_min, p_min=p_min)


def load_verified_domain_rules(path: Path) -> List[Rule]:
    """Load verified finite complement-domain rules from JSON.

    Expected domain row fields:
      name, p, b_min, b_max

    Optional row fields:
      p_min, p_max, t_min, t_max
    """
    if not path.exists():
        raise FileNotFoundError(f"verified domain file not found: {path}")

    data = json.loads(path.read_text(encoding="utf-8"))
    domains = data.get("domains")
    if not isinstance(domains, list):
        raise ValueError(f"{path}: expected top-level 'domains' list")

    rules: List[Rule] = []
    for idx, row in enumerate(domains, start=1):
        if not isinstance(row, dict):
            raise ValueError(f"{path}: domain row {idx} is not an object")

        name = str(row.get("name", f"verified_domain_{idx}"))
        p_value = row.get("p")
        p_min = row.get("p_min", p_value)
        p_max = row.get("p_max", p_value)

        try:
            rule = Rule(
                name=name,
                p_min=None if p_min is None else int(p_min),
                p_max=None if p_max is None else int(p_max),
                t_min=None if row.get("t_min") is None else int(row["t_min"]),
                t_max=None if row.get("t_max") is None else int(row["t_max"]),
                b_min=None if row.get("b_min") is None else int(row["b_min"]),
                b_max=None if row.get("b_max") is None else int(row["b_max"]),
            )
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{path}: invalid numeric field in domain row {idx}: {row}") from exc

        if rule.p_min is None or rule.p_max is None:
            raise ValueError(f"{path}: domain row {idx} must specify p or p_min/p_max")
        if rule.b_min is None and rule.t_min is None:
            raise ValueError(f"{path}: domain row {idx} must specify b_min/b_max or t_min/t_max")
        if rule.b_min is not None and rule.b_max is None:
            raise ValueError(f"{path}: domain row {idx} has b_min but no b_max")
        if rule.t_min is not None and rule.t_max is None:
            raise ValueError(f"{path}: domain row {idx} has t_min but no t_max")
        rules.append(rule)

    return rules


def verified_cases(max_prime: int, verified_rules: List[CoverageRule]) -> Set[Case]:
    out = set()
    for p in primes_upto(max_prime):
        for t in range(1, p):
            c = Case(p, t)
            if any(rule.covers(c) for rule in verified_rules):
                out.add(c)
    return out


def default_rules() -> List[CoverageRule]:
    return [
        Rule(name="small_set_t_le_12", t_min=None, t_max=12),
        Rule(name="very_large_b_le_2", b_min=None, b_max=2),
    ]


def format_case(c: Case) -> str:
    return f"p={c.p}, t={c.t}, |B|={c.b}"


def summarize_by_prime(cases: List[Case]) -> None:
    by_p = {}
    for c in cases:
        by_p.setdefault(c.p, []).append(c)
    if not by_p:
        print("  none")
        return
    for p in sorted(by_p):
        cs = by_p[p]
        ts = [c.t for c in cs]
        bs = [c.b for c in cs]
        print(f"p={p}: t={min(ts)}..{max(ts)} count={len(ts)} |B| values={sorted(set(bs))}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-prime", type=int, default=31)
    ap.add_argument("--range", action="append", default=[], help="Additional analytic coverage rule")
    ap.add_argument("--no-default-rules", action="store_true")
    ap.add_argument(
        "--verified-domain-file",
        default="certificates/verified_domains.json",
        help="JSON file recording verified finite complement domains",
    )
    ap.add_argument(
        "--cover-verified-domain",
        action="store_true",
        help="Treat the verified finite domain as covered by finite verification rules",
    )
    ap.add_argument(
        "--cover-small-exp-quarter",
        action="store_true",
        help="Add p-dependent small-set rule t <= floor(exp((log p)^(1/4))). Use only for exploratory audits until source-certified.",
    )
    ap.add_argument(
        "--small-exp-quarter-threshold",
        type=int,
        default=2,
        help="Prime threshold for --cover-small-exp-quarter.",
    )
    ap.add_argument(
        "--cover-medium-alpha",
        action="append",
        default=[],
        help="Add medium rule alpha:N_min:P_min[:name], covering N_min <= t <= floor(p^(1-alpha)) for p >= P_min.",
    )
    ap.add_argument(
        "--cover-large-power-c",
        type=float,
        default=None,
        help="Add large-set rule t >= ceil(p^(1-c)). Use only after c is source-certified.",
    )
    ap.add_argument(
        "--cover-large-power-threshold",
        type=int,
        default=2,
        help="Prime threshold for --cover-large-power-c.",
    )
    args = ap.parse_args()

    verified_rules = load_verified_domain_rules(Path(args.verified_domain_file))
    cases = [Case(p, t) for p in primes_upto(args.max_prime) for t in range(1, p)]

    rules: List[CoverageRule] = [] if args.no_default_rules else default_rules()
    if args.cover_verified_domain:
        rules.extend(verified_rules)
    if args.cover_small_exp_quarter:
        rules.append(SmallExpQuarterRule(p_min=args.small_exp_quarter_threshold))
    for spec in args.cover_medium_alpha:
        rules.append(parse_medium_alpha_rule(spec))
    if args.cover_large_power_c is not None:
        c = args.cover_large_power_c
        if not (0.0 < c < 1.0):
            raise ValueError(f"--cover-large-power-c must lie in (0,1), got {c}")
        rules.append(
            LargePowerRule(
                name=f"large_power_c_{c:g}_P{args.cover_large_power_threshold}",
                c=c,
                p_min=args.cover_large_power_threshold,
            )
        )
    rules.extend(parse_rule(x) for x in args.range)

    covered = set()
    coverage_by_rule = {r.name: 0 for r in rules}
    for ccase in cases:
        for rule in rules:
            if rule.covers(ccase):
                covered.add(ccase)
                coverage_by_rule[rule.name] += 1
                break

    residue = sorted(set(cases) - covered, key=lambda ccase: (ccase.p, ccase.t))
    residue_set = set(residue)
    verified = verified_cases(args.max_prime, verified_rules)

    verified_in_residue = sorted(residue_set & verified, key=lambda ccase: (ccase.p, ccase.t))
    residue_not_verified = sorted(residue_set - verified, key=lambda ccase: (ccase.p, ccase.t))
    verified_not_residue = sorted(verified - residue_set, key=lambda ccase: (ccase.p, ccase.t))

    print("=== Erdos 475 reduction residue audit ===")
    print(f"max_prime={args.max_prime}")
    print(f"verified_domain_file={args.verified_domain_file}")
    print(f"total_cases={len(cases)}")
    print(f"coverage_rules={len(rules)}")
    for rule in rules:
        print(f"  {rule.name}: covered_first={coverage_by_rule[rule.name]}")
    print(f"covered_cases={len(covered)}")
    print(f"residue_cases={len(residue)}")
    print()

    print("Residue by prime")
    print("----------------")
    summarize_by_prime(residue)

    print()
    print("Comparison to verified finite domain")
    print("------------------------------------")
    print(f"verified_cases_through_max_prime={len(verified)}")
    print(f"verified_in_residue={len(verified_in_residue)}")
    print(f"residue_not_verified={len(residue_not_verified)}")
    print(f"verified_not_residue={len(verified_not_residue)}")

    if residue_not_verified:
        print()
        print("First residue cases not verified")
        print("---------------------------------")
        for ccase in residue_not_verified[:120]:
            print(format_case(ccase))

    if verified_not_residue:
        print()
        print("Verified cases already covered by supplied rules")
        print("-------------------------------------------------")
        for ccase in verified_not_residue[:120]:
            print(format_case(ccase))
        if len(verified_not_residue) > 120:
            print(f"... {len(verified_not_residue) - 120} more")

    print()
    if not residue_not_verified:
        if residue_set <= verified:
            print("VERDICT: residue is contained in verified finite domain")
        else:
            print("VERDICT: no unverified residue detected")
    else:
        print("VERDICT: residue contains cases outside verified finite domain")
        print("Additional analytic coverage or finite verification is needed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
