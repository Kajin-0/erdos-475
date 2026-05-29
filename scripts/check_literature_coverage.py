#!/usr/bin/env python3
"""
Coverage interval checker for Erdős 475 / Graham's rearrangement problem.

This script does not prove any literature theorem.  It audits whether a declared
set of effective theorem ranges covers every pair (p,t) outside a declared finite
certificate domain.

The intended workflow is:

  1. Extract exact effective thresholds from the literature into JSON.
  2. Declare the finite computational certificate domain.
  3. Run this script to find uncovered (p,t) pairs up to a chosen audit bound.

The script is deliberately conservative.  If no literature JSON is supplied, it
runs only with finite domains and reports everything else as uncovered.
"""

from __future__ import annotations

import argparse
import ast
import json
import math
import operator
from dataclasses import dataclass
from typing import Any, Callable, Dict, Iterable, List, Sequence, Tuple


OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

FUNCS = {
    "floor": math.floor,
    "ceil": math.ceil,
    "log": math.log,
    "sqrt": math.sqrt,
    "exp": math.exp,
    "min": min,
    "max": max,
}


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


def safe_eval(expr: Any, names: Dict[str, float]) -> float:
    """Evaluate a small arithmetic expression in p,t,b and declared parameters."""
    if isinstance(expr, (int, float)):
        return expr
    if expr is None:
        raise ValueError("expression is None")
    if not isinstance(expr, str):
        raise TypeError(f"unsupported expression type: {type(expr)!r}")

    tree = ast.parse(expr, mode="eval")

    def _eval(node: ast.AST) -> float:
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError(f"unsupported constant: {node.value!r}")
        if isinstance(node, ast.Name):
            if node.id in names:
                return names[node.id]
            raise NameError(f"unknown name in expression: {node.id}")
        if isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in OPS:
                raise ValueError(f"unsupported operator: {op_type.__name__}")
            return OPS[op_type](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in OPS:
                raise ValueError(f"unsupported unary operator: {op_type.__name__}")
            return OPS[op_type](_eval(node.operand))
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name) or node.func.id not in FUNCS:
                raise ValueError("unsupported function call")
            args = [_eval(arg) for arg in node.args]
            return FUNCS[node.func.id](*args)
        raise ValueError(f"unsupported expression node: {type(node).__name__}")

    return _eval(tree)


@dataclass(frozen=True)
class Domain:
    p: int
    b_min: int
    b_max: int

    def contains(self, p: int, t: int) -> bool:
        if p != self.p:
            return False
        b = p - 1 - t
        return self.b_min <= b <= self.b_max


@dataclass(frozen=True)
class TheoremRange:
    source_id: str
    kind: str
    p_min: int | None
    p_max: int | None
    t_min_expr: Any | None
    t_max_expr: Any | None
    b_min_expr: Any | None
    b_max_expr: Any | None
    parameters: Dict[str, float]

    def covers(self, p: int, t: int) -> bool:
        b = p - 1 - t
        names = {"p": float(p), "t": float(t), "b": float(b), **self.parameters}

        if self.p_min is not None and p < self.p_min:
            return False
        if self.p_max is not None and p > self.p_max:
            return False
        if self.t_min_expr is not None and t < math.ceil(safe_eval(self.t_min_expr, names)):
            return False
        if self.t_max_expr is not None and t > math.floor(safe_eval(self.t_max_expr, names)):
            return False
        if self.b_min_expr is not None and b < math.ceil(safe_eval(self.b_min_expr, names)):
            return False
        if self.b_max_expr is not None and b > math.floor(safe_eval(self.b_max_expr, names)):
            return False
        return True


def parse_domain(text: str) -> Domain:
    # Format: p:b_min-b_max, e.g. 29:3-7
    left, right = text.split(":", 1)
    p = int(left)
    if "-" in right:
        b_min_s, b_max_s = right.split("-", 1)
        b_min = int(b_min_s)
        b_max = int(b_max_s)
    else:
        b_min = b_max = int(right)
    if b_min > b_max:
        raise ValueError(f"invalid domain {text!r}: b_min > b_max")
    return Domain(p=p, b_min=b_min, b_max=b_max)


def load_theorem_ranges(path: str | None) -> List[TheoremRange]:
    if path is None:
        return []
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    items = raw.get("ranges", raw if isinstance(raw, list) else [])
    out: List[TheoremRange] = []
    for item in items:
        out.append(
            TheoremRange(
                source_id=item["source_id"],
                kind=item.get("kind", "base_graham"),
                p_min=item.get("p_min"),
                p_max=item.get("p_max"),
                t_min_expr=item.get("t_min_expr"),
                t_max_expr=item.get("t_max_expr"),
                b_min_expr=item.get("b_min_expr"),
                b_max_expr=item.get("b_max_expr"),
                parameters={k: float(v) for k, v in item.get("parameters", {}).items()},
            )
        )
    return out


def explain_pair(p: int, t: int, ranges: Sequence[TheoremRange], finite_domains: Sequence[Domain]) -> str:
    b = p - 1 - t
    for d in finite_domains:
        if d.contains(p, t):
            return f"finite:{d.p}:{d.b_min}-{d.b_max}"
    for r in ranges:
        if r.covers(p, t):
            return f"theorem:{r.source_id}"
    return "uncovered"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--coverage-json", help="JSON file with effective theorem ranges")
    ap.add_argument("--max-p", type=int, default=101)
    ap.add_argument(
        "--finite-domain",
        action="append",
        default=[],
        help="Finite certified complement domain p:bmin-bmax, e.g. 29:3-7. Repeatable.",
    )
    ap.add_argument("--show-uncovered", type=int, default=100)
    ap.add_argument("--require-full-coverage", action="store_true")
    args = ap.parse_args()

    finite_domains = [parse_domain(x) for x in args.finite_domain]
    ranges = load_theorem_ranges(args.coverage_json)

    total = 0
    covered_by_finite = 0
    covered_by_theorem = 0
    uncovered: List[Tuple[int, int, int]] = []

    for p in primes_upto(args.max_p):
        for t in range(1, p):
            total += 1
            label = explain_pair(p, t, ranges, finite_domains)
            if label.startswith("finite:"):
                covered_by_finite += 1
            elif label.startswith("theorem:"):
                covered_by_theorem += 1
            else:
                uncovered.append((p, t, p - 1 - t))

    print("=== Erdős 475 literature coverage audit ===")
    print(f"max_p={args.max_p}")
    print(f"total_pairs={total}")
    print(f"finite_domains={len(finite_domains)}")
    print(f"theorem_ranges={len(ranges)}")
    print(f"covered_by_finite={covered_by_finite}")
    print(f"covered_by_theorem={covered_by_theorem}")
    print(f"uncovered={len(uncovered)}")

    if uncovered:
        print()
        print(f"First {min(len(uncovered), args.show_uncovered)} uncovered pairs as (p,t,b):")
        for p, t, b in uncovered[: args.show_uncovered]:
            print(f"  p={p} t={t} b={b}")

    if args.require_full_coverage and uncovered:
        print("VERDICT: FAIL")
        return 1

    print("VERDICT: PASS" if not uncovered else "VERDICT: INCOMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
