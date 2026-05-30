# Analytic Note: Template-Aware External Cancellation, T1

This note continues from `docs/PROOF_PROGRESS_CHECKPOINT.md`.

It attacks the first template-aware external cancellation subcase.

Claim boundary:

```text
This is a partial analytic note, not a complete proof of Erdős 475.
```

---

## Template T1

The clean first-blocker template is the general right blocker with length at least two.

Original local block:

```text
a, b, z, J
```

with

```text
sum(z,J) = -a,
sum(J) = -a-z.
```

Candidate move:

```text
a,b,z,J  ->  z,a,b,J.
```

The active block total is

```text
E = b.
```

Only two genuinely new relative partial-sum values are

```text
z,
z+a.
```

The move already removes the original forbidden relative value `a` unless an internal obstruction appears.

The known internal failures are:

```text
z = a+b,
z = b-a,
Y_s = -a-b,
Y_s = a-b,
```

where `Y_s` is a proper prefix of `J`.

This note studies the external collision at the first new value `z`.

---

## External collision normal form at `W=z`

For the proposed permutation

```text
pi(H) = z, a, b, J,
```

at the new prefix value

```text
W = z,
```

we have the split

```text
A = z,
B = a,b,J.
```

Since

```text
sum(J) = -a-z,
```

we have

```text
sum(B) = a+b+sum(J) = b-z.
```

Thus external collision normal form gives:

### Left external collision

There is an interval `K` immediately left of the active block such that

```text
sum(K) + z = 0.
```

### Right external collision

There is an interval `K` immediately right of the active block such that

```text
(b-z) + sum(K) = 0.
```

This note handles the first subcase:

```text
Left external collision at W=z with K a singleton.
```

---

## Subcase T1-Lz-1: left external collision at `z`, singleton `K`

Assume the left canceling interval is a singleton.

Then

```text
K = (-z).
```

The original combined block is

```text
-z, a, b, z, J.
```

Work relative to the basepoint before `-z`.

The original forbidden relative value is

```text
a-z,
```

because the original first forbidden hit occurs after the prefix

```text
-z, a.
```

The original total is

```text
-z + a + b + z + sum(J)
= -z + a + b + z - a - z
= b-z.
```

---

## Candidate repair for T1-Lz-1

Use the total-preserving move

```text
-z, a, b, z, J
   ->
z, a, b, -z, J.
```

The new total is

```text
z+a+b-z+sum(J)
= a+b-a-z
= b-z.
```

The new relative partial sums are

```text
z,
z+a,
z+a+b,
a+b,
a+b+Y_s,
...,
b-z.
```

The tail values

```text
a+b,
a+b+Y_s,
...,
b-z
```

already existed in the original ordering after the original prefix `-z,a,b,z`.

The genuinely new values are therefore

```text
z,
z+a,
z+a+b.
```

---

## Failure classification

The repair succeeds internally and avoids the forbidden value unless one of the following occurs.

### Forbidden-value hits

Forbidden relative value:

```text
a-z.
```

New values hit it if:

```text
z = a-z       -> 2z = a,
z+a = a-z     -> z = 0, impossible,
z+a+b = a-z   -> 2z+b = 0.
```

So genuine affine/singleton obstructions:

```text
2z = a,
2z+b = 0.
```

### Zero hits

```text
z = 0          impossible,
z+a = 0        -> z=-a, impossible because then sum(J)=0 and J is nonempty,
z+a+b = 0      -> z=-a-b.
```

Thus genuine affine/singleton obstruction:

```text
z = -a-b.
```

### Collisions with unchanged endpoint/tail values

The unchanged old tail values are

```text
a+b,
a+b+Y_s,
...,
b-z.
```

Collisions involving the new values give either affine/singleton conditions or shorter-prefix obstructions in `J`.

Representative equations:

```text
z = a+b                  -> affine singleton,
z = a+b+Y_s              -> Y_s = z-a-b,
z = b-z                  -> 2z = b,

z+a = a+b                -> z=b, impossible by distinctness,
z+a = a+b+Y_s            -> Y_s = z-b,
z+a = b-z                -> 2z+a-b = 0,

z+a+b = a+b              -> z=0, impossible,
z+a+b = a+b+Y_s          -> Y_s = z,
z+a+b = b-z              -> 2z+a = 0.
```

Therefore failures are contained in the following finite menu:

```text
Affine/singleton conditions:
  2z = a,
  2z+b = 0,
  z = -a-b,
  z = a+b,
  2z = b,
  2z+a-b = 0,
  2z+a = 0.

Shorter-prefix obstructions inside J:
  Y_s = z-a-b,
  Y_s = z-b,
  Y_s = z.

Impossible by nonzero/distinctness/Graham-validity:
  z = 0,
  z = b,
  z = -a with nonempty J.
```

Any remaining failure must be an external collision involving one of the genuinely new values

```text
z,
z+a,
z+a+b.
```

---

## Result of this subcase

### Lemma T1-Lz-1

In the T1 template, suppose the left external collision at `W=z` has singleton canceling interval `K=(-z)`.

Then the local move

```text
-z,a,b,z,J  ->  z,a,b,-z,J
```

is total-preserving and removes the original forbidden relative value `a-z`.

If it does not immediately give a valid endpoint-avoiding ordering, the failure is one of:

```text
1. an affine/singleton obstruction from the finite list above;
2. a proper-prefix obstruction inside J from the finite list above;
3. a further external collision involving z, z+a, or z+a+b;
4. an impossible nonzero/distinctness/Graham-validity violation.
```

This is a concrete template-aware reduction, not a bare `Left(T)` / `Right(T)` transition.

---

## Significance

This handles the first nontrivial external-child subcase after the external collision normal form correction.

It shows that at least in the singleton-left external collision branch of T1, the obstruction again reduces to the same types:

```text
success,
affine singleton,
shorter prefix,
further external cancellation,
impossible condition.
```

This supports the obstruction-tree program, but does not close it.

---

## Next subcases

Still needed for T1:

```text
T1-Lz-long:
  left external collision at W=z with K length >= 2.

T1-Rz:
  right external collision at W=z.

T1-Lza:
  left external collision at W=z+a.

T1-Rza:
  right external collision at W=z+a.
```

The most natural next target is `T1-Lz-long`: write the left canceling interval as

```text
K = K', y
```

with

```text
sum(K) = -z,
sum(K') = -z-y,
```

and try a total-preserving move on

```text
K', y, a, b, z, J.
```
