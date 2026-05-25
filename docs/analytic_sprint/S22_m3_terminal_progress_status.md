# S22. m=3 terminal-progress status

This file records the first neutral-progress analysis for the `m=3`, `D_short=(1,3,1,[2])` residual.

The data comes from:

```text
logs/summary_m3_terminal_progress_p17.json
logs/summary_m3_terminal_progress_p23.json
```

These were produced by:

```bash
python3 scripts/summarize_m3_terminal_progress.py \
  logs/one_sided_terminal_block_perms_p17.jsonl \
  --pretty \
  --out logs/summary_m3_terminal_progress_p17.json

python3 scripts/summarize_m3_terminal_progress.py \
  logs/one_sided_terminal_block_perms_p23.jsonl \
  --pretty \
  --out logs/summary_m3_terminal_progress_p23.json
```

## p=17 neutral progress

```text
input_records = 852
neutral_move_analyses = 600
records_with_neutral_analyses = 220
```

Move-level boundary progress:

```text
away_from_boundary       = 409
same_boundary_distance   = 185
toward_boundary          =   6
```

Record-best boundary progress:

```text
away_from_boundary       =  94
same_boundary_distance   = 124
toward_boundary          =   2
```

Center shift:

```text
right       = 458
same_center = 141
left        =   1
```

Left-index shift:

```text
right           = 458
same_left_index = 141
left            =   1
```

## p=23 neutral progress

```text
input_records = 756
neutral_move_analyses = 711
records_with_neutral_analyses = 302
```

Move-level boundary progress:

```text
away_from_boundary       = 422
same_boundary_distance   = 210
toward_boundary          =  79
```

Record-best boundary progress:

```text
away_from_boundary       = 128
same_boundary_distance   = 134
toward_boundary          =  40
```

Center shift:

```text
right       = 533
same_center = 168
left        =  10
```

Left-index shift:

```text
right           = 533
same_left_index = 168
left            =  10
```

## Key conclusion

The original candidate tie-break:

```text
nearest-boundary distance of the unique zero triple
```

is not supported.

Neutral moves usually do **not** move the zero triple toward the nearest boundary.  They mostly move it:

```text
rightward
```

or leave it at the same center/left index.

This is expected because the residual is orientation-normalized as a right-sided terminal bridge:

```text
R = X a b z q B Y,
z + sum(B)=0.
```

The natural progress direction is not nearest boundary.  It is toward the terminal side / right side.

## Better candidate progress coordinate

Use an orientation-normalized coordinate:

```text
P_right = right_distance of the unique zero triple
```

or equivalently:

```text
P_center = -center_position
```

for a right-terminal residual.

A neutral move that shifts the zero triple right decreases `right_distance` and increases center position.

Thus the refined defect should likely use:

```text
1. D_short;
2. terminal orientation class;
3. right-terminal progress: minimize right_distance of the unique zero triple;
4. support length / local pattern as secondary tie-break.
```

For a left-terminal residual, the reversed coordinate should be used.

## Stable neutral permutations

The neutral-heavy permutations are stable across p=17 and p=23:

```text
z A q B
q z A B
q B A z
A q z B
B q z A
```

These often preserve `D_short=(1,3,1,[2])` while shifting or preserving the unique zero triple.

## Important warning

The move-level center shift is promising, but we still need record-level terminal-direction progress.

Current summaries give move-level:

```text
center_shift_histogram
left_index_shift_histogram
```

but not the best available center/right progress per record.

## Next script patch

Patch:

```text
scripts/summarize_m3_terminal_progress.py
```

to report:

```text
record_best_center_shift_histogram
record_best_right_distance_progress_histogram
record_best_terminal_progress_perm_histogram
```

For the right-terminal orientation, define:

```text
terminal_progress = delta_right_distance < 0
```

or equivalently:

```text
delta_center2 > 0.
```

Record-level classification:

```text
rightward_progress
same_position
leftward_regress
```

The goal is to test whether every neutral record has a D_short-neutral move that shifts the unique zero triple rightward or at least does not shift left.

## Status

```text
Nearest-boundary coordinate rejected.
Orientation-normalized rightward progress is promising.
Next empirical target: record-level rightward progress under neutral moves.
```
