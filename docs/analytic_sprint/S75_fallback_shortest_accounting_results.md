# S75. Fallback shortest-block accounting results

This note records the output of:

```text
scripts/inspect_fallback_shortest_accounting.py
```

using:

```text
logs/fallback_shortest_accounting.jsonl
logs/summary_fallback_shortest_accounting.json
```

## Main result

There are exactly two primary-failure rows, and in both rows the fallback localization is `D_short`-neutral and introduces no new shortest blocks.

```text
primary_failure_rows = 2
fallback_class_counts = {neutral: 2}
fallback_new_short_presence = {no: 2}
fallback_new_short_symbols = {}
```

The primary-failure rows are:

```text
record_indices = [739, 716]
```

Both are in the same equality family:

```text
B_tail+q=A_complement
```

Family-level accounting:

```text
B_tail+q=A_complement:
  primary_failure_rows = 2
  fallback_neutral = 2
  fallback_no_new_short = 2
```

## Primary failure mechanism

The primary localization is:

```text
P_q_T_M
```

The new shortest blocks causing primary failure are:

```text
p=17 record 739:
  B3 q

p=23 record 716:
  B3 B4 q
```

Summary:

```text
primary_new_short_symbols:
  B3 q:     1
  B3 B4 q: 1
```

Both are of the same symbolic type:

```text
T_prefix + q = 0
```

where `T_prefix` is an initial segment of the extracted support tail `T`.

## Record 739, p=17

Family:

```text
B_tail+q=A_complement
```

Reduced equation:

```text
B4 B5 q = A2
```

Defects:

```text
old_defect      = [1,3,1,[2]]
primary_defect  = [2,2,1,[2,2]]
fallback_defect = [1,3,1,[2]]
```

Primary new shortest block:

```text
B3 q
```

Fallback new shortest blocks:

```text
none
```

Thus the fallback exactly restores the original `D_short` profile.

## Record 716, p=23

Family:

```text
B_tail+q=A_complement
```

Reduced equation:

```text
B5 q = A2
```

Defects:

```text
old_defect      = [1,3,1,[2]]
primary_defect  = [2,3,2,[2,2]]
fallback_defect = [1,3,1,[2]]
```

Primary new shortest block:

```text
B3 B4 q
```

Fallback new shortest blocks:

```text
none
```

Again, the fallback exactly restores the original `D_short` profile.

## Interpretation

The fallback behavior is now very sharp:

```text
P_q_T_M worse
  -> primary creates a new short block T_prefix + q
  -> q_T_P_M introduces no new shortest block
  -> q_T_P_M is D_short-neutral
```

This supports the symbolic fallback lemma:

```text
If moving P before q creates a new shortest q+T_prefix collision, then moving T immediately after q avoids creating any new shortest interval and preserves D_short.
```

## Proof consequence

The equality tie-break proof can use the following deterministic rule:

```text
1. Try primary localization P_q_T_M.
2. If primary is neutral, done.
3. If primary is worse, fallback q_T_P_M is neutral and has no new shortest blocks.
```

In both successful cases, `{q} union T` is contiguous, so

```text
S_tail = 0.
```

## Status

```text
Fallback accounting closed empirically.
Next: draft the symbolic primary-failure fallback lemma.
```
