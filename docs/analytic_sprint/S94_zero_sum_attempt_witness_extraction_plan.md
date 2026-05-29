# S94. Zero-sum attempt-level witness extraction plan

S93 confirmed that the route witness table has balanced coverage:

```text
2 zero-sum families x 4 route labels x 3 examples = 24 rows.
```

The next step is to unpack the attempt-level data inside:

```text
witness.move_routes
```

so the symbolic zero-sum routing lemma can be written in terms of explicit moves, flags, intervals, and defect comparisons.

## Goal

For each row in:

```text
logs/zero_sum_route_examples.jsonl
```

extract a compact representative attempt matching the row's route label:

```text
CLEAN_DESCENT,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
MIXED.
```

Each output row should include:

```text
family,
target,
route_label,
p,
record_index,
reduced_equation,
hidden_equation,
active_symbolic_order,
selected_move_route_summary,
selected_attempt,
branch_flags,
bridge_interval,
bridge_sum or symbolic block if available,
old/new defect if available.
```

## New script

Add:

```text
scripts/extract_zero_sum_attempt_witnesses.py
```

Input:

```text
logs/zero_sum_route_examples.jsonl
```

Outputs:

```text
logs/zero_sum_attempt_witnesses.jsonl
logs/summary_zero_sum_attempt_witnesses.json
```

## Robustness requirements

The script should tolerate evolving schemas.  It should search common fields such as:

```text
move_routes,
attempts,
attempts_first5,
branch_flags,
bridge_interval,
bridge_sum,
symbolic_block,
old_defect,
new_defect,
attempt_label_counts,
attempt_flag_counts.
```

If no exact route-label attempt is found, it should still output the best available route object and mark:

```text
matched_attempt = false.
```

## Desired summary

```text
rows = 24
matched_attempt_rows >= useful threshold
by_route_label = {CLEAN_DESCENT:6, DISTRIBUTED_BRIDGE:6, EXTERNAL_BRIDGE:6, MIXED:6}
```

## Proof use

This output should enable four symbolic route cases:

```text
CLEAN_DESCENT:
  show a concrete attempted rearrangement with improved defect.

DISTRIBUTED_BRIDGE:
  show the distributed repeated-sum witness.

EXTERNAL_BRIDGE:
  show the active-to-exterior bridge interval.

MIXED:
  choose one closed route flag from the simultaneous branch flags.
```

## Status

```text
Zero-sum family-route examples are balanced.
Next: unpack attempt-level witnesses from move_routes.
```
