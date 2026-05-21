# Analytic normalization pass A27: controlled residual reductions

This note documents the interval-relation normalizer:

```text
scripts/normalize_interval_relation.py
```

The tool implements the controlled descent from A26 for equal proper-overlap interval traps.

---

## Purpose

A25/A26 separate residual classes into:

```text
controlled descent classes,
zero-composite relocation classes,
hard weighted/midpoint classes.
```

A27 makes the first category executable.  It repeatedly applies:

```text
sum(x,y] = sum(u,v],   x<u<y<v
    ->
sum(x,u] = sum(y,v]
```

This is the A26.1 equal-outer-piece reduction.

A26.1 proves this reduction strictly lowers total span, so the normalization must terminate.

---

## Usage

Example proper-overlap equal relation:

```bash
python3 scripts/normalize_interval_relation.py \
  --t 30 --x 2 --y 14 --u 8 --v 20 --sign 1
```

This starts from:

```text
sum(2,14] = sum(8,20]
```

and reduces to:

```text
sum(2,8] = sum(14,20]
```

JSON output:

```bash
python3 scripts/normalize_interval_relation.py \
  --t 30 --x 2 --y 14 --u 8 --v 20 --sign 1 --json
```

---

## Output

The tool reports:

```text
status
terminal_relation
terminal_class
trace
```

The trace records each relation, span, geometry class, and applied reduction.

---

## Current implemented reductions

Implemented:

```text
A26.1 equal proper-overlap descent
```

Not yet implemented:

```text
two-piece zero relocation normalization,
separated signed composite relocation,
midpoint branch elimination,
weighted signed overlap/nesting elimination.
```

---

## Proof meaning

The normalizer does not prove endpoint avoidance.  It proves only that one class of residual relation is not terminal:

```text
reduction_equal_outer_pieces
```

can be iterated until it reaches a terminal geometry class.

The terminal class may still be hard, for example:

```text
residual_separated_equal
residual_two_piece_zero
residual_midpoint
```

But the normalizer prevents treating proper-overlap equal intervals as independent proof obligations.

---

## Current status

Implemented:

1. relation representation;
2. span computation;
3. A26.1 proper-overlap equal descent;
4. termination guard via strict span descent;
5. trace output and JSON output.

Not implemented:

1. automatic integration with A23/A24 batch histograms;
2. relocation normalization for two-piece zero composites;
3. final elimination of terminal residual classes;
4. endpoint avoidance theorem.
