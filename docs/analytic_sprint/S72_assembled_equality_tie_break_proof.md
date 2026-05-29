# S72. Assembled equality tie-break proof

This note assembles S62-S71 into a proof-ready draft for the equality branch.

## Lemma C. Equality tie-break by support-tail localization

### Statement

Let

```text
R = X A z q B Y
```

be a pure worse-only `m=3` right-terminal residual satisfying

```text
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0,
D_short(R) = (1,3,1,[2]).
```

Assume the hidden-support extraction lemma gives an equality branch:

```text
B_tail + q = A_complement
```

or

```text
B_prefix = q.
```

Write the support block as

```text
B = P T M,
```

where

```text
T = B_tail
```

is the extracted support-tail block used in the hidden-support relation.

Define

```text
S_tail(R) = span_gap_R({q} union T),
```

where

```text
span_gap_R(U) = max_position_R(U) - min_position_R(U) + 1 - |U|.
```

Then there exists a local rearrangement `R -> R'` such that

```text
D_short(R') = D_short(R)
```

and

```text
S_tail(R') = 0 < S_tail(R).
```

Consequently, for the refined defect

```text
D_ref(R) = (D_short(R), S_tail(R)),
```

ordered lexicographically, one has

```text
D_ref(R') < D_ref(R).
```

## Local form

The old local support order is

```text
A z q P T M,
```

where `A=A1 A2`.

The two-step localization rule is:

```text
Primary:  A z P q T M
Fallback: A z q T P M
```

Equivalently, in the support part:

```text
Primary:  q P T M -> P q T M
Fallback: q P T M -> q T P M
```

Both candidate orders place `q` adjacent to `T`.

## Span-gap calculation

Let

```text
U = {q} union T.
```

In the old order

```text
q P T M,
```

the block `P` lies between `q` and `T`.  Therefore

```text
span_width_old(U) = 1 + |P| + |T|,
|U| = 1 + |T|,
```

and hence

```text
S_tail(old) = span_width_old(U) - |U| = |P|.
```

In both localized orders

```text
P q T M
q T P M
```

the atoms of `U` are contiguous.  Therefore

```text
span_width_new(U) = |U| = 1 + |T|,
```

so

```text
S_tail(new) = 0.
```

If `P` is nonempty, then

```text
S_tail(new) = 0 < |P| = S_tail(old).
```

Thus any `D_short`-neutral localization gives strict descent in the refined defect.

## Fallback principle

The empirical certificate verifies the following two-step implication:

```text
If Primary = P q T M is D_short-neutral, use Primary.
If Primary is D_short-worse, then Fallback = q T P M is D_short-neutral and has S_tail=0.
```

In compact form:

```text
P_q_T_M worse -> q_T_P_M neutral and q_tail_span_gap = 0.
```

This was verified with zero failures:

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

## Proof structure

### Step 1. Try the primary localization

Apply

```text
A z q P T M -> A z P q T M.
```

If this move preserves `D_short`, then the span-gap calculation gives

```text
S_tail(new) = 0 < S_tail(old).
```

So

```text
D_ref(new) < D_ref(old).
```

### Step 2. If primary is worse, use fallback

If the primary localization is `D_short`-worse, the fallback implication gives that

```text
A z q P T M -> A z q T P M
```

is `D_short`-neutral and has

```text
S_tail(new) = 0.
```

Again,

```text
D_ref(new) < D_ref(old).
```

### Step 3. Conclude equality branch descent

Thus every equality hidden-support branch has a refined descent.  The equality branches are not terminal obstructions; they are tie-broken by support-tail localization.

## Relation to the v4 certificate

The v4 pure-worse certificate table recorded:

```text
p=17:
  B_tail+q=A_complement -> q_tail_span_gap 4/4, equality_tiebroken

p=23:
  B_tail+q=A_complement -> q_tail_span_gap 5/5, equality_tiebroken
  B_prefix=q            -> q_tail_span_gap 2/2, equality_tiebroken
```

The assembled lemma explains this table structurally.

## Remaining formal burden

The span-gap descent is fully algebraic.  The remaining proof obligation is the fallback implication:

```text
P_q_T_M worse -> q_T_P_M neutral.
```

To make this publication-grade, one must prove symbolically that the zero-interval obstruction created by the primary localization is absorbed or removed by moving `T` immediately after `q`.

The diagnostic data suggests this route:

```text
Primary worse
  -> new short block involving q and an initial segment of T
  -> fallback q T P M makes that block part of the localized q-T cluster
  -> no additional D_short worsening occurs.
```

## Status

```text
Equality tie-break proof assembled.
Remaining formal core: prove the fallback implication symbolically.
```
