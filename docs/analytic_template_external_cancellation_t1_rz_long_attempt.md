# Analytic Note: T1 Right External Cancellation at W=z, Long K Attempt

This note continues:

```text
docs/PROOF_PROGRESS_CHECKPOINT.md
docs/analytic_template_external_cancellation_t1.md
docs/analytic_template_external_cancellation_t1_lz_long.md
docs/analytic_template_external_cancellation_t1_rz_singleton.md
```

Claim boundary:

```text
This note records a serious partial analysis and a newly exposed gap.
It does not close the T1-Rz-long case.
It is not a proof of Erdős 475.
```

---

## Parent template T1

The parent template is

```text
a,b,z,J  ->  z,a,b,J
```

with

```text
sum(z,J) = -a,
sum(J) = -a-z.
```

The parent move has genuinely new values

```text
z,
z+a.
```

This note studies the right external collision at

```text
W = z.
```

At `W=z`, the proposed permutation splits as

```text
pi(H) = A,B = z, (a,b,J).
```

The suffix sum is

```text
sum(B) = a+b+sum(J) = b-z.
```

A right external collision therefore gives an interval `K` immediately to the right of the active block with

```text
sum(K) = z-b.
```

The singleton case

```text
K = (z-b)
```

is handled in `docs/analytic_template_external_cancellation_t1_rz_singleton.md`.

Now assume

```text
|K| >= 2.
```

Write

```text
K = y,K'
```

with `y` adjacent to the original active block and

```text
sum(K') = z-b-y.
```

The original combined block is

```text
a,b,z,J,y,K'.
```

The original forbidden relative value is still

```text
a.
```

The total of the combined block is

```text
a+b+z+sum(J)+y+sum(K')
= a+b+z-a-z+y+z-b-y
= z.
```

---

## Candidate move tested

The natural analogue of the singleton repair is to move `y` to the front:

```text
a,b,z,J,y,K'
   ->
y,a,b,z,J,K'.
```

The total is preserved:

```text
y+a+b+z+sum(J)+sum(K')
= y+a+b+z-a-z+z-b-y
= z.
```

New relative partial sums are

```text
y,
y+a,
y+a+b,
y+a+b+z,
y+a+b+z+Y_s,
...,
y+b,
y+b+U_t,
...,
z,
```

where:

```text
Y_s = proper prefix sums of J,
U_t = proper prefix sums of K'.
```

The values

```text
y+b,
y+b+U_t,
...,
z
```

already occurred in the original block after the old prefix through `J,y,K'`.

The main genuinely new fixed values are

```text
y,
y+a,
y+a+b,
y+a+b+z,
```

and the new J-prefix family

```text
y+a+b+z+Y_s.
```

---

## Basic forbidden-value reduction

The forbidden relative value is

```text
F = a.
```

The new fixed values hit `F` only under affine/singleton conditions:

```text
y = a              -> duplicate atom a,
y+a = a            -> y=0,
y+a+b = a          -> y=-b,
y+a+b+z = a        -> y=-b-z.
```

The first two are impossible by distinctness/nonzero. The latter two are affine/singleton conditions.

The J-prefix family hits `F` if

```text
y+a+b+z+Y_s = a
```

so

```text
Y_s = -y-b-z.
```

This is a proper-prefix obstruction inside `J`.

---

## Basic zero-hit reduction

New fixed values hit zero under:

```text
y=0,
y=-a,
y=-a-b,
y=-a-b-z.
```

The first is impossible. The others are affine/singleton or boundary-sensitive zero obstructions.

The J-prefix family hits zero if

```text
Y_s = -a-b-z-y.
```

This is a proper-prefix obstruction inside `J`.

---

## Fixed-value internal collisions

Among

```text
y,
y+a,
y+a+b,
y+a+b+z,
```

collisions force one of:

```text
a=0,
b=0,
z=0,
a+b=0,
b+z=0,
a+b+z=0.
```

The first three are impossible. The remaining cases are affine/degenerate conditions:

```text
a+b=0,
z=-b,
z=-a-b.
```

The condition `a+b=0` is boundary-sensitive: if the relevant block is interior, it forces a relative zero partial sum; if the whole block begins at the global start, it needs separate treatment.

---

## Prefix reductions inside J

Collisions between the J-prefix family

```text
y+a+b+z+Y_s
```

and the fixed new values give proper-prefix conditions:

```text
y+a+b+z+Y_s = y              -> Y_s=-a-b-z,
y+a+b+z+Y_s = y+a            -> Y_s=-b-z,
y+a+b+z+Y_s = y+a+b          -> Y_s=-z,
y+a+b+z+Y_s = y+a+b+z        -> Y_s=0.
```

The `Y_s=0` case contradicts Graham-validity for a nonempty proper prefix. The other three are proper-prefix obstructions inside `J`.

---

## New obstacle: cross-prefix bridge between J and K'

The serious new phenomenon appears when the new J-prefix family collides with the old K'-tail values.

Old K'-tail values have form

```text
y+b+U_t,
```

where `U_t` is a proper prefix sum of `K'`.

A collision

```text
y+a+b+z+Y_s = y+b+U_t
```

gives

```text
U_t - Y_s = a+z.
```

Equivalently,

```text
U_t = Y_s + a+z.
```

This is not a simple prefix obstruction in one interval.

It relates a prefix of `J` to a prefix of `K'`, two separated intervals.

This should be recorded as a **bridge obstruction**:

```text
Bridge(J,K'; a+z):
  U_t - Y_s = a+z.
```

Depending on the order of `s,t`, this can sometimes be converted into a subinterval obstruction only if `J` and `K'` are adjacent in the relevant ordering. In the original ordering they are separated by `y`; in the proposed ordering they are adjacent only after the moved block, and the proof is currently fixed-ordering based.

Therefore this is not safely closed by the existing prefix/suffix descent framework.

---

## Attempt status

The candidate move

```text
a,b,z,J,y,K'
   ->
y,a,b,z,J,K'
```

reduces many failures to the expected finite menu:

```text
affine/singleton obstruction,
proper prefix inside J,
impossible condition,
further external cancellation.
```

However, it also introduces a new bridge condition:

```text
U_t - Y_s = a+z,
```

between prefixes of `J` and `K'`.

This bridge condition is not currently handled by the existing termination theory.

---

## Current conclusion for T1-Rz-long

The T1-Rz-long case is **not closed**.

A future proof must do one of the following:

```text
1. find a different local move avoiding cross-prefix bridge terms;
2. prove bridge obstructions descend by a new measure;
3. show the bridge equation forces affine/singleton or zero-sum contradiction;
4. extend the obstruction-tree state space to include bridge states and prove termination.
```

This is currently the highest-value gap discovered in the template-aware external-cancellation program.

---

## Significant-result status

This note is significant because it prevents an unsafe overclaim.

The earlier bare `Left(T)` / `Right(T)` framework would have hidden this bridge obstruction. The template-aware framework exposes it.

The proof effort should now focus on this bridge issue before claiming a complete external-collision closure.
