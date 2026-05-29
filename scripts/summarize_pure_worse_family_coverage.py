#!/usr/bin/env python3
"""
Record-level family and meta-family coverage for pure_worse_only m=3 terminal residuals.

Input is produced by:

    scripts/analyze_pure_m3_terminal_structure.py

Typical inputs:

    logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
    logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl

This script classifies each non-tautological symbolic zero block into coarse
families and broader meta-families, then reports record-level coverage by
permutation:

    permutation -> family/meta-family -> records hit / records total

The meta-family layer is needed because p=23 splits one algebraic mechanism
across multiple lower-level symbolic families.
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


def meta_families(family: str) -> set[str]:
    metas = {"ANY_NONTAUT"}
    if family in {"A_all+B_prefix", "A_suffix+B_prefix", "q+A_all+B_prefix", "q+A_suffix+B_prefix", "q+A/B_mixed"}:
        metas.add("PREFIX_WITH_A")
    if family in {"A_all+B_prefix", "A_suffix+B_prefix"}:
        metas.add("A_PLUS_B_PREFIX")
    if family in {"B_tail+zq+A", "B_A_z_q_Y_mixed", "B_tail+A+Y", "B_tail+A+q", "B_tail+A_prefix"}:
        metas.add("B_TAIL_WITH_A_CORE")
    if family in {"B_tail+zq+A", "B_A_z_q_Y_mixed"}:
        metas.add("B_TAIL_ZQ_A_CORE")
    if family in {"B_tail+q", "B_tail+q+Y", "qz+Y_prefix", "z+Y_prefix", "A+z+Y"}:
        metas.add("RIGHT_EXTERIOR_OR_Q_TAIL")
    if family in {"B_tail+q", "B_tail+q+Y"}:
        metas.add("B_TAIL_WITH_Q")
    if family == "mixed_X_prefix":
        metas.add("LEFT_EXTERIOR_X")
    return metas


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


def record_perm_families(record: dict[str, Any]) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    families: dict[str, set[str]] = defaultdict(set)
    metas: dict[str, set[str]] = defaultdict(set)
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
                fam = classify_symbolic_block(sym)
                families[pk].add(fam)
                metas[pk].update(meta_families(fam))
    return dict(families), dict(metas)


def compact_example(record: dict[str, Any], perm: str, label: str, *, meta: bool = False) -> dict[str, Any] | None:
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
                fam = classify_symbolic_block(sym)
                if (not meta and fam == label) or (meta and label in meta_families(fam)):
                    return {
                        "record_index": record.get("record_index"),
                        "p": record.get("p"),
                        "perm": perm,
                        "family": fam,
                        "meta_family": label if meta else None,
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
    family_counts: dict[str, Counter[str]] = {perm: Counter() for perm in STABLE_PERMS}
    meta_counts: dict[str, Counter[str]] = {perm: Counter() for perm in STABLE_PERMS}
    support_by_meta: dict[str, Counter[str]] = defaultdict(Counter)
    support_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    examples: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for record in worse:
        support = str(first_candidate(record).get("support_length"))
        pf, pm = record_perm_families(record)
        for perm in STABLE_PERMS:
            for fam in pf.get(perm, set()):
                family_counts[perm][fam] += 1
                support_by_family[f"{perm}::{fam}"][support] += 1
                key = f"family::{perm}::{fam}"
                if len(examples[key]) < example_limit:
                    ex = compact_example(record, perm, fam, meta=False)
                    if ex is not None:
                        examples[key].append(ex)
            for meta in pm.get(perm, set()):
                meta_counts[perm][meta] += 1
                support_by_meta[f"{perm}::{meta}"][support] += 1
                key = f"meta::{perm}::{meta}"
                if len(examples[key]) < example_limit:
                    ex = compact_example(record, perm, meta, meta=True)
                    if ex is not None:
                        examples[key].append(ex)

    def coverage_obj(counter: Counter[str]) -> dict[str, Any]:
        return {
            label: {
                "records_with_label": count,
                "records_total": total,
                "coverage": count / total if total else 0.0,
                "universal": count == total,
            }
            for label, count in counter.most_common()
        }

    family_coverage = {perm: coverage_obj(counter) for perm, counter in family_counts.items()}
    meta_coverage = {perm: coverage_obj(counter) for perm, counter in meta_counts.items()}
    universal_families = {perm: sorted([fam for fam, count in c.items() if count == total]) for perm, c in family_counts.items()}
    universal_metas = {perm: sorted([m for m, count in c.items() if count == total]) for perm, c in meta_counts.items()}

    proof_candidates = []
    for perm, metas in universal_metas.items():
        for meta in metas:
            proof_candidates.append({
                "perm": perm,
                "meta_family": meta,
                "support_histogram": dict(support_by_meta[f"{perm}::{meta}"].most_common()),
                "examples": examples.get(f"meta::{perm}::{meta}", []),
            })
    for perm, fams in universal_families.items():
        for fam in fams:
            proof_candidates.append({
                "perm": perm,
                "family": fam,
                "support_histogram": dict(support_by_family[f"{perm}::{fam}"].most_common()),
                "examples": examples.get(f"family::{perm}::{fam}", []),
            })

    return {
        "pure_worse_records": total,
        "stable_perms": list(STABLE_PERMS),
        "coverage_by_perm_family": family_coverage,
        "coverage_by_perm_meta_family": meta_coverage,
        "universal_families_by_perm": universal_families,
        "universal_meta_families_by_perm": universal_metas,
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
