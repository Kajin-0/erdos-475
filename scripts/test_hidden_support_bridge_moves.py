#!/usr/bin/env python3
"""
Test deterministic bridge moves induced by the B z q A hidden-support equation.

Inputs:

    1. analyzed pure m=3 structure JSONL, produced by:
       scripts/analyze_pure_m3_terminal_structure.py

    2. hidden-support equation JSONL, produced by:
       scripts/extract_bzqa_tail_core_equations.py

Typical use:

    python3 scripts/test_hidden_support_bridge_moves.py \
      --analysis logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl \
      --equations logs/bzqa_hidden_support_equations_p17.jsonl \
      --out logs/hidden_support_bridge_moves_p17.jsonl \
      --summary-out logs/summary_hidden_support_bridge_moves_p17.json

The tested equation families are:

    B_tail+q
    B_tail+q+Y_prefix
    B_prefix=q

This script is exploratory.  It does not assume the moves prove anything by
themselves.  Its purpose is to identify a deterministic move primitive that
routes the hidden-support equation into D_short descent, rightward progress,
cyclic progress, or another classified bridge branch.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Sequence, Tuple

INF = 10**9
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


def defect_short(p: int, order: Sequence[int]) -> tuple[Any, ...]:
    P = partial_sums_extended(p, order)
    counts = Counter(P)
    E = len(P) - len(counts)
    if E == 0:
        return (0, INF, 0, tuple())
    zis = zero_intervals(p, order)
    L_min = min(length for _, _, length in zis)
    N_min = sum(1 for _, _, length in zis if length == L_min)
    M = tuple(sorted((c for c in counts.values() if c > 1), reverse=True))
    return (E, L_min, N_min, M)


def jsonable_defect(D: tuple[Any, ...]) -> list[Any]:
    return [D[0], D[1], D[2], list(D[3])]


def compare_defect(old: tuple[Any, ...], new: tuple[Any, ...]) -> str:
    if new < old:
        return "improved"
    if new == old:
        return "neutral"
    return "worse"


def unique_zero_interval_of_length(p: int, order: Sequence[int], length: int) -> tuple[int, int, int] | None:
    matches = [z for z in zero_intervals(p, order) if z[2] == length]
    if len(matches) == 1:
        return matches[0]
    return None


def interval_payload(order: Sequence[int], interval: tuple[int, int, int] | None) -> dict[str, Any] | None:
    if interval is None:
        return None
    i, j, length = interval
    n = len(order)
    return {
        "i": i,
        "j": j,
        "length": length,
        "block": [int(x) for x in order[i:j]],
        "left_distance": i,
        "right_distance": n - j,
        "center2": i + j,
    }


def terminal_progress(p: int, old_order: Sequence[int], new_order: Sequence[int]) -> str:
    old = interval_payload(old_order, unique_zero_interval_of_length(p, old_order, 3))
    new = interval_payload(new_order, unique_zero_interval_of_length(p, new_order, 3))
    if old is None or new is None:
        return "unknown"
    dc = int(new["center2"]) - int(old["center2"])
    if dc > 0:
        return "rightward_progress"
    if dc < 0:
        return "leftward_regress"
    return "same_position"


def find_subsequence(xs: Sequence[int], pat: Sequence[int]) -> int | None:
    n = len(xs)
    m = len(pat)
    for i in range(0, n - m + 1):
        if list(xs[i:i + m]) == list(pat):
            return i
    return None


def load_analysis(paths: list[str]) -> dict[tuple[int, int], dict[str, Any]]:
    out = {}
    for name in paths:
        for rec in iter_jsonl(Path(name)):
            if rec.get("pure_label") != "pure_worse_only":
                continue
            out[(int(rec["p"]), int(rec["record_index"]))] = rec
    return out


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


def split_B(eq: dict[str, Any]) -> dict[str, list[int] | int | None]:
    B = [int(x) for x in eq.get("B", [])]
    start = eq.get("B_tail_start_index")
    end = eq.get("B_tail_end_index")
    if start is None:
        return {"B_prefix": B, "B_tail": [], "B_middle_after_tail": [], "tail_start": None, "tail_end": None}
    s = int(start)
    e = int(end) if end is not None else len(B)
    prefix = B[: max(0, s - 1)]
    tail = B[max(0, s - 1): e]
    middle_after_tail = B[e:]
    return {
        "B_prefix": prefix,
        "B_tail": tail,
        "B_middle_after_tail": middle_after_tail,
        "tail_start": s,
        "tail_end": e,
    }


def parse_token(tok: str) -> tuple[str, int | None]:
    m = TOKEN_RE.match(tok)
    if not m:
        return (tok, None)
    base, idx = m.group(1), m.group(2)
    return (base, int(idx) if idx is not None else None)


def token_value(tok: str, eq: dict[str, Any], parts: dict[str, list[int]]) -> int | None:
    base, idx = parse_token(tok)
    if base == "q":
        return int(eq["q"])
    if base == "z":
        return int(eq["z"])
    if base == "A" and idx is not None:
        A = [int(x) for x in eq.get("A", [])]
        if 1 <= idx <= len(A):
            return A[idx - 1]
    if base == "B" and idx is not None:
        B = [int(x) for x in eq.get("B", [])]
        if 1 <= idx <= len(B):
            return B[idx - 1]
    if base == "Y" and idx is not None:
        Y = parts.get("Y", [])
        if 1 <= idx <= len(Y):
            return int(Y[idx - 1])
    if base == "X" and idx is not None:
        X = parts.get("X", [])
        if 1 <= idx <= len(X):
            return int(X[idx - 1])
    return None


def values_from_symbolic(eq: dict[str, Any], parts: dict[str, list[int]], symbolic: str) -> list[int]:
    vals = []
    for tok in symbolic.split():
        if tok == "=":
            continue
        v = token_value(tok, eq, parts)
        if v is not None:
            vals.append(v)
    return vals


def make_moves(parts: dict[str, list[int]], eq: dict[str, Any]) -> dict[str, list[int]]:
    X = parts["X"]
    A = parts["A"]
    z = parts["z"]
    q = parts["q"]
    Y = parts["Y"]
    bsplit = split_B(eq)
    Bp = list(bsplit["B_prefix"])
    Bt = list(bsplit["B_tail"])
    Bm = list(bsplit["B_middle_after_tail"])
    ylen = int(eq.get("Y_prefix_length") or 0)
    Yp = Y[:ylen]
    Yr = Y[ylen:]

    moves: dict[str, list[int]] = {}

    # Generic tail moves.  These are meaningful for both B_tail+q and B_tail+q+Y_prefix.
    moves["q_tail_prefix_middle"] = X + A + z + q + Bt + Yp + Bp + Bm + Yr
    moves["tail_q_prefix_middle"] = X + A + z + Bt + q + Yp + Bp + Bm + Yr
    moves["prefix_q_tail_middle"] = X + A + z + Bp + q + Bt + Yp + Bm + Yr
    moves["prefix_tail_q_middle"] = X + A + z + Bp + Bt + q + Yp + Bm + Yr

    # Exterior-aware variants keep Y_prefix with the hidden zero equation.
    if ylen > 0:
        moves["q_tail_Yprefix_then_prefix"] = X + A + z + q + Bt + Yp + Bp + Bm + Yr
        moves["tail_q_Yprefix_then_prefix"] = X + A + z + Bt + q + Yp + Bp + Bm + Yr
        moves["prefix_q_tail_Yprefix"] = X + A + z + Bp + q + Bt + Yp + Bm + Yr

    # Prefix=q variants.  These test support-prefix compression/swap patterns.
    if eq.get("reduced_family") == "B_prefix=q":
        moves["prefix_then_q_tail"] = X + A + z + Bp + q + Bt + Bm + Y
        moves["q_then_tail_then_prefix"] = X + A + z + q + Bt + Bm + Bp + Y
        moves["tail_then_q_then_prefix"] = X + A + z + Bt + Bm + q + Bp + Y
        moves["prefix_replaces_q_position"] = X + A + z + Bp + Bt + Bm + q + Y

    # Preserve only moves that are permutations of the original order.
    old_sorted = sorted(X + A + z + q + Bp + Bt + Bm + Y)
    return {name: m for name, m in moves.items() if sorted(m) == old_sorted and len(m) == len(old_sorted)}


def block_sum(p: int, xs: Sequence[int]) -> int:
    return sum(int(x) for x in xs) % p


def hidden_equation_check(eq: dict[str, Any], parts: dict[str, list[int]]) -> dict[str, Any]:
    """Verify the extracted equation from its symbolic reduced form.

    The first version reconstructed Y_prefix from length alone, which can be too
    coarse when the symbolic equation contains a specific exterior-labelled
    block.  This version evaluates the actual `reduced_equation` tokens.
    """
    p = int(eq["p"])
    bsplit = split_B(eq)
    Bp = list(bsplit["B_prefix"])
    Bt = list(bsplit["B_tail"])
    if eq.get("reduced_family") == "B_prefix=q":
        return {
            "family": "B_prefix=q",
            "lhs_sum": block_sum(p, Bp),
            "q": int(eq["q"]),
            "holds": block_sum(p, Bp) == int(eq["q"]) % p,
            "B_prefix": Bp,
            "B_tail": Bt,
            "reduced_equation": eq.get("reduced_equation"),
        }
    block = values_from_symbolic(eq, parts, str(eq.get("reduced_equation", "")))
    return {
        "family": eq.get("reduced_family"),
        "zero_block": block,
        "zero_block_sum": block_sum(p, block),
        "holds": block_sum(p, block) == 0,
        "B_prefix": Bp,
        "B_tail": Bt,
        "reduced_equation": eq.get("reduced_equation"),
    }


def analyze_equation(eq: dict[str, Any], record: dict[str, Any]) -> dict[str, Any]:
    p = int(eq["p"])
    old_order = [int(x) for x in record.get("order", [])]
    oldD = defect_short(p, old_order)
    parts = split_original(record, eq)
    if parts is None:
        return {
            "record_index": eq.get("record_index"),
            "p": p,
            "error": "could_not_split_original_order",
        }
    moves = make_moves(parts, eq)
    results = []
    for name, new_order in moves.items():
        newD = defect_short(p, new_order)
        results.append(
            {
                "move": name,
                "new_defect": jsonable_defect(newD),
                "class": compare_defect(oldD, newD),
                "terminal_progress": terminal_progress(p, old_order, new_order),
                "zero_intervals_first10": [list(z) for z in zero_intervals(p, new_order)[:10]],
                "new_order": new_order,
            }
        )
    best_rank = {"improved": 0, "neutral": 1, "worse": 2}
    best = min((best_rank[r["class"]] for r in results), default=99)
    best_class = {0: "improved", 1: "neutral", 2: "worse"}.get(best, "none")
    return {
        "record_index": eq.get("record_index"),
        "p": p,
        "support_length": eq.get("support_length"),
        "reduced_family": eq.get("reduced_family"),
        "extraction_kind": eq.get("extraction_kind"),
        "hidden_equation": hidden_equation_check(eq, parts),
        "old_defect": jsonable_defect(oldD),
        "move_count": len(results),
        "best_class": best_class,
        "result_counts": dict(Counter(r["class"] for r in results).most_common()),
        "terminal_progress_counts": dict(Counter(r["terminal_progress"] for r in results).most_common()),
        "results": results,
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    best = Counter(row.get("best_class", "error") for row in rows)
    family_best: dict[str, Counter[str]] = defaultdict(Counter)
    family_result: dict[str, Counter[str]] = defaultdict(Counter)
    progress: Counter[str] = Counter()
    hold = Counter(str(row.get("hidden_equation", {}).get("holds")) for row in rows if "hidden_equation" in row)
    for row in rows:
        fam = row.get("reduced_family", "unknown")
        family_best[fam][row.get("best_class", "error")] += 1
        family_result[fam].update(row.get("result_counts", {}))
        progress.update(row.get("terminal_progress_counts", {}))
    return {
        "records": len(rows),
        "hidden_equation_holds": dict(hold.most_common()),
        "best_class_counts": dict(best.most_common()),
        "best_class_by_family": {k: dict(v.most_common()) for k, v in family_best.items()},
        "move_class_by_family": {k: dict(v.most_common()) for k, v in family_result.items()},
        "terminal_progress_counts": dict(progress.most_common()),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--analysis", nargs="+", required=True, help="Analyzed pure m3 structure JSONL files.")
    ap.add_argument("--equations", nargs="+", required=True, help="Hidden-support equation JSONL files.")
    ap.add_argument("--out", default="-", help="Output JSONL path, or '-' for stdout.")
    ap.add_argument("--summary-out", default=None, help="Optional summary JSON path.")
    args = ap.parse_args()

    analysis = load_analysis(args.analysis)
    rows = []
    missing = []
    for eq_name in args.equations:
        for eq in iter_jsonl(Path(eq_name)):
            key = (int(eq["p"]), int(eq["record_index"]))
            rec = analysis.get(key)
            if rec is None:
                missing.append({"p": key[0], "record_index": key[1], "error": "missing_analysis_record"})
                continue
            rows.append(analyze_equation(eq, rec))

    if args.out == "-":
        for row in rows:
            print(json.dumps(row, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for row in rows:
                fh.write(json.dumps(row, separators=(",", ":")) + "\n")

    summary = summarize(rows)
    summary["missing_analysis_records"] = missing
    print("summary=" + json.dumps(summary, sort_keys=True))
    if args.summary_out:
        Path(args.summary_out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
