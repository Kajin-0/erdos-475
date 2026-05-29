# S39. Hidden bridge obstruction-core status

This note records the obstruction-core summaries for the verified hidden-support branch.

## Inputs

```text
logs/summary_hidden_bridge_obstruction_core_p17.json
logs/summary_hidden_bridge_obstruction_core_p23.json
```

These were generated from:

```text
logs/hidden_support_bridge_moves_p17_v5.jsonl
logs/hidden_support_bridge_moves_p23_v5.jsonl
```

using:

```text
scripts/summarize_hidden_bridge_obstruction_core.py
```

## p=17 summary

Records:

```text
B_tail+q                     = 23
B_tail+q+Y_prefix             =  8
B_tail+q=A_complement         =  4
```

Equation modes:

```text
B_tail+q                     -> zero_sum
B_tail+q+Y_prefix             -> zero_sum
B_tail+q=A_complement         -> equality
```

Best classes:

```text
B_tail+q                     -> worse
B_tail+q+Y_prefix             -> worse
B_tail+q=A_complement         -> neutral
```

Thus all equality cases are neutral, while all zero-sum cases remain worse under the current move menu.

## p=23 summary

Records:

```text
B_prefix=q                   =  2
B_tail+q                     = 20
B_tail+q+Y_prefix             = 32
B_tail+q=A_complement         =  5
```

Equation modes:

```text
B_prefix=q                   -> equality
B_tail+q                     -> zero_sum
B_tail+q+Y_prefix             -> zero_sum
B_tail+q=A_complement         -> equality
```

Best classes:

```text
B_prefix=q                   -> neutral
B_tail+q                     -> worse
B_tail+q+Y_prefix             -> worse
B_tail+q=A_complement         -> neutral
```

Again, equality cases are neutral, while zero-sum cases remain worse.

## Main interpretation

The verified hidden-support equation splits into two structural classes:

```text
1. Equality branch:
   B_tail+q=A_complement
   B_prefix=q

   Current moves are D_short-neutral.
   These likely need only a refined tie-break.

2. Zero-sum branch:
   B_tail+q=0
   B_tail+q+Y_prefix=0

   Current moves are always worse.
   These require a secondary obstruction analysis.
```

## Important obstruction signal

For the zero-sum branches, the best move signatures are not uniform in exact defect, but they are consistently worse by creating additional zero intervals.  The dominant effects are:

```text
E increases by 1, 2, or 3;
L often stays 3 or drops to 2;
N_min often stays the same or increases.
```

So the hidden-support equation is real, but naively making it contiguous creates another collision.  The next target is to identify that secondary collision symbolically.

## Next script

Add:

```text
scripts/summarize_hidden_bridge_secondary_collisions.py
```

Inputs:

```text
--analysis logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
--equations logs/bzqa_hidden_support_equations_p17_v3.jsonl
--bridge logs/hidden_support_bridge_moves_p17_v5.jsonl
```

and similarly for p=23.

Target output:

```text
1. symbolic shortest zero intervals in best failed bridge moves;
2. classify secondary blocks as:
   old_Az,
   terminal_zB,
   hidden_support_block,
   Bq_pair,
   A/B_prefix,
   exterior_bridge,
   partial_A,
   other;
3. summarize universal secondary obstruction patterns by reduced family;
4. representative examples.
```

## Proof implication

If the zero-sum branch always creates the same symbolic secondary collision, then the next lemma is:

```text
hidden zero-sum support relation
  + failure of bridge move
  => secondary collision of type S.
```

That may route to an already known branch: signed interval, pair-trap, distributed bridge, or external bridge.

## Status

```text
Hidden-support equation verified.
Equality branches are neutral.
Zero-sum branches are the remaining obstruction.
Next: symbolic secondary-collision analysis.
```
