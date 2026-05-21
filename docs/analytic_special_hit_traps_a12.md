# Analytic special-hit traps A12: equal-sum branches from cyclic rotation

This note handles the two non-cross cyclic-cut obstruction branches from A8.

When the cyclic cut after the first forbidden hit is Graham-valid but still hits the forbidden value `f`, A8 shows that the hit must arise from either

```text
S_alpha = 2f
```

on the first side of the cut, or

```text
S_beta = 2f - sigma
```

on the second side.  This note converts those branches into explicit equal-sum interval traps.

These are not zero-sum intervals.  They are equal-sum relations between disjoint or complementary intervals, so they need a different repair mechanism from the two-zero-block branch.

## Standing setup

Let

```text
R = (r_1, ..., r_t)
```

be a Graham-valid ordering of `A subset F_p^*`, with

```text
S_0=0,
S_i=r_1+...+r_i,
sigma=S_t.
```

Assume endpoint avoidance fails for `(A,f)` with

```text
f != sigma.
```

Choose `R` so that its unique forbidden hit occurs as early as possible:

```text
S_h=f.
```

Then `h<t`.

Write the three natural pieces around the first forbidden hit as

```text
L = (0,h]      = (r_1, ..., r_h),
M = (h,t]      = (r_{h+1}, ..., r_t).
```

Then

```text
sum(L)=f,
sum(M)=sigma-f.
```

The cyclic cut after `h` is

```text
Rot_h(R) = (M,L).
```

A8 says that if this cyclic cut is Graham-valid but still hits `f`, then the hit comes from either

```text
S_alpha=2f              with h<alpha<=t,
```

or

```text
S_beta=2f-sigma         with 1<=beta<=h.
```

By minimality of `h`, the rotated hit cannot occur before position `h`, giving the index constraints recorded in A8.

---

## Lemma A12.1: first-side special hit is an equal-sum interval trap

Assume

```text
h < alpha <= t
```

and

```text
S_alpha = 2f.
```

Then the interval after the forbidden hit and ending at `alpha` has the same sum as the prefix ending at the forbidden hit:

```text
sum(h,alpha] = sum(0,h] = f.
```

Equivalently,

```text
r_{h+1}+...+r_alpha = r_1+...+r_h.
```

### Proof

Since `S_h=f`,

```text
sum(h,alpha] = S_alpha-S_h = 2f-f=f.
```

Also

```text
sum(0,h]=S_h=f.
```

Therefore the two intervals have equal sum.  ∎

### Interpretation

The first-side special hit creates two consecutive intervals with equal sum:

```text
(0,h]       and       (h,alpha].
```

The second interval is not allowed to be too short under earliest-hit minimality: from A8, if the rotated ordering is Graham-valid, then `alpha>=2h`.

Thus the trap is not merely equal-sum; it is a late equal-sum repetition of the initial forbidden prefix.

---

## Lemma A12.2: second-side special hit is a tail-prefix equal-sum trap

Assume

```text
1 <= beta <= h
```

and

```text
S_beta = 2f - sigma.
```

Then the interval from `beta` to the forbidden hit has the same sum as the tail after the forbidden hit:

```text
sum(beta,h] = sum(h,t] = sigma-f.
```

Equivalently,

```text
r_{beta+1}+...+r_h = r_{h+1}+...+r_t.
```

### Proof

Using `S_h=f`,

```text
sum(beta,h] = S_h-S_beta = f-(2f-sigma)=sigma-f.
```

Also

```text
sum(h,t]=S_t-S_h=sigma-f.
```

Therefore the two intervals have equal sum.  ∎

### Interpretation

The second-side special hit creates two intervals with equal sum:

```text
(beta,h]       and       (h,t].
```

By A8 minimality, the rotated hit position

```text
t-h+beta
```

cannot be smaller than `h`.  Hence

```text
beta >= 2h-t.
```

So this is a late return constraint in the rotated ordering.

---

## Lemma A12.3: equal-sum interval traps become zero-sum after signed exchange

Let two disjoint intervals `I` and `J` in the ordering have equal sum:

```text
sum(I)=sum(J).
```

Then the signed difference

```text
sum(I)-sum(J)=0
```

is a zero-sum relation supported on two separated intervals with opposite signs.

In particular, the first-side special hit gives

```text
sum(0,h] - sum(h,alpha] = 0,
```

and the second-side special hit gives

```text
sum(beta,h] - sum(h,t] = 0.
```

### Proof

Immediate by subtraction.  ∎

### Interpretation

This explains the older phrase `sign-free avoidance` versus `external endpoint avoidance`.

The obstruction is not always an ordinary zero-sum interval.  Sometimes it is a signed zero-sum composite made of two equal-sum intervals.  To eliminate it by ordinary order moves, one needs to make the signed relation sign-free, usually by a rotation, reversal, or exchange that places one interval on the other side of the running-sum comparison.

This is exactly the kind of object that the Atomicium candidate repository calls a local/cyclic composite, but here we have the concrete formula in the present notation.

---

## 1. Rotation formulas for the equal-sum trap

The following formulas identify the natural repair move for an equal-sum branch.

### First-side equal-sum branch

Assume `S_alpha=2f`.  Decompose

```text
R = L U V
```

where

```text
L=(r_1,...,r_h),
U=(r_{h+1},...,r_alpha),
V=(r_{alpha+1},...,r_t).
```

Then

```text
sum(L)=sum(U)=f.
```

Consider the exchange

```text
L U V  ->  U L V.
```

The total sum of `LU` is unchanged, and since `sum(L)=sum(U)`, the endpoint after the first block remains `f`:

```text
sum(U)=f.
```

Thus this exchange does **not** avoid `f`; it merely moves the forbidden hit from position `h` to position `|U|=alpha-h`.

By the minimality of `h`, if the exchanged ordering is Graham-valid, then

```text
alpha-h >= h,
```

which is exactly the A8 condition `alpha>=2h`.

So the equal-sum exchange is useful only if it can be combined with an internal rotation of `U` or `L` that breaks the exact first-block sum `f` while preserving Graham-validity.

### Second-side equal-sum branch

Assume `S_beta=2f-sigma`.  Decompose

```text
R = A B C
```

where

```text
A=(r_1,...,r_beta),
B=(r_{beta+1},...,r_h),
C=(r_{h+1},...,r_t).
```

Then

```text
sum(B)=sum(C)=sigma-f.
```

The exchange

```text
A B C -> A C B
```

preserves the total sum and moves the same tail-sum block earlier.  Its first potential forbidden hit created by `C` occurs at position

```text
beta + |C| = beta + (t-h),
```

which is exactly the rotated-hit index from A8.  Minimality forces this to be at least `h` when the exchange is Graham-valid:

```text
beta + t - h >= h,
```

or

```text
beta >= 2h-t.
```

Again, the direct exchange alone does not prove avoidance; it identifies the precise block where a second-level perturbation is needed.

---

## 2. Refined proof target

The cyclic obstruction has now split into three analytic objects.

### Cross branch

Produces a basepoint-crossing zero block:

```text
sum(alpha,t] + sum(0,beta] = 0.
```

Handled by the two-zero-block transport program A10/A11.

### First-side special-hit branch

Produces an equal-sum trap:

```text
sum(0,h] = sum(h,alpha].
```

Need to perturb one of the equal-sum blocks so the first block no longer lands at `f`.

### Second-side special-hit branch

Produces an equal-sum trap:

```text
sum(beta,h] = sum(h,t].
```

Need to perturb one of the equal-sum blocks or relocate the tail block without producing a collision.

---

## Target A13: equal-sum perturbation lemma

A natural next theorem is:

> In a minimal endpoint-avoidance counterexample, an equal-sum interval trap from A12 can be perturbed by an adjacent swap, cyclic cut, or zero-block relocation unless it forces a local bypass zero-sum block already handled by A5/A9.

More concretely:

1. If `sum(0,h]=sum(h,alpha]`, then either an internal reorder of `(h,alpha]` avoids the value `f` when moved first, or every such reorder is blocked by a local zero-sum/pair trap.
2. If `sum(beta,h]=sum(h,t]`, then either moving the tail block earlier gives a valid earlier hit/avoidance contradiction, or the obstruction produces a new zero block crossing one of the block boundaries.

This would reduce the non-cross cyclic branches to the zero-block program.

---

## Current status

Proved here:

1. `S_alpha=2f` is equivalent to the equal-sum trap `sum(0,h]=sum(h,alpha]`;
2. `S_beta=2f-sigma` is equivalent to the equal-sum trap `sum(beta,h]=sum(h,t]`;
3. equal-sum traps are signed zero-sum composites;
4. direct block exchanges reproduce exactly the minimality inequalities from A8.

Not proved here:

1. equal-sum perturbation lemma;
2. reduction of equal-sum traps to zero-block traps;
3. endpoint avoidance theorem.
