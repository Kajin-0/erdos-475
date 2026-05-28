# S91. Zero-sum route example extraction results

This note records the successful rerun of:

```text
scripts/extract_zero_sum_route_examples.py
```

after patching the extractor to use:

```text
route_label_counts
```

instead of:

```text
best_class
```

The field `best_class=worse` is the bridge/move class, not the route mechanism.

## Main result

The extractor now finds representative examples for both zero-sum families and all four route labels.

Summary:

```text
examples_found = 24
missing_route_jsonl_files = []
unmatched_route_rows = 0
```

By family:

```text
B_tail+q:          12 examples
B_tail+q+Y_prefix: 12 examples
```

By route label:

```text
CLEAN_DESCENT:       6 examples
DISTRIBUTED_BRIDGE:  6 examples
EXTERNAL_BRIDGE:     6 examples
MIXED:               6 examples
```

By family and route:

```text
B_tail+q::CLEAN_DESCENT:           3
B_tail+q::DISTRIBUTED_BRIDGE:      3
B_tail+q::EXTERNAL_BRIDGE:         3
B_tail+q::MIXED:                   3
B_tail+q+Y_prefix::CLEAN_DESCENT:  3
B_tail+q+Y_prefix::DISTRIBUTED_BRIDGE: 3
B_tail+q+Y_prefix::EXTERNAL_BRIDGE:    3
B_tail+q+Y_prefix::MIXED:              3
```

## Interpretation

The route-example extraction now aligns with the zero-sum route certificate in S87.

The detailed JSONL schema is:

```text
best_class          = bridge/move class, usually worse
route_label_counts  = actual route-mechanism counts
```

Therefore symbolic examples should be grouped by `route_label_counts` keys:

```text
CLEAN_DESCENT,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
MIXED.
```

## Current output artifact

The examples are written to:

```text
logs/zero_sum_route_examples.jsonl
```

The summary is written to:

```text
logs/summary_zero_sum_route_examples.json
```

Each example includes:

```text
p,
record_index,
family,
target,
bridge_class,
route_label,
route_label_count,
reduced_equation,
active_symbolic_order,
witness.
```

The `witness` object currently carries the available row-level route data:

```text
hidden_equation,
useful_route_flags,
route_flag_counts,
route_label_counts,
move_routes.
```

## Proof use

This gives a balanced sample set for converting the zero-sum routing lemma from label-level language into partial-sum language.

The intended next proof translation is:

```text
CLEAN_DESCENT:
  identify the local rearrangement that strictly improves D_short.

DISTRIBUTED_BRIDGE:
  identify the distributed repeated-sum structure.

EXTERNAL_BRIDGE:
  identify the active-to-exterior repeated-sum equality.

MIXED:
  decompose into the simultaneous route flags present in useful_route_flags / route_flag_counts.
```

## Next diagnostic target

The next useful script should summarize the witness fields inside the 24 extracted examples:

```text
hidden_equation,
useful_route_flags,
route_flag_counts,
move_routes.
```

The goal is to produce a compact symbolic witness table:

```text
| family | route_label | record_index | reduced_equation | active_order | useful_flags | representative_move |
```

This will make S88 proof-ready.

## Status

```text
Zero-sum route example extraction fixed.
Representative examples exist for every family-route pair.
Next: compress witness details into a symbolic route-witness table.
```
