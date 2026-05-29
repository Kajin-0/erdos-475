#!/usr/bin/env python3
"""
Diagnose zero-sum attempt rows where matched_route_object=true but matched_attempt=false.

Input is produced by scripts/extract_zero_sum_attempt_witnesses.py.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable


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


def compact(value: Any, limit: int = 2000) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        text = value
    else:
        text = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return text if len(text) <= limit else text[: max(0, limit - 3)] + "..."


def analyze(row: dict[str, Any]) -> dict[str, Any] | None:
    if row.get("matched_attempt") is not False:
        return None
    selected_route = row.get("selected_route_compact", "") or ""
    selected_attempt = row.get("selected_attempt_compact", "") or ""
    label = str(row.get("route_label", ""))
    return {
        "family": row.get("family"),
        "target": row.get("target"),
        "route_label": label,
        "p": row.get("p"),
        "record_index": row.get("record_index"),
        "reduced_equation": row.get("reduced_equation"),
        "hidden_equation": row.get("hidden_equation"),
        "branch_flags": row.get("branch_flags"),
        "attempt_label_counts": row.get("attempt_label_counts"),
        "attempt_flag_counts": row.get("attempt_flag_counts"),
        "active_shortest_length": row.get("active_shortest_length"),
        "label_present_in_route_compact": label in selected_route,
        "label_present_in_attempt_compact": label in selected_attempt,
        "selected_attempt_compact": compact(selected_attempt, 2000),
        "selected_route_compact": compact(selected_route, 3000),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input_jsonl")
    ap.add_argument("--out", default="-")
    ap.add_argument("--summary-out", default=None)
    args = ap.parse_args()

    rows = []
    for row in iter_jsonl(Path(args.input_jsonl)):
        out = analyze(row)
        if out is not None:
            rows.append(out)

    if args.out == "-":
        for r in rows:
            print(json.dumps(r, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, separators=(",", ":")) + "\n")

    summary = {
        "unmatched_attempt_rows": len(rows),
        "record_indices": [r.get("record_index") for r in rows],
        "route_labels": sorted(set(str(r.get("route_label")) for r in rows)),
    }
    print("summary=" + json.dumps(summary, sort_keys=True))
    if args.summary_out:
        Path(args.summary_out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
