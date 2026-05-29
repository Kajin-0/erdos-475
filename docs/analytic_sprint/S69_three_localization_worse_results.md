# S69. Three-localization worse-condition results

This note records the output of:

```text
scripts/diagnose_three_localization_worse_conditions.py
```

using:

```text
logs/summary_three_localization_worse_conditions_p17.json
logs/summary_three_localization_worse_conditions_p23.json
```

## Main result

No equality record has all three localization candidates worse.

```text
p=17: all_three_worse = no 4 / 4
p=23: all_three_worse = no 7 / 7
```

Thus the finite alternative remains fully supported:

```text
Among P_q_T_M, q_T_P_M, and T_q_P_M, at least one is D_short-neutral.
```

## Stronger observed fallback rule

The data suggests a sharper two-step rule:

```text
Try P_q_T_M first.
If P_q_T_M is worse, then q_T_P_M is neutral.
```

Evidence:

### p=17

The worse combo involving `P_q_T_M` is:

```text
P_q_T_M|T_q_P_M: 1
```

The corresponding neutral combo is:

```text
q_T_P_M: 1
```

So the only p=17 case where `P_q_T_M` is worse is rescued by `q_T_P_M`.

### p=23

The worse combo involving `P_q_T_M` is:

```text
P_q_T_M: 1
```

The corresponding neutral combo is:

```text
q_T_P_M|T_q_P_M: 1
```

So the only p=23 case where `P_q_T_M` is worse is also rescued by `q_T_P_M`.

## Candidate behavior by family

### p=17: B_tail+q=A_complement

```text
records = 4
all_three_worse = no 4/4
```

Neutral combinations:

```text
P_q_T_M:             2
P_q_T_M|T_q_P_M:     1
q_T_P_M:             1
```

Worse combinations:

```text
P_q_T_M|T_q_P_M:     1
q_T_P_M:             1
q_T_P_M|T_q_P_M:     2
```

New shortest blocks causing worse candidates:

```text
P_q_T_M:
  B3 q: 1

T_q_P_M:
  B5 q B1: 1
  z B2:    1
  z B4:    1

q_T_P_M:
  B3 B4 B1: 1
  B4 B1:    1
```

### p=23: B_tail+q=A_complement

```text
records = 5
all_three_worse = no 5/5
```

Neutral combinations:

```text
P_q_T_M:                 3
P_q_T_M|q_T_P_M|T_q_P_M: 1
q_T_P_M|T_q_P_M:         1
```

Worse combinations:

```text
P_q_T_M:                 1
none:                    1
q_T_P_M|T_q_P_M:         3
```

New shortest blocks causing worse candidates:

```text
P_q_T_M:
  B3 B4 q: 1

T_q_P_M:
  B5 B6 Y1: 1
  z B4:     1

q_T_P_M:
  B5 B6 Y1: 1
```

### p=23: B_prefix=q

```text
records = 2
all_three_worse = no 2/2
```

Neutral combinations:

```text
P_q_T_M: 2
```

Worse combinations:

```text
q_T_P_M|T_q_P_M: 2
```

New shortest blocks causing worse candidates:

```text
T_q_P_M:
  z B8 q: 1

q_T_P_M:
  z q B8: 1
```

## Proof interpretation

The current equality proof can be organized as a fallback proof:

```text
1. Test L1 = P_q_T_M.
2. If L1 is neutral, done.
3. If L1 is worse, the observed obstruction has form B_tail-prefix + q.
4. In all observed L1-worse cases, L2 = q_T_P_M is neutral.
```

This is stronger than the symmetric finite-alternative statement and may be easier to prove.

## Candidate symbolic implication

The observed implication is:

```text
P_q_T_M worse -> q_T_P_M neutral.
```

A possible proof route:

```text
P_q_T_M worse
  -> a short zero interval is created by moving P before q
  -> that zero interval necessarily involves q with an initial segment of T
  -> moving T immediately after q absorbs/localizes that relation rather than creating an extra shortest collision
  -> q_T_P_M is neutral.
```

## Status

```text
No all-three-worse record observed.
A stronger fallback rule is suggested: P_q_T_M worse implies q_T_P_M neutral.
Next: verify this implication directly and extract the P-failure cases.
```
