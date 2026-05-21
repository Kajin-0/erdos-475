# Analytic secondary minimality A15: pruning prefix-trap equations

This note continues from A14.

A14 reduced the equal-sum obstruction branches to proper-prefix interleaving moves.  Those moves have several possible forbidden-hit and collision equations.  This note records a useful refinement: once an equal-sum branch is chosen minimally, some of the forbidden-hit equations disappear automatically.

The purpose is to reduce the remaining prefix-trap problem to fewer equations.

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

Choose `R` so that the unique forbidden hit occurs as early as possible:

```text
S_h=f.
```

The cyclic-cut obstruction from A8 has three branches:

```text
CROSS:   S_alpha = sigma + S_beta,
FIRST:   S_alpha = 2f,
SECOND:  S_beta = 2f - sigma.
```

This note treats the FIRST and SECOND equal-sum branches.

---

# 1. FIRST branch with minimal `2f` hit

Assume there exists at least one first-side special hit:

```text
S_alpha = 2f,    h < alpha <= t.
```

Choose `alpha` minimal among all such indices greater than `h`.

Decompose

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

Let `U=XY`, where `X` is a nonempty proper prefix of `U`, and write

```text
x=sum(X).
```

---

## Lemma A15.1: minimal FIRST branch eliminates proper-prefix `X_i=f` hits

Under the minimal choice of `alpha`, no proper prefix of `U` has sum `f`.

Equivalently, for every nonempty proper prefix `X'` of `U`,

```text
sum(X') != f.
```

In the A14 forbidden-hit list for the FIRST proper-prefix interleaving

```text
L X Y V -> X L Y V,
```

the condition

```text
X_i=f
```

cannot occur.

### Proof

Let `X'=(r_{h+1},...,r_q)` be a nonempty proper prefix of `U`, where

```text
h < q < alpha.
```

If `sum(X')=f`, then

```text
S_q = S_h + sum(X') = f+f=2f.
```

This gives a first-side special hit `S_q=2f` with

```text
h < q < alpha,
```

contradicting the minimal choice of `alpha`.  ∎

---

## Lemma A15.2: minimal FIRST branch also eliminates the final-prefix special equation `x=f`

For every proper nonempty prefix `X` of `U`,

```text
x=sum(X) != f.
```

### Proof

This is the special case of Lemma A15.1 in which `X'=X`.  ∎

---

## Remaining FIRST forbidden-hit equations

In A14, the FIRST proper-prefix interleaving

```text
L X Y V -> X L Y V
```

had forbidden-hit equations

```text
X_i = f,
L_j = f-x,
Y_k = -x,
V_m = -f.
```

With minimal `alpha`, the first family is impossible by Lemma A15.1.

The last family `V_m=-f` is impossible because it would give an old second hit of `f` after `alpha`:

```text
2f+V_m=f.
```

Thus only two forbidden-hit families remain:

```text
L_j = f-x,
Y_k = -x.
```

Equivalently,

```text
x = f-L_j,
x = -Y_k.
```

So every failed proper-prefix attempt in the FIRST branch must be caused by one of:

```text
1. x lies in f - Pref(L),
2. x lies in -Pref(Y),
3. one of the cross-collision equations from A14.
```

---

# 2. SECOND branch with extremal `2f-sigma` hit

Assume there exists at least one second-side special hit:

```text
S_beta = 2f - sigma,    1 <= beta <= h.
```

The relevant proper-prefix move in A14 decomposes

```text
R = A B C
```

where

```text
A=(r_1,...,r_beta),
B=(r_{beta+1},...,r_h),
C=(r_{h+1},...,r_t),
```

and

```text
sum(B)=sum(C)=sigma-f.
```

For the proper-prefix move, split

```text
C = X Y
```

with `X` nonempty and proper.

Here the forbidden-hit equation

```text
X_j = sigma-f
```

is automatically impossible for proper prefixes of `C`, regardless of how `beta` was chosen.

---

## Lemma A15.3: proper prefixes of `C` cannot have sum `sigma-f`

Let `X'=(r_{h+1},...,r_q)` be a nonempty proper prefix of `C`, so

```text
h < q < t.
```

Then

```text
sum(X') != sigma-f.
```

### Proof

If `sum(X')=sigma-f`, then

```text
S_q = S_h + sum(X') = f + (sigma-f)=sigma.
```

But `S_t=sigma` and `q<t`.  This would give a repeated nonempty partial sum

```text
S_q=S_t,
```

contradicting Graham-validity of `R`.  ∎

---

## Remaining SECOND forbidden-hit equations

In A14, the SECOND proper-prefix interleaving

```text
A B X Y -> A X B Y
```

had forbidden-hit equations

```text
A_i = f,
X_j = sigma-f,
B_k = sigma-f-x,
Y_m = -x.
```

The second family is impossible by Lemma A15.3.

The first family `A_i=f` can occur only if the original forbidden hit lies in `A`.  Since `A` ends at `beta<=h` and the unique forbidden hit is at `h`, this means:

```text
A_i=f  iff  beta=h and i=h.
```

Therefore:

- if `beta<h`, the first family is impossible;
- if `beta=h`, the first family is present as the endpoint of `A` and must be treated as a boundary pair-trap case.

Thus, away from the boundary case `beta=h`, only two forbidden-hit families remain:

```text
B_k = sigma-f-x,
Y_m = -x.
```

Equivalently,

```text
x = sigma-f-B_k,
x = -Y_m.
```

---

# 3. Refined prefix-trap target

After the pruning above, the equal-sum branches have a cleaner trap structure.

## FIRST branch trap set

For each proper prefix sum `x` of `U`, the forbidden-hit obstructions reduce to

```text
x in f - Pref(L),
x in -Pref(Y),
```

plus the cross-collision families from A14.

## SECOND branch trap set

For each proper prefix sum `x` of `C`, away from the boundary case `beta=h`, the forbidden-hit obstructions reduce to

```text
x in sigma-f-Pref(B),
x in -Pref(Y),
```

plus the cross-collision families from A14.

The boundary case `beta=h` is already aligned with the pair-trap boundary identified in A11.

---

## Target A16: pruned prefix-trap dichotomy

Prove that a movable block cannot have all of its proper prefix sums trapped by the pruned equations unless one of the following happens:

```text
1. a local zero-sum block is exposed;
2. a short pair trap occurs, including beta=h boundary cases;
3. a collision already existed in the original Graham-valid ordering;
4. the block has impossible additive concentration under the distinct-prefix constraints.
```

This is now a more tractable target than the raw A14 prefix-trap dichotomy.

---

## Current status

Proved here:

1. minimal FIRST `2f` hit eliminates all proper-prefix equations `X_i=f`;
2. proper prefixes of the SECOND tail block cannot have sum `sigma-f` by Graham-validity;
3. the equal-sum proper-prefix trap equations are pruned to two main forbidden-hit families plus cross-collisions;
4. the SECOND boundary case `beta=h` is identified as a pair-trap boundary.

Not proved here:

1. the pruned prefix-trap dichotomy;
2. elimination of all equal-sum branches;
3. endpoint avoidance theorem.
