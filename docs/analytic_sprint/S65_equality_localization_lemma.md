# S65. Equality localization lemma

This note sharpens S62 using the symbolic move patterns extracted in S64.

## Purpose

The equality branch after hidden-support extraction consists of:

```text
B_tail + q = A_complement,
B_prefix = q.
```

S64 showed that every equality record has a `D_short`-neutral move that makes

```text
{q} union B_tail
```

contiguous.  Hence

```text
q_tail_span_gap(new) = 0.
```

This note states the corresponding symbolic localization lemma.

## Notation

Write the support block as

```text
B = P T,
```

where

```text
P = B_prefix,
T = B_tail.
```

The old active order has the form

```text
A1 A2 z q P T.
```

Define

```text
S_tail(R) = span_gap_R({q} union T),
```

where

```text
span_gap_R(U) = max_position_R(U) - min_position_R(U) + 1 - |U|.
```

If `P` is nonempty, then in the old order

```text
S_tail(A1 A2 z q P T) = |P|.
```

because `P` lies strictly between `q` and `T`.

## Observed localization moves

The improving neutral moves have one of the symbolic final forms:

```text
A1 A2 z P q T,
A1 A2 z q T P,
A1 A2 z T q P.
```

In each case, `q` is adjacent to `T`, so

```text
S_tail(new) = 0.
```

## Lemma C'. Equality localization lemma

### Statement

Let `R = X A z q B Y` be a pure worse-only `m=3` right-terminal residual in the equality hidden-support branch.  Write

```text
B = P T,
```

where `T = B_tail` is the extracted support tail.

Assume the hidden-support extraction gives one of:

```text
T + q = A_complement,
P = q.
```

Then there exists a `D_short`-neutral rearrangement of the local support block taking

```text
q P T
```

to one of

```text
P q T,
q T P,
T q P,
```

such that

```text
D_short(R') = D_short(R)
```

and

```text
S_tail(R') = 0 < S_tail(R).
```

Therefore

```text
D_ref(R') < D_ref(R),
D_ref = (D_short, S_tail).
```

## Algebraic span calculation

In the old active order

```text
q P T,
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
S_tail(old) = span_width_old(U) - |U| = |P|.
```

For each allowed localized final form:

```text
P q T,
q T P,
T q P,
```

the atoms in `U` are contiguous.  Hence

```text
span_width_new(U) = |U| = 1 + |T|,
```

so

```text
S_tail(new) = 0.
```

Thus if `P` is nonempty,

```text
S_tail(new) = 0 < |P| = S_tail(old).
```

## Family-specific interpretation

### Family 1: `T + q = A_complement`

The extracted equality is

```text
T + q = A_complement.
```

The old active order is

```text
q P T.
```

The certificate found neutral localizations of the form:

```text
P q T,
q T P,
T q P.
```

At least one exists in every certified record.

### Family 2: `P = q`

The extracted equality is

```text
P = q.
```

The extracted `T` is the complementary support tail after the prefix `P`.  The observed neutral localization is

```text
q P T -> P q T.
```

Again, this places `q` adjacent to `T` and gives

```text
S_tail(new) = 0.
```

## Certificate support

The equality move-pattern extractor gave:

```text
p=17:
  B_tail+q=A_complement: 4 / 4 records have gap-improving neutral move.

p=23:
  B_tail+q=A_complement: 5 / 5 records have gap-improving neutral move.
  B_prefix=q:            2 / 2 records have gap-improving neutral move.
```

In all reported improving moves:

```text
new_q_tail_span_gap = 0.
```

The observed move names were:

```text
prefix_q_tail_middle,
q_tail_prefix_middle,
tail_q_prefix_middle,
prefix_then_q_tail.
```

At the symbolic final-order level these collapse to:

```text
P q T,
q T P,
T q P.
```

## What remains formal

The span calculation is fully formal once the support split

```text
B = P T
```

is fixed.

The remaining nontrivial part is to prove the existence of at least one `D_short`-neutral localization among

```text
P q T,
q T P,
T q P
```

for every equality-branch residual.

The empirical certificate shows this for all equality records:

```text
p=17: 4 / 4,
p=23: 7 / 7.
```

A formal proof likely needs a finite comparison of the zero intervals created by these three localizations.  Since all three make `{q} union T` contiguous, the only obstruction to neutrality is whether one creates a shorter or additional shortest zero interval.  The equality-branch data indicates at least one avoids that obstruction.

## Suggested next lemma

Define a finite alternative lemma:

```text
Among P q T, q T P, and T q P, at least one is D_short-neutral in the equality hidden-support branch.
```

This is now the last symbolic subclaim needed for the equality tie-break proof.

## Status

```text
Equality rank descent reduced to a localization lemma over P, q, T.
Span-gap descent is algebraically proved once localization is neutral.
```
