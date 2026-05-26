#!/usr/bin/env python3
"""
Route Bq/BqY secondary obstructions through existing external-bridge classifier logic.

Input is produced by:

    scripts/test_hidden_support_bridge_moves.py

Typical use:

    python3 scripts/route_bq_bqy_obstructions.py \
      logs/hidden_support_bridge_moves_p17_v5.jsonl \
      --out logs/route_bq_bqy_obstructions_p17.jsonl \
      --summary-out logs/summary_route_bq_bqy_obstructions_p17.json

This script focuses on the zero-sum hidden-support families:

    B_tail+q
    B_tail+q+Y_prefix

For each record, it takes best bridge-move orders and runs the same q-insertion
classifier logic used by scripts/test_external_bridge_overlap.py.  The goal is
to see whether Bq/BqY secondary obstructions are already routed to:

    SIGNED_INTERVAL
    DISTRIBUTED_BRIDGE
    EXTERNAL_BRIDGE
    terminal bridge flags
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Sequence, Tuple

INF = 10**9
TARGET_FAMILIES = {"B_tail+q", "B_tail+q+Y_prefix"}
ROUTE_FLAGS = {
    "CLEAN_DESCENT",
    "SIGNED_INTERVAL",
    "DISTRIBUTED_BRIDGE",
    "EXTERNAL_BRIDGE",
    "RIGHT_TERMINAL_BRIDGE",
    "LEFT_TERMINAL_BRIDGE",
    "MIXED_TERMINAL_BRIDGE",
    "SHORT_TERMINAL_BRIDGE",
    "LONG_TERMINAL_BRIDGE",
}
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
    out = []
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


def prefix_sums_block(p: int, block: Sequence[int]) -> list[int]:
    s = 0
    out = [0]
    for x in block:
        s = (s + int(x)) % p
        out.append(s)
    return out


def insert_atom(order: Sequence[int], src: int, dst_before: int) -> tuple[int, ...]:
    arr = list(order)
    q = arr.pop(src)
    if src < dst_before:
        dst_before -= 1
    arr.insert(dst_before, q)
    return tuple(arr)


def external_indices_for_window(n_atoms: int, z_i: int, z_j: int, q_index: int) -> set[int]:
    local = set(range(z_i, z_j + 1))
    local.add(q_index + 1)
    return set(range(n_atoms + 1)) - local


def terminal_support_metadata(*, m: int, q_index: int, z_i: int, ext_index: int, side: str) -> dict[str, Any]:
    if side == "right":
        support_len = ext_index - (q_index + 1)
    elif side == "left":
        support_len = z_i - ext_index
    else:
        support_len = None
    if support_len is None or support_len <= 0:
        return {
            "external_index": ext_index,
            "side": side,
            "support_length": support_len,
            "terminal_total_length": None,
            "short_terminal": False,
            "long_terminal": False,
            "valid_support_length": False,
        }
    terminal_total = 1 + support_len
    return {
        "external_index": ext_index,
        "side": side,
        "support_length": support_len,
        "terminal_total_length": terminal_total,
        "short_terminal": terminal_total < m,
        "long_terminal": terminal_total >= m,
        "valid_support_length": True,
    }


def classify_right_insertion(p: int, order: Sequence[int], z_i: int, z_j: int, k: int) -> dict[str, Any]:
    n = len(order)
    m = z_j - z_i
    q_index = z_j
    q = int(order[q_index])
    Z = order[z_i:z_j]
    T = prefix_sums_block(p, Z)
    P = partial_sums_extended(p, order)
    base = P[z_i]

    new_order = insert_atom(order, q_index, z_i + k)
    oldD = defect_short(p, order)
    newD = defect_short(p, new_order)

    signed = []
    external = []
    ext_indices = external_indices_for_window(n, z_i, z_j, q_index)
    ext_value_to_indices: dict[int, list[int]] = defaultdict(list)
    for idx in ext_indices:
        ext_value_to_indices[P[idx]].append(idx)

    for a in range(0, k + 1):
        for b in range(k, m):
            if T[a] % p == (q + T[b]) % p:
                signed.append({"a": a, "b": b, "value": (base + T[a]) % p})

    for b in range(k, m):
        val = (base + q + T[b]) % p
        if val in ext_value_to_indices:
            side_counts = Counter("left" if idx < z_i else "right" for idx in ext_value_to_indices[val])
            bridge = {"b": b, "value": val, "indices": ext_value_to_indices[val], "side_counts": dict(side_counts)}
            if b == m - 1:
                terminal_meta = []
                for idx in ext_value_to_indices[val]:
                    side = "left" if idx < z_i else "right"
                    terminal_meta.append(terminal_support_metadata(m=m, q_index=q_index, z_i=z_i, ext_index=idx, side=side))
                bridge["terminal_support"] = terminal_meta
                bridge["short_terminal"] = any(x["short_terminal"] for x in terminal_meta)
                bridge["long_terminal"] = any(x["long_terminal"] for x in terminal_meta)
            external.append(bridge)

    bset = sorted({e["b"] for e in external})
    terminal = [e for e in external if e["b"] == m - 1]
    nonterminal = [e for e in external if e["b"] != m - 1]

    branch_flags = []
    if newD < oldD:
        branch_flags.append("CLEAN_DESCENT")
    if signed:
        branch_flags.append("SIGNED_INTERVAL")
    if len(bset) >= 2:
        branch_flags.append("DISTRIBUTED_BRIDGE")
    elif nonterminal:
        branch_flags.append("EXTERNAL_BRIDGE")
    elif terminal:
        side_counts = Counter()
        short_terminal = False
        long_terminal = False
        for e in terminal:
            side_counts.update(e["side_counts"])
            short_terminal = short_terminal or bool(e.get("short_terminal"))
            long_terminal = long_terminal or bool(e.get("long_terminal"))
        if side_counts.get("right", 0) and not side_counts.get("left", 0):
            branch_flags.append("RIGHT_TERMINAL_BRIDGE")
        elif side_counts.get("left", 0) and not side_counts.get("right", 0):
            branch_flags.append("LEFT_TERMINAL_BRIDGE")
        else:
            branch_flags.append("MIXED_TERMINAL_BRIDGE")
        if short_terminal:
            branch_flags.append("SHORT_TERMINAL_BRIDGE")
        if long_terminal:
            branch_flags.append("LONG_TERMINAL_BRIDGE")

    if not branch_flags:
        if newD == oldD:
            branch_flags.append("CLEAN_NO_DESCENT")
        else:
            branch_flags.append("WORSE_UNCLASSIFIED")

    if "CLEAN_DESCENT" in branch_flags and len(branch_flags) == 1:
        label = "CLEAN_DESCENT"
    elif len(branch_flags) == 1:
        label = branch_flags[0]
    else:
        label = "MIXED"

    return {
        "side": "right",
        "k": k,
        "q": q,
        "old_defect": list(oldD),
        "new_defect": list(newD),
        "label": label,
        "branch_flags": branch_flags,
        "signed": signed,
        "external": external,
        "bridge_indices": bset,
        "new_order": list(new_order),
    }


def classify_left_by_reversal(p: int, order: Sequence[int], z_i: int, z_j: int, k: int) -> dict[str, Any]:
    n = len(order)
    rev = tuple(reversed(order))
    rz_i = n - z_j
    rz_j = n - z_i
    rec = classify_right_insertion(p, rev, rz_i, rz_j, k)
    rec["side"] = "left_via_reversal"
    rec["new_order_reversed_back"] = list(reversed(rec["new_order"]))
    return rec


def analyze_order_with_external_classifier(p: int, order: Sequence[int], max_intervals: int = 6) -> dict[str, Any] | None:
    zis = zero_intervals(p, order)
    if not zis:
        return None
    L_min = min(length for _, _, length in zis)
    active_intervals = [(i, j, length) for i, j, length in zis if length == L_min]
    attempts = []
    for z_i, z_j, m in active_intervals[:max_intervals]:
        if m < 2:
            continue
        if z_j < len(order):
            attempts.extend(classify_right_insertion(p, order, z_i, z_j, k) for k in range(1, m))
        if z_i > 0:
            attempts.extend(classify_left_by_reversal(p, order, z_i, z_j, k) for k in range(1, m))
    if not attempts:
        return None
    return {
        "active_shortest_length": L_min,
        "attempt_label_counts": dict(Counter(a["label"] for a in attempts)),
        "attempt_flag_counts": dict(Counter(flag for a in attempts for flag in a["branch_flags"])),
        "attempts_first10": attempts[:10],
    }


def best_moves(row: dict[str, Any]) -> list[dict[str, Any]]:
    moves = row.get("results", []) or []
    if not moves:
        return []
    best = min(CLASS_RANK.get(m.get("class", "none"), 99) for m in moves)
    return [m for m in moves if CLASS_RANK.get(m.get("class", "none"), 99) == best]


def route_record(row: dict[str, Any]) -> dict[str, Any]:
    p = int(row["p"])
    family = row.get("reduced_family")
    move_routes = []
    route_flags = Counter()
    route_labels = Counter()
    for move in best_moves(row):
        new_order = [int(x) for x in move.get("new_order", [])]
        if not new_order:
            continue
        routed = analyze_order_with_external_classifier(p, new_order)
        if routed is None:
            move_routes.append({"move": move.get("move"), "bridge_class": move.get("class"), "routed": False})
            continue
        flags = routed.get("attempt_flag_counts", {})
        labels = routed.get("attempt_label_counts", {})
        route_flags.update(flags)
        route_labels.update(labels)
        move_routes.append(
            {
                "move": move.get("move"),
                "bridge_class": move.get("class"),
                "routed": True,
                "attempt_flag_counts": flags,
                "attempt_label_counts": labels,
                "active_shortest_length": routed.get("active_shortest_length"),
                "attempts_first5": routed.get("attempts_first10", [])[:5],
            }
        )
    useful_flags = sorted(set(route_flags) & ROUTE_FLAGS)
    return {
        "p": p,
        "record_index": row.get("record_index"),
        "reduced_family": family,
        "hidden_equation": row.get("hidden_equation", {}).get("reduced_equation"),
        "best_class": row.get("best_class"),
        "route_success": bool(useful_flags),
        "useful_route_flags": useful_flags,
        "route_flag_counts": dict(route_flags.most_common()),
        "route_label_counts": dict(route_labels.most_common()),
        "move_routes": move_routes,
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    records_by_family = Counter(r.get("reduced_family") for r in rows)
    success_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    flags_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    labels_by_family: dict[str, Counter[str]] = defaultdict(Counter)
    for r in rows:
        fam = r.get("reduced_family")
        success_by_family[fam]["yes" if r.get("route_success") else "no"] += 1
        flags_by_family[fam].update(r.get("route_flag_counts", {}))
        labels_by_family[fam].update(r.get("route_label_counts", {}))
    return {
        "records": len(rows),
        "records_by_family": dict(records_by_family.most_common()),
        "route_success_by_family": {k: dict(v.most_common()) for k, v in success_by_family.items()},
        "route_flags_by_family": {k: dict(v.most_common()) for k, v in flags_by_family.items()},
        "route_labels_by_family": {k: dict(v.most_common()) for k, v in labels_by_family.items()},
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Bridge move JSONL files from test_hidden_support_bridge_moves.py")
    ap.add_argument("--out", default="-", help="Output JSONL path, or '-' for stdout")
    ap.add_argument("--summary-out", default=None, help="Optional summary JSON path")
    args = ap.parse_args()

    rows = []
    for name in args.jsonl:
        for row in iter_jsonl(Path(name)):
            if row.get("reduced_family") not in TARGET_FAMILIES:
                continue
            rows.append(route_record(row))

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
