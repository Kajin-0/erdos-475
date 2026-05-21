# Analytic batch residual classifier A23

This note documents the batch classifier:

```text
scripts/batch_classify_a19_residuals.py
```

It builds on:

```text
scripts/classify_interval_traps.py
scripts/classify_a19_residual_row.py
```

The goal is to enumerate branch-valid symbolic index ranges for the A19 residual families and produce histograms of A20 geometry classes.

---

## What the tool does

For a chosen branch, the script enumerates all positional residual rows consistent with the basic branch inequalities.

### FIRST branch input

```bash
python3 scripts/batch_classify_a19_residuals.py \
  --branch first --t 30 --h 10 --alpha 22
```

FIRST branch assumptions:

```text
R = L U V
L=(1..h)
U=(h+1..alpha)
V=(alpha+1..t)
sum(L)=sum(U)=f
```

The singleton-prefix move requires:

```text
|U| >= 2
```

so:

```text
alpha >= h+2.
```

The tool enumerates residual families:

```text
F1r, F3r, F4r, F5r, F6r
```

`F2r` is excluded because it is the prefix-zero branch, not an atom-equals-interval row.

### SECOND branch input

```bash
python3 scripts/batch_classify_a19_residuals.py \
  --branch second --t 30 --h 10 --beta 4
```

SECOND branch assumptions:

```text
R = A B C
A=(1..beta)
B=(beta+1..h)
C=(h+1..t)
sum(B)=sum(C)=sigma-f
```

The singleton-prefix move requires:

```text
|C| >= 2.
```

The boundary case

```text
beta=h
```

is excluded because it is already a pair-trap boundary.

The tool enumerates residual families:

```text
S1r, S2r, S3r, S4r, S5r
```

---

## Local blocker enumeration

For each residual row, the tool also enumerates the local blocker index `j` from A5:

```text
S_{h-1}+b=S_j,
j != h.
```

The case

```text
j=h-1
```

is skipped because it would force

```text
b=0.
```

The tool uses the A22 orientation-correct normalization:

```text
b=S_j-S_{h-1}
```

is represented as a signed interval depending on whether `j` lies before or after `h-1`.

---

## Output

The script prints:

```text
total_rows
by_class
by_family_class
```

With `--show-examples`, it also prints one example row for each geometry class.

With `--json`, it emits the full summary object as JSON.

---

## Interpretation

The important classes are divided into three categories.

### Immediate collapse classes

```text
collapse_old_collision
collapse_prefix_zero
collapse_interior_zero
```

These are not final proof gaps; they map to already understood contradiction or prefix-zero branches.

### Reduction class

```text
reduction_equal_outer_pieces
```

This means the residual row reduces to a shorter equal-interval trap.

### Genuine residual classes

```text
residual_midpoint
residual_two_piece_zero
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

## Example commands for audit

FIRST branch sample:

```bash
python3 scripts/batch_classify_a19_residuals.py \
  --branch first --t 30 --h 10 --alpha 22 --show-examples
```

SECOND branch sample:

```bash
python3 scripts/batch_classify_a19_residuals.py \
  --branch second --t 30 --h 10 --beta 4 --show-examples
```

JSON sample:

```bash
python3 scripts/batch_classify_a19_residuals.py \
  --branch first --t 30 --h 10 --alpha 22 --json
```

---

## Current status

Implemented:

1. branch-valid enumeration for FIRST residual families;
2. branch-valid enumeration for SECOND residual families away from `beta=h`;
3. local blocker enumeration with `j=h,h-1` exclusions;
4. orientation-correct row classification via A22;
5. class and family histograms;
6. optional examples and JSON output.

Not implemented:

1. using stronger secondary inequalities such as `alpha>=2h` or `beta>=2h-t` selectively;
2. symbolic proof elimination of residual classes;
3. automatic generation of manuscript tables;
4. endpoint avoidance theorem.
