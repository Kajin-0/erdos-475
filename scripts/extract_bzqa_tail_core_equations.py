#!/usr/bin/env python3
"""
Extract the universal B z q A hidden-support equation from pure_worse_only m=3 residuals.

Input is produced by:

    scripts/analyze_pure_m3_terminal_structure.py

Typical inputs:

    logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
    logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl

For each pure_worse_only record, this script searches the permutation:

    B z q A

for one of three proof-relevant hidden support equations.

Full-A tail-core case:

    B_tail + z + q + A1 + A2 + optional Y_prefix = 0

Since A1+A2+z=0, this reduces to:

    B_tail + q + optional Y_prefix = 0.

Partial-A tail-core case:

    B_tail + z + q + A_i + optional Y_prefix = 0.

Since A1+A2+z=0, this reduces to:

    B_tail + q + optional Y_prefix = A_j,

where {i,j}={1,2}.

Prefix-core case:

    B_tail + z + q = 0.

Since B_prefix+B_tail+z=0, subtracting gives:

    B_prefix = q.

The unified output is therefore one of:

    B_tail+q
    B_tail+q+Y_prefix
    B_tail+q(+Y_prefix)=A_complement
    B_prefix=q
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


def a_indices(tokens: list[str]) -> set[int]:
    return {idx for base, idx in (parse_token(t) for t in tokens) if base == "A" and idx is not None}


def is_tautological(tokens: list[str]) -> bool:
    if set(tokens) == {"A1", "A2", "z"} and len(tokens) == 3:
        return True
    if "z" in tokens and all(t == "z" or t.startswith("B") for t in tokens):
        return True
    return False


def has_full_A_tail_core(tokens: list[str]) -> bool:
    bases = set(token_bases(tokens))
    return {"B", "z", "q", "A"}.issubset(bases) and a_indices(tokens) == {1, 2} and not is_tautological(tokens)


def has_partial_A_tail_core(tokens: list[str]) -> bool:
    bases = set(token_bases(tokens))
    return {"B", "z", "q", "A"}.issubset(bases) and a_indices(tokens) in ({1}, {2}) and not is_tautological(tokens)


def has_prefix_core(tokens: list[str]) -> bool:
    """Detect B_tail+z+q=0, which implies B_prefix=q by terminal subtraction."""
    bases = set(token_bases(tokens))
    return bases.issubset({"B", "z", "q"}) and {"B", "z", "q"}.issubset(bases) and not is_tautological(tokens)


def reduced_full_A_tail_tokens(tokens: list[str]) -> list[str]:
    """Remove one z and A1,A2, leaving B_tail+q(+Y_prefix)."""
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


def reduced_partial_A_equation_tokens(tokens: list[str]) -> list[str]:
    """Convert B_tail+z+q+A_i(+Y)=0 into B_tail+q(+Y)=A_j."""
    present = a_indices(tokens)
    if present == {1}:
        complement = "A2"
    elif present == {2}:
        complement = "A1"
    else:
        complement = "A?"
    out = []
    removed_z = False
    for t in tokens:
        if t in {"A1", "A2"}:
            continue
        if t == "z" and not removed_z:
            removed_z = True
            continue
        out.append(t)
    out += ["=", complement]
    return out


def b_indices(tokens: list[str]) -> list[int]:
    return [idx for base, idx in (parse_token(t) for t in tokens) if base == "B" and idx is not None]


def y_prefix_len(tokens: list[str]) -> int:
    yidx = [idx for base, idx in (parse_token(t) for t in tokens) if base == "Y" and idx is not None]
    return max(yidx) if yidx else 0


def reduced_family_from_full_A_tail(tokens: list[str]) -> str:
    rt = reduced_full_A_tail_tokens(tokens)
    bases = set(token_bases([t for t in rt if t != "="]))
    if bases.issubset({"B", "q"}) and "B" in bases and "q" in bases:
        return "B_tail+q"
    if bases.issubset({"B", "q", "Y"}) and "B" in bases and "q" in bases and "Y" in bases:
        return "B_tail+q+Y_prefix"
    if "X" in bases:
        return "mixed_X_or_left_exterior"
    return "other_reduced"


def reduced_family_from_partial_A_tail(tokens: list[str]) -> str:
    rt = reduced_partial_A_equation_tokens(tokens)
    bases = set(token_bases([t for t in rt if t != "="]))
    if "Y" in bases:
        return "B_tail+q+Y_prefix=A_complement"
    return "B_tail+q=A_complement"


def prefix_equation_tokens(tokens: list[str], support_length: int) -> list[str]:
    tail = b_indices(tokens)
    if not tail:
        return ["q"]
    start = min(tail)
    # B_tail begins at start, so B_prefix is B1...(B_{start-1}).
    return [f"B{i}" for i in range(1, start)] + ["=", "q"]


def make_row(record: dict[str, Any], cand: dict[str, Any], ma: dict[str, Any], zint: dict[str, Any], sym: str, tokens: list[str], kind: str) -> dict[str, Any]:
    support_length = int(cand.get("support_length"))
    if kind == "tail_core":
        red = reduced_full_A_tail_tokens(tokens)
        bidx = b_indices(red)
        reduced_equation = " ".join(red)
        reduced_family = reduced_family_from_full_A_tail(tokens)
        b_tail_start = min(bidx) if bidx else None
        b_tail_end = max(bidx) if bidx else None
        b_tail_len = len(bidx)
        b_prefix_len = (b_tail_start - 1) if b_tail_start is not None else None
        y_len = y_prefix_len(red)
    elif kind == "partial_A_tail_core":
        red = reduced_partial_A_equation_tokens(tokens)
        bidx = b_indices(red)
        reduced_equation = " ".join(red)
        reduced_family = reduced_family_from_partial_A_tail(tokens)
        b_tail_start = min(bidx) if bidx else None
        b_tail_end = max(bidx) if bidx else None
        b_tail_len = len(bidx)
        b_prefix_len = (b_tail_start - 1) if b_tail_start is not None else None
        y_len = y_prefix_len(red)
    elif kind == "prefix_core":
        bidx0 = b_indices(tokens)
        b_tail_start = min(bidx0) if bidx0 else None
        b_tail_end = max(bidx0) if bidx0 else None
        b_tail_len = len(bidx0)
        b_prefix_len = (b_tail_start - 1) if b_tail_start is not None else None
        reduced_equation = " ".join(prefix_equation_tokens(tokens, support_length))
        reduced_family = "B_prefix=q"
        y_len = 0
    else:
        raise ValueError(kind)

    return {
        "record_index": record.get("record_index"),
        "p": record.get("p"),
        "perm": TARGET_PERM,
        "support_length": support_length,
        "A": cand.get("A"),
        "z": cand.get("z"),
        "q": cand.get("q"),
        "B": cand.get("B"),
        "extraction_kind": kind,
        "symbolic_equation": sym,
        "reduced_equation": reduced_equation,
        "reduced_family": reduced_family,
        "B_tail_start_index": b_tail_start,
        "B_tail_end_index": b_tail_end,
        "B_tail_length": b_tail_len,
        "B_prefix_length": b_prefix_len,
        "Y_prefix_length": y_len,
        "numeric_block": zint.get("block"),
        "signature": f"{zint.get('left_label') or 'ext'}={zint.get('right_label') or 'ext'}:L{zint.get('length')}:{zint.get('span_type')}",
        "new_defect": ma.get("new_defect"),
    }


def find_hidden_support_equation(record: dict[str, Any]) -> dict[str, Any] | None:
    if record.get("pure_label") != "pure_worse_only":
        return None
    for ca in record.get("candidate_analyses", []):
        cand = ca.get("candidate", {})
        labels = symbolic_labels(record, cand)
        for ma in ca.get("moves_analyzed", []):
            if ma.get("perm_key") != TARGET_PERM:
                continue
            full_tail_candidates = []
            partial_tail_candidates = []
            prefix_candidates = []
            for zint in ma.get("new_zero_intervals", []) or []:
                sym = symbolic_block(zint.get("block", []), labels)
                tokens = sym.split()
                if has_full_A_tail_core(tokens):
                    red = reduced_full_A_tail_tokens(tokens)
                    bidx = b_indices(red)
                    full_tail_candidates.append((len(tokens), y_prefix_len(red), len(bidx), sym, tokens, zint, cand, ma))
                elif has_partial_A_tail_core(tokens):
                    red = reduced_partial_A_equation_tokens(tokens)
                    bidx = b_indices(red)
                    partial_tail_candidates.append((len(tokens), y_prefix_len(red), len(bidx), sym, tokens, zint, cand, ma))
                elif has_prefix_core(tokens):
                    bidx0 = b_indices(tokens)
                    prefix_candidates.append((len(tokens), len(bidx0), sym, tokens, zint, cand, ma))
            if full_tail_candidates:
                full_tail_candidates.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
                _length, _ylen, _blen, sym, tokens, zint, cand, ma = full_tail_candidates[0]
                return make_row(record, cand, ma, zint, sym, tokens, "tail_core")
            if partial_tail_candidates:
                partial_tail_candidates.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
                _length, _ylen, _blen, sym, tokens, zint, cand, ma = partial_tail_candidates[0]
                return make_row(record, cand, ma, zint, sym, tokens, "partial_A_tail_core")
            if prefix_candidates:
                prefix_candidates.sort(key=lambda x: (x[0], x[1], x[2]))
                _length, _blen, sym, tokens, zint, cand, ma = prefix_candidates[0]
                return make_row(record, cand, ma, zint, sym, tokens, "prefix_core")
    return None


def summarize(rows: list[dict[str, Any]], input_records: int) -> dict[str, Any]:
    fam = Counter(row["reduced_family"] for row in rows)
    kind = Counter(row["extraction_kind"] for row in rows)
    support = Counter(str(row["support_length"]) for row in rows)
    tail_start = Counter(str(row["B_tail_start_index"]) for row in rows)
    tail_len = Counter(str(row["B_tail_length"]) for row in rows)
    prefix_len = Counter(str(row["B_prefix_length"]) for row in rows)
    y_len = Counter(str(row["Y_prefix_length"]) for row in rows)
    sig = Counter(row["signature"] for row in rows)
    return {
        "input_records": input_records,
        "extracted_records": len(rows),
        "extraction_kind_histogram": dict(kind.most_common()),
        "reduced_family_histogram": dict(fam.most_common()),
        "support_length_histogram": dict(support.most_common()),
        "B_tail_start_histogram": dict(tail_start.most_common()),
        "B_tail_length_histogram": dict(tail_len.most_common()),
        "B_prefix_length_histogram": dict(prefix_len.most_common()),
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
            row = find_hidden_support_equation(rec)
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
