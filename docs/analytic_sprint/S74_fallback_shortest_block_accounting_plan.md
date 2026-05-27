# S74. Fallback shortest-block accounting plan

S73 isolated the remaining equality proof core:

```text
P_q_T_M worse -> q_T_P_M neutral.
```

The fallback verifier confirmed this implication with zero failures in the current certificate.

## Goal

Inspect only the primary-failure rows and compare shortest-block accounting:

```text
old order,
primary localization P_q_T_M,
fallback localization q_T_P_M.
```

We want to see exactly why the primary candidate is worse and why the fallback candidate remains neutral.

## New diagnostic

Add:

```text
scripts/inspect_fallback_shortest_accounting.py
```

Input:

```text
logs/three_localization_worse_conditions_p17.jsonl
logs/three_localization_worse_conditions_p23.jsonl
```

The script should filter rows satisfying:

```text
P_q_T_M is worse.
```

For each such row, print:

```text
p,
record_index,
family,
reduced_equation,
old_defect,
old_active_symbolic,
old_shortest_blocks,
primary_defect,
primary_new_short_blocks,
fallback_defect,
fallback_new_short_blocks,
fallback_class.
```

## Desired proof-facing result

The ideal summary is:

```text
primary failure rows = 2
fallback neutral rows = 2
fallback new shortest blocks = none or already accounted-compatible
```

If fallback has new shortest blocks, we need to classify them as transported/compatible with the old defect count.

## Proof use

This diagnostic supports the final symbolic fallback proof:

```text
Primary failure creates a q + T_prefix zero block.
Fallback q_T_P_M does not increase D_short; its shortest-block profile matches the old defect.
```

## Status

```text
Next: inspect primary-failure rows at the shortest-block level.
```
