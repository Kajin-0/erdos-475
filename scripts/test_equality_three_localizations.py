#!/usr/bin/env python3
"""
Test the three symbolic equality localizations from S65/S66.

For equality hidden-support records, write

    B = P T M

where T is the extracted B_tail.  Old active order is

    A z q P T M

with A = A1 A2.  Test the three localizations:

    L1: A z P q T M
    L2: A z q T P M
    L3: A z T q P M

Each candidate places q adjacent to T, so S_tail should become 0.  The question
is whether at least one candidate is D_short-neutral.
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


def symbolic_labels(parts: dict[str, list[int]], eq: dict[str, Any]) -> dict[int, list[str]]:
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


def active_symbolic(order: Sequence[int], labels: dict[int, list[str]]) -> str:
    toks = symbolic_order(order, labels).split()
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


def analyze_record(rec: dict[str, Any], eq: dict[str, Any]) -> dict[str, Any] | None:
    if eq.get("reduced_family") not in TARGET_FAMILIES:
        return None
    parts = split_original(rec, eq)
    if parts is None:
        return None
    P, T, M = split_B(eq)
    p = int(rec["p"])
    labels = symbolic_labels(parts, eq)
    candidates = build_candidates(parts, eq)
    oldD = defect_short(p, candidates["old"])
    U = [int(eq["q"])] + T
    old_gap = span_gap(candidates["old"], U)
    cand_rows = []
    for name, order in candidates.items():
        D = defect_short(p, order)
        gap = span_gap(order, U)
        if name == "old":
            continue
        cand_rows.append(
            {
                "name": name,
                "defect": list(D),
                "class_vs_old": "improved" if D < oldD else ("neutral" if D == oldD else "worse"),
                "q_tail_span_gap": gap,
                "gap_delta": None if old_gap is None or gap is None else gap - old_gap,
                "active_symbolic": active_symbolic(order, labels),
            }
        )
    neutral_zero_gap = [c for c in cand_rows if c["class_vs_old"] == "neutral" and c["q_tail_span_gap"] == 0]
    return {
        "p": p,
        "record_index": rec.get("record_index"),
        "family": eq.get("reduced_family"),
        "reduced_equation": eq.get("reduced_equation"),
        "B_prefix_length": len(P),
        "B_tail_length": len(T),
        "B_suffix_length": len(M),
        "old_defect": list(oldD),
        "old_q_tail_span_gap": old_gap,
        "old_active_symbolic": active_symbolic(candidates["old"], labels),
        "candidates": cand_rows,
        "has_neutral_zero_gap": bool(neutral_zero_gap),
        "neutral_zero_gap_names": [c["name"] for c in neutral_zero_gap],
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    records_by_family = Counter(r["family"] for r in rows)
    success_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    candidate_class_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    neutral_name_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    for r in rows:
        fam = r["family"]
        success_by_family[fam]["yes" if r["has_neutral_zero_gap"] else "no"] += 1
        for c in r["candidates"]:
            candidate_class_by_family[fam][f"{c['name']}:{c['class_vs_old']}"] += 1
        for name in r["neutral_zero_gap_names"]:
            neutral_name_by_family[fam][name] += 1
    return {
        "records": len(rows),
        "records_by_family": dict(records_by_family.most_common()),
        "has_neutral_zero_gap_by_family": {k: dict(v.most_common()) for k, v in success_by_family.items()},
        "candidate_class_by_family": {k: dict(v.most_common()) for k, v in candidate_class_by_family.items()},
        "neutral_zero_gap_name_by_family": {k: dict(v.most_common()) for k, v in neutral_name_by_family.items()},
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
