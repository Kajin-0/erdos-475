# S30. Pure worse-only symbolic block status

This note records the first symbolic-block output from:

```text
scripts/summarize_pure_worse_symbolic_blocks.py
```

using:

```text
logs/summary_pure_worse_symbolic_blocks_p17.json
logs/summary_pure_worse_symbolic_blocks_p23.json
```

## Confirmed stable fact: A q z B is terminal-only

For p=17:

```text
A_q_z_B_collision_class_counts = {
  terminal_zB: 35
}
```

For p=23:

```text
A_q_z_B_collision_class_counts = {
  terminal_zB: 59
}
```

Thus the separated permutation:

```text
A q z B
```

never creates a non-tautological collision in the pure worse-only datasets.  It worsens only because it makes the terminal zero block contiguous:

```text
z B,
```

where:

```text
z + sum(B) = 0.
```

This confirms the `terminal-stall` mechanism.

## Stable hidden-collision permutations

The earlier coverage table identified five permutations with universal non-tautological collisions in both p=17 and p=23:

```text
A B q z
B A q z
B z q A
z q A B
z q B A
```

The symbolic output confirms that these moves produce many non-tautological zero blocks, but the raw symbolic histograms are too large for proof work.

## Dominant symbolic families visible in the output

The raw symbolic blocks repeatedly fall into a small number of coarse families:

```text
A-prefix plus B-prefix:
  A1 A2 B1 B2
  A1 A2 B1 B2 B3
  A2 B1
  A2 B1 B2

B-tail plus q / z / A:
  Bk q
  Bk B{k+1} q
  Bk z q A1 A2
  Bk A1
  Bk A1 A2 q z

right-exterior equations:
  z Y1
  z Y1 Y2
  q z Y1
  q z Y1 Y2

q plus A/B prefixes:
  q A1 A2 B1...
  q B1 B2... A1...
```

These are algebraic zero-sum equations.  For example:

```text
A2 B1 = 0
```

means:

```text
a_2 + b_1 = 0.
```

and:

```text
A1 A2 B1 B2 = 0
```

means:

```text
sum(A) + b_1 + b_2 = 0.
```

Since `sum(A)=sum(B)=-z`, this gives:

```text
sum(B) + b_1 + b_2 = 0.
```

So these symbolic families are the correct next abstraction layer.

## Why a new compact summarizer is needed

The symbolic output is too detailed.  It distinguishes:

```text
B3 q,
B4 q,
B5 q,
```

but for proof these are all the same family:

```text
B_tail q = 0.
```

Likewise:

```text
A1 A2 B1 B2,
A1 A2 B1 B2 B3,
A1 A2 B1 B2 B3 B4
```

belong to:

```text
A_all + B_prefix(k) = 0.
```

The next script should normalize symbolic blocks into families.

## Next script

Add:

```text
scripts/summarize_pure_worse_symbolic_families.py
```

Input:

```text
logs/summary_pure_worse_symbolic_blocks_p17.json
logs/summary_pure_worse_symbolic_blocks_p23.json
```

Output:

```text
1. family histogram by stable permutation;
2. shortest-family histogram by stable permutation;
3. families common to both p=17 and p=23;
4. support-length dependence if available;
5. compact examples.
```

Useful family labels:

```text
A_all+B_prefix
A_suffix+B_prefix
B_tail+q
B_tail+zq+A
B_tail+A_prefix
z+Y_prefix
qz+Y_prefix
q+A_all+B_prefix
q+B_prefix+A_prefix
mixed_X_prefix
other
```

## Candidate proof routes suggested by symbolic families

### Route 1: signed/pair extraction

Blocks like:

```text
A2 B1
B3 q
z Y1
```

are short zero-sum equations.  These should be interpreted as signed/pair relations in the moved order.  If they occur systematically, the pure worse-only branch may hide a pair-trap or signed route.

### Route 2: prefix-sum contradiction inside B

Blocks like:

```text
A1 A2 B1 ... Bk
```

combined with:

```text
sum(A)=sum(B)
```

imply:

```text
sum(B) + sum(B_1...B_k) = 0.
```

Equivalently:

```text
sum(B_{k+1}...B_s) = -2 sum(B_1...B_k)
```

or related prefix/tail constraints.  Repeated occurrence across several permutations may force two incompatible prefix equations.

### Route 3: exterior exhaustion

Blocks like:

```text
z Y1,
q z Y1,
z Y1 Y2
```

mean the residual is not purely local after all.  It depends on the right exterior `Y`.  Since p=17 pure worse has small Y length, these may be boundary-exhaustion cases.

## Status

```text
A q z B terminal-only mechanism confirmed.
Universal hidden-collision moves confirmed.
Raw symbolic output too large.
Next: collapse symbolic zero blocks into algebraic families.
```
