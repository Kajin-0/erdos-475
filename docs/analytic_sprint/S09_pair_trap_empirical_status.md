# S09. Pair-trap empirical status

This file records the first low-compute test result for the S08 pair-trap elimination attack.

## Test configuration

The VM run used:

```bash
python3 scripts/test_pair_trap_moves.py \
  --p 17 \
  --size 9 \
  --max-sets 200 \
  --order-samples 1000 \
  --orders-per-set 10 \
  --random-sets \
  --seed 1 \
  --order-mode defective \
  --active-mode longest \
  --out logs/pair_trap_defective_p17_size9_v3.jsonl
```

## Observed aggregate

```text
sets_seen=200
orders_tested=1820
pair_trap_records=1803
aggregate={
  "danger": 2,
  "external_only": 2584,
  "improved": 11457,
  "supported_results": 14043,
  "unsupported": 14549
}
```

## Interpretation

Among supported trap types:

```text
supported_results = 14043
improved          = 11457
external_only     = 2584
danger            = 2
```

Therefore:

```text
improved + external_only = 14041 / 14043 = 0.99985758...
```

or about:

```text
99.986% routed to descent or external bridge.
```

This is a strong signal that the S08 compression is structurally correct after excluding unsupported trap types.

## Meaning for the proof program

The pair-trap branch should not be treated as a broad hard case.

Current evidence suggests:

```text
PAIR_TRAP
  -> D_short descent
  or EXTERNAL_BRIDGE
  except for a tiny residual danger class.
```

The correct next task is not to expand the state machine.  It is to inspect the two danger cases and determine whether they are:

```text
1. script-classification artifacts;
2. unsupported endpoint degeneracies incorrectly counted as supported;
3. real residual pair-trap obstructions needing a sharper move;
4. evidence that D_short needs one extra tie-break coordinate.
```

## Immediate next command

Extract compact danger records:

```bash
jq -c 'select(.summary.danger > 0)' \
  logs/pair_trap_defective_p17_size9_v3.jsonl \
  > logs/pair_trap_danger_records_v3.jsonl

wc -l logs/pair_trap_danger_records_v3.jsonl
```

Then extract only the dangerous result entries:

```bash
jq -c '{
  p,
  S,
  sigma,
  order,
  partial_sums,
  defect,
  active_zero_interval,
  danger_results: [.results[] | select(.improved == false and .external_collision_change == false and (.move? // "moved") != null)]
}' logs/pair_trap_danger_records_v3.jsonl \
  > logs/pair_trap_danger_only_v3.jsonl
```

## Proof priority update

Before attacking persistent external bridge globally, inspect these two danger cases.

If both are artifacts or endpoint degeneracies, then S08 should be promoted from exploratory to near-lemma status:

```text
Pair-trap block move lemma:
Every supported disjoint/crossing/nested pair trap either decreases D_short or creates an external bridge obstruction.
```

If one danger case is genuine, use it to define the missing residual obstruction class and add one sharper move.

## Status

```text
S08 empirical status: strong support.
Residual: 2 danger cases out of 14043 supported moves.
Next step: inspect danger cases manually and classify them.
```
