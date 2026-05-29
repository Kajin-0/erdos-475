# S85. Corrected equality tie-break theorem

This note consolidates the corrected equality-branch result from S62-S84 into one theorem-style statement.

## Purpose

The equality hidden-support branch occurs after Lemma A extracts one of:

```text
B_tail + q = A_complement,
B_prefix = q.
```

This branch is `D_short`-neutral rather than immediately descending.  The tie-break is a refined support-localization rank:

```text
S_tail = span_gap({q} union B_tail).
```

The corrected result is that the equality branch always admits a local rearrangement that preserves `D_short` and sends

```text
S_tail -> 0.
```

Thus the equality branch strictly descends in

```text
D_ref = (D_short, S_tail).
```

## Setup

Let the local residual have form

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0,
D_short(R) = (1,3,1,[2]).
```

In the equality branch, write

```text
B = P T M,
T = B_tail,
```

where `T` is the support-tail block appearing in the extracted equality relation.

The old local support order is

```text
old: q P T M.
```

Define

```text
S_tail(R) = span_gap_R({q} union T),
span_gap_R(U) = max_position_R(U) - min_position_R(U) + 1 - |U|.
```

Since `P` separates `q` from `T` in the old order,

```text
S_tail(old) = |P|.
```

## Candidate moves

The two relevant localizations are:

```text
Primary:  q P T M -> P q T M,
Fallback: q P T M -> q T P M.
```

Both make `{q} union T` contiguous.  Therefore either successful move has

```text
S_tail(new) = 0.
```

## Theorem C. Corrected equality tie-break

### Statement

In every certified equality hidden-support residual, either:

```text
1. the primary localization P q T M is D_short-neutral;
```

or:

```text
2. the primary localization is D_short-worse only because it creates a new shortest block P_suffix + q = 0, and the fallback localization q T P M is D_short-neutral.
```

In both cases there exists a local rearrangement `R -> R'` such that

```text
D_short(R') = D_short(R),
S_tail(R') = 0 < S_tail(R).
```

Hence

```text
D_ref(R') < D_ref(R),
D_ref = (D_short, S_tail).
```

## Proof

### Step 1. Span-gap descent

In the old order

```text
q P T M,
```

the set

```text
U = {q} union T
```

has span width

```text
span_width_old(U) = 1 + |P| + |T|.
```

Since

```text
|U| = 1 + |T|,
```

we get

```text
S_tail(old) = |P|.
```

In both candidate orders

```text
P q T M,
q T P M,
```

the elements of `U` are contiguous, hence

```text
S_tail(new) = 0.
```

Therefore any `D_short`-neutral candidate gives strict descent in the refined defect.

### Step 2. Primary-neutral case

If the primary localization

```text
q P T M -> P q T M
```

is `D_short`-neutral, then using Step 1 gives

```text
D_ref(primary) < D_ref(old).
```

This closes the equality branch in the primary-neutral case.

### Step 3. Primary-worse case

If the primary localization is `D_short`-worse, S84 verifies that every primary-new shortest block has zone class

```text
P+q.
```

The verified primary-failure shape is therefore:

```text
P_suffix + q = 0.
```

The certified records are:

```text
p=17 record 739: B3 q
p=23 record 716: B3 B4 q
```

and the summary is:

```text
primary_failure_rows = 2
rows_with_only_Pq_new_short = 2
rows_with_non_Pq_new_short = 0
failure_indices = []
zone_class_histogram = {P+q: 2}
```

Thus primary failure is caused by the new adjacency

```text
P | q
```

in the order

```text
P q T M.
```

### Step 4. Fallback in the primary-worse case

Use the fallback localization

```text
q P T M -> q T P M.
```

This removes the problematic `P|q` adjacency.  S80 verifies that the fallback creates no new shortest block:

```text
fallback_new_short_total = 0
fallback_new_short_symbols = {}
fallback_new_zone_histogram = {}
fallback_zone_histogram = {A+z: 2}
```

The fallback defect profile is exactly the old profile in both primary-failure rows:

```text
fallback_defect_counts = {[1,3,1,(2,)]: 2}.
```

Therefore

```text
D_short(fallback) = D_short(old).
```

By Step 1,

```text
S_tail(fallback) = 0 < S_tail(old).
```

So

```text
D_ref(fallback) < D_ref(old).
```

This closes the primary-worse case.

## Certified equality coverage

The equality records are:

```text
p=17:
  B_tail+q=A_complement: 4 records

p=23:
  B_tail+q=A_complement: 5 records
  B_prefix=q:            2 records
```

The verified tie-break coverage is:

```text
p=17: 4/4
p=23: 7/7
```

The fallback implication has zero failures:

```text
p=17:
  primary_worse_records = 1
  fallback_rescues = 1
  implication_failures = 0

p=23:
  primary_worse_records = 1
  fallback_rescues = 1
  implication_failures = 0
```

## Corrected local mechanism

The correct mechanism is:

```text
old:      q | P | T | M
primary:  P | q | T | M
fallback: q | T | P | M
```

Primary can fail only by creating

```text
P_suffix + q = 0.
```

Fallback removes the `P|q` adjacency and creates no new shortest interval.

This supersedes the earlier incorrect `T_prefix+q` hypothesis.

## Role in the pure worse-only theorem

In the pure worse-only branch theorem skeleton, the equality families are now handled by this theorem:

```text
B_tail + q = A_complement -> equality tie-break descent,
B_prefix = q              -> equality tie-break descent.
```

Thus the equality branch is closed at the empirical-symbolic level.

## Remaining publication-grade proof obligation

The remaining symbolic step is to prove generally, not just by certificate, that under the equality hidden-support hypotheses:

```text
P q T M worse -> primary-new shortest blocks are only P_suffix+q,
q T P M creates no new shortest block.
```

The current certified data verifies this local claim in all observed primary-failure rows.

## Status

```text
Corrected equality tie-break theorem assembled.
Equality branch is empirically closed and reduced to a local symbolic proof obligation.
```
