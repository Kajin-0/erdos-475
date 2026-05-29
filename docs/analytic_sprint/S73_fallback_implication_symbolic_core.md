# S73. Symbolic core for equality fallback implication

This note isolates the remaining equality-branch proof core after S72.

## Current equality proof state

The equality hidden-support branch has been reduced to the following two-step localization rule.

Write

```text
B = P T M,
```

where `T` is the extracted `B_tail`.  The old active support order is

```text
A z q P T M.
```

The primary localization is

```text
L1 = A z P q T M.
```

The fallback localization is

```text
L2 = A z q T P M.
```

Both make `{q} union T` contiguous, hence both have

```text
S_tail = span_gap({q} union T) = 0.
```

Thus the equality branch is closed once we prove:

```text
L1 worse -> L2 neutral.
```

## Empirical fallback result

The fallback implication was verified with zero failures:

```text
p=17:
  records = 4
  primary_worse_records = 1
  fallback_rescues = 1
  implication_failures = 0

p=23:
  records = 7
  primary_worse_records = 1
  fallback_rescues = 1
  implication_failures = 0
```

So there are only two certified primary-failure cases across the current datasets.

## Primary-failure signatures

From S69, the new shortest blocks causing `P_q_T_M` to be worse are:

```text
p=17:
  B3 q

p=23:
  B3 B4 q
```

Both have the same symbolic form:

```text
T_prefix + q = 0,
```

where `T_prefix` is a nonempty initial segment of the extracted tail `T` after the primary localization places `q` immediately before `T`.

Thus the observed primary failure mechanism is:

```text
L1 = P q T M creates a short zero block q + T_prefix.
```

## Why the fallback should rescue

The fallback localization is

```text
L2 = q T P M.
```

Under `L2`, the same relation

```text
q + T_prefix = 0
```

appears at the left edge of the localized `q T` cluster instead of after moving `P` across `q`.

The key empirical fact is that this does not worsen `D_short`; it preserves the original defect.

A plausible symbolic explanation is:

```text
If q + T_prefix = 0 is forced, then the fallback move does not create an additional independent shortest collision.  It relocates the forced q-T_prefix collision into the already-accounted localized qT cluster.
```

In other words:

```text
primary worse because q collides with initial tail segment;
fallback neutral because q is kept before the entire tail, so that collision is absorbed rather than duplicated.
```

## Candidate formal fallback lemma

### Lemma C2. Primary-failure fallback

Let `R` be an equality hidden-support residual and write

```text
B = P T M.
```

Assume the primary localization

```text
q P T M -> P q T M
```

is `D_short`-worse.  Then there exists a nonempty prefix `T0` of `T` such that

```text
q + T0 = 0.
```

Moreover, the fallback localization

```text
q P T M -> q T P M
```

is `D_short`-neutral.

Consequently, fallback gives

```text
S_tail = 0
```

and closes the equality branch.

## Proof plan for Lemma C2

### Step 1. Characterize primary worsening

In

```text
L1 = A z P q T M,
```

any new shortest zero interval responsible for worsening must involve the newly adjacent pair

```text
q | T.
```

If the interval did not involve the boundary `q|T`, then it would have already existed in the old order or would be a routed support/exterior branch.

Therefore primary worsening implies a zero block of the form

```text
q + T0 = 0
```

for a nonempty prefix `T0` of `T`.

### Step 2. Move the whole tail after q

In the fallback order

```text
L2 = A z q T P M,
```

that same block `q + T0` remains contiguous, but it is now part of the intended `qT` localization.  Since `P` is no longer between `q` and `T`, no additional support-tail separation is introduced.

### Step 3. Compare defects

Show that all shortest intervals in `L2` are either:

```text
1. old shortest intervals transported by the move;
2. the forced q+T0 interval already implied by primary failure;
3. terminal/support tautologies already accounted for.
```

Then `D_short(L2)=D_short(R)`.

## What remains hard

The unresolved symbolic point is Step 3.  It must rule out the possibility that `L2` creates an additional shortest collision beyond the forced `q+T0` block.

Empirically this never occurs in the current equality certificate.

## Recommended next diagnostic

Extract only the primary-failure rows and print:

```text
old shortest blocks,
L1 new shortest blocks,
L2 shortest blocks,
which L2 blocks are old vs new,
whether L2 shortest count equals old shortest count.
```

This will show exactly how `D_short` remains neutral in the fallback cases.

## Status

```text
Equality proof core isolated.
Primary-failure mechanism appears to be q + T_prefix = 0.
Next: inspect fallback-neutral shortest interval accounting in the primary-failure rows.
```
