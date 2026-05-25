#!/usr/bin/env python3
"""
Extract the universal B z q A tail-core equation from pure_worse_only m=3 residuals.

Input is produced by:

    scripts/analyze_pure_m3_terminal_structure.py

Typical inputs:

    logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
    logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl

For each pure_worse_only record, this script finds a non-tautological zero block
under the permutation:

    B z q A

whose symbolic form contains B-tail, z, q, and A.  Since z + A = 0 in the
m=3 residual, it also emits the reduced equation:

    B_tail + q + optional Y_prefix = 0

This is intended to turn the empirical family result into proof-ready algebraic data.
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


def token_bases(tokens: list[str]) -> list[str]:
    return [parse_token(t)[0] for t in tokens]


def is_tautological(tokens: list[str]) -> bool:
    if set(tokens) == {"A1", "A2", "z"} and len(tokens) == 3:
        return True
    if "z" in tokens and all(t == "z" or t.startswith("B") for t in tokens):
        return True
    return False


def is_tail_core(tokens: list[str]) -> bool:
    bases = set(token_bases(tokens))
    return {"B", "z", "q", "A"}.issubset(bases) and not is_tautological(tokens)


def reduced_tokens(tokens: list[str]) -> list[str]:
    """Remove one z and all A tokens, leaving the reduced tail equation.

    In this residual, A1+A2+z=0, so a zero block containing z+A1+A2 reduces by
    deleting z,A1,A2.  Preserve the original order of all other tokens.
    """
    removed_z = False
    out = []
    for t in tokens:
        if t in {"A1", "A2"}:
            continue
        if t == "z" and not removed_z:
            removed_z = True
            continue
        out.append(t)
    return out


def reduced_family(tokens: list[str]) -> str:
    rt = reduced_tokens(tokens)
    bases = set(token_bases(rt))
    if bases.issubset({"B", "q"}) and "B" in bases and "q" in bases:
        return "B_tail+q"
    if bases.issubset({"B", "q", "Y"}) and "B" in bases and "q" in bases and "Y" in bases:
        return "B_tail+q+Y_prefix"
    if "X" in bases:
        return "mixed_X_or_left_exterior"
    return "other_reduced"


def b_tail_indices(tokens: list[str]) -> list[int]:
    return [idx for base, idx in (parse_token(t) for t in tokens) if base == "B" and idx is not None]


def y_prefix_len(tokens: list[str]) -> int:
    yidx = [idx for base, idx in (parse_token(t) for t in tokens) if base == "Y" and idx is not None]
    return max(yidx) if yidx else 0


def find_tail_core(record: dict[str, Any]) -> dict[str, Any] | None:
    if record.get("pure_label") != "pure_worse_only":
        return None
    for ca in record.get("candidate_analyses", []):
        cand = ca.get("candidate", {})
        labels = symbolic_labels(record, cand)
        for ma in ca.get("moves_analyzed", []):
            if ma.get("perm_key") != TARGET_PERM:
                continue
            candidates = []
            for zint in ma.get("new_zero_intervals", []) or []:
                sym = symbolic_block(zint.get("block", []), labels)
                toks = sym.split()
                if not is_tail_core(toks):
                    continue
                red = reduced_tokens(toks)
                bidx = b_tail_indices(red)
                candidates.append((len(toks), y_prefix_len(red), len(bidx), sym, red, zint, cand, ma))
            if not candidates:
                continue
            # Prefer shortest symbolic equation, then no exterior, then shortest B tail.
            candidates.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
            _length, _ylen, _blen, sym, red, zint, cand, ma = candidates[0]
            bidx = b_tail_indices(red)
            return {
                "record_index": record.get("record_index"),
                "p": record.get("p"),
                "perm": TARGET_PERM,
                "support_length": cand.get("support_length"),
                "A": cand.get("A"),
                "z": cand.get("z"),
                "q": cand.get("q"),
                "B": cand.get("B"),
                "symbolic_equation": sym,
                "reduced_equation": " ".join(red),
                "reduced_family": reduced_family(toks),
                "B_tail_start_index": min(bidx) if bidx else None,
                "B_tail_end_index": max(bidx) if bidx else None,
                "B_tail_length": len(bidx),
                "Y_prefix_length": y_prefix_len(red),
                "numeric_block": zint.get("block"),
                "signature": f"{zint.get('left_label') or 'ext'}={zint.get('right_label') or 'ext'}:L{zint.get('length')}:{zint.get('span_type')}",
                "new_defect": ma.get("new_defect"),
            }
    return None


def summarize(rows: list[dict[str, Any]], input_records: int) -> dict[str, Any]:
    fam = Counter(row["reduced_family"] for row in rows)
    support = Counter(str(row["support_length"]) for row in rows)
    tail_start = Counter(str(row["B_tail_start_index"]) for row in rows)
    tail_len = Counter(str(row["B_tail_length"]) for row in rows)
    y_len = Counter(str(row["Y_prefix_length"]) for row in rows)
    sig = Counter(row["signature"] for row in rows)
    return {
        "input_records": input_records,
        "extracted_records": len(rows),
        "reduced_family_histogram": dict(fam.most_common()),
        "support_length_histogram": dict(support.most_common()),
        "B_tail_start_histogram": dict(tail_start.most_common()),
        "B_tail_length_histogram": dict(tail_len.most_common()),
        "Y_prefix_length_histogram": dict(y_len.most_common()),
        "signature_histogram": dict(sig.most_common(25)),
        "missing_records": input_records - len(rows),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input analyzed pure m3 structure JSONL files.")
    ap.add_argument("--out", default="-", help="Output JSONL path, or '-' for stdout.")
    ap.add_argument("--summary-out", default=None, help="Optional summary JSON path.")
    args = ap.parse_args()

    rows = []
    input_pure_worse = 0
    input_files = {}
    for name in args.jsonl:
        path = Path(name)
        loaded = list(iter_jsonl(path))
        input_files[str(path)] = len(loaded)
        for rec in loaded:
            if rec.get("pure_label") != "pure_worse_only":
                continue
            input_pure_worse += 1
            row = find_tail_core(rec)
            if row is not None:
                rows.append(row)

    if args.out == "-":
        for row in rows:
            print(json.dumps(row, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for row in rows:
                fh.write(json.dumps(row, separators=(",", ":")) + "\n")

    summary = summarize(rows, input_pure_worse)
    summary["input_files"] = input_files
    print("summary=" + json.dumps(summary, sort_keys=True))
    if args.summary_out:
        Path(args.summary_out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
