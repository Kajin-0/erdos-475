# S95. Zero-sum attempt-level witness results

This note records the output of:

```text
scripts/extract_zero_sum_attempt_witnesses.py
```

using:

```text
logs/zero_sum_attempt_witnesses.jsonl
logs/summary_zero_sum_attempt_witnesses.json
```

## Main result

The extractor found attempt-level witness information for the zero-sum route examples.

Summary:

```text
rows = 24
matched_route_object_rows = 24
matched_attempt_rows = 23
```

Thus every route-example row has a matching route object, and all but one have a route-label-matching attempt.

## Coverage by family

```text
B_tail+q:          12
B_tail+q+Y_prefix: 12
```

## Coverage by route label

```text
CLEAN_DESCENT:       6
DISTRIBUTED_BRIDGE:  6
EXTERNAL_BRIDGE:     6
MIXED:               6
```

## Coverage by family and route

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

## Branch-flag histogram

The attempt-level branch flags appearing in selected attempts are:

```text
CLEAN_DESCENT:          8
EXTERNAL_BRIDGE:        8
DISTRIBUTED_BRIDGE:     5
LONG_TERMINAL_BRIDGE:   5
RIGHT_TERMINAL_BRIDGE:  5
SIGNED_INTERVAL:        4
LEFT_TERMINAL_BRIDGE:   1
SHORT_TERMINAL_BRIDGE:  1
```

This confirms that the zero-sum branch routes through the expected closed mechanisms:

```text
CLEAN_DESCENT,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
SIGNED_INTERVAL,
terminal bridges.
```

## Notable witness patterns

### CLEAN_DESCENT

Example rows include direct defect improvement:

```text
B_tail+q+Y_prefix, p=17, record 0:
  hidden_equation = B3 q Y1
  branch_flags = [CLEAN_DESCENT]
  old_defect = [3,3,2,[3,2]]
  new_defect = [2,4,1,[2,2]]
```

```text
B_tail+q, p=17, record 62:
  hidden_equation = B2 B3 q
  branch_flags = [CLEAN_DESCENT]
  old_defect = [2,3,2,[3]]
  new_defect = [1,3,1,[2]]
```

### EXTERNAL_BRIDGE

Examples show explicit external route flags:

```text
B_tail+q, p=17, record 24:
  hidden_equation = B3 B4 q
  branch_flags = [EXTERNAL_BRIDGE]
  old_defect = [2,3,2,[2,2]]
  new_defect = [2,3,2,[2,2]]
```

```text
B_tail+q+Y_prefix, p=23, record 31:
  hidden_equation = B3 B4 B5 B6 q Y1
  branch_flags = [EXTERNAL_BRIDGE]
  old_defect = [2,3,1,[2,2]]
  new_defect = [2,6,1,[2,2]]
```

### DISTRIBUTED_BRIDGE

Examples show distributed route flags:

```text
B_tail+q, p=17, record 338:
  hidden_equation = B2 B3 q
  branch_flags = [DISTRIBUTED_BRIDGE]
  old_defect = [2,3,2,[2,2]]
  new_defect = [3,2,1,[2,2,2]]
```

```text
B_tail+q+Y_prefix, p=17, record 666:
  hidden_equation = B2 B3 B4 q Y1
  branch_flags = [DISTRIBUTED_BRIDGE]
  old_defect = [2,3,1,[3]]
  new_defect = [3,2,1,[2,2,2]]
```

### MIXED

Mixed examples contain simultaneous closed route flags.  For formal proof purposes, any one closed flag can be selected as the exit.

Example:

```text
B_tail+q+Y_prefix, p=17, record 247:
  hidden_equation = B2 B3 q Y1
  branch_flags = [CLEAN_DESCENT, SIGNED_INTERVAL, EXTERNAL_BRIDGE]
  old_defect = [2,3,1,[3]]
  new_defect = [2,2,1,[3]]
```

## One unmatched attempt row

There is one row where:

```text
matched_route_object = true
matched_attempt = false
```

The row is:

```text
family = B_tail+q
route_label = DISTRIBUTED_BRIDGE
p = 23
record_index = 183
reduced_equation = B2 B3 q
hidden_equation = B2 B3 q
selected branch_flags = [RIGHT_TERMINAL_BRIDGE, LONG_TERMINAL_BRIDGE]
```

This likely means that the detailed route object contains `DISTRIBUTED_BRIDGE` in aggregate counts, but the truncated `attempts_first5` sample does not include the distributed attempt.  The route object is still matched, but the selected attempt is not.

## Proof interpretation

At the attempt level, the zero-sum branch now has explicit representatives for:

```text
CLEAN_DESCENT,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
MIXED.
```

The symbolic route lemma can use the following interpretation:

```text
Bq_zero or BqY_zero produces a repeated partial-sum relation.
That relation triggers one of the closed branch flags.
If CLEAN_DESCENT occurs, the defect descends directly.
If EXTERNAL_BRIDGE occurs, the partial sum links active and exterior zones.
If DISTRIBUTED_BRIDGE occurs, the repeated-sum obstruction is distributed across route components.
If MIXED occurs, at least one closed route flag is available.
```

## Status

```text
Attempt-level zero-sum witnesses extracted.
23/24 rows have exact route-label-matching attempts.
1/24 needs a diagnostic because the matching attempt may be outside attempts_first5.
```
