# S48. Equality tie-break attack plan

The v3 pure worse certificate table closed the zero-sum branch:

```text
B_tail+q              -> Bq_zero  -> routed
B_tail+q+Y_prefix     -> BqY_zero -> routed
```

The only remaining pure worse-only branch is the equality branch:

```text
B_tail+q=A_complement
B_prefix=q
```

Observed certificate:

```text
p=17:
  B_tail+q=A_complement -> neutral 4/4

p=23:
  B_tail+q=A_complement -> neutral 5/5
  B_prefix=q            -> neutral 2/2
```

## Goal

Find a refined tie-break rank that decreases on the neutral equality moves while preserving `D_short`.

## Candidate ranks

### 1. Terminal position rank

For a right-terminal residual, prefer rightward motion of the unique length-3 zero triple.

Equivalent ranks:

```text
T_right = n - j
T_center = -(i+j)
```

where `[i,j)` is the distinguished length-3 zero interval.  Smaller `T_right` or smaller `T_center` is better.

### 2. Cyclic triple rank

The old terminal triple is:

```text
A1 A2 z
```

A neutral move may preserve the zero triple but cyclically rotate it.

Candidate cyclic order:

```text
z A1 A2  <  A1 A2 z  <  A2 z A1
```

or another canonical cyclic ordering.  The script should report the observed cyclic order before and after, not assume the correct order.

### 3. Support equality span rank

For

```text
B_tail+q=A_complement,
```

rank the span needed to cover:

```text
B_tail, q
```

and also:

```text
B_tail, q, A_complement.
```

For

```text
B_prefix=q,
```

rank the span needed to cover:

```text
B_prefix, q.
```

Define:

```text
span_gap(S) = (max_position(S)-min_position(S)+1) - |S|.
```

Lower `span_gap` means the equality relation is more localized.

## New diagnostic

Add:

```text
scripts/test_equality_tie_break_ranks.py
```

Inputs:

```text
--analysis logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
--equations logs/bzqa_hidden_support_equations_p17_v3.jsonl
--bridge logs/hidden_support_bridge_moves_p17_v5.jsonl
```

and similarly for p=23.

Output:

```text
1. equality records by family;
2. neutral move counts;
3. rank deltas for:
   - terminal position;
   - cyclic order;
   - q-tail span;
   - q-tail-complement span;
   - q-prefix span;
4. coverage of records where at least one rank improves.
```

## Desired result

The strongest useful outcome is:

```text
B_tail+q=A_complement:
  every record has a neutral move decreasing q_tail_comp_span or q_tail_span.

B_prefix=q:
  every record has a neutral move decreasing q_prefix_span.
```

If true, the equality branch closes under a refined support-localization rank.

## Status

```text
Zero-sum branch closed.
Equality branch isolated.
Next: test concrete tie-break ranks.
```
