# S06. Signed-interval elimination attack

This file attacks the easier obstruction from S04 before confronting external bridge overlap.

## Goal

Reduce all local cross-side insertion failures to either:

```text
1. a defect-decreasing move;
2. a pair-trap/equal-difference obstruction;
3. an external bridge obstruction.
```

If successful, the hard case becomes only persistent external overlap.

## Setup

Let

```text
R = X Z q Y,
Z = z_1 ... z_m,
sum(Z)=0,
q outside Z,
```

and let

```text
T_0=0,
T_k=z_1+...+z_k,
T_m=0.
```

Assume `Z` is a shortest zero interval, so

```text
T_0,T_1,...,T_{m-1} are pairwise distinct.
```

For useful insertion position `1 <= k < m`, the local endpoint set is

```text
E_k={T_0,...,T_k} union {q+T_k,...,q+T_m}.
```

A local cross-side collision is

```text
T_a = q + T_b,
0 <= a <= k <= b <= m,
a != b.
```

Equivalently:

```text
q = T_a - T_b.
```

## Interval meaning

If `a < b`, then

```text
q + z_{a+1}+...+z_b = 0.
```

So the block

```text
q, z_{a+1},...,z_b
```

has zero sum.

If `b < a`, then

```text
q = z_{b+1}+...+z_a.
```

Equivalently

```text
-q + z_{b+1}+...+z_a = 0,
```

but `-q` need not be an atom of `S`.  Therefore the `a<b` case is more directly repairable.

Under the insertion constraints `a <= k <= b`, the common generic case is `a <= b`.

## Key observation: signed collision creates a new zero block containing q

When `a < b`, the signed collision means inserting `q` immediately before `z_{a+1}` or immediately after `z_b` can create a contiguous zero block involving `q` and the subinterval `z_{a+1}...z_b`.

This sounds bad, but it is useful because that new zero block has length

```text
(b-a)+1.
```

Since `z_{a+1}...z_b` is a proper subinterval of `Z`,

```text
1 <= b-a < m.
```

Thus the new zero block has length at most `m`.

If it has length `<m`, it contradicts shortestness after the move only if the move is not defect-decreasing.  If it has length `m`, then `b-a=m-1`, so the subinterval omits exactly one atom of `Z`.

This edge case is highly structured.

## Lemma S06.1: proper signed interval gives shorter q-zero candidate unless endpoint-sized

Assume

```text
q + z_{a+1}+...+z_b = 0
```

with

```text
0 <= a < b <= m,
1 <= b-a < m.
```

Then the block consisting of `q` and that subinterval has zero sum and length

```text
L = (b-a)+1.
```

If

```text
b-a <= m-2,
```

then

```text
L <= m-1,
```

so any ordering that makes this block contiguous contains a zero interval shorter than `Z`.

### Interpretation

A local insertion that creates such a block cannot be the desired repair directly, but it identifies a shorter obstruction involving `q`.  Therefore a D-minimal ordering should avoid producing this pattern unless the block is not contiguous or an external bridge compensates.

## Lemma S06.2: signed interval with small support suggests q should be absorbed into Z

Suppose `q + I = 0` where `I` is a proper interval of `Z` with length `r <= m-2`.

Then replacing the active interval `Z` by the shorter q-interval gives a lower shortest-zero length obstruction after a suitable local move, unless the move also destroys enough existing collision excess to improve `D`.

This gives a fork:

```text
1. defect improves -> done;
2. shorter q-zero interval appears -> contradicts choice of active Z in a globally minimal counterexample after reselecting active interval;
3. an external collision appears -> external bridge branch.
```

### Current status

This lemma is not yet fully proved.  The issue is that creating a shorter zero interval after a move is not automatically a contradiction unless the move preserves or improves earlier defect coordinates.  It must be stated using the chosen defect ordering.

## Endpoint-sized signed interval

The hard signed case is:

```text
b-a = m-1.
```

Then `I` is `Z` with one endpoint-side atom omitted.

Since

```text
sum(Z)=0,
```

we have:

```text
sum(I) = -z_omit.
```

The relation

```text
q + sum(I)=0
```

becomes

```text
q = z_omit.
```

But `q` is outside `Z`, and `S` is a set, so `q` cannot equal an atom inside `Z`.

Therefore endpoint-sized signed intervals are impossible in the direct `a<b` case.

## Lemma S06.3: endpoint-sized direct signed intervals are impossible

Assume

```text
q + z_{a+1}+...+z_b = 0,
```

where `Z=z_1...z_m`, `sum(Z)=0`, and `b-a=m-1`.

Then the interval `z_{a+1}...z_b` omits exactly one atom `z_h` of `Z`, so

```text
z_{a+1}+...+z_b = -z_h.
```

Thus

```text
q - z_h = 0,
q=z_h,
```

contradicting that `q` is outside `Z` and atoms are distinct.

Therefore the only direct signed-interval local collisions have interval length at most `m-2` and create a strictly shorter q-zero candidate. ∎

## Reverse signed case

If `b<a`, then

```text
q = z_{b+1}+...+z_a.
```

This does not directly create a zero block using `q`, but since `sum(Z)=0`, the complementary interval has sum

```text
-z_{b+1}-...-z_a = -q.
```

Therefore

```text
q + sum(complement interval) = 0.
```

The complement interval inside `Z` has length

```text
m-(a-b).
```

If this complement length is at most `m-2`, the same shorter q-zero candidate appears.  If it is `m-1`, then the omitted interval has length `1`, so `q` equals the omitted atom, impossible.

## Lemma S06.4: every signed interval obstruction gives a shorter q-zero candidate

Let a cross-side local collision occur:

```text
T_a = q + T_b,
a != b.
```

Then either:

```text
1. q equals an atom of Z, impossible; or
2. there exists a proper interval I of Z with length <= m-2 such that q + sum(I)=0.
```

### Proof

If `a<b`, use `I=z_{a+1}...z_b`.  If `|I|=m-1`, Lemma S06.3 gives `q=z_h`, impossible.  Otherwise `|I|<=m-2`.

If `b<a`, use the complementary interval in `Z` outside `z_{b+1}...z_a`.  Since `sum(Z)=0` and `q=sum(z_{b+1}...z_a)`, the complement has sum `-q`.  If its length is `m-1`, then the omitted direct interval has length `1`, hence `q` is that single atom, impossible.  Otherwise the complement has length at most `m-2`. ∎

## Consequence

Local signed-interval failures never merely preserve the active shortest zero interval.  They expose a strictly shorter zero-sum structure involving `q` and a proper subinterval of `Z`.

This is powerful because a shortest-zero-interval proof can exploit it.

## Remaining proof gap

The shorter q-zero structure may not be contiguous in the moved ordering.  To turn it into descent, we need one more lemma.

## Target Lemma S06.5: q-zero compression lemma

Let `Z` be an active shortest zero interval in a D-minimal ordering, and suppose there is a proper subinterval `I` of `Z` with

```text
q + sum(I)=0,
|I| <= m-2.
```

Then one of the following holds:

```text
1. moving q next to I creates a shorter zero interval and improves the defect profile;
2. moving q next to I creates an external bridge collision;
3. a two-block exchange around I decreases collision excess;
4. the configuration contains a pair-trap equal-difference relation.
```

If S06.5 is proved, signed intervals are eliminated and all hard failures reduce to external bridge / pair trap.

## Why S06.5 is a strong target

It is local, finite, and algebraic.  It should be much easier than the full weighted state machine.

It is also a good AI target because the statement is precise enough for proof attempts and counterexample searches.

## Next action

Write a falsification script for S06.5 on small primes:

```text
Find shortest zero interval Z, outside adjacent q, and proper interval I with q+sum(I)=0.
Test whether any move placing q next to I improves D or whether all failures are external/pair-trap.
```

Do not brute-force large p.  Use small p to refine the lemma statement.

## Status

```text
S06.1--S06.4: promising, mostly algebraic.
S06.5: main open signed-interval compression lemma.
Risk: ORANGE.
Payoff: reduces the problem to external bridge overlap.
```
