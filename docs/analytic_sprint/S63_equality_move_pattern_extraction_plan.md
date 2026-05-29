# S63. Equality neutral-move pattern extraction plan

S62 drafted the equality tie-break lemma:

```text
B_tail + q = A_complement
B_prefix = q
```

should admit a `D_short`-neutral move with

```text
S_tail(new) < S_tail(old),
S_tail(R) = span_gap_R({q} union B_tail).
```

The rank test already showed full empirical coverage:

```text
p=17: 4 / 4 equality records improve q_tail_span_gap.
p=23: 7 / 7 equality records improve q_tail_span_gap.
```

## Remaining issue

The proof still needs a symbolic description of the neutral move.

We need to know whether all equality records are handled by one uniform move pattern or by multiple subcase moves.

## New diagnostic

Add:

```text
scripts/extract_equality_tie_break_patterns.py
```

Inputs:

```text
--analysis logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
--equations logs/bzqa_hidden_support_equations_p17_v3.jsonl
--bridge logs/hidden_support_bridge_moves_p17_v5.jsonl
```

and similarly for p=23.

The script should print, for each equality record:

```text
p,
record_index,
family,
reduced_equation,
old_symbolic_order,
new_symbolic_order,
move_name,
B_tail labels,
q label,
old q_tail_span_gap,
new q_tail_span_gap,
old q_tail_span_width,
new q_tail_span_width,
improved rank keys.
```

It should also summarize:

```text
1. old/new symbolic pattern histogram;
2. move-name histogram by family;
3. records whose best neutral move improves q_tail_span_gap;
4. representative examples.
```

## Desired outcome

The ideal result is a compact symbolic rule such as:

```text
Move q adjacent to B_tail by applying permutation P.
```

or two rules:

```text
B_tail+q=A_complement:
  move pattern P1.

B_prefix=q:
  move pattern P2.
```

## Status

```text
Equality tie-break rank found.
Next: extract symbolic move pattern for proof.
```
