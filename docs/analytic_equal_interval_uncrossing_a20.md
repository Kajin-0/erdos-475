# Analytic equal-interval uncrossing A20: geometry table and immediate collapses

This note continues from A19.

A19 compressed the remaining singleton-prefix residuals to equal-interval and signed-equal-interval traps.  This note develops the interval geometry of those traps.

The purpose is conservative: prove the endpoint-sharing and adjacent signed-interval collapses, and record the exact residual algebra for proper overlap, nesting, and separated cases.  This avoids a common false shortcut: equal intervals do not automatically produce a smaller zero-sum interval.

---

## Standing notation

Let

```text
R=(r_1,...,r_t)
```

be a Graham-valid ordering, with

```text
S_0=0,
S_i=r_1+...+r_i.
```

For `0 <= x < y <= t`, write

```text
I=(x,y],
sum(I)=S_y-S_x.
```

Recall the basic Graham-validity fact:

```text
if 1 <= u < v <= t, then S_u != S_v.
```

Thus no interior interval `(u,v]` with `u>=1` can have sum zero.

---

# 1. Equal-interval traps

An equal-interval trap has the form

```text
sum(x,y] = sum(u,v].
```

Equivalently,

```text
S_y-S_x = S_v-S_u.
```

---

## Lemma A20.1: shared left endpoint collapses

Assume

```text
x=u,
sum(x,y]=sum(x,v].
```

Then

```text
S_y=S_v.
```

If `y != v`, this contradicts Graham-validity.  Therefore in a valid residual case with shared left endpoint, one must have

```text
y=v,
```

so the two intervals are identical.

### Proof

Subtracting the equal sums gives `S_y=S_v`.  Since both `y` and `v` are nonzero endpoints of nonempty intervals, distinctness of nonempty partial sums forces `y=v`.  ∎

---

## Lemma A20.2: shared right endpoint collapses except for prefix-zero

Assume

```text
y=v,
sum(x,y]=sum(u,y].
```

Then

```text
S_x=S_u.
```

If `x,u >= 1` and `x != u`, this contradicts Graham-validity.  If exactly one of `x,u` is zero, then the equality says that the other endpoint is a prefix-zero index:

```text
S_w=0.
```

### Proof

Subtract the two equal sums to get `S_x=S_u`.  If both are nonzero partial-sum indices, Graham-validity forces equality of indices.  If one endpoint is `0`, then the equality says the other partial sum equals `S_0=0`, which is allowed by Graham's condition and is exactly the prefix-zero branch.  ∎

---

## Lemma A20.3: proper overlap creates equal outer pieces

Assume two intervals have proper overlap:

```text
x < u < y < v.
```

Decompose

```text
A=(x,u],
B=(u,y],
C=(y,v].
```

If

```text
sum(x,y]=sum(u,v],
```

then

```text
sum(A)=sum(C).
```

### Proof

The equality is

```text
sum(A)+sum(B)=sum(B)+sum(C).
```

Cancel `sum(B)` to obtain `sum(A)=sum(C)`.  ∎

### Status

Residual.  Proper overlap of equal intervals reduces to a shorter equal-interval trap on the two outer pieces, but those pieces are separated rather than contiguous.  This is an uncrossing reduction, not an immediate contradiction.

---

## Lemma A20.4: nested equal intervals create a two-piece zero complement

Assume

```text
x < u < v < y.
```

If

```text
sum(x,y]=sum(u,v],
```

then

```text
sum(x,u]+sum(v,y]=0.
```

### Proof

Decompose

```text
(x,y]=(x,u] union (u,v] union (v,y].
```

The equality says

```text
sum(x,u]+sum(u,v]+sum(v,y]=sum(u,v].
```

Cancel the middle term to get

```text
sum(x,u]+sum(v,y]=0.
```

∎

### Status

Residual two-piece zero branch.  If the two complement pieces can be made adjacent by a cyclic cut or block relocation, this becomes an ordinary zero-sum interval.  Otherwise it remains a signed/two-piece composite.

---

## Lemma A20.5: adjacent equal intervals give a midpoint relation, not a contradiction

Assume

```text
x < y = u < v
```

and

```text
sum(x,y]=sum(y,v].
```

Then

```text
2S_y=S_x+S_v.
```

### Proof

The equality is

```text
S_y-S_x=S_v-S_y.
```

Rearranging gives the claim.  ∎

### Status

Residual midpoint branch.  This may become useful over fields of odd characteristic, but it is not an immediate contradiction.

---

# 2. Signed-equal-interval traps

A signed-equal-interval trap has the form

```text
sum(x,y] = -sum(u,v].
```

Equivalently,

```text
sum(x,y]+sum(u,v]=0.
```

---

## Lemma A20.6: adjacent signed intervals collapse to zero-sum interval

Assume

```text
x < y = u < v
```

and

```text
sum(x,y] = -sum(y,v].
```

Then

```text
sum(x,v]=0.
```

If `x>=1`, this contradicts Graham-validity.  If `x=0`, this is a prefix-zero branch.

### Proof

Adding the two intervals gives

```text
sum(x,y]+sum(y,v]=sum(x,v]=0.
```

If `x>=1`, the zero interval is interior and contradicts Graham-validity.  If `x=0`, it is a prefix-zero interval and is allowed.  ∎

---

## Lemma A20.7: disjoint signed intervals produce a two-piece zero composite

Assume

```text
x < y < u < v
```

and

```text
sum(x,y] = -sum(u,v].
```

Then the two separated intervals form a zero-sum two-piece composite:

```text
sum(x,y]+sum(u,v]=0.
```

### Status

Residual.  This is not an ordinary zero-sum interval unless the gap `(y,u]` is moved away or the two pieces are made adjacent by a cyclic surgery.

---

## Lemma A20.8: overlapping signed intervals create an ordinary zero subinterval plus residual tails

Assume proper overlap

```text
x < u < y < v.
```

Decompose

```text
A=(x,u],
B=(u,y],
C=(y,v].
```

If

```text
sum(x,y] = -sum(u,v],
```

then

```text
sum(A)+2sum(B)+sum(C)=0.
```

### Proof

The signed equality is

```text
sum(A)+sum(B)=-(sum(B)+sum(C)).
```

Move all terms to one side:

```text
sum(A)+2sum(B)+sum(C)=0.
```

∎

### Status

Residual.  In odd characteristic this is a weighted relation, not a direct zero-sum interval.  In characteristic `2`, it reduces to `sum(A)+sum(C)=0`, but the problem is trivial for very small `p` and separately covered computationally.

---

## Lemma A20.9: nested signed intervals produce an ordinary decomposition equation

Assume

```text
x < u < v < y.
```

If

```text
sum(x,y] = -sum(u,v],
```

then

```text
sum(x,u]+2sum(u,v]+sum(v,y]=0.
```

### Proof

Decompose `(x,y]` into `(x,u]`, `(u,v]`, and `(v,y]`, then add `sum(u,v]` to both sides.  ∎

### Status

Residual weighted composite branch.

---

# 3. Application to same-atom landing equations

The residual singleton-prefix cases from A19 all have two landing equations for the same atom `b`:

```text
S_{h-1}+b=S_j,
S_u+b=S_v
```

or a signed version

```text
S_{h-1}+b=S_j,
S_v+b=S_u.
```

The first pair gives

```text
sum(h-1,j]=sum(u,v].
```

The signed pair gives

```text
sum(h-1,j]=-sum(u,v].
```

Thus the residual problem now has an interval geometry case split:

```text
1. shared endpoint collapse;
2. adjacent signed zero collapse;
3. proper overlap equal-outer-piece reduction;
4. nested two-piece zero composite;
5. adjacent equal midpoint branch;
6. separated equal/signed composite branch;
7. prefix-zero branch.
```

---

# 4. Immediate collapses available for A19 residuals

The following are now automatic checks for each residual row in A19.

## Shared left endpoint

If the local interval `(h-1,j]` and the residual interval `(u,v]` begin at the same index, then they must have the same right endpoint or contradict Graham-validity.

## Shared right endpoint

If they end at the same index, then either their left endpoints agree, or one left endpoint is `0` and the other is a prefix-zero branch, or there is an old Graham collision.

## Adjacent signed intervals

If the signed relation produces adjacent intervals, the union is zero-sum.  This is either an interior zero-sum contradiction or a prefix-zero branch.

These checks should be implemented in a small symbolic classifier in the next step.

---

# 5. Target A21: symbolic residual classifier

The next practical step is to implement a symbolic classifier for residual rows of A19.

Input:

```text
local interval:      (h-1,j]
residual interval:   (u,v]
relation sign:       +1 or -1
known inequalities:  branch-specific index constraints
```

Output one of:

```text
collapse: old Graham collision
collapse: prefix-zero
collapse: interior zero interval
reduction: shorter equal-interval trap
residual: nested two-piece zero composite
residual: adjacent midpoint branch
residual: separated composite
```

This will identify which residual cases truly need new mathematics and which are bookkeeping collapses.

---

## Current status

Proved here:

1. shared-left equal intervals collapse;
2. shared-right equal intervals collapse except prefix-zero;
3. proper-overlap equal intervals reduce to equal outer pieces;
4. nested equal intervals produce a two-piece zero complement;
5. adjacent signed intervals collapse to zero-sum interval;
6. signed overlap/nesting formulas are explicit.

Not proved here:

1. elimination of separated equal-interval composites;
2. elimination of midpoint branches;
3. elimination of nested two-piece zero composites;
4. endpoint avoidance theorem.
