# S34. B z q A tail-equation extraction status

This note records the output of:

```text
scripts/extract_bzqa_tail_core_equations.py
```

from:

```text
logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl
```

## p=17 result

```text
input_records      = 35
extracted_records  = 35
missing_records    = 0
```

Reduced-family histogram:

```text
B_tail+q          = 28
B_tail+q+Y_prefix =  7
```

Tail-length histogram:

```text
1: 15
2: 16
3:  4
```

Tail-start histogram:

```text
2:  8
3: 12
4: 11
5:  4
```

Right-exterior prefix length:

```text
0: 28
1:  6
2:  1
```

Thus every p=17 pure worse-only residual has a reduced equation of the form:

```text
B_tail + q + Y_prefix = 0.
```

Most are the stronger local equation:

```text
B_tail + q = 0.
```

## p=23 result

```text
input_records      = 59
extracted_records  = 57
missing_records    = 2
```

Reduced-family histogram:

```text
B_tail+q          = 32
B_tail+q+Y_prefix = 25
```

Tail-length histogram:

```text
1: 26
2: 13
3:  8
4:  7
5:  2
6:  1
```

Tail-start histogram:

```text
2:  5
3: 17
4: 13
5:  9
6:  4
7:  7
8:  2
```

Right-exterior prefix length:

```text
0: 32
1: 19
2:  4
3:  2
```

Thus at least 57 of 59 p=23 pure worse-only residuals have the same reduced equation:

```text
B_tail + q + Y_prefix = 0.
```

The two missing records are now the only obstruction to a universal p=23 statement.

## Main theorem-shaped output

For the pure worse-only branch, the permutation

```text
B z q A
```

exposes a hidden zero block of the form:

```text
B_tail + z + q + A + Y_prefix = 0.
```

Because in the m=3 residual:

```text
A + z = 0,
```

this reduces to:

```text
B_tail + q + Y_prefix = 0.
```

This is the proof-relevant hidden equation.

## Interpretation

The pure worse-only branch is now reduced to:

```text
p=17: universal hidden tail equation, 35/35.
p=23: hidden tail equation for 57/59; two cases require diagnosis.
```

This is likely enough to write a conditional lemma, but the two p=23 missing records should be inspected before formalizing.

## Next diagnostic

Add:

```text
scripts/diagnose_missing_bzqa_tail_core.py
```

It should:

```text
1. rerun the B z q A symbolic-block analysis;
2. identify pure_worse_only records where extract_bzqa_tail_core_equations.py fails;
3. print all non-tautological symbolic zero blocks under B z q A;
4. classify each block into family/meta-family;
5. show whether the miss is due to:
   - exterior-only terms;
   - missing q;
   - missing z;
   - missing A;
   - B-prefix rather than B-tail;
   - classifier-labeling error.
```

## Proof priority after diagnosis

If the two missing records are classifier misses, patch the extractor and promote the lemma to universal.

If they are genuine exceptions, split the pure worse-only branch into:

```text
1. B_tail + q + Y_prefix = 0 tail-equation branch;
2. exceptional B z q A branch, size 2 in p=23 sample.
```

## Status

```text
B z q A tail-equation branch extracted.
p=17 universal.
p=23 almost universal; diagnose 2 missing records next.
```
