# S41. Genuine obstruction coverage status

This note records the filtered genuine-obstruction output from:

```text
scripts/summarize_hidden_bridge_genuine_obstructions.py
```

using:

```text
logs/summary_hidden_bridge_genuine_obstructions_p17.json
logs/summary_hidden_bridge_genuine_obstructions_p23.json
```

## Main split

After filtering out expected intervals:

```text
old_Az
terminal_zB
hidden_reduced_exact
```

the branch splits cleanly:

```text
Equality branches:
  B_tail+q=A_complement
  B_prefix=q

Zero-sum branches:
  B_tail+q
  B_tail+q+Y_prefix
```

## Equality branches

The equality branches remain neutral and have no genuine secondary obstruction in the current move menu.

### p=17

```text
B_tail+q=A_complement:
  records = 4
  record_has_genuine = no: 4
```

### p=23

```text
B_tail+q=A_complement:
  records = 5
  record_has_genuine = no: 5

B_prefix=q:
  records = 2
  record_has_genuine = no: 2
```

Interpretation:

```text
Equality branches likely require only a refined tie-break or cyclic-rank/position-rank argument.
```

## Zero-sum branches

The zero-sum branches always have a genuine secondary obstruction after filtering.

### p=17

```text
B_tail+q:
  records = 23
  record_has_genuine = yes: 23
  Bq_zero record coverage = 23 / 23

B_tail+q+Y_prefix:
  records = 8
  record_has_genuine = yes: 8
  BqY_zero record coverage = 8 / 8
```

### p=23

```text
B_tail+q:
  records = 20
  record_has_genuine = yes: 20
  Bq_zero record coverage = 20 / 20

B_tail+q+Y_prefix:
  records = 32
  record_has_genuine = yes: 32
  BqY_zero record coverage = 29 / 32
```

The only incomplete universal family is:

```text
p=23, B_tail+q+Y_prefix:
  BqY_zero = 29 / 32
```

Therefore there are exactly three p=23 records in this family that need diagnosis.

## Proof-relevant statements now supported

### Lemma candidate A: pure B-tail zero-sum branch

```text
If the verified hidden-support equation is B_tail+q=0,
then every best failed bridge move creates a genuine Bq_zero secondary collision.
```

Observed support:

```text
p=17: 23 / 23
p=23: 20 / 20
```

### Lemma candidate B: exterior tail zero-sum branch

```text
If the verified hidden-support equation is B_tail+q+Y_prefix=0,
then every best failed bridge move creates a genuine secondary obstruction.
```

Observed support:

```text
p=17: 8 / 8
p=23: 32 / 32
```

Most of these are `BqY_zero`:

```text
p=17: 8 / 8
p=23: 29 / 32
```

The p=23 residual three cases need a gap diagnostic.

## Next diagnostic

Add:

```text
scripts/diagnose_genuine_obstruction_coverage_gaps.py
```

Target invocation:

```bash
python3 scripts/diagnose_genuine_obstruction_coverage_gaps.py \
  --analysis logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl \
  --equations logs/bzqa_hidden_support_equations_p23_v3.jsonl \
  --bridge logs/hidden_support_bridge_moves_p23_v5.jsonl \
  --target-family 'B_tail+q+Y_prefix' \
  --target-class BqY_zero \
  --out logs/gaps_Btail_q_Yprefix_missing_BqY_p23.jsonl \
  --summary-out logs/summary_gaps_Btail_q_Yprefix_missing_BqY_p23.json
```

The goal is to identify what replaces `BqY_zero` in the three gap records:

```text
B_prefix_or_mixed?
right_exterior_zY?
other?
```

## Current proof state

```text
1. Hidden-support equation is universally verified.
2. Equality branches are neutral and need tie-break refinement.
3. Zero-sum B_tail+q branch has universal Bq_zero secondary obstruction.
4. Zero-sum B_tail+q+Y_prefix branch has universal genuine obstruction, mostly BqY_zero.
5. Three p=23 records must be diagnosed to complete the exterior-tail obstruction classification.
```
