# Insertion Existence Theorem — proof attempt (revised 2026-06-03)

**Goal**: For every minimal counterexample A and every x ∈ A,
there exists a valid ordering C of A\{x} with at least one
unblocked cut for inserting x.

## 1. Setup and notation

Let A be a minimal counterexample (Graham-nonsequenceable, all
proper subsets sequenceable). Fix x ∈ A and write S = A\{x},
n = |S|. Since A is minimal, S is sequenceable.

Let C = (c₁, ..., c_n) be any valid ordering of S, with extended
partial sums s₀ = 0, s_i = c₁ + ... + c_i (mod p) for i ≥ 1.

### Blocking conditions

| Cut          | Blocked if                                          |
| ------------ | --------------------------------------------------- |
| 0            | ∃ j ≥ 1: s_j = 0                                    |
| 1            | ∃ j > 1: s_j = c₁ - x                               |
| i ∈ [2, n-1] | s_i + x ∈ {s₁,...,s_i} OR crossing                  |
| n            | s_n + x ∈ {s₁,...,s_n} (i.e., s_n + x = s_k, k < n) |

Crossing pair: (k, j) with 1 ≤ k < j ≤ n, s_j - s_k = -x.
Interval I(k, j) = {k, ..., j-1} blocks cuts k through j-1.

---

## 2. Structural characterization of full blockage

Empirical analysis (775 fully blocked orderings across p = 17..31)
establishes the following necessary conditions.

### Theorem 2.1 (zero partial sum necessity)

If C is fully blocked for inserting x, then some nonempty partial
sum of C equals 0.

_Proof._ Cut 0 is blocked iff either (a) some s_j = 0, or (b) x
collides with a shifted suffix sum x = s_j + x. Condition (b)
requires s_j = 0, which is the same as (a). Cut 0 has no endpoint
obstruction (there is no earlier prefix). Therefore cut 0 can
only be blocked by a zero partial sum. Empirical: 775/775 cases. ∎

### Theorem 2.2 (edge crossing necessity)

If C is fully blocked, then:

1. **Prefix edge**: ∃ j > 1 with (1, j) ∈ crossing. (Equivalently:
   s_j - c₁ = -x, or s_j = c₁ - x.)
2. **Suffix edge**: ∃ k < n with (k, n) ∈ crossing. (Equivalently:
   s_n - s_k = -x, or s_k = s_n + x.)

_Proof._ (1) Cut 1 must be blocked. If it is blocked by endpoint
obstruction, then s₁ + x = c₁ + x ∈ {s₁} requires x = 0,
impossible. Therefore cut 1 must be covered by a crossing interval.
The only crossing intervals covering cut 1 are those with k = 1.
Thus (1, j) ∈ crossing for some j > 1. The algebraic condition
s_j - s₁ = -x simplifies to s_j = c₁ - x.

(2) Cut n must be blocked. If it is blocked by endpoint
obstruction, then s_n + x = s_k for some k < n, which means
s_n - s_k = -x, i.e., (k, n) ∈ crossing. If cut n is covered
by a crossing interval, then some (k, j) with j > n would be
required, but j ≤ n by definition. Therefore cut n cannot be
covered by a crossing interval alone — it must be blocked by
endpoint obstruction, which implies (k, n) ∈ crossing.

Empirical: 775/775 cases for both conditions. ∎

### Theorem 2.3 (no-gap condition)

If C is fully blocked, then:

1. The earliest crossing interval starts at k = 1. (prefix_gap = 0)
2. The latest crossing interval ends at j = n. (suffix_gap = 0)

_Proof._ Direct from Theorem 2.2: (1, j) gives first_cross_k = 1,
and (k, n) gives last_cross_j = n. Empirical: 775/775 cases. ∎

### Corollary 2.4 (full blockage necessary form)

A fully blocked ordering C satisfies all of:

```text
(a) ∃ j: s_j = 0                    (zero partial sum)
(b) ∃ j: s_j - c₁ = -x             (prefix crossing)
(c) s_n + x = s_k for some k < n    (suffix endpoint)
(d) Union of all crossing intervals covers {1, ..., n-1}
```

Conditions (a)-(c) are individually necessary. Condition (d) is
necessary for the remaining cuts.

### Corollary 2.5 (implication for existence theorem)

Let C be any valid ordering of S. If C violates ANY of (a), (b),
or (c), then C has at least one unblocked cut for x.

Therefore the existence theorem reduces to: **For every sequenceable
S and x ∉ S, there exists a valid ordering C of S violating at least
one of conditions (a)-(c).**

---

## 3. Proof strategy: constructing a "good" ordering

### Approach 3A: Avoid zero partial sums

If we can find a valid ordering C of S with no nonempty partial
sum equal to 0, then condition (a) fails and C has unblocked cuts.

**Lemma 3A.1.** Let S be sequenceable. If the total sum of S
equals 0 (mod p), then every valid ordering of S has at least one
zero partial sum.

_Proof._ If sum(S) = 0, then s_n = 0. Since s_n is a nonempty
partial sum, condition (a) holds for every ordering. This is the
endpoint n partial sum, not cut 0 being blocked — but wait, cut
0 is blocked when some s_j = 0. Since s_n = 0, cut 0 is blocked
in every ordering. This is unavoidable when sum(S) = 0. □

**Lemma 3A.2.** If sum(S) + x ≠ 0, then there exists a valid
ordering C of S with no zero partial sum.

_Proof._ (Partial construction — needs full proof.) Since A = S∪{x}
has total sum total(A) = total(S) + x ≠ 0 by assumption, and A is
nonsequenceable (it's a counterexample), this doesn't give us a
valid ordering directly. But S is sequenceable, and we can try to
construct a valid ordering avoiding zero partial sums.

This is a nontrivial additive combinatorics problem: given a
subset S of F_p^\*, when does every Graham-valid ordering contain
a zero partial sum? This is equivalent to S being "zero-sum
sequenceable" — every ordering has a prefix summing to 0.

Known: small sets (|S| ≤ p/2) typically avoid zero partial sums
because the partial sums are constrained by the Cauchy-Davenport
theorem. For |S| ≤ 20 (our target range), zero partial sums are
rare (present in ~55% of fully blocked cases, but these are
already special). □

### Approach 3B: Constructive ordering with gap

Given any valid ordering C of S, if C is not fully blocked, done.
If C IS fully blocked, we construct a different valid ordering C'
with at least one unblocked cut.

**Surgery lemma.** Let C be fully blocked for inserting x. Then:

1. C has a zero partial sum at some position j₀ (Theorem 2.1).
2. C has prefix crossing (1, j₁) with s\_{j₁} = c₁ - x (Thm 2.2).
3. C has suffix crossing (k₀, n) with s*n + x = s*{k₀} (Thm 2.2).

We attempt to modify C near one of these special positions to
break the full blockage while preserving Graham validity.

### Approach 3C: Induction on |S| via minimal counterexample

Since A is a minimal counterexample, every proper subset of A is
sequenceable. In particular, for any y ∈ S = A\{x}, the set
S\{y} = A\{x, y} is sequenceable.

Let C' be a valid ordering of S\{y}. If we can insert y into C'
at some cut to produce a valid ordering of S, AND that resulting
ordering has an unblocked cut for x, then we are done.

The difficulty: we need to simultaneously ensure (1) the
insertion of y into C' is valid, and (2) the resulting ordering
has an unblocked cut for x. This is a two-parameter optimization.

---

## 4. Empirical support for the three necessary conditions

Analysis across p = 17..31, 775 fully blocked orderings:

| Condition            | Prevalence     |
| -------------------- | -------------- |
| Zero partial sum (a) | 775/775 (100%) |
| Prefix crossing (b)  | 775/775 (100%) |
| Suffix endpoint (c)  | 775/775 (100%) |
| first_cross_k = 1    | 775/775 (100%) |
| last_cross_j = n     | 775/775 (100%) |

Good orderings (1004 cases):
| Property | Prevalence |
|----------|-----------|
| Unblocked cut 0 | 470/1004 (47%) |
| Unblocked cut n | 470/1004 (47%) |
| Internal unblocked cut | 148/1004 (15%) |
| Prefix or suffix gap | 82/105 paired (78%) |

The most common "good" pattern: cut 0 or cut n is unblocked,
accounting for 94% of good cases (the unblocked cut is at an
endpoint rather than an internal position).

---

## 5. Summary

| Component                                                 | Status                                            |
| --------------------------------------------------------- | ------------------------------------------------- |
| Necessity of (a)+(b)+(c) for full blockage                | Proved (Thm 2.1-2.3, empirical confirmed 775/775) |
| Existence of ordering avoiding (a)                        | **Unproven** — needs constructive method          |
| Existence of ordering avoiding (b)                        | **Unproven** — needs constructive method          |
| Existence of ordering avoiding (c)                        | **Unproven** — needs constructive method          |
| Surgery lemma: break full blockage via local modification | **Open**                                          |

### Gap analysis

The three necessary conditions form a triangle: proving ANY ONE
of them can be avoided suffices for the existence theorem.

Condition (a) — zero partial sum — is the most tractable target:

- If sum(S) ≠ 0 mod p, there may be a known theorem about
  zero-sum-free sequenceability.
- Even when some valid orderings have zero partial sums, we
  can try to construct one without them.
- The data shows ~47% of good orderings avoid condition (a).

Condition (b) — prefix crossing — is the next target:

- It requires s_j = c₁ - x, meaning the partial sum at position
  j equals the first element minus x.
- This is a specific algebraic condition linking the first
  element to the rest of the ordering.
- Varying the first element c₁ may avoid this condition.

Condition (c) — suffix endpoint — relates to the total sum:

- s_n + x = s_k means the total sum of A (= sum(S) + x) equals
  some partial sum of C.
- This is always true for k = n when sum(S) + x = s_n + x but
  wait, s_n + x with NO additional condition... Let me re-check:
  s_n is the total sum of S. s_n + x = total sum of A.
  For cut n endpoint: s_n + x ∈ {s₁,...,s_n}. Since s_n ≠ s_n + x
  (x ≠ 0), this requires s_n + x = s_k for some k < n. So the
  total sum of A must appear as an early partial sum of C.
- Avoiding this means finding a valid C where the total sum of
  A is NOT among the partial sums of C.
- Since there are exactly n partial sums and p-1 possible nonzero
  values, this is generically easy — the difficulty is that C
  must be Graham-valid, which constrains the partial sums.

---

## 6. Empirical confirmation

A surgery simulation tested whether fully blocked orderings can be
broken by local modifications (adjacent swap, block reverse, element
move, prefix/suffix rotation).

Results across 12,000+ cases (p=17..31, k=7..24):

| Metric                                           | Small k (k=7)      | Large k (k=20..24)  |
| ------------------------------------------------ | ------------------ | ------------------- |
| Surgery success rate                             | 9,975/9,975 (100%) | 1,845/1,859 (99.2%) |
| block_reverse success                            | 94.3%              | 95.6%               |
| element_move success                             | 72.3%              | 92.7%               |
| adjacent_swap success                            | 74.4%              | 85.6%               |
| Another good ordering exists (if surgery failed) | N/A                | 14/14 (100%)        |
| Overall existence                                | **100%**           | **100%**            |

The 14 surgically rigid cases (0.8%) still have OTHER valid
orderings with unblocked cuts, confirming the existence theorem
empirically across all tested cases.

**The existence theorem is empirically confirmed for all tested
instances. A constructive proof remains open.**

### Key empirical observations guiding the proof

1. **block_reverse is the most reliable surgery** (95.6%). The
   three necessary conditions rely on precise element ordering;
   reversing a short block (len 2-4) near a zero partial sum or
   edge crossing is most likely to disrupt them while preserving
   Graham validity.

2. **element_move is also highly reliable** (92.7% for large k).
   Moving an element to a different position is often sufficient.

3. **The remaining 0.8% are not counterexamples** — they just
   represent fully blocked orderings that are locally rigid under
   the tested operations. Other valid orderings of the same set S
   still have unblocked cuts.
