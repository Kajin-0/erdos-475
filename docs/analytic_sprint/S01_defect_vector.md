# S01. Defect vector: zero-sum interval defect

This file proposes the first analytic invariant for the AI-first proof sprint.

## Extended partial sums

For an ordering

```text
R = (r_1, ..., r_t)
```

define

```text
P_0 = 0,
P_i = r_1 + ... + r_i mod p,  1 <= i <= t.
```

An SNS ordering is exactly an ordering for which

```text
P_0, P_1, ..., P_t
```

are pairwise distinct.

Equivalently, there is no pair `0 <= i < j <= t` such that

```text
P_i = P_j.
```

This equality is equivalent to a contiguous zero-sum interval:

```text
r_{i+1} + ... + r_j = 0.
```

## Zero interval notation

A zero interval of `R` is a pair

```text
I = [i+1, j]
```

with

```text
0 <= i < j <= t
sum(r_{i+1}, ..., r_j) = 0 mod p.
```

Its length is

```text
ell(I) = j - i.
```

Because each atom is nonzero, no zero interval has length `1`.

If `sigma(S) != 0`, the whole interval `[1,t]` is not a zero interval.

## Defect candidate D0

The simplest defect is:

```text
D0(R) = number of zero intervals in R.
```

Then `D0(R)=0` if and only if `R` is SNS.

This is conceptually clean, but local moves can destroy one zero interval while creating several new ones.  Therefore `D0` alone may be too coarse.

## Defect candidate D1

The next candidate is lexicographic:

```text
D1(R) = (
  N_zero(R),
  L_min(R),
  N_min(R)
)
```

where

```text
N_zero(R) = number of zero intervals;
L_min(R) = minimum length of a zero interval, or infinity if none;
N_min(R) = number of zero intervals of length L_min(R).
```

Problem: a local move that destroys a shortest interval may create a longer zero interval, so `N_zero` may increase even when the shortest obstruction improves.  This makes `N_zero` a dangerous first coordinate.

## Defect candidate D2: shortest-first defect

A more local invariant is:

```text
D2(R) = (
  L_min(R),
  N_min(R),
  N_short_window(R),
  N_zero(R)
)
```

with lexicographic minimization but with `L_min` ordered normally or inversely?

We want zero intervals to disappear.  If no zero intervals exist, set

```text
L_min(R) = infinity.
```

If minimizing lexicographically, infinity is bad.  Therefore use inverse shortest length:

```text
K_min(R) = t + 1 - L_min(R)
```

where `K_min=0` if there are no zero intervals.

Then define:

```text
D2(R) = (
  K_min(R),
  N_min(R),
  N_zero(R)
)
```

and minimize lexicographically.

Interpretation:

```text
First eliminate the shortest zero intervals.
Then reduce how many shortest intervals remain.
Then reduce total zero intervals.
```

However, this makes shorter zero intervals worse than longer zero intervals.  Since length `2` zero intervals cannot occur in a set of distinct atoms unless `a+b=0`, this may force early structure.

## Defect candidate D3: collision multiplicity profile

Let the extended partial sums define multiplicities

```text
m_x(R) = |{i : P_i = x}|,   x in F_p.
```

SNS means every multiplicity is `0` or `1`.

Define the collision excess:

```text
E(R) = sum_x max(0, m_x(R)-1).
```

Equivalently,

```text
E(R) = (t+1) - |{P_0, ..., P_t}|.
```

This counts how many repeated partial-sum occurrences must be removed.

A stronger profile is:

```text
M(R) = sorted descending list of multiplicities m_x(R) greater than 1.
```

Candidate:

```text
D3(R) = (
  E(R),
  M(R),
  K_min(R),
  N_min(R)
)
```

This is globally meaningful but less directly connected to a specific local interval.

## Recommended working defect

Use two levels:

### Global choice

Choose `R` minimizing

```text
E(R) = (t+1) - |{P_0, ..., P_t}|.
```

Among those, minimize the collision profile `M(R)` lexicographically.

Among those, maximize the shortest zero-interval length, equivalently minimize:

```text
K_min(R) = t + 1 - L_min(R).
```

Among those, minimize the number of shortest zero intervals.

So:

```text
D(R) = (
  E(R),
  M(R),
  K_min(R),
  N_min(R)
)
```

with lexicographic minimization, where `M(R)` is lexicographically sorted decreasing.

### Active object

After choosing minimal `R`, select a shortest zero interval

```text
Z = [a,b]
```

with length

```text
ell = b-a+1.
```

Study local moves involving atoms adjacent to or outside `Z`.

## Why this is promising

If a local move preserves all old partial-sum distinctness outside a controlled window and removes one collision class, then it decreases `E`.

If it preserves `E` but spreads one high-multiplicity collision into lower multiplicities, it decreases `M`.

If it preserves both but increases the shortest zero interval length, it decreases `K_min`.

Therefore obstruction equations must explain why all such improvements fail.

## First lemma target

```text
Lemma S01.1: Let R be D-minimal and let Z be a shortest zero interval.  Let q be an atom outside Z adjacent to one endpoint.  If inserting q into the interior of Z creates no new repeated extended partial sum outside the old collision class, then the resulting ordering contradicts D-minimality.
```

This lemma is almost tautological once the affected partial sums are written correctly.  Its value is that it defines what a `failed useful insertion` must algebraically mean.

## Key algebra for insertion

Suppose

```text
R = X q Y Ztail
```

and move `q` rightward across a block `Y`.  The affected partial sums over the crossed block shift by `-q` or `+q` depending on convention.

A collision after the move has one of these forms:

```text
old_internal_sum - q = old_external_sum
old_internal_sum + q = old_external_sum
old_internal_sum - q = old_internal_sum'
old_internal_sum + q = old_internal_sum'
```

Thus every failed insertion produces an equation of the form

```text
q = P_u - P_v
```

where `P_u, P_v` are old extended partial sums.

This is the bridge from local failure to additive structure.

## Sprint decision

Use `D(R) = (E, M, K_min, N_min)` as the current working defect.

Do not add more coordinates until a concrete false lemma forces it.
