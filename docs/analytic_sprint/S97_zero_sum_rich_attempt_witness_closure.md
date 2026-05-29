# S97. Zero-sum rich attempt witness closure

This note records the successful rich-attempt rerun after adding:

```text
scripts/route_bq_bqy_obstructions_with_attempts.py
```

and patching:

```text
scripts/extract_zero_sum_attempt_witnesses.py
```

to consume:

```text
attempts_by_label,
attempts_by_flag.
```

## Motivation

S95-S96 found that the zero-sum branch had complete route-level coverage, but one route-label-specific attempt was missing from the selected attempt sample:

```text
matched_route_object_rows = 24
matched_attempt_rows = 23
```

The unmatched row was:

```text
family = B_tail+q
target = Bq_zero
route_label = DISTRIBUTED_BRIDGE
p = 23
record_index = 183
hidden_equation = B2 B3 q
```

S96 diagnosed this as a truncation issue:

```text
DISTRIBUTED_BRIDGE existed in attempt_label_counts,
but not in attempts_first5.
```

## Fix

The rich route producer now emits per-label and per-flag attempt samples:

```text
attempts_by_label,
attempts_by_flag,
attempts_first10,
attempts_total.
```

The attempt witness extractor now prefers:

```text
attempts_by_label[route_label]
attempts_by_flag[route_label]
```

before falling back to flattened truncated attempts.

## Rich route rerun

The rich producer was run on:

```text
logs/hidden_support_bridge_moves_p17_v5.jsonl
logs/hidden_support_bridge_moves_p23_v5.jsonl
```

Output:

```text
logs/route_bq_bqy_obstructions_p17_with_attempts.jsonl
logs/summary_route_bq_bqy_obstructions_p17_with_attempts.json
logs/route_bq_bqy_obstructions_p23_with_attempts.jsonl
logs/summary_route_bq_bqy_obstructions_p23_with_attempts.json
```

## Route-level summary remains complete

### p = 17

```text
records = 31
records_by_family:
  B_tail+q:          23
  B_tail+q+Y_prefix: 8

route_success_by_family:
  B_tail+q:          yes 23
  B_tail+q+Y_prefix: yes 8
```

Route labels:

```text
B_tail+q:
  CLEAN_DESCENT:       182
  DISTRIBUTED_BRIDGE:  1
  EXTERNAL_BRIDGE:     6
  MIXED:               125

B_tail+q+Y_prefix:
  CLEAN_DESCENT:       92
  DISTRIBUTED_BRIDGE:  2
  MIXED:               54
```

### p = 23

```text
records = 52
records_by_family:
  B_tail+q:          20
  B_tail+q+Y_prefix: 32

route_success_by_family:
  B_tail+q:          yes 20
  B_tail+q+Y_prefix: yes 32
```

Route labels:

```text
B_tail+q:
  CLEAN_DESCENT:       103
  DISTRIBUTED_BRIDGE:  3
  EXTERNAL_BRIDGE:     12
  MIXED:               92

B_tail+q+Y_prefix:
  CLEAN_DESCENT:       487
  DISTRIBUTED_BRIDGE:  12
  EXTERNAL_BRIDGE:     32
  MIXED:               305
```

## Rich example extraction

The rich route files were then passed through:

```text
scripts/extract_zero_sum_route_examples.py
```

Output:

```text
logs/zero_sum_route_examples_with_attempts.jsonl
logs/summary_zero_sum_route_examples_with_attempts.json
```

Summary:

```text
examples_found = 24
missing_route_jsonl_files = []
unmatched_route_rows = 0
```

Balanced by family:

```text
B_tail+q:          12
B_tail+q+Y_prefix: 12
```

Balanced by route label:

```text
CLEAN_DESCENT:       6
DISTRIBUTED_BRIDGE:  6
EXTERNAL_BRIDGE:     6
MIXED:               6
```

Balanced by family-route pair:

```text
B_tail+q::CLEAN_DESCENT:                    3
B_tail+q::DISTRIBUTED_BRIDGE:               3
B_tail+q::EXTERNAL_BRIDGE:                  3
B_tail+q::MIXED:                            3
B_tail+q+Y_prefix::CLEAN_DESCENT:           3
B_tail+q+Y_prefix::DISTRIBUTED_BRIDGE:      3
B_tail+q+Y_prefix::EXTERNAL_BRIDGE:         3
B_tail+q+Y_prefix::MIXED:                   3
```

## Rich attempt-witness extraction

The rich examples were then passed through:

```text
scripts/extract_zero_sum_attempt_witnesses.py
```

Output:

```text
logs/zero_sum_attempt_witnesses_with_attempts.jsonl
logs/summary_zero_sum_attempt_witnesses_with_attempts.json
```

Main result:

```text
rows = 24
matched_route_object_rows = 24
matched_attempt_rows = 24
```

The earlier gap is closed.

## Attempt-level route coverage

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

By family-route pair:

```text
B_tail+q::CLEAN_DESCENT:                    3
B_tail+q::DISTRIBUTED_BRIDGE:               3
B_tail+q::EXTERNAL_BRIDGE:                  3
B_tail+q::MIXED:                            3
B_tail+q+Y_prefix::CLEAN_DESCENT:           3
B_tail+q+Y_prefix::DISTRIBUTED_BRIDGE:      3
B_tail+q+Y_prefix::EXTERNAL_BRIDGE:         3
B_tail+q+Y_prefix::MIXED:                   3
```

## Branch-flag histogram

The selected matched attempts contain:

```text
CLEAN_DESCENT:       8
DISTRIBUTED_BRIDGE:  6
EXTERNAL_BRIDGE:     8
SIGNED_INTERVAL:     3
LONG_TERMINAL_BRIDGE: 4
RIGHT_TERMINAL_BRIDGE: 4
LEFT_TERMINAL_BRIDGE: 1
SHORT_TERMINAL_BRIDGE: 1
```

This gives explicit attempt-level witnesses for all route labels needed by the zero-sum routing lemma.

## Final zero-sum branch status

The zero-sum branch now has three layers of complete evidence:

```text
Record-level route coverage:
  83/83 routed.

Representative route examples:
  24/24 extracted.

Attempt-level witnesses:
  24/24 matched.
```

Thus:

```text
Bq_zero and BqY_zero are not primitive obstructions.
```

Every zero-sum hidden-support record triggers at least one closed route mechanism:

```text
CLEAN_DESCENT,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
SIGNED_INTERVAL,
terminal bridge.
```

## Role in the pure worse-only theorem

Together with S85, all four hidden-support families are now covered:

```text
B_tail + q = 0                  -> zero_sum_routed
B_tail + q + Y_prefix = 0       -> zero_sum_routed
B_tail + q = A_complement       -> equality_tiebroken
B_prefix = q                    -> equality_tiebroken
```

The zero-sum branch is closed at the empirical-symbolic level with explicit attempt witnesses.

## Remaining publication-grade proof obligation

The remaining formal work is to replace these certificate-backed route labels with symbolic implications:

```text
Bq_zero  -> CLEAN_DESCENT or SIGNED/DISTRIBUTED/EXTERNAL/terminal route,
BqY_zero -> CLEAN_DESCENT or SIGNED/DISTRIBUTED/EXTERNAL/terminal route.
```

The rich attempt witnesses provide the concrete cases needed to write that symbolic classifier.

## Status

```text
Zero-sum rich attempt witness closure complete.
No remaining attempt-witness gap.
Next: assemble the corrected pure worse-only hidden-support branch theorem using S85 and S97.
```
