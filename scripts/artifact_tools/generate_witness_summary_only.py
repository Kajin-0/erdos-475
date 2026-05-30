#!/usr/bin/env python3
r"""
Summary-only witness generator for Erdos 475 finite residue classes.

This is for disk-pressure situations. It does NOT write the large witness JSONL.
For each canonical complement B, it finds a valid ordering, verifies the partial
sums immediately, and updates an aggregate SHA256 digest over the canonical JSON
record that would have been written.

Output:
  small text summary only.

Example:
  python generate_witness_summary_only.py --cases 31:16 --out p31_b16_summary.txt --progress 1000

Resume/chunk support:
  python generate_witness_summary_only.py --cases 31:16 --start-index 0 --stop-index 500000 --out p31_b16_chunk_000000_500000.txt
  python generate_witness_summary_only.py --cases 31:16 --start-index 500000 --stop-index 1000000 --out p31_b16_chunk_500000_1000000.txt

Indexing:
  start-index is inclusive, stop-index is exclusive, over canonical B orbit representatives
  in deterministic enumeration order.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import time
import hashlib
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


@dataclass(frozen=True)
class CaseSpec:
    p: int
    b_min: int
    b_max: int


def parse_cases(spec: str) -> List[CaseSpec]:
    out = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        p_str, b_str = part.split(":", 1)
        p = int(p_str)
        if ".." in b_str:
            a, b = b_str.split("..", 1)
            out.append(CaseSpec(p, int(a), int(b)))
        else:
            b = int(b_str)
            out.append(CaseSpec(p, b, b))
    return out


def partial_sums(p: int, order: Sequence[int]) -> List[int]:
    s = 0
    out = []
    for x in order:
        s = (s + int(x)) % p
        out.append(s)
    return out


def is_valid_order(p: int, order: Sequence[int]) -> bool:
    ps = partial_sums(p, order)
    return len(ps) == len(set(ps))


def scale_subset(p: int, B: Sequence[int], a: int) -> Tuple[int, ...]:
    return tuple(sorted((a * x) % p for x in B))


def canonical_subset(p: int, B: Sequence[int]) -> Tuple[int, ...]:
    return min(scale_subset(p, B, a) for a in range(1, p))


def canonical_Bs(p: int, b_size: int) -> Iterable[Tuple[int, ...]]:
    for B in itertools.combinations(range(1, p), b_size):
        Bt = tuple(B)
        if Bt == canonical_subset(p, Bt):
            yield Bt


def stable_case_seed(seed: int, p: int, b_size: int, B: Tuple[int, ...], restart: int) -> int:
    value = seed
    for x in (p, b_size, restart, *B):
        value = (value * 1000003 + x) & 0xFFFFFFFF
    return value


def greedy_attempt(p: int, A: List[int], rng: random.Random) -> Optional[List[int]]:
    unused = A[:]
    rng.shuffle(unused)
    order = []
    s = 0
    seen = set()

    while unused:
        candidates = []
        for x in unused:
            ns = (s + x) % p
            if ns in seen:
                continue

            future = 0
            for y in unused:
                if y == x:
                    continue
                n2 = (ns + y) % p
                if n2 not in seen and n2 != ns:
                    future += 1

            candidates.append((future, rng.random(), x, ns))

        if not candidates:
            return None

        candidates.sort()
        _, _, x, ns = candidates[0]
        order.append(x)
        seen.add(ns)
        s = ns
        unused.remove(x)

    return order if is_valid_order(p, order) else None


def dfs_once(
    p: int,
    A: List[int],
    rng: random.Random,
    max_nodes: int,
    greedy_restarts: int,
) -> Tuple[Optional[List[int]], int]:
    for _ in range(greedy_restarts):
        order = greedy_attempt(p, A, rng)
        if order is not None:
            return order, 0

    n = len(A)
    full_mask = (1 << n) - 1
    memo = set()
    nodes = 0

    tie = list(range(n))
    rng.shuffle(tie)
    tie_rank = {idx: r for r, idx in enumerate(tie)}
    start_bias = {idx: rng.random() for idx in range(n)}

    def rec(used_mask: int, s: int, seen_mask: int) -> Optional[List[int]]:
        nonlocal nodes
        nodes += 1
        if nodes > max_nodes:
            return None
        if used_mask == full_mask:
            return []

        key = (used_mask, s, seen_mask)
        if key in memo:
            return None

        candidates = []
        remaining_count = n - used_mask.bit_count()

        for i, x in enumerate(A):
            if used_mask & (1 << i):
                continue
            ns = (s + x) % p
            if seen_mask & (1 << ns):
                continue

            new_seen = seen_mask | (1 << ns)
            new_used = used_mask | (1 << i)

            onward = 0
            for j, y in enumerate(A):
                if new_used & (1 << j):
                    continue
                if not (new_seen & (1 << ((ns + y) % p))):
                    onward += 1

            if remaining_count > 1 and onward == 0:
                continue

            candidates.append((onward, start_bias[i], tie_rank[i], i, x, ns, new_used, new_seen))

        if not candidates:
            memo.add(key)
            return None

        candidates.sort()

        for _, _, _, i, x, ns, new_used, new_seen in candidates:
            tail = rec(new_used, ns, new_seen)
            if tail is not None:
                return [x] + tail

        memo.add(key)
        return None

    order = rec(0, 0, 0)
    if order is not None and is_valid_order(p, order):
        return order, nodes
    return None, nodes


def find_order(
    p: int,
    A: List[int],
    seed: int,
    b_size: int,
    B: Tuple[int, ...],
    max_nodes: int,
    restarts: int,
    greedy_restarts: int,
) -> Tuple[Optional[List[int]], int, int]:
    total_nodes = 0
    for r in range(restarts):
        rng = random.Random(stable_case_seed(seed, p, b_size, B, r))
        order, nodes = dfs_once(p, A, rng, max_nodes=max_nodes, greedy_restarts=greedy_restarts)
        total_nodes += nodes
        if order is not None:
            return order, total_nodes, r
    return None, total_nodes, restarts


def make_record(p: int, B: Tuple[int, ...], final_order: List[int]) -> Dict:
    Q = list(range(1, p))
    Bset = set(B)
    initial_order = [x for x in Q if x not in Bset]
    return {
        "p": p,
        "B": list(B),
        "Q_p": Q,
        "initial_order": initial_order,
        "final_order": final_order,
        "final_partial_sums": partial_sums(p, final_order),
    }


def expected_count(p: int, b_size: int) -> int:
    return sum(1 for _ in canonical_Bs(p, b_size))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", required=True, help="Example: 31:16 or 31:16..17")
    ap.add_argument("--out", required=True)
    ap.add_argument("--seed", type=int, default=475)
    ap.add_argument("--max-nodes", type=int, default=1000000)
    ap.add_argument("--restarts", type=int, default=8)
    ap.add_argument("--greedy-restarts", type=int, default=80)
    ap.add_argument("--progress", type=int, default=1000)
    ap.add_argument("--start-index", type=int, default=0)
    ap.add_argument("--stop-index", type=int, default=None)
    args = ap.parse_args()

    specs = parse_cases(args.cases)
    t0 = time.time()

    total_seen = 0
    total_solved = 0
    failed = []
    digest = hashlib.sha256()

    with open(args.out, "w", encoding="utf-8") as log:
        def emit(msg: str):
            print(msg)
            log.write(msg + "\n")
            log.flush()

        emit("=== Summary-only witness generator ===")
        emit(f"cases={args.cases}")
        emit(f"out={args.out}")
        emit(f"seed={args.seed}")
        emit(f"max_nodes={args.max_nodes}")
        emit(f"restarts={args.restarts}")
        emit(f"greedy_restarts={args.greedy_restarts}")
        emit(f"start_index={args.start_index}")
        emit(f"stop_index={args.stop_index}")
        emit("")

        for spec in specs:
            for b_size in range(spec.b_min, spec.b_max + 1):
                p = spec.p
                class_seen = 0
                class_solved = 0
                class_digest = hashlib.sha256()

                for global_idx, B in enumerate(canonical_Bs(p, b_size)):
                    if global_idx < args.start_index:
                        continue
                    if args.stop_index is not None and global_idx >= args.stop_index:
                        break

                    class_seen += 1
                    total_seen += 1

                    Bset = set(B)
                    A = [x for x in range(1, p) if x not in Bset]

                    order, nodes, restart_used = find_order(
                        p=p,
                        A=A,
                        seed=args.seed,
                        b_size=b_size,
                        B=B,
                        max_nodes=args.max_nodes,
                        restarts=args.restarts,
                        greedy_restarts=args.greedy_restarts,
                    )

                    if order is None:
                        failed.append((p, b_size, global_idx, B, nodes))
                        emit(f"FAIL p={p} |B|={b_size} index={global_idx} B={B} nodes={nodes}")
                        continue

                    rec = make_record(p, B, order)
                    if not is_valid_order(p, order):
                        failed.append((p, b_size, global_idx, B, -1))
                        emit(f"FAIL_INVALID p={p} |B|={b_size} index={global_idx} B={B}")
                        continue

                    line = json.dumps(rec, separators=(",", ":"), sort_keys=True).encode("utf-8")
                    digest.update(line)
                    digest.update(b"\n")
                    class_digest.update(line)
                    class_digest.update(b"\n")

                    class_solved += 1
                    total_solved += 1

                    if args.progress and total_seen % args.progress == 0:
                        emit(
                            f"progress total={total_seen} solved={total_solved} failed={len(failed)} "
                            f"current=p{p}_b{b_size} index={global_idx} restart={restart_used} "
                            f"elapsed={time.time()-t0:.1f}s"
                        )

                emit("")
                emit(f"Class summary p={p} |B|={b_size}")
                emit(f"  processed={class_seen}")
                emit(f"  solved={class_solved}")
                emit(f"  failed_so_far={len(failed)}")
                emit(f"  class_sha256={class_digest.hexdigest()}")

        emit("")
        emit("Final summary")
        emit("-------------")
        emit(f"total_processed={total_seen}")
        emit(f"total_solved={total_solved}")
        emit(f"failed={len(failed)}")
        emit(f"aggregate_sha256={digest.hexdigest()}")
        emit(f"elapsed_seconds={time.time()-t0:.2f}")

        if failed:
            emit("First failures")
            for p, b, idx, B, nodes in failed[:20]:
                emit(f"p={p} |B|={b} index={idx} B={B} nodes={nodes}")
            emit("VERDICT: FAIL")
            return 2

        emit("VERDICT: PASS")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
