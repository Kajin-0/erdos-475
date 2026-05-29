#!/usr/bin/env python3
"""
Taxonomize fallback q_T_P_M zero intervals for equality primary-failure rows.

This script rebuilds old, primary, and fallback localizations for equality records:

    old:      A z q P T M
    primary:  A z P q T M
    fallback: A z q T P M

It selects rows where primary is D_short-worse, then classifies every fallback
zero interval by the local q|T|P|M zones and marks whether the symbolic block
already appears in the old order.
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
    for i in range(0, len(xs) - len(pat) + 1):
        if list(xs[i:i + len(pat)]) == list(pat):
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
    return {"X": order[:start], "A": A, "z": [z], "q": [q], "B": B, "Y": order[end:]}


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


def build_orders(parts: dict[str, list[int]], eq: dict[str, Any]) -> tuple[dict[str, list[int]], dict[str, str]]:
    P, T, M = split_B(eq)
    X, A, z, q, Y = parts["X"], parts["A"], parts["z"], parts["q"], parts["Y"]
    orders = {
        "old": X + A + z + q + P + T + M + Y,
        "primary": X + A + z + P + q + T + M + Y,
        "fallback": X + A + z + q + T + P + M + Y,
    }
    zone_by_value: dict[str, str] = {}
    for x in q:
        zone_by_value[str(int(x))] = "q"
    for x in T:
        zone_by_value[str(int(x))] = "T"
    for x in P:
        zone_by_value[str(int(x))] = "P"
    for x in M:
        zone_by_value[str(int(x))] = "M"
    for x in A:
        zone_by_value[str(int(x))] = "A"
    for x in z:
        zone_by_value[str(int(x))] = "z"
    for x in X:
        zone_by_value[str(int(x))] = "X"
    for x in Y:
        zone_by_value[str(int(x))] = "Y"
    return orders, zone_by_value


def classify_zones(block: Sequence[int], zone_by_value: dict[str, str]) -> str:
    zones = [zone_by_value.get(str(int(x)), "?") for x in block]
    compressed: list[str] = []
    for z in zones:
        if not compressed or compressed[-1] != z:
            compressed.append(z)
    return "+".join(compressed)


def interval_records(p: int, order: Sequence[int], lab: dict[int, list[str]], zone_by_value: dict[str, str]) -> list[dict[str, Any]]:
    out = []
    for i, j, length in zero_intervals(p, order):
        block = list(order[i:j])
        out.append({
            "interval": [i, j, length],
            "length": length,
            "symbolic_block": sym(block, lab),
            "numeric_block": block,
            "zone_class": classify_zones(block, zone_by_value),
        })
    out.sort(key=lambda b: (b["length"], b["zone_class"], b["symbolic_block"]))
    return out


def analyze(rec: dict[str, Any], eq: dict[str, Any]) -> dict[str, Any] | None:
    if eq.get("reduced_family") not in TARGET_FAMILIES:
        return None
    parts = split_original(rec, eq)
    if parts is None:
        return None
    p = int(rec["p"])
    lab = labels(parts, eq)
    orders, zone_by_value = build_orders(parts, eq)
    oldD = defect_short(p, orders["old"])
    primaryD = defect_short(p, orders["primary"])
    fallbackD = defect_short(p, orders["fallback"])
    if not (primaryD > oldD):
        return None
    old_blocks = interval_records(p, orders["old"], lab, zone_by_value)
    primary_blocks = interval_records(p, orders["primary"], lab, zone_by_value)
    fallback_blocks = interval_records(p, orders["fallback"], lab, zone_by_value)
    old_symbols = {b["symbolic_block"] for b in old_blocks}
    fallback_annotated = []
    for b in fallback_blocks:
        bb = dict(b)
        bb["old_or_new"] = "old" if b["symbolic_block"] in old_symbols else "new"
        fallback_annotated.append(bb)
    min_fallback = min((b["length"] for b in fallback_annotated), default=None)
    fallback_new_short = [b for b in fallback_annotated if b["old_or_new"] == "new" and b["length"] == min_fallback]
    return {
        "p": p,
        "record_index": rec.get("record_index"),
        "family": eq.get("reduced_family"),
        "reduced_equation": eq.get("reduced_equation"),
        "old_defect": list(oldD),
        "primary_defect": list(primaryD),
        "fallback_defect": list(fallbackD),
        "old_active_order": sym(orders["old"], lab),
        "primary_active_order": sym(orders["primary"], lab),
        "fallback_active_order": sym(orders["fallback"], lab),
        "primary_new_short_blocks": [b for b in primary_blocks if b["symbolic_block"] not in old_symbols and b["length"] == min(x["length"] for x in primary_blocks)],
        "fallback_zero_intervals": fallback_annotated,
        "fallback_new_intervals": [b for b in fallback_annotated if b["old_or_new"] == "new"],
        "fallback_new_short_blocks": fallback_new_short,
        "fallback_new_short_count": len(fallback_new_short),
        "fallback_zone_histogram": dict(Counter(b["zone_class"] for b in fallback_annotated).most_common()),
        "fallback_new_zone_histogram": dict(Counter(b["zone_class"] for b in fallback_annotated if b["old_or_new"] == "new").most_common()),
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    zone_hist = Counter()
    new_zone_hist = Counter()
    new_short = Counter()
    fallback_defects = Counter()
    for r in rows:
        zone_hist.update(r.get("fallback_zone_histogram", {}))
        new_zone_hist.update(r.get("fallback_new_zone_histogram", {}))
        fallback_defects[str(r.get("fallback_defect", []))] += 1
        for b in r.get("fallback_new_short_blocks", []):
            new_short[b["symbolic_block"]] += 1
    return {
        "primary_failure_rows": len(rows),
        "record_indices": [r.get("record_index") for r in rows],
        "fallback_defect_counts": dict(fallback_defects.most_common()),
        "fallback_new_short_total": sum(r.get("fallback_new_short_count", 0) for r in rows),
        "fallback_new_short_symbols": dict(new_short.most_common()),
        "fallback_zone_histogram": dict(zone_hist.most_common()),
        "fallback_new_zone_histogram": dict(new_zone_hist.most_common()),
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
            key = (int(eq.get("p")), int(eq.get("record_index")))
            rec = analysis.get(key)
            if rec is None:
                continue
            row = analyze(rec, eq)
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
