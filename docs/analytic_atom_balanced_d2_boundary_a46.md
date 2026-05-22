# Analytic atom-balanced D2 boundary A46

This note continues from A45.

A45 showed that the stronger A44 local model still has balanced D2 survivors, and the first survivors are dominated by the atom-balanced boundary

```text
k=m=1.
```

In this boundary, the A41 intermediate-prefix descent mechanisms cannot apply because there are no intermediate paired-prefix values.

This note derives the exact atom-level structure of this branch.

---

## Standing setup

Let a displayed segment be

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
C = c L,
Y = y N,
```

where `c` and `y` are the first atoms of `C` and `Y`, and `L` is the tail of `C` after its first atom.

Thus

```text
sum(C)=c+sum(L)=a.
```

The atom-balanced D2 boundary is

```text
c = 2a + g + y.
```

Equivalently,

```text
c-y = 2a+g.
```

---

# 1. Zero-composite form

## Lemma A46.1: atom-balanced D2 is equivalent to a zero composite `A G L y`

The equation

```text
c = 2a+g+y
```

is equivalent to

```text
sum(A G L y)=0.
```

### Proof

Since `c+sum(L)=a`, we have

```text
sum(L)=a-c.
```

Therefore

```text
sum(A G L y)=a+g+(a-c)+y=2a+g+y-c.
```

This is zero exactly when `c=2a+g+y`. ∎

### Interpretation

The atom-balanced D2 boundary is not merely an atom equation.  It is a composite zero relation

```text
A + G + tail(C) + y = 0.
```

It has the same support length as `A G C` because it replaces the atom `c` by the atom `y`.

---

# 2. Pair-difference form

## Lemma A46.2: atom-balanced D2 is a pair-difference trap

The boundary equation is equivalent to

```text
c-y = sum(A G C).
```

### Proof

The total sum of `A G C` is

```text
sum(A)+sum(G)+sum(C)=a+g+a=2a+g.
```

D2 says `c-y=2a+g`. ∎

### Interpretation

The pair `(c,y)` measures exactly the full displayed-block sum of `A G C`.

This is analogous to the Q2 pair-difference branch from A33, but with the pair difference equal to a larger displayed-block sum rather than a prefix of `Y`.

---

# 3. Direct atom swap between c and y

The natural atom-level move is to swap the first atom of `C` with the first atom of `Y`:

```text
X A G c L y N  ->  X A G y L c N.
```

This replaces the original block `A G C = A G c L` by `A G y L`.

---

## Lemma A46.3: direct c/y swap endpoint formula

Let

```text
x=sum(X),
H=A G,
h=sum(H)=a+g.
```

Original displayed partial sums around `c L y` include

```text
x+h+c,
x+h+c+L_r,
x+2a+g,
x+2a+g+y.
```

After the swap

```text
H c L y -> H y L c,
```

the corresponding partial sums are

```text
x+h+y,
x+h+y+L_r,
x+h+y+sum(L)+c,
x+h+y+sum(L)+c+N_s.
```

Since `sum(L)=a-c`, the endpoint after `H y L c` is

```text
x+h+y+a = x+2a+g+y.
```

Thus the final endpoint of the displayed block is unchanged, but the internal `c/L/y` levels are shifted.

### Proof

Direct summation. ∎

---

## Lemma A46.4: under atom-balanced D2, the endpoint after `H y L` equals the pre-`H` basepoint

In the swapped order, the endpoint after `H y L` is

```text
x+h+y+sum(L).
```

Using `h=a+g` and `sum(L)=a-c`, this is

```text
x+2a+g+y-c.
```

Under atom-balanced D2, `c=2a+g+y`, so this endpoint equals

```text
x.
```

### Proof

Substitute the D2 equation into the displayed expression. ∎

### Consequence

The direct `c/y` swap exposes a zero block

```text
A G y L
```

because

```text
sum(A G y L)=0.
```

This is exactly Lemma A46.1 with the pieces made contiguous in the order `A G y L`.

Thus the naive atom swap does not repair the obstruction; it contiguizes the balanced D2 composite zero.

---

# 4. Insertion form

Instead of swapping `c` and `y`, insert `y` before `c`:

```text
X A G c L y N -> X A G y c L N.
```

This tests whether the pair can break the balanced zero composite without moving the tail `L` first.

## Lemma A46.5: insertion of y before c produces a changed endpoint `x+a+g+y`

In the move

```text
A G c L y -> A G y c L,
```

the endpoint immediately after `A G y` is

```text
x+a+g+y.
```

Under D2, since `c-y=2a+g`, this value can be rewritten as

```text
x+c-a.
```

### Proof

The endpoint after `A G y` is direct.  From `c-y=2a+g`, one has `a+g+y=c-a`. ∎

### Status

This is an atom landing equation.  It does not collapse locally without additional information about whether `x+c-a` is an old partial sum or forbidden value.

---

# 5. Collision routes under c/y insertion

The insertion move changes only the translated families associated with `y`, `c`, and `L`.  The important first obstruction is whether the new endpoint after `A G y` collides with an old displayed family.

## Lemma A46.6: first insertion collision routes to an equal-interval or pair trap

If

```text
x+a+g+y = x+A_i,
```

then

```text
A_i = a+g+y = c-a.
```

Equivalently,

```text
A_i+a = c.
```

This is an atom-plus-prefix landing relation.

If

```text
x+a+g+y = x+a+G_j,
```

then

```text
G_j = g+y,
```

so

```text
tail_j(G)+y=0.
```

This is a two-piece zero composite, unless `j=|G|`, in which case it gives `y=0`, impossible.

If

```text
x+a+g+y = x+a+g+c+L_r,
```

then

```text
y=c+L_r,
```

or

```text
y-c=L_r.
```

Using `c-y=2a+g`, this gives

```text
L_r=-(2a+g),
```

which is a signed interval relation against the total displayed sum.

### Proof

Each statement follows by subtracting the common base translation and using D2 where indicated. ∎

---

# 6. Boundary observation: L empty

If `L` is empty, then `C=(c)` and `sum(C)=a` gives

```text
c=a.
```

D2 becomes

```text
a=2a+g+y,
```

so

```text
a+g+y=0.
```

That is,

```text
sum(A G y)=0.
```

## Lemma A46.7: if `C` has length one, atom-balanced D2 is a two-piece/three-piece zero branch

When `C=(c)` is a single atom, atom-balanced D2 reduces to

```text
sum(A G y)=0.
```

Thus it is an exposed composite-zero branch, not a new balanced-transfer object.

### Proof

As above. ∎

---

# 7. Current status of atom-balanced D2

The atom-balanced D2 boundary has been reduced to the following facts:

1. It is equivalent to the zero composite

```text
A G tail(C) y = 0.
```

2. It is also equivalent to the pair-difference relation

```text
c-y=sum(A G C).
```

3. Swapping `c` and `y` contiguizes the zero composite rather than repairing it.

4. Inserting `y` before `c` creates atom/prefix landing equations that route to:

```text
two-piece zero,
equal-interval / atom-prefix landing,
signed total-sum interval relation,
forbidden-hit recurrence if the new landing is f.
```

5. If `C` has length one, the branch is already a composite-zero branch.

---

# 8. Consequence

A46 does not close atom-balanced D2 locally.

It shows that the `k=m=1` survivors found in A44 are real local obstructions: they are not artifacts of missing D1/D3/D4/D5 checks.  They require either:

```text
1. composite-zero descent using A28--A33;
2. global recurrence control using A34;
3. compatibility with the original first-hit/cyclic obstruction package.
```

---

# 9. Target A47

A47 should integrate the atom-balanced D2 composite

```text
A G tail(C) y = 0
```

with the zero-composite machinery from A28--A33.

The target theorem should be:

> Atom-balanced D2 either produces a strict composite-zero descent after one insertion/contiguization step, or produces a forbidden recurrence controlled by A34.

The key object is now not the pair `(c,y)` alone, but the zero composite:

```text
A, G, tail(C), y.
```

---

## Current status

Proved here:

1. atom-balanced D2 equivalent to `A G tail(C) y=0`;
2. atom-balanced D2 equivalent to `c-y=sum(A G C)`;
3. direct `c/y` swap contiguizes the zero composite;
4. insertion of `y` before `c` routes first collisions to known interval/composite types;
5. `|C|=1` boundary is already composite-zero.

Not proved here:

1. full atom-balanced D2 elimination;
2. global recurrence descent;
3. endpoint avoidance theorem.
