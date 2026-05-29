#!/usr/bin/env python3
"""
Extract representative examples for zero-sum Bq/BqY route labels.

Detailed route JSONL rows contain:

    best_class = worse
    route_label_counts = {CLEAN_DESCENT: ..., EXTERNAL_BRIDGE: ..., ...}

Therefore examples are expanded by the keys of route_label_counts.  The old
best_class field is retained only as bridge_class metadata.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Sequence

ZERO_SUM_FAMILIES = {"B_tail+q", "B_tail+q+Y_prefix"}
TARGET = {
    "B_tail+q": "Bq_zero",
    "B_tail+q+Y_prefix": "BqY_zero",
}
ROUTE_LABEL_KEYS = ["route_label_counts", "route_class_counts", "attempt_label_counts", "attempt_flag_counts"]


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
        p = Path(name)
        if not p.exists():
            continue
        for rec in iter_jsonl(p):
            if "p" in rec and "record_index" in rec:
                out[(int(rec["p"]), int(rec["record_index"]))] = rec
    return out


def first(row: dict[str, Any], keys: Sequence[str], default: Any = None) -> Any:
    for k in keys:
        if k in row and row[k] not in (None, ""):
            return row[k]
    return default


def family_of(row: dict[str, Any], eq: dict[str, Any] | None = None) -> str | None:
    fam = first(row, ["family", "reduced_family", "target_family", "source_family"])
    if fam:
        return str(fam)
    if eq:
        fam = eq.get("reduced_family")
        if fam:
            return str(fam)
    return None


def route_label_counts(row: dict[str, Any]) -> dict[str, int]:
    for key in ROUTE_LABEL_KEYS:
        counts = row.get(key)
        if isinstance(counts, dict) and counts:
            return {str(k): int(v) for k, v in counts.items()}
    direct = first(row, ["route_label", "route_class", "label", "result_class", "best_route_label"])
    if direct:
        return {str(direct): 1}
    return {}


def split_original(record: dict[str, Any], eq: dict[str, Any]) -> dict[str, list[int]] | None:
    order = [int(x) for x in record.get("order", [])]
    A = [int(x) for x in eq.get("A", [])]
    z = int(eq["z"])
    q = int(eq["q"])
    B = [int(x) for x in eq.get("B", [])]
    pattern = A + [z, q] + B
    for start in range(0, len(order) - len(pattern) + 1):
        if order[start:start + len(pattern)] == pattern:
            end = start + len(pattern)
            return {"X": order[:start], "A": A, "z": [z], "q": [q], "B": B, "Y": order[end:]}
    return None


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


def active_symbolic(record: dict[str, Any], eq: dict[str, Any] | None) -> str | None:
    if not eq or not record:
        return None
    parts = split_original(record, eq)
    if parts is None:
        return None
    lab = labels(parts, eq)
    return sym(parts["A"] + parts["z"] + parts["q"] + parts["B"], lab)


def extract_witness(row: dict[str, Any]) -> dict[str, Any]:
    keys = [
        "hidden_equation",
        "useful_route_flags",
        "route_flag_counts",
        "route_label_counts",
        "move_routes",
        "route_witness",
        "witness",
        "best_witness",
        "zero_interval",
        "interval",
        "route_detail",
        "details",
        "partial_sum_equality",
        "equality",
        "new_zero_block",
        "symbolic_block",
    ]
    out = {}
    for k in keys:
        if k in row:
            out[k] = row[k]
    return out


def row_examples(row: dict[str, Any], analysis: dict[tuple[int, int], dict[str, Any]], equations: dict[tuple[int, int], dict[str, Any]]) -> list[dict[str, Any]]:
    # Some route rows may contain per-candidate arrays.  Flatten common containers.
    containers = ["routes", "results", "examples", "records"]
    for key in containers:
        val = row.get(key)
        if isinstance(val, list) and val and all(isinstance(x, dict) for x in val):
            out = []
            for sub in val:
                merged = dict(row)
                merged.pop(key, None)
                merged.update(sub)
                out.extend(row_examples(merged, analysis, equations))
            return out

    p = first(row, ["p", "prime"])
    record_index = first(row, ["record_index", "index", "record", "rid"])
    if p is None or record_index is None:
        return []
    key = (int(p), int(record_index))
    rec = analysis.get(key, {})
    eq = equations.get(key, {})
    fam = family_of(row, eq)
    if fam not in ZERO_SUM_FAMILIES:
        return []
    counts = route_label_counts(row)
    if not counts:
        return []

    bridge_class = str(row.get("best_class", "-"))
    base = {
        "p": int(p),
        "record_index": int(record_index),
        "family": fam,
        "target": TARGET.get(fam, "-"),
        "bridge_class": bridge_class,
        "reduced_equation": eq.get("reduced_equation") or row.get("reduced_equation"),
        "active_symbolic_order": active_symbolic(rec, eq),
        "witness": extract_witness(row),
    }
    out = []
    for label, count in counts.items():
        ex = dict(base)
        ex["route_label"] = label
        ex["route_label_count"] = count
        out.append(ex)
    return out


def summarize(rows: list[dict[str, Any]], missing: list[str], unmatched: int) -> dict[str, Any]:
    return {
        "examples_found": len(rows),
        "examples_by_family": dict(Counter(r["family"] for r in rows).most_common()),
        "examples_by_route_label": dict(Counter(r["route_label"] for r in rows).most_common()),
        "examples_by_family_route": dict(Counter(f"{r['family']}::{r['route_label']}" for r in rows).most_common()),
        "missing_route_jsonl_files": missing,
        "unmatched_route_rows": unmatched,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--analysis", nargs="+", required=True)
    ap.add_argument("--equations", nargs="+", required=True)
    ap.add_argument("--route-jsonl", nargs="+", required=True)
    ap.add_argument("--max-per-family-label", type=int, default=3)
    ap.add_argument("--out", default="-")
    ap.add_argument("--summary-out", default=None)
    args = ap.parse_args()

    analysis = load_index(args.analysis)
    equations = load_index(args.equations)
    missing = [name for name in args.route_jsonl if not Path(name).exists()]
    rows: list[dict[str, Any]] = []
    unmatched = 0
    seen_bucket: Counter[str] = Counter()

    for name in args.route_jsonl:
        path = Path(name)
        if not path.exists():
            continue
        for row in iter_jsonl(path):
            exs = row_examples(row, analysis, equations)
            if not exs:
                unmatched += 1
                continue
            for ex in exs:
                bucket = f"{ex['family']}::{ex['route_label']}"
                if seen_bucket[bucket] >= args.max_per_family_label:
                    continue
                seen_bucket[bucket] += 1
                rows.append(ex)

    if args.out == "-":
        for r in rows:
            print(json.dumps(r, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, separators=(",", ":")) + "\n")

    summary = summarize(rows, missing, unmatched)
    print("summary=" + json.dumps(summary, sort_keys=True))
    if args.summary_out:
        Path(args.summary_out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
