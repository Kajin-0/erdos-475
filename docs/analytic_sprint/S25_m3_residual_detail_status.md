# S25. m=3 progress residual detail status

This file records the detailed split of the kept `m=3` progress residuals.

Input summaries:

```text
logs/summary_m3_progress_residual_details_p17.json
logs/summary_m3_progress_residual_details_p23.json
```

These were produced from:

```text
logs/m3_progress_residuals_p17.jsonl
logs/m3_progress_residuals_p23.jsonl
```

using:

```text
scripts/summarize_m3_progress_residual_details.py
```

## Current branch

The remaining branch after S24 is:

```text
m=3,
D_short=(1,3,1,[2]),
one-sided right-long-terminal,
```

with label:

```text
neutral_no_rightward_progress
or
worse_only.
```

## p=17 detailed residual

```text
records = 68
neutral_no_rightward_progress = 19
worse_only                    = 49
```

### p=17 signed/distributed split

Neutral no-rightward:

```text
has_signed_or_distributed =  5
pure_terminal_local       = 14
```

Worse-only:

```text
has_signed_or_distributed = 14
pure_terminal_local       = 35
```

Total pure terminal residual:

```text
14 + 35 = 49
```

Total already-routable residual:

```text
5 + 14 = 19
```

### p=17 support lengths

Neutral no-rightward:

```text
3: 6
4: 5
5: 8
```

Worse-only:

```text
3: 15
4: 22
5: 12
```

### p=17 neutral no-rightward permutations

```text
z A q B : 19
z A B q :  1
```

Thus the neutral no-rightward branch is almost entirely the local rotation:

```text
A z q B -> z A q B.
```

This preserves `D_short` and does not move the unique zero triple rightward.

## p=23 detailed residual

```text
records = 122
neutral_no_rightward_progress = 37
worse_only                    = 85
```

### p=23 signed/distributed split

Neutral no-rightward:

```text
has_signed_or_distributed = 17
pure_terminal_local       = 20
```

Worse-only:

```text
has_signed_or_distributed = 26
pure_terminal_local       = 59
```

Total pure terminal residual:

```text
20 + 59 = 79
```

Total already-routable residual:

```text
17 + 26 = 43
```

### p=23 support lengths

Neutral no-rightward:

```text
3:  5
4: 12
5:  6
6:  7
7:  7
```

Worse-only:

```text
3: 15
4: 12
5: 19
6: 13
7: 17
8:  9
```

### p=23 neutral no-rightward permutations

```text
z A q B : 32
z A B q :  3
B A q z :  2
z q B A :  2
```

Again, the dominant same-position neutral move is:

```text
A z q B -> z A q B.
```

## Key conclusions

### 1. A nontrivial fraction already routes through existing branches

For p=17:

```text
19 / 68 ≈ 27.94%
```

of the kept residual has signed or distributed flags.

For p=23:

```text
43 / 122 ≈ 35.25%
```

of the kept residual has signed or distributed flags.

These are not new obstructions. They should route through S07/S10/distributed-bridge reductions.

### 2. The genuinely new residue is pure terminal

Pure terminal counts:

```text
p=17: 49
p=23: 79
```

This is the true local bottleneck.

### 3. Neutral no-rightward is mostly cyclic rotation of the zero triple

The dominant neutral no-rightward move is:

```text
z A q B
```

Since `A` has length 2 in the `m=3` residual, this transforms:

```text
A z
```

into:

```text
z A
```

The zero triple remains contiguous, but it is cyclically rotated.

Therefore a possible secondary progress coordinate is the cyclic orientation/rank of the unique zero triple, not boundary distance.

### 4. Worse-only is genuinely worse under all tested local permutations

For worse-only records, every tested block permutation is best-class `worse`.  This indicates that the pure terminal worse-only branch requires either:

```text
1. a nonlocal move;
2. a pair/distributed/signed route not detected by local terminal progress;
3. an algebraic contradiction special to m=3;
4. or a stronger global minimality/tie-break condition.
```

## Normal form for pure terminal residual

The genuine residue has:

```text
R = X a b z q B Y,
a+b+z=0,
sum(B)=a+b=-z,
|B|>=2,
D_short=(1,3,1,[2]),
```

with no signed or distributed flags detected by the current classifier.

The pure terminal no-rightward neutral subcase adds:

```text
A z q B -> z A q B
```

is neutral, where `A=a b`.

The pure terminal worse-only subcase adds:

```text
every local permutation of A,z,q,B worsens D_short.
```

## Next proof target

Proceed to:

```text
docs/analytic_sprint/S26_pure_m3_terminal_residual.md
```

Target theorem:

```text
Pure m=3 terminal residual reduction.
Let R be minimal under a refined defect order. Suppose
  R = X a b z q B Y,
  a+b+z=0,
  sum(B)=a+b,
  D_short=(1,3,1,[2]),
  no signed/distributed branch is present.
Then either the cyclic rotation z a b gives refined progress, or the worse-only case contradicts minimality by a nonlocal rotation/exchange using the unique-collision property.
```

## Next script target

Add:

```text
scripts/extract_pure_m3_terminal_residuals.py
```

It should filter:

```text
pure terminal local residuals only
```

from:

```text
logs/m3_progress_residuals_p17.jsonl
logs/m3_progress_residuals_p23.jsonl
```

and emit:

```text
logs/pure_m3_terminal_residuals_p17.jsonl
logs/pure_m3_terminal_residuals_p23.jsonl
```

with labels:

```text
pure_neutral_same_position
pure_worse_only
```

## Status

```text
Kept m=3 residual split complete.
Already-routable signed/distributed fraction identified.
True new bottleneck: pure terminal m=3 residual.
```
