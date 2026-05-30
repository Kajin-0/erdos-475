#!/usr/bin/env python3
"""Local search for insertion-friendly orderings in Erdős 475.

Given a prime p, a set S = A\{x}, and an element x, this script searches for
Graham-valid orderings C of S that minimize the insertion cut-cover obstruction
measure for reinserting x.

This is proof-mining infrastructure, not a proof.  It helps identify whether
hard finite instances admit an ordering of A\{x} with an unblocked insertion cut,
and it records obstruction signatures for local-surgery analysis.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import analyze_insertion_blocks as blocks


@dataclass(frozen=True)
class Candidate:
    order: tuple[int, ...]
    measure: tuple[int, int, int, int, int, int]
    unblocked_cuts: tuple[int, ...]
    source: str

    @property
    def blocked_count(self) -> int:
        return self.measure[0]

    @property
    def total_multiplicity(self) -> int:
        return self.measure[1]


def parse_int_list_csv(text: str) -> list[int]:
    if not text.strip():
        return []
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def insertion_measure(analysis: blocks.InsertionAnalysis) -> tuple[int, int, int, int, int, int]:
    return (
        analysis.blocked_count,
        sum(analysis.cut_multiplicities),
        analysis.crossing_interval_count,
        analysis.total_crossing_length,
        len(analysis.endpoint_blocked_cuts),
        1 if analysis.zero_partial_blocked_cut_zero else 0,
    )


def evaluate_order(order: Sequence[int], x: int, p: int, source: str) -> Candidate | None:
    if not blocks.is_graham_valid(order, p):
        return None
    analysis = blocks.analyze_insertion(order, x, p)
    return Candidate(
        order=tuple(order),
        measure=insertion_measure(analysis),
        unblocked_cuts=tuple(analysis.unblocked_cuts),
        source=source,
    )


def adjacent_swap_neighbors(order: Sequence[int]) -> Iterable[tuple[int, ...]]:
    order = tuple(order)
    for i in range(len(order) - 1):
        values = list(order)
        values[i], values[i + 1] = values[i + 1], values[i]
        yield tuple(values)


def block_reverse_neighbors(order: Sequence[int], max_len: int) -> Iterable[tuple[int, ...]]:
    order = tuple(order)
    n = len(order)
    for length in range(2, min(max_len, n) + 1):
        for i in range(0, n - length + 1):
            values = list(order)
            values[i : i + length] = reversed(values[i : i + length])
            yield tuple(values)


def random_permutation(values: Sequence[int], rng: random.Random) -> tuple[int, ...]:
    arr = list(values)
    rng.shuffle(arr)
    return tuple(arr)


def search(
    *,
    p: int,
    x: int,
    values: Sequence[int],
    seed_order: Sequence[int] | None,
    random_trials: int,
    local_rounds: int,
    max_reverse_len: int,
    rng: random.Random,
) -> Candidate | None:
    seen: set[tuple[int, ...]] = set()
    best: Candidate | None = None

    def consider(order: Sequence[int], source: str) -> None:
        nonlocal best
        key = tuple(order)
        if key in seen:
            return
        seen.add(key)
        cand = evaluate_order(key, x, p, source)
        if cand is None:
            return
        if best is None or cand.measure < best.measure:
            best = cand

    if seed_order is not None:
        consider(seed_order, "seed")

    sorted_values = tuple(sorted(values))
    consider(sorted_values, "sorted")
    consider(tuple(reversed(sorted_values)), "reverse_sorted")

    n = len(values)
    if n <= 8:
        for perm in itertools.permutations(values):
            consider(perm, "exhaustive")
            if best is not None and best.unblocked_cuts:
                # This already proves insertion success for this x and S.
                # Continue exhaustive search only if small enough; for n<=8 this is cheap.
                pass

    for trial in range(random_trials):
        consider(random_permutation(values, rng), f"random_{trial}")

    # Greedy descent over local neighbors from the best order found so far.
    for round_idx in range(local_rounds):
        if best is None:
            break
        improved = False
        current = best
        for neighbor in itertools.chain(
            adjacent_swap_neighbors(current.order),
            block_reverse_neighbors(current.order, max_reverse_len),
        ):
            before = best
            consider(neighbor, f"local_round_{round_idx}")
            if best is not before:
                improved = True
                current = best
        if not improved:
            break

    return best


def row_from_candidate(candidate: Candidate | None, *, p: int, x: int, values: Sequence[int]) -> dict:
    if candidate is None:
        return {
            "p": p,
            "x": x,
            "values": list(values),
            "valid_order_found": False,
        }
    return {
        "p": p,
        "x": x,
        "values": list(values),
        "valid_order_found": True,
        "order": list(candidate.order),
        "measure": list(candidate.measure),
        "blocked_count": candidate.blocked_count,
        "total_multiplicity": candidate.total_multiplicity,
        "unblocked_count": len(candidate.unblocked_cuts),
        "unblocked_cuts": list(candidate.unblocked_cuts),
        "source": candidate.source,
    }


def witness_rows(path: Path) -> Iterable[dict]:
    with path.open("r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            row["_source_line"] = line_no
            yield row


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--p", type=int, help="Prime modulus for direct mode")
    ap.add_argument("--values", help="Comma-separated values of S=A\\{x} in direct mode")
    ap.add_argument("--x", type=int, help="Element to insert in direct mode")
    ap.add_argument("--seed-order", help="Optional comma-separated seed ordering of S")
    ap.add_argument("--witness-jsonl", help="Minimal witness JSONL file")
    ap.add_argument("--limit", type=int, default=None, help="Limit number of x-deletion tasks in witness mode")
    ap.add_argument("--random-trials", type=int, default=200)
    ap.add_argument("--local-rounds", type=int, default=5)
    ap.add_argument("--max-reverse-len", type=int, default=5)
    ap.add_argument("--rng-seed", type=int, default=475)
    ap.add_argument("--jsonl-out", help="Optional output JSONL path")
    args = ap.parse_args()

    rng = random.Random(args.rng_seed)
    output_rows: list[dict] = []

    if args.witness_jsonl:
        processed = 0
        for row in witness_rows(Path(args.witness_jsonl)):
            p = int(row["p"])
            order = [int(v) for v in row["final_order"]]
            for idx, x in enumerate(order):
                values = [*order[:idx], *order[idx + 1 :]]
                candidate = search(
                    p=p,
                    x=x,
                    values=values,
                    seed_order=values,
                    random_trials=args.random_trials,
                    local_rounds=args.local_rounds,
                    max_reverse_len=args.max_reverse_len,
                    rng=rng,
                )
                out = row_from_candidate(candidate, p=p, x=x, values=values)
                out["source_line"] = row["_source_line"]
                out["B"] = row.get("B", [])
                output_rows.append(out)
                processed += 1
                if args.limit is not None and processed >= args.limit:
                    break
            if args.limit is not None and processed >= args.limit:
                break
    else:
        if args.p is None or args.values is None or args.x is None:
            raise SystemExit("direct mode requires --p, --values, and --x, or use --witness-jsonl")
        values = parse_int_list_csv(args.values)
        seed_order = parse_int_list_csv(args.seed_order) if args.seed_order else None
        candidate = search(
            p=args.p,
            x=args.x,
            values=values,
            seed_order=seed_order,
            random_trials=args.random_trials,
            local_rounds=args.local_rounds,
            max_reverse_len=args.max_reverse_len,
            rng=rng,
        )
        output_rows.append(row_from_candidate(candidate, p=args.p, x=args.x, values=values))

    valid = [r for r in output_rows if r.get("valid_order_found")]
    closed = [r for r in valid if r.get("unblocked_count", 0) > 0]
    full_blocked = [r for r in valid if r.get("unblocked_count", 0) == 0]

    print("=== Insertion reordering search summary ===")
    print(f"tasks={len(output_rows)}")
    print(f"valid_order_found={len(valid)}")
    print(f"insertion_success_found={len(closed)}")
    print(f"fully_blocked_best_found={len(full_blocked)}")
    if valid:
        print(f"min_measure={min(r['measure'] for r in valid)}")
        print(f"min_blocked_count={min(r['blocked_count'] for r in valid)}")
        print(f"max_unblocked_count={max(r['unblocked_count'] for r in valid)}")

    if args.jsonl_out:
        out_path = Path(args.jsonl_out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("w", encoding="utf-8") as fh:
            for row in output_rows:
                fh.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")
    else:
        for row in output_rows[:20]:
            print(json.dumps(row, sort_keys=True))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
