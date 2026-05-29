#!/usr/bin/env python3
"""
Diagnose the rare left_external_X endpoint-taxonomy cases under B z q A.

Input is produced by:

    scripts/analyze_pure_m3_terminal_structure.py

Typical use:

    python3 scripts/diagnose_bzqa_left_external_cases.py \
      logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl \
      --out logs/bzqa_left_external_cases_p23.jsonl \
      --summary-out logs/summary_bzqa_left_external_cases_p23.json
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

TOKEN_RE = re.compile(r"^([A-Z]+|z|q)(\d+)?$")
TARGET_PERM = "B z q A"
TARGET_CLASSES = {"hidden_full_A_tail_core", "hidden_partial_A_tail_core", "hidden_prefix_core"}


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


def classify(tokens: list[str], support_length: int | None = None) -> str:
    bases = set(token_bases(tokens))
    Aidx = a_indices(tokens)
    Bidx = b_indices(tokens)
    if set(tokens) == {"A1", "A2", "z"} and len(tokens) == 3:
        return "tautology_old_Az"
    if "z" in tokens and all(t == "z" or t.startswith("B") for t in tokens):
        return "tautology_terminal_zB"
    if {"B", "z", "q", "A"}.issubset(bases) and Aidx == {1, 2}:
        return "hidden_full_A_tail_core"
    if {"B", "z", "q", "A"}.issubset(bases) and Aidx in ({1}, {2}):
        return "hidden_partial_A_tail_core"
    if bases.issubset({"B", "z", "q"}) and {"B", "z", "q"}.issubset(bases):
        return "hidden_prefix_core"
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
    return "other"


def record_blocks(record: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
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
                out.append({
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
                })
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input analyzed pure m3 structure JSONL files.")
    ap.add_argument("--out", default="-")
    ap.add_argument("--summary-out", default=None)
    args = ap.parse_args()

    rows = []
    total_pure = 0
    for name in args.jsonl:
        for rec in iter_jsonl(Path(name)):
            if rec.get("pure_label") != "pure_worse_only":
                continue
            total_pure += 1
            blocks = record_blocks(rec)
            left_blocks = [b for b in blocks if b["class"] == "left_external_X"]
            if not left_blocks:
                continue
            target_blocks = [b for b in blocks if b["class"] in TARGET_CLASSES]
            rows.append({
                "p": rec.get("p"),
                "record_index": rec.get("record_index"),
                "order": rec.get("order"),
                "left_external_blocks": left_blocks,
                "target_blocks": target_blocks,
                "all_class_counts": dict(Counter(b["class"] for b in blocks).most_common()),
            })

    if args.out == "-":
        for r in rows:
            print(json.dumps(r, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, separators=(",", ":")) + "\n")

    summary = {
        "pure_records_seen": total_pure,
        "records_with_left_external_X": len(rows),
        "record_indices": [r["record_index"] for r in rows],
        "target_presence_in_left_external_records": dict(Counter("yes" if r["target_blocks"] else "no" for r in rows).most_common()),
        "left_external_class_counts": dict(Counter(b["class"] for r in rows for b in r["left_external_blocks"]).most_common()),
        "target_class_counts_in_left_external_records": dict(Counter(b["class"] for r in rows for b in r["target_blocks"]).most_common()),
    }
    print("summary=" + json.dumps(summary, sort_keys=True))
    if args.summary_out:
        Path(args.summary_out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
