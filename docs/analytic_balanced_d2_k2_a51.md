# Analytic proper balanced D2, first case A51: the k=m=2 branch

This note continues from A50.

A50 identified the first unresolved proper balanced D2 branch as

```text
k=m=2.
```

A41 reduced balanced D2 to a paired difference walk.  For `k=2`, there is only one intermediate value, so the branch is small enough to write completely.

This note derives the exact algebra, records what the absence of the other direct-exchange branches forces, and isolates the remaining atom-pair obstruction.  It does not close the branch.

---

## Standing setup

Let a separated equal-interval segment be

```text
X A G C Y
```

with

```text
sum(A)=sum(C)=a,
sum(G)=g.
```

Write

```text
C = c_1 c_2 L,
Y = y_1 y_2 N.
```

Let

```text
K_1=c_1,
K_2=c_1+c_2,
M_1=y_1,
M_2=y_1+y_2.
```

The balanced D2 condition for `k=m=2` is

```text
K_2 = 2a+g+M_2.
```

Equivalently,

```text
(c_1+c_2)-(y_1+y_2)=2a+g.
```

Define the intermediate pair-difference

```text
delta = c_1-y_1.
```

Then

```text
c_2-y_2 = 2a+g-delta.
```

---

# 1. A41 residual conditions for k=2

For `k=2`, the paired difference walk is

```text
D_0=0,
D_1=delta,
D_2=2a+g.
```

The residual A41 conditions are exactly:

```text
delta != 0,
delta != 2a+g.
```

The first condition says the first atom pair is not equal:

```text
c_1 != y_1.
```

The second condition says the second atom pair is not equal:

```text
c_2 != y_2.
```

## Lemma A51.1: k=2 residual balanced D2 is equivalent to two nonzero complementary pair differences

The `k=2` residual branch is equivalent to the existence of

```text
delta notin {0,2a+g}
```

such that

```text
c_1-y_1=delta,
c_2-y_2=2a+g-delta.
```

### Proof

The first equality is the definition of `delta`.  The second follows by subtracting the first pair-difference from the total balanced D2 difference.  The residual A41 conditions are exactly that neither pair-difference vanishes. ∎

---

# 2. Composite-zero form

Since

```text
C = c_1 c_2 L,
sum(C)=a,
```

we have

```text
sum(L)=a-c_1-c_2.
```

Balanced D2 gives

```text
c_1+c_2=2a+g+y_1+y_2.
```

Therefore

```text
sum(A G L y_1 y_2)=0.
```

## Lemma A51.2: k=2 balanced D2 is a balanced two-atom replacement zero composite

The equation

```text
c_1+c_2=2a+g+y_1+y_2
```

is equivalent to

```text
sum(A G L y_1 y_2)=0.
```

### Proof

Compute:

```text
sum(A G L y_1 y_2)
= a+g+(a-c_1-c_2)+(y_1+y_2)
=2a+g+y_1+y_2-(c_1+c_2).
```

This vanishes exactly under balanced D2. ∎

### Interpretation

The `k=2` balanced branch is a zero composite obtained by replacing the two-atom prefix

```text
c_1 c_2
```

of `C` with the two-atom prefix

```text
y_1 y_2
```

of `Y`.

This is the length-2 analog of the atom-balanced D2 branch from A46--A47.

---

# 3. Consequences of absence of shorter balanced transfer

For `k=2`, the only shorter balanced transfer length is `1`.

A shorter balanced transfer would occur if

```text
D_1 = 2a+g.
```

But the residual condition excludes this.

A smaller separated equal prefix would occur if

```text
D_1=0.
```

The residual condition excludes this as well.

Thus the length-2 balanced branch is exactly the case where neither individual atom-pair difference closes the transfer by itself.

---

# 4. Absence of D1, D3, D4, D5

The direct-exchange branch D2 is active only after excluding the other collision branches.

Recall:

```text
D1: C_k = a+G_j
D3: A_i = G_j-g
D4: A_i = a+Y_m
D5: C_k = a+g+A_i
```

For the present `k=m=2` branch, the relevant forced exclusions include the following.

## Lemma A51.3: absence of D1 excludes C-prefix/G-prefix matches

For every valid prefix index `j` of `G`, absence of D1 gives

```text
c_1 != a+G_j,
c_1+c_2 != a+G_j.
```

Using balanced D2, the second exclusion is equivalent to

```text
2a+g+y_1+y_2 != a+G_j,
```

or

```text
a+g+y_1+y_2 != G_j.
```

### Status

These exclusions prevent the D2 obstruction from immediately routing to the D1 equal-interval descent branch.

---

## Lemma A51.4: absence of D4 excludes A-prefix/Y-prefix matches

For every valid prefix index `i` of `A`, absence of D4 gives

```text
A_i != a+y_1,
A_i != a+y_1+y_2.
```

Equivalently,

```text
tail_i(A)+y_1 != 0,
tail_i(A)+y_1+y_2 != 0.
```

### Proof

Rearrange `A_i != a+Y_m` using `a-A_i=tail_i(A)`. ∎

### Status

These exclusions prevent immediate two-piece zero routes of the type already handled in A36/A49.

---

## Lemma A51.5: absence of D5 at k=2 repeats the D4 m=2 exclusion

At `k=2`, D5 would be

```text
c_1+c_2 = a+g+A_i.
```

Using balanced D2,

```text
2a+g+y_1+y_2 = a+g+A_i,
```

so

```text
A_i = a+y_1+y_2.
```

This is exactly the D4 exclusion for `m=2`.

### Proof

Immediate by substitution. ∎

---

## Lemma A51.6: absence of D3 excludes A-prefix/G-tail zero composites

D3 absence gives, for every `i,j`,

```text
A_i != G_j-g.
```

Equivalently,

```text
A_i+tail_j(G) != 0.
```

### Proof

Since `tail_j(G)=g-G_j`, the equality `A_i=G_j-g` is equivalent to `A_i+tail_j(G)=0`. ∎

---

# 5. Pair-swap structure inside the two-atom transfer

The length-2 transfer has two atom pairs:

```text
(c_1,y_1),
(c_2,y_2).
```

Their differences are

```text
delta,
T-delta,
```

where

```text
T=2a+g.
```

Swapping the order of the transferred pair on either side changes the intermediate difference values.

## Lemma A51.7: reversing the Y-pair changes the intermediate difference to c_1-y_2

If one compares

```text
K=(c_1,c_2)
```

against the reversed pair

```text
M'=(y_2,y_1),
```

then the total difference remains

```text
T=(c_1+c_2)-(y_1+y_2),
```

but the intermediate value becomes

```text
delta' = c_1-y_2.
```

If

```text
delta'=0
```

then `c_1=y_2`, impossible by distinctness if the blocks are disjoint.

If

```text
delta'=T,
```

then

```text
c_2=y_1,
```

also impossible by distinctness.

### Proof

The total difference is unchanged by reordering the `Y` pair.  If `c_1-y_2=T`, then

```text
c_1-y_2=(c_1+c_2)-(y_1+y_2),
```

so `c_2=y_1`. ∎

### Interpretation

For a disjoint pair, reversing the two `Y` atoms cannot create an endpoint value `0` or `T` at the first step.  Thus reversal alone does not force descent in length 2.

---

## Lemma A51.8: reversing the C-pair gives the intermediate value c_2-y_1

If one compares

```text
K'=(c_2,c_1),
M=(y_1,y_2),
```

then the total difference remains `T`, but the intermediate value is

```text
c_2-y_1.
```

Endpoint intermediate values again imply atom equality:

```text
c_2-y_1=0  -> c_2=y_1,
```

and

```text
c_2-y_1=T -> c_1=y_2.
```

Both are impossible for disjoint atoms.

### Status

Pair reversal does not by itself eliminate the residual branch.

---

# 6. Consequence: k=2 is a genuine local residual

The `k=2` proper balanced branch cannot be closed by the same intermediate-walk argument as larger `k`, because there is only one intermediate value.

It also cannot be closed merely by reversing the two-atom pairs, because endpoint intermediate values under reversal would force atom equality and therefore are excluded rather than guaranteed.

Thus the remaining local object is a rigid two-pair difference system:

```text
c_1-y_1 = delta,
c_2-y_2 = T-delta,
```

with all cross-equalities excluded by distinctness and D1/D3/D4/D5 absence.

---

# 7. Routing to composite-zero machinery

Despite being locally residual, A51.2 shows that the branch is already a zero-composite relation:

```text
sum(A G L y_1 y_2)=0.
```

This suggests applying the same A47 strategy used for `k=1`:

```text
Z = A G L y_1 y_2,
```

then insert the outside two-atom block `c_1 c_2` or one of its atoms into a cut of `Z`.

## Lemma A51.9: if L is nonempty, the cut P=AG, Q=L y_1 y_2 avoids the single-atom Q2 boundary

Assume `L` is nonempty.  For the zero block

```text
Z=A G L y_1 y_2,
```

choose

```text
P=A G,
Q=L y_1 y_2.
```

Then

```text
|Q|=|L|+2 >= 3.
```

Therefore atom insertion into this cut avoids the Q2 single-atom boundary from A31--A33.

### Proof

Immediate from `|L|>=1`. ∎

### Consequence

When `L` is nonempty, inserting either `c_1` or `c_2` into the canonical cut routes to the atom-insertion descent framework, with only A34 recurrence remaining.

---

## Lemma A51.10: if L is empty, k=2 balanced D2 is already a lower-piece composite-zero branch

If `L` is empty, then `C=(c_1,c_2)` and balanced D2 gives

```text
sum(A G y_1 y_2)=0.
```

This is already a composite-zero branch with no remaining C-tail.

### Proof

Set `L=empty` in Lemma A51.2. ∎

---

# 8. Conditional reduction of k=2 balanced D2

## Proposition A51.11: k=2 balanced D2 reduces to composite-zero descent plus A34 recurrence

Assume balanced D2 with `k=m=2`.

By Lemma A51.2, it gives the zero composite

```text
Z=A G L y_1 y_2.
```

If `L` is empty, this is already a composite-zero branch.

If `L` is nonempty, choose the canonical cut

```text
P=A G,
Q=L y_1 y_2.
```

Then `|Q|>=3`, so atom insertion of `c_1` or `c_2` avoids the Q2 single-atom boundary.  The A31--A33 atom-insertion analysis routes all non-forbidden-hit obstructions to strict descent, equal-interval descent, zero collapse, or lower composite-zero branches.

Therefore the only non-descending obstruction left by this route is A34 forbidden-hit recurrence.

### Proof

Combine Lemmas A51.2, A51.9, A51.10, and the atom-insertion descent framework A31--A33. ∎

---

# 9. Consequence

The first proper balanced case `k=m=2` is not closed absolutely, but it is controlled modulo the same global recurrence theorem A34.

This suggests the general pattern:

```text
balanced D2 with k=m=q
  -> zero composite A G tail_q(C) prefix_q(Y)=0
  -> choose cut P=AG, Q=tail_q(C) prefix_q(Y)
  -> if Q has length >=2, atom insertion avoids the Q2 boundary
  -> controlled modulo A34.
```

This is exactly the generalization that should be proved next.

---

# 10. Target A52

Generalize A47 and A51 to all balanced D2 cases `k=m=q`.

Expected theorem:

> Balanced D2 for any `q>=1` gives a zero composite
>
> ```text
> A G tail_q(C) prefix_q(Y)=0.
> ```
>
> If the composite remainder after the canonical cut has length at least two, atom insertion avoids the Q2 single-atom boundary and is controlled by A31--A33 plus A34 recurrence.
>
> The only boundary is when that remainder has length one, which reduces to the atom-balanced case already handled by A47.

---

## Current status

Proved here:

1. exact algebra for `k=m=2`;
2. residual conditions in terms of complementary pair differences;
3. absence constraints from D1/D3/D4/D5;
4. pair reversal does not force local descent;
5. `k=2` balanced D2 gives zero composite `A G L y_1 y_2=0`;
6. canonical cut avoids Q2 single-atom boundary when `L` is nonempty;
7. conditional reduction to composite-zero descent plus A34 recurrence.

Not proved here:

1. A34 global recurrence theorem;
2. full balanced D2 theorem for all `k`;
3. endpoint avoidance theorem.
