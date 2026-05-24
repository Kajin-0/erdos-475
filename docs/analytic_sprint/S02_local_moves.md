# S02. Local move algebra

This file records the small library of local moves for the zero-interval proof sprint.

The goal is to keep the move library small enough for a human-readable proof.

## Notation

Let

```text
R = (r_1, ..., r_t)
```

with extended partial sums

```text
P_0 = 0,
P_i = r_1 + ... + r_i.
```

A zero interval is a pair `(i,j)` with `0 <= i < j <= t` and

```text
P_i = P_j.
```

The corresponding block is

```text
r_{i+1}, ..., r_j.
```

## Move M1: adjacent swap

Suppose an adjacent pair is

```text
..., a, b, ...
```

and the prefix before `a` is `Q`.

Before the swap:

```text
Q,
Q+a,
Q+a+b.
```

After swapping to `..., b, a, ...`:

```text
Q,
Q+b,
Q+b+a.
```

Only the intermediate partial sum changes:

```text
Q+a  ->  Q+b.
```

All later partial sums are unchanged.

### Collision criterion

If the old ordering is locally valid except for a collision involving `Q+a`, then the swap repairs it exactly when

```text
Q+b
```

is not already an extended partial sum outside the removed value.

Failure equation:

```text
Q+b = P_k
```

or

```text
b = P_k - Q.
```

Thus a failed adjacent swap pins the neighboring atom as a difference of old partial sums.

## Move M2: cut-and-insert one atom across a block

Let the ordering contain

```text
X, q, Y, Z
```

where

```text
Y = (y_1, ..., y_m).
```

Move `q` to the right of `Y`:

```text
X, Y, q, Z.
```

Let `Q` be the prefix sum before `q`.

Before:

```text
Q
Q+q
Q+q+y_1
Q+q+y_1+y_2
...
Q+q+sum(Y)
```

After:

```text
Q
Q+y_1
Q+y_1+y_2
...
Q+sum(Y)
Q+sum(Y)+q
```

The final partial sum after the moved block is unchanged:

```text
Q + q + sum(Y) = Q + sum(Y) + q.
```

The affected internal partial sums are shifted by `-q`:

```text
Q+q+sum(y_1,...,y_k)  ->  Q+sum(y_1,...,y_k)
```

for `1 <= k <= m`.

Equivalently:

```text
old_internal_value -> old_internal_value - q.
```

### Failure equations

A new collision occurs if

```text
P_u - q = P_v
```

for an old internal affected value `P_u` and an old unaffected value or another shifted affected value `P_v`.

Thus:

```text
q = P_u - P_v.
```

This is the core obstruction equation.

## Move M3: cut-and-insert one atom left across a block

Let the ordering contain

```text
X, Y, q, Z.
```

Move `q` to the left of `Y`:

```text
X, q, Y, Z.
```

The affected internal partial sums of `Y` shift by `+q`.

Failure equations have the form

```text
P_u + q = P_v
```

or

```text
q = P_v - P_u.
```

Again, failure pins `q` as a difference of old partial sums.

## Move M4: block rotation

A block rotation moves one endpoint atom of a zero interval to the other side.

If

```text
Z = (z_1, z_2, ..., z_l)
```

and

```text
sum(Z)=0,
```

then rotating to

```text
(z_2, ..., z_l, z_1)
```

preserves the total sum of the block and all partial sums outside the block.

Internal partial sums transform by translation relative to the block prefix.

This move is useful because the zero interval remains zero as a block, but its internal zero-subintervals may change.

Potential use:

```text
If Z is shortest, then Z has no internal zero interval.
Therefore its internal partial sums are distinct.
Rotating Z may alter how external atoms interact with Z.
```

## Move M5: two-block exchange

Let two adjacent blocks be

```text
U, V
```

with sums

```text
u = sum(U),
v = sum(V).
```

Swapping them changes partial sums inside `U` and `V`, but all later partial sums are unchanged because the total `u+v` is preserved.

This is more complex and should be avoided unless M1--M3 are insufficient.

## First analytic focus

Use only M1--M3 initially.

These are enough to produce universal failure equations:

```text
q = P_u - P_v.
```

The proof program becomes:

```text
If every useful insertion of an outside atom into/through a shortest zero interval fails,
then many outside atoms lie in a difference set of old partial sums associated with the interval.
```

The next step is to compress those equations into obstruction classes.

## Candidate local lemma S02.1

Let `R` be D-minimal and let `Z=[i+1,j]` be a shortest zero interval.  Let `q` be the atom immediately before `Z`, if it exists.

Move `q` rightward across the first `k` atoms of `Z`, for `1 <= k <= ell(Z)`.

If for some `k` no new repeated extended partial sum is created except possibly the old collision `P_i=P_j`, then the move contradicts D-minimality.

Therefore, in a D-minimal counterexample, every such `k` produces a collision equation

```text
q = P_u - P_v
```

with `P_u` in the affected window.

## Why this lemma matters

For one outside atom `q`, multiple failed insertion depths produce multiple equations involving the same `q`.

Subtracting two equations gives:

```text
P_u - P_v = P_{u'} - P_{v'}.
```

This is an additive energy relation among partial sums.

The hoped-for analytic compression is:

```text
many failed insertions => high additive energy => structured obstruction => repair or contradiction.
```

## Guardrail

Do not claim that high additive energy alone is enough.  The structure here is ordered and interval-based, not just set-based.
