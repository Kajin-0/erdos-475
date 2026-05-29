# S19. One-sided long-terminal block permutation status

This file records the result of testing the local block-permutation family for the dominant right-one-sided long-terminal branch.

## Background

S18 identified the right one-sided long-terminal structure:

```text
R = X A z q B Y_r,
Z = A z,
z + sum(B) = 0,
sum(A) = sum(B).
```

The first tested move was the single equal-sum exchange:

```text
A z q B -> B z q A.
```

That move was mostly negative:

```text
p=17: neutral 140, worse 1359
p=23: neutral  94, worse 1173
```

Therefore `scripts/test_one_sided_terminal_exchange.py` was upgraded to test all nontrivial block permutations of:

```text
A, z, q, B
```

while preserving internal order inside `A` and `B`.

## p=17 result

Input:

```text
logs/external_bridge_hard_terminal_lengths_p17.jsonl
```

Command:

```bash
python3 scripts/test_one_sided_terminal_exchange.py \
  logs/external_bridge_hard_terminal_lengths_p17.jsonl \
  --max-candidates 10 \
  --out logs/one_sided_terminal_block_perms_p17.jsonl
```

Observed:

```text
input_records = 2783
eligible_right_one_sided_long_records = 852
aggregate_record_best = {
  "improved": 583,
  "neutral": 220,
  "worse": 49
}
aggregate_candidate_best = {
  "improved": 583,
  "neutral": 220,
  "worse": 49
}
aggregate_move = {
  "improved": 966,
  "neutral": 2852,
  "worse": 15778
}
```

Record-level improvement rate:

```text
583 / 852 ≈ 68.43%
```

Non-worse rate:

```text
(583 + 220) / 852 ≈ 94.25%
```

## p=23 result

Input:

```text
logs/external_bridge_hard_terminal_lengths_p23.jsonl
```

Command:

```bash
python3 scripts/test_one_sided_terminal_exchange.py \
  logs/external_bridge_hard_terminal_lengths_p23.jsonl \
  --max-candidates 10 \
  --out logs/one_sided_terminal_block_perms_p23.jsonl
```

Observed:

```text
input_records = 3391
eligible_right_one_sided_long_records = 756
aggregate_record_best = {
  "improved": 369,
  "neutral": 302,
  "worse": 85
}
aggregate_candidate_best = {
  "improved": 369,
  "neutral": 302,
  "worse": 85
}
aggregate_move = {
  "improved": 491,
  "neutral": 1835,
  "worse": 15062
}
```

Record-level improvement rate:

```text
369 / 756 ≈ 48.81%
```

Non-worse rate:

```text
(369 + 302) / 756 ≈ 88.76%
```

## Interpretation

The single exchange was the wrong local move, but the block-permutation family is highly informative.

At record level:

```text
p=17: 68.43% improved, 94.25% non-worse
p=23: 48.81% improved, 88.76% non-worse
```

This suggests the one-sided long-terminal branch is not a monolithic obstruction.

A local block permutation often provides `D_short` descent.  The remaining hard residue is:

```text
1. neutral block-permutation records;
2. worse-only block-permutation records.
```

The next task is to identify which permutations work and classify the residual records.

## Key next questions

```text
1. Which permutation most often gives improvement?
2. Are neutral records preserving E but failing to improve L_min/N_min/M?
3. Are worse-only records boundary artifacts, wrong orientation, or genuine global obstructions?
4. Do neutral records become improved under left-orientation testing?
5. Do worse-only records contain terminal+distributed or terminal+signed flags already handled elsewhere?
```

## Next script

Add:

```text
scripts/summarize_terminal_block_perms.py
```

It should report:

```text
record_best_class counts
best improving permutation histogram
best neutral permutation histogram
worse-only records
records with any terminal_zero_contiguous move
records with any old_Z_contiguous move
residual examples for inspection
```

## Proof consequence

A plausible next lemma is not:

```text
A single canonical exchange always descends.
```

The data rejects that.

The likely lemma is instead:

```text
For a one-sided long-terminal bridge, at least one local permutation of A,z,q,B either descends or preserves D_short while increasing a terminal-support/endpoint-progress coordinate.  Worse-only cases must route to distributed/signed/two-sided terminal or boundary exhaustion.
```

This indicates `D_short` may need one more terminal-progress tie-break coordinate for the final proof route.

## Status

```text
One-sided long-terminal branch: partially compressed by block permutations.
Main unresolved residue: neutral/worse block-permutation records.
Next empirical target: best-permutation and residual-class summary.
```
