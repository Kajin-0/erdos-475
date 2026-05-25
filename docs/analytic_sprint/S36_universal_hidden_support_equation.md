# S36. Universal hidden-support equation for pure worse-only m=3 residuals

This note records the patched output of:

```text
scripts/extract_bzqa_tail_core_equations.py
```

from:

```text
logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl
```

## Main result

The pure worse-only `m=3` right-terminal residual now has a universal hidden-support equation under the permutation:

```text
B z q A
```

For every observed pure worse-only record, the extracted equation is one of:

```text
B_tail + q = 0
B_tail + q + Y_prefix = 0
B_prefix = q
```

No records are missing.

## p=17 patched extraction

```text
input_records      = 35
extracted_records  = 35
missing_records    = 0
```

Extraction kind:

```text
tail_core = 35
```

Reduced-family histogram:

```text
B_tail+q          = 28
B_tail+q+Y_prefix =  7
```

Right exterior prefix length:

```text
Y_prefix_length = 0: 28
Y_prefix_length = 1:  6
Y_prefix_length = 2:  1
```

Support-length distribution:

```text
3:  8
4: 19
5:  8
```

## p=23 patched extraction

```text
input_records      = 59
extracted_records  = 59
missing_records    = 0
```

Extraction kind:

```text
tail_core   = 57
prefix_core =  2
```

Reduced-family histogram:

```text
B_tail+q          = 32
B_tail+q+Y_prefix = 25
B_prefix=q        =  2
```

Right exterior prefix length:

```text
Y_prefix_length = 0: 34
Y_prefix_length = 1: 19
Y_prefix_length = 2:  4
Y_prefix_length = 3:  2
```

Support-length distribution:

```text
3:  9
4:  7
5: 12
6: 13
7: 13
8:  5
```

## Algebraic normal form

The pure worse-only residual has:

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0.
```

Therefore:

```text
A + z = 0,
sum(A) = sum(B) = -z.
```

Under the move:

```text
B z q A
```

the observed hidden equation is either:

```text
B_tail + z + q + A + Y_prefix = 0
```

which reduces using `A+z=0` to:

```text
B_tail + q + Y_prefix = 0,
```

or:

```text
B_tail + z + q = 0,
```

which, together with:

```text
B_prefix + B_tail + z = 0,
```

reduces to:

```text
B_prefix = q.
```

## Proof-relevant conclusion

The pure worse-only branch is not a primitive obstruction.  It implies a hidden support relation involving the separator `q`:

```text
B_tail + q + Y_prefix = 0
```

or

```text
B_prefix = q.
```

This should be promoted to a branch lemma:

```text
Pure worse-only m=3 terminal residual
  => hidden support-prefix/tail bridge involving q.
```

## Branch reduction status

The one-sided right-long-terminal `m=3` residual is now split as:

```text
1. D_short descent by finite block permutation;
2. D_short-neutral rightward progress;
3. pure neutral same-position / leftward branch;
4. pure worse-only hidden support-prefix/tail branch.
```

For branch 3, the likely resolution is a cyclic-rank tie-break on the unique zero triple.

For branch 4, the resolution should be a hidden support-bridge lemma using:

```text
B_tail + q + Y_prefix = 0
```

or

```text
B_prefix = q.
```

## Status

```text
Universal hidden-support equation extracted.
p=17: 35/35.
p=23: 59/59.
Pure worse-only branch reduced to explicit algebraic support relation.
```
