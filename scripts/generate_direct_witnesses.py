#!/usr/bin/env python3
"""Generate direct minimal witnesses for finite Erdős 475 complement domains.

This script enumerates canonical complement representatives B under nonzero
multiplicative scaling and searches for a witness ordering of A = F_p^* \ B.

It is intended to promote small, log-only, or externally verified finite domains
into committed Tier 1 certificate artifacts.  It is deterministic by default:
randomized search uses a seed derived from (p,B), so reruns reproduce the same
witnesses unless the search parameters change.

Example:

  python scripts/generate_direct_witnesses.py \
    --domain 17:3 \
    --domain 19:3-5 \
    --domain 23:3-9 \
    --out certificates/direct_witnesses_small_primes.jsonl \
    --max-trials 1000000 \
    --progress-every 1000

The output rows are compatible with scripts/verify_minimal_witnesses.py.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import random
import sys
from pathlib import Path
from typing import Iterable, Sequence


def parse_domain(text: str) -> tuple[int, range]:
    left, right = text.split(":", 1)
    p = int(left)
    if "-" in right:
        lo, hi = right.split("-", 1)
        return p, range(int(lo), int(hi) + 1)
    k = int(right)
    return p, range(k, k + 1)


def canonical_scale(B: Sequence[int], p: int) -> tuple[int, ...]:
    return min(tuple(sorted((lam * x) % p for x in B)) for lam in range(1, p))


def canonical_scale_lambda(B: Sequence[int], p: int) -> int:
    best_lam = 1
    best = tuple(sorted(B))
    for lam in range(1, p):
        scaled = tuple(sorted((lam * x) % p for x in B))
        if scaled < best:
            best = scaled
            best_lam = lam
    return best_lam


def iter_canonical_complements(p: int, k: int) -> Iterable[tuple[int, ...]]:
    universe = range(1, p)
    seen: set[tuple[int, ...]] = set()
    for comb in itertools.combinations(universe, k):
        rep = canonical_scale(comb, p)
        if rep in seen:
            continue
        seen.add(rep)
        yield rep


def partials_distinct(order: Sequence[int], p: int) -> bool:
    total = 0
    seen: set[int] = set()
    for x in order:
        total = (total + x) % p
        if total in seen:
            return False
        seen.add(total)
    return True


def deterministic_seed(p: int, B: Sequence[int], salt: int) -> int:
    payload = f"erdos475-direct-witness-v1|p={p}|B={','.join(map(str, B))}|salt={salt}"
    return int(hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16], 16)


def deterministic_variants(A: Sequence[int], p: int) -> Iterable[tuple[int, ...]]:
    A = tuple(A)
    yield tuple(sorted(A))
    yield tuple(sorted(A, reverse=True))
    yield tuple(sorted(A, key=lambda x: (x % 2, x)))
    yield tuple(sorted(A, key=lambda x: (x % 2, -x)))
    yield tuple(sorted(A, key=lambda x: ((2 * x) % p, x)))
    yield tuple(sorted(A, key=lambda x: ((3 * x) % p, x)))
    yield tuple(sorted(A, key=lambda x: ((5 * x) % p, x)))


def random_witness(A: Sequence[int], p: int, B: Sequence[int], max_trials: int, salt: int) -> tuple[tuple[int, ...] | None, int]:
    seen_variants: set[tuple[int, ...]] = set()
    for order in deterministic_variants(A, p):
        if order in seen_variants:
            continue
        seen_variants.add(order)
        if partials_distinct(order, p):
            return order, 0

    rng = random.Random(deterministic_seed(p, B, salt))
    arr = list(A)
    for trial in range(1, max_trials + 1):
        rng.shuffle(arr)
        order = tuple(arr)
        if partials_distinct(order, p):
            return order, trial
    return None, max_trials


def load_existing_keys(path: Path) -> set[tuple[int, tuple[int, ...]]]:
    keys: set[tuple[int, tuple[int, ...]]] = set()
    if not path.exists():
        return keys
    with path.open("r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            p = int(row["p"])
            B = tuple(sorted(int(x) for x in row["B"]))
            keys.add((p, B))
    return keys


def append_row(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")
        fh.flush()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain", action="append", required=True, help="Domain p:k or p:k-lo, e.g. 23:3-9")
    parser.add_argument("--out", required=True, help="Output JSONL file")
    parser.add_argument("--max-trials", type=int, default=1_000_000)
    parser.add_argument("--salt", type=int, default=0, help="Deterministic randomized-search salt")
    parser.add_argument("--resume", action="store_true", help="Skip rows already present in --out")
    parser.add_argument("--progress-every", type=int, default=1000)
    parser.add_argument("--stop-after", type=int, default=None, help="Stop after generating this many new rows")
    args = parser.parse_args()

    out_path = Path(args.out)
    existing = load_existing_keys(out_path) if args.resume else set()

    generated = 0
    skipped = 0
    failures: list[dict] = []

    for domain_text in args.domain:
        p, k_range = parse_domain(domain_text)
        for k in k_range:
            domain_generated = 0
            domain_seen = 0
            print(f"[generate] domain p={p} |B|={k}", flush=True)
            for B in iter_canonical_complements(p, k):
                domain_seen += 1
                key = (p, B)
                if key in existing:
                    skipped += 1
                    continue

                A = [x for x in range(1, p) if x not in set(B)]
                order, trials = random_witness(A, p, B, args.max_trials, args.salt)
                if order is None:
                    failures.append({"p": p, "B": list(B), "k": k, "trials": trials})
                    print(f"[generate] FAIL p={p} |B|={k} B={list(B)} trials={trials}", file=sys.stderr, flush=True)
                    continue

                row = {
                    "p": p,
                    "B": list(B),
                    "canonical_scale_lambda": canonical_scale_lambda(B, p),
                    "final_order": list(order),
                    "source": "direct_deterministic_search",
                    "search_trials": trials,
                    "search_salt": args.salt,
                }
                append_row(out_path, row)
                existing.add(key)
                generated += 1
                domain_generated += 1

                if args.progress_every and generated % args.progress_every == 0:
                    print(
                        f"[generate] progress generated={generated} skipped={skipped} "
                        f"current_domain=p{p}_b{k} domain_seen={domain_seen}",
                        flush=True,
                    )
                if args.stop_after is not None and generated >= args.stop_after:
                    print(f"[generate] stop_after reached: {generated}", flush=True)
                    break
            print(f"[generate] domain done p={p} |B|={k} seen={domain_seen} generated={domain_generated}", flush=True)
            if args.stop_after is not None and generated >= args.stop_after:
                break
        if args.stop_after is not None and generated >= args.stop_after:
            break

    print("=== direct witness generation summary ===")
    print(f"output={out_path}")
    print(f"generated={generated}")
    print(f"skipped={skipped}")
    print(f"failures={len(failures)}")
    if failures:
        fail_path = out_path.with_suffix(out_path.suffix + ".failures.json")
        fail_path.write_text(json.dumps(failures, indent=2, sort_keys=True), encoding="utf-8")
        print(f"failure_file={fail_path}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
