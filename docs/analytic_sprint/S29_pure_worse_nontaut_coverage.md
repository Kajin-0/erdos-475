# S29. Pure worse-only non-tautological coverage status

This file records the compact coverage table from:

```text
scripts/print_pure_worse_nontaut_coverage.py
```

using:

```text
logs/summary_pure_worse_nontautological_core_p17.json
logs/summary_pure_worse_nontautological_core_p23.json
```

## p=17 coverage

```text
pure_worse_records = 35
```

Coverage table:

```text
A B q z   35 / 35 = 1.000
A B z q   35 / 35 = 1.000
A q B z   33 / 35 = 0.943
A q z B    0 / 35 = 0.000
B A q z   35 / 35 = 1.000
B z q A   35 / 35 = 1.000
q A B z   32 / 35 = 0.914
q z B A   19 / 35 = 0.543
z B A q   29 / 35 = 0.829
z B q A   34 / 35 = 0.971
z q A B   35 / 35 = 1.000
z q B A   35 / 35 = 1.000
```

## p=23 coverage

```text
pure_worse_records = 59
```

Coverage table:

```text
A B q z   59 / 59 = 1.000
A B z q   55 / 59 = 0.932
A q B z   53 / 59 = 0.898
A q z B    0 / 59 = 0.000
B A q z   59 / 59 = 1.000
B z q A   59 / 59 = 1.000
q A B z   57 / 59 = 0.966
q z B A   50 / 59 = 0.847
z B A q   53 / 59 = 0.898
z B q A   52 / 59 = 0.881
z q A B   59 / 59 = 1.000
z q B A   59 / 59 = 1.000
```

## Stable universal separated permutations

The following permutations have non-tautological collisions in every pure-worse record for both p=17 and p=23:

```text
A B q z
B A q z
B z q A
z q A B
z q B A
```

Additionally:

```text
A B z q
```

is universal for p=17 but not for p=23.

## Special zero-nontautological permutation

The permutation:

```text
A q z B
```

has zero non-tautological collisions in both datasets:

```text
p=17: 0 / 35
p=23: 0 / 59
```

This is important.  It separates `A` and `z`, but it places:

```text
z B
```

contiguously.  Since the terminal relation is:

```text
z + sum(B) = 0,
```

this move creates the terminal zero block `zB` and appears to worsen only by replacing the length-3 triple `Az` with the longer terminal zero block `zB`.

Thus the pure worse-only branch has two mechanisms:

```text
1. terminal-stall mechanism: A q z B creates only the long terminal zero interval zB;
2. hidden-collision mechanism: several other separated permutations create non-tautological collisions universally.
```

## Next target

The next analysis should convert numeric collision blocks into symbolic blocks using labels:

```text
A1,A2,z,q,B1,...,Bs,Y1,...
```

For example, instead of reporting:

```text
[7, 11, 16]
```

it should report something like:

```text
B3 q Y1
```

or similar, depending on the original order.

This is necessary because the final proof needs algebraic equations, not numeric examples.

## Next script

Add:

```text
scripts/summarize_pure_worse_symbolic_blocks.py
```

Input:

```text
logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl
```

Target output:

```text
1. symbolic nontautological block patterns by permutation;
2. shortest symbolic nontautological block per record/permutation;
3. universal symbolic patterns by support length;
4. examples in symbolic form;
5. special summary for A q z B showing only terminal_zB.
```

## Proof direction

Focus on the five stable universal permutations:

```text
A B q z,
B A q z,
B z q A,
z q A B,
z q B A.
```

For each pure worse record, at least one non-tautological collision equation appears for each of these five moves.  Once expressed symbolically, these equations should reveal a hidden distributed/pair relation or a contradiction with pure terminality.

## Status

```text
Pure worse-only coverage resolved.
Next: symbolic collision equations.
```
