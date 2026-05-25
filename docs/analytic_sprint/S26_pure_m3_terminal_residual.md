# S26. Pure m=3 terminal residual attack

This file records the current true bottleneck after stripping all signed/distributed cases from the `m=3` one-sided terminal residual.

## Input summaries

The pure residual summaries are:

```text
logs/summary_pure_m3_terminal_residuals_p17.json
logs/summary_pure_m3_terminal_residuals_p23.json
```

These were produced from:

```text
logs/m3_progress_residuals_p17.jsonl
logs/m3_progress_residuals_p23.jsonl
```

using:

```text
scripts/extract_pure_m3_terminal_residuals.py
```

## p=17 pure residual

```text
input_records = 68
skipped_signed_distributed = 19
records = 49
```

Pure labels:

```text
pure_neutral_same_position = 14
pure_worse_only            = 35
```

Support length histogram:

```text
3: 13
4: 22
5: 14
```

Attempt flags:

```text
LONG_TERMINAL_BRIDGE  = 98
RIGHT_TERMINAL_BRIDGE = 98
```

No signed or distributed flags remain.

## p=23 pure residual

```text
input_records = 122
skipped_signed_distributed = 43
records = 79
```

Pure labels:

```text
pure_neutral_same_position = 19
pure_neutral_leftward_regress = 1
pure_worse_only = 59
```

Support length histogram:

```text
3: 11
4: 13
5: 13
6: 18
7: 19
8:  5
```

Attempt flags:

```text
LONG_TERMINAL_BRIDGE  = 168
RIGHT_TERMINAL_BRIDGE = 168
```

No signed or distributed flags remain.

## Compression status

The original right-one-sided long-terminal branch has now been compressed to:

```text
pure m=3 right-terminal residual
```

with normal form:

```text
R = X a b z q B Y,
a+b+z=0,
sum(B)=a+b=-z,
|B|>=3 in observed pure cases,
D_short=(1,3,1,[2]),
```

and with no detected:

```text
SIGNED_INTERVAL
DISTRIBUTED_BRIDGE
```

## Important observation: support length starts at 3

Although long terminal only requires:

```text
|B| >= 2
```

for `m=3`, the pure residual summaries show no support length `2` cases.

Observed pure support lengths:

```text
p=17: 3,4,5
p=23: 3,4,5,6,7,8
```

This suggests that terminal support length `2` is already killed by local descent/progress or by signed/distributed routing.

Thus the true pure residual has:

```text
|B| >= 3.
```

That extra slack is important.

## Algebraic normal form

Let

```text
A = a b,
Z = A z.
```

The unique zero triple gives:

```text
a+b+z=0.
```

The right terminal bridge gives:

```text
z + B = 0.
```

Therefore:

```text
sum(A)=sum(B).
```

So the pure residual is an equal-sum replacement:

```text
a+b = y_1+...+y_s,
s>=3.
```

But it is not a generic equal-sum replacement, because every local block permutation of:

```text
A,z,q,B
```

is either worse or at best a same-position cyclic neutral move.

## Pure neutral same-position branch

The dominant neutral move is:

```text
A z q B -> z A q B.
```

For `A=a b`, this is:

```text
a b z q B -> z a b q B.
```

The zero triple remains contiguous and is cyclically rotated:

```text
a b z -> z a b.
```

Thus the correct secondary tie-break for this subcase is not boundary distance or rightward progress. It is cyclic orientation of the unique zero triple.

A natural cyclic rank is:

```text
rank(a,b,z) > rank(z,a,b) > rank(b,z,a)
```

or a lexicographic rank after canonicalizing the zero triple under cyclic rotation.

## Candidate lemma S26.1: cyclic neutral progress

In the pure neutral same-position branch, if

```text
A z q B -> z A q B
```

preserves `D_short=(1,3,1,[2])`, then the unique zero triple is cyclically rotated.

Therefore a refined defect that minimizes the cyclic representative of the unique zero triple rules out this neutral loop.

### Proof sketch

The move changes the local contiguous zero block from:

```text
a b z
```

to:

```text
z a b.
```

Both blocks have zero sum.  If `D_short` is preserved and no signed/distributed flags appear, the only repeated partial-sum pair still bounds this cyclically rotated zero triple.  A cyclic-rank tie-break forbids returning to an equivalent or worse cyclic orientation.

## Pure worse-only branch

The pure worse-only branch is harder:

```text
every tested local permutation of A,z,q,B worsens D_short.
```

Since `D_short=(1,3,1,[2])`, worsening usually means creating additional collisions:

```text
E increases from 1 to 2,3,4,...
```

or lengthening the unique zero interval while preserving E.

But the starting state has exactly one collision, so every new collision created by a local permutation must involve a moved endpoint.

That is strong. It means each failed permutation generates an explicit equality involving one of:

```text
A endpoints,
z endpoint,
q endpoint,
B endpoints,
external endpoints.
```

The pure classifier says these are not currently detected as signed/distributed, so the classifier may be missing a nonlocal equality type.

## Candidate lemma S26.2: worse-only creates many endpoint collision equations

If all local permutations of `A,z,q,B` worsen from `D_short=(1,3,1,[2])`, then each permutation creates at least one new collision involving a moved endpoint.

Because there are only finitely many external endpoints and many permutations, two generated collisions must share enough structure to create an equal-difference relation.

That equal-difference relation should be a distributed bridge or pair-trap after a refined definition.

### Interpretation

The pure worse-only branch may be an artifact of the current classifier being too local.  It likely hides a higher-order distributed relation produced by comparing collision equations from different failed permutations.

## Next empirical target

We need a pure-structure analyzer that extracts for each pure residual:

```text
1. X length and Y length;
2. a,b,z,q,B;
3. support length |B|;
4. position of the unique zero triple;
5. all new collisions created by each local permutation;
6. which moved endpoint participates in each collision;
7. whether two failed permutations imply a common equal-difference relation.
```

## Next script

Proceed to:

```text
scripts/analyze_pure_m3_terminal_structure.py
```

Input:

```text
logs/pure_m3_terminal_residuals_p17.jsonl
logs/pure_m3_terminal_residuals_p23.jsonl
```

Output:

```text
logs/analyze_pure_m3_terminal_structure_p17.jsonl
logs/analyze_pure_m3_terminal_structure_p23.jsonl
```

Summary should include:

```text
pure label counts
support lengths
X/Y boundary lengths
zero triple cyclic patterns
new collision endpoint participation by permutation
collision value histograms
common collision equations across permutations
```

## Proof priority

Attack order:

```text
1. pure neutral same-position: cyclic-rank tie-break;
2. pure worse-only: endpoint-collision comparison across failed permutations;
3. support-length >=3 lemma;
4. nonlocal distributed relation extraction.
```

## Status

```text
True bottleneck isolated:
  pure m=3 right-terminal residual.
Next:
  analyze collision equations in pure worse-only records.
```
