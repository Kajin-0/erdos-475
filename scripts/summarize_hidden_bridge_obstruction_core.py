#!/usr/bin/env python3
"""
Summarize obstruction cores from hidden-support bridge move tests.

Input is produced by:

    scripts/test_hidden_support_bridge_moves.py

Typical inputs:

    logs/hidden_support_bridge_moves_p17_v5.jsonl
    logs/hidden_support_bridge_moves_p23_v5.jsonl

The goal is to understand why the verified hidden support equations do not yet
produce D_short descent under the naive bridge moves.

The script summarizes by reduced family:

    - best move classes
    - best move names
    - new defects
    - shortest zero-interval length created
    - zero-interval signatures relative to the old defect
    - compact representative examples
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

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


def tuple_key(x: Any) -> str:
    if isinstance(x, (list, tuple)):
        return "(" + ",".join(tuple_key(v) if isinstance(v, (list, tuple)) else str(v) for v in x) + ")"
    return str(x)


def best_moves(row: dict[str, Any]) -> list[dict[str, Any]]:
    moves = row.get("results", []) or []
    if not moves:
        return []
    best = min(CLASS_RANK.get(m.get("class", "none"), 99) for m in moves)
    return [m for m in moves if CLASS_RANK.get(m.get("class", "none"), 99) == best]


def shortest_interval_lengths(move: dict[str, Any]) -> list[int]:
    return sorted({int(z[2]) for z in move.get("zero_intervals_first10", []) or [] if len(z) >= 3})


def interval_signature(old_defect: list[Any], move: dict[str, Any]) -> str:
    nd = move.get("new_defect")
    if not nd:
        return "missing_new_defect"
    try:
        old_E, old_L, old_N = int(old_defect[0]), int(old_defect[1]), int(old_defect[2])
        new_E, new_L, new_N = int(nd[0]), int(nd[1]), int(nd[2])
    except Exception:
        return "bad_defect"
    pieces = []
    if new_E > old_E:
        pieces.append(f"E+{new_E-old_E}")
    elif new_E == old_E:
        pieces.append("E=")
    else:
        pieces.append(f"E{new_E-old_E}")
    if new_L > old_L:
        pieces.append(f"L+{new_L-old_L}")
    elif new_L == old_L:
        pieces.append("L=")
    else:
        pieces.append(f"L{new_L-old_L}")
    if new_N > old_N:
        pieces.append(f"N+{new_N-old_N}")
    elif new_N == old_N:
        pieces.append("N=")
    else:
        pieces.append(f"N{new_N-old_N}")
    pieces.append("M=" + tuple_key(nd[3] if len(nd) > 3 else []))
    return ";".join(pieces)


def compact_example(row: dict[str, Any], move: dict[str, Any]) -> dict[str, Any]:
    he = row.get("hidden_equation", {}) or {}
    return {
        "p": row.get("p"),
        "record_index": row.get("record_index"),
        "reduced_family": row.get("reduced_family"),
        "extraction_kind": row.get("extraction_kind"),
        "hidden_equation": {
            "mode": he.get("mode"),
            "reduced_equation": he.get("reduced_equation"),
            "family": he.get("family"),
        },
        "move": move.get("move"),
        "class": move.get("class"),
        "terminal_progress": move.get("terminal_progress"),
        "old_defect": row.get("old_defect"),
        "new_defect": move.get("new_defect"),
        "interval_signature": interval_signature(row.get("old_defect", []), move),
        "zero_intervals_first10": move.get("zero_intervals_first10", [])[:10],
    }


def summarize(records: list[dict[str, Any]], example_limit: int) -> dict[str, Any]:
    family_records = Counter()
    family_best_class: dict[str, Counter[str]] = defaultdict(Counter)
    family_best_move: dict[str, Counter[str]] = defaultdict(Counter)
    family_best_progress: dict[str, Counter[str]] = defaultdict(Counter)
    family_new_defect: dict[str, Counter[str]] = defaultdict(Counter)
    family_interval_sig: dict[str, Counter[str]] = defaultdict(Counter)
    family_shortest_lengths: dict[str, Counter[str]] = defaultdict(Counter)
    family_equation_mode: dict[str, Counter[str]] = defaultdict(Counter)
    examples: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for row in records:
        fam = row.get("reduced_family", "unknown")
        family_records[fam] += 1
        he = row.get("hidden_equation", {}) or {}
        family_equation_mode[fam][str(he.get("mode"))] += 1
        bms = best_moves(row)
        if not bms:
            family_best_class[fam]["none"] += 1
            continue
        for bm in bms:
            cls = bm.get("class", "none")
            family_best_class[fam][cls] += 1
            family_best_move[fam][bm.get("move", "unknown")] += 1
            family_best_progress[fam][bm.get("terminal_progress", "unknown")] += 1
            family_new_defect[fam][tuple_key(bm.get("new_defect"))] += 1
            family_interval_sig[fam][interval_signature(row.get("old_defect", []), bm)] += 1
            lens = shortest_interval_lengths(bm)
            if lens:
                family_shortest_lengths[fam][str(lens[0])] += 1
            else:
                family_shortest_lengths[fam]["none"] += 1
            if len(examples[fam]) < example_limit:
                examples[fam].append(compact_example(row, bm))

    return {
        "records": len(records),
        "records_by_family": dict(family_records.most_common()),
        "equation_mode_by_family": {k: dict(v.most_common()) for k, v in family_equation_mode.items()},
        "best_class_by_family": {k: dict(v.most_common()) for k, v in family_best_class.items()},
        "best_move_by_family": {k: dict(v.most_common()) for k, v in family_best_move.items()},
        "best_terminal_progress_by_family": {k: dict(v.most_common()) for k, v in family_best_progress.items()},
        "best_new_defect_by_family": {k: dict(v.most_common(20)) for k, v in family_new_defect.items()},
        "best_interval_signature_by_family": {k: dict(v.most_common(20)) for k, v in family_interval_sig.items()},
        "best_shortest_zero_length_by_family": {k: dict(v.most_common()) for k, v in family_shortest_lengths.items()},
        "examples_by_family": dict(examples),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input hidden-support bridge move JSONL files.")
    ap.add_argument("--out", default="-", help="Output JSON path, or '-' for stdout.")
    ap.add_argument("--pretty", action="store_true")
    ap.add_argument("--example-limit", type=int, default=2)
    args = ap.parse_args()

    records: list[dict[str, Any]] = []
    input_files = {}
    for name in args.jsonl:
        loaded = list(iter_jsonl(Path(name)))
        input_files[name] = len(loaded)
        records.extend(loaded)

    summary = summarize(records, args.example_limit)
    summary["input_files"] = input_files
    text = json.dumps(summary, indent=2 if args.pretty else None, sort_keys=True)
    if args.out == "-":
        print(text)
    else:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
