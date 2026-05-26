#!/usr/bin/env python3
"""
Extract symbolic neutral-move patterns for equality hidden-support branches.

Inputs:

    --analysis   logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
    --equations  logs/bzqa_hidden_support_equations_p17_v3.jsonl
    --bridge     logs/hidden_support_bridge_moves_p17_v5.jsonl

and similarly for p=23.

Target equality families:

    B_tail+q=A_complement
    B_tail+q+Y_prefix=A_complement
    B_prefix=q

The goal is to identify the symbolic neutral move pattern that decreases

    q_tail_span_gap = span_gap({q} union B_tail).
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Sequence

TARGET_FAMILIES = {"B_tail+q=A_complement", "B_tail+q+Y_prefix=A_complement", "B_prefix=q"}
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


def load_index(paths: list[str]) -> dict[tuple[int, int], dict[str, Any]]:
    out = {}
    for name in paths:
        for rec in iter_jsonl(Path(name)):
            if "p" in rec and "record_index" in rec:
                out[(int(rec["p"]), int(rec["record_index"]))] = rec
    return out


def find_subsequence(xs: Sequence[int], pat: Sequence[int]) -> int | None:
    n = len(xs)
    m = len(pat)
    for i in range(0, n - m + 1):
        if list(xs[i:i + m]) == list(pat):
            return i
    return None


def split_original(record: dict[str, Any], eq: dict[str, Any]) -> dict[str, list[int]] | None:
    order = [int(x) for x in record.get("order", [])]
    A = [int(x) for x in eq.get("A", [])]
    z = int(eq["z"])
    q = int(eq["q"])
    B = [int(x) for x in eq.get("B", [])]
    pattern = A + [z, q] + B
    start = find_subsequence(order, pattern)
    if start is None:
        return None
    end = start + len(pattern)
    return {
        "X": order[:start],
        "A": A,
        "z": [z],
        "q": [q],
        "B": B,
        "Y": order[end:],
    }


def split_B(eq: dict[str, Any]) -> tuple[list[int], list[int], list[int]]:
    B = [int(x) for x in eq.get("B", [])]
    start = eq.get("B_tail_start_index")
    end = eq.get("B_tail_end_index")
    if start is None:
        return B, [], []
    s = int(start)
    e = int(end) if end is not None else len(B)
    return B[: max(0, s - 1)], B[max(0, s - 1):e], B[e:]


def labels_for(eq: dict[str, Any], parts: dict[str, list[int]]) -> dict[int, list[str]]:
    out: dict[int, list[str]] = defaultdict(list)
    for i, x in enumerate(parts.get("X", []), start=1):
        out[int(x)].append(f"X{i}")
    for i, x in enumerate(eq.get("A", []), start=1):
        out[int(x)].append(f"A{i}")
    out[int(eq["z"])].append("z")
    out[int(eq["q"])].append("q")
    for i, x in enumerate(eq.get("B", []), start=1):
        out[int(x)].append(f"B{i}")
    for i, x in enumerate(parts.get("Y", []), start=1):
        out[int(x)].append(f"Y{i}")
    return out


def symbolic_order(order: Sequence[int], labels: dict[int, list[str]]) -> str:
    return " ".join("/".join(labels.get(int(x), [f"?{x}"])) for x in order)


def symbolic_values(values: Sequence[int], labels: dict[int, list[str]]) -> list[str]:
    return ["/".join(labels.get(int(x), [f"?{x}"])) for x in values]


def positions(order: Sequence[int]) -> dict[int, int]:
    return {int(v): i for i, v in enumerate(order)}


def span_gap(order: Sequence[int], values: Sequence[int]) -> int | None:
    pos = positions(order)
    ps = [pos.get(int(v)) for v in values]
    if any(p is None for p in ps):
        return None
    xs = [int(p) for p in ps if p is not None]
    if not xs:
        return None
    return max(xs) - min(xs) + 1 - len(xs)


def span_width(order: Sequence[int], values: Sequence[int]) -> int | None:
    pos = positions(order)
    ps = [pos.get(int(v)) for v in values]
    if any(p is None for p in ps):
        return None
    xs = [int(p) for p in ps if p is not None]
    if not xs:
        return None
    return max(xs) - min(xs) + 1


def neutral_moves(row: dict[str, Any]) -> list[dict[str, Any]]:
    return [m for m in (row.get("results", []) or []) if m.get("class") == "neutral"]


def summarize_pattern(old_sym: str, new_sym: str) -> str:
    old_tokens = old_sym.split()
    new_tokens = new_sym.split()
    # Compact active-window view: strip leading/trailing X/Y tokens when possible.
    def active(tokens: list[str]) -> list[str]:
        keep = [i for i, t in enumerate(tokens) if not (t.startswith("X") or t.startswith("Y"))]
        if not keep:
            return tokens
        return tokens[min(keep): max(keep) + 1]
    return "OLD[" + " ".join(active(old_tokens)) + "] -> NEW[" + " ".join(active(new_tokens)) + "]"


def analyze_row(row: dict[str, Any], rec: dict[str, Any], eq: dict[str, Any]) -> dict[str, Any] | None:
    p = int(row.get("p"))
    old_order = [int(x) for x in rec.get("order", [])]
    parts = split_original(rec, eq)
    if parts is None:
        return None
    labels = labels_for(eq, parts)
    _Bp, Bt, _Bm = split_B(eq)
    q = int(eq["q"])
    tail_values = [q] + Bt
    old_gap = span_gap(old_order, tail_values)
    old_width = span_width(old_order, tail_values)
    old_sym = symbolic_order(old_order, labels)
    rows = []
    for m in neutral_moves(row):
        new_order = [int(x) for x in m.get("new_order", [])]
        new_gap = span_gap(new_order, tail_values)
        new_width = span_width(new_order, tail_values)
        improves = []
        if old_gap is not None and new_gap is not None and new_gap < old_gap:
            improves.append("q_tail_span_gap")
        if old_width is not None and new_width is not None and new_width < old_width:
            improves.append("q_tail_span_width")
        new_sym = symbolic_order(new_order, labels)
        rows.append({
            "move": m.get("move"),
            "new_defect": m.get("new_defect"),
            "old_q_tail_span_gap": old_gap,
            "new_q_tail_span_gap": new_gap,
            "old_q_tail_span_width": old_width,
            "new_q_tail_span_width": new_width,
            "improves": improves,
            "new_symbolic_order": new_sym,
            "pattern": summarize_pattern(old_sym, new_sym),
        })
    return {
        "p": p,
        "record_index": row.get("record_index"),
        "family": row.get("reduced_family"),
        "reduced_equation": eq.get("reduced_equation"),
        "B_tail_labels": symbolic_values(Bt, labels),
        "q_label": "q",
        "old_symbolic_order": old_sym,
        "neutral_move_count": len(rows),
        "neutral_moves": rows,
        "patterns": sorted(set(r["pattern"] for r in rows)),
        "moves_improving_gap": [r for r in rows if "q_tail_span_gap" in r["improves"]],
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    records_by_family = Counter(r["family"] for r in rows)
    pattern_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    move_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    gap_improve_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    for r in rows:
        fam = r["family"]
        gap_improve_by_family[fam]["yes" if r["moves_improving_gap"] else "no"] += 1
        for pat in r["patterns"]:
            pattern_by_family[fam][pat] += 1
        for m in r["neutral_moves"]:
            move_by_family[fam][m["move"]] += 1
    return {
        "records": len(rows),
        "records_by_family": dict(records_by_family.most_common()),
        "gap_improve_by_family": {k: dict(v.most_common()) for k, v in gap_improve_by_family.items()},
        "move_name_by_family": {k: dict(v.most_common()) for k, v in move_by_family.items()},
        "pattern_by_family": {k: dict(v.most_common()) for k, v in pattern_by_family.items()},
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--analysis", nargs="+", required=True)
    ap.add_argument("--equations", nargs="+", required=True)
    ap.add_argument("--bridge", nargs="+", required=True)
    ap.add_argument("--out", default="-")
    ap.add_argument("--summary-out", default=None)
    args = ap.parse_args()

    analysis = load_index(args.analysis)
    equations = load_index(args.equations)
    rows = []
    for name in args.bridge:
        for row in iter_jsonl(Path(name)):
            if row.get("reduced_family") not in TARGET_FAMILIES:
                continue
            key = (int(row.get("p")), int(row.get("record_index")))
            rec = analysis.get(key)
            eq = equations.get(key)
            if rec is None or eq is None:
                continue
            out = analyze_row(row, rec, eq)
            if out is not None:
                rows.append(out)

    if args.out == "-":
        for r in rows:
            print(json.dumps(r, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, separators=(",", ":")) + "\n")

    summary = summarize(rows)
    print("summary=" + json.dumps(summary, sort_keys=True))
    if args.summary_out:
        Path(args.summary_out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
