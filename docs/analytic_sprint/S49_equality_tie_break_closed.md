# S49. Equality tie-break closure status

This note records the output of:

```text
scripts/test_equality_tie_break_ranks.py
```

using:

```text
logs/equality_tie_break_ranks_p17.jsonl
logs/equality_tie_break_ranks_p23.jsonl
logs/summary_equality_tie_break_ranks_p17.json
logs/summary_equality_tie_break_ranks_p23.json
```

## Result

The equality branch is empirically closed by the support-localization tie-break:

```text
q_tail_span_gap
```

and equivalently by:

```text
q_tail_span_width
```

for every equality record in the current certificate.

## p=17

Records:

```text
B_tail+q=A_complement: 4
```

Tie-break improvement:

```text
has_improve_by_family:
  B_tail+q=A_complement: yes 4 / 4
```

Improving ranks:

```text
q_tail_span_gap        4 / 4
q_tail_span_width      4 / 4
q_tail_comp_span_gap   2 / 4
q_tail_comp_span_width 2 / 4
```

Thus the simplest universal rank for p=17 is:

```text
q_tail_span_gap
```

## p=23

Records:

```text
B_tail+q=A_complement: 5
B_prefix=q:            2
```

Tie-break improvement:

```text
has_improve_by_family:
  B_tail+q=A_complement: yes 5 / 5
  B_prefix=q:            yes 2 / 2
```

Improving ranks:

```text
B_tail+q=A_complement:
  q_tail_span_gap        5 / 5
  q_tail_span_width      5 / 5
  q_tail_comp_span_gap   2 / 5
  q_tail_comp_span_width 2 / 5

B_prefix=q:
  q_tail_span_gap        2 / 2
  q_tail_span_width      2 / 2
  q_tail_comp_span_gap   2 / 2
  q_tail_comp_span_width 2 / 2
```

Again, the simplest universal rank is:

```text
q_tail_span_gap
```

## Interpretation

The equality branch does not need a new collision/routing lemma.  It is neutral with respect to `D_short`, but it decreases a support-localization rank.

Define:

```text
S_tail(R) = span_gap(q, B_tail)
```

where:

```text
span_gap(U) = max_position(U) - min_position(U) + 1 - |U|.
```

Then the tested neutral equality moves satisfy:

```text
D_short(new) = D_short(old)
S_tail(new) < S_tail(old).
```

Observed coverage:

```text
p=17: 4 / 4
p=23: 7 / 7
```

## Refined defect proposal

For the pure worse-only terminal branch, use a refined defect of the form:

```text
D_ref = (D_short, S_tail)
```

or, more conservatively,

```text
D_ref = (D_short, T_pos, C_rank, S_tail),
```

where `S_tail` is sufficient for the observed equality branch.

## Formal lemma candidate

```text
Lemma: Equality hidden-support tie-break.
Let R = X A z q B Y be a pure worse-only m=3 right-terminal residual.  Suppose the B z q A hidden-support extraction gives one of the equality forms

  B_tail + q = A_complement

or

  B_prefix = q.

Then there exists a D_short-neutral bridge move such that

  S_tail(new) < S_tail(old),

where S_tail is the span gap of q together with the extracted B_tail.
```

## Proof consequence

Together with the zero-sum routing result, the pure worse-only branch is now empirically closed:

```text
zero-sum families:
  target obstruction classified and routed through existing branch machinery.

equality families:
  D_short-neutral but S_tail-decreasing.
```

## Status

```text
Pure worse-only m=3 branch is now closed at the empirical-certificate level.
Remaining work: convert each empirical reduction into formal endpoint/partial-sum lemmas.
```
