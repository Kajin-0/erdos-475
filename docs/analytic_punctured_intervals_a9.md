# Analytic punctured intervals A9: contiguizing the local obstruction

This note continues the endpoint-avoidance proof program after A5--A8.

The main point is structural: the local right-swap obstruction is not merely an arbitrary collision.  After the blocked adjacent swap, the obstruction becomes a **contiguous zero-sum block**.  This explains why the swap fails and gives the next object to attack: break, rotate, or relocate that zero-sum block without recreating the forbidden hit.

## Standing setup

Let `p` be prime.  Let

```text
A subset F_p^*
```

and let

```text
f in F_p,    f != sigma(A).
```

Assume single-forbidden endpoint avoidance fails for `(A,f)`.

Choose a Graham-valid ordering

```text
R = (r_1, ..., r_t)
```

whose unique forbidden hit occurs as early as possible:

```text
S_h=f,
```

where

```text
S_0=0,
S_i=r_1+...+r_i,
sigma=S_t.
```

Since `f != sigma`, one has `h<t`.

Write

```text
a = r_h,
b = r_{h+1},
P = S_{h-1}.
```

Then

```text
P+a=f.
```

The right-adjacent swap of `a,b` is blocked.  Hence there exists `j != h` such that

```text
P+b = S_j.
```

Let `R^swap` be the adjacent-swapped sequence

```text
(r_1, ..., r_{h-1}, b, a, r_{h+2}, ..., r_t).
```

Its partial sums are the same as those of `R`, except at index `h`, where the value is `P+b=S_j`.

Thus `R^swap` has at least the collision

```text
S_h(R^swap)=S_j(R^swap).
```

---

## 1. Ordinary interval and punctured interval notation

For indices `u < v`, write

```text
R(u,v] = (r_{u+1}, ..., r_v),
sum_R(u,v] = S_v-S_u.
```

The local obstruction equation

```text
P+b = S_j
```

can be written as

```text
S_{h-1}+b=S_j.
```

This has different interval interpretations depending on whether `j<h` or `j>h`.

---

## Lemma A9.1: local obstruction as an ordinary interval with one distinguished atom

### Forward case

If `j>h`, then

```text
sum_R(h-1,j] = b.
```

Equivalently, the ordinary interval

```text
(r_h,r_{h+1},...,r_j) = (a,b,r_{h+2},...,r_j)
```

has total sum `b`; after deleting the distinguished atom `b=r_{h+1}`, the remaining punctured interval has sum zero:

```text
a+r_{h+2}+...+r_j=0.
```

### Backward case

If `j<h`, then

```text
sum_R(j,h-1] = -b.
```

Equivalently,

```text
r_{j+1}+...+r_{h-1}+b=0.
```

Also the larger ordinary interval

```text
R(j,h+1]=(r_{j+1},...,r_{h-1},a,b)
```

has total sum `a`.

### Proof

Forward case:

From `S_{h-1}+b=S_j`,

```text
S_j-S_{h-1}=b,
```

which is exactly `sum_R(h-1,j]=b`.  Expanding the interval gives

```text
a+b+r_{h+2}+...+r_j=b,
```

hence

```text
a+r_{h+2}+...+r_j=0.
```

Backward case:

From `S_{h-1}+b=S_j`,

```text
S_{h-1}-S_j=-b,
```

which is

```text
r_{j+1}+...+r_{h-1}=-b.
```

Adding `b` gives the punctured zero-sum relation.  Adding `a+b` instead gives

```text
r_{j+1}+...+r_{h-1}+a+b=a.
```

∎

---

## Lemma A9.2: the blocked adjacent swap contiguizes the zero-sum relation

In `R^swap`, the local obstruction collision is realized by a contiguous zero-sum block.

### Forward case `j>h`

The block

```text
(r_h^swap, r_{h+1}^swap, ..., r_j^swap)
```

from positions `h` through `j` is

```text
(b,a,r_{h+2},...,r_j).
```

Its subblock from positions `h+1` through `j` is

```text
a,r_{h+2},...,r_j,
```

and has sum zero:

```text
a+r_{h+2}+...+r_j=0.
```

Thus the collision in `R^swap` between indices `h` and `j` is exactly the zero-sum contiguous block

```text
R^swap(h,j] = (a,r_{h+2},...,r_j).
```

### Backward case `j<h`

The block from positions `j+1` through `h` in `R^swap` is

```text
r_{j+1},...,r_{h-1},b,
```

and has sum zero:

```text
r_{j+1}+...+r_{h-1}+b=0.
```

Thus the collision in `R^swap` between indices `j` and `h` is exactly the zero-sum contiguous block

```text
R^swap(j,h] = (r_{j+1},...,r_{h-1},b).
```

### Proof

Both statements are immediate from Lemma A9.1 and from the definition of the adjacent-swapped ordering `R^swap`.  ∎

---

## Interpretation: the pair trap is a forced zero-block trap

The adjacent swap successfully removes the forbidden hit value `f` at position `h`, because it replaces

```text
P+a=f
```

by

```text
P+b != f.
```

The only reason the swap fails is that it creates a new contiguous zero-sum block in the swapped ordering.

Therefore the pair `(a,b)` is not merely locally blocked.  It is blocked because swapping it **contiguizes** a zero-sum punctured interval.

This gives a sharper meaning to the earlier phrase:

```text
pair trap branch is controlled by first-cut pair reinsertion.
```

A repair must do one of the following:

1. swap `a,b` and then break the newly contiguous zero-sum block;
2. move the distinguished atom `a` or `b` through the punctured interval before swapping;
3. rotate the entire obstruction block so that the zero-sum block is not exposed as a collision;
4. combine this zero-block with a cyclic zero-sum complement from A8 and uncross the two intervals.

---

## 2. Zero-sum block relocation formula

The next lemma is a general bookkeeping tool.

Let an ordering be decomposed as

```text
R = X Z Y,
```

where `Z` is a contiguous block with

```text
sigma(Z)=0.
```

Let

```text
R' = X Y Z
```

be the ordering obtained by moving `Z` to the right end of the displayed region.

## Lemma A9.3: zero-sum block relocation partial sums

Let `x=sum(X)`.  Write the internal partial sums of `Z` as

```text
Z_k = z_1+...+z_k,    1 <= k <= |Z|.
```

and the internal partial sums of `Y` as

```text
Y_l = y_1+...+y_l,    1 <= l <= |Y|.
```

Since `sigma(Z)=0`, moving `Z` past `Y` has the following effect.

In `R=XZY`, the displayed-region partial sums are

```text
x+Z_1, ..., x+Z_|Z|=x,
x+Y_1, ..., x+Y_|Y|.
```

In `R'=XYZ`, they are

```text
x+Y_1, ..., x+Y_|Y|,
x+Y_|Y|+Z_1, ..., x+Y_|Y|+Z_|Z|=x+Y_|Y|.
```

Thus all partial sums after the displayed region are unchanged, and the only nontrivial new values are the translated internal values

```text
x+Y_|Y|+Z_k.
```

### Proof

The total sum of `Z` is zero, so passing through `Z` does not change the running sum at the end of the block.  The formulas are obtained by directly summing the entries in the two displayed orderings.  ∎

## Lemma A9.4: zero-sum relocation obstruction criterion

With the notation of Lemma A9.3, suppose the original ordering `R=XZY` is Graham-valid outside the fact that `Z` may be an exposed zero-sum block in an auxiliary sequence such as `R^swap`.

Then the relocation `XZY -> XYZ` can fail Graham-validity only if one of the new translated internal values

```text
x+Y_|Y|+Z_k,   1 <= k < |Z|,
```

collides with:

1. another translated internal value;
2. an unchanged partial sum outside the moved block;
3. one of the partial sums inside `Y`.

It can fail endpoint avoidance for forbidden value `f` only if

```text
x+Y_|Y|+Z_k=f
```

for some `1 <= k < |Z|`, or if an unchanged partial sum already equals `f`.

### Proof

The endpoint values of the zero-sum block are unchanged because `Z_|Z|=0`.  All post-region partial sums are unchanged.  Therefore every new collision or forbidden hit must involve one of the newly translated proper internal partial sums of `Z`.  ∎

---

## 3. How A9 connects A6 and A8

A6 gave explicit bypass rotations directly in the original ordering.

A9 gives a different view:

1. perform the right-adjacent swap, producing `R^swap`;
2. observe that the failure is a contiguous zero-sum block `Z` in `R^swap`;
3. attempt to relocate or rotate `Z` using Lemma A9.3;
4. every failure is now an explicit collision involving a translated proper internal partial sum of `Z`.

A8 gave a cyclic zero-sum complement whenever the cyclic cut fails by cross-collision.  That complement is also a zero-sum block, but on the cyclic order rather than the original linear order.

Thus the remaining proof can be recast as a two-zero-block problem:

```text
local zero block from blocked adjacent swap
+
cyclic zero block from cyclic cut obstruction
```

The likely next move is to prove an uncrossing lemma for two zero-sum blocks on a cycle.

---

## Target A10: two-zero-block uncrossing

A plausible formal target is:

> Let a minimal endpoint-avoidance counterexample produce both a local zero block `Z_loc` in `R^swap` and a cyclic zero block `Z_cyc` from the cyclic cut.  Then either the two zero blocks can be uncrossed to produce a smaller local obstruction, or one can be relocated to give a Graham-valid ordering avoiding `f`.

The finite certificate package suggests that the relevant interval geometries should split into a small number of cases:

```text
separated disjoint,
endpoint adjacent,
proper overlap,
nested.
```

This is the analytic analogue of the atomic interval classification used by the finite checker.

---

## Current status

Proved here:

1. the local obstruction is a punctured zero-sum interval;
2. the blocked adjacent swap contiguizes that punctured interval into an exposed zero-sum block;
3. a general zero-sum block relocation formula;
4. an exact obstruction criterion for zero-sum block relocation.

Not proved here:

1. that relocation must succeed;
2. the two-zero-block uncrossing lemma;
3. endpoint avoidance.
