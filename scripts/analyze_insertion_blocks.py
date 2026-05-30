#!/usr/bin/env python3
"""Analyze insertion cut-cover obstructions for Erdős 475.

Given a prime p, a Graham-valid ordering C of a set S, and an element x not in S,
this script computes which insertion cuts are blocked by endpoint/crossing
obstructions.

It can also read minimal witness JSONL records of the form

    {"p": 29, "B": [...], "final_order": [...]}

and, for each x in final_order, delete x to form C.  If the deletion ordering C
is Graham-valid, the script analyzes insertion of x back into C.  This is not a
proof by itself; it is a diagnostic bridge between finite witnesses and the
analytic insertion/cut-cover program.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(frozen=True)
class InsertionAnalysis:
    p: int
    x: int
    n: int
    blocked_cuts: tuple[int, ...]
    unblocked_cuts: tuple[int, ...]
    endpoint_blocked_cuts: tuple[int, ...]
    crossing_intervals: tuple[tuple[int, int], ...]
    cut_multiplicities: tuple[int, ...]

    @property
    def blocked_count(self) -> int:
        return len(self.blocked_cuts)

    @property
    def unblocked_count(self) -> int:
        return len(self.unblocked_cuts)

    @property
    def crossing_interval_count(self) -> int:
        return len(self.crossing_intervals)

    @property
    def total_crossing_length(self) -> int:
        return sum(j - k for k, j in self.crossing_intervals)

    @property
    def max_cut_multiplicity(self) -> int:
        return max(self.cut_multiplicities) if self.cut_multiplicities else 0


def parse_int_list_csv(text: str) -> list[int]:
    if not text.strip():
        return []
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def nonempty_partials(order: Sequence[int], p: int) -> list[int]:
    out: list[int] = []
    s = 0
    for value in order:
        s = (s + value) % p
        out.append(s)
    return out


def extended_partials(order: Sequence[int], p: int) -> list[int]:
    return [0, *nonempty_partials(order, p)]


def is_graham_valid(order: Sequence[int], p: int) -> bool:
    sums = nonempty_partials(order, p)
    return len(sums) == len(set(sums))


def is_subset_of_fp_star(values: Iterable[int], p: int) -> bool:
    return all(1 <= int(v) <= p - 1 for v in values)


def analyze_insertion(order: Sequence[int], x: int, p: int) -> InsertionAnalysis:
    """Return cut-cover obstruction data for inserting x into valid order."""
    if not is_subset_of_fp_star(order, p):
        raise ValueError("order must be contained in F_p^*")
    if not (1 <= x <= p - 1):
        raise ValueError("x must be contained in F_p^*")
    if x in set(order):
        raise ValueError("x must not already occur in order")
    if not is_graham_valid(order, p):
        raise ValueError("order is not Graham-valid")

    n = len(order)
    s = extended_partials(order, p)
    multiplicities = [0 for _ in range(n + 1)]
    endpoint_cuts: set[int] = set()
    crossing_intervals: list[tuple[int, int]] = []

    for i in range(n + 1):
        if i >= 1:
            inserted_sum = (s[i] + x) % p
            prefix_nonempty = set(s[1 : i + 1])
            if inserted_sum in prefix_nonempty:
                endpoint_cuts.add(i)
                multiplicities[i] += 1

    target = (-x) % p
    for k in range(1, n + 1):
        for j in range(k, n + 1):
            if (s[j] - s[k]) % p == target:
                # This pair blocks cuts i with k <= i < j.
                if k < j:
                    crossing_intervals.append((k, j))
                    for i in range(k, j):
                        multiplicities[i] += 1

    blocked = {i for i, m in enumerate(multiplicities) if m > 0}
    # Endpoint collisions at a cut are already counted in multiplicities.
    # Keep endpoint_cuts explicit for diagnostic attribution.
    blocked |= endpoint_cuts
    unblocked = [i for i in range(n + 1) if i not in blocked]

    return InsertionAnalysis(
        p=p,
        x=x,
        n=n,
        blocked_cuts=tuple(sorted(blocked)),
        unblocked_cuts=tuple(unblocked),
        endpoint_blocked_cuts=tuple(sorted(endpoint_cuts)),
        crossing_intervals=tuple(crossing_intervals),
        cut_multiplicities=tuple(multiplicities),
    )


def witness_rows(path: Path) -> Iterable[dict]:
    with path.open("r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_no}: invalid JSON: {exc}") from exc
            row["_source_line"] = line_no
            yield row


def analyze_witness_deletions(path: Path, limit: int | None = None) -> list[dict]:
    results: list[dict] = []
    processed = 0
    for row in witness_rows(path):
        p = int(row["p"])
        order = [int(v) for v in row["final_order"]]
        b = [int(v) for v in row.get("B", [])]
        if not is_graham_valid(order, p):
            raise ValueError(f"{path}:{row['_source_line']}: final_order is not valid")
        for idx, x in enumerate(order):
            c_order = [*order[:idx], *order[idx + 1 :]]
            if not is_graham_valid(c_order, p):
                results.append(
                    {
                        "p": p,
                        "B": b,
                        "source_line": row["_source_line"],
                        "x": x,
                        "deleted_order_valid": False,
                    }
                )
                continue
            analysis = analyze_insertion(c_order, x, p)
            results.append(
                {
                    "p": p,
                    "B": b,
                    "source_line": row["_source_line"],
                    "x": x,
                    "deleted_order_valid": True,
                    "blocked_count": analysis.blocked_count,
                    "unblocked_count": analysis.unblocked_count,
                    "endpoint_count": len(analysis.endpoint_blocked_cuts),
                    "crossing_interval_count": analysis.crossing_interval_count,
                    "total_crossing_length": analysis.total_crossing_length,
                    "max_cut_multiplicity": analysis.max_cut_multiplicity,
                    "unblocked_cuts": list(analysis.unblocked_cuts),
                }
            )
            processed += 1
            if limit is not None and processed >= limit:
                return results
    return results


def summarize_results(results: Sequence[dict]) -> None:
    total = len(results)
    invalid_deletions = sum(1 for r in results if not r.get("deleted_order_valid"))
    valid = [r for r in results if r.get("deleted_order_valid")]
    full_blocked = [r for r in valid if r.get("unblocked_count") == 0]
    print("=== Insertion block analysis summary ===")
    print(f"records={total}")
    print(f"valid_deletion_orders={len(valid)}")
    print(f"invalid_deletion_orders={invalid_deletions}")
    print(f"fully_blocked_valid_deletions={len(full_blocked)}")
    if valid:
        print(f"min_unblocked={min(int(r['unblocked_count']) for r in valid)}")
        print(f"max_blocked={max(int(r['blocked_count']) for r in valid)}")
        print(f"max_crossing_intervals={max(int(r['crossing_interval_count']) for r in valid)}")
        print(f"max_cut_multiplicity={max(int(r['max_cut_multiplicity']) for r in valid)}")
    if full_blocked:
        print("WARNING: some valid deletion orders have all cuts blocked")
        for row in full_blocked[:10]:
            print(json.dumps(row, sort_keys=True))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--p", type=int, help="Prime modulus for direct mode")
    ap.add_argument("--order", help="Comma-separated Graham-valid ordering C for direct mode")
    ap.add_argument("--x", type=int, help="Element to insert for direct mode")
    ap.add_argument("--witness-jsonl", help="Minimal witness JSONL file to analyze by deletions")
    ap.add_argument("--limit", type=int, default=None, help="Limit valid deletion analyses in witness mode")
    ap.add_argument("--jsonl-out", help="Optional output path for per-instance JSONL diagnostics")
    args = ap.parse_args()

    if args.witness_jsonl:
        results = analyze_witness_deletions(Path(args.witness_jsonl), limit=args.limit)
        summarize_results(results)
        if args.jsonl_out:
            out = Path(args.jsonl_out)
            out.parent.mkdir(parents=True, exist_ok=True)
            with out.open("w", encoding="utf-8") as fh:
                for row in results:
                    fh.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")
        return 0

    if args.p is None or args.order is None or args.x is None:
        raise SystemExit("direct mode requires --p, --order, and --x, or use --witness-jsonl")

    order = parse_int_list_csv(args.order)
    analysis = analyze_insertion(order, args.x, args.p)
    print("=== Insertion block analysis ===")
    print(f"p={analysis.p}")
    print(f"x={analysis.x}")
    print(f"n={analysis.n}")
    print(f"blocked_count={analysis.blocked_count}")
    print(f"unblocked_count={analysis.unblocked_count}")
    print(f"blocked_cuts={list(analysis.blocked_cuts)}")
    print(f"unblocked_cuts={list(analysis.unblocked_cuts)}")
    print(f"endpoint_blocked_cuts={list(analysis.endpoint_blocked_cuts)}")
    print(f"crossing_intervals={list(analysis.crossing_intervals)}")
    print(f"cut_multiplicities={list(analysis.cut_multiplicities)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
