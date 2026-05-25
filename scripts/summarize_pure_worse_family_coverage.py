#!/usr/bin/env python3
"""
Record-level family coverage for pure_worse_only m=3 terminal residuals.

Input is produced by:

    scripts/analyze_pure_m3_terminal_structure.py

Typical inputs:

    logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
    logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl

This script classifies each non-tautological symbolic zero block into coarse
families and reports record-level coverage by permutation:

    permutation -> family -> records hit / records total

The goal is to identify proof-ready universal statements such as:

    B z q A -> B_tail+zq+A in every pure_worse_only record.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

STABLE_PERMS = ("A B q z", "B A q z", "B z q A", "z q A B", "z q B A")
TOKEN_RE = re.compile(r"^([A-Z]+|z|q)(\d+)?$")


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


def parse_token(tok: str) -> tuple[str, int | None]:
    m = TOKEN_RE.match(tok)
    if not m:
        return (tok, None)
    base, idx = m.group(1), m.group(2)
    return (base, int(idx) if idx is not None else None)


def bases(tokens: list[str]) -> list[str]:
    return [parse_token(t)[0] for t in tokens]


def indices_of(tokens: list[str], base: str) -> list[int]:
    return [idx for b, idx in (parse_token(t) for t in tokens) if b == base and idx is not None]


def is_prefix(idxs: list[int]) -> bool:
    return bool(idxs) and sorted(idxs) == list(range(1, max(idxs) + 1))


def is_suffix_like(idxs: list[int]) -> bool:
    return bool(idxs) and not is_prefix(idxs)


def has_only(tokens: list[str], allowed: set[str]) -> bool:
    return set(bases(tokens)).issubset(allowed)


def classify_symbolic_block(sym: str) -> str:
    toks = sym.split()
    bs = bases(toks)
    sbs = set(bs)
    a_idxs = indices_of(toks, "A")
    b_idxs = indices_of(toks, "B")
    has_A1A2 = sorted(a_idxs) == [1, 2]
    has_A2_only = sorted(a_idxs) == [2]
    b_prefix = is_prefix(b_idxs)
    b_tail = is_suffix_like(b_idxs)

    if any(b == "X" for b in bs):
        return "mixed_X_prefix"

    if sbs == {"A", "B"}:
        if has_A1A2 and b_prefix:
            return "A_all+B_prefix"
        if has_A2_only and b_prefix:
            return "A_suffix+B_prefix"
        if b_tail:
            return "B_tail+A_prefix"
        return "A_B_mixed"

    if sbs == {"B", "q"}:
        if b_tail:
            return "B_tail+q"
        if b_prefix:
            return "B_prefix+q"
        return "B_mixed+q"

    if sbs == {"z", "Y"}:
        return "z+Y_prefix"

    if sbs == {"q", "z", "Y"}:
        return "qz+Y_prefix"

    if has_only(toks, {"A", "B", "q"}):
        if "q" in bs and has_A1A2 and b_prefix:
            return "q+A_all+B_prefix"
        if "q" in bs and has_A2_only and b_prefix:
            return "q+A_suffix+B_prefix"
        return "q+A/B_mixed"

    if has_only(toks, {"B", "z", "q", "A", "Y"}):
        if "B" in bs and "z" in bs and "q" in bs and "A" in bs:
            return "B_tail+zq+A"
        if "B" in bs and "A" in bs and "q" in bs:
            return "B_tail+A+q"
        if "B" in bs and "A" in bs and "Y" in bs:
            return "B_tail+A+Y"
        if "B" in bs and "q" in bs and "Y" in bs:
            return "B_tail+q+Y"
        if "B" in bs and "z" in bs and "Y" in bs:
            return "B_tail+z+Y"
        if "A" in bs and "z" in bs and "Y" in bs:
            return "A+z+Y"
        return "B_A_z_q_Y_mixed"

    return "other"


def first_candidate(record: dict[str, Any]) -> dict[str, Any]:
    cas = record.get("candidate_analyses", [])
    if not cas:
        return {}
    return cas[0].get("candidate", {}) or {}


def symbolic_labels(record: dict[str, Any], cand: dict[str, Any]) -> dict[int, list[str]]:
    order = [int(x) for x in record.get("order", [])]
    z_i = int(cand.get("z_i", 0))
    ext = int(cand.get("external_index", len(order)))
    A = [int(x) for x in cand.get("A", [])]
    B = [int(x) for x in cand.get("B", [])]
    z = int(cand.get("z"))
    q = int(cand.get("q"))
    out: dict[int, list[str]] = defaultdict(list)
    for idx, value in enumerate(order[:z_i]):
        out[int(value)].append(f"X{idx+1}")
    for idx, value in enumerate(A):
        out[int(value)].append(f"A{idx+1}")
    out[z].append("z")
    out[q].append("q")
    for idx, value in enumerate(B):
        out[int(value)].append(f"B{idx+1}")
    for idx, value in enumerate(order[ext:]):
        out[int(value)].append(f"Y{idx+1}")
    return out


def symbolic_block(block: list[int], labels: dict[int, list[str]]) -> str:
    return " ".join("/".join(labels.get(int(v), [f"?{v}"])) for v in block)


def is_tautological(sym: str) -> bool:
    toks = sym.split()
    if set(toks) == {"A1", "A2", "z"} and len(toks) == 3:
        return True
    if "z" in toks and all(t == "z" or t.startswith("B") for t in toks):
        return True
    return False


def record_perm_families(record: dict[str, Any]) -> dict[str, set[str]]:
    out: dict[str, set[str]] = defaultdict(set)
    for ca in record.get("candidate_analyses", []):
        cand = ca.get("candidate", {})
        labels = symbolic_labels(record, cand)
        for ma in ca.get("moves_analyzed", []):
            pk = ma.get("perm_key")
            if pk not in STABLE_PERMS:
                continue
            for zint in ma.get("new_zero_intervals", []) or []:
                sym = symbolic_block(zint.get("block", []), labels)
                if is_tautological(sym):
                    continue
                out[pk].add(classify_symbolic_block(sym))
    return dict(out)


def compact_example(record: dict[str, Any], perm: str, family: str) -> dict[str, Any] | None:
    for ca in record.get("candidate_analyses", []):
        cand = ca.get("candidate", {})
        labels = symbolic_labels(record, cand)
        for ma in ca.get("moves_analyzed", []):
            if ma.get("perm_key") != perm:
                continue
            for zint in ma.get("new_zero_intervals", []) or []:
                sym = symbolic_block(zint.get("block", []), labels)
                if is_tautological(sym):
                    continue
                if classify_symbolic_block(sym) == family:
                    return {
                        "record_index": record.get("record_index"),
                        "p": record.get("p"),
                        "perm": perm,
                        "family": family,
                        "symbolic_block": sym,
                        "numeric_block": zint.get("block"),
                        "candidate": {
                            "support_length": cand.get("support_length"),
                            "A": cand.get("A"),
                            "z": cand.get("z"),
                            "q": cand.get("q"),
                            "B": cand.get("B"),
                        },
                    }
    return None


def summarize(records: list[dict[str, Any]], example_limit: int) -> dict[str, Any]:
    worse = [r for r in records if r.get("pure_label") == "pure_worse_only"]
    total = len(worse)
    family_record_counts: dict[str, Counter[str]] = {perm: Counter() for perm in STABLE_PERMS}
    support_by_universal_candidate: dict[str, Counter[str]] = defaultdict(Counter)
    examples: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for record in worse:
        support = str(first_candidate(record).get("support_length"))
        pf = record_perm_families(record)
        for perm in STABLE_PERMS:
            fams = pf.get(perm, set())
            for fam in fams:
                family_record_counts[perm][fam] += 1
                support_by_universal_candidate[f"{perm}::{fam}"][support] += 1
                key = f"{perm}::{fam}"
                if len(examples[key]) < example_limit:
                    ex = compact_example(record, perm, fam)
                    if ex is not None:
                        examples[key].append(ex)

    coverage = {}
    universal = {}
    for perm, counter in family_record_counts.items():
        coverage[perm] = {
            fam: {
                "records_with_family": count,
                "records_total": total,
                "coverage": count / total if total else 0.0,
                "universal": count == total,
            }
            for fam, count in counter.most_common()
        }
        universal[perm] = sorted([fam for fam, count in counter.items() if count == total])

    proof_candidates = []
    for perm, fams in universal.items():
        for fam in fams:
            proof_candidates.append({
                "perm": perm,
                "family": fam,
                "support_histogram": dict(support_by_universal_candidate[f"{perm}::{fam}"].most_common()),
                "examples": examples.get(f"{perm}::{fam}", []),
            })

    return {
        "pure_worse_records": total,
        "stable_perms": list(STABLE_PERMS),
        "coverage_by_perm_family": coverage,
        "universal_families_by_perm": universal,
        "proof_candidates": proof_candidates,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input analyzed pure m3 structure JSONL files.")
    ap.add_argument("--out", default="-", help="Output JSON path, or '-' for stdout.")
    ap.add_argument("--pretty", action="store_true")
    ap.add_argument("--example-limit", type=int, default=3)
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
