# S64. Equality neutral-move pattern results

This note records the output of:

```text
scripts/extract_equality_tie_break_patterns.py
```

using:

```text
logs/equality_tie_break_patterns_p17.jsonl
logs/equality_tie_break_patterns_p23.jsonl
logs/summary_equality_tie_break_patterns_p17.json
logs/summary_equality_tie_break_patterns_p23.json
```

## Main result

Every equality record has a `D_short`-neutral move that makes `{q} union B_tail` contiguous.

Equivalently:

```text
old q_tail_span_gap > 0,
new q_tail_span_gap = 0.
```

Thus the equality branch is not merely decreasing the support-localization rank.  It decreases it maximally.

## p=17 summary

Equality family:

```text
B_tail+q=A_complement: 4 records
```

Coverage:

```text
gap_improve_by_family:
  B_tail+q=A_complement: yes 4 / 4
```

Move names observed:

```text
prefix_q_tail_middle: 3
tail_q_prefix_middle: 1
q_tail_prefix_middle: 1
```

There are 5 neutral moves across 4 records because one record has two neutral improving moves.

## p=23 summary

Equality families:

```text
B_tail+q=A_complement: 5 records
B_prefix=q:            2 records
```

Coverage:

```text
gap_improve_by_family:
  B_tail+q=A_complement: yes 5 / 5
  B_prefix=q:            yes 2 / 2
```

Move names observed:

```text
B_tail+q=A_complement:
  prefix_q_tail_middle: 4
  q_tail_prefix_middle: 2
  tail_q_prefix_middle: 2

B_prefix=q:
  prefix_q_tail_middle: 2
  prefix_then_q_tail:   2
```

There are more neutral moves than records because some records admit multiple improving neutral moves.

## Unified symbolic notation

Write

```text
B = P T,
```

where:

```text
P = B_prefix,
T = B_tail.
```

The old active order is:

```text
A1 A2 z q P T.
```

The observed neutral improving moves are rotations/localizations that place `q` adjacent to `T`.

## Observed symbolic move classes

### Class 1. prefix_q_tail_middle

```text
OLD: A1 A2 z q P T
NEW: A1 A2 z P q T
```

This moves the prefix block `P` before `q`, placing `q` immediately before `T`.

For this move:

```text
span_gap({q} union T) -> 0.
```

This is the dominant pattern.

### Class 2. q_tail_prefix_middle

```text
OLD: A1 A2 z q P T
NEW: A1 A2 z q T P
```

This moves `T` immediately after `q`.

For this move:

```text
span_gap({q} union T) -> 0.
```

### Class 3. tail_q_prefix_middle

```text
OLD: A1 A2 z q P T
NEW: A1 A2 z T q P
```

This moves `T` immediately before `q`.

For this move:

```text
span_gap({q} union T) -> 0.
```

### Class 4. prefix_then_q_tail

Observed only as a duplicate pattern for `B_prefix=q` records.

```text
OLD: A1 A2 z q P T
NEW: A1 A2 z P q T
```

It is symbolically equivalent to `prefix_q_tail_middle` at the final-order level.

## Record-level observations

### p=17

Representative records:

```text
record 388:
  equation: B3 B4 q = A2
  B_tail: B3 B4
  neutral improving moves:
    A1 A2 z B3 B4 q B1 B2
    A1 A2 z B1 B2 q B3 B4
  old gap = 2
  new gap = 0

record 410:
  equation: B2 B3 B4 q = A2
  B_tail: B2 B3 B4
  neutral improving move:
    A1 A2 z B1 q B2 B3 B4
  old gap = 1
  new gap = 0

record 538:
  equation: B4 B5 q = A2
  B_tail: B4 B5
  neutral improving move:
    A1 A2 z B1 B2 B3 q B4 B5
  old gap = 3
  new gap = 0

record 739:
  equation: B4 B5 q = A2
  B_tail: B4 B5
  neutral improving move:
    A1 A2 z q B4 B5 B1 B2 B3
  old gap = 3
  new gap = 0
```

### p=23

Representative records:

```text
record 247:
  equation: B7 q = A2
  B_tail: B7
  move: A1 A2 z B1 B2 B3 B4 B5 B6 q B7
  old gap = 6
  new gap = 0

record 384:
  equation: B3 q = A2
  B_tail: B3
  improving moves:
    A1 A2 z q B3 B1 B2
    A1 A2 z B3 q B1 B2
    A1 A2 z B1 B2 q B3
  old gap = 2
  new gap = 0

record 466:
  equation: B1 B2 B3 B4 = q
  B_tail: B5 B6
  move: A1 A2 z B1 B2 B3 B4 q B5 B6
  old gap = 4
  new gap = 0

record 688:
  equation: B1 B2 B3 B4 B5 B6 B7 = q
  B_tail: B8
  move: A1 A2 z B1 B2 B3 B4 B5 B6 B7 q B8
  old gap = 7
  new gap = 0
```

## Formal interpretation

The equality branch has a simple tie-break mechanism:

```text
Move/rotate the support block so that q is adjacent to B_tail.
```

The allowed final forms are:

```text
P q T,
q T P,
T q P.
```

All satisfy:

```text
span_gap({q} union T) = 0.
```

Therefore, if the old order has `q` separated from `T` by nonempty `P`, then any of these final forms gives:

```text
S_tail(new) = 0 < S_tail(old).
```

## Updated equality tie-break lemma

The empirical statement can now be sharpened:

```text
Lemma: Equality tie-break localization.
In the equality hidden-support branch, there exists a D_short-neutral cyclic support rearrangement that places q adjacent to B_tail.  Hence S_tail decreases to zero.
```

## Remaining proof task

The only nontrivial formal step is to prove the existence of at least one `D_short`-neutral localization among:

```text
P q T,
q T P,
T q P.
```

The certificate shows this holds in all equality records:

```text
p=17: 4 / 4
p=23: 7 / 7
```

## Status

```text
Equality move pattern extracted.
The tie-break proof now reduces to a finite symbolic localization lemma over P, q, and T.
```
