# S81. Corrected fallback local lemma

This note updates the equality fallback proof after the local taxonomy in S80.

## Correction

Earlier notes guessed that primary failure had the form

```text
T_prefix + q = 0.
```

The fallback local taxonomy shows this is incorrect.

The observed primary failure mechanism is instead

```text
P_suffix + q = 0,
```

where `P_suffix` is a nonempty suffix of the support prefix block `P` immediately preceding `q` in the primary order.

## Local orders

Write

```text
B = P T M,
```

where

```text
T = extracted B_tail.
```

The old local order is

```text
R0 = q P T M.
```

The primary localization is

```text
R1 = P q T M.
```

The fallback localization is

```text
R2 = q T P M.
```

Both `R1` and `R2` place `q` adjacent to `T`, hence both force

```text
S_tail = span_gap({q} union T) = 0.
```

The only issue is whether `D_short` is preserved.

## Empirical local taxonomy

The two primary-failure rows are:

```text
p=17 record 739
p=23 record 716
```

The primary new shortest blocks are:

```text
p=17: B3 q
p=23: B3 B4 q
```

Both have zone class:

```text
P + q.
```

Thus primary failure occurs because `R1=P q T M` creates a new short zero interval crossing the new adjacency

```text
P | q.
```

The fallback order `R2=q T P M` removes this adjacency.

The fallback local taxonomy reports:

```text
fallback_new_short_total = 0
fallback_new_short_symbols = {}
fallback_new_zone_histogram = {}
fallback_zone_histogram = {A+z: 2}
```

So the only fallback zero interval class is the old terminal triple:

```text
A1 + A2 + z = 0.
```

No new fallback zero interval occurs in the local `q|T|P|M` zones.

## Corrected Lemma C2. Primary-failure fallback

### Statement

Let `R0=q P T M` be an equality hidden-support residual with extracted support tail `T`.  Assume:

```text
1. the primary localization R1=P q T M is D_short-worse;
2. the new primary shortest interval has form P_suffix + q = 0;
3. the fallback localization R2=q T P M creates no new shortest interval.
```

Then

```text
D_short(R2)=D_short(R0),
S_tail(R2)=0<S_tail(R0),
```

and hence

```text
D_ref(R2)<D_ref(R0),
D_ref=(D_short,S_tail).
```

## Proof

Since `R2=q T P M` places `q` adjacent to `T`, the set

```text
U={q} union T
```

is contiguous. Therefore

```text
S_tail(R2)=0.
```

In the old order `R0=q P T M`, the block `P` separates `q` from `T`, so if `P` is nonempty,

```text
S_tail(R0)=|P|>0.
```

By assumption (3), the fallback creates no new shortest zero interval.  The local taxonomy strengthens this: the fallback creates no new local zero interval at all in the `q|T|P|M` zones, and its only zero interval class is the old `A+z` relation.

Therefore the fallback preserves the old shortest-zero profile:

```text
D_short(R2)=D_short(R0).
```

Consequently,

```text
D_ref(R2)=(D_short(R0),0)<(D_short(R0),|P|)=D_ref(R0).
```

## Why the fallback removes primary failure

The primary order

```text
P q T M
```

creates the adjacency

```text
P | q.
```

The observed primary-failure block has form

```text
P_suffix + q = 0.
```

The fallback order

```text
q T P M
```

removes the `P|q` adjacency entirely.  The block `P_suffix+q` is no longer contiguous, and the fallback taxonomy confirms that no replacement shortest block appears.

## Remaining formal proof obligation

The remaining symbolic statement is now:

```text
If P q T M is D_short-worse in the equality branch, then the only possible new shortest block is P_suffix+q, and q T P M creates no new shortest interval.
```

This is a local endpoint statement comparing:

```text
primary zones:  P | q | T | M
fallback zones: q | T | P | M
```

## Proof direction

A final proof should enumerate the new adjacencies introduced by the primary and fallback moves.

### Primary new adjacencies

Compared with the old order `q|P|T|M`, the primary order `P|q|T|M` introduces:

```text
P | q,
q | T.
```

The taxonomy shows the only primary-failure new shortest block crosses `P|q`.

### Fallback new adjacencies

The fallback order `q|T|P|M` introduces:

```text
q | T,
T | P.
```

The taxonomy shows neither creates a new shortest interval in the primary-failure rows.

Thus the symbolic fallback proof should show that under the equality hypotheses, a `P_suffix+q` primary obstruction is incompatible with a fallback shortest obstruction crossing `q|T` or `T|P`.

## Status

```text
Fallback proof corrected.
Primary failure is P_suffix+q.
Fallback removes the P|q adjacency and creates no new shortest interval in certified rows.
```
