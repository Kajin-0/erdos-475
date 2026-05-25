#!/usr/bin/env python3
"""
Test the equal-sum exchange exposed by one-sided long terminal bridges.

Input is a JSONL log produced by scripts/test_external_bridge_overlap.py, usually
filtered to hard records with no CLEAN_DESCENT, for example:

    logs/external_bridge_hard_terminal_lengths_p17.jsonl

This script focuses first on the right-sided orientation:

    R = X A z_m q B Y_r
    Z = A z_m
    z_m + sum(B) = 0
    sum(A) = sum(B)

where B is the terminal right external support.  It tests the equal-sum exchange

    A z_m q B  ->  B z_m q A

and compares D_short before/after.

This is diagnostic infrastructure for the S18 one-sided long terminal attack.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Sequence, Tuple

INF = 10**9


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


def defect_short(p: int, order: Sequence[int]) -> Tuple[int, int, int, Tuple[int, ...]]:
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


def flags(record: dict[str, Any]) -> Counter[str]:
    return Counter(record.get("attempt_flag_counts", {}))


def is_right_one_sided_long(record: dict[str, Any]) -> bool:
    f = flags(record)
    return (
        f.get("RIGHT_TERMINAL_BRIDGE", 0) > 0
        and f.get("LEFT_TERMINAL_BRIDGE", 0) == 0
        and f.get("LONG_TERMINAL_BRIDGE", 0) > 0
    )


def right_long_terminal_candidates(record: dict[str, Any]) -> list[dict[str, Any]]:
    """Return candidate exchange moves from right terminal metadata.

    Candidate contains enough indices to perform:

        A z_m q B -> B z_m q A

    with A = order[z_i:z_j-1], z_m = order[z_j-1], q=order[z_j],
    B = order[z_j+1:external_index].
    """
    out: list[dict[str, Any]] = []
    order = record["order"]
    p = int(record["p"])
    for interval in record.get("interval_records", []):
        z_i = int(interval["i"])
        z_j = int(interval["j"])
        m = int(interval["length"])
        rq = interval.get("right_q")
        if not rq:
            continue
        for attempt in rq.get("attempts", []):
            if "RIGHT_TERMINAL_BRIDGE" not in attempt.get("branch_flags", []):
                continue
            for bridge in attempt.get("external", []):
                if bridge.get("b") != m - 1:
                    continue
                for meta in bridge.get("terminal_support", []) or []:
                    if meta.get("side") != "right":
                        continue
                    if not meta.get("long_terminal"):
                        continue
                    ext_index = int(meta["external_index"])
                    support_length = int(meta["support_length"])
                    if support_length <= 0:
                        continue
                    # Need A nonempty and B nonempty; m>=3 from previous logs, but validate anyway.
                    if z_j - z_i < 3:
                        continue
                    if ext_index <= z_j + 1 or ext_index > len(order):
                        continue
                    A = order[z_i : z_j - 1]
                    z_m = order[z_j - 1]
                    q = order[z_j]
                    B = order[z_j + 1 : ext_index]
                    if not A or not B:
                        continue
                    if sum(A) % p != sum(B) % p:
                        # If this fails, metadata or indexing is wrong; keep a diagnostic candidate.
                        valid_equal_sum = False
                    else:
                        valid_equal_sum = True
                    out.append(
                        {
                            "z_i": z_i,
                            "z_j": z_j,
                            "m": m,
                            "k": attempt.get("k"),
                            "external_index": ext_index,
                            "support_length": support_length,
                            "terminal_total_length": meta.get("terminal_total_length"),
                            "A": A,
                            "z_m": z_m,
                            "q": q,
                            "B": B,
                            "valid_equal_sum": valid_equal_sum,
                        }
                    )
    return out


def apply_right_exchange(order: Sequence[int], cand: dict[str, Any]) -> tuple[int, ...]:
    z_i = cand["z_i"]
    z_j = cand["z_j"]
    ext = cand["external_index"]
    A = tuple(cand["A"])
    z_m = (cand["z_m"],)
    q = (cand["q"],)
    B = tuple(cand["B"])
    return tuple(order[:z_i]) + B + z_m + q + A + tuple(order[ext:])


def classify_exchange(oldD: tuple, newD: tuple, cand: dict[str, Any]) -> str:
    if not cand.get("valid_equal_sum"):
        return "bad_indexing"
    if newD < oldD:
        return "improved"
    if newD == oldD:
        return "neutral"
    return "worse"


def analyze_record(record: dict[str, Any], *, max_candidates: int) -> dict[str, Any] | None:
    if not is_right_one_sided_long(record):
        return None
    p = int(record["p"])
    order = tuple(int(x) for x in record["order"])
    oldD = defect_short(p, order)
    cands = right_long_terminal_candidates(record)
    results = []
    for cand in cands[:max_candidates]:
        new_order = apply_right_exchange(order, cand)
        newD = defect_short(p, new_order)
        results.append(
            {
                "candidate": cand,
                "old_defect": oldD,
                "new_defect": newD,
                "class": classify_exchange(oldD, newD, cand),
                "new_order": list(new_order),
                "new_zero_intervals_first10": [list(z) for z in zero_intervals(p, new_order)[:10]],
            }
        )
    if not results:
        return None
    return {
        "p": p,
        "S": record.get("S"),
        "sigma": record.get("sigma"),
        "order": list(order),
        "defect": oldD,
        "attempt_flag_counts": record.get("attempt_flag_counts", {}),
        "results": results,
        "result_counts": dict(Counter(r["class"] for r in results)),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("jsonl", nargs="+", help="Input external-bridge hard JSONL logs.")
    ap.add_argument("--out", default="-", help="Output JSONL path, or '-' for stdout.")
    ap.add_argument("--max-candidates", type=int, default=20)
    args = ap.parse_args()

    records_out = []
    input_records = 0
    eligible_records = 0
    aggregate = Counter()

    for name in args.jsonl:
        for rec in iter_jsonl(Path(name)):
            input_records += 1
            analyzed = analyze_record(rec, max_candidates=args.max_candidates)
            if analyzed is None:
                continue
            eligible_records += 1
            aggregate.update(analyzed["result_counts"])
            records_out.append(analyzed)

    if args.out == "-":
        for rec in records_out:
            print(json.dumps(rec, separators=(",", ":")))
    else:
        with Path(args.out).open("w", encoding="utf-8") as fh:
            for rec in records_out:
                fh.write(json.dumps(rec, separators=(",", ":")) + "\n")

    print(f"input_records={input_records}")
    print(f"eligible_right_one_sided_long_records={eligible_records}")
    print("aggregate=" + json.dumps(dict(aggregate), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
