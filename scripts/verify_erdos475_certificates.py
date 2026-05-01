#!/usr/bin/env python3
"""
Independent certificate verifier for Erdos Problem #475 descent/escape CSVs.

It reloads the original JSONL traces, reconstructs each referenced state,
recomputes Phi=(E,P,L), applies claimed moves/paths, and verifies strict descent.

Supports:
  1) non-atomic descent CSVs from analyze_erdos475_nonatomic_descent.py
  2) one-collision escape CSVs from analyze_erdos475_one_collision_deep_escape.py
  3) atomic instance CSVs from extract_erdos475_atomic_local_certificates.py
  4) optional atomic signature certificate CSV against atomic instances

Example:
  python verify_erdos475_certificates.py \
    --trace-files p29_r3_to_r7_repair_traces_strict.jsonl p31_r3_to_r6_repair_traces_strict.jsonl \
    --nonatomic-csv p29_nonatomic_descent_full.csv p31_nonatomic_descent_full.csv \
    --onecollision-csv p29_one_collision_deep_full.csv p31_one_collision_deep_full.csv \
    --atomic-instances atomic_local_cert_instances.csv \
    --atomic-certs atomic_local_certs.csv \
    --require-onecollision-intermediates \
    --strict-csv
"""
from __future__ import annotations

import argparse
import ast
import collections
import csv
import json
import os
import sys
from typing import Any, Dict, List, Tuple, Optional

Move = Tuple[int, int, int]
Phi = Tuple[int, int, int]


def read_csv(path: str) -> List[Dict[str, str]]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["_csv_path"] = path
    return rows


def partial_sums_with_zero(p: int, order: List[int]) -> List[int]:
    s = 0
    out = [0]
    for a in order:
        s = (s + int(a)) % p
        out.append(s)
    return out


def collision_data(p: int, order: List[int]) -> Dict[str, Any]:
    # Analyzer convention: collisions over S_1,...,S_n, excluding S_0.
    pos: Dict[int, List[int]] = collections.defaultdict(list)
    for idx, x in enumerate(partial_sums_with_zero(p, order)[1:], start=1):
        pos[x].append(idx)

    E = P = L = 0
    intervals = []
    for residue, xs in pos.items():
        m = len(xs)
        if m < 2:
            continue
        E += m - 1
        P += m * (m - 1) // 2
        for a in range(m):
            for b in range(a + 1, m):
                i, j = xs[a], xs[b]
                intervals.append({
                    "residue": residue,
                    "i": i,
                    "j": j,
                    "span": j - i,
                    "z0": i,
                    "z1": j - 1,
                })
                L += j - i

    intervals.sort(key=lambda I: (I["span"], I["i"], I["j"], I["residue"]))
    max_m = max((len(xs) for xs in pos.values()), default=1)
    return {
        "E": E,
        "P": P,
        "L": L,
        "Phi": (E, P, L),
        "positions": dict(pos),
        "intervals": intervals,
        "max_multiplicity": max_m,
    }


def move_tuple(order: Tuple[int, ...], start: int, length: int, insert: int) -> Tuple[int, ...]:
    block = order[start:start + length]
    rest = order[:start] + order[start + length:]
    return rest[:insert] + block + rest[insert:]


def apply_move(order: List[int], mv: Move) -> List[int]:
    start, length, insert = mv
    n = len(order)
    if length < 1 or start < 0 or start + length > n:
        raise ValueError(f"invalid start/length move={mv} for n={n}")
    rest_len = n - length
    if insert < 0 or insert > rest_len:
        raise ValueError(f"invalid insert move={mv} for n={n}, rest_len={rest_len}")
    if insert == start:
        raise ValueError(f"degenerate move insert==start: {mv}")
    return list(move_tuple(tuple(order), start, length, insert))


def parse_move_tuple(s: str) -> Move:
    obj = ast.literal_eval(s.strip())
    if not (isinstance(obj, tuple) and len(obj) == 3):
        raise ValueError(f"not a move tuple: {s}")
    return int(obj[0]), int(obj[1]), int(obj[2])


def parse_path(s: str) -> List[Move]:
    if not s:
        return []
    out: List[Move] = []
    for part in s.split(";"):
        part = part.strip()
        if part:
            out.append(parse_move_tuple(part))
    return out


def load_traces(paths: List[str]) -> Dict[str, Dict[int, Dict[str, Any]]]:
    db: Dict[str, Dict[int, Dict[str, Any]]] = {}
    for path in paths:
        line_map: Dict[int, Dict[str, Any]] = {}
        with open(path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                if line.strip():
                    line_map[line_no] = json.loads(line)
        for alias in {path, os.path.abspath(path), os.path.basename(path), os.path.normpath(path)}:
            db[alias] = line_map
    return db


def select_trace_map(trace_db: Dict[str, Dict[int, Dict[str, Any]]], csv_path: str, row: Dict[str, str]) -> Dict[int, Dict[str, Any]]:
    if row.get("source_file"):
        src = row["source_file"]
        for key in (src, os.path.abspath(src), os.path.basename(src), os.path.normpath(src)):
            if key in trace_db:
                return trace_db[key]
        raise KeyError(f"cannot resolve source_file={src!r}")

    unique_maps = []
    seen_ids = set()
    for m in trace_db.values():
        if id(m) not in seen_ids:
            unique_maps.append(m)
            seen_ids.add(id(m))
    if len(unique_maps) == 1:
        return unique_maps[0]

    b = os.path.basename(csv_path).lower()
    for key, m in trace_db.items():
        kb = os.path.basename(key).lower()
        if "p29" in b and "p29" in kb:
            return m
        if "p31" in b and "p31" in kb:
            return m
    raise KeyError(f"cannot infer trace file for csv={csv_path}")


def reconstruct_state(rec: Dict[str, Any], state_label: str) -> List[int]:
    order = [int(x) for x in rec["initial_order"]]
    moves = rec.get("moves", [])
    if state_label == "initial":
        return order
    if state_label == "prefinal":
        upto = max(0, len(moves) - 1)
    elif state_label.startswith("after_"):
        upto = int(state_label.split("_", 1)[1])
    else:
        raise ValueError(f"unknown state_label={state_label!r}")
    if upto > len(moves):
        raise ValueError(f"state_label={state_label} but only {len(moves)} trace moves")
    for mv in moves[:upto]:
        order = apply_move(order, (int(mv["start"]), int(mv["length"]), int(mv["insert"])))
    return order


def branch_name(cd: Dict[str, Any]) -> str:
    if cd["E"] < 2:
        return "E_lt_2"
    if cd["max_multiplicity"] >= 3:
        return "multiplicity"
    if cd["max_multiplicity"] == 2 and cd["P"] == 2:
        return "atomic_P2_matching"
    if cd["max_multiplicity"] == 2 and cd["P"] >= 3:
        return "matching_Pge3"
    return "other_Ege2"


def strict_csv_check(row: Dict[str, str], cd: Dict[str, Any], prefix: str) -> Optional[str]:
    for key, val in (("E", cd["E"]), ("P", cd["P"]), ("L", cd["L"])):
        col = f"{prefix}_{key}"
        if col in row and row[col] not in ("", None):
            if int(row[col]) != val:
                return f"{col} mismatch csv={row[col]} recomputed={val}"
    return None


def verify_nonatomic(rows: List[Dict[str, str]], trace_db, strict_csv: bool, allow_atomic: bool, max_fail: int):
    ok = fail = 0
    msgs = []
    for idx, row in enumerate(rows, start=1):
        try:
            rec = select_trace_map(trace_db, row["_csv_path"], row)[int(row["line_no"])]
            order = reconstruct_state(rec, row["state_label"])
            p = int(row.get("p") or rec["p"])
            cd0 = collision_data(p, order)
            if strict_csv:
                msg = strict_csv_check(row, cd0, "state")
                if msg:
                    raise AssertionError(msg)
            br = branch_name(cd0)
            if cd0["E"] < 2:
                raise AssertionError(f"not E>=2: Phi={cd0['Phi']}")
            if br == "atomic_P2_matching" and not allow_atomic:
                raise AssertionError("atomic row encountered in non-atomic verifier")
            mv = (int(row["start"]), int(row["length"]), int(row["insert"]))
            cd1 = collision_data(p, apply_move(order, mv))
            if not (cd1["Phi"] < cd0["Phi"]):
                raise AssertionError(f"move not descending: before={cd0['Phi']} after={cd1['Phi']} mv={mv}")
            if strict_csv and all(row.get(k) not in (None, "") for k in ["after_E", "after_P", "after_L"]):
                expected = (int(row["after_E"]), int(row["after_P"]), int(row["after_L"]))
                if cd1["Phi"] != expected:
                    raise AssertionError(f"after Phi mismatch csv={expected} recomputed={cd1['Phi']}")
            ok += 1
        except Exception as e:
            fail += 1
            if len(msgs) < max_fail:
                msgs.append(f"[nonatomic] csv={row.get('_csv_path')} row={idx} line={row.get('line_no')} state={row.get('state_label')} error={e}")
    return ok, fail, msgs


def verify_onecollision(rows: List[Dict[str, str]], trace_db, strict_csv: bool, require_intermediates: bool, max_fail: int):
    ok = fail = 0
    msgs = []
    for idx, row in enumerate(rows, start=1):
        try:
            rec = select_trace_map(trace_db, row["_csv_path"], row)[int(row["line_no"])]
            order = reconstruct_state(rec, row["state_label"])
            p = int(row.get("p") or rec["p"])
            cd0 = collision_data(p, order)
            if strict_csv:
                prefix = "initial" if "initial_E" in row else "state"
                msg = strict_csv_check(row, cd0, prefix)
                if msg:
                    raise AssertionError(msg)
            if not (cd0["E"] == 1 and cd0["P"] == 1):
                raise AssertionError(f"not one-collision: Phi={cd0['Phi']}")
            if row.get("path"):
                path = parse_path(row["path"])
            elif row.get("status") == "direct":
                path = [(int(row["second_start"]), int(row["second_length"]), int(row["second_insert"]))]
            elif row.get("status") == "two_step":
                path = [
                    (int(row["first_start"]), int(row["first_length"]), int(row["first_insert"])),
                    (int(row["second_start"]), int(row["second_length"]), int(row["second_insert"])),
                ]
            else:
                raise AssertionError("no path/direct/two_step certificate found")
            cur = order
            for step_idx, mv in enumerate(path, start=1):
                cur = apply_move(cur, mv)
                cd_mid = collision_data(p, cur)
                if require_intermediates and step_idx < len(path):
                    if not (cd_mid["E"] == 1 and cd_mid["P"] == 1):
                        raise AssertionError(f"intermediate step {step_idx} not one-collision: Phi={cd_mid['Phi']}")
            cd_final = collision_data(p, cur)
            if not (cd_final["Phi"] < cd0["Phi"]):
                raise AssertionError(f"path not descending: before={cd0['Phi']} final={cd_final['Phi']} path={path}")
            if strict_csv and all(row.get(k) not in (None, "") for k in ["final_E", "final_P", "final_L"]):
                expected = (int(row["final_E"]), int(row["final_P"]), int(row["final_L"]))
                if cd_final["Phi"] != expected:
                    raise AssertionError(f"final Phi mismatch csv={expected} recomputed={cd_final['Phi']}")
            ok += 1
        except Exception as e:
            fail += 1
            if len(msgs) < max_fail:
                msgs.append(f"[onecollision] csv={row.get('_csv_path')} row={idx} line={row.get('line_no')} state={row.get('state_label')} error={e}")
    return ok, fail, msgs


def verify_atomic_instances(rows: List[Dict[str, str]], trace_db, strict_csv: bool, max_fail: int):
    ok = fail = 0
    msgs = []
    for idx, row in enumerate(rows, start=1):
        try:
            rec = select_trace_map(trace_db, row["_csv_path"], row)[int(row["line_no"])]
            order = reconstruct_state(rec, row["state_label"])
            p = int(row.get("p") or rec["p"])
            cd0 = collision_data(p, order)
            if strict_csv:
                msg = strict_csv_check(row, cd0, "state")
                if msg:
                    raise AssertionError(msg)
            if not (cd0["P"] == 2 and cd0["max_multiplicity"] == 2):
                raise AssertionError(f"not atomic P=2 max_m=2: Phi={cd0['Phi']} max_m={cd0['max_multiplicity']}")
            origin = int(row["origin"])
            rel_moves = parse_path(row["candidate_moves"])
            if not rel_moves:
                raise AssertionError("empty candidate_moves")
            good = False
            for rs, length, ri in rel_moves:
                try:
                    mv = (origin + rs, length, origin + ri)
                    cd1 = collision_data(p, apply_move(order, mv))
                    if cd1["Phi"] < cd0["Phi"]:
                        good = True
                        break
                except Exception:
                    pass
            if not good:
                raise AssertionError(f"no candidate move descends among {len(rel_moves)} candidates")
            ok += 1
        except Exception as e:
            fail += 1
            if len(msgs) < max_fail:
                msgs.append(f"[atomic-instance] csv={row.get('_csv_path')} row={idx} line={row.get('line_no')} state={row.get('state_label')} error={e}")
    return ok, fail, msgs


def load_atomic_certs(path: str) -> Dict[str, List[Move]]:
    certs: Dict[str, List[Move]] = {}
    for row in read_csv(path):
        certs[row["signature_hash"]] = parse_path(row["certificate_moves"])
    return certs


def verify_atomic_certs(instance_rows: List[Dict[str, str]], certs: Dict[str, List[Move]], trace_db, max_fail: int):
    ok = fail = 0
    msgs = []
    for idx, row in enumerate(instance_rows, start=1):
        try:
            sig = row["signature_hash"]
            if sig not in certs:
                raise AssertionError(f"signature missing from cert table: {sig}")
            rec = select_trace_map(trace_db, row["_csv_path"], row)[int(row["line_no"])]
            order = reconstruct_state(rec, row["state_label"])
            p = int(row.get("p") or rec["p"])
            cd0 = collision_data(p, order)
            origin = int(row["origin"])
            good = False
            for rs, length, ri in certs[sig]:
                try:
                    mv = (origin + rs, length, origin + ri)
                    cd1 = collision_data(p, apply_move(order, mv))
                    if cd1["Phi"] < cd0["Phi"]:
                        good = True
                        break
                except Exception:
                    pass
            if not good:
                raise AssertionError(f"no certificate move descends for signature={sig}")
            ok += 1
        except Exception as e:
            fail += 1
            if len(msgs) < max_fail:
                msgs.append(f"[atomic-cert] row={idx} sig={row.get('signature_hash')} line={row.get('line_no')} state={row.get('state_label')} error={e}")
    return ok, fail, msgs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trace-files", nargs="+", required=True)
    ap.add_argument("--nonatomic-csv", nargs="*", default=[])
    ap.add_argument("--onecollision-csv", nargs="*", default=[])
    ap.add_argument("--atomic-instances", nargs="*", default=[])
    ap.add_argument("--atomic-certs", nargs="*", default=[])
    ap.add_argument("--strict-csv", action="store_true")
    ap.add_argument("--allow-atomic-in-nonatomic", action="store_true")
    ap.add_argument("--require-onecollision-intermediates", action="store_true")
    ap.add_argument("--max-fail-examples", type=int, default=20)
    args = ap.parse_args()

    print("=== Erdos 475 independent certificate verifier ===")
    print(f"trace_files={len(args.trace_files)}")
    trace_db = load_traces(args.trace_files)

    total_ok = total_fail = 0
    all_msgs: List[str] = []

    if args.nonatomic_csv:
        rows: List[Dict[str, str]] = []
        for p in args.nonatomic_csv:
            rows.extend(read_csv(p))
        ok, fail, msgs = verify_nonatomic(rows, trace_db, args.strict_csv, args.allow_atomic_in_nonatomic, args.max_fail_examples)
        total_ok += ok; total_fail += fail; all_msgs.extend(msgs)
        print(f"nonatomic: ok={ok} fail={fail}")

    if args.onecollision_csv:
        rows = []
        for p in args.onecollision_csv:
            rows.extend(read_csv(p))
        ok, fail, msgs = verify_onecollision(rows, trace_db, args.strict_csv, args.require_onecollision_intermediates, args.max_fail_examples)
        total_ok += ok; total_fail += fail; all_msgs.extend(msgs)
        print(f"onecollision: ok={ok} fail={fail}")

    atomic_rows: List[Dict[str, str]] = []
    if args.atomic_instances:
        for p in args.atomic_instances:
            atomic_rows.extend(read_csv(p))
        ok, fail, msgs = verify_atomic_instances(atomic_rows, trace_db, args.strict_csv, args.max_fail_examples)
        total_ok += ok; total_fail += fail; all_msgs.extend(msgs)
        print(f"atomic-instances-candidate: ok={ok} fail={fail}")

    if args.atomic_certs:
        if not atomic_rows:
            print("atomic-signature-certs: skipped because --atomic-instances not supplied")
        else:
            certs: Dict[str, List[Move]] = {}
            for p in args.atomic_certs:
                certs.update(load_atomic_certs(p))
            ok, fail, msgs = verify_atomic_certs(atomic_rows, certs, trace_db, args.max_fail_examples)
            total_ok += ok; total_fail += fail; all_msgs.extend(msgs)
            print(f"atomic-signature-certs: ok={ok} fail={fail}")

    print()
    print(f"TOTAL ok={total_ok} fail={total_fail}")
    if all_msgs:
        print("\nFailure examples:")
        for m in all_msgs[:args.max_fail_examples]:
            print("  " + m)
    print("\nVERDICT: " + ("PASS" if total_fail == 0 else "FAIL"))
    return 0 if total_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
