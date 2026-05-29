# S70. Fallback implication verification plan

S69 found a stronger empirical pattern inside the equality-localization branch.

The finite alternative is:

```text
Among P_q_T_M, q_T_P_M, and T_q_P_M, at least one is D_short-neutral.
```

But the observed data suggests a sharper fallback rule:

```text
P_q_T_M worse -> q_T_P_M neutral.
```

If this holds generally, the equality proof becomes simpler:

```text
1. Try P_q_T_M.
2. If neutral, done.
3. If worse, switch to q_T_P_M.
4. q_T_P_M is neutral and still has q_tail_span_gap = 0.
```

## Goal

Add a direct verifier for the implication:

```text
P_q_T_M worse => q_T_P_M neutral and q_tail_span_gap(q_T_P_M)=0.
```

## New diagnostic

Add:

```text
scripts/verify_equality_fallback_implication.py
```

Inputs:

```text
logs/equality_three_localizations_p17.jsonl
logs/equality_three_localizations_p23.jsonl
```

The script should report:

```text
records,
records_where_P_q_T_M_worse,
records_where_implication_holds,
records_where_implication_fails,
failure rows,
family-level counts.
```

## Desired output

```text
p=17:
  P_q_T_M worse records = 1
  implication failures = 0

p=23:
  P_q_T_M worse records = 1
  implication failures = 0
```

Combined:

```text
P_q_T_M worse -> q_T_P_M neutral zero-gap: 2 / 2
```

## Proof use

If verified, the equality localization lemma can be written as:

```text
Lemma: Equality fallback localization.
Let B=P T M.  If the localization P q T M is D_short-neutral, use it. Otherwise, the equality hypotheses force the alternative localization q T P M to be D_short-neutral. Both moves make q adjacent to T, so S_tail drops to zero.
```

## Status

```text
Next: verify fallback implication directly from three-localization rows.
```
