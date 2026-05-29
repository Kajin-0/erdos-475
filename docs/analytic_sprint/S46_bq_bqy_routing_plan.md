# S46. Bq/BqY routing plan

The v2 certificate table reduced the pure worse-only branch to two classes:

```text
zero-sum branches:
  B_tail+q              -> Bq_zero
  B_tail+q+Y_prefix     -> BqY_zero

equality branches:
  B_tail+q=A_complement -> tie-break needed
  B_prefix=q            -> tie-break needed
```

The next target is the zero-sum routing lemma.

## Goal

Determine whether the secondary obstructions

```text
Bq_zero
BqY_zero
```

are already covered by the earlier branch classifier vocabulary:

```text
SIGNED_INTERVAL
DISTRIBUTED_BRIDGE
EXTERNAL_BRIDGE
RIGHT_TERMINAL_BRIDGE
LEFT_TERMINAL_BRIDGE
SHORT_TERMINAL_BRIDGE
LONG_TERMINAL_BRIDGE
```

The relevant classifier logic already exists in:

```text
scripts/test_external_bridge_overlap.py
```

It classifies q-insertion attempts around shortest zero intervals and emits:

```text
attempt_label_counts
attempt_flag_counts
```

## New diagnostic

Add:

```text
scripts/route_bq_bqy_obstructions.py
```

Inputs:

```text
logs/hidden_support_bridge_moves_p17_v5.jsonl
logs/hidden_support_bridge_moves_p23_v5.jsonl
```

The script should:

```text
1. select records with reduced_family in:
   B_tail+q,
   B_tail+q+Y_prefix;

2. take each best bridge move order;

3. run the external-bridge classifier on the best move order;

4. summarize flags by original hidden-support family;

5. report whether every Bq/BqY obstruction has at least one route flag among:
   SIGNED_INTERVAL,
   DISTRIBUTED_BRIDGE,
   EXTERNAL_BRIDGE,
   terminal bridge flags.
```

## Desired outcome

The strongest outcome would be:

```text
B_tail+q:
  all records route to SIGNED_INTERVAL or terminal/support-tail bridge.

B_tail+q+Y_prefix:
  all records route to EXTERNAL_BRIDGE or DISTRIBUTED_BRIDGE.
```

If not, the residual unclassified cases become a precise new branch lemma.

## Status

```text
Proceeding from proof skeleton to route-classifier diagnostic.
```
