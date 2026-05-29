# S21. The m=3 one-sided terminal residual

This file records the residual classification after `scripts/summarize_terminal_residuals.py`.

The one-sided long-terminal branch has now compressed to a very specific special case.

## Input summaries

The residual summaries used:

```text
logs/summary_terminal_residuals_p17.json
logs/summary_terminal_residuals_p23.json
```

These were produced from:

```text
logs/one_sided_terminal_block_perms_p17.jsonl
logs/one_sided_terminal_block_perms_p23.jsonl
```

by selecting:

```text
record_best_class in {neutral, worse}
```

## p=17 residual

```text
input_records     = 852
selected_records  = 269
neutral           = 220
worse             = 49
```

Critical histograms:

```text
old_defect_histogram = {
  (1,3,1,(2)): 269
}

m_histogram = {
  3: 269
}

candidate_validity = {
  valid: 269
}
```

Therefore:

```text
m3_and_defect_1_3_1_fraction = 1.0
```

## p=23 residual

```text
input_records     = 756
selected_records  = 387
neutral           = 302
worse             = 85
```

Critical histograms:

```text
old_defect_histogram = {
  (1,3,1,(2)): 387
}

m_histogram = {
  3: 387
}

candidate_validity = {
  valid: 387
}
```

Therefore:

```text
m3_and_defect_1_3_1_fraction = 1.0
```

## Main conclusion

The neutral/worse residue is not a general terminal-bridge problem.

It is exactly:

```text
m = 3,
D_short = (1,3,1,[2]),
one-sided right-long-terminal,
valid terminal/equal-sum candidate.
```

Thus the remaining local branch is:

```text
unique zero-sum triple residual.
```

## Normal form

Write the active shortest zero interval as:

```text
Z = a b z,
a + b + z = 0.
```

Since this is a right terminal bridge, there is a right support block:

```text
B = y_1 ... y_s,
s >= 2,
z + sum(B) = 0.
```

Therefore:

```text
sum(B) = -z = a+b.
```

So the residual has the form:

```text
R = X a b z q B Y,
sum(a b z)=0,
sum(B)=a+b,
D_short=(1,3,1,[2]).
```

There is exactly one repeated partial-sum value, hence exactly one zero interval in the ordering: the triple `a b z`.

## Consequence of D_short=(1,3,1,[2])

Since `E=1` and `M=[2]`, the only partial-sum collision is the pair bounding the interval `a b z`.

Therefore any move that preserves `E=1` but changes the location or support of the unique zero interval is a viable progress move if we add a tie-break coordinate.

This explains the large neutral branch.

## Observed neutral/worse behavior

For p=17 residuals:

```text
best_delta_histogram includes:
  dE=0,dL=0,dN=0,M:(2)->(2): 600
  dE=1,dL=0,dN=0,M:(2)->(2,2): 256
  dE=2,dL=0,dN=0,M:(2)->(2,2,2): 132
```

For p=23 residuals:

```text
best_delta_histogram includes:
  dE=0,dL=0,dN=0,M:(2)->(2): 711
  dE=1,dL=0,dN=0,M:(2)->(2,2): 432
  dE=2,dL=0,dN=0,M:(2)->(2,2,2): 293
```

So the neutral cases are not noise; they preserve the exact current defect.

The worse cases mainly increase `E`, often keeping or shortening `L_min`.

## Why m=3 is special

For `m>3`, the block-permutation family frequently finds a `D_short` descent.

For `m=3`, the active zero interval is minimal beyond an inverse pair, and the terminal relation is:

```text
sum(B)=a+b.
```

This externalizes the two-atom prefix of the zero triple.

Since `B` is long, `|B|>=2`, so the support block has at least the same length as the two-atom prefix.

The residual is therefore an equal-sum replacement of a two-atom block by a longer block.

## Candidate progress coordinate

Define a terminal residual coordinate:

```text
P_terminal = distance of the unique zero triple from the boundary or from the terminal support endpoint.
```

A neutral move preserving `D_short=(1,3,1,[2])` may still move the unique zero triple toward a boundary or increase/decrease the terminal support length.

Possible tie-breaks:

```text
1. minimize D_short;
2. among those, minimize distance from the unique zero triple to nearest boundary;
3. among those, minimize terminal support length;
4. among those, lexicographically minimize the local pattern class.
```

The neutral branch should then become descent in the refined defect.

## Candidate theorem S21.1: unique zero triple terminal residual is not terminal-stable

Let `R` be minimal under a refined defect order and suppose:

```text
D_short(R) = (1,3,1,[2]),
Z = a b z,
sum(Z)=0,
R = X a b z q B Y,
sum(B)=a+b,
|B|>=2.
```

Then one of the finite block permutations of `A,z,q,B`, with `A=a b`, either:

```text
1. decreases D_short;
2. preserves D_short but decreases the refined terminal coordinate;
3. exposes a signed/distributed bridge;
4. moves the unique zero triple to a boundary, where a final rotation removes it.
```

## Boundary subcase

If the unique zero triple is at a boundary:

```text
R = a b z q B Y
```

then moving `z` away from `a b` or moving `q` before the triple often breaks the only zero interval.  If no new collision is created, this gives `E=0`.

If a new collision is created, because the old ordering had only one collision, the new collision must involve a moved endpoint.  That collision should be classified as signed/distributed/terminal.

## Next empirical task

The next script should analyze neutral moves specifically.

Create:

```text
scripts/summarize_m3_terminal_progress.py
```

Input:

```text
logs/one_sided_terminal_block_perms_p17.jsonl
logs/one_sided_terminal_block_perms_p23.jsonl
```

For records with:

```text
record_best_class in {neutral,worse},
defect=(1,3,1,[2]),
m=3,
```

extract best neutral moves and compute:

```text
1. old unique zero interval position;
2. new unique zero interval position;
3. distance to left boundary before/after;
4. distance to right boundary before/after;
5. terminal support length before/after if detectable;
6. whether zero triple changed atoms;
7. whether neutral move shifts the zero triple left/right.
```

## Proof priority

The next proof path is no longer broad external bridge.

It is:

```text
m=3 unique-zero-triple terminal residual
```

Attack order:

```text
1. measure neutral progress under finite permutation menu;
2. define refined defect coordinate from the observed monotonic quantity;
3. prove neutral moves decrease the refined coordinate;
4. handle worse-only residual by boundary/signed/distributed classification.
```

## Status

```text
Residual fully localized:
  m=3, D_short=(1,3,1,[2]).
Next step:
  analyze neutral progress and define refined terminal tie-break.
```
