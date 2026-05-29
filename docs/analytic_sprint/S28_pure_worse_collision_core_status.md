# S28. Pure worse-only collision-core status

This records the first collision-core summary for the corrected pure `m=3` terminal residual.

## Inputs

```text
logs/summary_pure_worse_collision_core_p17.json
logs/summary_pure_worse_collision_core_p23.json
```

These were produced from:

```text
logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl
```

using:

```text
scripts/summarize_pure_worse_collision_core.py
```

## Pure worse-only counts

```text
p=17: 35 records
p=23: 59 records
```

Support lengths:

```text
p=17:
  3:  8
  4: 19
  5:  8

p=23:
  3:  9
  4:  7
  5: 12
  6: 13
  7: 13
  8:  5
```

## Universal signatures

Both p=17 and p=23 have the same universal L3 internal signatures:

```text
after_B=after_BAz:L3:internal_window
after_B=after_BzA:L3:internal_window
after_Bq=after_BqAz:L3:internal_window
after_Bq=after_BqzA:L3:internal_window
after_q=after_qAz:L3:internal_window
after_q=after_qzA:L3:internal_window
after_qB=after_qBAz:L3:internal_window
after_qB=after_qBzA:L3:internal_window
window_start=after_Az:L3:internal_window
window_start=after_zA:L3:internal_window
```

## Important correction

Most universal signatures are tautological in the following sense:

```text
A z = a b z
z A = z a b
```

Both are zero triples because:

```text
a+b+z=0.
```

Therefore any permutation with `A` adjacent to `z` automatically recreates a length-3 zero interval. This is useful, but it is not yet the hidden contradiction.

The next target is not all collision signatures. It is:

```text
non-tautological collision signatures
```

where the new collision is not simply the zero triple `A z` or `z A`.

## Key next split

For each pure worse-only move:

```text
1. tautological zero-triple collision:
   block multiset equals A ∪ {z}

2. known terminal collision:
   block multiset equals B ∪ {z}

3. non-tautological collision:
   anything else
```

The hard evidence will come from class 3, especially for permutations where `A` and `z` are separated.

## Next script

Add:

```text
scripts/summarize_pure_worse_nontautological_core.py
```

Input:

```text
logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl
```

Output fields:

```text
pure_worse_records
permutation classification by A/z adjacency
non-tautological collision signatures by permutation
universal non-tautological signatures by permutation
records where every separated-Az permutation has non-tautological collision
representative non-tautological examples
```

## Proof direction

The pure worse-only branch should be attacked through permutations where `A` and `z` are separated. If those still always worsen, the worsening collision cannot be the original zero triple. It must encode an additional equality involving `q`, `B`, or the exterior.

That equality is the likely hidden distributed or pair-trap relation.

## Status

```text
Universal L3 signatures found.
Most are tautological A/z zero-triple recreations.
Next: isolate non-tautological collision core.
```
