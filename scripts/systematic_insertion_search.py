#!/usr/bin/env python3
"""Systematic search for worst-case valid orderings of A\{x}.

Processes triples (p, set, x) in parallel.  For each:
  - k ≤ 8: enumerate ALL valid permutations
  - k ≤ 12: sample random permutations (up to 200K attempts or 500 found)
  - k > 12: perturbation search from native ordering
"""
from __future__ import annotations
import itertools, json, random, sys, time
from collections import Counter
from multiprocessing import Pool, cpu_count

random.seed(20260603)


def nonempty_partials(order, p):
    out, s = [], 0
    for v in order:
        s = (s + v) % p
        out.append(s)
    return out

def is_graham_valid(order, p):
    s = nonempty_partials(order, p)
    return len(s) == len(set(s))

def analyze_insertion(order, x, p):
    n = len(order)
    s = [0]
    acc = 0
    for v in order:
        acc = (acc + v) % p
        s.append(acc)
    mult = [0] * (n + 1)
    endpoint = set()
    zero_partial = any(v == 0 for v in s[1:])
    if zero_partial:
        mult[0] += 1
    for i in range(1, n + 1):
        ins = (s[i] + x) % p
        if ins in set(s[1:i+1]):
            endpoint.add(i)
            mult[i] += 1
    target = (-x) % p
    for k in range(1, n + 1):
        for j in range(k, n + 1):
            if (s[j] - s[k]) % p == target and k < j:
                for i in range(k, j):
                    mult[i] += 1
    blocked = {i for i, m in enumerate(mult) if m > 0} | endpoint
    unblocked = [i for i in range(n + 1) if i not in blocked]
    return {"blocked": len(blocked), "unblocked": len(unblocked)}


def search_triple(args):
    p, elements, x = args
    k = len(elements)
    baseline = analyze_insertion(elements, x, p)
    best_worst = baseline
    total_valid = 0
    fully_blocked = False

    if k <= 8:
        for perm in itertools.permutations(elements):
            if not is_graham_valid(perm, p):
                continue
            total_valid += 1
            obs = analyze_insertion(perm, x, p)
            if obs["blocked"] > best_worst["blocked"]:
                best_worst = obs
            if obs["unblocked"] == 0:
                fully_blocked = True
                break

    elif k <= 12:
        for _ in range(200_000):
            perm = list(elements)
            random.shuffle(perm)
            if not is_graham_valid(perm, p):
                continue
            total_valid += 1
            obs = analyze_insertion(perm, x, p)
            if obs["blocked"] > best_worst["blocked"]:
                best_worst = obs
            if obs["unblocked"] == 0:
                fully_blocked = True
                break
            if total_valid >= 500:
                break

    else:
        current = list(elements)
        current_blocked = baseline["blocked"]
        total_valid = 1
        for _ in range(50_000):
            idx = random.randrange(k)
            pos = random.randrange(k)
            val = current.pop(idx)
            current.insert(pos, val)
            if not is_graham_valid(current, p):
                val = current.pop(pos)
                current.insert(idx, val)
                continue
            total_valid += 1
            obs = analyze_insertion(current, x, p)
            if obs["blocked"] > best_worst["blocked"]:
                best_worst = obs
                current_blocked = obs["blocked"]
                if obs["unblocked"] == 0:
                    fully_blocked = True
                    break
            elif obs["blocked"] >= current_blocked:
                current_blocked = obs["blocked"]
            else:
                val = current.pop(pos)
                current.insert(idx, val)

    return {
        "k": k,
        "native_blocked": baseline["blocked"],
        "native_unblocked": baseline["unblocked"],
        "worst_blocked": best_worst["blocked"],
        "worst_unblocked": best_worst["unblocked"],
        "fully_blocked_found": fully_blocked,
        "worst_improved": best_worst["blocked"] > baseline["blocked"],
        "total_valid_explored": total_valid,
    }


def load_and_search(path, limit, workers):
    # Single-pass: collect triples and immediate results
    immediate: list[dict] = []
    triples: list[tuple] = []  # (p, s, x)
    meta: list[dict] = []  # metadata per triple

    with open(path) as fh:
        for line_no, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            p = int(row["p"])
            order = [int(v) for v in row["final_order"]]
            b = [int(v) for v in row.get("B", [])]
            for idx, x in enumerate(order):
                s = [*order[:idx], *order[idx+1:]]
                if not s:
                    immediate.append({"p": p, "B": b, "x": x, "k": 0, "native_valid": True,
                                      "native_blocked": 1, "native_unblocked": 0,
                                      "fully_blocked_found": True, "worst_improved": False,
                                      "total_valid_explored": 1})
                    continue
                if not is_graham_valid(s, p):
                    immediate.append({"p": p, "B": b, "x": x, "k": len(s), "native_valid": False})
                    continue
                # Queue for search
                triples.append((p, s, x))
                meta.append({"p": p, "B": b, "x": x, "source_line": line_no})
            if limit and line_no >= limit:
                break

    print(f"Immediate (non-search) results: {len(immediate)}", file=sys.stderr)
    print(f"Triples to search: {len(triples)}", file=sys.stderr)

    start = time.monotonic()
    if triples:
        with Pool(workers) as pool:
            search_results = pool.map(search_triple, triples)
        for m, sr in zip(meta, search_results):
            immediate.append({**m, **sr, "native_valid": True})
    elapsed = time.monotonic() - start

    print(f"Search wall time: {elapsed:.1f}s", file=sys.stderr)

    return immediate, elapsed


def main():
    path = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else None
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else cpu_count() // 2
    jsonl_out = sys.argv[4] if len(sys.argv) > 4 else None

    results, elapsed = load_and_search(path, limit, workers)

    if jsonl_out:
        from pathlib import Path
        Path(jsonl_out).parent.mkdir(parents=True, exist_ok=True)
        with open(jsonl_out, "w") as fh:
            for r in results:
                fh.write(json.dumps(r, sort_keys=True) + "\n")
        print(f"\nDetailed results written to {jsonl_out}", file=sys.stderr)

    valid = [r for r in results if r.get("native_valid")]
    fb = [r for r in valid if r.get("fully_blocked_found")]
    improved = [r for r in valid if r.get("worst_improved")]

    print(f"\n{'='*60}")
    print(f"Total entries:         {len(results)}")
    print(f"Valid deletions:       {len(valid)}")
    print(f"Fully blocked found:   {len(fb)} ({100*len(fb)/len(valid):.1f}% of valid)" if valid else "N/A")
    print(f"Worst > native:        {len(improved)} ({100*len(improved)/len(valid):.1f}% of valid)" if valid else "N/A")
    print(f"Search wall time:      {elapsed:.1f}s")

    by_k = Counter()
    fb_by_k = Counter()
    imp_by_k = Counter()
    for r in valid:
        by_k[r["k"]] += 1
        if r["fully_blocked_found"]:
            fb_by_k[r["k"]] += 1
        if r["worst_improved"]:
            imp_by_k[r["k"]] += 1

    print(f"\n{'k':>4} {'total':>6} {'fb':>6} {'fb%':>7} {'imp':>6} {'imp%':>7}")
    for k in sorted(by_k):
        t = by_k[k]
        f = fb_by_k.get(k, 0)
        i = imp_by_k.get(k, 0)
        print(f"{k:4d} {t:6d} {f:6d} {100*f/t:6.1f}% {i:6d} {100*i/t:6.1f}%")
        # (details omitted for brevity; use JSONL output for per-row inspection)

    v_by_p = Counter()
    fb_by_p = Counter()
    for r in valid:
        v_by_p[r["p"]] += 1
        if r["fully_blocked_found"]:
            fb_by_p[r["p"]] += 1
    print(f"\nPer-prime fully blocked:")
    for p in sorted(v_by_p):
        print(f"  p={p:3d}: {fb_by_p.get(p,0):4d}/{v_by_p[p]:4d}")


if __name__ == "__main__":
    main()
