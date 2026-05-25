#!/usr/bin/env python3
"""
Summarize the collision-signature core of pure_worse_only m=3 terminal residuals.

Input is produced by:

    scripts/analyze_pure_m3_terminal_structure.py

Typical inputs:

    logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
    logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl

This script focuses on records labeled:

    pure_worse_only

and reports record-level signature structure:

    - support length histogram
    - X/Y length histogram
    - signatures present in every pure_worse_only record
    - signatures present by support length
    - per-permutation signature cores
    - representative compact examples by support length
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


def record_signatures(record: dict[str, Any]) -> set[str]:
    sigs: set[str] = set()
    for ca in record.get("candidate_analyses", []):
        for ma in ca.get("moves_analyzed", []):
            for sig in ma.get("touching_collision_signatures", []) or []:
                sigs.add(sig)
    return sigs


def record_perm_signatures(record: dict[str, Any]) -> dict[str, set[str]]:
    out: dict[str, set[str]] = defaultdict(set)
    for ca in record.get("candidate_analyses", []):
        for ma in ca.get("moves_analyzed", []):
            pk = ma.get("perm_key", "UNKNOWN")
            for sig in ma.get("touching_collision_signatures", []) or []:
                out[pk].add(sig)
    return dict(out)


def first_candidate(record: dict[str, Any]) -> dict[str, Any]:
    cas = record.get("candidate_analyses", [])
    if not cas:
        return {}
    return cas[0].get("candidate", {}) or {}


def support_length(record: dict[str, Any]) -> int | None:
    c = first_candidate(record)
    s = c.get("support_length")
    return int(s) if s is not None else None


def compact_example(record: dict[str, Any]) -> dict[str, Any]:
    c = first_candidate(record)
    return {
        "p": record.get("p"),
        "record_index": record.get("record_index"),
        "order": record.get("order"),
        "defect": record.get("defect"),
        "old_unique_zero_triple": record.get("old_unique_zero_triple"),
        "candidate": {
            "X_length": c.get("X_length"),
            "Y_length": c.get("Y_length"),
            "support_length": c.get("support_length"),
            "A": c.get("A"),
            "z": c.get("z"),
            "q": c.get("q"),
            "B": c.get("B"),
            "sum_A": c.get("sum_A"),
            "sum_B": c.get("sum_B"),
            "z_plus_B": c.get("z_plus_B"),
        },
        "signature_sample": sorted(record_signatures(record))[:20],
    }


def summarize(records: list[dict[str, Any]], example_limit: int) -> dict[str, Any]:
    worse = [r for r in records if r.get("pure_label") == "pure_worse_only"]
    support_hist: Counter[str] = Counter()
    x_hist: Counter[str] = Counter()
    y_hist: Counter[str] = Counter()
    signature_presence: Counter[str] = Counter()
    signature_by_support: dict[str, Counter[str]] = defaultdict(Counter)
    record_count_by_support: Counter[str] = Counter()
    perm_signature_presence: dict[str, Counter[str]] = defaultdict(Counter)
    perm_record_counts: Counter[str] = Counter()
    new_defect_hist: Counter[str] = Counter()
    examples_by_support: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for r in worse:
        c = first_candidate(r)
        s = str(c.get("support_length"))
        support_hist[s] += 1
        record_count_by_support[s] += 1
        x_hist[str(c.get("X_length"))] += 1
        y_hist[str(c.get("Y_length"))] += 1
        sigs = record_signatures(r)
        signature_presence.update(sigs)
        signature_by_support[s].update(sigs)
        pmap = record_perm_signatures(r)
        for pk, psigs in pmap.items():
            perm_record_counts[pk] += 1
            perm_signature_presence[pk].update(psigs)
        for ca in r.get("candidate_analyses", []):
            for ma in ca.get("moves_analyzed", []):
                nd = ma.get("new_defect")
                if nd is not None:
                    new_defect_hist[str(tuple_key(nd))] += 1
        if len(examples_by_support[s]) < example_limit:
            examples_by_support[s].append(compact_example(r))

    universal = sorted([sig for sig, count in signature_presence.items() if count == len(worse)])

    universal_by_support = {}
    for s, count in record_count_by_support.items():
        universal_by_support[s] = sorted([sig for sig, c in signature_by_support[s].items() if c == count])

    universal_by_perm = {}
    for pk, count in perm_record_counts.items():
        universal_by_perm[pk] = sorted([sig for sig, c in perm_signature_presence[pk].items() if c == count])

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
        "X_length_histogram": sort_numeric(x_hist),
        "Y_length_histogram": sort_numeric(y_hist),
        "universal_signatures": universal,
        "top_signature_presence": dict(signature_presence.most_common(50)),
        "universal_signatures_by_support_length": universal_by_support,
        "top_signatures_by_support_length": {k: dict(v.most_common(25)) for k, v in signature_by_support.items()},
        "universal_signatures_by_perm": universal_by_perm,
        "perm_record_counts": dict(perm_record_counts.most_common()),
        "new_defect_histogram": dict(new_defect_hist.most_common(50)),
        "examples_by_support_length": dict(examples_by_support),
    }


def tuple_key(x: Any) -> str:
    if isinstance(x, (list, tuple)):
        return "(" + ",".join(tuple_key(v) if isinstance(v, (list, tuple)) else str(v) for v in x) + ")"
    return str(x)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input analyzed pure m3 structure JSONL files.")
    ap.add_argument("--out", default="-", help="Output JSON path, or '-' for stdout.")
    ap.add_argument("--pretty", action="store_true")
    ap.add_argument("--example-limit", type=int, default=2)
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
