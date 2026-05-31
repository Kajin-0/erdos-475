# Analytic Note: T1 Left External Cancellation at W=z+a, Long K

This note continues:

```text
docs/PROOF_PROGRESS_CHECKPOINT.md
docs/analytic_template_external_cancellation_t1_lza_singleton.md
```

Claim boundary:

```text
This is a partial analytic reduction note. It is not a complete proof of Erdős 475.
```

---

## Parent template T1

Parent template:

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

This note treats the left external collision at

```text
W = z+a
```

when the left canceling interval has length at least two.

---

## External collision normal form at W=z+a

At `W=z+a`, the proposed permutation splits as

```text
pi(H) = A,B = (z,a), (b,J).
```

A left external collision gives an interval `K` immediately left of the active block with

```text
sum(K) + z+a = 0.
```

So

```text
sum(K) = -z-a.
```

The singleton case `K=(-z-a)` is handled in:

```text
docs/analytic_template_external_cancellation_t1_lza_singleton.md
```

Now assume

```text
|K| >= 2.
```

Write

```text
K = K', y
```

where `y` is adjacent to the original active block. Then

```text
sum(K') = -z-a-y.
```

The original combined block is

```text
K', y, a, b, z, J.
```

Work relative to the basepoint before `K'`.

The original forbidden relative value is

```text
-z,
```

because after the prefix `K,a` the relative sum is

```text
sum(K)+a = -z-a+a = -z.
```

The total of the combined block is

```text
sum(K')+y+a+b+z+sum(J)
= (-z-a-y)+y+a+b+z-a-z
= b-a-z.
```

---

## Candidate repair

Use the total-preserving move

```text
K', y, a, b, z, J
   ->
K', z, a, b, y, J.
```

The new total is

```text
sum(K')+z+a+b+y+sum(J)
= (-z-a-y)+z+a+b+y-a-z
= b-a-z.
```

So all later partial sums are preserved.

The partial sums through `K'` are unchanged. After `K'`, the new relative values are

```text
-a-y,
-y,
b-y,
b,
b+Y_s,
...,
b-a-z,
```

where `Y_s` ranges over proper prefix sums of `J`.

The values

```text
b,
b+Y_s,
...,
b-a-z
```

already occurred in the original ordering after the old prefix `K',y,a,b,z`.

Therefore the genuinely new values are

```text
N_1 = -a-y,
N_2 = -y,
N_3 = b-y.
```

---

## Forbidden-value check

Forbidden relative value:

```text
F = -z.
```

The new values hit `F` only if

```text
-a-y = -z     -> y = z-a,
-y = -z       -> y = z,
b-y = -z      -> y = b+z.
```

The middle condition `y=z` is impossible by distinctness of `S` because `z` is already an atom in the active block.

Thus the genuine affine/singleton obstructions from forbidden hits are

```text
y = z-a,
y = b+z.
```

---

## Zero-hit check

The new values hit zero only if

```text
-a-y = 0      -> y = -a,
-y = 0        -> y = 0,
b-y = 0       -> y = b.
```

The conditions `y=0` and `y=b` are impossible by nonzero atom and distinctness assumptions.

The condition

```text
y = -a
```

is an affine/singleton obstruction. It is not automatically impossible here because `-a` need not be a singleton atom in the T1 parent template.

---

## Internal collisions among new values

Pairwise collisions among

```text
-a-y,
-y,
b-y
```

force one of:

```text
a=0,
b=0,
a+b=0.
```

The cases `a=0` and `b=0` are impossible.

The condition `a+b=0` is boundary-sensitive. If the relevant local block is interior, it makes the partial sum after `a,b` return to the local basepoint and contradicts Graham-validity. If the active block starts at the global beginning, relative zero requires separate boundary handling.

---

## Collisions with unchanged non-prefix values

The old non-prefix values after `K'` include

```text
-z-a,
-z,
b-z,
b,
b+Y_s,
...,
b-a-z.
```

The value `-z` is the forbidden value already handled.

Collisions of the new values with the remaining fixed old values give affine/singleton conditions.

A sufficient finite list is:

```text
y in {
  z-a,
  b+z,
  -a,
  z+a,
  a+b+z,
  z-a-b,
  z-b,
  -a-b,
  -b,
  a+z-b,
  a+z
}.
```

This list is intentionally conservative. Some entries may be impossible in special cases by distinctness or Graham-validity, but each listed case is a singleton/affine obstruction, not a new obstruction type.

---

## Collisions with proper prefixes of J

If a proper prefix `Y_s` of `J` collides with one of the new values, then

```text
-a-y = b+Y_s      -> Y_s = -a-b-y,
-y = b+Y_s        -> Y_s = -b-y,
b-y = b+Y_s       -> Y_s = -y.
```

Thus proper-prefix obstructions inside `J` are

```text
Y_s in {
  -a-b-y,
  -b-y,
  -y
}.
```

These are strictly shorter than the original `J` tail.

---

## Collisions with prefixes of K'

Let `X_s` be a proper prefix sum of `K'`.

Since

```text
sum(K') = -z-a-y,
```

collisions with the new values create proper suffix obstructions inside `K'`:

```text
X_s = -a-y     -> suffix(K') = -z,
X_s = -y       -> suffix(K') = -z-a,
X_s = b-y      -> suffix(K') = -z-a-b.
```

So proper-suffix obstructions inside `K'` have targets

```text
-z,
-z-a,
-z-a-b.
```

These are strictly shorter than the original left canceling interval `K`.

---

## Full reduction statement

### Lemma T1-Lza-long

In template T1, suppose the left external collision at `W=z+a` has a canceling interval

```text
K = K',y
```

with length at least two and

```text
sum(K) = -z-a.
```

Then the move

```text
K',y,a,b,z,J
   ->
K',z,a,b,y,J
```

is total-preserving and removes the forbidden relative value `-z`.

If it does not produce a valid endpoint-avoiding local repair, every failure is one of:

```text
1. an affine/singleton obstruction involving y and the local atoms;
2. a proper-prefix obstruction inside J;
3. a proper-suffix obstruction inside K';
4. a further external cancellation involving one of -a-y, -y, b-y;
5. an impossible nonzero, duplicate-atom, Graham-validity, or boundary-sensitive zero condition.
```

This is template-aware and does not treat the external collision as a bare interval state.

---

## Consequence for T1-Lza

Together with `T1-Lza-1`, this closes the left external collision branch at `W=z+a` for template T1 up to the standard finite menu:

```text
success,
affine singleton,
proper subinterval obstruction,
further external cancellation,
impossible condition.
```

---

## Remaining T1 branch

The only unworked parent external branch for T1 is now:

```text
T1-Rza:
  right external collision at W=z+a.
```

The next target should be its singleton case.
