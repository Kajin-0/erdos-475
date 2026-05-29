# S76. Symbolic fallback lemma draft

This note drafts the remaining symbolic lemma suggested by S73-S75.

## Goal

Prove the equality fallback implication:

```text
P_q_T_M worse -> q_T_P_M neutral.
```

The empirical accounting from S75 sharpened this to:

```text
P_q_T_M worse
  -> primary creates a new shortest block T_prefix + q
  -> fallback q_T_P_M creates no new shortest block
  -> fallback is D_short-neutral.
```

## Setup

Let the equality branch have support decomposition

```text
B = P T M,
```

where `T` is the extracted support tail.  The old local order is

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

Both `L1` and `L2` make `{q} union T` contiguous, so both give

```text
S_tail = 0.
```

The only issue is preservation of `D_short`.

## Lemma C2. Primary-failure fallback lemma

### Statement

Assume the equality hidden-support hypotheses and write `B=P T M`.  If the primary localization

```text
q P T M -> P q T M
```

is `D_short`-worse, then the fallback localization

```text
q P T M -> q T P M
```

is `D_short`-neutral.

Moreover, in the certified failure mechanism, primary worsening occurs because there is a nonempty prefix `T0` of `T` such that

```text
T0 + q = 0.
```

The fallback creates no new shortest zero interval beyond those already present in the old order.

## Proof skeleton

### Step 1. Locate the only new boundary in the primary move

The old support order is

```text
q | P | T | M.
```

The primary order is

```text
P | q | T | M.
```

The primary move changes the local adjacencies involving `q` and the boundary between `P` and `T`.

Any zero interval that is new in `L1` and responsible for worsening must cross a newly created adjacency.  The relevant new adjacency is

```text
q | T.
```

Therefore the new shortest interval responsible for primary failure has the form

```text
q + T0 = 0,
```

where `T0` is a nonempty prefix of `T`.

This matches the observed primary-failure signatures:

```text
B3 q,
B3 B4 q.
```

### Step 2. Compare the fallback order

The fallback order is

```text
q | T | P | M.
```

The same block

```text
q + T0
```

is still contiguous, but now it lies at the leading edge of the intentionally localized `qT` cluster.

Empirically, this block is not a new shortest block relative to the old order's defect accounting.  The fallback new-shortest-block set is empty in both primary-failure records.

### Step 3. Show no new shortest interval appears in fallback

A final proof must show that every fallback shortest interval is either:

```text
1. an old shortest interval transported by the rearrangement;
2. a terminal/support tautology already accounted for;
3. longer than the current shortest length;
4. routed by an already-closed branch.
```

Under this condition,

```text
D_short(L2) = D_short(old).
```

### Step 4. Conclude refined descent

Since `L2` places `q` adjacent to `T`,

```text
S_tail(L2) = 0.
```

Since `D_short(L2)=D_short(old)`, we get

```text
D_ref(L2) < D_ref(old),
D_ref = (D_short, S_tail).
```

## Empirical certificate

The focused accounting shows:

```text
primary_failure_rows = 2
fallback_class_counts = {neutral: 2}
fallback_new_short_presence = {no: 2}
fallback_new_short_symbols = {}
```

Primary new shortest symbols:

```text
B3 q:     1
B3 B4 q: 1
```

Thus the fallback has no new shortest blocks in the certified primary-failure cases.

## Final remaining symbolic gap

The proof still needs a general argument for:

```text
primary creates q+T_prefix as the only possible primary-failure mechanism,
q_T_P_M introduces no new shortest block under that mechanism.
```

This is now a small local combinatorial statement about the four blocks:

```text
q, P, T, M.
```

## Status

```text
Fallback lemma drafted.
Equality branch proof reduced to a local block-combinatorics claim over q, P, T, M.
```
