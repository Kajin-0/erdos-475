#!/usr/bin/env python3
"""
Collapse pure-worse symbolic zero blocks into coarse algebraic families.

Input is produced by:

    scripts/summarize_pure_worse_symbolic_blocks.py

Typical inputs:

    logs/summary_pure_worse_symbolic_blocks_p17.json
    logs/summary_pure_worse_symbolic_blocks_p23.json

The raw symbolic output is too detailed for proof work.  This script maps blocks
such as:

    A1 A2 B1 B2 B3
    A2 B1
    B4 q
    z Y1

into families such as:

    A_all+B_prefix
    A_suffix+B_prefix
    B_tail+q
    z+Y_prefix

and reports compact histograms by permutation.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

STABLE_PERMS = {"A B q z", "B A q z", "B z q A", "z q A B", "z q B A"}
TOKEN_RE = re.compile(r"^([A-Z]+|z|q)(\d+)?$")


def load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


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
    # We do not know support length here, so any non-prefix increasing B indices are treated as tail-like.
    return bool(idxs) and not is_prefix(idxs)


def has_only(tokens: list[str], allowed: set[str]) -> bool:
    return set(bases(tokens)).issubset(allowed)


def classify_symbolic_block(sym: str) -> str:
    toks = sym.split()
    bs = bases(toks)
    sbs = set(bs)
    a_idxs = indices_of(toks, "A")
    b_idxs = indices_of(toks, "B")
    has_A1A2 = a_idxs == [1, 2] or sorted(a_idxs) == [1, 2]
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


def expand_counts(block_counts: dict[str, int]) -> Counter[str]:
    fam = Counter()
    for sym, count in block_counts.items():
        fam[classify_symbolic_block(sym)] += int(count)
    return fam


def summarize_file(path: Path, data: dict[str, Any]) -> dict[str, Any]:
    raw_by_perm: dict[str, dict[str, int]] = data.get("stable_perm_symbolic_blocks", {})
    shortest_by_perm: dict[str, dict[str, int]] = data.get("shortest_symbolic_blocks_by_perm", {})

    family_by_perm = {perm: dict(expand_counts(counts).most_common()) for perm, counts in raw_by_perm.items()}
    shortest_family_by_perm = {perm: dict(expand_counts(counts).most_common()) for perm, counts in shortest_by_perm.items() if perm in STABLE_PERMS}

    aggregate = Counter()
    for counts in raw_by_perm.values():
        aggregate.update(expand_counts(counts))

    return {
        "file": path.name,
        "pure_worse_records": data.get("pure_worse_records"),
        "A_q_z_B_collision_class_counts": data.get("A_q_z_B_collision_class_counts"),
        "aggregate_stable_family_histogram": dict(aggregate.most_common()),
        "family_by_stable_perm": family_by_perm,
        "shortest_family_by_stable_perm": shortest_family_by_perm,
    }


def common_families(summaries: list[dict[str, Any]]) -> dict[str, Any]:
    common_by_perm = {}
    for perm in sorted(STABLE_PERMS):
        sets = []
        for s in summaries:
            fams = set((s.get("family_by_stable_perm", {}).get(perm, {}) or {}).keys())
            sets.append(fams)
        common_by_perm[perm] = sorted(set.intersection(*sets)) if sets else []
    return common_by_perm


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("summary_json", nargs="+", help="Input summary_pure_worse_symbolic_blocks_*.json files.")
    ap.add_argument("--out", default="-", help="Output JSON path, or '-' for stdout.")
    ap.add_argument("--pretty", action="store_true")
    args = ap.parse_args()

    summaries = []
    for name in args.summary_json:
        path = Path(name)
        summaries.append(summarize_file(path, load(path)))

    out = {
        "files": summaries,
        "common_families_by_stable_perm": common_families(summaries),
    }

    text = json.dumps(out, indent=2 if args.pretty else None, sort_keys=True)
    if args.out == "-":
        print(text)
    else:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
