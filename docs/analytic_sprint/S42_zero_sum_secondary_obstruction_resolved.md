# S42. Zero-sum secondary obstruction resolved

This note records the gap diagnostic for the exterior zero-sum hidden-support branch.

## Input

The diagnostic run was:

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

Output:

```text
target_family = B_tail+q+Y_prefix
target_class = BqY_zero
target_records = 32
records_with_target_class = 32
gap_records = 0
gap_record_indices = []
```

## Resolution

The earlier filtered summary reported:

```text
B_tail+q+Y_prefix, p=23:
  BqY_zero = 29 / 32
```

That was a restricted count from the compact filtered summary.  The direct gap diagnostic checks record-level existence across the best bridge moves and shows:

```text
B_tail+q+Y_prefix, p=23:
  BqY_zero = 32 / 32
```

Therefore the apparent three-record gap is resolved.

## Universal zero-sum obstruction coverage

For the hidden-support zero-sum branches:

```text
B_tail+q = 0
B_tail+q+Y_prefix = 0
```

we now have universal secondary-obstruction coverage.

### Pure tail case

```text
B_tail+q = 0
  p=17: Bq_zero = 23 / 23
  p=23: Bq_zero = 20 / 20
```

### Exterior tail case

```text
B_tail+q+Y_prefix = 0
  p=17: BqY_zero = 8 / 8
  p=23: BqY_zero = 32 / 32
```

## Proof interpretation

The zero-sum hidden-support branches do not become immediate descent moves under the naive bridge menu.  However, every failed bridge move exposes a genuine secondary zero interval of the same algebraic type:

```text
B_tail+q=0            -> Bq_zero
B_tail+q+Y_prefix=0   -> BqY_zero
```

Thus the failed bridge move is not arbitrary.  It is structurally self-replicating: trying to realize the hidden zero-sum support relation contiguously produces another zero-sum relation involving `q` and a support/exterior block.

## Formal lemma candidate

```text
Lemma: Hidden zero-sum support obstruction.
Let R = X A z q B Y be a pure worse-only m=3 right-terminal residual.
If the B z q A extraction gives a zero-sum hidden-support equation

  B_tail + q = 0

or

  B_tail + q + Y_prefix = 0,

then every best bridge realization of that equation either descends in D_short
or exposes a genuine secondary zero interval of type

  Bq_zero

or

  BqY_zero,

respectively.
```

Empirically, in the observed samples, the bridge realization does not descend but always exposes the secondary obstruction.

## Remaining branch structure

The pure worse-only branch is now partitioned into:

```text
1. zero-sum tail branch:
   B_tail+q = 0
   -> universal Bq_zero secondary obstruction.

2. zero-sum exterior-tail branch:
   B_tail+q+Y_prefix = 0
   -> universal BqY_zero secondary obstruction.

3. equality branch:
   B_tail+q = A_complement
   -> neutral under current moves.

4. prefix equality branch:
   B_prefix = q
   -> neutral under current moves.
```

## Status

```text
The zero-sum hidden-support branch is fully classified.
Remaining hard work: prove the secondary Bq/BqY obstruction forces an earlier branch or define a refined descent order for equality branches.
```
