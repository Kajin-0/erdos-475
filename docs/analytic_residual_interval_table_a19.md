# Analytic residual interval table A19: translating singleton traps into interval identities

This note continues from A18.

A18 reduced the equal-sum singleton-prefix branches to a finite residual family list.  This note rewrites each residual family in old-partial-sum and interval language.

The purpose is not to claim that all residuals are eliminated.  The purpose is to make the remaining symbolic cases explicit enough that each can be attacked by interval moves, prefix cuts, or finite local templates.

---

## Standing setup

Let

```text
R=(r_1,...,r_t)
```

be a Graham-valid ordering of `A subset F_p^*`, with

```text
S_0=0,
S_i=r_1+...+r_i,
sigma=S_t.
```

Assume endpoint avoidance fails for `(A,f)`, where

```text
f != sigma.
```

Choose `R` so that its unique forbidden hit occurs as early as possible:

```text
S_h=f.
```

Write

```text
a=r_h,
b=r_{h+1},
P=S_{h-1}.
```

Then

```text
P+a=f.
```

The local right-swap obstruction gives a blocker index `j != h` such that

```text
P+b=S_j.
```

Equivalently,

```text
b=S_j-P.
```

For intervals, write

```text
sum(u,v] = S_v-S_u.
```

---

# 1. FIRST branch residual table

Assume the FIRST equal-sum branch:

```text
R=LUV,
sum(L)=sum(U)=f,
```

where

```text
L=(r_1,...,r_h),
U=(r_{h+1},...,r_alpha),
V=(r_{alpha+1},...,r_t),
S_alpha=2f.
```

Let

```text
U_s = r_{h+1}+...+r_{h+s} = S_{h+s}-f,
V_m = r_{alpha+1}+...+r_{alpha+m} = S_{alpha+m}-2f.
```

A18 leaves the following FIRST residual families.

---

## F1r. `b=f-L_i`, with `1 <= i <= h-2`

Since `L_i=S_i`, the trap equation is

```text
b=f-S_i.
```

Equivalent forms:

```text
S_i+b=f=S_h,
sum(i,h] = b.
```

Thus the interval from `i+1` through `h` has the same sum as the atom `b`:

```text
r_{i+1}+...+r_h = b.
```

Combining with the local blocker relation gives

```text
S_j = P+f-S_i.
```

Using `f=P+a`, this becomes

```text
S_j = 2P+a-S_i.
```

### Status

Residual.  This is an atom-equals-interval relation before the first hit.  The excluded boundary cases `i=h` and `i=h-1` were already eliminated in A18.

---

## F2r. `L_i=0`, with `1 <= i <= h`

This says

```text
S_i=0.
```

Equivalent interval form:

```text
sum(0,i]=0.
```

### Status

Residual prefix-zero branch.  This is not a Graham collision because `S_0=0` is not included among the required distinct nonempty partial sums.

Potential use: cut after the zero-prefix.  Since the prefix has total zero, moving it later preserves subsequent running sums up to translation by zero at the cut endpoint.  This branch should be handled by a prefix-zero cut lemma.

---

## F3r. `b=f+U_s`, with `2 <= s <= |U|`

Since

```text
f+U_s = S_{h+s},
```

the trap equation is

```text
b=S_{h+s}.
```

Equivalent forms:

```text
S_{h+s}=b,
S_j=P+S_{h+s}.
```

Also

```text
sum(0,h+s]=b.
```

### Status

Residual atom-as-old-partial-sum branch.  This is not an old collision by itself because `b` is an element of `A`, not necessarily an old partial sum elsewhere.  It becomes rigid only when combined with `P+b=S_j`.

---

## F4r. `b=2f+V_m`

Since

```text
2f+V_m = S_{alpha+m},
```

the trap equation is

```text
b=S_{alpha+m}.
```

Combining with the local blocker relation gives

```text
S_j=P+S_{alpha+m}.
```

### Status

Residual tail atom-as-old-partial-sum branch.  Similar to F3r, but the old partial sum is in the `V` tail after the repeated `2f` hit.

---

## F5r. `b=f+U_s-L_i`, with `2 <= s <= |U|`, `1 <= i <= h-1`

Since

```text
f+U_s=S_{h+s},
L_i=S_i,
```

the trap equation is

```text
b=S_{h+s}-S_i.
```

Equivalent interval form:

```text
sum(i,h+s]=b.
```

Thus the interval from `i+1` through `h+s` has sum equal to the atom `b`:

```text
r_{i+1}+...+r_{h+s}=b.
```

Combining with the local blocker gives

```text
S_j=P+S_{h+s}-S_i.
```

### Status

Residual atom-equals-crossing-interval branch.  The eliminated boundary `i=h` was an old Graham collision.  The remaining cases cross the first forbidden hit and extend into `U`.

---

## F6r. `b=2f+V_m-L_i`

Since

```text
2f+V_m=S_{alpha+m},
L_i=S_i,
```

the trap equation is

```text
b=S_{alpha+m}-S_i.
```

Equivalent interval form:

```text
sum(i,alpha+m]=b.
```

Combining with the local blocker gives

```text
S_j=P+S_{alpha+m}-S_i.
```

### Status

Residual long atom-equals-interval branch.  It crosses the first hit, all of `U`, and part of `V`.

---

# 2. SECOND branch residual table

Assume the SECOND equal-sum branch:

```text
R=ABC,
sum(B)=sum(C)=sigma-f,
```

where

```text
A=(r_1,...,r_beta),
B=(r_{beta+1},...,r_h),
C=(r_{h+1},...,r_t),
S_beta=2f-sigma.
```

Write

```text
sA=S_beta=2f-sigma,
B_k=r_{beta+1}+...+r_{beta+k}=S_{beta+k}-sA,
C_s=r_{h+1}+...+r_{h+s}=S_{h+s}-f.
```

The boundary case `beta=h` is excluded here and treated as a pair-trap branch.

---

## S1r. `b=sigma-f-B_k`, with `1 <= k < |B|`

Since

```text
sum(B)=sigma-f,
```

the equation says that `b` equals the remaining tail of `B` after its first `k` entries:

```text
b = B_{|B|}-B_k.
```

In old partial sums:

```text
B_k=S_{beta+k}-S_beta,
B_{|B|}=S_h-S_beta=f-sA=sigma-f.
```

Thus

```text
b=S_h-S_{beta+k}=f-S_{beta+k}.
```

Equivalent forms:

```text
S_{beta+k}+b=f=S_h,
sum(beta+k,h]=b.
```

### Status

Residual atom-equals-pre-hit-tail branch.  This is the SECOND analogue of F1r.

---

## S2r. `b=A_i-sA`, with `1 <= i < beta`

Since `A_i=S_i` and `sA=S_beta`,

```text
b=S_i-S_beta.
```

Equivalent signed interval form:

```text
S_beta+b=S_i,
-sum(i,beta]=b.
```

or

```text
sum(i,beta] = -b.
```

### Status

Residual negative-interval atom branch.  It says a pre-`beta` interval has sum `-b`.  This is a signed version of an atom-equals-interval trap.

---

## S3r. `b=A_i-sA-B_k`

Substitute

```text
A_i=S_i,
sA+B_k=S_{beta+k}.
```

Then

```text
b=S_i-S_{beta+k}.
```

Equivalent signed interval form:

```text
S_{beta+k}+b=S_i,
sum(i,beta+k] = -b
```

when `i<beta+k`, which is the natural index geometry here.

### Status

Residual signed atom-equals-interval branch crossing `A` into `B`.

---

## S4r. `b=f+C_s-sA`, with `2 <= s <= |C|`

Since

```text
f+C_s=S_{h+s},
```

we get

```text
b=S_{h+s}-S_beta.
```

Equivalent interval form:

```text
sum(beta,h+s]=b.
```

Combining with the local blocker relation gives

```text
S_j=P+S_{h+s}-S_beta.
```

### Status

Residual atom-equals-long-interval branch from `beta` into the tail `C`.  The endpoint case `s=|C|` gives `b=sigma-sA=2(sigma-f)` and does not collapse automatically.

---

## S5r. `b=f+C_s-sA-B_k`, with `2 <= s <= |C|`

Substitute

```text
f+C_s=S_{h+s},
sA+B_k=S_{beta+k}.
```

Then

```text
b=S_{h+s}-S_{beta+k}.
```

Equivalent interval form:

```text
sum(beta+k,h+s]=b.
```

### Status

Residual atom-equals-interval branch from inside `B` into the tail `C`.

---

# 3. Structural compression

After rewriting, all residual singleton-prefix traps have one of three forms.

## Type I: atom equals forward interval

```text
b = S_v-S_u = sum(u,v]
```

Examples:

```text
F1r, F5r, F6r, S1r, S4r, S5r.
```

These say that inserting `b` after position `u` lands exactly at old partial sum `S_v`:

```text
S_u+b=S_v.
```

## Type II: atom equals negative interval

```text
b = S_u-S_v = -sum(u,v]
```

Examples:

```text
S2r, S3r.
```

These say that inserting `b` after position `v` lands at old partial sum `S_u`:

```text
S_v+b=S_u.
```

## Type III: prefix-zero

```text
S_i=0.
```

Example:

```text
F2r.
```

This branch is special because it is compatible with Graham-validity.

---

# 4. Relation to local blocker geometry

The local blocker relation itself says

```text
P+b=S_j,
```

or

```text
S_{h-1}+b=S_j.
```

Thus every residual atom-equals-interval identity gives two placements of the same atom `b` that land on old partial sums:

```text
S_{h-1}+b=S_j,
S_u+b=S_v
```

or in signed cases

```text
S_v+b=S_u.
```

Subtracting the two landing equations gives an equal-difference relation among old partial sums:

```text
S_j-S_{h-1}=S_v-S_u.
```

or

```text
S_j-S_{h-1}=S_u-S_v.
```

Equivalently, two intervals have equal sum:

```text
sum(h-1,j] = sum(u,v]
```

or

```text
sum(h-1,j] = -sum(u,v].
```

This is the key simplification: the residual singleton-prefix cases are all equal-interval or signed-equal-interval traps.

---

# 5. Target A20: equal-interval uncrossing

The next theorem should no longer be phrased in terms of the original long trap lists.

It should be stated as:

> In a minimal endpoint-avoidance counterexample, if the same atom `b` has two landing equations
>
> ```text
> S_x+b=S_y,
> S_u+b=S_v,
> ```
>
> then the resulting equal-interval relation can be uncrossed, unless it is one of the already separated branches: prefix-zero, boundary pair trap, or cyclic zero block.

Equivalently, eliminate equal-interval traps of the form

```text
sum(x,y]=sum(u,v]
```

or signed traps

```text
sum(x,y]=-sum(u,v].
```

under the minimal first-hit hypothesis.

---

## Current status

Proved here:

1. every FIRST residual family becomes atom-equals-interval, atom-as-old-partial-sum, or prefix-zero;
2. every SECOND residual family becomes atom-equals-interval or signed atom-equals-interval;
3. combining with the local blocker turns all atom-equals-interval residuals into equal-interval or signed-equal-interval traps;
4. the remaining obstruction is compressed to equal-interval uncrossing plus prefix-zero and boundary pair-trap branches.

Not proved here:

1. equal-interval uncrossing;
2. prefix-zero cut reduction;
3. boundary pair-trap repair;
4. endpoint avoidance theorem.
