# Analytic atom-balanced D2 zero-composite integration A47

This note continues from A46.

A46 showed that the atom-balanced D2 boundary

```text
k=m=1,
C=cL,
Y=yN,
c=2a+g+y
```

is equivalent to the zero-composite relation

```text
sum(A G L y)=0,
```

where

```text
sum(A)=sum(C)=a,
sum(G)=g,
sum(L)=a-c.
```

This note integrates that relation with the zero-composite machinery from A28--A33.

The result is conservative: it gives exact standard forms and descent conditions, but it does not claim full closure.

---

## Standing setup

Let a displayed segment be

```text
X A G c L y N
```

with

```text
C=cL,
Y=yN,
sum(A)=sum(C)=a,
sum(G)=g.
```

The atom-balanced D2 equation is

```text
c=2a+g+y.
```

Equivalently,

```text
sum(A G L y)=0.
```

Write

```text
Z = A G L y.
```

Then `Z` is a multi-piece zero composite whose pieces are already almost contiguous except that the atom `c` separates `G` from `L`, and the atom `y` lies after `L`.

In the original segment the support order is

```text
A G c L y.
```

The zero-composite order ignoring the blocker atom `c` is

```text
A G L y.
```

---

# 1. Contiguization by moving c to the right

The direct move from A46 was

```text
A G c L y -> A G y L c.
```

This made `A G y L` contiguous and zero.  A slightly more canonical zero-composite contiguization is

```text
A G c L y -> A G L y c.
```

This moves the separating atom `c` after the zero composite.

---

## Lemma A47.1: moving c after L y exposes the zero block A G L y

Under atom-balanced D2, the block move

```text
X A G c L y N -> X A G L y c N
```

makes

```text
A G L y
```

contiguous and zero-sum.

### Proof

By A46.1,

```text
sum(A G L y)=0.
```

After the move, those pieces are adjacent in exactly the order `A G L y`.  ∎

---

## Lemma A47.2: c-contiguization partial-sum formula

Let

```text
h=sum(A G)=a+g,
ell=sum(L)=a-c.
```

Original segment:

```text
A G c L y N.
```

Moved segment:

```text
A G L y c N.
```

Relative to the base value `x=sum(X)`, the changed internal families are:

Original:

```text
x+h+c,
x+h+c+L_r,
x+h+c+ell+y,
x+h+c+ell+y+N_s.
```

Moved:

```text
x+h+L_r,
x+h+ell+y,
x,
x+c+N_s.
```

More explicitly:

- the `L` family is translated by `-c` relative to its original position;
- the endpoint after `A G L y` is `x` because `A G L y` is zero;
- the post-`c` `N` family is translated by `-sum(A G L y)=0` relative to the displayed endpoint but by a different local route.

### Proof

Original values after `AGcL_r` are `x+h+c+L_r`.  After moving `c` right, values after `AGL_r` are `x+h+L_r`, a translation by `-c`.

The endpoint after `AGLy` is

```text
x+h+ell+y.
```

Using `ell=a-c` and `c=2a+g+y`, this is

```text
x+(a+g)+(a-c)+y=x+2a+g+y-c=x.
```

The remaining formulas are direct.  ∎

---

## Lemma A47.3: raw contiguization necessarily exposes a zero-block endpoint collision

If the position before `A` corresponds to a nonempty partial sum, the moved ordering

```text
X A G L y c N
```

has a Graham collision between the partial sum before `A` and the partial sum after `A G L y`.

If the position before `A` is the basepoint, it is a prefix-zero branch.

### Proof

The block `A G L y` has total zero by Lemma A47.1.  This is exactly the zero-block endpoint collision criterion from A29.1.  ∎

### Consequence

As in A28/A29, contiguization is diagnostic, not a repair.  The exposed zero block must be broken by inserting `c` or another outside atom/block into its interior.

---

# 2. Breaking the exposed atom-balanced zero block

After contiguization, the standard local form is

```text
X A G L y c N
```

with zero block

```text
Z=A G L y.
```

The adjacent outside atom is `c`.  The standard A29 insertion move inserts `c` into the zero block.

There are several insertion positions.  The most natural one is between `G` and `L`, because that reverses the original separation:

```text
A G L y c -> A G c L y.
```

But this is just the original order.  Therefore the useful insertions are the other cuts:

```text
A c G L y,
A G L c y,
A G L y  c  (no break; c outside),
A G y c L,
...
```

The next lemma records the generic insertion criterion.

---

## Lemma A47.4: inserting c into a zero block breaks the endpoint collision iff the inserted prefix before the remainder has nonzero sum

Let a zero block decompose as

```text
Z=P Q,
sum(P)+sum(Q)=0.
```

Insert an outside atom `c` between `P` and `Q`:

```text
P Q c -> P c Q.
```

Then the endpoint after `P c Q` has value shifted by `c` relative to the endpoint before `P`.  Since `c != 0`, the old zero-block endpoint collision is broken.

### Proof

The block `P c Q` has sum

```text
sum(P)+c+sum(Q)=c.
```

Thus its endpoint differs from its starting value by `c`, nonzero.  ∎

### Note

This is the atom version of A29.3.

---

# 3. Generic obstruction equations for inserting c

Let

```text
Z=P Q,
sum(P)=p,
sum(Q)=-p.
```

Insert `c`:

```text
X P Q c N -> X P c Q N.
```

A29.6 applies with `q=c`.  The changed partial sums are

```text
x+p+c,
x+p+c+Q_j.
```

The collision equations are:

```text
c=P_i-p,
c=N_m-p,
Q_j=P_i-p-c,
Q_j=N_m-p,
Q_j=0.
```

The forbidden-hit equations are:

```text
x+p+c=f,
x+p+c+Q_j=f.
```

---

## Lemma A47.5: every c-insertion obstruction routes to known classes

For the atom-balanced D2 zero block `Z=A G L y`, any insertion of `c` into a cut `Z=P Q` has obstruction equations that route to:

```text
two-piece zero,
three-piece zero,
equal-interval / prefix-trap,
zero-prefix or interior-zero,
forbidden recurrence.
```

### Proof

This is A30 applied to the zero block `Z=P Q` and inserted atom `c`.  The identities are independent of the internal names of `P` and `Q`.  ∎

---

# 4. Descent condition for c-insertion

A31 gives descent for most atom-insertion branches.  Applied here, the main descent branch is:

```text
c + tail(P) = 0
```

or a smaller equal-prefix obstruction.

## Lemma A47.6: a c-insertion obstruction is strict support descent unless it falls into the A31 boundary classes

For any proper cut `Z=P Q`, insertion of `c` into `P|Q` is controlled by A31:

- Q1 gives strict support descent;
- Q5 collapses to zero-prefix/interior-zero;
- Q4 routes to equal-interval descent or zero collapse;
- Q2 descends unless the second piece has length one;
- Q3 non-descent forces the A32 atom-identification boundary;
- forbidden hits are A34 recurrence branches.

Thus the only non-descending cases are precisely the A31/A32/A33 boundary and recurrence cases.

### Proof

Substitute the zero block `Z=P Q` and inserted atom `c` into the A31--A33 analysis.  ∎

---

# 5. Choosing a cut in Z

The remaining question is whether at least one useful cut `Z=P Q` avoids the A31/A32 boundary cases.

The zero block is

```text
Z=A G L y.
```

Canonical cuts are:

```text
P=A,          Q=G L y;
P=A G,        Q=L y;
P=A G L,      Q=y.
```

The last cut has `|Q|=1`, exactly the Q2 boundary type.  The earlier cuts often have `|Q|>1`, unless `G L y` or `L y` is a single atom.

---

## Lemma A47.7: if `|L|>=1`, the cut `P=A G`, `Q=L y` avoids the Q2 single-atom boundary

Assume `L` is nonempty.  For the cut

```text
P=A G,
Q=L y,
```

one has

```text
|Q|=|L|+1 >= 2.
```

Therefore the Q2 atom-insertion branch for this cut is a strict support descent by A31.4, not the `|B|=1` boundary.

### Proof

Immediate from `|L|>=1`.  ∎

### Consequence

The problematic atom-balanced D2 cases with `|C|>=2` have a canonical cut avoiding the Q2 single-atom boundary.  This is exactly the case seen in the A44 survivor examples, where `C=cL` and `L` is nonempty.

---

## Lemma A47.8: if `L` is empty, atom-balanced D2 is already a lower-piece composite-zero branch

If `L` is empty, then A46.7 gives

```text
sum(A G y)=0.
```

This is a three-piece or two-piece zero composite depending on whether `A,G` are treated separately or merged.  It is not a balanced-transfer obstruction.

### Proof

This is A46.7.  ∎

---

# 6. Main conditional reduction

## Proposition A47.9: atom-balanced D2 reduces to atom-insertion descent plus A34 recurrence

Assume atom-balanced D2 with `C=cL`.

If `L` is empty, the branch is already composite-zero by Lemma A47.8.

If `L` is nonempty, expose the zero block

```text
Z=A G L y
```

and choose the cut

```text
P=A G,
Q=L y.
```

Insert `c` between `P` and `Q`.  Then all non-forbidden-hit obstruction branches are controlled by A31--A33, and the Q2 single-atom boundary is avoided by Lemma A47.7.

Therefore the only remaining non-descending obstruction is a forbidden-hit recurrence branch governed by the global A34 measure.

### Proof

The zero block exists by A46.1.  The cut has `|Q|>=2` by Lemma A47.7.  A31--A33 classify all atom-insertion obstructions.  With the Q2 single-atom boundary excluded, the remaining non-descending branches are the recurrence branches H1/H2 and any global measure-tie cases already isolated in A34.  ∎

---

# 7. Consequence

Atom-balanced D2 is no longer a purely local hard residual.  It is reduced to:

```text
1. composite-zero descent via A31--A33;
2. forbidden-hit recurrence controlled by A34.
```

This matches the desired target from A46.

The proof still depends on the open global recurrence theorem A34.R.

---

# 8. Target A48

The next useful step is to update the branch-status map:

```text
A45/A46 atom-balanced D2 boundary
```

should move from `hard local residual` to:

```text
controlled modulo A34 recurrence.
```

Then the remaining major hard branches are:

```text
1. global recurrence descent A34.R;
2. proper balanced D2 with k>=2 under stronger global constraints;
3. gap-after move obstructions;
4. weighted signed overlap/nesting not already routed to composite zero.
```

---

## Current status

Proved here:

1. canonical contiguization of atom-balanced D2 zero composite;
2. exposed zero-block endpoint collision;
3. insertion of `c` into a cut of the zero block routes to A30/A31 classes;
4. canonical cut `P=AG`, `Q=Ly` avoids Q2 single-atom boundary when `L` is nonempty;
5. atom-balanced D2 reduces to composite-zero descent plus A34 recurrence.

Not proved here:

1. A34 global recurrence theorem;
2. complete endpoint avoidance theorem.
