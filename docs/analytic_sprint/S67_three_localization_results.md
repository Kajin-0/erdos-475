# S67. Three-localization equality results

This note records the output of:

```text
scripts/test_equality_three_localizations.py
```

using:

```text
logs/equality_three_localizations_p17.jsonl
logs/equality_three_localizations_p23.jsonl
logs/summary_equality_three_localizations_p17.json
logs/summary_equality_three_localizations_p23.json
```

## Main result

The finite equality-localization alternative is empirically closed.

For every equality hidden-support record, at least one of the three symbolic localizations is `D_short`-neutral and has

```text
q_tail_span_gap = 0.
```

The three tested localizations were:

```text
old: A z q P T M

L1:  A z P q T M
L2:  A z q T P M
L3:  A z T q P M
```

where

```text
B = P T M,
T = extracted B_tail.
```

## p=17 result

Records:

```text
B_tail+q=A_complement: 4
```

Coverage:

```text
has_neutral_zero_gap_by_family:
  B_tail+q=A_complement: yes 4 / 4
```

Candidate class histogram:

```text
P_q_T_M: neutral 3, worse 1
T_q_P_M: neutral 1, worse 3
q_T_P_M: neutral 1, worse 3
```

Neutral zero-gap candidates:

```text
P_q_T_M: 3
T_q_P_M: 1
q_T_P_M: 1
```

The count exceeds 4 because one record has multiple neutral zero-gap localizations.

## p=23 result

Records:

```text
B_tail+q=A_complement: 5
B_prefix=q:            2
```

Coverage:

```text
has_neutral_zero_gap_by_family:
  B_tail+q=A_complement: yes 5 / 5
  B_prefix=q:            yes 2 / 2
```

Candidate class histogram:

```text
B_tail+q=A_complement:
  P_q_T_M: neutral 4, worse 1
  T_q_P_M: neutral 2, worse 3
  q_T_P_M: neutral 2, worse 3

B_prefix=q:
  P_q_T_M: neutral 2
  T_q_P_M: worse 2
  q_T_P_M: worse 2
```

Neutral zero-gap candidates:

```text
B_tail+q=A_complement:
  P_q_T_M: 4
  T_q_P_M: 2
  q_T_P_M: 2

B_prefix=q:
  P_q_T_M: 2
```

## Interpretation

The strongest uniform observation is:

```text
P_q_T_M is neutral in 3/4 p=17 equality records and 6/7 p=23 equality records.
```

However, one p=17 record requires a different localization.  Therefore the proof should not claim that `P q T M` is always neutral.

The correct finite alternative is:

```text
Among P q T M, q T P M, and T q P M, at least one is D_short-neutral and has q_tail_span_gap = 0.
```

This statement has full empirical coverage:

```text
p=17: 4 / 4
p=23: 7 / 7
```

## Equality localization lemma, final empirical form

```text
Lemma: Three-localization equality tie-break.
Let R be an equality hidden-support residual.  Write B = P T M, where T is the extracted B_tail.  Then among the localizations

  A z P q T M,
  A z q T P M,
  A z T q P M,

at least one preserves D_short and makes {q} union T contiguous.  Therefore S_tail drops to zero.
```

## Consequence

Combining this with S65:

```text
S_tail(old) = span_gap({q} union T) = |P| > 0,
S_tail(new) = 0,
D_short(new) = D_short(old).
```

Thus

```text
D_ref(new) < D_ref(old),
D_ref = (D_short, S_tail).
```

## Remaining formal burden

The only remaining equality-branch proof obligation is now the finite alternative itself:

```text
Prove that at least one of P_q_T_M, q_T_P_M, T_q_P_M is D_short-neutral under the equality hidden-support hypotheses.
```

This can likely be attacked by comparing the zero-interval defects of the three candidate orders.  Since all candidates make `{q} union T` contiguous, the only issue is avoiding a worse `D_short` collision.

## Status

```text
Equality branch empirically closed by explicit three-localization finite alternative.
Next proof target: derive symbolic conditions under which each of the three localizations is worse, and show they cannot all be worse simultaneously.
```
