# Analytic symbolic classifier A21: interval-trap classification tool

This note documents the first symbolic tool for the residual interval traps from A19/A20.

Tool:

```text
scripts/classify_interval_traps.py
```

The script implements the interval-geometry table from:

```text
docs/analytic_equal_interval_uncrossing_a20.md
```

It is not a proof of endpoint avoidance.  It is a reproducible classifier for the residual geometry cases.

---

## Input model

An interval is represented as

```text
(x,y]
```

with

```text
0 <= x < y <= t.
```

A relation has sign:

```text
+1:  sum(x,y] =  sum(u,v]
-1:  sum(x,y] = -sum(u,v]
```

The script is invoked as:

```bash
python3 scripts/classify_interval_traps.py \
  --t 20 --x 2 --y 8 --u 5 --v 12 --sign 1
```

---

## Output classes

The classifier returns one of the following classes.

### Collapse classes

```text
collapse_old_collision
collapse_prefix_zero
collapse_interior_zero
```

These are already understood branches:

- old nonempty partial-sum collision;
- allowed prefix-zero branch;
- forbidden interior zero-sum interval.

### Reduction classes

```text
reduction_equal_outer_pieces
```

This means proper-overlap equal intervals have been reduced to shorter separated equal outer pieces.

### Residual classes

```text
residual_two_piece_zero
residual_midpoint
residual_separated_equal
residual_separated_signed
residual_signed_overlap_weighted
residual_signed_nested_weighted
residual_signed_self
residual_shared_left_signed
residual_shared_right_signed
```

These remain mathematical work.

---

## Examples

### Shared-left collapse

```bash
python3 scripts/classify_interval_traps.py --t 20 --x 3 --y 8 --u 3 --v 10 --sign 1
```

Output class:

```text
collapse_old_collision
```

Reason:

```text
S_8=S_10
```

### Shared-right prefix-zero

```bash
python3 scripts/classify_interval_traps.py --t 20 --x 0 --y 8 --u 3 --v 8 --sign 1
```

Output class:

```text
collapse_prefix_zero
```

Reason:

```text
S_3=0
```

### Proper overlap equal intervals

```bash
python3 scripts/classify_interval_traps.py --t 20 --x 2 --y 8 --u 5 --v 12 --sign 1
```

Output class:

```text
reduction_equal_outer_pieces
```

Derived relation:

```text
sum(2,5]=sum(8,12]
```

### Adjacent signed collapse

```bash
python3 scripts/classify_interval_traps.py --t 20 --x 2 --y 8 --u 8 --v 12 --sign -1
```

Output class:

```text
collapse_interior_zero
```

Derived relation:

```text
sum(2,12]=0
```

---

## How this fits A19/A20

A19 shows that each residual atom trap plus the local blocker gives either:

```text
sum(h-1,j] = sum(u,v]
```

or

```text
sum(h-1,j] = -sum(u,v].
```

A21 classifies the geometry of the interval pair.

The next task is row-specific: for each residual family F1r--F6r and S1r--S5r, feed the known index inequalities into this classifier.  The base classifier is deliberately syntactic and does not yet know facts such as:

```text
j<h or j>h,
i<h-1,
beta<h,
alpha>=2h,
```

Those constraints should be encoded in a later A22 row-specific classifier.

---

## Current status

Implemented:

1. equal-interval geometry classifier;
2. signed-equal-interval geometry classifier;
3. command-line interface;
4. documented class names and examples.

Not implemented:

1. row-specific A19 residual classifier;
2. automatic use of branch inequalities;
3. proof elimination of residual classes;
4. endpoint avoidance theorem.
