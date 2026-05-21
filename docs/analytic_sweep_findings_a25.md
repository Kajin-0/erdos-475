# Analytic sweep findings A25: residual priority after A24

This note records the main finding from the A24 symbolic sweep.

Log:

```text
logs/a24_sweep_max_t20_summary.txt
```

The sweep used the same symbolic classifier logic as:

```text
scripts/sweep_a23_residual_histograms.py
```

with `max_t=20`, both with and without the optional secondary inequalities.

---

## Finding 1: secondary constraints help but do not close the residuals

With secondary constraints enabled, the symbolic row volume drops substantially.

### FIRST branch

```text
without secondary: 844341 rows
with secondary:    421725 rows
```

### SECOND branch

```text
without secondary: 740316 rows
with secondary:    394884 rows
```

So the secondary minimality constraints remove roughly half the symbolic rows.

However, the major residual geometry classes remain.

---

## Finding 2: endpoint-sharing and adjacent-signed collapses are not the bottleneck

The sweep confirms that many rows already collapse to:

```text
collapse_old_collision
collapse_prefix_zero
collapse_interior_zero
identical
```

These are not the main remaining proof problem.

The proof should now focus on the residual composite interval classes.

---

## Priority residual classes after secondary constraints

### FIRST branch, secondary constraints enabled

```text
reduction_equal_outer_pieces:      124530
residual_two_piece_zero:           109713
residual_signed_nested_weighted:    23592
residual_signed_overlap_weighted:   13524
residual_shared_left_signed:        11028
residual_separated_signed:           2856
```

### SECOND branch, secondary constraints enabled

```text
reduction_equal_outer_pieces:       74817
residual_two_piece_zero:            73002
residual_signed_overlap_weighted:   51966
residual_separated_signed:          45834
residual_signed_nested_weighted:    12852
residual_shared_left_signed:         9048
residual_midpoint:                   3816
residual_separated_equal:            3906
```

---

## Main proof implication

The remaining proof is not primarily a local adjacent-swap problem anymore.

It has become a composite interval surgery problem involving:

```text
1. equal outer-piece descent;
2. two-piece zero relocation;
3. separated signed composite relocation;
4. weighted signed overlap/nesting elimination;
5. midpoint branch elimination.
```

---

## Target A26: composite interval surgery lemmas

The next proof layer should define and attack the following general lemmas.

### Lemma A26.1: equal outer-piece descent

If a residual relation reduces to

```text
sum(A)=sum(C)
```

for two separated outer pieces created by a proper overlap, then either:

```text
1. the equal-interval trap has strictly smaller span than the original;
2. the outer pieces can be exchanged to produce an earlier forbidden hit;
3. the exchange exposes a zero-sum/pair trap already classified.
```

### Lemma A26.2: two-piece zero relocation

If

```text
sum(A)+sum(C)=0
```

for two separated pieces, then either:

```text
1. a cyclic cut makes A and C adjacent, producing an ordinary zero-sum interval;
2. the gap relocation avoids f;
3. failure creates a shorter equal-interval trap.
```

### Lemma A26.3: separated signed composite relocation

If

```text
sum(A)=-sum(C)
```

for two separated intervals, then the composite `A+C` is zero-sum.  The goal is to move the middle gap away so the two pieces become adjacent, then use the zero-sum-block relocation formulas from A9.

### Lemma A26.4: weighted signed overlap/nesting elimination

For relations such as

```text
sum(A)+2sum(B)+sum(C)=0,
```

one must use the fact that the same relation arose from a singleton atom `b` and a local blocker.  The coefficient `2` is not arbitrary; it is produced by signed overlap.  The likely repair is a midpoint or pair-swap move.

---

## Current status

Proved/implemented:

1. max_t=20 symbolic sweep summary;
2. residual priority ordering;
3. identification that composite interval surgery is now the main bottleneck.

Not proved:

1. equal outer-piece descent;
2. two-piece zero relocation;
3. separated signed composite relocation;
4. weighted signed branch elimination;
5. endpoint avoidance theorem.
