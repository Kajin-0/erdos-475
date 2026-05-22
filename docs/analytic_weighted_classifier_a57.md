# Analytic weighted signed classifier A57

This note documents the classifier:

```text
scripts/classify_weighted_signed_normal_form.py
```

It implements the normal-form tests from:

```text
docs/analytic_weighted_signed_normal_forms_a56.md
```

The target relation is:

```text
sum(A)+2sum(B)+sum(C)=0.
```

---

## Purpose

A56 showed that not every coefficient-2 branch is genuinely weighted.

Many are transported-prefix artifacts, zero-composite branches, or endpoint collapses.

A57 makes that classification mechanical.

---

## Usage

Transported prefix artifact:

```bash
python3 scripts/classify_weighted_signed_normal_form.py \
  --transported-prefix --odd-prime
```

Zero doubled block:

```bash
python3 scripts/classify_weighted_signed_normal_form.py \
  --b-zero --odd-prime
```

Adjacent pair zero:

```bash
python3 scripts/classify_weighted_signed_normal_form.py \
  --ab-zero --odd-prime
```

Equal outer pieces:

```bash
python3 scripts/classify_weighted_signed_normal_form.py \
  --outer-equal --odd-prime
```

Genuine weighted core:

```bash
python3 scripts/classify_weighted_signed_normal_form.py \
  --odd-prime
```

JSON output:

```bash
python3 scripts/classify_weighted_signed_normal_form.py \
  --transported-prefix --json
```

---

## Output classes

The classifier returns one of:

```text
transported_prefix_artifact
transported_tail_artifact
zero_doubled_block_collapse
adjacent_pair_zero_left
adjacent_pair_zero_right
equal_outer_reduction
equal_outer_needs_characteristic_check
genuine_weighted_core
```

with statuses such as:

```text
controlled_composite_zero
zero_collapse_or_two_piece_zero
two_piece_zero
two_piece_zero_or_midpoint_boundary
hard_residual
```

---

## Test order

The classifier applies A56 tests in order:

```text
W1 transported-prefix/tail artifact
W2 zero doubled block
W3 adjacent-pair zero
W4 equal outer pieces
W5 genuine weighted core
```

The order is intentional.  Transported-prefix rewrites should be detected before calling something genuinely weighted.

---

## Interpretation

A result of

```text
genuine_weighted_core
```

means only:

```text
none of the currently encoded A56 reductions applies.
```

It does not prove the branch is realizable.  It marks the branch as still needing a new analytic argument or a stronger contextual reduction.

---

## Current status

Implemented:

1. W1 prefix/tail transported artifact detection;
2. W2 zero doubled-block collapse;
3. W3 adjacent-pair zero reductions;
4. W4 equal outer reduction with odd-prime check;
5. W5 genuine weighted-core fallback;
6. JSON output.

Not implemented:

1. automatic extraction of these flags from A20 interval geometry;
2. finite-field realizability checking;
3. elimination of genuine weighted cores;
4. endpoint avoidance theorem.
