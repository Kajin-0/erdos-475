# Insertion cut-cover program for Erdős 475

This document records an independent analytic route toward the full theorem.  It is separate from the finite-residue/computational completion track.

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

The original problem only requires the nonempty sums `s_1,...,s_n` to be distinct.  The value `s_0=0` is an auxiliary endpoint and must be handled carefully.

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

Assume `C` is Graham-valid, so `s_1,...,s_n` are pairwise distinct.  The insertion `C^{(i,x)}` is Graham-valid if and only if the following two obstruction types are absent.

### Endpoint obstruction

```text
s_i + x = s_k for some 1 <= k <= i.
```

For `i=0`, this obstruction is empty because there are no earlier nonempty partial sums.

### Crossing obstruction

```text
s_j + x = s_k for some 1 <= k <= i < j <= n.
```

Equivalently,

```text
s_j - s_k = -x.
```

### Proof

The old prefix sums `s_1,...,s_i` remain distinct because `C` is valid.  The shifted suffix sums `s_{i+1}+x,...,s_n+x` remain distinct because translation by `x` is injective.  The inserted sum `s_i+x` cannot collide with a shifted suffix sum `s_j+x` for `j>i`, since this would imply `s_i=s_j`; if `i=0`, this would imply `s_j=0`, which is not automatically forbidden by Graham-validity and must be treated as an endpoint edge case.  For the internal-validity version, the remaining forbidden collisions are exactly endpoint collisions with earlier nonempty prefix sums and crossing collisions from shifted suffix sums into earlier prefix sums.  ∎

## 4. Cut-cover formulation

For fixed `C` and `x`, define the blocked-cut set

```text
Block(C,x) subset {0,1,...,n}
```

as the set of cuts `i` for which insertion of `x` is not Graham-valid.

The endpoint obstruction blocks cut `i` if

```text
s_i + x in {s_1,...,s_i}.
```

For each pair `(k,j)` satisfying

```text
1 <= k <= j <= n,
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

Assume `A` is a minimal counterexample by set size.  Then every proper subset of `A` has a Graham-valid ordering.

For every `x in A`, choose a Graham-valid ordering `C_x` of `A \ {x}`.  If there exists `x` and a cut `i` such that insertion of `x` into `C_x` is Graham-valid, then `A` is not a counterexample.

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
D_x(C) = #{(k,j): 1 <= k <= j <= n and s_j - s_k = -x}.
```

Each pair contributes one blocking interval.  If the union of all crossing intervals and endpoint obstructions fails to cover all `n+1` cuts, insertion succeeds.

The core challenge is that a small number of long intervals can cover all cuts.  Therefore a purely cardinality-based bound on `D_x(C)` is insufficient unless it also controls interval geometry.

Useful quantities:

```text
number of blocking intervals;
maximum interval length;
minimum left endpoint;
maximum right endpoint;
coverage multiplicity per cut;
endpoint obstruction count;
number of zero-sum consecutive blocks in C.
```

## 8. Local surgery strategy

If all cuts are blocked, choose a cut with minimal blocking multiplicity.  Analyze a minimal obstruction responsible for that cut.  Try one of the following operations:

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
  endpoint_obstruction_count
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

If all verified examples admit orderings with many unblocked cuts, that supports the insertion strategy.  If some examples are nearly fully blocked, those become model obstructions for the analytic proof.

## 11. Current status

This program is not yet a proof.  It is the independent analytic route most aligned with the computational certificate data.

The next useful artifact is a script that, given a valid ordering `C` and candidate `x`, computes:

```text
Block(C,x),
endpoint obstructions,
crossing intervals,
coverage multiplicities,
minimal unblocked cuts.
```

This would connect the analytic obstruction program to the existing witness data.
