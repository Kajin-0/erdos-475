# Analytic Note: T1 Left External Cancellation at W=z, Long K

This note continues `docs/analytic_template_external_cancellation_t1.md`.

Claim boundary:

```text
This is a partial analytic reduction note. It is not a complete proof of Erdős 475.
```

---

## Parent template T1

The parent template is the general right-blocker move with length at least two:

```text
a,b,z,J  ->  z,a,b,J
```

where

```text
sum(z,J) = -a,
sum(J) = -a-z.
```

The two genuinely new relative partial-sum values in the parent move are

```text
z,
z+a.
```

This note treats the left external collision at

```text
W = z
```

when the left canceling interval has length at least two.

---

## External collision normal form

At `W=z`, the proposed permutation is split as

```text
pi(H) = A,B = z, (a,b,J).
```

A left external collision gives an interval `K` immediately left of the active block with

```text
sum(K) + z = 0.
```

So

```text
sum(K) = -z.
```

The singleton case `K=(-z)` is handled in `docs/analytic_template_external_cancellation_t1.md`.

Now assume

```text
|K| >= 2.
```

Write

```text
K = K', y
```

where `y` is the atom of `K` adjacent to the original active block. Then

```text
sum(K') = -z-y.
```

The combined original local block is

```text
K', y, a, b, z, J.
```

Work relative to the basepoint before `K'`.

The original forbidden relative value is

```text
a-z,
```

because after `K,a` the relative sum is

```text
sum(K)+a = -z+a = a-z.
```

The total of the combined block is

```text
sum(K') + y + a+b+z+sum(J)
= (-z-y)+y+a+b+z+(-a-z)
= b-z.
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
sum(K') + z+a+b+y+sum(J)
= (-z-y)+z+a+b+y+(-a-z)
= b-z.
```

So all later partial sums are preserved.

The partial sums through `K'` are unchanged. After `K'`, the new relative values are

```text
-y,
a-y,
a+b-y,
a+b,
a+b+Y_s,
...,
b-z,
```

where `Y_s` ranges over proper prefix sums of `J`.

The values

```text
a+b,
a+b+Y_s,
...,
b-z
```

already occurred in the original ordering after the old prefix `K',y,a,b,z`.

Therefore the genuinely new values are

```text
N_1 = -y,
N_2 = a-y,
N_3 = a+b-y.
```

---

## Forbidden-value check

Forbidden relative value:

```text
F = a-z.
```

The new values hit `F` only if

```text
-y = a-z       -> y = z-a,
a-y = a-z      -> y = z,
a+b-y = a-z    -> y = b+z.
```

The middle condition `y=z` is impossible by distinctness of `S` because `z` is already an atom in the active block.

Thus genuine affine/singleton obstructions from forbidden hits are

```text
y = z-a,
y = b+z.
```

---

## Zero-hit check

The new values hit zero only if

```text
-y = 0         -> y = 0, impossible,
a-y = 0       -> y = a, duplicate atom,
a+b-y = 0     -> y = a+b.
```

Thus the only genuine zero-hit affine condition is

```text
y = a+b.
```

The condition `y=a` is impossible by distinctness because `a` is already a local atom.

---

## Internal collisions among new values

Pairwise collisions among

```text
-y,
a-y,
a+b-y
```

force

```text
a=0,
a+b=0,
b=0.
```

The cases `a=0` and `b=0` are impossible because `S subset F_p^*`.

The case `a+b=0` would make the original local partial sum after `a,b` equal the basepoint before `a`, contradicting Graham-validity. Thus it is impossible.

---

## Collisions with the unchanged endpoint/tail after `K'`

The unchanged endpoint/tail values after `K'` include

```text
-z,
a-z,
a+b-z,
a+b,
a+b+Y_s,
...,
b-z.
```

Here `a-z` is the forbidden value already handled above.

The finite affine/singleton conditions from collisions with the non-prefix unchanged values include:

```text
y = a+z,
y = a+b+z,
y = z-a-b,
y = z-b,
y = -a-b,
y = -b,
y = z-b,
y = a+z-b,
y = a+z,
y = a+b,
```

with repetitions allowed in the list. A cleaned unique sufficient list is

```text
y in {
  z-a,
  b+z,
  a+b,
  a+z,
  a+b+z,
  z-a-b,
  z-b,
  -a-b,
  -b,
  a+z-b
}.
```

This list is intentionally conservative. Some entries may be impossible in special cases by distinctness or by Graham-validity, but every listed condition is a singleton/affine obstruction and is not a new obstruction type.

---

## Collisions with proper prefixes of J

If a proper prefix `Y_s` of `J` collides with one of the new values, then

```text
-y = a+b+Y_s       -> Y_s = -a-b-y,
a-y = a+b+Y_s      -> Y_s = -b-y,
a+b-y = a+b+Y_s    -> Y_s = -y.
```

Thus proper-prefix obstructions inside `J` are:

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

If `X_s` equals a new value, then the suffix of `K'` after that prefix has a controlled target.

Since

```text
sum(K') = -z-y,
```

we get:

```text
X_s = -y       -> suffix(K') = -z,
X_s = a-y      -> suffix(K') = -a-z,
X_s = a+b-y    -> suffix(K') = -a-b-z.
```

Thus proper-suffix obstructions inside `K'` are:

```text
-z,
-a-z,
-a-b-z.
```

These are strictly shorter than the original left canceling interval `K`.

---

## Full reduction statement

### Lemma T1-Lz-long

In template T1, suppose the left external collision at `W=z` has a canceling interval

```text
K = K',y
```

with length at least two and

```text
sum(K) = -z.
```

Then the move

```text
K',y,a,b,z,J
   ->
K',z,a,b,y,J
```

is total-preserving and removes the forbidden relative value `a-z`.

If it does not produce a valid endpoint-avoiding local repair, every failure is one of the following:

```text
1. an affine/singleton obstruction involving y and the local atoms;
2. a proper-prefix obstruction inside J;
3. a proper-suffix obstruction inside K';
4. a further external cancellation involving one of -y, a-y, a+b-y;
5. an impossible nonzero, duplicate-atom, or Graham-validity violation.
```

This is a template-aware reduction. It does not treat the external collision as a bare interval state.

---

## Consequence for T1-Lz

Together with the singleton case in `docs/analytic_template_external_cancellation_t1.md`, this closes the left external collision branch at `W=z` for template T1 up to the standard finite menu:

```text
success,
affine singleton,
proper subinterval obstruction,
further external cancellation,
impossible condition.
```

---

## Remaining T1 external branches

Still needed:

```text
T1-Rz:
  right external collision at W=z.

T1-Lza:
  left external collision at W=z+a.

T1-Rza:
  right external collision at W=z+a.
```

The next most natural target is `T1-Rz`, because it is the right-side analogue of this note.
