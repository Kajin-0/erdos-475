# Analytic two-piece zero standard form A28: relocation obstruction equations

This note continues from A26/A27.

A26 showed that two separated intervals with opposite sums can be made adjacent by moving the gap between them.  This note puts that operation into a standard form and records the exact collision/forbidden-hit equations that must occur if the relocation fails.

The point is to reduce the classes

```text
residual_two_piece_zero
residual_separated_signed
```

to the same style of explicit translated-prefix obstruction used earlier in A9/A14/A16.

This note does not prove that the relocation always succeeds.

---

## Standing notation

Let an ordering segment be decomposed as

```text
X A G C Y
```

where

```text
sum(A)+sum(C)=0.
```

Write

```text
x=sum(X),
a=sum(A),
g=sum(G),
c=sum(C)=-a.
```

Let internal prefix sums be:

```text
A_i = a_1+...+a_i,      1 <= i <= |A|,
G_j = g_1+...+g_j,      1 <= j <= |G|,
C_k = c_1+...+c_k,      1 <= k <= |C|,
Y_m = y_1+...+y_m.      1 <= m <= |Y|
```

The two-piece-zero relocation is

```text
X A G C Y  ->  X A C G Y.
```

After the move, `AC` is a contiguous zero-sum block.

---

## Lemma A28.1: partial-sum families before and after relocation

In the original ordering `XAGCY`, the displayed-region partial sums are

```text
x + A_i,
x + a + G_j,
x + a + g + C_k,
x + g + Y_m.
```

In the relocated ordering `XACGY`, the displayed-region partial sums are

```text
x + A_i,
x + a + C_k,
x + G_j,
x + g + Y_m.
```

Thus only the `C` and `G` internal families change:

```text
old C-family: x+a+g+C_k  ->  new C-family: x+a+C_k,
old G-family: x+a+G_j    ->  new G-family: x+G_j.
```

The `A` family and the post-region `Y` family are unchanged.

### Proof

Direct summation.  Since `a+c=0`, the total displayed segment has sum `g` both before and after relocation, so the `Y` family remains translated by `x+g`.  ∎

---

## Lemma A28.2: exact Graham-collision obstruction list

Assume the original ordering is Graham-valid.  Then the relocated ordering `XACGY` can fail Graham-validity only if one of the following equalities occurs.

### New C-family against unchanged families

```text
x+a+C_k = x+A_i,
x+a+C_k = x+g+Y_m.
```

Equivalently:

```text
C_k = A_i-a,
C_k = g-a+Y_m.
```

### New G-family against unchanged families

```text
x+G_j = x+A_i,
x+G_j = x+g+Y_m.
```

Equivalently:

```text
G_j = A_i,
G_j = g+Y_m.
```

### New C-family against new G-family

```text
x+a+C_k = x+G_j,
```

or

```text
G_j = a+C_k.
```

### Internal collisions inside new families

Internal collisions inside the new `C` family are impossible if the original `C` prefixes were distinct.  Internal collisions inside the new `G` family are impossible if the original `G` prefixes were distinct.  These distinctness conditions follow from Graham-validity of the original ordering unless the relevant block begins at the basepoint and hits zero; any such exception is a prefix-zero branch.

### Proof

By Lemma A28.1, only the `C` and `G` families change.  The original unchanged families were collision-free among themselves.  Therefore every new collision must involve at least one changed family.  Listing all pairings gives the displayed equations.  ∎

---

## Lemma A28.3: exact forbidden-hit obstruction list

Let `f` be a forbidden value.  Suppose every unchanged family value avoids `f` except the known original first hit if it lies outside the moved families.

Then the relocated ordering `XACGY` has a forbidden hit only if one of the changed-family equations holds:

```text
x+a+C_k=f,
x+G_j=f.
```

Equivalently:

```text
C_k=f-x-a,
G_j=f-x.
```

### Proof

By Lemma A28.1, unchanged families retain their old values.  Thus only the new `C` and `G` families can create a new forbidden hit.  ∎

---

## Lemma A28.4: exposed zero-block endpoint collision is automatic

In the relocated ordering `XACGY`, the block `AC` has total sum zero.  Therefore the running sum after `A` and after `AC` is the same:

```text
x+a = x+a+c = x.
```

More precisely, the partial sum at the end of `AC` equals the running value before `A`:

```text
x+a+c=x.
```

If the position before `A` corresponds to a nonempty partial sum in the ordering, then the relocation has an exposed Graham collision.  If the position before `A` is the basepoint, then the exposed zero block is a prefix-zero branch.

### Proof

Since `c=-a`, `a+c=0`.  The rest is the standard zero-sum interval criterion.  ∎

### Interpretation

The raw move `XAGCY -> XACGY` usually creates a zero-sum block and therefore is not itself a final repair.  Its value is that it converts a separated two-piece composite into a standard exposed zero-block obstruction.  One must then apply a zero-block breaking move of the A9 type.

---

# 1. Zero-block breaking after contiguization

After relocation, the local segment has the form

```text
X Z G Y
```

where

```text
Z = A C,
sum(Z)=0.
```

A9 already gives the general relocation formula for a zero block `Z`.  Here is the specialized target.

## Target A28.5: two-piece-zero break lemma

Let `Z=AC` be the zero block produced from a two-piece-zero composite.  Then either:

```text
1. a proper internal rotation of Z destroys the zero-block collision without creating another collision or forbidden hit;
2. every such rotation is blocked by translated internal prefix equations;
3. those translated prefix equations reduce to a shorter equal-interval trap or a local pair trap.
```

This target is not proved in this note.  The contribution of this note is the exact standard form and failure equations needed to attack it.

---

# 2. Relation to residual classes

## residual_two_piece_zero

A nested equal-interval residual from A20 gives

```text
sum(A)+sum(C)=0
```

for the complement pieces around the nested interval.  A28 applies directly.

## residual_separated_signed

A separated signed residual gives

```text
sum(A)=-sum(C),
```

which is exactly

```text
sum(A)+sum(C)=0.
```

A28 applies directly.

Thus both classes reduce to the same standard form.

---

# 3. Current status

Proved here:

1. exact partial-sum families before/after two-piece-zero gap relocation;
2. exact Graham-collision obstruction equations;
3. exact forbidden-hit obstruction equations;
4. exposed zero-block endpoint collision after contiguization;
5. reduction of `residual_two_piece_zero` and `residual_separated_signed` to a common standard form.

Not proved here:

1. zero-block breaking always succeeds;
2. all translated-prefix obstruction equations reduce to known branches;
3. endpoint avoidance theorem.
