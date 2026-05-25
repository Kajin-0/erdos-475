#!/usr/bin/env python3
"""
Diagnose records where a target genuine obstruction class is missing.

Inputs are the same as summarize_hidden_bridge_genuine_obstructions.py:

    --analysis   logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl
    --equations  logs/bzqa_hidden_support_equations_p23_v3.jsonl
    --bridge     logs/hidden_support_bridge_moves_p23_v5.jsonl

Example:

    python3 scripts/diagnose_genuine_obstruction_coverage_gaps.py \
      --analysis logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl \
      --equations logs/bzqa_hidden_support_equations_p23_v3.jsonl \
      --bridge logs/hidden_support_bridge_moves_p23_v5.jsonl \
      --target-family 'B_tail+q+Y_prefix' \
      --target-class BqY_zero \
      --out logs/gaps_Btail_q_Yprefix_missing_BqY_p23.jsonl \
      --summary-out logs/summary_gaps_Btail_q_Yprefix_missing_BqY_p23.json

This prints records in the target family whose best bridge moves have genuine
secondary obstructions, but none of the requested target class.
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
IGNORE_CLASSES = {"old_Az", "terminal_zB", "hidden_reduced_exact"}


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
    out = []
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


def find_subsequence(xs: Sequence[int], pat: Sequence[int]) -> int | None:
    n = len(xs)
    m = len(pat)
    for i in range(0, n - m + 1):
        if list(xs[i:i + m]) == list(pat):
            return i
    return None


def load_index(paths: list[str]) -> dict[tuple[int, int], dict[str, Any]]:
    out = {}
    for name in paths:
        for rec in iter_jsonl(Path(name)):
            if "p" in rec and "record_index" in rec:
                out[(int(rec["p"]), int(rec["record_index"]))] = rec
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


def symbolic_block(block: Sequence[int], labels: dict[int, list[str]]) -> str:
    return " ".join("/".join(labels.get(int(v), [f"?{v}"])) for v in block)


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


def best_moves(row: dict[str, Any]) -> list[dict[str, Any]]:
    moves = row.get("results", []) or []
    if not moves:
        return []
    best = min(CLASS_RANK.get(m.get("class", "none"), 99) for m in moves)
    return [m for m in moves if CLASS_RANK.get(m.get("class", "none"), 99) == best]


def genuine_for_record(row: dict[str, Any], rec: dict[str, Any], eq: dict[str, Any]) -> list[dict[str, Any]]:
    labels = symbolic_labels(rec, eq)
    out = []
    for move in best_moves(row):
        new_order = [int(x) for x in move.get("new_order", [])]
        if not new_order:
            continue
        for zint in zero_intervals(int(row.get("p")), new_order):
            i, j, length = zint
            sym = symbolic_block(new_order[i:j], labels)
            cls = classify_symbolic_zero(sym, eq)
            if cls in IGNORE_CLASSES:
                continue
            out.append({
                "class": cls,
                "symbol": sym,
                "length": length,
                "interval": [i, j, length],
                "move": move.get("move"),
                "bridge_class": move.get("class"),
                "new_defect": move.get("new_defect"),
            })
    out.sort(key=lambda r: (int(r["length"]), r["class"], r["symbol"], r["move"]))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--analysis", nargs="+", required=True)
    ap.add_argument("--equations", nargs="+", required=True)
    ap.add_argument("--bridge", nargs="+", required=True)
    ap.add_argument("--target-family", required=True)
    ap.add_argument("--target-class", required=True)
    ap.add_argument("--out", default="-")
    ap.add_argument("--summary-out", default=None)
    args = ap.parse_args()

    analysis = load_index(args.analysis)
    equations = load_index(args.equations)
    rows = []
    total_target = 0
    target_has_class = 0
    for name in args.bridge:
        for row in iter_jsonl(Path(name)):
            if row.get("reduced_family") != args.target_family:
                continue
            total_target += 1
            key = (int(row.get("p")), int(row.get("record_index")))
            rec = analysis.get(key)
            eq = equations.get(key)
            if rec is None or eq is None:
                continue
            genuine = genuine_for_record(row, rec, eq)
            has_target = any(g["class"] == args.target_class for g in genuine)
            if has_target:
                target_has_class += 1
                continue
            rows.append({
                "p": row.get("p"),
                "record_index": row.get("record_index"),
                "target_family": args.target_family,
                "missing_target_class": args.target_class,
                "reduced_equation": eq.get("reduced_equation"),
                "extraction_kind": eq.get("extraction_kind"),
                "candidate": {
                    "support_length": eq.get("support_length"),
                    "A": eq.get("A"),
                    "z": eq.get("z"),
                    "q": eq.get("q"),
                    "B": eq.get("B"),
                },
                "best_classes": row.get("result_counts"),
                "genuine_class_counts": dict(Counter(g["class"] for g in genuine).most_common()),
                "genuine_symbols_first30": genuine[:30],
            })

    if args.out == "-":
        for r in rows:
            print(json.dumps(r, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, separators=(",", ":")) + "\n")

    summary = {
        "target_family": args.target_family,
        "target_class": args.target_class,
        "target_records": total_target,
        "records_with_target_class": target_has_class,
        "gap_records": len(rows),
        "gap_record_indices": [r["record_index"] for r in rows],
        "gap_class_histogram": dict(Counter(c for r in rows for c, n in r["genuine_class_counts"].items() for _ in range(n)).most_common()),
    }
    print("summary=" + json.dumps(summary, sort_keys=True))
    if args.summary_out:
        Path(args.summary_out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
