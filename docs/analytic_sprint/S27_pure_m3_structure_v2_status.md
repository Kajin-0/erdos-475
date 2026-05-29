# S27. Pure m=3 structure v2 status

This file records the corrected pure-residual structure analysis after excluding handled neutral-rightward records.

## Corrected filter

The first analyzer version included handled neutral records with rightward progress.  The corrected default keeps only:

```text
pure_worse_only
pure_neutral_same_position
pure_neutral_leftward_regress
```

and excludes:

```text
pure_neutral_rightward_progress
```

Use this override only for broad diagnostics:

```bash
--include-rightward-neutral
```

## p=17 corrected pure residual

```text
records = 49
include_rightward_neutral = false
```

Labels:

```text
pure_neutral_same_position = 14
pure_worse_only            = 35
```

Support lengths:

```text
3: 13
4: 22
5: 14
```

Boundary geometry:

```text
X_length = 0 for all 49 records
Y_length:
  0: 14
  1: 22
  2: 13
```

## p=23 corrected pure residual

```text
records = 79
include_rightward_neutral = false
```

Labels:

```text
pure_neutral_same_position    = 19
pure_neutral_leftward_regress =  1
pure_worse_only               = 59
```

Support lengths:

```text
3: 11
4: 13
5: 13
6: 18
7: 19
8:  5
```

Boundary geometry:

```text
X_length:
  0: 74
  4:  4
  5:  1

Y_length:
  0:  8
  1: 21
  2: 18
  3: 13
  4: 11
  5:  8
```

## Neutral same-position branch

For both p=17 and p=23, the neutral same-position branch has signature:

```text
window_start=after_zA:L3:internal_window
```

This corresponds to the cyclic rotation:

```text
A z q B -> z A q B
```

For m=3, with A=a b:

```text
a b z q B -> z a b q B
```

The unique zero triple remains in place but is cyclically rotated.  This branch should be handled by a cyclic-rank tie-break on the unique zero triple.

## Pure worse-only branch

For pure_worse_only, several L3 internal-window collision signatures occur once per record in both p=17 and p=23, including:

```text
after_B=after_BAz:L3:internal_window
after_B=after_BzA:L3:internal_window
after_Bq=after_BqAz:L3:internal_window
after_Bq=after_BqzA:L3:internal_window
after_q=after_qAz:L3:internal_window
after_q=after_qzA:L3:internal_window
after_qB=after_qBAz:L3:internal_window
after_qB=after_qBzA:L3:internal_window
window_start=after_Az:L3:internal_window
```

The worse-only branch is therefore highly structured.  It repeatedly creates short internal zero triples at predictable block-boundary pairs.

## Next script

Proceed to:

```text
scripts/summarize_pure_worse_collision_core.py
```

It should summarize:

```text
1. pure_worse_only record counts;
2. support length by record;
3. X/Y boundary lengths by record;
4. record-level signature presence histogram;
5. signatures present in every pure_worse_only record;
6. signatures present for each support length;
7. representative records for each support length.
```

## Status

```text
Corrected pure residual verified.
Neutral same-position -> cyclic-rank tie-break.
Worse-only -> finite collision-signature core analysis.
```
