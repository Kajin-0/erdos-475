#!/usr/bin/env python3
"""
Summarize endpoint taxonomy for non-tautological zero intervals under B z q A.

Input is produced by:

    scripts/analyze_pure_m3_terminal_structure.py

Typical use:

    python3 scripts/summarize_bzqa_endpoint_taxonomy.py \
      logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl \
      --pretty \
      --out logs/summary_bzqa_endpoint_taxonomy_p17.json

The goal is to support the formal endpoint-exclusion lemma for the hidden-support
extraction step.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

TARGET_PERM = "B z q A"
TOKEN_RE = re.compile(r"^([A-Z]+|z|q)(\d+)?$")

TARGET_CLASSES = {
    "hidden_full_A_tail_core",
    "hidden_partial_A_tail_core",
    "hidden_prefix_core",
}


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


def token_bases(tokens: list[str]) -> list[str]:
    return [parse_token(t)[0] for t in tokens]


def a_indices(tokens: list[str]) -> set[int]:
    return {idx for base, idx in (parse_token(t) for t in tokens) if base == "A" and idx is not None}


def b_indices(tokens: list[str]) -> list[int]:
    return [idx for base, idx in (parse_token(t) for t in tokens) if base == "B" and idx is not None]


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


def is_old_Az(tokens: list[str]) -> bool:
    return set(tokens) == {"A1", "A2", "z"} and len(tokens) == 3


def is_terminal_zB(tokens: list[str]) -> bool:
    return "z" in tokens and all(t == "z" or t.startswith("B") for t in tokens)


def classify(tokens: list[str], support_length: int | None = None) -> str:
    bases = set(token_bases(tokens))
    Aidx = a_indices(tokens)
    Bidx = b_indices(tokens)

    if is_old_Az(tokens):
        return "tautology_old_Az"
    if is_terminal_zB(tokens):
        return "tautology_terminal_zB"

    if {"B", "z", "q", "A"}.issubset(bases) and Aidx == {1, 2}:
        return "hidden_full_A_tail_core"
    if {"B", "z", "q", "A"}.issubset(bases) and Aidx in ({1}, {2}):
        return "hidden_partial_A_tail_core"
    if bases.issubset({"B", "z", "q"}) and {"B", "z", "q"}.issubset(bases):
        return "hidden_prefix_core"

    if "X" in bases and "Y" in bases:
        return "mixed_XY_external"
    if "X" in bases:
        return "left_external_X"
    if "Y" in bases and "q" in bases and "B" in bases:
        return "right_external_BqY"
    if "Y" in bases and "z" in bases:
        return "right_external_zY"
    if "Y" in bases:
        return "right_external_Y"
    if bases.issubset({"B", "q"}) and "B" in bases and "q" in bases:
        return "support_Bq"
    if bases.issubset({"A", "B"}) and "A" in bases and "B" in bases:
        return "support_AB"
    if bases.issubset({"A", "B", "q"}) and "A" in bases and "B" in bases:
        return "support_ABq"
    if bases.issubset({"A", "q"}) and "A" in bases and "q" in bases:
        return "support_Aq"
    if bases.issubset({"B"}) and Bidx:
        if support_length is not None and max(Bidx) == support_length and min(Bidx) > 1:
            return "B_tail_only"
        if min(Bidx) == 1:
            return "B_prefix_only"
        return "B_internal_only"
    return "other"


def iter_bzqa_blocks(record: dict[str, Any]) -> Iterable[dict[str, Any]]:
    if record.get("pure_label") != "pure_worse_only":
        return
    for ca in record.get("candidate_analyses", []):
        cand = ca.get("candidate", {})
        labels = symbolic_labels(record, cand)
        support_len = cand.get("support_length")
        for ma in ca.get("moves_analyzed", []):
            if ma.get("perm_key") != TARGET_PERM:
                continue
            for zint in ma.get("new_zero_intervals", []) or []:
                sym = symbolic_block(zint.get("block", []), labels)
                toks = sym.split()
                cls = classify(toks, support_len)
                yield {
                    "record_index": record.get("record_index"),
                    "p": record.get("p"),
                    "class": cls,
                    "symbolic_block": sym,
                    "numeric_block": zint.get("block"),
                    "length": zint.get("length"),
                    "signature": f"{zint.get('left_label') or 'ext'}={zint.get('right_label') or 'ext'}:L{zint.get('length')}:{zint.get('span_type')}",
                    "candidate": {
                        "support_length": support_len,
                        "A": cand.get("A"),
                        "z": cand.get("z"),
                        "q": cand.get("q"),
                        "B": cand.get("B"),
                        "X_length": cand.get("X_length"),
                        "Y_length": cand.get("Y_length"),
                    },
                }


def summarize(records: list[dict[str, Any]], example_limit: int) -> dict[str, Any]:
    blocks = []
    rec_target_classes: dict[tuple[int, int], set[str]] = defaultdict(set)
    rec_all_classes: dict[tuple[int, int], set[str]] = defaultdict(set)
    examples: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for rec in records:
        key = (int(rec.get("p")), int(rec.get("record_index")))
        any_block = False
        for block in iter_bzqa_blocks(rec):
            any_block = True
            blocks.append(block)
            cls = block["class"]
            rec_all_classes[key].add(cls)
            if cls in TARGET_CLASSES:
                rec_target_classes[key].add(cls)
            if len(examples[cls]) < example_limit:
                examples[cls].append(block)
        if not any_block:
            rec_all_classes[key].add("NO_BZQA_BLOCKS")

    target_presence = Counter("yes" if rec_target_classes.get(k) else "no" for k in rec_all_classes)
    non_target_presence = Counter("yes" if (rec_all_classes[k] - TARGET_CLASSES) else "no" for k in rec_all_classes)
    target_combo = Counter("|".join(sorted(rec_target_classes.get(k, []))) or "none" for k in rec_all_classes)
    non_target_combo = Counter("|".join(sorted(rec_all_classes[k] - TARGET_CLASSES)) or "none" for k in rec_all_classes)

    return {
        "records": len(records),
        "blocks": len(blocks),
        "block_class_histogram": dict(Counter(b["class"] for b in blocks).most_common()),
        "target_presence": dict(target_presence.most_common()),
        "non_target_presence": dict(non_target_presence.most_common()),
        "target_combo_histogram": dict(target_combo.most_common()),
        "non_target_combo_histogram": dict(non_target_combo.most_common(50)),
        "examples_by_class": dict(examples),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input analyzed pure m3 structure JSONL files.")
    ap.add_argument("--out", default="-", help="Output JSON path, or '-' for stdout.")
    ap.add_argument("--pretty", action="store_true")
    ap.add_argument("--example-limit", type=int, default=3)
    args = ap.parse_args()

    records = []
    for name in args.jsonl:
        records.extend([r for r in iter_jsonl(Path(name)) if r.get("pure_label") == "pure_worse_only"])

    summary = summarize(records, args.example_limit)
    text = json.dumps(summary, indent=2 if args.pretty else None, sort_keys=True)
    if args.out == "-":
        print(text)
    else:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
