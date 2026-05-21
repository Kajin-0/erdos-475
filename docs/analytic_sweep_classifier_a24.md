# Analytic sweep classifier A24: aggregate residual geometry histograms

This note documents the sweep-level classifier:

```text
scripts/sweep_a23_residual_histograms.py
```

A23 classifies residual rows for a fixed symbolic branch instance.  A24 sweeps over many symbolic branch instances and aggregates the geometry classes.

---

## Purpose

The proof program has reduced many equal-sum branch residuals to interval-geometry classes.  Before attacking the remaining classes mathematically, it is useful to know which classes survive the basic index constraints.

A24 answers:

```text
Across all symbolic FIRST / SECOND branch configurations up to max_t,
which A20 geometry classes appear, and in which residual families?
```

This is a proof-audit tool, not a theorem.

---

## Usage

Sweep FIRST branch:

```bash
python3 scripts/sweep_a23_residual_histograms.py \
  --branch first --max-t 30
```

Sweep SECOND branch:

```bash
python3 scripts/sweep_a23_residual_histograms.py \
  --branch second --max-t 30
```

Sweep both:

```bash
python3 scripts/sweep_a23_residual_histograms.py \
  --branch both --max-t 30
```

Use secondary minimality constraints:

```bash
python3 scripts/sweep_a23_residual_histograms.py \
  --branch both --max-t 30 --use-secondary-constraints
```

JSON output:

```bash
python3 scripts/sweep_a23_residual_histograms.py \
  --branch both --max-t 30 --use-secondary-constraints --json
```

---

## FIRST branch sweep constraints

Basic FIRST branch positional constraints:

```text
1 <= h < alpha <= t,
alpha-h >= 2
```

The condition `alpha-h>=2` is required because the singleton-prefix move needs the movable block `U` to have a nonempty remainder after removing `b`.

Optional secondary constraint:

```text
alpha >= 2h
```

This comes from the minimality analysis of the direct equal-sum exchange when the cyclic cut remains Graham-valid.

---

## SECOND branch sweep constraints

Basic SECOND branch positional constraints:

```text
1 <= beta < h < t,
t-h >= 2
```

The boundary case

```text
beta=h
```

is excluded because it is treated as a boundary pair-trap branch.

Optional secondary constraint:

```text
beta >= 2h-t
```

This comes from the minimality analysis of the direct equal-sum exchange when the cyclic cut remains Graham-valid.

---

## Output

For each branch, the tool reports:

```text
config_count
total_rows
by_class
by_family_class
```

The geometry classes are inherited from A21/A22, including:

```text
collapse_old_collision
collapse_prefix_zero
collapse_interior_zero
reduction_equal_outer_pieces
residual_midpoint
residual_two_piece_zero
residual_separated_equal
residual_separated_signed
residual_signed_overlap_weighted
residual_signed_nested_weighted
```

---

## Interpretation guardrail

A24 is purely positional.  It does not know whether a symbolic configuration is algebraically realizable over any finite field, nor whether a given residual equation can coexist with Graham-validity beyond the interval geometry already encoded.

Therefore:

```text
class appears in A24 histogram
```

means only:

```text
this interval geometry is not eliminated by the currently encoded positional constraints.
```

It does not mean the case is truly realizable.

---

## Current status

Implemented:

1. aggregate FIRST sweeps;
2. aggregate SECOND sweeps;
3. optional secondary inequalities;
4. class histograms;
5. family-by-class histograms;
6. JSON output.

Not implemented:

1. automatic proof elimination of residual classes;
2. algebraic realizability checking;
3. export of LaTeX tables;
4. endpoint avoidance theorem.
