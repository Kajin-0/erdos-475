# S82. Corrected equality branch closure note

This note consolidates the corrected equality fallback mechanism after S80-S81.

## Correction summary

Earlier notes S73, S76, and S78 guessed that the primary localization failure had form

```text
T_prefix + q = 0.
```

The fallback local taxonomy in S80 corrected this.

The primary failure mechanism is:

```text
P_suffix + q = 0.
```

where `P_suffix` is a nonempty suffix of the support-prefix block `P`.

## Local orders

Write the support block as

```text
B = P T M,
```

where

```text
T = extracted B_tail.
```

The equality branch starts from local order

```text
old:      q P T M.
```

The primary localization is

```text
primary:  P q T M.
```

The fallback localization is

```text
fallback: q T P M.
```

Both primary and fallback make `{q} union T` contiguous, so both give

```text
S_tail = span_gap({q} union T) = 0.
```

The only question is whether `D_short` is preserved.

## Certified behavior

The fallback implication was verified with zero failures:

```text
P_q_T_M worse -> q_T_P_M neutral and q_tail_span_gap = 0.
```

The fallback accounting then sharpened the result:

```text
primary_failure_rows = 2
fallback_class_counts = {neutral: 2}
fallback_new_short_presence = {no: 2}
fallback_new_short_symbols = {}
```

The fallback local interval taxonomy confirmed:

```text
fallback_new_short_total = 0
fallback_new_short_symbols = {}
fallback_new_zone_histogram = {}
fallback_zone_histogram = {A+z: 2}
```

Thus, in both primary-failure rows, the only fallback zero interval class is the old terminal triple:

```text
A1 + A2 + z = 0.
```

## Primary-failure rows

The two primary-failure rows are:

```text
p=17, record 739
p=23, record 716
```

Both are in the family:

```text
B_tail+q=A_complement.
```

### p=17 record 739

```text
reduced_equation = B4 B5 q = A2
old_defect       = [1,3,1,[2]]
primary_defect   = [2,2,1,[2,2]]
fallback_defect  = [1,3,1,[2]]
```

Primary new shortest block:

```text
B3 q
zone_class = P+q
```

Fallback new shortest blocks:

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

Primary new shortest block:

```text
B3 B4 q
zone_class = P+q
```

Fallback new shortest blocks:

```text
none
```

## Corrected equality fallback lemma

### Lemma C2. Corrected fallback localization

Let `R` be an equality hidden-support residual with local support decomposition

```text
B = P T M,
```

where `T` is the extracted support tail.  Consider the primary and fallback localizations:

```text
primary:  q P T M -> P q T M,
fallback: q P T M -> q T P M.
```

If the primary localization is `D_short`-worse, then the certified failure mechanism is a new shortest interval of form

```text
P_suffix + q = 0.
```

The fallback localization removes the `P|q` adjacency, creates no new shortest interval, and satisfies

```text
D_short(fallback) = D_short(old).
```

Since fallback also makes `{q} union T` contiguous,

```text
S_tail(fallback) = 0 < S_tail(old).
```

Therefore

```text
D_ref(fallback) < D_ref(old),
D_ref = (D_short, S_tail).
```

## Proof-level interpretation

The equality branch can now be written as a deterministic two-step rule:

```text
1. Try primary P q T M.
2. If primary is D_short-neutral, use it.
3. If primary is D_short-worse, the obstruction is P_suffix+q.
4. Use fallback q T P M; it removes P|q and creates no new shortest interval.
```

In either successful case, `{q} union T` is contiguous, so

```text
S_tail = 0.
```

## Remaining formal proof obligation

The remaining symbolic proof obligation is now narrow and corrected:

```text
If P q T M is D_short-worse in the equality branch, then the only possible primary-new shortest block is P_suffix+q, and q T P M creates no new shortest block.
```

This is a local endpoint-combinatorics claim comparing:

```text
old:      q | P | T | M
primary:  P | q | T | M
fallback: q | T | P | M
```

## Supersession note

This note supersedes the earlier `T_prefix+q` hypothesis in S73, S76, and S78.  The correct primary-failure mechanism is `P_suffix+q`.

## Status

```text
Equality branch closure corrected and consolidated.
Next formal target: prove the local endpoint claim for P_suffix+q primary failure and no-new-short fallback.
```
