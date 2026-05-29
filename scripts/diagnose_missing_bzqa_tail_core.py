#!/usr/bin/env python3
"""
Diagnose pure_worse_only records where extract_bzqa_tail_core_equations.py fails.

Input is produced by:

    scripts/analyze_pure_m3_terminal_structure.py

Typical input:

    logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl

The script prints only missing records under the B z q A extractor logic and all
symbolic non-tautological zero blocks for the target permutation.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

TOKEN_RE = re.compile(r"^([A-Z]+|z|q)(\d+)?$")
TARGET_PERM = "B z q A"


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


def parse_token(tok: str) -> tuple[str, int | None]:
    m = TOKEN_RE.match(tok)
    if not m:
        return (tok, None)
    base, idx = m.group(1), m.group(2)
    return (base, int(idx) if idx is not None else None)


def symbolic_labels(record: dict[str, Any], cand: dict[str, Any]) -> dict[int, list[str]]:
    order = [int(x) for x in record.get("order", [])]
    z_i = int(cand.get("z_i", 0))
    ext = int(cand.get("external_index", len(order)))
    A = [int(x) for x in cand.get("A", [])]
    B = [int(x) for x in cand.get("B", [])]
    z = int(cand.get("z"))
    q = int(cand.get("q"))
    out: dict[int, list[str]] = defaultdict(list)
    for idx, value in enumerate(order[:z_i]):
        out[int(value)].append(f"X{idx+1}")
    for idx, value in enumerate(A):
        out[int(value)].append(f"A{idx+1}")
    out[z].append("z")
    out[q].append("q")
    for idx, value in enumerate(B):
        out[int(value)].append(f"B{idx+1}")
    for idx, value in enumerate(order[ext:]):
        out[int(value)].append(f"Y{idx+1}")
    return out


def symbolic_block(block: list[int], labels: dict[int, list[str]]) -> str:
    return " ".join("/".join(labels.get(int(v), [f"?{v}"])) for v in block)


def token_bases(tokens: list[str]) -> list[str]:
    return [parse_token(t)[0] for t in tokens]


def is_tautological(tokens: list[str]) -> bool:
    if set(tokens) == {"A1", "A2", "z"} and len(tokens) == 3:
        return True
    if "z" in tokens and all(t == "z" or t.startswith("B") for t in tokens):
        return True
    return False


def is_tail_core(tokens: list[str]) -> bool:
    bases = set(token_bases(tokens))
    return {"B", "z", "q", "A"}.issubset(bases) and not is_tautological(tokens)


def rough_reason(tokens: list[str]) -> str:
    bases = set(token_bases(tokens))
    missing = sorted({"B", "z", "q", "A"} - bases)
    if is_tautological(tokens):
        return "tautological"
    if missing:
        return "missing_" + "_".join(missing)
    return "tail_core_present"


def reduced_tokens(tokens: list[str]) -> list[str]:
    removed_z = False
    out = []
    for t in tokens:
        if t in {"A1", "A2"}:
            continue
        if t == "z" and not removed_z:
            removed_z = True
            continue
        out.append(t)
    return out


def extract_tail_core(record: dict[str, Any]) -> dict[str, Any] | None:
    for ca in record.get("candidate_analyses", []):
        cand = ca.get("candidate", {})
        labels = symbolic_labels(record, cand)
        for ma in ca.get("moves_analyzed", []):
            if ma.get("perm_key") != TARGET_PERM:
                continue
            for zint in ma.get("new_zero_intervals", []) or []:
                sym = symbolic_block(zint.get("block", []), labels)
                toks = sym.split()
                if is_tail_core(toks):
                    return {"symbolic_equation": sym, "reduced_equation": " ".join(reduced_tokens(toks))}
    return None


def diagnose_record(record: dict[str, Any]) -> dict[str, Any] | None:
    if record.get("pure_label") != "pure_worse_only":
        return None
    if extract_tail_core(record) is not None:
        return None

    blocks = []
    reason_counts = Counter()
    for ca in record.get("candidate_analyses", []):
        cand = ca.get("candidate", {})
        labels = symbolic_labels(record, cand)
        for ma in ca.get("moves_analyzed", []):
            if ma.get("perm_key") != TARGET_PERM:
                continue
            for zint in ma.get("new_zero_intervals", []) or []:
                sym = symbolic_block(zint.get("block", []), labels)
                toks = sym.split()
                if is_tautological(toks):
                    continue
                reason = rough_reason(toks)
                reason_counts[reason] += 1
                blocks.append(
                    {
                        "symbolic_block": sym,
                        "numeric_block": zint.get("block"),
                        "reason": reason,
                        "signature": f"{zint.get('left_label') or 'ext'}={zint.get('right_label') or 'ext'}:L{zint.get('length')}:{zint.get('span_type')}",
                    }
                )
    first_cand = (record.get("candidate_analyses") or [{}])[0].get("candidate", {})
    return {
        "record_index": record.get("record_index"),
        "p": record.get("p"),
        "order": record.get("order"),
        "candidate": {
            "support_length": first_cand.get("support_length"),
            "A": first_cand.get("A"),
            "z": first_cand.get("z"),
            "q": first_cand.get("q"),
            "B": first_cand.get("B"),
            "X_length": first_cand.get("X_length"),
            "Y_length": first_cand.get("Y_length"),
        },
        "reason_counts": dict(reason_counts.most_common()),
        "nontautological_blocks": blocks,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input analyzed pure m3 structure JSONL files.")
    ap.add_argument("--out", default="-", help="Output JSONL path, or '-' for stdout.")
    ap.add_argument("--summary-out", default=None, help="Optional summary JSON path.")
    args = ap.parse_args()

    missing = []
    pure_worse = 0
    for name in args.jsonl:
        for rec in iter_jsonl(Path(name)):
            if rec.get("pure_label") != "pure_worse_only":
                continue
            pure_worse += 1
            diag = diagnose_record(rec)
            if diag is not None:
                missing.append(diag)

    if args.out == "-":
        for row in missing:
            print(json.dumps(row, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for row in missing:
                fh.write(json.dumps(row, separators=(",", ":")) + "\n")

    summary = {
        "pure_worse_records": pure_worse,
        "missing_tail_core_records": len(missing),
        "missing_record_indices": [x.get("record_index") for x in missing],
        "reason_counts": dict(Counter(r for m in missing for r, c in m.get("reason_counts", {}).items() for _ in range(c)).most_common()),
    }
    print("summary=" + json.dumps(summary, sort_keys=True))
    if args.summary_out:
        Path(args.summary_out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
