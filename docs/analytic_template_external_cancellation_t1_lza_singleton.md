# Analytic Note: T1 Left External Cancellation at W=z+a, Singleton K

This note continues the template-aware external cancellation program from:

```text
docs/PROOF_PROGRESS_CHECKPOINT.md
docs/analytic_template_external_cancellation_t1.md
docs/analytic_template_external_cancellation_t1_lz_long.md
docs/analytic_template_external_cancellation_t1_rz_singleton.md
docs/analytic_template_bridge_routing_t1_rz.md
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

The genuinely new values in the parent move are

```text
z,
z+a.
```

This note treats the left external collision at

```text
W = z+a
```

when the left canceling interval is a singleton.

---

## External collision normal form at W=z+a

At `W=z+a`, the proposed permutation splits as

```text
pi(H) = A,B = (z,a), (b,J).
```

A left external collision gives an interval `K` immediately left of the active block with

```text
sum(K) + z + a = 0.
```

In this note assume the singleton case:

```text
K = ( -z-a ).
```

The combined original local block is

```text
-z-a, a, b, z, J.
```

Work relative to the basepoint before `-z-a`.

The original forbidden relative value is

```text
-z,
```

because the original first forbidden hit occurs after the prefix

```text
-z-a, a.
```

The total of the combined block is

```text
(-z-a)+a+b+z+sum(J)
= b-a-z.
```

---

## Candidate repair

Use the total-preserving move

```text
-z-a, a, b, z, J
   ->
z, a, b, -z-a, J.
```

The new total is

```text
z+a+b-z-a+sum(J)
= b-a-z.
```

The new relative partial sums are

```text
z,
z+a,
z+a+b,
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

already occurred in the original block after the old prefix `-z-a,a,b,z`.

Therefore the genuinely new values are

```text
N_0 = z,
N_1 = z+a,
N_2 = z+a+b.
```

---

## Forbidden-value hits

The forbidden relative value is

```text
F = -z.
```

The new values hit `F` only if

```text
z = -z          -> 2z=0, impossible for odd p and z != 0,
z+a = -z        -> 2z+a=0,
z+a+b = -z      -> 2z+a+b=0.
```

Thus genuine affine/singleton obstructions are

```text
2z+a=0,
2z+a+b=0.
```

---

## Zero hits

The new values hit zero only if

```text
z = 0           impossible,
z+a = 0         -> z=-a,
z+a+b = 0       -> z=-a-b.
```

The condition `z=-a` implies

```text
sum(J)=0.
```

Since `J` is nonempty in template T1, this creates a nonempty zero-sum interval and contradicts Graham-validity.

Thus the genuine zero-hit affine obstruction is

```text
z=-a-b.
```

---

## Fixed internal collisions

Among

```text
z,
z+a,
z+a+b,
```

collisions force one of

```text
a=0,
b=0,
a+b=0.
```

The first two are impossible. The condition `a+b=0` is boundary-sensitive: if the local block is interior, then the original partial sum after `a,b` returns to the active basepoint; if the active block starts at the global beginning, relative zero needs separate boundary treatment. This is recorded as a boundary-sensitive degeneracy, not silently discarded.

---

## Collisions with unchanged tail values

The unchanged tail values are

```text
b,
b+Y_s,
...,
b-a-z.
```

Collisions give the following finite menu.

### Collision of `z` with tail

```text
z = b              -> duplicate atom b, impossible,
z = b+Y_s          -> Y_s = z-b,
z = b-a-z          -> 2z = b-a.
```

### Collision of `z+a` with tail

```text
z+a = b            -> z = b-a,
z+a = b+Y_s        -> Y_s = z+a-b,
z+a = b-a-z        -> 2z+2a-b=0.
```

### Collision of `z+a+b` with tail

```text
z+a+b = b          -> z=-a, impossible by zero-sum J,
z+a+b = b+Y_s      -> Y_s = z+a,
z+a+b = b-a-z      -> z=-a, impossible by zero-sum J.
```

Thus failures are contained in:

```text
Affine/singleton:
  2z+a=0,
  2z+a+b=0,
  z=-a-b,
  2z=b-a,
  z=b-a,
  2z+2a-b=0.

Proper-prefix obstructions inside J:
  Y_s = z-b,
  Y_s = z+a-b,
  Y_s = z+a.

Impossible / boundary-sensitive:
  z=0,
  z=b,
  z=-a with nonempty J,
  a=0,
  b=0,
  a+b=0 boundary-sensitive.
```

Any remaining failure must be an external cancellation involving one of the genuinely new values

```text
z,
z+a,
z+a+b.
```

---

## Full reduction statement

### Lemma T1-Lza-1

In template T1, suppose the left external collision at `W=z+a` has singleton canceling interval

```text
K=(-z-a).
```

Then the move

```text
-z-a,a,b,z,J
   ->
z,a,b,-z-a,J
```

is total-preserving and removes the forbidden relative value `-z`.

If it does not produce a valid endpoint-avoiding local repair, every failure is one of:

```text
1. affine/singleton obstruction;
2. proper-prefix obstruction inside J;
3. further external cancellation involving z, z+a, or z+a+b;
4. impossible nonzero, duplicate-atom, Graham-validity, or boundary-sensitive zero condition.
```

This is template-aware and does not treat the external collision as a bare interval state.

---

## Significance

This closes the singleton-left external collision at the second new value `z+a` for template T1.

Together with the earlier T1 notes, the currently handled singleton branches are:

```text
T1-Lz-1,
T1-Rz-1,
T1-Lza-1.
```

---

## Remaining T1 branches

Still needed:

```text
T1-Lza-long:
  left external collision at W=z+a with K length >= 2.

T1-Rza:
  right external collision at W=z+a.
```

The next natural target is `T1-Lza-long`, the long analogue of this note.
