# S62. Equality tie-break lemma draft

This note formalizes the equality branch remaining after Lemma A.

## Purpose

The pure worse-only `m=3` branch has been reduced to four hidden-support families:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

The zero-sum families are already routed:

```text
B_tail+q              -> Bq_zero  -> existing route
B_tail+q+Y_prefix     -> BqY_zero -> existing route
```

The equality families are:

```text
B_tail + q = A_complement,
B_prefix = q.
```

They are neutral in `D_short`, but the certificate shows that they decrease a support-localization rank:

```text
q_tail_span_gap.
```

## Definitions

Let `R` be an extracted equality-branch residual with order

```text
R = X A z q B Y,
B = B_prefix B_tail B_suffix,
```

where `B_tail` is the support block appearing in the hidden-support relation.

Define the span width of a finite set of atoms `U` in an order `R` by

```text
span_width_R(U) = max_position_R(U) - min_position_R(U) + 1.
```

Define the span gap by

```text
span_gap_R(U) = span_width_R(U) - |U|.
```

For the equality branch, define

```text
S_tail(R) = span_gap_R({q} union B_tail).
```

Thus `S_tail(R)` measures how many unrelated atoms separate `q` from the extracted support tail.

## Refined defect

Use the refined defect

```text
D_ref(R) = (D_short(R), S_tail(R)),
```

ordered lexicographically.

A move is acceptable if either:

```text
D_short decreases,
```

or

```text
D_short is unchanged and S_tail decreases.
```

## Lemma C. Equality hidden-support tie-break

### Statement

Let `R = X A z q B Y` be a pure worse-only `m=3` right-terminal residual satisfying the normal form

```text
A1 + A2 + z = 0,
sum(B) + z = 0,
D_short(R) = (1,3,1,[2]).
```

Suppose the `B z q A` hidden-support extraction gives one of the equality relations:

```text
B_tail + q = A_complement,
```

or

```text
B_prefix = q.
```

Then there exists a tested neutral bridge move `R -> R'` such that

```text
D_short(R') = D_short(R)
```

and

```text
S_tail(R') < S_tail(R).
```

Therefore

```text
D_ref(R') < D_ref(R).
```

## Certificate support

The equality tie-break rank tester verified:

```text
p=17:
  B_tail+q=A_complement records = 4
  q_tail_span_gap improves       = 4/4

p=23:
  B_tail+q=A_complement records = 5
  q_tail_span_gap improves       = 5/5

  B_prefix=q records             = 2
  q_tail_span_gap improves       = 2/2
```

Total equality coverage:

```text
p=17: 4/4
p=23: 7/7
```

The same coverage holds for `q_tail_span_width`; since

```text
span_gap(U) = span_width(U) - |U|,
```

and `|{q} union B_tail|` is fixed for a given extraction, these two ranks are equivalent for the move comparison.

## Proof idea

The equality hidden-support relation says that `q` is algebraically tied to a support prefix/tail component:

```text
B_tail + q = A_complement,
```

or

```text
B_prefix = q.
```

The neutral bridge move does not remove the existing shortest zero structure, so `D_short` is preserved.  However, it moves `q` closer to the extracted `B_tail` relation.  Since the relation involves exactly `{q} union B_tail`, localizing this set reduces the number of intervening atoms:

```text
S_tail(new) < S_tail(old).
```

This gives a strict refined descent even when `D_short` is unchanged.

## Proof skeleton

### Step 1. Identify the equality relation

From Lemma A, the equality branch has either:

```text
B_tail + q = A_complement,
```

or

```text
B_prefix = q.
```

In both cases the extracted `B_tail` is a contiguous sub-block of `B` and `q` lies outside it in the original terminal order.

### Step 2. Apply the neutral bridge move

The tested bridge move relocates the relevant support block relative to `q`.  It is selected among moves that preserve `D_short`:

```text
D_short(R') = D_short(R).
```

Empirically, this is the best available move class for equality records:

```text
neutral: all equality records.
```

### Step 3. Show support localization

The move decreases the span containing `{q} union B_tail`:

```text
span_width_{R'}({q} union B_tail) < span_width_R({q} union B_tail).
```

Since the cardinality of `{q} union B_tail` is unchanged,

```text
S_tail(R') < S_tail(R).
```

### Step 4. Conclude refined descent

Therefore

```text
D_ref(R') = (D_short(R'), S_tail(R'))
          < (D_short(R),  S_tail(R))
          = D_ref(R).
```

## What remains formal

The empirical certificate proves the move exists in the tested records.  A final proof must specify the neutral bridge move explicitly in symbolic terms for each equality family.

### Equality family 1

For

```text
B_tail + q = A_complement,
```

one must define the move that brings `q` adjacent to `B_tail` or shortens the span of `{q} union B_tail` without creating a worse `D_short`.

### Equality family 2

For

```text
B_prefix = q,
```

one must define the move that converts this prefix equality into support-localized form while preserving `D_short`.

## Recommended next diagnostic

To turn this from an empirical lemma into a symbolic proof, add a script that prints the neutral move pattern for each equality record:

```text
old symbolic order,
new symbolic order,
B_tail labels,
q position,
old S_tail,
new S_tail,
move name.
```

This should reveal whether a single symbolic move pattern covers all equality records.

## Status

```text
Equality tie-break lemma drafted.
Remaining task: extract symbolic neutral move patterns for equality branches.
```
