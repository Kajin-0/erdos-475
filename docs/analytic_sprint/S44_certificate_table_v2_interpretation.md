# S44. Pure worse certificate table v2 interpretation

The first compact certificate table correctly summarized the pure worse-only branch, but it was too noisy for proof use because the column

```text
genuine_record_classes
```

listed every genuine secondary collision class present in a record.  For the formal proof, the important value is not the full class list.  It is the target obstruction coverage.

## Target obstruction map

The proof-relevant target map is:

```text
B_tail+q              -> Bq_zero
B_tail+q+Y_prefix     -> BqY_zero
B_tail+q=A_complement -> equality_tie_break
B_prefix=q            -> equality_tie_break
```

Thus the certificate table should display:

```text
family,
records,
mode,
verified_total,
best_bridge_class,
target_obstruction,
target_coverage,
status.
```

## Correct target coverage from current summaries

### p=17

```text
B_tail+q:
  records = 23
  target_obstruction = Bq_zero
  target_coverage = 23 / 23
  status = zero_sum_classified

B_tail+q+Y_prefix:
  records = 8
  target_obstruction = BqY_zero
  target_coverage = 8 / 8
  status = zero_sum_classified

B_tail+q=A_complement:
  records = 4
  target_obstruction = equality_tie_break
  target_coverage = 4 / 4 neutral
  status = tie_break_needed
```

### p=23

```text
B_tail+q:
  records = 20
  target_obstruction = Bq_zero
  target_coverage = 20 / 20
  status = zero_sum_classified

B_tail+q+Y_prefix:
  records = 32
  target_obstruction = BqY_zero
  target_coverage = 32 / 32
  status = zero_sum_classified

B_tail+q=A_complement:
  records = 5
  target_obstruction = equality_tie_break
  target_coverage = 5 / 5 neutral
  status = tie_break_needed

B_prefix=q:
  records = 2
  target_obstruction = equality_tie_break
  target_coverage = 2 / 2 neutral
  status = tie_break_needed
```

## Proof interpretation

The pure worse-only branch now has a clean two-class reduction.

### Zero-sum class

```text
B_tail+q=0
B_tail+q+Y_prefix=0
```

These are fully classified by target secondary obstructions:

```text
Bq_zero
BqY_zero
```

This is the branch for the next formal obstruction lemma.

### Equality class

```text
B_tail+q=A_complement
B_prefix=q
```

These are bridge-neutral and have no genuine secondary obstruction under the current move menu.  They need a refined tie-break, likely involving terminal position, cyclic rank, or support-prefix rank.

## Formal proof statement supported by the v2 certificate

```text
For every observed pure worse-only m=3 terminal residual, the B z q A hidden-support extraction produces exactly one of four reduced families.  The two zero-sum families force a target secondary obstruction with full record-level coverage in p=17 and p=23.  The two equality families are neutral under tested bridge moves and are isolated as tie-break obligations.
```

## Status

```text
Use v2 certificate table for proof writing.
The v1 table remains useful for debugging, but v2 is the formal branch table.
```
