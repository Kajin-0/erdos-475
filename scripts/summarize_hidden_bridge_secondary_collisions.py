#!/usr/bin/env python3
"""
Summarize symbolic secondary collisions created by failed hidden-support bridge moves.

Inputs:

    --analysis   logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
    --equations  logs/bzqa_hidden_support_equations_p17_v3.jsonl
    --bridge     logs/hidden_support_bridge_moves_p17_v5.jsonl

and similarly for p=23.

The bridge-move summaries show that equality branches are neutral, while zero-sum
branches are worse.  This script inspects the best failed bridge moves and labels
the zero intervals they create symbolically.

Output is intended to identify the secondary obstruction that prevents the
hidden-support zero-sum relation from becoming a descent move.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Sequence, Tuple

TOKEN_RE = re.compile(r"^([A-Z]+|z|q)(\d+)?$")
CLASS_RANK = {"improved": 0, "neutral": 1, "worse": 2, "none": 9}


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


def partial_sums_extended(p: int, order: Sequence[int]) -> list[int]:
    s = 0
    out = [0]
    for x in order:
        s = (s + int(x)) % p
        out.append(s)
    return out


def zero_intervals(p: int, order: Sequence[int]) -> list[Tuple[int, int, int]]:
    P = partial_sums_extended(p, order)
    out: list[Tuple[int, int, int]] = []
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            if P[i] == P[j]:
                out.append((i, j, j - i))
    return out


def parse_token(tok: str) -> tuple[str, int | None]:
    m = TOKEN_RE.match(tok)
    if not m:
        return (tok, None)
    base, idx = m.group(1), m.group(2)
    return (base, int(idx) if idx is not None else None)


def bases(sym: str) -> list[str]:
    return [parse_token(t)[0] for t in sym.split()]


def b_indices(sym: str) -> list[int]:
    return [idx for base, idx in (parse_token(t) for t in sym.split()) if base == "B" and idx is not None]


def load_index(paths: list[str], key_fields: tuple[str, str] = ("p", "record_index")) -> dict[tuple[int, int], dict[str, Any]]:
    out = {}
    for name in paths:
        for rec in iter_jsonl(Path(name)):
            if key_fields[0] in rec and key_fields[1] in rec:
                out[(int(rec[key_fields[0]]), int(rec[key_fields[1]]))] = rec
    return out


def symbolic_labels(record: dict[str, Any], eq: dict[str, Any]) -> dict[int, list[str]]:
    order = [int(x) for x in record.get("order", [])]
    A = [int(x) for x in eq.get("A", [])]
    B = [int(x) for x in eq.get("B", [])]
    z = int(eq.get("z"))
    q = int(eq.get("q"))
    pattern = A + [z, q] + B
    start = find_subsequence(order, pattern)
    if start is None:
        start = 0
    end = start + len(pattern)
    out: dict[int, list[str]] = defaultdict(list)
    for idx, value in enumerate(order[:start]):
        out[int(value)].append(f"X{idx+1}")
    for idx, value in enumerate(A):
        out[int(value)].append(f"A{idx+1}")
    out[z].append("z")
    out[q].append("q")
    for idx, value in enumerate(B):
        out[int(value)].append(f"B{idx+1}")
    for idx, value in enumerate(order[end:]):
        out[int(value)].append(f"Y{idx+1}")
    return out


def find_subsequence(xs: Sequence[int], pat: Sequence[int]) -> int | None:
    n = len(xs)
    m = len(pat)
    for i in range(0, n - m + 1):
        if list(xs[i:i + m]) == list(pat):
            return i
    return None


def symbolic_block(block: Sequence[int], labels: dict[int, list[str]]) -> str:
    return " ".join("/".join(labels.get(int(v), [f"?{v}"])) for v in block)


def interval_symbolic(new_order: Sequence[int], zint: Sequence[int], labels: dict[int, list[str]]) -> str:
    i, j, _length = map(int, zint)
    return symbolic_block(new_order[i:j], labels)


def best_moves(row: dict[str, Any]) -> list[dict[str, Any]]:
    moves = row.get("results", []) or []
    if not moves:
        return []
    best = min(CLASS_RANK.get(m.get("class", "none"), 99) for m in moves)
    return [m for m in moves if CLASS_RANK.get(m.get("class", "none"), 99) == best]


def classify_symbolic_zero(sym: str, eq: dict[str, Any]) -> str:
    toks = sym.split()
    bs = set(bases(sym))
    bidx = b_indices(sym)
    support_len = int(eq.get("support_length") or len(eq.get("B", [])))

    if set(toks) == {"A1", "A2", "z"} and len(toks) == 3:
        return "old_Az"
    if "z" in toks and all(t == "z" or t.startswith("B") for t in toks):
        return "terminal_zB"
    if sym == str(eq.get("reduced_equation", "")):
        return "hidden_reduced_exact"
    if bs.issubset({"B", "q"}) and "B" in bs and "q" in bs:
        return "Bq_zero"
    if bs.issubset({"B", "q", "Y"}) and "B" in bs and "q" in bs and "Y" in bs:
        return "BqY_zero"
    if bs.issubset({"A", "B"}) and "A" in bs and "B" in bs:
        return "AB_zero"
    if bs.issubset({"A", "B", "q"}) and "A" in bs and "B" in bs and "q" in bs:
        return "ABq_zero"
    if "Y" in bs and "z" in bs:
        return "right_exterior_zY"
    if "Y" in bs and "q" in bs:
        return "right_exterior_qY"
    if "X" in bs:
        return "left_exterior_X"
    if bidx and min(bidx) > 1 and max(bidx) == support_len:
        return "B_tail_only_or_mixed"
    if bidx and min(bidx) == 1:
        return "B_prefix_or_mixed"
    return "other"


def summarize_records(analysis: dict[tuple[int, int], dict[str, Any]], equations: dict[tuple[int, int], dict[str, Any]], bridge_rows: list[dict[str, Any]], example_limit: int) -> dict[str, Any]:
    records_by_family = Counter()
    best_class_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    secondary_class_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    secondary_symbol_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    shortest_secondary_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    move_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    examples: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for row in bridge_rows:
        fam = row.get("reduced_family", "unknown")
        records_by_family[fam] += 1
        key = (int(row.get("p")), int(row.get("record_index")))
        rec = analysis.get(key)
        eq = equations.get(key)
        if rec is None or eq is None:
            continue
        labels = symbolic_labels(rec, eq)
        for move in best_moves(row):
            best_class_by_family[fam][move.get("class", "none")] += 1
            move_by_family[fam][move.get("move", "unknown")] += 1
            new_order = [int(x) for x in move.get("new_order", [])]
            if not new_order:
                continue
            p = int(row.get("p"))
            zints = zero_intervals(p, new_order)
            syms = []
            for zint in zints:
                sym = interval_symbolic(new_order, zint, labels)
                cls = classify_symbolic_zero(sym, eq)
                syms.append((zint[2], cls, sym, zint))
            syms.sort(key=lambda x: (x[0], x[1], x[2]))
            if syms:
                shortest_secondary_by_family[fam][str(syms[0][0])] += 1
            # Record all shortest zero intervals.  These are usually the obstruction driver.
            if syms:
                min_len = syms[0][0]
                for length, cls, sym, zint in syms:
                    if length != min_len:
                        continue
                    secondary_class_by_family[fam][cls] += 1
                    secondary_symbol_by_family[fam][sym] += 1
                    if len(examples[fam]) < example_limit:
                        examples[fam].append(
                            {
                                "p": row.get("p"),
                                "record_index": row.get("record_index"),
                                "reduced_family": fam,
                                "reduced_equation": eq.get("reduced_equation"),
                                "move": move.get("move"),
                                "move_class": move.get("class"),
                                "new_defect": move.get("new_defect"),
                                "shortest_zero_length": length,
                                "secondary_class": cls,
                                "secondary_symbol": sym,
                                "secondary_interval": list(zint),
                            }
                        )

    return {
        "records": len(bridge_rows),
        "records_by_family": dict(records_by_family.most_common()),
        "best_class_by_family": {k: dict(v.most_common()) for k, v in best_class_by_family.items()},
        "best_move_by_family": {k: dict(v.most_common()) for k, v in move_by_family.items()},
        "shortest_zero_length_by_family": {k: dict(v.most_common()) for k, v in shortest_secondary_by_family.items()},
        "secondary_class_by_family": {k: dict(v.most_common(30)) for k, v in secondary_class_by_family.items()},
        "secondary_symbol_by_family": {k: dict(v.most_common(30)) for k, v in secondary_symbol_by_family.items()},
        "examples_by_family": dict(examples),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--analysis", nargs="+", required=True, help="Analyzed pure m3 structure JSONL files.")
    ap.add_argument("--equations", nargs="+", required=True, help="Hidden-support equation JSONL files.")
    ap.add_argument("--bridge", nargs="+", required=True, help="Hidden-support bridge move JSONL files.")
    ap.add_argument("--out", default="-", help="Output JSON path, or '-' for stdout.")
    ap.add_argument("--pretty", action="store_true")
    ap.add_argument("--example-limit", type=int, default=3)
    args = ap.parse_args()

    analysis = load_index(args.analysis)
    equations = load_index(args.equations)
    bridge_rows = []
    for name in args.bridge:
        bridge_rows.extend(list(iter_jsonl(Path(name))))

    summary = summarize_records(analysis, equations, bridge_rows, args.example_limit)
    summary["input_counts"] = {
        "analysis": len(analysis),
        "equations": len(equations),
        "bridge_rows": len(bridge_rows),
    }
    text = json.dumps(summary, indent=2 if args.pretty else None, sort_keys=True)
    if args.out == "-":
        print(text)
    else:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
