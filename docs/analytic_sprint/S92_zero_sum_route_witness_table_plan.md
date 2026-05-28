# S92. Zero-sum route witness table plan

S91 confirmed that representative route examples now extract correctly from the detailed route JSONL files.

The extractor now uses:

```text
route_label_counts
```

rather than:

```text
best_class
```

so it finds the true route mechanisms:

```text
CLEAN_DESCENT,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
MIXED.
```

## Current example coverage

```text
examples_found = 24
missing_route_jsonl_files = []
unmatched_route_rows = 0
```

Balanced by family and route:

```text
B_tail+q::CLEAN_DESCENT:                3
B_tail+q::DISTRIBUTED_BRIDGE:           3
B_tail+q::EXTERNAL_BRIDGE:              3
B_tail+q::MIXED:                        3
B_tail+q+Y_prefix::CLEAN_DESCENT:       3
B_tail+q+Y_prefix::DISTRIBUTED_BRIDGE:  3
B_tail+q+Y_prefix::EXTERNAL_BRIDGE:     3
B_tail+q+Y_prefix::MIXED:               3
```

## Goal

Compress the 24 examples into a proof-facing witness table.

Each row should include:

```text
family,
target,
route_label,
p,
record_index,
reduced_equation,
active_symbolic_order,
hidden_equation,
useful_route_flags,
route_flag_counts,
representative_move_routes.
```

## New script

Add:

```text
scripts/make_zero_sum_route_witness_table.py
```

Input:

```text
logs/zero_sum_route_examples.jsonl
```

Outputs:

```text
logs/zero_sum_route_witness_table.md
logs/zero_sum_route_witness_table.json
```

## Proof use

The table should expose, for each route mechanism:

```text
CLEAN_DESCENT:
  which move produces descent.

DISTRIBUTED_BRIDGE:
  which repeated structure gives distributed routing.

EXTERNAL_BRIDGE:
  which exterior-crossing structure appears.

MIXED:
  which simultaneous flags occur.
```

This table is the bridge between the route labels and the symbolic partial-sum proof needed for Lemma Z.

## Status

```text
Representative examples exist for every family-route pair.
Next: compress them into a route witness table.
```
