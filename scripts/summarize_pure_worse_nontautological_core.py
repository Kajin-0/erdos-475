#!/usr/bin/env python3
"""
Summarize non-tautological collision structure in pure_worse_only m=3 terminal residuals.

Input is produced by:

    scripts/analyze_pure_m3_terminal_structure.py

Typical inputs:

    logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
    logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl

This script focuses on pure_worse_only records and classifies each new zero interval as:

    old_triple_Az       block multiset equals A + z
    terminal_zB         block multiset equals z + B
    nontautological     any other zero interval

The goal is to ignore tautological A/z zero-triple recreations and expose the
extra collision equations that make separated-A,z permutations worse.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


def iter_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSON in {path}:{line_no}: {exc}") from exc


def sorted_block(xs: list[int]) -> tuple[int, ...]:
    return tuple(sorted(int(x) for x in xs))


def perm_key(perm: list[str] | tuple[str, ...]) -> str:
    return " ".join(str(x) for x in perm)


def az_adjacent(perm: list[str] | tuple[str, ...]) -> bool:
    p = list(perm)
    try:
        ia = p.index("A")
        iz = p.index("z")
    except ValueError:
        return False
    return abs(ia - iz) == 1


def classify_interval(block: list[int], cand: dict[str, Any]) -> str:
    A = [int(x) for x in cand.get("A", [])]
    z = int(cand.get("z"))
    B = [int(x) for x in cand.get("B", [])]
    sb = sorted_block(block)
    if sb == sorted_block(A + [z]):
        return "old_triple_Az"
    if sb == sorted_block(B + [z]):
        return "terminal_zB"
    return "nontautological"


def move_collision_classes(cand: dict[str, Any], move: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
    for zint in move.get("new_zero_intervals", []) or []:
        cls = classify_interval(zint.get("block", []), cand)
        out.append(
            {
                "class": cls,
                "signature": signature(zint),
                "length": zint.get("length"),
                "span_type": zint.get("span_type"),
                "block": zint.get("block"),
                "left_label": zint.get("left_label"),
                "right_label": zint.get("right_label"),
                "touches_moved_boundary": zint.get("touches_moved_boundary"),
            }
        )
    return out


def signature(zint: dict[str, Any]) -> str:
    left = zint.get("left_label") or "ext"
    right = zint.get("right_label") or "ext"
    return f"{left}={right}:L{zint.get('length')}:{zint.get('span_type')}"


def first_candidate(record: dict[str, Any]) -> dict[str, Any]:
    cas = record.get("candidate_analyses", [])
    if not cas:
        return {}
    return cas[0].get("candidate", {}) or {}


def compact_example(record: dict[str, Any], move: dict[str, Any], cand: dict[str, Any], classified: list[dict[str, Any]]) -> dict[str, Any]:
    nont = [x for x in classified if x["class"] == "nontautological"]
    return {
        "p": record.get("p"),
        "record_index": record.get("record_index"),
        "order": record.get("order"),
        "candidate": {
            "support_length": cand.get("support_length"),
            "X_length": cand.get("X_length"),
            "Y_length": cand.get("Y_length"),
            "A": cand.get("A"),
            "z": cand.get("z"),
            "q": cand.get("q"),
            "B": cand.get("B"),
        },
        "perm": move.get("perm"),
        "new_defect": move.get("new_defect"),
        "nontautological_collisions": nont[:5],
    }


def summarize(records: list[dict[str, Any]], example_limit: int) -> dict[str, Any]:
    worse = [r for r in records if r.get("pure_label") == "pure_worse_only"]
    support_hist = Counter()
    perm_counts = Counter()
    perm_adj_counts = Counter()
    class_counts = Counter()
    nont_sig_counts = Counter()
    nont_sig_by_perm: dict[str, Counter[str]] = defaultdict(Counter)
    nont_records_by_perm: dict[str, Counter[str]] = defaultdict(Counter)
    perm_record_counts: Counter[str] = Counter()
    separated_perm_records = Counter()
    separated_perm_with_nont = Counter()
    examples = []

    for r in worse:
        seen_perm_this_record = set()
        seen_perm_nont_this_record = set()
        c0 = first_candidate(r)
        if c0.get("support_length") is not None:
            support_hist[str(c0["support_length"])] += 1
        for ca in r.get("candidate_analyses", []):
            cand = ca.get("candidate", {})
            for ma in ca.get("moves_analyzed", []):
                pk = ma.get("perm_key") or perm_key(ma.get("perm", []))
                perm_counts[pk] += 1
                adj = az_adjacent(ma.get("perm", []))
                perm_adj_counts["Az_adjacent" if adj else "Az_separated"] += 1
                seen_perm_this_record.add(pk)
                classified = move_collision_classes(cand, ma)
                move_has_nont = False
                for item in classified:
                    class_counts[item["class"]] += 1
                    if item["class"] == "nontautological":
                        move_has_nont = True
                        nont_sig_counts[item["signature"]] += 1
                        nont_sig_by_perm[pk][item["signature"]] += 1
                if move_has_nont:
                    seen_perm_nont_this_record.add(pk)
                    if len(examples) < example_limit:
                        examples.append(compact_example(r, ma, cand, classified))
        for pk in seen_perm_this_record:
            perm_record_counts[pk] += 1
        for pk in seen_perm_nont_this_record:
            nont_records_by_perm[pk]["records_with_nont"] += 1
        for pk in seen_perm_this_record:
            # Need adjacency from key.
            parts = pk.split()
            if not az_adjacent(parts):
                separated_perm_records[pk] += 1
                if pk in seen_perm_nont_this_record:
                    separated_perm_with_nont[pk] += 1

    universal_nont_by_perm = {}
    for pk, nrec in separated_perm_records.items():
        universal_nont_by_perm[pk] = {
            "records": nrec,
            "records_with_nont": separated_perm_with_nont.get(pk, 0),
            "all_have_nont": separated_perm_with_nont.get(pk, 0) == nrec,
            "top_nont_signatures": dict(nont_sig_by_perm.get(pk, Counter()).most_common(10)),
        }

    def sort_numeric(c: Counter[str]) -> dict[str, int]:
        def keyfn(item: tuple[str, int]) -> tuple[int, str]:
            k, _v = item
            try:
                return (int(k), k)
            except Exception:
                return (10**9, k)
        return dict(sorted(c.items(), key=keyfn))

    return {
        "input_records": len(records),
        "pure_worse_records": len(worse),
        "support_length_histogram": sort_numeric(support_hist),
        "perm_counts": dict(perm_counts.most_common()),
        "perm_adjacency_counts": dict(perm_adj_counts),
        "collision_class_counts": dict(class_counts.most_common()),
        "top_nontautological_signatures": dict(nont_sig_counts.most_common(50)),
        "nontautological_signatures_by_perm": {k: dict(v.most_common(20)) for k, v in nont_sig_by_perm.items()},
        "separated_perm_nontautological_record_coverage": universal_nont_by_perm,
        "examples": examples,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input analyzed pure m3 structure JSONL files.")
    ap.add_argument("--out", default="-", help="Output JSON path, or '-' for stdout.")
    ap.add_argument("--pretty", action="store_true")
    ap.add_argument("--example-limit", type=int, default=10)
    args = ap.parse_args()

    records: list[dict[str, Any]] = []
    input_counts = {}
    for name in args.jsonl:
        path = Path(name)
        loaded = list(iter_jsonl(path))
        input_counts[str(path)] = len(loaded)
        records.extend(loaded)

    summary = summarize(records, args.example_limit)
    summary["input_files"] = input_counts

    text = json.dumps(summary, indent=2 if args.pretty else None, sort_keys=True)
    if args.out == "-":
        print(text)
    else:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
