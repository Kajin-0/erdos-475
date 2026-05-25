#!/usr/bin/env python3
"""
Summarize symbolic non-tautological collision blocks in pure_worse_only m=3 residuals.

Input is produced by:

    scripts/analyze_pure_m3_terminal_structure.py

Typical inputs:

    logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
    logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl

This script maps numerical atoms back to symbolic local labels:

    A1,A2,z,q,B1,...,Bs,Y1,... and X labels when present

and reports symbolic collision blocks by permutation.  The goal is to convert
empirical collisions into algebraic equations suitable for proof work.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

STABLE_PERMS = {"A B q z", "B A q z", "B z q A", "z q A B", "z q B A"}


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


def first_candidate(record: dict[str, Any]) -> dict[str, Any]:
    cas = record.get("candidate_analyses", [])
    if not cas:
        return {}
    return cas[0].get("candidate", {}) or {}


def symbolic_labels(record: dict[str, Any], cand: dict[str, Any]) -> dict[int, list[str]]:
    """Map atom values to possible symbolic labels.

    Since S is a set, values are unique in a record, but store lists for safety.
    """
    order = [int(x) for x in record.get("order", [])]
    z_i = int(cand.get("z_i", 0))
    ext = int(cand.get("external_index", len(order)))
    A = [int(x) for x in cand.get("A", [])]
    B = [int(x) for x in cand.get("B", [])]
    z = int(cand.get("z"))
    q = int(cand.get("q"))

    label_by_value: dict[int, list[str]] = defaultdict(list)

    # Original structure is X A z q B Y.
    for idx, value in enumerate(order[:z_i]):
        label_by_value[int(value)].append(f"X{idx+1}")
    for idx, value in enumerate(A):
        label_by_value[int(value)].append(f"A{idx+1}")
    label_by_value[z].append("z")
    label_by_value[q].append("q")
    for idx, value in enumerate(B):
        label_by_value[int(value)].append(f"B{idx+1}")
    for idx, value in enumerate(order[ext:]):
        label_by_value[int(value)].append(f"Y{idx+1}")
    return label_by_value


def symbolic_block(block: list[int], labels: dict[int, list[str]]) -> str:
    parts = []
    for value in block:
        labs = labels.get(int(value))
        if labs:
            parts.append("/".join(labs))
        else:
            parts.append(f"?{value}")
    return " ".join(parts)


def classify_symbolic(sym: str) -> str:
    toks = sym.split()
    if set(toks) == {"A1", "A2", "z"} and len(toks) == 3:
        return "old_triple_Az"
    if "z" in toks and all(t == "z" or t.startswith("B") for t in toks):
        return "terminal_zB"
    return "nontautological"


def summarize(records: list[dict[str, Any]], example_limit: int) -> dict[str, Any]:
    worse = [r for r in records if r.get("pure_label") == "pure_worse_only"]
    sym_by_perm: dict[str, Counter[str]] = defaultdict(Counter)
    shortest_sym_by_perm: dict[str, Counter[str]] = defaultdict(Counter)
    stable_sym_by_perm: dict[str, Counter[str]] = defaultdict(Counter)
    support_sym_by_perm: dict[str, dict[str, Counter[str]]] = defaultdict(lambda: defaultdict(Counter))
    aqzb_class_counts = Counter()
    examples = []

    for record in worse:
        for ca in record.get("candidate_analyses", []):
            cand = ca.get("candidate", {})
            labels = symbolic_labels(record, cand)
            support = str(cand.get("support_length"))
            for ma in ca.get("moves_analyzed", []):
                pk = ma.get("perm_key", "UNKNOWN")
                nont_syms = []
                for zint in ma.get("new_zero_intervals", []) or []:
                    sym = symbolic_block(zint.get("block", []), labels)
                    cls = classify_symbolic(sym)
                    if pk == "A q z B":
                        aqzb_class_counts[cls] += 1
                    if cls != "nontautological":
                        continue
                    nont_syms.append((len(zint.get("block", [])), sym, zint))
                    sym_by_perm[pk][sym] += 1
                    support_sym_by_perm[support][pk][sym] += 1
                    if pk in STABLE_PERMS:
                        stable_sym_by_perm[pk][sym] += 1
                if nont_syms:
                    nont_syms.sort(key=lambda x: (x[0], x[1]))
                    shortest = nont_syms[0][1]
                    shortest_sym_by_perm[pk][shortest] += 1
                    if len(examples) < example_limit:
                        length, sym, zint = nont_syms[0]
                        examples.append(
                            {
                                "p": record.get("p"),
                                "record_index": record.get("record_index"),
                                "perm": pk,
                                "support_length": cand.get("support_length"),
                                "A": cand.get("A"),
                                "z": cand.get("z"),
                                "q": cand.get("q"),
                                "B": cand.get("B"),
                                "symbolic_block": sym,
                                "length": length,
                                "numeric_block": zint.get("block"),
                                "signature": f"{zint.get('left_label') or 'ext'}={zint.get('right_label') or 'ext'}:L{zint.get('length')}:{zint.get('span_type')}",
                            }
                        )

    return {
        "input_records": len(records),
        "pure_worse_records": len(worse),
        "symbolic_blocks_by_perm": {k: dict(v.most_common(25)) for k, v in sym_by_perm.items()},
        "shortest_symbolic_blocks_by_perm": {k: dict(v.most_common(25)) for k, v in shortest_sym_by_perm.items()},
        "stable_perm_symbolic_blocks": {k: dict(v.most_common(25)) for k, v in stable_sym_by_perm.items()},
        "symbolic_blocks_by_support_and_perm": {
            s: {pk: dict(cnt.most_common(10)) for pk, cnt in by_perm.items()}
            for s, by_perm in support_sym_by_perm.items()
        },
        "A_q_z_B_collision_class_counts": dict(aqzb_class_counts.most_common()),
        "examples": examples,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input analyzed pure m3 structure JSONL files.")
    ap.add_argument("--out", default="-", help="Output JSON path, or '-' for stdout.")
    ap.add_argument("--pretty", action="store_true")
    ap.add_argument("--example-limit", type=int, default=20)
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
