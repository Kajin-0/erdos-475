# S59. E3 local active-window interval routing

This note formalizes E3 from S56.

## Purpose

In the endpoint-zone proof for

```text
R' = X B z q A Y,
```

we must dispose of local active-window zero intervals that are neither:

```text
1. the terminal tautology B + z = 0;
2. a hidden-support target interval;
3. an exterior crossing interval.
```

Such intervals are local collisions created inside the active window.  They route to signed interval, support-trap, pair-trap, or distributed-bridge machinery.

## Setup

The moved order is

```text
R' = X B z q A Y.
```

The active window is

```text
W = B z q A.
```

Let the partial sums inside `W` be

```text
T_0 = 0,
T_j = w_1 + ... + w_j.
```

A local active-window zero interval is a repeated local partial sum:

```text
T_a = T_b,
```

with both endpoints inside the active window.

## Lemma E3

### Statement

Let `I` be a zero interval contained inside the active window `B z q A` or crossing between its internal zones, but suppose `I` is not one of:

```text
B + z = 0,
B_tail + z + q = 0,
B_tail + z + q + A_i + Y_prefix = 0,
B_tail + z + q + A1 + A2 + Y_prefix = 0.
```

Then `I` produces one of the already-routed local mechanisms:

```text
SIGNED_INTERVAL,
DISTRIBUTED_BRIDGE,
PAIR_TRAP,
support-tail trap,
local support collision.
```

Therefore such an interval is excluded from the pure worse-only residual.

## Local interval families

Inside the active zones

```text
B | z | q | A,
```

a non-target local interval has one of the following shapes.

### 1. Support-only interval

```text
B_i + ... + B_j = 0.
```

This is a support sub-block zero relation.  It is excluded by support minimality or routes to support-trap machinery.

This overlaps E1 when the interval lies in `B z`, but here we record it as a local support collision.

### 2. Support-q interval

```text
B_i + ... + B_j + q = 0.
```

This is a `Bq_zero`-type support-tail obstruction.

In the current proof architecture, such intervals are routed by the Bq/BqY routing lemma:

```text
Bq_zero -> existing classifier route.
```

### 3. A-only or q-A interval

```text
A_i = 0,
A_i + A_j = 0,
q + A_i = 0,
q + A_i + A_j = 0.
```

These create a short local zero relation involving `q` or a proper part of `A`.  Since the intended terminal triple is

```text
A1 + A2 + z = 0,
```

any additional local relation involving only `q` and/or a proper part of `A` creates an immediate signed/local obstruction.

Such a case is not pure worse-only.

### 4. A-B interval not crossing zq in target form

Examples:

```text
A_prefix + B_subblock = 0,
A_prefix + B_subblock + q = 0,
B_subblock + z + A_prefix = 0.
```

These identify two local partial sums inside the active window that are not the endpoint pair of a hidden-support crossing interval.  They give a signed interval or a distributed bridge because a local partial sum before the moved separator coincides with a local partial sum after it.

### 5. Multiple local bridge indices

If more than one internal partial-sum equality is generated, the local interval is not isolated.  This is exactly the distributed-bridge situation:

```text
multiple active bridge indices -> DISTRIBUTED_BRIDGE.
```

## Partial-sum proof mechanism

Every local zero interval in `W` is an equality

```text
T_a = T_b.
```

The hidden-support target intervals are the equalities where the interval begins at a suffix of `B`, crosses the consecutive separator

```text
z q,
```

and ends at one of:

```text
before A,
after A_i,
after A1 A2 plus optional Y_prefix.
```

All other local equalities either:

```text
1. lie entirely inside B or A;
2. involve q without the required B_tail-z-q crossing shape;
3. connect B and A without the zq separator;
4. produce more than one active bridge index.
```

These are precisely the signed/support/distributed local obstruction mechanisms.

## Relation to classifier vocabulary

The existing branch vocabulary has labels for these cases:

```text
SIGNED_INTERVAL
DISTRIBUTED_BRIDGE
PAIR_TRAP
support-tail trap
```

and, after the Bq/BqY routing closure:

```text
Bq_zero
BqY_zero
```

are no longer primitive obstructions.  They route to existing branch machinery.

## Use in Lemma A

E3 lets the endpoint-zone enumeration discard local active-window non-target intervals.

After E1 handles intervals inside `B z`, and E2 handles exterior crossings, E3 handles all remaining local intervals that fail to have hidden-support shape.  Therefore the only unresolved interval shapes are exactly:

```text
B_tail + z + q = 0,
B_tail + z + q + A_i + Y_prefix = 0,
B_tail + z + q + A1 + A2 + Y_prefix = 0.
```

These are the hidden-support extraction intervals.

## Formal proof sentence

A compact formal version is:

```text
A local active-window zero interval that is not terminal-tautological and not a B_tail-z-q-A/Y crossing interval determines a repeated local partial sum pair whose endpoints lie on the same side of the hidden-support crossing or connect incompatible local zones.  Such a repeated local pair is exactly a signed/support/distributed obstruction.  Pure worse-only residuals exclude these already-routed obstructions, so such intervals are not remaining cases.
```

## Status

```text
E3 is formalized as a local partial-sum routing lemma.
Remaining sublemma: E4, the definition-level exclusion of already-routed branches.
```
