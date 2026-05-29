# S40. Filtered secondary-obstruction plan

The first secondary-collision summary produced useful data, but it is still dominated by expected zero intervals:

```text
old_Az              = A1 A2 z
hidden_reduced_exact = the intended hidden-support zero block
terminal_zB          = inherited terminal support block
```

These are not the obstruction.  They are expected consequences of the residual normal form or of the bridge move being tested.

## Latest observed pattern

The verified hidden-support branch has four reduced families:

```text
B_tail+q
B_tail+q+Y_prefix
B_tail+q=A_complement
B_prefix=q
```

The bridge-move tester shows:

```text
Equality families:
  B_tail+q=A_complement -> neutral
  B_prefix=q            -> neutral

Zero-sum families:
  B_tail+q              -> worse
  B_tail+q+Y_prefix     -> worse
```

The secondary-collision output confirms that the zero-sum families create additional short zero intervals, but the raw summary mixes genuine secondary intervals with expected ones.

## Required filtering

The next analysis must ignore the following symbolic classes:

```text
old_Az
terminal_zB
hidden_reduced_exact
```

and report only genuine additional collisions such as:

```text
Bq_zero
BqY_zero
B_prefix_or_mixed
AB_zero
ABq_zero
right_exterior_qY
right_exterior_zY
left_exterior_X
other
```

## Main proof target

For zero-sum hidden-support branches, we need a statement of the form:

```text
If a bridge move attempting to realize B_tail+q(+Y_prefix)=0 worsens,
then it creates a genuine secondary collision of type S.
```

If `S` is always one of:

```text
Bq_zero
BqY_zero
B_prefix_or_mixed
right_exterior_qY
```

then the hidden-support branch should reduce to signed/exterior/support-prefix bridge lemmas.

## Next script

Add:

```text
scripts/summarize_hidden_bridge_genuine_obstructions.py
```

Input:

```text
logs/summary_hidden_bridge_secondary_collisions_p17.json
logs/summary_hidden_bridge_secondary_collisions_p23.json
```

or directly:

```text
--analysis logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
--equations logs/bzqa_hidden_support_equations_p17_v3.jsonl
--bridge logs/hidden_support_bridge_moves_p17_v5.jsonl
```

The direct form is preferred because it can compute record-level coverage.

Output:

```text
1. records by reduced family;
2. records with any genuine secondary obstruction;
3. genuine obstruction class histogram;
4. genuine obstruction symbolic histogram;
5. record-level coverage by obstruction class;
6. representative examples.
```

## Expected result to test

For zero-sum families:

```text
B_tail+q
B_tail+q+Y_prefix
```

we want to test whether:

```text
every record has at least one genuine secondary obstruction after removing old_Az and hidden_reduced_exact.
```

For equality families:

```text
B_tail+q=A_complement
B_prefix=q
```

we expect mostly no genuine obstruction, because current best moves are neutral.  Those likely require only a refined tie-break.

## Status

```text
Raw secondary collisions identified.
Need filtered genuine-obstruction summary next.
```
