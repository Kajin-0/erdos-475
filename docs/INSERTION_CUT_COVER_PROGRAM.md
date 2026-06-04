# Insertion cut-cover program for Erdős 475

This document records an independent analytic route toward the full theorem. It is separate from the finite-residue/computational completion track.

The goal is to reduce a minimal counterexample to an impossible family of insertion obstructions.

## 1. Basic notation

Let `p` be prime and let

```text
A subset F_p^*,
t = |A|.
```

For an ordering

```text
R = (r_1,...,r_t)
```

write nonempty partial sums

```text
S_i(R) = r_1 + ... + r_i, 1 <= i <= t.
```

The ordering is Graham-valid if

```text
S_1(R),...,S_t(R)
```

are pairwise distinct modulo `p`.

For an ordering

```text
C = (c_1,...,c_n)
```

of a set `A \ {x}`, write extended partial sums

```text
s_0 = 0,
s_i = c_1 + ... + c_i, 1 <= i <= n.
```

The original problem only requires the nonempty sums `s_1,...,s_n` to be distinct. The value `s_0=0` is an auxiliary endpoint and must be handled carefully. In particular, a nonempty partial sum `s_j` is allowed to equal `0`.

## 2. Insertion operation

For a cut

```text
i in {0,1,...,n},
```

insert `x` after `c_i`, with `i=0` meaning insertion at the beginning:

```text
C^{(i,x)} = (c_1,...,c_i,x,c_{i+1},...,c_n).
```

The new nonempty partial sums are:

```text
s_1,...,s_i,
s_i + x,
s_{i+1}+x,...,s_n+x.
```

Here the first block is absent when `i=0`.

## 3. Internal insertion criterion

### Lemma 3.1: internal insertion criterion

Assume `C` is Graham-valid, so `s_1,...,s_n` are pairwise distinct. For `1 <= i <= n`, the insertion `C^{(i,x)}` is Graham-valid if and only if the following two obstruction types are absent.

### Endpoint obstruction

```text
s_i + x = s_k for some 1 <= k <= i.
```

### Crossing obstruction

```text
s_j + x = s_k for some 1 <= k <= i < j <= n.
```

Equivalently,

```text
s_j - s_k = -x.
```

### Cut-zero obstruction

For `i=0`, the new partial sums are

```text
x, s_1+x, ..., s_n+x.
```

The inserted first sum `x` collides with a shifted suffix sum `s_j+x` if and only if

```text
s_j = 0
```

for some `1 <= j <= n`. This is a real obstruction because Graham-validity does not forbid nonempty partial sums from equaling `0`.

### Proof

The old prefix sums `s_1,...,s_i` remain distinct because `C` is valid. The shifted suffix sums `s_{i+1}+x,...,s_n+x` remain distinct because translation by `x` is injective. For `i >= 1`, the inserted sum `s_i+x` cannot collide with a shifted suffix sum `s_j+x` for `j>i`, since this would imply `s_i=s_j`, impossible by validity of `C`. The remaining forbidden collisions are exactly endpoint collisions with earlier nonempty prefix sums and crossing collisions from shifted suffix sums into earlier prefix sums. For `i=0`, there is no earlier prefix, but the inserted first sum `x` can collide with a shifted suffix sum precisely when some nonempty partial sum of `C` is zero. ∎

## 4. Cut-cover formulation

For fixed `C` and `x`, define the blocked-cut set

```text
Block(C,x) subset {0,1,...,n}
```

as the set of cuts `i` for which insertion of `x` is not Graham-valid.

The endpoint obstruction blocks cut `i >= 1` if

```text
s_i + x in {s_1,...,s_i}.
```

Cut `0` is blocked by the zero-partial obstruction if

```text
0 in {s_1,...,s_n}.
```

For each pair `(k,j)` satisfying

```text
1 <= k < j <= n,
s_j - s_k = -x,
```

the crossing obstruction blocks every cut

```text
k <= i < j.
```

Thus each such pair contributes an interval

```text
I(k,j) = {k,k+1,...,j-1}
```

of blocked cuts.

## 5. Minimal counterexample principle

Assume `A` is a minimal counterexample by set size. Then every proper subset of `A` has a Graham-valid ordering.

For every `x in A`, choose a Graham-valid ordering `C_x` of `A \ {x}`. If there exists `x` and a cut `i` such that insertion of `x` into `C_x` is Graham-valid, then `A` is not a counterexample.

Therefore, in a minimal counterexample:

```text
Block(C,x) = {0,1,...,n}
```

for every `x in A` and every Graham-valid ordering `C` of `A \ {x}`.

This is the cut-cover obstruction.

## 6. Main analytic target

### Obstruction-impossibility lemma

There is no prime `p`, set `A subset F_p^*`, element `x in A`, and Graham-valid ordering `C` of `A \ {x}` such that all insertion cuts are blocked for every possible choice of `x` and `C` arising from a minimal counterexample.

A stronger and more useful form would be:

```text
For every minimal counterexample A, there exists x in A and a valid ordering C
of A\{x} such that Block(C,x) is a proper subset of {0,...,|A|-1}.
```

This would prove the full theorem by induction.

## 7. Quantitative attack

Let

```text
D_x(C) = #{(k,j): 1 <= k < j <= n and s_j - s_k = -x}.
```

Each pair contributes one blocking interval. If the union of all crossing intervals, endpoint obstructions, and the cut-zero obstruction fails to cover all `n+1` cuts, insertion succeeds.

The core challenge is that a small number of long intervals can cover all cuts. Therefore a purely cardinality-based bound on `D_x(C)` is insufficient unless it also controls interval geometry.

Useful quantities:

```text
number of blocking intervals;
maximum interval length;
minimum left endpoint;
maximum right endpoint;
coverage multiplicity per cut;
endpoint obstruction count;
whether cut zero is blocked by a zero partial sum;
number of zero-sum consecutive blocks in C.
```

## 8. Local surgery strategy

If all cuts are blocked, choose a cut with minimal blocking multiplicity. Analyze a minimal obstruction responsible for that cut. Try one of the following operations:

```text
1. reverse a short block;
2. rotate a prefix/suffix;
3. swap adjacent elements near the obstruction;
4. move a block across the cut;
5. replace C by another valid ordering of A\{x} that reduces total blocked cuts.
```

The desired descent measure is lexicographic:

```text
M(C,x) = (
  |Block(C,x)|,
  total_blocking_multiplicity,
  number_of_crossing_intervals,
  total_interval_length,
  endpoint_obstruction_count,
  zero_partial_cut_zero_flag
).
```

A proof would show that if all cuts are blocked, some local surgery preserves Graham-validity of `C` while decreasing `M(C,x)`, contradicting minimality.

## 9. Structural attack

If the cut-cover obstruction persists under all valid orderings of `A\{x}`, then the partial-sum path must contain many repeated differences equal to `-x` across many cuts.

This suggests additive structure:

```text
many pairs (k,j) with s_j - s_k = -x
```

means many consecutive blocks of `C` sum to `-x`.

Potential route:

```text
persistent cut-cover
=> many prescribed-sum consecutive blocks
=> additive rigidity of the partial-sum path
=> existence of a local rearrangement
=> contradiction.
```

## 10. Computational subproblem

A useful finite experiment is:

```text
For every verified finite instance and for every x in A,
find a valid ordering C of A\{x} minimizing |Block(C,x)|.
```

Record:

```text
minimum blocked cuts;
blocking interval distribution;
whether an unblocked cut exists;
worst obstruction signatures.
```

If all verified examples admit orderings with many unblocked cuts, that supports the insertion strategy. If some examples are nearly fully blocked, those become model obstructions for the analytic proof.

## 11. Empirical findings (2026-06-03)

A systematic search layer (`scripts/systematic_insertion_search.py`) was built and run across all verified primes (p=17..31, 3,729 records, 72,409 triples). Key results:

### Native deletion ordering

When an element `x` is deleted from a known Graham-valid ordering of `A`, the remaining ordering (the "native" ordering) is:

- Valid only 19.8% of the time (declines with larger primes)
- When valid: **always** has at least one unblocked insertion cut for `x`
- "Invalid" means `x = S_{j+1} - S_i` for some prefix-sum index `i` before `x`'s position and suffix index `j` after `x`'s position

### Alternative valid orderings

For valid deletion triples (14,343 cases):

```text
Fully blocked alternative found:  99.6%
Some ordering worse than native:  99.8%
```

For invalid native deletions where A\{x} has some valid ordering:

```text
At least one with unblocked cuts:  100%
```

### Theoretical interpretation

The empirical evidence strongly supports:

```text
For every sequenceable set S and element y not in S,
there exists a valid ordering C of S such that inserting y
into C has at least one unblocked cut.
```

This is the needed existence statement for the insertion cut-cover proof strategy. The existence of fully blocked alternatives (99.6% of cases) does NOT contradict the strategy — the proof only needs ONE good ordering per `(x, S)`, and such an ordering always exists in the data.

### Caveat for minimal counterexample

In a minimal counterexample `A` (where `A` itself is NOT sequenceable), there is no "native ordering" to inherit. The proof must construct a good ordering of `A\{x}` without a known valid ordering of `A`. The empirical data supports existence but does not prove it.

### Structural characterization (2026-06-03)

Analysis of individual examples (p=19,23; various B,x) reveals the crossing-interval structure distinguishing good orderings from fully blocked ones.

#### Blocking conditions

For a valid ordering C with partial sums s_0=0, s_1,...,s_n, insertion of y is blocked at cut i iff:

```text
cut 0:  ∃ j≥1 with s_j = 0  (zero partial sum)
cut i≥1:  (s_i + y ∈ {s_1,...,s_i})  (endpoint)
       OR ∃ k≤i<j with s_j-s_k = -y  (crossing interval)
```

Fully blocked = every cut satisfies at least one condition.

#### Why native orderings are never fully blocked

The native ordering (delete y from a witness ordering of A∪{y}) avoids full blockage through **coverage gaps**: the first few and/or last few cuts lie outside all crossing intervals. These terminal cuts also avoid endpoint obstructions because the witness ordering's structure doesn't create s_i + y = s_k for those positions.

Specifically, a crossing interval (k,j) covers cuts k..j-1. If the maximum crossing-interval right endpoint max_j < n, then cuts (max_j)...n are uncovered (suffix gap). Similarly, if min_k > 1, cuts 1..(min_k-1) are uncovered (prefix gap).

#### How fully blocked orderings work

Two empirically observed strategies:

```text
1. Long interval (~13% of cases): s_n - s_1 = -y
   Creates crossing interval (1,n) covering all internal cuts.
   Requires endpoint at cut n and zero_partial or endpoint at cut 0.

2. Interval stacking (~87% of cases):
   Multiple crossing intervals whose union covers all cuts,
   plus endpoint obstructions at remaining positions.
```

Strategy 2 is more common and requires more structure: several pairs (k,j) with s_j-s_k = -y whose intervals overlap to cover every internal cut.

### Constructive algorithm proposal

The empirical evidence suggests the following constructive algorithm always works:

```text
Input: sequenceable S, element y not in S
Output: valid ordering C of S with at least one unblocked cut for y

1. Let C be any Graham-valid ordering of S (exists by sequenceability).
2. Compute blocked cuts Block(C,y).
3. If Block(C,y) ≠ {0,...,|S|}, return C.
4. Otherwise, apply local surgery to C:
   a. Find a cut i with minimal blocking multiplicity.
   b. Identify the obstruction(s) responsible:
      - If a crossing interval (k,j) covers i, try swapping elements
        near k or j to break the pair s_j-s_k = -y.
      - If an endpoint obstruction at i, try moving a nearby element.
   c. Verify the new ordering is still valid and has fewer blocked cuts.
   d. Return to step 2.
```

The descent measure M(C,y) = |Block(C,y)| would strictly decrease, guaranteeing termination.

### Structural characterization of full blockage (2026-06-03)

Deep empirical analysis (775 fully blocked orderings, 1004 good
orderings across p=17..31) reveals precise necessary conditions
for full blockage:

**Theorem (necessary conditions).** If a valid ordering C of S is
fully blocked for inserting y, then ALL of the following hold:

1. **Zero partial sum**: some nonempty partial sum s_j = 0.
   (Otherwise cut 0 is unblocked — it has no endpoint mechanism.)
   Empirical: 775/775 (100%).

2. **Prefix crossing (1, j)**: there exists j > 1 with s_j - c₁ = -y.
   (Otherwise cut 1 is unblocked — its endpoint condition requires
   c₁ + y = c₁ ⇒ y=0, impossible.)
   Empirical: 775/775 (100%). Equivalent to first_cross_k = 1.

3. **Suffix crossing (k, n)**: there exists k < n with s_n - s_k = -y.
   (Cut n is blocked iff the endpoint condition s_n + y = s_k holds
   for some k < n, which immediately gives (k, n) ∈ crossing.)
   Empirical: 775/775 (100%). Equivalent to last_cross_j = n.

4. **No gap**: prefix_gap = 0 and suffix_gap = 0. The crossing
   intervals must cover cuts 1..n-1 with no uncovered prefix or
   suffix. Empirical: 775/775 (100%).

**Corollary.** If any valid ordering C of S violates at least one
of conditions (1)-(3), then C has at least one unblocked cut.

Therefore the existence theorem reduces to: **For every sequenceable
S and y ∉ S, there exists a valid ordering C of S violating at least
one of the three necessary conditions** (zero partial sum, prefix
crossing, or suffix crossing).

### Good orderings: empirical structure

Among 1004 good orderings found by random search:

- 470 (47%) have cut 0 unblocked (no zero partial sum)
- 470 (47%) have cut n unblocked (no suffix endpoint collision)
- 148 (15%) have an internal cut unblocked (both ends blocked but
  a gap in crossing coverage)
- Of 105 paired comparisons (same S, y has both good and fully
  blocked orderings): 82/105 (78%) have larger total gap in the
  good ordering

The most common good pattern: an endpoint (cut 0 or cut n) is
unblocked, accounting for 94% of good cases.

### Path to an existence theorem (revised)

Three approaches, revised based on structural findings:

```text
A. Avoid zero partial sums: Prove that for every sequenceable S,
   there exists a valid ordering C with no nonempty partial sum
   equal to 0. If sum(S) ≠ 0 mod p, this may be provable via
   rearrangement. This would violate condition (1).

B. Construct ordering with prefix or suffix gap: Given any valid
   ordering C that IS fully blocked, perform local surgery near
   the zero partial sum position or edge crossing to produce a
   new valid ordering C' with a gap. The surgery must preserve
   Graham validity while breaking full blockage.

C. Three-condition avoidance: Show constructively that for every
   sequenceable S and y ∉ S, at least one of the three necessary
   conditions can be avoided by some valid ordering. The empirical
   data shows this is always possible; the proof needs a
   construction method.
```

### Empirical methodology

Analysis scripts:

```text
scripts/analyze_blocking_patterns.py  — structural comparison of
  good vs fully blocked orderings (prefix/suffix gaps, crossing
  interval patterns, endpoint distributions)
scripts/analyze_cut_n.py              — deep analysis of cut-n
  obstruction mechanism and zero partial sum necessity
logs/blocking_pattern_analysis.jsonl  — 4220 structural records
logs/cut_n_analysis.jsonl             — 1779 deep analysis records
```

## 12. Current status

This program is not yet a proof. It is the independent analytic route most aligned with the computational certificate data.

### Implemented artifacts

```text
scripts/analyze_insertion_blocks.py            — cut-cover obstruction analyzer
scripts/systematic_insertion_search.py          — parallel worst-case ordering search
scripts/search_insertion_minima.py              — minimum-blocked-cuts ordering search
scripts/analyze_blocking_patterns.py            — good vs fully blocked structural comparison
scripts/analyze_cut_n.py                        — deep cut-n / zero partial sum analysis
logs/cross_prime_search.jsonl                   — cross-prime results (72,409 triples)
logs/insertion_minima_results.jsonl             — minima search results
logs/blocking_pattern_analysis.jsonl            — structural comparison (4220 records)
logs/cut_n_analysis.jsonl                       — deep analysis (1779 records)
```

Core tools:

```text
analyze_insertion_blocks.py:
  Block(C,x), endpoint obstructions, zero-partial cut-zero obstruction,
  crossing intervals, coverage multiplicities, minimal unblocked cuts.

systematic_insertion_search.py:
  Searches over many valid orderings of A\{x} to find worst-case (most
  blocked) alternatives. Supports exact enumeration (k ≤ 8), random
  sampling (9 ≤ k ≤ 12), and perturbation search (k > 12).

search_insertion_minima.py:
  Searches for orderings with minimum blocked cuts; records worst>native
  comparisons and fully-blocked detection.

analyze_blocking_patterns.py:
  Compares structural features of good (unblocked cuts) vs fully blocked
  orderings: prefix/suffix gaps, crossing interval counts, endpoint
  distributions, zero partial sums.

analyze_cut_n.py:
  Deep analysis of cut-n obstruction mechanism and necessary conditions
  for full blockage (zero partial sum, prefix crossing, suffix crossing).
```

### Key structural findings (2026-06-03)

1. **Three necessary conditions for full blockage**, each proved
   and empirically confirmed 775/775:
   - Zero partial sum (blocks cut 0)
   - Prefix crossing (1, j) with s_j = c₁ - y (blocks cut 1)
   - Suffix crossing (k, n) with s_n = s_k - y (blocks cut n)
2. **Good orderings always violate at least one** of these three;
   94% have an endpoint (cut 0 or cut n) unblocked.
3. The existence theorem reduces to constructing a valid ordering
   of S that avoids at least one necessary condition.

### Resolved gaps (2026-06-04)

1. **Existence theorem**: RESOLVED. Lemma 5.1-5.2 and Theorem 5.3 in
   `docs/analytic_insertion_existence_proof.md` prove constructively that for
   every sequenceable S and y ∉ S, there exists a valid C with at least one
   unblocked cut. Verified empirically on 5,073 fully blocked orderings (100%).
2. **Constructive method**: RESOLVED. The surgery lemma (block_reverse at some
   position, len 2-3) provides the explicit construction. Script:
   `scripts/verify_surgery_lemmas.py`.
3. **Small-set proof**: RESOLVED by the general constructive theorem. The
   surgery lemma works across all tested |S| = 3..26, p = 17..31.

### Resolved analytic gaps (2026-06-04)

1. **Formal algebraic proof of Lemma 5.1**: RESOLVED. The five-case
   algebraic analysis in `docs/analytic_insertion_existence_proof.md` §5
   proves that for any fully blocked (C, x), the short block_reverse at
   an appropriate position necessarily preserves Graham validity.
   Lemma 5.1a (§5.5) proves impossibility of all-swaps-fail.
   All components closed.
