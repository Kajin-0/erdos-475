# Independent analytic program for Graham / Erdos 475

This document begins an independent proof attempt for the remaining intermediate regime. It does not rely on a published large-prime reduction theorem.

## Target theorem

Let `p` be prime and let

```text
A subset F_p^*
t = |A|
B = F_p^* \ A
|B| = p - 1 - t
```

The finite verification currently covers all exposed residue through:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

The missing independent analytic theorem can be stated as:

```text
For every prime p >= 37 and every A subset F_p^* with 13 <= |A| <= p - 4,
there is an ordering a_1,...,a_t of A such that the partial sums
s_i = a_1 + ... + a_i are pairwise distinct modulo p.
```

Equivalently, in complement notation:

```text
For every prime p >= 37 and every B subset F_p^* with 3 <= |B| <= p - 14,
A = F_p^* \ B has a valid ordering.
```

## Strategy choice

The most direct independent route is an induction / insertion strategy.

Given a valid ordering of `A \ {x}`, try to insert `x` into one of the cuts. If every cut is blocked, the existing ordering has a strong additive-interval obstruction. The goal is to prove that such obstructions cannot persist for all `x` in a minimal counterexample.

This converts the global ordering problem into a family of interval-covering statements in the partial-sum path.

## Definitions

Let

```text
C = (c_1,...,c_n)
```

be an ordering of a set `S subset F_p^*`. Define partial sums with the empty sum included:

```text
s_0 = 0
s_i = c_1 + ... + c_i, 1 <= i <= n
```

The path of partial sums is:

```text
P(C) = (s_0,s_1,...,s_n)
```

The ordering is called internally valid if

```text
s_1,...,s_n are pairwise distinct.
```

When useful, a stronger condition is used:

```text
s_0,s_1,...,s_n are pairwise distinct.
```

The original problem only requires internal validity. The stronger condition is cleaner for insertion lemmas but must be relaxed later to handle zero-sum sets.

## Lemma 1. Strong insertion cut criterion

Assume `C=(c_1,...,c_n)` is strongly valid, so `s_0,...,s_n` are pairwise distinct. Let `x notin S`.

For a cut `i`, where `0 <= i <= n`, insert `x` after `c_i`:

```text
(c_1,...,c_i, x, c_{i+1},...,c_n)
```

with the convention that `i=0` means insertion at the beginning.

Then the inserted ordering is strongly valid if and only if both conditions hold:

```text
(1) s_i + x is not in {s_0,...,s_i}
(2) for no pair k <= i < j do we have s_j - s_k = -x
```

### Proof

The new partial sums are:

```text
s_1,...,s_i,
s_i + x,
s_{i+1}+x,...,s_n+x.
```

The old prefix sums remain distinct because `C` was strongly valid. The shifted suffix sums remain distinct for the same reason.

The inserted point `s_i+x` cannot collide with a shifted suffix point `s_j+x`, because that would imply `s_i=s_j`, impossible for `j>i`.

Thus the only possible collisions are:

```text
s_i + x = s_k          for some k <= i,
```

or

```text
s_j + x = s_k          for some k <= i < j.
```

The second equality is equivalent to:

```text
s_j - s_k = -x.
```

This proves the criterion.

## Lemma 2. Cut-cover obstruction

Under the hypotheses of Lemma 1, if `x` cannot be inserted into any cut of `C`, then every cut `i in {0,...,n}` is blocked by at least one of the following events:

```text
A_i(x): s_i + x belongs to {s_0,...,s_i}
B_i(x): there exist k <= i < j with s_j - s_k = -x
```

Equivalently, define the crossing interval associated to a pair `(k,j)` with `k<j` and `s_j-s_k=-x` as:

```text
I(k,j) = {i : k <= i < j}.
```

Then the cuts are covered by:

```text
{ i : A_i(x) occurs } union union_{s_j-s_k=-x} I(k,j).
```

### Proof

Immediate from Lemma 1.

## Lemma 3. Minimal-counterexample obstruction principle

Suppose `A` is a minimal counterexample under set size: every proper subset of `A` has a valid ordering, but `A` has no valid ordering.

Then for every `x in A` and every valid ordering `C` of `A \ {x}`, the cut-cover obstruction of Lemma 2 holds, after adjusting the endpoint convention if `C` is only internally valid.

### Proof sketch

If some cut allowed insertion of `x`, then inserting `x` into `C` would give a valid ordering of `A`, contradicting that `A` is a counterexample.

The only technical issue is that the original problem permits a prefix sum equal to `0`; therefore the strong version must be replaced by an internal-validity version. This requires keeping track of collisions only among nonempty partial sums.

## Lemma 4. Internal insertion criterion, project version

Let `C` be internally valid, so `s_1,...,s_n` are distinct but `0` may coincide with one of them. Insert `x` after cut `i`.

The inserted ordering is internally valid if and only if the following collision types are absent:

```text
(1) s_i + x = s_k for some 1 <= k <= i
(2) s_j + x = s_k for some 1 <= k <= i < j <= n
(3) s_i + x = s_j + x for some j > i
(4) collisions inside the old prefix or shifted suffix
```

Because `C` is internally valid, types `(3)` and `(4)` are automatically absent except for the impossible equality `s_i=s_j` with `j>i` when `i>=1`. For `i=0`, the inserted first partial sum is `x`, and the same criterion holds with the prefix set empty among nonempty sums.

A compact sufficient condition for a valid insertion is therefore:

```text
s_i + x notin {s_1,...,s_i}
```

and

```text
there do not exist 1 <= k <= i < j <= n with s_j - s_k = -x.
```

This is slightly weaker than the strong criterion because `s_0=0` is not itself a forbidden previous partial sum.

## Main missing analytic lemma

The induction program reduces the intermediate regime to the following obstruction-impossibility statement.

### Obstruction-impossibility lemma

Let `p >= 37`, let `A subset F_p^*`, and let `13 <= |A| <= p-4`. Suppose every proper subset of `A` has a valid ordering.

Then there exists `x in A` and a valid ordering `C` of `A \ {x}` such that at least one cut is not blocked by the insertion obstruction for `x`.

Equivalently, no minimal counterexample can satisfy the cut-cover obstruction for every `x in A` and every valid ordering of `A \ {x}`.

If this lemma is proved, the intermediate-regime theorem follows immediately by induction on `|A|`.

## Proof of reduction from obstruction-impossibility to the target theorem

Assume the obstruction-impossibility lemma.

Let `A subset F_p^*` with `13 <= |A| <= p-4`. Suppose, for contradiction, that `A` has no valid ordering. Choose such an `A` of minimal size.

For every `x in A`, the set `A \ {x}` is smaller, hence has a valid ordering by minimality. By the obstruction-impossibility lemma, for some `x` and some valid ordering `C` of `A \ {x}`, there is an unblocked cut. Inserting `x` into that cut gives a valid ordering of `A`, contradiction.

Therefore no counterexample exists.

## What remains to prove

The remaining hard step is proving the obstruction-impossibility lemma.

Useful directions:

```text
1. Bound how many cuts can be blocked by a fixed difference -x.
2. Show that a valid ordering of A\{x} can be chosen to minimize blocked cuts.
3. Use rotations, reversals, or local swaps to reduce the cut-cover unless insertion is possible.
4. Show that persistent cut-cover obstructions force an additive structure incompatible with A subset F_p^* in the intermediate range.
5. Connect the obstruction intervals I(k,j) to zero-sum consecutive blocks and apply local surgery.
```

## Next subproblem

Prove or disprove the following sharper lemma.

### Sparse crossing lemma

Let `C` be a valid ordering of a set `S` with `|S|=n`, and let `x notin S`. If the number of pairs `(k,j)` with

```text
1 <= k <= j <= n,
s_j - s_k = -x
```

is less than a threshold depending on `n`, then some cut admits insertion of `x`.

This is true in the trivial form that if the crossing intervals plus endpoint obstructions fail to cover all cuts, insertion succeeds. The useful version must give a structural or quantitative condition forcing such a failure.

## Current status

This document gives a real reduction path for a new analytic proof, but the complete proof is not finished.

The next mathematical task is to prove the obstruction-impossibility lemma or find a stronger replacement.
