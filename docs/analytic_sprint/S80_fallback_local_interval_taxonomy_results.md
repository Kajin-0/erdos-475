# S80. Fallback local interval taxonomy results

This note records the successful rerun of:

```text
scripts/taxonomize_fallback_local_intervals.py
```

using:

```text
logs/fallback_local_interval_taxonomy.jsonl
logs/summary_fallback_local_interval_taxonomy.json
```

## Main result

The fallback localization creates no new shortest blocks in the primary-failure rows.

```text
primary_failure_rows = 2
record_indices = [739, 716]
fallback_new_short_total = 0
fallback_new_short_symbols = {}
fallback_new_zone_histogram = {}
```

The fallback defect profile is exactly the old profile in both rows:

```text
fallback_defect_counts:
  [1, 3, 1, (2,)] : 2
```

Thus the fallback order is `D_short`-neutral in every primary-failure row.

## Fallback zero interval taxonomy

The fallback zero interval histogram is:

```text
fallback_zone_histogram:
  A+z : 2
```

This means the only fallback zero interval class detected is the old terminal triple relation:

```text
A1 + A2 + z = 0.
```

No new fallback local interval appears in the zones:

```text
q | T | P | M.
```

## Primary failure rows

The primary-failure rows are:

```text
p=17, record_index=739
p=23, record_index=716
```

Both are in the equality family:

```text
B_tail+q=A_complement
```

In both rows, the primary localization creates a new short block of type:

```text
P + q
```

but the fallback creates none.

### p=17 record 739

```text
reduced_equation = B4 B5 q = A2
old_defect       = [1,3,1,[2]]
primary_defect   = [2,2,1,[2,2]]
fallback_defect  = [1,3,1,[2]]
```

Primary new short block:

```text
B3 q
zone_class = P+q
```

Fallback new short blocks:

```text
none
```

### p=23 record 716

```text
reduced_equation = B5 q = A2
old_defect       = [1,3,1,[2]]
primary_defect   = [2,3,2,[2,2]]
fallback_defect  = [1,3,1,[2]]
```

Primary new short block:

```text
B3 B4 q
zone_class = P+q
```

Fallback new short blocks:

```text
none
```

## Interpretation

The fallback mechanism is now sharply characterized:

```text
Primary P q T M fails by creating a P+q short block.
Fallback q T P M creates no new shortest blocks and preserves D_short.
```

This differs slightly from the earlier guess that the primary failure had form `T_prefix+q`.  The corrected taxonomy says the primary failure is:

```text
P_suffix + q = 0
```

where `P_suffix` is a suffix of the support prefix block `P` immediately preceding `q` after the primary localization.

The fallback moves `T` immediately after `q`, so the problematic `P+q` adjacency disappears.

## Updated symbolic fallback mechanism

The correct local statement is:

```text
old:      q P T M
primary:  P q T M
fallback: q T P M
```

Primary can fail because moving `P` before `q` creates a new short relation:

```text
P_suffix + q = 0.
```

Fallback avoids this by placing `T` between `q` and `P`:

```text
q T P M.
```

The fallback taxonomy confirms that this introduces no new shortest intervals.

## Consequence for the equality tie-break proof

The equality fallback implication can now be stated more accurately:

```text
If P q T M is worse, then it is worse because of a new P_suffix+q shortest block.  The fallback q T P M removes that adjacency, creates no new shortest block, and is D_short-neutral.
```

Together with the span-gap calculation:

```text
S_tail(q T P M)=0<S_tail(q P T M old),
```

this closes the equality tie-break at the empirical-symbolic level.

## Remaining formal proof obligation

A publication-grade proof still needs to show symbolically that:

```text
P q T M worse -> only possible primary-new shortest block is P_suffix+q,
q T P M creates no new shortest block.
```

But the local taxonomy has reduced this to a small endpoint statement over:

```text
q | P | T | M
```

and its fallback:

```text
q | T | P | M.
```

## Status

```text
Fallback local interval taxonomy closed.
Condition B from S78 is verified in the certified rows.
The primary-failure mechanism is corrected to P_suffix+q, not T_prefix+q.
```
