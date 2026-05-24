#!/usr/bin/env python3
"""Extract minimal final witness certificates from repair trace JSONL files.

The output is intentionally small:

    {"p": 29, "B": [...], "final_order": [...], "source": "..."}

The extractor is schema-tolerant because historical trace files may use different
field names.  The verifier, not this extractor, is the trusted kernel.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable


def as_int_list(value: Any) -> list[int] | None:
    if value is None:
        return None
    if isinstance(value, list):
        try:
            return [int(x) for x in value]
        except (TypeError, ValueError):
            return None
    return None


def deep_get(obj: dict[str, Any], paths: Iterable[tuple[str, ...]]) -> Any:
    for path in paths:
        cur: Any = obj
        ok = True
        for key in path:
            if not isinstance(cur, dict) or key not in cur:
                ok = False
                break
            cur = cur[key]
        if ok:
            return cur
    return None


def extract_record(raw: dict[str, Any], source: str, line_no: int) -> dict[str, Any] | None:
    p = deep_get(raw, [
        ("p",),
        ("prime",),
        ("metadata", "p"),
        ("instance", "p"),
    ])
    B = deep_get(raw, [
        ("B",),
        ("b_set",),
        ("complement",),
        ("metadata", "B"),
        ("instance", "B"),
    ])
    final_order = deep_get(raw, [
        ("final_order",),
        ("witness",),
        ("ordering",),
        ("final", "order"),
        ("result", "final_order"),
    ])

    try:
        p_int = int(p)
    except (TypeError, ValueError):
        return None

    B_list = as_int_list(B)
    order_list = as_int_list(final_order)
    if B_list is None or order_list is None:
        return None

    return {
        "p": p_int,
        "B": sorted(B_list),
        "final_order": order_list,
        "source": source,
        "source_line": line_no,
    }


def key_of(record: dict[str, Any]) -> tuple[int, tuple[int, ...]]:
    return int(record["p"]), tuple(int(x) for x in record["B"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trace", action="append", required=True, help="Trace JSONL file. May be passed multiple times.")
    parser.add_argument("--out", required=True, help="Output minimal witness JSONL file.")
    parser.add_argument("--strict", action="store_true", help="Fail if no witness records are extracted.")
    args = parser.parse_args()

    records: dict[tuple[int, tuple[int, ...]], dict[str, Any]] = {}
    scanned = 0
    extracted = 0

    for trace_name in args.trace:
        path = Path(trace_name)
        if not path.exists():
            raise FileNotFoundError(f"trace file not found: {path}")
        with path.open("r", encoding="utf-8") as fh:
            for line_no, line in enumerate(fh, start=1):
                line = line.strip()
                if not line:
                    continue
                scanned += 1
                try:
                    raw = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"invalid JSON in {path}:{line_no}: {exc}") from exc
                rec = extract_record(raw, str(path), line_no)
                if rec is None:
                    continue
                extracted += 1
                records.setdefault(key_of(rec), rec)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as fh:
        for rec in sorted(records.values(), key=key_of):
            fh.write(json.dumps(rec, sort_keys=True, separators=(",", ":")) + "\n")

    print(f"scanned_records={scanned}")
    print(f"extracted_records={extracted}")
    print(f"unique_witnesses={len(records)}")
    print(f"output={out_path}")

    if args.strict and not records:
        raise SystemExit("no witness records extracted")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
