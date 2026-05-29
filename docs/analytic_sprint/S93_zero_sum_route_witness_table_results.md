# S93. Zero-sum route witness table results

This note records the output of:

```text
scripts/make_zero_sum_route_witness_table.py
```

using:

```text
logs/zero_sum_route_witness_table.md
logs/zero_sum_route_witness_table.json
```

## Main result

The zero-sum route witness table was successfully generated.

Summary:

```text
rows = 24
```

By family:

```text
B_tail+q:          12
B_tail+q+Y_prefix: 12
```

By route label:

```text
CLEAN_DESCENT:       6
DISTRIBUTED_BRIDGE:  6
EXTERNAL_BRIDGE:     6
MIXED:               6
```

By family and route:

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

Thus the table has balanced witness coverage across:

```text
2 zero-sum families x 4 route labels x 3 examples = 24 rows.
```

## Representative rows

### Bq_zero / CLEAN_DESCENT

Example:

```text
family: B_tail+q
target: Bq_zero
route_label: CLEAN_DESCENT
p: 17
record_index: 24
reduced_equation: B3 B4 q
active_symbolic_order: A1 A2 z q B1 B2 B3 B4
hidden_equation: B3 B4 q
useful_route_flags: [CLEAN_DESCENT]
route_flag_counts: {CLEAN_DESCENT:18}
```

### Bq_zero / DISTRIBUTED_BRIDGE

Example:

```text
family: B_tail+q
target: Bq_zero
route_label: DISTRIBUTED_BRIDGE
p: 17
record_index: 338
reduced_equation: B2 B3 q
active_symbolic_order: A1 A2 z q B1 B2 B3
hidden_equation: B2 B3 q
useful_route_flags: [DISTRIBUTED_BRIDGE]
route_flag_counts: {DISTRIBUTED_BRIDGE:1}
```

### Bq_zero / EXTERNAL_BRIDGE

Example:

```text
family: B_tail+q
target: Bq_zero
route_label: EXTERNAL_BRIDGE
p: 17
record_index: 24
reduced_equation: B3 B4 q
active_symbolic_order: A1 A2 z q B1 B2 B3 B4
hidden_equation: B3 B4 q
useful_route_flags: [EXTERNAL_BRIDGE]
route_flag_counts: {EXTERNAL_BRIDGE:5}
```

### Bq_zero / MIXED

Example:

```text
family: B_tail+q
target: Bq_zero
route_label: MIXED
p: 17
record_index: 24
reduced_equation: B3 B4 q
active_symbolic_order: A1 A2 z q B1 B2 B3 B4
hidden_equation: B3 B4 q
useful_route_flags: [CLEAN_DESCENT, EXTERNAL_BRIDGE, LEFT_TERMINAL_BRIDGE, LONG_TERMINAL_BRIDGE, RIGHT_TERMINAL_BRIDGE, SHORT_TERMINAL_BRIDGE]
```

### BqY_zero / CLEAN_DESCENT

Example:

```text
family: B_tail+q+Y_prefix
target: BqY_zero
route_label: CLEAN_DESCENT
p: 17
record_index: 0
reduced_equation: B3 q Y1
active_symbolic_order: A1 A2 z q B1 B2 B3
hidden_equation: B3 q Y1
useful_route_flags: [CLEAN_DESCENT]
route_flag_counts: {CLEAN_DESCENT:42}
```

### BqY_zero / DISTRIBUTED_BRIDGE

Example:

```text
family: B_tail+q+Y_prefix
target: BqY_zero
route_label: DISTRIBUTED_BRIDGE
p: 17
record_index: 666
reduced_equation: B2 B3 B4 q Y1
active_symbolic_order: A1 A2 z q B1 B2 B3 B4
hidden_equation: B2 B3 B4 q Y1
useful_route_flags: [DISTRIBUTED_BRIDGE]
route_flag_counts: {DISTRIBUTED_BRIDGE:3}
```

### BqY_zero / EXTERNAL_BRIDGE

Example:

```text
family: B_tail+q+Y_prefix
target: BqY_zero
route_label: EXTERNAL_BRIDGE
p: 23
record_index: 31
reduced_equation: B3 B4 B5 B6 q Y1
active_symbolic_order: A1 A2 z q B1 B2 B3 B4 B5 B6
hidden_equation: B3 B4 B5 B6 q Y1
useful_route_flags: [EXTERNAL_BRIDGE]
route_flag_counts: {EXTERNAL_BRIDGE:2}
```

### BqY_zero / MIXED

Example:

```text
family: B_tail+q+Y_prefix
target: BqY_zero
route_label: MIXED
p: 17
record_index: 0
reduced_equation: B3 q Y1
active_symbolic_order: A1 A2 z q B1 B2 B3
hidden_equation: B3 q Y1
useful_route_flags: [CLEAN_DESCENT, EXTERNAL_BRIDGE, LONG_TERMINAL_BRIDGE, RIGHT_TERMINAL_BRIDGE]
```

## Interpretation

The route witness table confirms that the zero-sum route labels are attached to explicit hidden equations:

```text
Bq_zero examples:
  B2 B3 q,
  B3 B4 q,
  B3 B4 B5 q,
  B4 B5 B6 q.

BqY_zero examples:
  B3 q Y1,
  B2 B3 q Y1,
  B3 B4 q Y1,
  B2 B3 q Y1 Y2 Y3,
  B3 B4 B5 B6 q Y1.
```

The available witness fields expose:

```text
hidden_equation,
useful_route_flags,
route_flag_counts,
route_label_counts,
move_routes.
```

These are enough to begin translating route labels into symbolic partial-sum cases.

## Proof translation targets

### CLEAN_DESCENT

Rows with `useful_route_flags=[CLEAN_DESCENT]` should be translated into:

```text
there exists a local move whose resulting defect is strictly smaller.
```

The `representative_move_routes` field contains the attempt-level data needed to identify the move.

### DISTRIBUTED_BRIDGE

Rows with `useful_route_flags=[DISTRIBUTED_BRIDGE]` should be translated into:

```text
the zero-sum hidden equation creates a repeated-sum bridge distributed across more than one local support component.
```

### EXTERNAL_BRIDGE

Rows with `useful_route_flags=[EXTERNAL_BRIDGE]` should be translated into:

```text
the zero-sum relation aligns an active-window partial sum with an exterior partial sum.
```

This is especially natural for `BqY_zero` because the hidden equation includes a `Y_prefix`.

### MIXED

Rows with `MIXED` collect simultaneous flags such as:

```text
CLEAN_DESCENT,
EXTERNAL_BRIDGE,
LEFT_TERMINAL_BRIDGE,
LONG_TERMINAL_BRIDGE,
RIGHT_TERMINAL_BRIDGE,
SHORT_TERMINAL_BRIDGE,
SIGNED_INTERVAL.
```

These should be handled by choosing any one closed route flag as the formal exit.

## Next proof step

The next useful script should extract a single representative move from `representative_move_routes` for each row and print:

```text
route_label,
branch_flags,
bridge_interval,
bridge_sum or symbolic block,
old/new defect if present.
```

That would make the `CLEAN_DESCENT`, `EXTERNAL_BRIDGE`, and `DISTRIBUTED_BRIDGE` routes fully explicit.

## Status

```text
Zero-sum route witness table generated.
Balanced symbolic examples exist for every zero-sum family-route pair.
Next: extract attempt-level witness moves from representative_move_routes.
```
