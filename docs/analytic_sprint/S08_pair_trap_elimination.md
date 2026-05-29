# S08. Pair-trap elimination attack

This file attacks the next obstruction after S07.

S07 reduced signed-interval failures to:

```text
1. pair-trap / equal-difference relation inside Z;
2. external bridge obstruction.
```

The goal here is to eliminate or compress pair traps so that the only primitive hard case is external bridge overlap.

## Setup

Let

```text
Z = z_1 ... z_m
```

be a shortest zero interval in a `D_short`-minimal ordering, with internal prefix sums

```text
T_0 = 0,
T_i = z_1 + ... + z_i,
T_m = 0.
```

Shortestness gives:

```text
T_0,T_1,...,T_{m-1} are pairwise distinct.
```

Equivalently, no proper nonempty contiguous subinterval of `Z` has sum zero.

For `0 <= i < j <= m`, define the oriented interval sum

```text
U(i,j) = T_j - T_i = z_{i+1}+...+z_j.
```

## Pair trap definition

A pair trap is a nontrivial equal-interval-sum relation

```text
U(i,j) = U(k,l)
```

with

```text
0 <= i < j <= m,
0 <= k < l <= m,
(i,j) != (k,l).
```

Equivalently:

```text
T_j - T_i = T_l - T_k.
```

or

```text
T_j + T_k = T_l + T_i.
```

This is exactly the equal-difference obstruction produced by local-local collision after q-compression.

## First cleanup: shared endpoints are impossible

### Lemma S08.1: pair traps do not share exactly one endpoint

If

```text
U(i,j)=U(k,l)
```

and the two intervals share the same left endpoint, then they share the same right endpoint.

Likewise, if they share the same right endpoint, then they share the same left endpoint.

### Proof

If `i=k`, then

```text
T_j - T_i = T_l - T_i,
```

so

```text
T_j = T_l.
```

If `j,l < m`, prefix distinctness gives `j=l`.  If one of `j,l` equals `m`, then `T_m=T_0=0`, so equality with another `T_r` forces `r=0` or `r=m`.  Since `r` is a right endpoint greater than the common left endpoint, the only admissible equality is again the same endpoint except for the whole-zero endpoint degeneracy.  That degeneracy corresponds to the full interval `Z`, not a proper pair-trap inside a shortest-zero analysis.

The same argument applies if `j=l`: then `T_i=T_k`, hence `i=k` except for the full-zero endpoint degeneracy. ∎

## Classification by interval geometry

After removing shared-endpoint degeneracies, two distinct intervals have one of three geometric types.

```text
TYPE A: disjoint
  i < j < k < l     or     k < l < i < j

TYPE B: crossing
  i < k < j < l     or     k < i < l < j

TYPE C: nested
  i < k < l < j     or     k < i < j < l
```

By symmetry, assume the displayed first ordering in each case.

## Type C nested pair trap

Assume

```text
i < k < l < j
```

and

```text
U(i,j)=U(k,l).
```

Then

```text
U(i,k) + U(l,j) = 0.
```

### Proof

Since

```text
U(i,j)=U(i,k)+U(k,l)+U(l,j),
```

and `U(i,j)=U(k,l)`, subtract to get

```text
U(i,k)+U(l,j)=0.
```

∎

### Meaning

A nested pair trap gives a two-piece separated zero relation:

```text
sum(left gap) + sum(right gap) = 0.
```

This is not itself a contiguous zero interval, but it is a strong structure: two separated flank blocks have opposite sums.

### Attack move

Bring the two flank blocks together by moving the middle interval `z_{k+1}...z_l` or rotating the containing block.

If the flank blocks become contiguous, they form a shorter zero interval because their total length is

```text
(k-i) + (j-l) = (j-i) - (l-k) < j-i <= m.
```

Therefore nested pair traps should either:

```text
1. produce D_short descent after a block rotation/exchange;
2. create an external bridge collision during the rotation;
3. reduce to a smaller pair trap.
```

## Type B crossing pair trap

Assume

```text
i < k < j < l
```

and

```text
U(i,j)=U(k,l).
```

Then

```text
U(i,k)=U(j,l).
```

### Proof

Expand:

```text
U(i,j)=U(i,k)+U(k,j),
U(k,l)=U(k,j)+U(j,l).
```

Equality gives

```text
U(i,k)=U(j,l).
```

∎

### Meaning

A crossing pair trap produces an equal-sum relation between two disjoint flank intervals.

This is structurally simpler than the original crossing relation.

### Attack move

Exchange the two equal-sum flank blocks.  Because their sums are equal, endpoints outside the combined window are preserved.

The combined window is:

```text
A B C = z_{i+1}...z_k   z_{k+1}...z_j   z_{j+1}...z_l
```

with

```text
sum(A)=sum(C).
```

Swapping `A` and `C` keeps the total window sum fixed and preserves the boundary endpoint after the window.

Expected outcome:

```text
1. internal collision profile decreases;
2. a shorter zero interval appears;
3. an external bridge collision is exposed.
```

## Type A disjoint pair trap

Assume

```text
i < j < k < l
```

and

```text
U(i,j)=U(k,l).
```

This is already an equal-sum relation between disjoint blocks.

### Attack move

Swap the two equal-sum blocks:

```text
A M B  ->  B M A
```

where

```text
A = z_{i+1}...z_j,
M = z_{j+1}...z_k,
B = z_{k+1}...z_l,
sum(A)=sum(B).
```

Because `sum(A)=sum(B)`, the total sum of `A M B` and `B M A` is the same, and endpoints after the window are preserved.

The changed endpoints inside the window are translations by

```text
sum(B)-sum(A)=0
```

at the window boundary but not inside the blocks.

This is the cleanest case for a two-block exchange lemma.

## Lemma S08.2: pair traps reduce to separated equal-sum blocks or separated zero flanks

Every nontrivial pair trap inside `Z` is one of:

```text
A. disjoint equal-sum blocks;
B. crossing relation, equivalent to disjoint equal-sum flank blocks;
C. nested relation, equivalent to separated zero-flank relation.
```

Thus pair traps never remain arbitrary four-endpoint equations.  They reduce to block geometry.

### Proof

Use the interval geometry classification above.  Shared endpoints are eliminated by Lemma S08.1.  Type A is already disjoint equal-sum.  Type B gives equal flank sums by the crossing calculation.  Type C gives zero-sum flanks by the nested calculation. ∎

## Candidate theorem S08.3: separated equal-sum exchange theorem

Let `R` be `D_short`-minimal and let `Z` be a shortest zero interval.  Suppose inside `Z` there are two disjoint nonempty intervals `A` and `B` with

```text
sum(A)=sum(B).
```

Then exchanging `A` and `B` either:

```text
1. decreases D_short;
2. creates an external bridge obstruction;
3. creates a nested zero-flank relation with smaller total support;
4. preserves all internal endpoint data, forcing periodicity of the internal prefix set.
```

The fourth case should be impossible unless the internal endpoint set is invariant under a nonzero translation, which in `F_p` forces it to be all of `F_p`.  That is incompatible with a short proper interval unless the block is field-sized.

## Candidate theorem S08.4: separated zero-flank compression theorem

Let `R` be `D_short`-minimal and suppose inside `Z` there are separated nonempty blocks `A` and `C` with

```text
sum(A)+sum(C)=0.
```

Then moving `A` next to `C` either:

```text
1. creates a shorter zero interval and decreases D_short;
2. creates an external bridge obstruction;
3. creates a disjoint equal-sum pair trap with smaller support.
```

## Strategic result

If S08.3 and S08.4 are proved, pair traps reduce to external bridge.

Then the entire analytic proof has the following compression:

```text
q-through-Z failure
  -> signed interval or external bridge
  -> q-zero compression
  -> pair trap or external bridge
  -> pair-trap exchange/compression
  -> external bridge
```

So the only primitive hard obstruction becomes:

```text
persistent external bridge overlap.
```

## What must be tested next

Before writing more prose, small-prime tests should classify whether S08.3/S08.4 are too optimistic.

The test should generate shortest-zero intervals and pair traps, then try:

```text
1. swap disjoint equal-sum blocks;
2. swap crossing flank equal-sum blocks;
3. bring nested zero flanks together;
4. record whether D_short decreases or whether new collisions are external.
```

This is low-compute and high-value.

## Immediate script target

```text
scripts/test_pair_trap_moves.py
```

The script should not attempt to prove the theorem.  It should produce minimal counterexamples to S08.3/S08.4 or confirm the obstruction classification on small primes.

## Status

```text
S08.1--S08.2: strong algebraic classification.
S08.3--S08.4: main open pair-trap elimination theorems.
Risk: ORANGE.
Payoff: reduces all local/internal obstructions to external bridge.
```
