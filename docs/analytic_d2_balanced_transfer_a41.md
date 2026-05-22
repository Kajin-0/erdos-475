# Analytic D2 balanced-transfer branch A41

This note continues from A40.

A40 showed that the D2 composite-zero branch from separated equal-interval surgery is strict support descent exactly when

```text
m<k.
```

The first non-descending case is the balanced-transfer boundary

```text
m=k.
```

This note analyzes that boundary.  It does not eliminate it completely.  It rewrites it in a form suitable for prefix-by-prefix comparison and isolates the next required lemma.

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
C=K L,
Y=M N,
```

where

```text
K=prefix_k(C),
L=tail_k(C),
M=prefix_m(Y).
```

The D2 equation is

```text
C_k=2a+g+Y_m.
```

A38 showed this is equivalent to

```text
sum(A G)+sum(L)+sum(M)=0.
```

A40 showed support is unchanged exactly when

```text
m=k.
```

In this note assume

```text
m=k.
```

---

# 1. Balanced-transfer identity

The original displayed support `A G C` is

```text
A G K L.
```

The D2 composite-zero support is

```text
A G L M.
```

Thus the balanced case replaces the `C`-prefix `K` by an equal-length `Y`-prefix `M`.

---

## Lemma A41.1: balanced D2 is an equal-length transfer identity

Under `m=k`, D2 is equivalent to

```text
sum(A G L M)=0
```

where `|M|=|K|`.

Equivalently,

```text
sum(A G C) - sum(K) + sum(M)=0.
```

Since

```text
sum(A G C)=2a+g,
```

this is the same as

```text
2a+g - C_k + Y_k=0,
```

or

```text
C_k=2a+g+Y_k.
```

### Proof

Immediate from A38/A40 with `m=k`.  ∎

---

# 2. Prefix comparison between K and M

Let

```text
K=(c_1,...,c_k),
M=(y_1,...,y_k).
```

Define paired prefix differences

```text
D_r = (c_1+...+c_r) - (y_1+...+y_r),      1 <= r <= k.
```

Also define

```text
D_0=0.
```

The total difference is

```text
D_k=sum(K)-sum(M)=C_k-Y_k.
```

By D2,

```text
D_k=2a+g.
```

---

## Lemma A41.2: if an intermediate paired prefix difference equals `2a+g`, then balanced D2 shortens

Suppose there exists `r<k` such that

```text
D_r=2a+g.
```

Then

```text
sum(A G C) - D_r = 0.
```

Equivalently,

```text
sum(A G C) - sum(K_r) + sum(M_r)=0.
```

This gives the same D2-type zero composite but with the shorter equal-length transfer length `r<k`.

### Proof

Since `sum(A G C)=2a+g`, the condition `D_r=2a+g` is exactly

```text
sum(A G C)-D_r=0.
```

Expanding `D_r=sum(K_r)-sum(M_r)` gives the displayed relation.  ∎

### Status

This is strict descent in transfer length from `k` to `r`.

---

## Lemma A41.3: if an intermediate paired prefix difference is zero, then K and M have an equal-prefix relation

Suppose there exists `0<r<k` such that

```text
D_r=0.
```

Then

```text
sum(K_r)=sum(M_r).
```

This is a separated equal-interval relation with support length `2r`, strictly smaller than the balanced transfer support length `2k`.

### Proof

`D_r=0` is the equality of the paired prefixes.  Since `r<k`, the support is strictly smaller.  ∎

---

## Lemma A41.4: if no intermediate paired prefix difference is `0` or `2a+g`, the branch is a strict avoidance problem on the difference walk

If for every `0<r<k`,

```text
D_r notin {0, 2a+g},
```

then the paired-difference walk

```text
D_0,D_1,...,D_k
```

starts at `0`, ends at `2a+g`, and avoids both endpoint values at all intermediate times.

### Proof

This is a restatement of the assumptions and the identity `D_k=2a+g`.  ∎

### Interpretation

This residual branch is not an ordinary interval obstruction.  It is a paired-prefix path from `0` to `2a+g` avoiding both endpoints internally.

The natural next move is to compare the first step or last step of this walk.  A collision in the difference walk gives either:

```text
1. equal-sum subblocks of K and M;
2. a shorter balanced transfer;
3. a pair trap between corresponding atoms c_r and y_r.
```

---

# 3. Difference-walk collision analysis

The paired difference increments are

```text
D_r-D_{r-1}=c_r-y_r.
```

If two difference-walk values coincide:

```text
D_r=D_s,
0<=r<s<=k,
```

then

```text
sum(c_{r+1},...,c_s)=sum(y_{r+1},...,y_s).
```

---

## Lemma A41.5: repeated difference-walk values give a smaller separated equal interval

If

```text
D_r=D_s,
0<=r<s<=k,
```

then the subblocks

```text
K_{r+1:s},
M_{r+1:s}
```

have equal sum.

If `s-r<k`, this is a strictly smaller separated equal-interval branch.

### Proof

Subtract:

```text
D_s-D_r=0.
```

By definition of `D`, this is

```text
sum(c_{r+1},...,c_s)-sum(y_{r+1},...,y_s)=0.
```

Thus the two subblocks have equal sum.  If `s-r<k`, the support is smaller than the full transfer pair.  ∎

---

## Lemma A41.6: injective difference walk has length constraint

If the difference-walk values

```text
D_0,D_1,...,D_k
```

are pairwise distinct in `F_p`, then

```text
k+1 <= p.
```

### Proof

There are `k+1` pairwise distinct values in a field of size `p`.  ∎

### Status

This is weak for the target theorem, but it shows that very long balanced-transfer branches force a repeated difference value and hence a smaller separated equal interval.

---

# 4. Atom-pair boundary inside the difference walk

If an increment vanishes,

```text
c_r-y_r=0,
```

then

```text
c_r=y_r.
```

Since the original ordering is a set ordering with distinct atoms, this is impossible if `K` and `M` are disjoint subblocks of the same set.

## Lemma A41.7: zero increment is impossible for disjoint K and M

If `K` and `M` are disjoint blocks of a set with distinct elements, then

```text
D_r-D_{r-1}=0
```

is impossible.

### Proof

The increment is `c_r-y_r`.  If it is zero, then `c_r=y_r`, contradicting distinctness of atoms in disjoint positions.  ∎

---

# 5. Current status of balanced D2

The balanced D2 branch is now reduced to a paired-difference walk problem.

Closed/descending subcases:

```text
1. some intermediate D_r=0        -> smaller separated equal interval;
2. some intermediate D_r=2a+g    -> shorter balanced transfer;
3. repeated D_r=D_s              -> smaller separated equal interval;
4. zero increment                -> impossible by atom distinctness.
```

Residual subcase:

```text
D_0,D_1,...,D_k are pairwise distinct,
D_r avoids 0 and 2a+g for 0<r<k,
all increments are nonzero.
```

This is a genuine path-avoidance object.

---

# 6. Target A42

A42 should attack the residual injective difference-walk case.

Possible approaches:

```text
1. Use reversal of one of K or M to force a repeated difference value.
2. Use cyclic shifting of M relative to K and average over k alignments.
3. Use additive-combinatorial bounds: the difference walk of paired atoms cannot avoid both endpoints under all alignments.
4. Show that if every alignment is injective/endpoint-avoiding, then the K/M atoms form a rigid arithmetic progression, which creates a pair trap elsewhere.
```

The most concrete next step is to implement a finite symbolic/field search for small `k,p` to see which paired-difference walks can satisfy the residual conditions.

---

## Current status

Proved here:

1. balanced D2 is an equal-length transfer identity;
2. intermediate `D_r=2a+g` gives shorter balanced transfer;
3. intermediate `D_r=0` gives smaller separated equal interval;
4. repeated difference-walk values give smaller separated equal interval;
5. zero increments are impossible for disjoint atom blocks.

Not proved here:

1. injective endpoint-avoiding difference-walk elimination;
2. long-prefix recurrence elimination;
3. endpoint avoidance theorem.
