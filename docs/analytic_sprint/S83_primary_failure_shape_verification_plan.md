# S83. Primary failure shape verification plan

S80-S82 corrected the equality fallback mechanism.

The primary localization failure is not

```text
T_prefix + q = 0.
```

It is

```text
P_suffix + q = 0.
```

where `P_suffix` is a nonempty suffix of the support-prefix block `P` immediately before `q` in the primary order

```text
primary: P | q | T | M.
```

## Goal

Add a small verifier that checks the primary-failure shape directly.

For every equality row where

```text
P_q_T_M is D_short-worse,
```

verify that every primary-new shortest block has zone class

```text
P+q
```

and symbolic form

```text
P_suffix q.
```

## New diagnostic

Add:

```text
scripts/verify_primary_failure_shape.py
```

Inputs:

```text
logs/fallback_local_interval_taxonomy.jsonl
```

The script should report:

```text
primary_failure_rows,
rows_with_only_Pq_new_short,
rows_with_non_Pq_new_short,
failure rows,
zone-class histogram,
symbolic-block histogram.
```

## Desired output

```text
primary_failure_rows = 2
rows_with_only_Pq_new_short = 2
rows_with_non_Pq_new_short = 0
```

with:

```text
zone_class_histogram = {P+q: 2}
symbolic_block_histogram = {B3 q: 1, B3 B4 q: 1}
```

## Proof use

Together with S80, this gives both local conditions in S78:

```text
A. Primary worsening implies only P_suffix+q new shortest blocks.
B. Fallback q T P M creates no new shortest blocks.
```

Then the corrected equality fallback proof is:

```text
primary worse -> P_suffix+q obstruction
fallback removes P|q adjacency
fallback creates no new shortest block
fallback is D_short-neutral
fallback makes {q} union T contiguous
D_ref descends
```

## Status

```text
Next: add the verifier for primary-failure shape.
```
