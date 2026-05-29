#!/usr/bin/env python3
"""
Diagnose why equality three-localization candidates are worse.

This script rebuilds the old, L1, L2, L3 orders for equality hidden-support
records and compares zero-interval defects.  It reports the new shortest zero
blocks that appear in worse candidates.

Inputs:

    --analysis  logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
    --equations logs/bzqa_hidden_support_equations_p17_v3.jsonl

Typical use:

    python3 scripts/diagnose_three_localization_worse_conditions.py \
      --analysis logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl \
      --equations logs/bzqa_hidden_support_equations_p17_v3.jsonl \
      --out logs/three_localization_worse_conditions_p17.jsonl \
      --summary-out logs/summary_three_localization_worse_conditions_p17.json
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Sequence, Tuple

INF = 10**9
TARGET_FAMILIES = {"B_tail+q=A_complement", "B_tail+q+Y_prefix=A_complement", "B_prefix=q"}


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
    out: list[Tuple[int, int, int]] = []
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            if P[i] == P[j]:
                out.append((i, j, j - i))
    return out


def defect_short(p: int, order: Sequence[int]) -> tuple[int, int, int, tuple[int, ...]]:
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


def labels(parts: dict[str, list[int]], eq: dict[str, Any]) -> dict[int, list[str]]:
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


def sym(order: Sequence[int], lab: dict[int, list[str]]) -> str:
    return " ".join("/".join(lab.get(int(x), [f"?{x}"])) for x in order)


def active_sym(order: Sequence[int], lab: dict[int, list[str]]) -> str:
    toks = sym(order, lab).split()
    keep = [i for i, t in enumerate(toks) if not (t.startswith("X") or t.startswith("Y"))]
    if not keep:
        return " ".join(toks)
    return " ".join(toks[min(keep): max(keep) + 1])


def build_candidates(parts: dict[str, list[int]], eq: dict[str, Any]) -> dict[str, list[int]]:
    P, T, M = split_B(eq)
    X = parts["X"]
    A = parts["A"]
    z = parts["z"]
    q = parts["q"]
    Y = parts["Y"]
    return {
        "old": X + A + z + q + P + T + M + Y,
        "P_q_T_M": X + A + z + P + q + T + M + Y,
        "q_T_P_M": X + A + z + q + T + P + M + Y,
        "T_q_P_M": X + A + z + T + q + P + M + Y,
    }


def interval_blocks(p: int, order: Sequence[int], lab: dict[int, list[str]]) -> list[dict[str, Any]]:
    blocks = []
    for i, j, length in zero_intervals(p, order):
        block = list(order[i:j])
        blocks.append({
            "interval": [i, j, length],
            "length": length,
            "symbolic_block": sym(block, lab),
            "numeric_block": block,
        })
    blocks.sort(key=lambda b: (b["length"], b["symbolic_block"]))
    return blocks


def classify_vs(oldD: tuple[int, int, int, tuple[int, ...]], newD: tuple[int, int, int, tuple[int, ...]]) -> str:
    if newD < oldD:
        return "improved"
    if newD == oldD:
        return "neutral"
    return "worse"


def new_short_blocks(old_blocks: list[dict[str, Any]], cand_blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    old_set = {b["symbolic_block"] for b in old_blocks}
    if not cand_blocks:
        return []
    min_len = min(b["length"] for b in cand_blocks)
    return [b for b in cand_blocks if b["length"] == min_len and b["symbolic_block"] not in old_set]


def analyze_record(rec: dict[str, Any], eq: dict[str, Any]) -> dict[str, Any] | None:
    if eq.get("reduced_family") not in TARGET_FAMILIES:
        return None
    parts = split_original(rec, eq)
    if parts is None:
        return None
    p = int(rec["p"])
    lab = labels(parts, eq)
    candidates = build_candidates(parts, eq)
    old_order = candidates["old"]
    oldD = defect_short(p, old_order)
    old_blocks = interval_blocks(p, old_order, lab)
    rows = []
    for name, order in candidates.items():
        if name == "old":
            continue
        D = defect_short(p, order)
        blocks = interval_blocks(p, order, lab)
        cls = classify_vs(oldD, D)
        rows.append({
            "name": name,
            "class_vs_old": cls,
            "defect": list(D),
            "active_symbolic": active_sym(order, lab),
            "shortest_blocks_first10": blocks[:10],
            "new_short_blocks_first10": new_short_blocks(old_blocks, blocks)[:10],
        })
    worse_rows = [r for r in rows if r["class_vs_old"] == "worse"]
    neutral_rows = [r for r in rows if r["class_vs_old"] == "neutral"]
    return {
        "p": p,
        "record_index": rec.get("record_index"),
        "family": eq.get("reduced_family"),
        "reduced_equation": eq.get("reduced_equation"),
        "old_defect": list(oldD),
        "old_active_symbolic": active_sym(old_order, lab),
        "old_shortest_blocks_first10": old_blocks[:10],
        "candidates": rows,
        "worse_candidate_names": [r["name"] for r in worse_rows],
        "neutral_candidate_names": [r["name"] for r in neutral_rows],
        "all_three_worse": len(worse_rows) == 3,
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    records_by_family = Counter(r["family"] for r in rows)
    all_three = Counter("yes" if r["all_three_worse"] else "no" for r in rows)
    worse_combo_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    neutral_combo_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    new_short_by_candidate: dict[str, Counter[str]] = defaultdict(Counter)
    for r in rows:
        fam = r["family"]
        worse_combo_by_family[fam]["|".join(r["worse_candidate_names"]) or "none"] += 1
        neutral_combo_by_family[fam]["|".join(r["neutral_candidate_names"]) or "none"] += 1
        for c in r["candidates"]:
            if c["class_vs_old"] != "worse":
                continue
            key = f"{fam}:{c['name']}"
            for b in c.get("new_short_blocks_first10", []):
                new_short_by_candidate[key][b["symbolic_block"]] += 1
    return {
        "records": len(rows),
        "records_by_family": dict(records_by_family.most_common()),
        "all_three_worse": dict(all_three.most_common()),
        "worse_combo_by_family": {k: dict(v.most_common()) for k, v in worse_combo_by_family.items()},
        "neutral_combo_by_family": {k: dict(v.most_common()) for k, v in neutral_combo_by_family.items()},
        "new_short_blocks_by_worse_candidate": {k: dict(v.most_common(20)) for k, v in new_short_by_candidate.items()},
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--analysis", nargs="+", required=True)
    ap.add_argument("--equations", nargs="+", required=True)
    ap.add_argument("--out", default="-")
    ap.add_argument("--summary-out", default=None)
    args = ap.parse_args()

    analysis = load_index(args.analysis)
    rows = []
    for name in args.equations:
        for eq in iter_jsonl(Path(name)):
            if eq.get("reduced_family") not in TARGET_FAMILIES:
                continue
            key = (int(eq.get("p")), int(eq.get("record_index")))
            rec = analysis.get(key)
            if rec is None:
                continue
            row = analyze_record(rec, eq)
            if row is not None:
                rows.append(row)

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
