# S84. Primary failure shape verification results

This note records the output of:

```text
scripts/verify_primary_failure_shape.py
```

using:

```text
logs/primary_failure_shape.jsonl
logs/summary_primary_failure_shape.json
```

## Main result

The corrected primary-failure shape is verified with zero failures.

```text
primary_failure_rows = 2
rows_with_only_Pq_new_short = 2
rows_with_non_Pq_new_short = 0
failure_indices = []
```

The primary-failure record indices are:

```text
[739, 716]
```

The zone-class histogram is:

```text
P+q : 2
```

The symbolic-block histogram is:

```text
B3 q     : 1
B3 B4 q  : 1
```

## Interpretation

Every primary-failure row satisfies:

```text
primary-new shortest block has zone class P+q.
```

Thus the primary localization

```text
q P T M -> P q T M
```

fails only by creating a shortest zero interval of the form

```text
P_suffix + q = 0.
```

There are no primary-failure rows with a non-`P+q` new shortest block.

## Combined with fallback taxonomy

S80 verified the companion fallback condition:

```text
fallback_new_short_total = 0
fallback_new_short_symbols = {}
fallback_new_zone_histogram = {}
fallback_zone_histogram = {A+z: 2}
```

Together, S80 and S84 give the certified local fallback package:

```text
Primary P q T M failure:
  only P_suffix+q new shortest blocks.

Fallback q T P M:
  no new shortest blocks.
```

Therefore, in every certified primary-failure row,

```text
D_short(fallback) = D_short(old),
S_tail(fallback) = 0.
```

## Equality branch consequence

The equality branch now has a verified two-step rule:

```text
1. Try primary P q T M.
2. If primary is neutral, use it.
3. If primary is worse, it fails only by P_suffix+q.
4. Use fallback q T P M.
5. Fallback creates no new shortest block and is D_short-neutral.
```

Both successful routes make `{q} union T` contiguous, so

```text
S_tail = 0.
```

This gives strict descent in the refined defect

```text
D_ref = (D_short, S_tail).
```

## Corrected local lemma status

The empirical-symbolic equality closure is now:

```text
If P q T M is D_short-worse, then the only primary-new shortest block is P_suffix+q; q T P M removes the P|q adjacency and creates no new shortest interval.
```

This is the corrected local endpoint statement over:

```text
old:      q | P | T | M
primary:  P | q | T | M
fallback: q | T | P | M
```

## Remaining formal proof obligation

For a publication-grade proof, the remaining symbolic step is to prove generally that under the equality hidden-support hypotheses:

```text
P q T M worse -> primary-new shortest blocks are only P_suffix+q,
q T P M creates no new shortest block.
```

The current certificate verifies this in the observed equality primary-failure rows.

## Status

```text
Primary-failure shape verification closed.
Together with S80, the corrected equality fallback package is empirically complete.
```
