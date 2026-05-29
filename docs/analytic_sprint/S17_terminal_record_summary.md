# S17. Terminal record-level summary

This file records the record-level terminal summary produced by `scripts/summarize_terminal_records.py`.

The purpose is to decide whether the next proof attack should be:

```text
1. two-sided long terminal bridge; or
2. one-sided/boundary long terminal bridge.
```

The data favors one-sided long terminal as the larger residue, while two-sided long terminal remains a substantial subcase.

## p=17 hard terminal records

Input:

```text
logs/external_bridge_hard_terminal_lengths_p17.jsonl
```

Summary:

```text
records = 2783
```

Record counts:

```text
records_with_terminal                  = 2783
records_with_long_terminal             = 2783
records_with_long_only_terminal        = 2363
records_with_short_terminal            =  420
records_with_both_short_and_long       =  420
records_with_both_left_right_terminal  =  773
records_with_right_only_terminal       = 1601
records_with_left_only_terminal        =  409
records_with_terminal_and_distributed  =  817
records_with_terminal_and_signed       =  448
```

Sidedness:

```text
both_left_right =  773
right_only      = 1601
left_only       =  409
```

Terminal length class:

```text
long_only           = 2363
both_short_and_long =  420
```

Support length statistics:

```text
count  = 7962
min    = 1
median = 3
max    = 5
```

Terminal total length statistics:

```text
count  = 7962
min    = 2
median = 4
max    = 6
```

Support length histogram:

```text
1:  840
2: 2504
3: 1988
4: 1572
5: 1058
```

## p=23 hard terminal records

Input:

```text
logs/external_bridge_hard_terminal_lengths_p23.jsonl
```

Summary:

```text
records = 3391
```

Record counts:

```text
records_with_terminal                  = 3391
records_with_long_terminal             = 3391
records_with_long_only_terminal        = 2917
records_with_short_terminal            =  474
records_with_both_short_and_long       =  474
records_with_both_left_right_terminal  = 1371
records_with_right_only_terminal       = 1456
records_with_left_only_terminal        =  564
records_with_terminal_and_distributed  = 1514
records_with_terminal_and_signed       =  365
```

Sidedness:

```text
both_left_right = 1371
right_only      = 1456
left_only       =  564
```

Terminal length class:

```text
long_only           = 2917
both_short_and_long =  474
```

Support length statistics:

```text
count  = 10890
min    = 1
median = 3
max    = 8
```

Terminal total length statistics:

```text
count  = 10890
min    = 2
median = 4
max    = 9
```

Support length histogram:

```text
1:  948
2: 2486
3: 2042
4: 1718
5: 1388
6: 1056
7:  772
8:  480
```

## Key conclusions

### 1. Every hard terminal record has a long terminal bridge

For both datasets:

```text
records_with_long_terminal = records
```

So the dominant obstruction is not merely terminal bridge; it is long terminal bridge.

### 2. Long-only dominates

For p=17:

```text
long_only / records = 2363 / 2783 ≈ 84.91%
```

For p=23:

```text
long_only / records = 2917 / 3391 ≈ 86.02%
```

Thus short terminal bridge is mostly an accompanying feature, not the core residue.

### 3. One-sided terminal is larger than two-sided terminal

For p=17:

```text
one-sided = 1601 + 409 = 2010
two-sided = 773
```

For p=23:

```text
one-sided = 1456 + 564 = 2020
two-sided = 1371
```

So one-sided long terminal is the larger branch, though two-sided is still significant.

### 4. Right-only dominates left-only in these samples

For p=17:

```text
right_only / left_only = 1601 / 409 ≈ 3.91
```

For p=23:

```text
right_only / left_only = 1456 / 564 ≈ 2.58
```

This may be partly due to ordering/sampling bias, but it means the immediate proof should treat one-sided terminal in an orientation-normalized way.

### 5. Terminal + distributed is common

For p=17:

```text
terminal_and_distributed = 817 / 2783 ≈ 29.36%
```

For p=23:

```text
terminal_and_distributed = 1514 / 3391 ≈ 44.65%
```

So a substantial fraction already routes toward the distributed/equal-difference branch.

## Proof priority update

The next proof attack should be:

```text
one-sided long terminal bridge reduction
```

not two-sided first.

Reason:

```text
1. every hard terminal record has long terminal;
2. long-only dominates;
3. one-sided dominates two-sided;
4. terminal+distributed already removes many cases;
5. the remaining one-sided long-only branch is the clearest bottleneck.
```

## Proposed next theorem

```text
One-sided long terminal reduction.
Let R be D_short-minimal and let Z be an active shortest zero interval with m>=3.
Suppose one side of Z has only long terminal bridges and no clean descent, signed interval, pair trap, or distributed bridge.
Then either:
  1. Z lies too close to the boundary for both-sided testing;
  2. the opposite adjacent atom gives a nonterminal obstruction;
  3. the long support contains an internal shortest-zero trigger;
  4. endpoint absorption along the long support exposes a shorter zero interval;
  5. a global counting contradiction occurs.
```

## Next file

Proceed to:

```text
docs/analytic_sprint/S18_one_sided_long_terminal.md
```

## Status

```text
Terminal record summary complete.
Dominant branch: one-sided long terminal.
Next attack: one-sided long-terminal reduction.
```
