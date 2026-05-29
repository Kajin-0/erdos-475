# S71. Equality fallback implication results

This note records the output of:

```text
scripts/verify_equality_fallback_implication.py
```

using:

```text
logs/summary_equality_fallback_implication_p17.json
logs/summary_equality_fallback_implication_p23.json
logs/equality_fallback_implication_p17.jsonl
logs/equality_fallback_implication_p23.jsonl
```

## Main result

The sharpened fallback implication is verified in all certified equality records:

```text
P_q_T_M worse -> q_T_P_M neutral and q_tail_span_gap = 0.
```

There are no implication failures.

```text
p=17: implication_failures = 0
p=23: implication_failures = 0
```

## p=17 result

```text
records = 4
primary = P_q_T_M
fallback = q_T_P_M
primary_worse_records = 1
implication_holds_on_primary_worse = 1
implication_failures = 0
failure_indices = []
```

Family-level counts:

```text
B_tail+q=A_complement:
  records = 4
  primary_worse = 1
  fallback_rescues = 1
```

## p=23 result

```text
records = 7
primary = P_q_T_M
fallback = q_T_P_M
primary_worse_records = 1
implication_holds_on_primary_worse = 1
implication_failures = 0
failure_indices = []
```

Family-level counts:

```text
B_tail+q=A_complement:
  records = 5
  primary_worse = 1
  fallback_rescues = 1

B_prefix=q:
  records = 2
```

In the `B_prefix=q` family, the primary localization `P_q_T_M` is neutral in both records, so the fallback is not needed.

## Interpretation

The equality proof no longer needs the full three-way statement:

```text
Among P_q_T_M, q_T_P_M, and T_q_P_M, at least one is neutral.
```

Instead, it can use the sharper two-step rule:

```text
1. Try P_q_T_M.
2. If P_q_T_M is neutral, use it.
3. If P_q_T_M is worse, use q_T_P_M.
```

Both localizations make `{q} union T` contiguous.  Therefore either selected move has:

```text
q_tail_span_gap = 0.
```

## Proof-facing fallback lemma

```text
Lemma: Equality fallback localization.
Let R be an equality hidden-support residual and write B=P T M, where T is the extracted B_tail.  Consider the primary localization P q T M.  If it is D_short-neutral, then it gives the required refined descent.  If it is D_short-worse, then the fallback localization q T P M is D_short-neutral.  In both cases S_tail drops to zero.
```

## Status

```text
Fallback implication verified.
Equality branch can now be written as a two-step proof rather than a three-way finite alternative.
```
