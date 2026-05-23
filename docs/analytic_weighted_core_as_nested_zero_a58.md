# Analytic weighted core as nested zero-composite A58

This note continues from A56--A57.

A56 isolated the remaining genuinely weighted signed core:

```text
sum(A)+2sum(B)+sum(C)=0
```

where none of the transported-prefix, zero-block, adjacent-pair-zero, or equal-outer reductions applies.

This note records a sharper normal form:

```text
A+2B+C=0
```

is equivalent to a nested zero-composite relation

```text
sum(A B C)+sum(B)=0.
```

This does not close the branch, but it changes its interpretation.  The weighted core is not a completely new algebraic species; it is a zero-composite relation between a whole block and its middle subblock.

---

## Standing setup

Let a displayed consecutive segment be

```text
X A B C Y
```

with block sums

```text
a=sum(A),
b=sum(B),
c=sum(C).
```

The genuine weighted core is

```text
a+2b+c=0.
```

Assume the A56 easy reductions do not apply:

```text
b != 0,
a+b != 0,
b+c != 0,
a != c,
```

and no transported-prefix/tail rewrite is already available.

---

# 1. Nested zero-composite identity

## Lemma A58.1: weighted core equals whole-block plus middle-block zero

The relation

```text
a+2b+c=0
```

is equivalent to

```text
sum(A B C)+sum(B)=0.
```

### Proof

Since

```text
sum(A B C)=a+b+c,
```

we have

```text
sum(A B C)+sum(B)=a+b+c+b=a+2b+c.
```

Thus the two equations are identical.  ∎

### Interpretation

The weighted core is a nested zero-composite:

```text
outer block: A B C
inner block: B
```

with opposite sums:

```text
sum(A B C)=-sum(B).
```

---

# 2. Complement form

The same equation also gives

```text
a+c=-2b.
```

Since the field has odd characteristic, this can be written as

```text
b=-(a+c)/2.
```

This is a midpoint condition on block sums, not on partial-sum positions.

## Lemma A58.2: weighted core is a block-sum midpoint relation

Over odd prime fields,

```text
a+2b+c=0
```

is equivalent to

```text
b=-(a+c)/2.
```

### Proof

Rearrange and divide by `2`.  ∎

### Status

This midpoint form may be useful, but it does not by itself create a collision or descent.  The nested zero-composite form is more compatible with A28--A33.

---

# 3. Moving the middle block

A natural operation is to move `B` after `C`:

```text
X A B C Y -> X A C B Y.
```

This separates the middle block from its original position and makes the outer complement `A C` adjacent.

---

## Lemma A58.3: middle-block move partial-sum formula

Original segment:

```text
X A B C Y.
```

Moved segment:

```text
X A C B Y.
```

Relative to `x=sum(X)`, original displayed families are

```text
x+A_i,
x+a+B_j,
x+a+b+C_k,
x+a+b+c+Y_m.
```

Moved displayed families are

```text
x+A_i,
x+a+C_k,
x+a+c+B_j,
x+a+c+b+Y_m.
```

Thus:

1. the `A` family is unchanged;
2. the `C` family is translated by `-b` relative to its original position;
3. the `B` family is translated by `c` relative to its original position;
4. the post-segment `Y` family is unchanged because the total segment sum `a+b+c` is unchanged.

### Proof

Direct summation.  ∎

---

## Lemma A58.4: under the weighted core, the endpoint after `A C B` has total shift `-b`

The moved full segment `A C B` has sum

```text
a+c+b.
```

Under

```text
a+2b+c=0,
```

this equals

```text
-b.
```

Thus the moved segment endpoint is

```text
x-b,
```

not equal to the original base `x` unless `b=0`, which is excluded by the genuine-core assumptions.

### Proof

From `a+2b+c=0`, `a+c+b=-b`.  ∎

### Consequence

Unlike ordinary zero-block exposure, moving `B` after `C` does not immediately expose a zero block.  It changes the block endpoint by `-b`.

---

# 4. Exposing the nested zero relation

The nested relation is

```text
sum(A B C)+sum(B)=0.
```

To make this a standard zero-composite, one must place a copy of `B` outside `ABC`; but the ordering has only one copy of `B`.  Therefore this relation is not directly a disjoint two-piece zero composite.

However, it can still be attacked by cutting `B` and applying transported-prefix tests.

Let

```text
B=P R,
```

with sums

```text
p=sum(P),
r=sum(R),
b=p+r.
```

Then the weighted core becomes

```text
a+2p+2r+c=0.
```

Using A56.1/A56.2, if either complementary piece appears in a collision equation, the doubled term becomes removable.

---

## Lemma A58.5: every proper cut of B creates two potential transported-prefix reductions

For any proper cut

```text
B=P R,
```

the weighted core can be written as either

```text
[a+p] + [p+r+c] + r = 0
```

or

```text
[a+p+r] + [r+c] + p = 0.
```

Equivalently,

```text
sum(A P)+sum(P R C)+sum(R)=0,
```

and

```text
sum(A P R)+sum(R C)+sum(P)=0.
```

### Proof

Expand the first expression:

```text
(a+p)+(p+r+c)+r = a+2p+2r+c = a+2b+c.
```

The second expands similarly:

```text
(a+p+r)+(r+c)+p = a+2p+2r+c.
```

∎

### Interpretation

A cut of the doubled block `B` exposes hidden three-piece zero-composite structures.  These are not necessarily disjoint in the original order, but they are closer to the A28--A33 composite-zero framework than the raw weighted form.

---

# 5. Endpoint cut collapses

## Lemma A58.6: endpoint cuts recover the A56 easy reductions

If `P` is empty, Lemma A58.5 reduces to

```text
A + B C + B = 0,
```

which is the original nested zero relation.

If `R` is empty, it reduces to

```text
A B + B C = 0.
```

This is exactly the decomposition

```text
(A+B)+(B+C)=0.
```

If either `A+B=0` or `B+C=0`, A56.5 applies.

### Proof

Set `p=0` or `r=0` in Lemma A58.5.  ∎

---

# 6. Current status of genuine weighted core

A58 does not eliminate the genuine weighted core.  It proves:

1. the raw weighted relation is a nested zero-composite relation;
2. moving the middle block does not directly expose a zero block;
3. cutting the doubled block creates hidden three-piece zero identities;
4. endpoint/easy cases agree with A56 reductions.

The hard residual is now more precise:

```text
A+2B+C=0,
with B nonzero,
A+B nonzero,
B+C nonzero,
A != C,
no transported rewrite,
and no cut of B yet shown to force descent.
```

---

# 7. Target A59

A59 should test cuts of `B`.

For each proper cut

```text
B=P R,
```

analyze whether the hidden identities from Lemma A58.5 can be converted into:

```text
1. a smaller zero-composite branch;
2. a transported-prefix artifact;
3. a midpoint/equal-outer branch;
4. a forbidden recurrence controlled by A34.
```

A finite local search may also help:

```text
search for A,B,C over F_p satisfying genuine weighted core,
all A56 easy reductions absent,
and no proper cut of B producing an A58.5 descent.
```

If no such examples exist in small fields, the next analytic lemma is likely a cut-of-B descent theorem.

---

## Current status

Proved here:

1. weighted core equals nested zero-composite `ABC+B=0`;
2. weighted core equals block-sum midpoint relation over odd fields;
3. middle-block move formulas;
4. proper cuts of B expose hidden three-piece zero identities;
5. endpoint cuts recover A56 easy reductions.

Not proved here:

1. cut-of-B descent theorem;
2. genuine weighted core elimination;
3. A34 global recurrence theorem;
4. endpoint avoidance theorem.
