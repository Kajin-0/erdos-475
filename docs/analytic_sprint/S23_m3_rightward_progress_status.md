# S23. m=3 rightward terminal-progress status

This file records the v2 neutral-progress analysis for the `m=3`, `D_short=(1,3,1,[2])` terminal residual.

The nearest-boundary coordinate failed in S22.  The corrected orientation-normalized coordinate is:

```text
right-terminal progress = movement of the unique zero triple toward the right terminal side.
```

Equivalently:

```text
delta_right_distance < 0
```

or

```text
delta_center2 > 0.
```

## p=17 v2 result

Input:

```text
logs/one_sided_terminal_block_perms_p17.jsonl
```

Summary:

```text
input_records = 852
neutral_move_analyses = 600
records_with_neutral_analyses = 220
```

Move-level terminal direction:

```text
rightward_progress = 458
same_position      = 141
leftward_regress   =   1
```

Right-distance equivalent:

```text
toward_right_terminal = 458
same_right_distance   = 141
away_from_right       =   1
```

Record-best terminal direction:

```text
rightward_progress = 201
same_position      =  19
leftward_regress   =   0
```

Thus:

```text
201 / 220 ≈ 91.36%
```

of neutral records have a `D_short`-neutral move that progresses rightward.

## p=23 v2 result

Input:

```text
logs/one_sided_terminal_block_perms_p23.jsonl
```

Summary:

```text
input_records = 756
neutral_move_analyses = 711
records_with_neutral_analyses = 302
```

Move-level terminal direction:

```text
rightward_progress = 533
same_position      = 168
leftward_regress   =  10
```

Right-distance equivalent:

```text
toward_right_terminal = 533
same_right_distance   = 168
away_from_right       =  10
```

Record-best terminal direction:

```text
rightward_progress = 265
same_position      =  33
leftward_regress   =   4
```

Thus:

```text
265 / 302 ≈ 87.75%
```

of neutral records have a `D_short`-neutral move that progresses rightward.

## Interpretation

The refined-progress coordinate should be orientation-normalized, not nearest-boundary based.

For a right-terminal residual, use:

```text
P_R = right_distance of the unique zero triple.
```

A neutral move with

```text
delta_right_distance < 0
```

is progress because it moves the unique zero triple toward the terminal support side.

For a left-terminal residual, apply the same definition after reversal.

## Current compression of the one-sided long-terminal branch

The branch now splits into:

```text
1. finite-menu D_short descent;
2. D_short-neutral rightward terminal progress;
3. no-rightward-progress residual;
4. worse-only residual.
```

The first two are large:

```text
p=17:
  improved records = 583
  neutral-rightward records = 201
  total handled = 784 / 852 ≈ 92.02%

p=23:
  improved records = 369
  neutral-rightward records = 265
  total handled = 634 / 756 ≈ 83.86%
```

This is a major compression of the one-sided right-long-terminal case.

## Residual sizes

For neutral records with no rightward progress:

```text
p=17: 19 records
p=23: 33 + 4 = 37 records
```

Together with the worse-only records:

```text
p=17 worse-only = 49
p=23 worse-only = 85
```

The remaining one-sided branch is now small and highly structured.

## Candidate refined defect

For right-terminal `m=3` residuals, use:

```text
D_ref = (
  D_short,
  terminal_side,
  right_distance(unique zero triple),
  support_length,
  local_pattern_rank
)
```

For left-terminal residuals, reverse orientation and use left-distance analogously.

The computational data supports the coordinate:

```text
right_distance(unique zero triple)
```

as a genuine neutral-progress tie-break.

## Next empirical task

The next task is to extract the small residual:

```text
neutral records with no rightward-progress move
worse-only records
```

and summarize:

```text
1. support length distribution;
2. permutation patterns;
3. whether same-position records preserve the same zero-triple atom multiset;
4. whether leftward-regress cases are tied to specific permutations;
5. whether worse-only records all increase E by exactly 1 or 2;
6. whether residuals are boundary-adjacent.
```

## Next script

Add:

```text
scripts/extract_m3_progress_residuals.py
```

Target output:

```text
logs/m3_progress_residuals_p17.jsonl
logs/m3_progress_residuals_p23.jsonl
```

with record-level labels:

```text
neutral_no_rightward
worse_only
```

## Status

```text
Nearest-boundary coordinate rejected.
Right-terminal progress coordinate supported.
Remaining residual: small no-rightward/worse-only m=3 set.
```
