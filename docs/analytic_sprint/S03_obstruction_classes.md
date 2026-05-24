# S03. Obstruction classes

This file defines the first obstruction classes arising from failed local moves.

The purpose is to turn failed repairs into named algebraic objects that AI and scripts can attack one at a time.

## Universal failure equation

For the local moves M1--M3, failure has the generic form

```text
q = P_u - P_v
```

where:

```text
q     = outside atom being moved;
P_u   = an affected old partial sum;
P_v   = an old partial sum that collides with the shifted value.
```

Thus failed repairs are controlled by difference relations among extended partial sums.

## Obstruction O1: repeated blocker

### Definition

A repeated blocker occurs when the same outside atom `q` blocks many insertion depths by colliding with the same external partial sum `P_v`:

```text
q = P_{u_k} - P_v       for many k.
```

### Immediate consequence

If `v` is fixed and `q` is fixed, then

```text
P_{u_k} = q + P_v
```

for many `k`, so the affected values coincide.

If those `P_{u_k}` are supposed to be distinct inside a shortest zero interval, this is impossible.

### Expected role

This obstruction should be easy to eliminate unless the affected values already have multiplicity.  If multiplicity exists, it may decrease the collision profile after a move.

### Lemma target

```text
O1 lemma:
A D-minimal ordering cannot have a repeated blocker with fixed q and fixed P_v over two distinct affected values P_u, P_u' unless those affected values already belong to the same collision class.
```

## Obstruction O2: pair trap

### Definition

A pair trap occurs when two insertion depths are blocked by paired equations

```text
q = P_u - P_v
q = P_{u'} - P_{v'}
```

which imply

```text
P_u - P_{u'} = P_v - P_{v'}.
```

Equivalently, two differences inside the partial-sum path are equal.

### Interval interpretation

The equality

```text
P_u - P_{u'} = P_v - P_{v'}
```

means two contiguous intervals have equal sum, up to orientation.

This suggests a two-block exchange or cut-and-paste repair.

### Lemma target

```text
O2 lemma:
If a shortest zero interval is protected only by pair-trap equal-difference equations,
then a two-block exchange produces either a smaller collision excess or a longer shortest zero interval.
```

Status: high-risk. Needs examples.

## Obstruction O3: signed interval

### Definition

A signed interval obstruction occurs when a failed move forces

```text
q = ± sum(I)
```

for a proper contiguous interval `I` inside or adjacent to the active zero interval.

### Why it matters

If `Z` is a shortest zero interval, no proper subinterval of `Z` has sum zero.

Signed interval equations with repeated signs may force a shorter zero interval after adding or removing `q`.

### Lemma target

```text
O3 lemma:
Let Z be shortest zero-sum. If an outside atom q equals the signed sum of a proper endpoint interval of Z, then inserting q at the opposite endpoint destroys Z and cannot create an equal-or-shorter zero interval unless a pair trap occurs.
```

## Obstruction O4: midpoint adjacent

### Definition

A midpoint-adjacent obstruction occurs when adjacent swap failure gives

```text
Q + b = P_k
```

while the old bad value is

```text
Q + a = P_l.
```

Subtracting gives

```text
b - a = P_k - P_l.
```

If `P_k` and `P_l` are symmetrically placed around the active zero interval, this can imply a midpoint relation.

### Expected role

This obstruction may be an artifact of using adjacent swaps only.  It may disappear when using cut-and-insert moves.

Status: low priority until examples show it is common.

## Obstruction O5: external bridge

### Definition

An external bridge occurs when every insertion of `q` into a shortest zero interval `Z` fails because shifted internal partial sums collide with partial sums outside `Z`.

In generic form:

```text
InternalPartial_k - q = ExternalPartial_m.
```

Thus:

```text
q = InternalPartial_k - ExternalPartial_m.
```

### Why it matters

If many internal positions map to external partial sums under translation by `-q`, then the translated internal path overlaps the external path heavily.

This suggests a rigidity statement:

```text
large overlap between an interval path and its q-translate
=> periodic/additive structure
=> contradiction with distinct atoms or shorter zero interval.
```

### Lemma target

```text
O5 lemma:
Let Z be shortest zero-sum. If translate(Z-internal-partial-sums, -q) has large overlap with the external partial-sum set for every adjacent outside q, then either there is a shorter zero interval or an exchange move decreases D.
```

Status: central but difficult.

## Obstruction O6: internal self-overlap

### Definition

When moving `q` across a block, shifted affected partial sums may collide with other shifted affected partial sums:

```text
P_u - q = P_{u'} - q.
```

This reduces to

```text
P_u = P_{u'}.
```

So translation alone cannot create new collisions among affected sums that were not already present.

Therefore internal self-overlap is not a real new obstruction for one-atom insertion.

### Consequence

For M2/M3, new collisions are primarily affected-vs-unaffected collisions.

This simplifies the local lemma.

## Current obstruction priority

```text
1. O5 external bridge
2. O2 pair trap
3. O3 signed interval
4. O1 repeated blocker
5. O4 midpoint adjacent
```

O6 is eliminated as a non-obstruction for pure translation moves.

## Immediate next task

Write a small obstruction miner that:

```text
1. generates small prime sets S;
2. searches for D-minimal-looking defective orderings;
3. selects a shortest zero interval;
4. tries adjacent outside atom insertions;
5. records the equations q = P_u - P_v for every failed insertion.
```

The output should be fed back into AI to compress actual obstruction patterns.
