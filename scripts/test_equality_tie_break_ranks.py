#!/usr/bin/env python3
"""
Test candidate refined tie-break ranks for the equality hidden-support branch.

Inputs:

    --analysis   logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
    --equations  logs/bzqa_hidden_support_equations_p17_v3.jsonl
    --bridge     logs/hidden_support_bridge_moves_p17_v5.jsonl

and similarly for p=23.

Target equality families:

    B_tail+q=A_complement
    B_prefix=q

The goal is to see whether neutral bridge moves decrease any natural refined
rank while preserving D_short:

    terminal position rank,
    cyclic triple rank,
    q-tail span rank,
    q-tail-complement span rank,
    q-prefix span rank.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Sequence, Tuple

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


def length3_intervals(p: int, order: Sequence[int]) -> list[tuple[int, int, int]]:
    return [z for z in zero_intervals(p, order) if z[2] == 3]


def distinguished_length3(p: int, order: Sequence[int]) -> tuple[int, int, int] | None:
    zs = length3_intervals(p, order)
    if not zs:
        return None
    # Right-terminal branch: use rightmost length-3 zero interval as distinguished.
    return max(zs, key=lambda z: (z[1], z[0]))


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


def parse_token(tok: str) -> tuple[str, int | None]:
    m = TOKEN_RE.match(tok)
    if not m:
        return (tok, None)
    base, idx = m.group(1), m.group(2)
    return (base, int(idx) if idx is not None else None)


def split_B(eq: dict[str, Any]) -> tuple[list[int], list[int], list[int]]:
    B = [int(x) for x in eq.get("B", [])]
    start = eq.get("B_tail_start_index")
    end = eq.get("B_tail_end_index")
    if start is None:
        return B, [], []
    s = int(start)
    e = int(end) if end is not None else len(B)
    return B[: max(0, s - 1)], B[max(0, s - 1):e], B[e:]


def complement_A(eq: dict[str, Any]) -> int | None:
    red = str(eq.get("reduced_equation", ""))
    if "=" not in red:
        return None
    rhs = red.split("=", 1)[1].strip().split()
    A = [int(x) for x in eq.get("A", [])]
    for tok in rhs:
        base, idx = parse_token(tok)
        if base == "A" and idx is not None and 1 <= idx <= len(A):
            return A[idx - 1]
    return None


def cyclic_triple_rank(order: Sequence[int], eq: dict[str, Any]) -> int | None:
    A = [int(x) for x in eq.get("A", [])]
    if len(A) != 2:
        return None
    z = int(eq.get("z"))
    triples = [A + [z], [A[1], z, A[0]], [z] + A]
    # Lower is better.  Tentative canonical preference: z A1 A2, A1 A2 z, A2 z A1.
    rank_map = {tuple([z] + A): 0, tuple(A + [z]): 1, tuple([A[1], z, A[0]]): 2}
    for i in range(0, len(order) - 2):
        block = tuple(int(x) for x in order[i:i + 3])
        if block in rank_map:
            return rank_map[block]
    return None


def terminal_rank(order: Sequence[int], p: int) -> dict[str, Any]:
    z = distinguished_length3(p, order)
    if z is None:
        return {"exists": False, "right_distance": None, "center2_rank": None, "interval": None}
    i, j, _ = z
    return {"exists": True, "right_distance": len(order) - j, "center2_rank": -(i + j), "interval": [i, j, 3]}


def rank_payload(order: Sequence[int], p: int, eq: dict[str, Any]) -> dict[str, Any]:
    Bp, Bt, _Bm = split_B(eq)
    q = int(eq.get("q"))
    acomp = complement_A(eq)
    fam = eq.get("reduced_family")
    terminal = terminal_rank(order, p)
    payload = {
        "terminal_right_distance": terminal["right_distance"],
        "terminal_center2_rank": terminal["center2_rank"],
        "terminal_interval": terminal["interval"],
        "cyclic_triple_rank": cyclic_triple_rank(order, eq),
        "q_tail_span_gap": span_gap(order, [q] + Bt),
        "q_tail_span_width": span_width(order, [q] + Bt),
        "q_tail_comp_span_gap": span_gap(order, [q] + Bt + ([acomp] if acomp is not None else [])),
        "q_tail_comp_span_width": span_width(order, [q] + Bt + ([acomp] if acomp is not None else [])),
        "q_prefix_span_gap": span_gap(order, [q] + Bp),
        "q_prefix_span_width": span_width(order, [q] + Bp),
    }
    return payload


def delta(old: Any, new: Any) -> str:
    if old is None or new is None:
        return "unknown"
    if new < old:
        return "improved"
    if new == old:
        return "same"
    return "worse"


def neutral_moves(row: dict[str, Any]) -> list[dict[str, Any]]:
    return [m for m in (row.get("results", []) or []) if m.get("class") == "neutral"]


def analyze_row(row: dict[str, Any], rec: dict[str, Any], eq: dict[str, Any]) -> dict[str, Any]:
    p = int(row.get("p"))
    old_order = [int(x) for x in rec.get("order", [])]
    old_rank = rank_payload(old_order, p, eq)
    moves = []
    for m in neutral_moves(row):
        new_order = [int(x) for x in m.get("new_order", [])]
        new_rank = rank_payload(new_order, p, eq)
        deltas = {k: delta(old_rank.get(k), new_rank.get(k)) for k in old_rank if not k.endswith("interval")}
        improves = sorted(k for k, v in deltas.items() if v == "improved")
        moves.append(
            {
                "move": m.get("move"),
                "old_rank": old_rank,
                "new_rank": new_rank,
                "deltas": deltas,
                "improves": improves,
                "new_defect": m.get("new_defect"),
            }
        )
    all_improves = sorted(set(k for m in moves for k in m["improves"]))
    return {
        "p": p,
        "record_index": row.get("record_index"),
        "family": row.get("reduced_family"),
        "reduced_equation": eq.get("reduced_equation"),
        "candidate": {
            "A": eq.get("A"),
            "z": eq.get("z"),
            "q": eq.get("q"),
            "B": eq.get("B"),
            "B_tail_start_index": eq.get("B_tail_start_index"),
            "B_tail_length": eq.get("B_tail_length"),
            "B_prefix_length": eq.get("B_prefix_length"),
        },
        "neutral_move_count": len(moves),
        "all_improves": all_improves,
        "has_any_improve": bool(all_improves),
        "moves": moves,
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    records_by_family = Counter(r["family"] for r in rows)
    has_improve_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    improve_key_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    neutral_count_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    for r in rows:
        fam = r["family"]
        has_improve_by_family[fam]["yes" if r["has_any_improve"] else "no"] += 1
        neutral_count_by_family[fam][str(r["neutral_move_count"])] += 1
        for key in r["all_improves"]:
            improve_key_by_family[fam][key] += 1
    return {
        "records": len(rows),
        "records_by_family": dict(records_by_family.most_common()),
        "has_improve_by_family": {k: dict(v.most_common()) for k, v in has_improve_by_family.items()},
        "neutral_move_count_by_family": {k: dict(v.most_common()) for k, v in neutral_count_by_family.items()},
        "improve_key_coverage_by_family": {k: dict(v.most_common()) for k, v in improve_key_by_family.items()},
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
            rows.append(analyze_row(row, rec, eq))

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
