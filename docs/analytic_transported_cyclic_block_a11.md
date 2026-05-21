# Analytic transported cyclic block A11: effect of the adjacent swap on the cyclic obstruction

This note continues from A8--A10.

The goal is to understand how the cyclic zero block produced by a cyclic-cut cross obstruction behaves under the adjacent swap at the first forbidden hit.

A useful simplification occurs: in the actual A8 geometry, the cyclic zero block can contain `a=r_h`, but it cannot contain `b=r_{h+1}`.  Therefore the transport case split is smaller than the generic interval-geometry case split suggested in A10.

## Standing setup

Let

```text
R = (r_1, ..., r_t)
```

be a Graham-valid ordering of `A subset F_p^*`, with partial sums

```text
S_0=0,
S_i=r_1+...+r_i,
sigma=S_t.
```

Assume endpoint avoidance fails for `(A,f)` with

```text
f != sigma.
```

Choose `R` so that its unique forbidden hit

```text
S_h=f
```

has minimal index `h` among all Graham-valid orderings of `A`.

Write

```text
a = r_h,
b = r_{h+1},
P = S_{h-1}.
```

Thus

```text
P+a=f.
```

Let `R^swap` be the adjacent-swapped ordering

```text
(r_1, ..., r_{h-1}, b, a, r_{h+2}, ..., r_t).
```

The right-swap obstruction from A5 says that `R^swap` has a collision caused by a contiguous zero block `Z_loc`.

Now assume the cyclic cut after `h` fails by a cross obstruction.  Then there exist indices

```text
1 <= beta <= h < alpha <= t
```

such that

```text
S_alpha = sigma + S_beta.
```

Equivalently, the cyclic block

```text
Z_cyc = (alpha,t] union (0,beta]
      = (r_{alpha+1},...,r_t,r_1,...,r_beta)
```

has sum zero.

---

## Lemma A11.1: position of the adjacent pair relative to `Z_cyc`

With `1 <= beta <= h < alpha <= t`, the cyclic zero block `Z_cyc` never contains `b=r_{h+1}`.  It contains `a=r_h` if and only if

```text
beta = h.
```

### Proof

The block `Z_cyc` contains exactly the positions

```text
{alpha+1, ..., t} union {1, ..., beta}.
```

Since `alpha>h`, position `h+1` satisfies

```text
h+1 <= alpha
```

unless `alpha=h`, which is impossible.  Hence `h+1` is not in `{alpha+1,...,t}`.  Also `h+1>beta` because `beta<=h`, so `h+1` is not in `{1,...,beta}`.  Therefore `b=r_{h+1}` is not in `Z_cyc`.

Position `h` is not in `{alpha+1,...,t}` because `alpha>h`.  It is in `{1,...,beta}` exactly when `beta=h`.  ∎

---

## Lemma A11.2: transported sum of `Z_cyc` under the adjacent swap

Let `Z_cyc^swap` denote the cyclic block using the same index set

```text
{alpha+1, ..., t} union {1, ..., beta}
```

but read in `R^swap` instead of `R`.

Then

```text
sum_{R^swap}(Z_cyc^swap) = 0
```

if `beta<h`, while

```text
sum_{R^swap}(Z_cyc^swap) = b-a
```

if `beta=h`.

### Proof

The adjacent swap changes only the entries at positions `h` and `h+1`:

```text
position h:   a -> b,
position h+1: b -> a.
```

By Lemma A11.1, position `h+1` is never in `Z_cyc`.  Position `h` is in `Z_cyc` exactly when `beta=h`.

If `beta<h`, neither changed position belongs to `Z_cyc`, so its sum is unchanged.  Since `Z_cyc` has sum zero in `R`, it remains zero in `R^swap`.

If `beta=h`, the block contained `a` at position `h` in `R`, but contains `b` at position `h` in `R^swap`.  All other entries in the block are unchanged, so the sum changes by `b-a`.  Since the original sum was zero, the new sum is `b-a`.  ∎

---

## Lemma A11.3: if `beta<h`, then the swapped ordering has two zero blocks

Assume the cyclic cross obstruction has `beta<h`.

Then in the swapped ordering `R^swap`:

1. the local block `Z_loc` from A9 is a contiguous linear zero-sum block;
2. the transported cyclic block `Z_cyc^swap` is still a cyclic zero-sum block crossing the basepoint.

### Proof

The first statement is Lemma A9.2.  The second is Lemma A11.2 with `beta<h`.  The block still has the same index geometry, hence crosses the basepoint as before.  ∎

### Consequence

In the subcase `beta<h`, the remaining contradiction can be attacked as a true two-zero-block problem in the same auxiliary ordering `R^swap`.

This is the cleanest uncrossing branch.

---

## Lemma A11.4: if `beta=h`, transport creates a pair-difference atom

Assume the cyclic cross obstruction has `beta=h`.

Then

```text
sum_{R^swap}(Z_cyc^swap)=b-a.
```

Equivalently, the transported cyclic block fails to remain zero by exactly the pair difference

```text
b-a.
```

Since the local swapped value at the former forbidden-hit index is

```text
S_h(R^swap)=P+b,
```

and the original forbidden hit is

```text
f=P+a,
```

the same pair difference is

```text
b-a = S_h(R^swap)-f.
```

### Proof

The first statement is Lemma A11.2 with `beta=h`.  The final identity follows from subtraction:

```text
(P+b)-(P+a)=b-a.
```

∎

### Interpretation

The boundary case `beta=h` is exactly a pair-trap case.  The cyclic zero block cuts at the forbidden-hit atom `a`.  After the adjacent swap, the transported cyclic block measures the displacement away from the forbidden value.

This gives a precise algebraic form to the earlier phrase:

```text
cyclic block cuts between a and b -> pair trap.
```

---

## 2. Interaction with the local zero block in `R^swap`

Recall the local zero block `Z_loc` in `R^swap`.

### Forward local branch

If the right-swap blocker has `j>h`, then

```text
Z_loc = (h,j] in R^swap
      = (a,r_{h+2},...,r_j),
```

and

```text
sum(Z_loc)=0.
```

### Backward local branch

If the right-swap blocker has `j<h`, then

```text
Z_loc = (j,h] in R^swap
      = (r_{j+1},...,r_{h-1},b),
```

and

```text
sum(Z_loc)=0.
```

Thus, when `beta<h`, the auxiliary ordering `R^swap` contains both `Z_loc` and a basepoint-crossing cyclic zero block.  When `beta=h`, the transported cyclic block has sum `b-a`, which is exactly the local forbidden displacement.

---

## 3. Refined A12 target

The previous generic target A10 can now be sharpened.

### Branch A: true two-zero-block branch

If the cyclic cross obstruction has `beta<h`, prove that a linear zero block `Z_loc` and a basepoint-crossing cyclic zero block `Z_cyc^swap` in `R^swap` can be uncrossed or relocated to produce either:

```text
1. a Graham-valid ordering avoiding f, or
2. a Graham-valid ordering with an earlier f-hit, or
3. a contradiction to the minimality of the local blocker.
```

### Branch B: boundary pair-trap branch

If the cyclic cross obstruction has `beta=h`, use

```text
sum(Z_cyc^swap)=b-a
```

and the local zero block to produce a short algebraic repair.  This branch should be finite-dimensional, because all nonzero behavior is compressed into the pair difference `b-a`.

---

## Current status

Proved here:

1. `Z_cyc` never contains `b=r_{h+1}`;
2. `Z_cyc` contains `a=r_h` iff `beta=h`;
3. transported cyclic block remains zero if `beta<h`;
4. transported cyclic block has sum `b-a` if `beta=h`;
5. the cyclic-cross branch splits into a true two-zero-block branch and a boundary pair-trap branch.

Not proved here:

1. true two-zero-block uncrossing;
2. boundary pair-trap repair;
3. endpoint avoidance.
