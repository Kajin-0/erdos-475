# S37. Formal lemma roadmap after hidden-support extraction

This note turns the current empirical reduction into formal proof targets.

## Current terminal-residual state

The difficult branch is:

```text
m=3,
D_short=(1,3,1,[2]),
right one-sided long terminal,
R = X A z q B Y,
A = A1 A2,
A+z=0,
B+z=0.
```

The local terminal window is:

```text
A z q B.
```

The terminal relation is:

```text
sum(B)=sum(A)=-z.
```

## Lemma target 1: finite descent/progress menu

A finite menu of block permutations of `A,z,q,B` gives either:

```text
1. D_short descent;
2. D_short-neutral rightward progress of the unique zero triple;
3. pure neutral cyclic case;
4. pure worse-only hidden support equation.
```

The empirically important permutations are:

```text
z q A B
A B q z
z q B A
B A q z
B z q A
A q z B
z A q B
```

## Lemma target 2: rightward-progress tie-break

For right-terminal residuals, define:

```text
P_R = right distance of the unique zero triple.
```

A neutral move with smaller `P_R` is progress under a refined defect:

```text
D_ref = (D_short, P_R, ...).
```

For left-terminal residuals, use the reversed coordinate.

## Lemma target 3: cyclic neutral branch

The pure neutral same-position branch is dominated by:

```text
A z q B -> z A q B.
```

For `A=A1 A2`, this changes:

```text
A1 A2 z -> z A1 A2.
```

The unique zero triple stays at the same position but is cyclically rotated.

Add a cyclic-rank tie-break:

```text
cyc_rank(A1,A2,z)
```

so that:

```text
z A1 A2 < A1 A2 z
```

or use canonical cyclic representative of the unique zero triple.

Proof target:

```text
If D_short and P_R are unchanged under A z q B -> z A q B, then cyc_rank decreases.
```

## Lemma target 4: pure worse-only hidden support equation

For every observed pure worse-only residual, the move:

```text
B z q A
```

exposes one of:

```text
B_tail + q + Y_prefix = 0
B_prefix = q
```

This should become the central structural lemma:

```text
Pure worse-only m=3 terminal residual
  => hidden support-prefix/tail relation involving q.
```

Formal proof sketch:

```text
1. Since B z q A worsens from D_short=(1,3,1,[2]), it creates an additional zero interval.
2. The tautological intervals are only A+z=0 and B+z=0.
3. In pure worse-only records, the new non-tautological interval under B z q A must cross the rearranged B/z/q/A boundary.
4. The only possible universal local forms are:
   B_tail + z + q + A + Y_prefix = 0,
   or B_tail + z + q = 0.
5. These reduce respectively to:
   B_tail + q + Y_prefix = 0,
   or B_prefix = q.
```

## Lemma target 5: hidden support relation is reducible

Need to prove that either hidden-support form contradicts pure terminality or routes to an earlier branch.

### Case 5A: B_tail + q = 0

This gives a zero block inside the moved order using a suffix of `B` and `q`.

Target route:

```text
terminal-tail bridge / signed interval / pair-trap
```

Candidate move:

```text
A z q B_prefix B_tail
```

Since:

```text
q + B_tail = 0,
```

moving `B_tail` next to `q` creates a controlled zero block shorter than or comparable to the terminal block.

### Case 5B: B_tail + q + Y_prefix = 0

This is a right-exterior bridge.

Target route:

```text
external bridge overlap / right-terminal exterior bridge
```

It should be handled by extending the external bridge lemmas to allow `q` plus a support tail and a right exterior prefix.

### Case 5C: B_prefix = q

Since `q` is a single atom equal to a prefix sum of `B`, this is a prefix replacement relation.

Target route:

```text
support-prefix compression
```

Possible move:

```text
replace B_prefix by q
```

or compare:

```text
B_prefix + B_tail + z = 0
q + B_tail + z = 0.
```

This creates two zero intervals sharing `B_tail+z`, likely forcing a collision contradiction or a pair-trap.

## Recommended next empirical/proof step

Add a script to test the hidden-support relation as a move primitive:

```text
scripts/test_hidden_support_bridge_moves.py
```

Input:

```text
logs/bzqa_hidden_support_equations_p17.jsonl
logs/bzqa_hidden_support_equations_p23.jsonl
```

It should attempt deterministic moves for each family:

```text
B_tail+q:
  make q B_tail contiguous, or B_tail q contiguous.

B_tail+q+Y_prefix:
  make q B_tail Y_prefix contiguous, or route as exterior bridge.

B_prefix=q:
  swap q with B_prefix, or compress B_prefix against q.
```

Metrics:

```text
old D_ref
new D_ref
D_short descent?
rightward progress?
cyclic-rank progress?
external/signed/distributed flag created?
```

## Formal proof priority

The current best path is:

```text
1. promote the empirical hidden-support equation to a formal structural lemma;
2. define the refined defect order with rightward and cyclic tie-breaks;
3. prove hidden-support equations route to signed/external/support-prefix bridge;
4. integrate into the full terminal-bridge proof.
```

## Status

```text
Empirical terminal residual is now proof-structured.
Remaining work: turn hidden support relation into a reduction lemma.
```
