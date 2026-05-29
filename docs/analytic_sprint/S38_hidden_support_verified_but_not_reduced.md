# S38. Hidden-support equations verified, but naive bridge moves do not close branch

This note records the v5 run of:

```text
scripts/test_hidden_support_bridge_moves.py
```

against the v3 hidden-support equation files.

## Inputs

```text
logs/bzqa_hidden_support_equations_p17_v3.jsonl
logs/bzqa_hidden_support_equations_p23_v3.jsonl
logs/hidden_support_bridge_moves_p17_v5.jsonl
logs/hidden_support_bridge_moves_p23_v5.jsonl
```

## Equation verification is now clean

The bridge tester now correctly distinguishes zero-sum equations from congruence equations.

### p=17

```text
records = 35
hidden_equation_holds = {True: 35}
hidden_equation_modes = {
  zero_sum: 31,
  equality: 4
}
```

### p=23

```text
records = 59
hidden_equation_holds = {True: 59}
hidden_equation_modes = {
  zero_sum: 52,
  equality: 7
}
```

Therefore the universal hidden-support extraction is now internally verified.

## Correct reduced-family split

### p=17

```text
B_tail+q                  = 23
B_tail+q+Y_prefix          =  8
B_tail+q=A_complement      =  4
```

### p=23

```text
B_tail+q                  = 20
B_tail+q+Y_prefix          = 32
B_tail+q=A_complement      =  5
B_prefix=q                =  2
```

## Naive bridge moves do not close the branch

The deterministic move menu currently gives no D_short descent.

### p=17

```text
best_class_counts = {
  neutral: 4,
  worse: 31
}
```

By family:

```text
B_tail+q                  -> worse 23
B_tail+q+Y_prefix          -> worse  8
B_tail+q=A_complement      -> neutral 4
```

### p=23

```text
best_class_counts = {
  neutral: 7,
  worse: 52
}
```

By family:

```text
B_tail+q                  -> worse 20
B_tail+q+Y_prefix          -> worse 32
B_tail+q=A_complement      -> neutral 5
B_prefix=q                -> neutral 2
```

## Interpretation

The equality branches are structurally weaker and produce neutral moves:

```text
B_tail+q=A_complement
B_prefix=q
```

The zero-sum branches remain resistant to naive local rearrangement:

```text
B_tail+q
B_tail+q+Y_prefix
```

This suggests the next proof step should not be a local bridge permutation.  Instead, we need to analyze the obstruction created when trying to realize the hidden zero block contiguously.

## Next target

Add:

```text
scripts/summarize_hidden_bridge_obstruction_core.py
```

It should read:

```text
logs/hidden_support_bridge_moves_p17_v5.jsonl
logs/hidden_support_bridge_moves_p23_v5.jsonl
```

and summarize:

```text
1. records by reduced family;
2. best move per record;
3. zero-interval lengths created by best moves;
4. universal obstruction signatures by reduced family;
5. whether equality-neutral branches are exactly cyclic-rank/tie-break cases;
6. whether zero-sum worse branches always create the same secondary obstruction.
```

## Updated proof state

The pure worse-only branch is now reduced to a verified hidden-support equation, but not yet to a decreasing move.

Current proof obligations:

```text
1. Equality branch:
   B_tail+q=A_complement or B_prefix=q
   -> neutral under current move menu; likely tie-break/cyclic-rank/refined order.

2. Zero-sum branch:
   B_tail+q or B_tail+q+Y_prefix
   -> current local moves worsen; need obstruction-core analysis.
```

## Status

```text
Hidden support relation verified universally.
Naive bridge moves insufficient.
Next: classify obstruction core of failed hidden bridge moves.
```
