# S96. Unmatched zero-sum attempt diagnostic

This note records the output of:

```text
scripts/diagnose_unmatched_zero_sum_attempts.py
```

using:

```text
logs/unmatched_zero_sum_attempts.jsonl
logs/summary_unmatched_zero_sum_attempts.json
```

## Main result

There is exactly one attempt-level unmatched row:

```text
unmatched_attempt_rows = 1
record_indices = [183]
route_labels = [DISTRIBUTED_BRIDGE]
```

The row is:

```text
family = B_tail+q
target = Bq_zero
route_label = DISTRIBUTED_BRIDGE
p = 23
record_index = 183
reduced_equation = B2 B3 q
hidden_equation = B2 B3 q
```

## Important interpretation

This is not a route-coverage failure.

The route object is matched:

```text
matched_route_object = true
label_present_in_route_compact = true
```

The route object contains the aggregate counts:

```text
attempt_label_counts:
  MIXED: 5
  CLEAN_DESCENT: 2
  DISTRIBUTED_BRIDGE: 1

attempt_flag_counts:
  RIGHT_TERMINAL_BRIDGE: 4
  LONG_TERMINAL_BRIDGE: 4
  CLEAN_DESCENT: 4
  DISTRIBUTED_BRIDGE: 1
  LEFT_TERMINAL_BRIDGE: 1
  SHORT_TERMINAL_BRIDGE: 1
```

Thus the detailed route object confirms that a `DISTRIBUTED_BRIDGE` attempt exists.

The mismatch is only at the selected-attempt level:

```text
matched_attempt = false
label_present_in_attempt_compact = false
```

The selected attempt was the first available attempt from `attempts_first5`, with flags:

```text
RIGHT_TERMINAL_BRIDGE,
LONG_TERMINAL_BRIDGE
```

and label:

```text
MIXED
```

Therefore, the missing `DISTRIBUTED_BRIDGE` attempt is likely outside the truncated `attempts_first5` sample.

## Diagnostic row summary

The selected attempt was:

```text
branch_flags = [RIGHT_TERMINAL_BRIDGE, LONG_TERMINAL_BRIDGE]
bridge_indices = [2]
external value = 5
old_defect = [2,3,2,[3]]
new_defect = [2,4,1,[2,2]]
label = MIXED
```

The selected route object reports:

```text
active_shortest_length = 3
attempt_label_counts = {CLEAN_DESCENT:2, DISTRIBUTED_BRIDGE:1, MIXED:5}
attempt_flag_counts = {CLEAN_DESCENT:4, DISTRIBUTED_BRIDGE:1, LEFT_TERMINAL_BRIDGE:1, LONG_TERMINAL_BRIDGE:4, RIGHT_TERMINAL_BRIDGE:4, SHORT_TERMINAL_BRIDGE:1}
```

## Consequence

The attempt-level witness extraction status is:

```text
24/24 route objects matched
23/24 route-label-specific attempts matched in attempts_first5
1/24 label exists in aggregate route counts but not in attempts_first5
```

This should be treated as a truncation/sampling issue, not a mathematical gap.

## Recommended fix

Patch the detailed route producer:

```text
scripts/route_bq_bqy_obstructions.py
```

so it emits one or more of:

```text
matching_attempts_by_label,
first_attempt_by_label,
attempts_by_label,
all_attempts,
```

instead of only:

```text
attempts_first5.
```

Then rerun:

```text
scripts/route_bq_bqy_obstructions.py
scripts/extract_zero_sum_route_examples.py
scripts/extract_zero_sum_attempt_witnesses.py
```

and verify:

```text
matched_attempt_rows = 24
```

## Status

```text
Unmatched attempt diagnosed.
Route-level coverage remains intact.
Next: patch route_bq_bqy_obstructions.py to emit per-label matching attempts.
```
