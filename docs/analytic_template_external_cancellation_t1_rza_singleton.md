# Analytic Note: T1 Right External Cancellation at W=z+a, Singleton K

This note continues the template-aware external cancellation program.

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

This note treats the right external collision at

```text
W = z+a
```

when the right canceling interval is a singleton.

---

## External collision normal form at W=z+a

At `W=z+a`, the proposed permutation splits as

```text
pi(H) = A,B = (z,a), (b,J).
```

The suffix has sum

```text
sum(B) = b+sum(J) = b-a-z.
```

A right external collision gives an interval `K` immediately right of the active block with

```text
sum(B)+sum(K)=0.
```

Thus

```text
sum(K)=z+a-b.
```

In this note assume the singleton case:

```text
K=(z+a-b).
```

The combined original local block is

```text
a,b,z,J,z+a-b.
```

The total is

```text
a+b+z+sum(J)+z+a-b
= a+b+z-a-z+z+a-b
= z+a.
```

The original forbidden relative value is still

```text
a.
```

---

## Candidate repair

Move the singleton canceling atom to the front:

```text
a,b,z,J,z+a-b
   ->
z+a-b,a,b,z,J.
```

The new total is

```text
(z+a-b)+a+b+z+sum(J)
= z+a-b+a+b+z-a-z
= z+a.
```

The new relative partial sums are

```text
z+a-b,
z+2a-b,
z+2a,
2z+2a,
2z+2a+Y_s,
...,
z+a,
```

where `Y_s` ranges over proper prefix sums of `J`.

The final endpoint `z+a` is unchanged.

The genuinely new values before the final endpoint are

```text
N_0 = z+a-b,
N_1 = z+2a-b,
N_2 = z+2a,
N_3 = 2z+2a,
N_s = 2z+2a+Y_s.
```

---

## Forbidden-value hits

The forbidden relative value is

```text
F=a.
```

New values hit `F` only if

```text
z+a-b = a          -> z=b, impossible by distinctness,
z+2a-b = a        -> z=b-a,
z+2a = a          -> z=-a,
2z+2a = a         -> 2z+a=0,
2z+2a+Y_s = a     -> Y_s=-2z-a.
```

The condition `z=-a` implies

```text
sum(J)=0,
```

and since `J` is nonempty in T1, this contradicts Graham-validity.

Thus genuine outcomes are:

```text
Affine/singleton:
  z=b-a,
  2z+a=0.

Proper-prefix obstruction inside J:
  Y_s=-2z-a.
```

---

## Zero hits

New values hit zero only if

```text
z+a-b = 0          -> z=b-a,
z+2a-b = 0        -> z=b-2a,
z+2a = 0          -> z=-2a,
2z+2a = 0         -> z=-a,
2z+2a+Y_s = 0     -> Y_s=-2z-2a.
```

Again `z=-a` gives `sum(J)=0` and is impossible by Graham-validity.

Thus genuine outcomes are:

```text
Affine/singleton:
  z=b-a,
  z=b-2a,
  z=-2a.

Proper-prefix obstruction inside J:
  Y_s=-2z-2a.
```

---

## Fixed internal collisions

Among the fixed new values

```text
z+a-b,
z+2a-b,
z+2a,
2z+2a,
```

collisions force one of:

```text
a=0,
b=0,
z=0,
a+b=0,
z=-a-b,
z=-b.
```

The first three are impossible. The cases

```text
a+b=0,
z=-a-b,
z=-b
```

are boundary-sensitive or affine/singleton obstructions. In particular, `a+b=0` usually gives a local relative-zero partial sum in an interior block and must be handled by boundary rules rather than silently discarded.

---

## Collisions with old fixed values

Old fixed values from the original combined block include

```text
a,
a+b,
a+b+z,
b,
z+a.
```

The value `a` is the forbidden value already handled. The final endpoint `z+a` is unchanged.

Collisions of fixed new values with the remaining fixed old values yield only affine/singleton or impossible conditions. A sufficient conservative list is:

```text
z in {
  b-a,
  b-2a,
  -2a,
  -a-b,
  -b,
  a+b,
  2b,
  2b-a,
  2b-2a
}
```

plus scalar/boundary degeneracies such as

```text
a+b=0,
a=2b.
```

This list is intentionally conservative. The point is that these are singleton/affine cases, not a new obstruction type.

---

## Collisions involving proper prefixes of J

The new J-family is

```text
2z+2a+Y_s.
```

Collisions with old fixed values give proper-prefix targets inside `J`:

```text
2z+2a+Y_s = a+b      -> Y_s=-2z-a+b,
2z+2a+Y_s = a+b+z    -> Y_s=-z-a+b,
2z+2a+Y_s = b        -> Y_s=-2z-2a+b,
2z+2a+Y_s = z+a      -> Y_s=-z-a.
```

Together with forbidden and zero hits, proper-prefix targets include:

```text
Y_s in {
  -2z-a,
  -2z-2a,
  -2z-a+b,
  -z-a+b,
  -2z-2a+b,
  -z-a
}.
```

---

## Cross-prefix collisions inside J

Old J-prefix values have form

```text
a+b+z+Y_t.
```

A collision

```text
2z+2a+Y_s = a+b+z+Y_t
```

gives

```text
Y_t - Y_s = z+a-b.
```

This means a nonempty subinterval of `J` has sum

```text
z+a-b
```

or

```text
b-a-z,
```

depending on the order of the two prefix positions.

Thus cross-prefix collisions inside `J` produce a proper internal subinterval obstruction, not a terminal obstruction.

---

## Full reduction statement

### Lemma T1-Rza-1

In template T1, suppose the right external collision at `W=z+a` has singleton canceling interval

```text
K=(z+a-b).
```

Then the move

```text
a,b,z,J,z+a-b
   ->
z+a-b,a,b,z,J
```

is total-preserving and removes the forbidden relative value `a`.

If it does not produce a valid endpoint-avoiding local repair, every failure is one of:

```text
1. affine/singleton obstruction involving z,a,b;
2. proper-prefix obstruction inside J;
3. proper internal subinterval obstruction inside J;
4. further external cancellation involving one of the new values;
5. impossible nonzero, duplicate-atom, Graham-validity, or boundary-sensitive zero condition.
```

This is template-aware and does not treat the external collision as a bare interval state.

---

## Significance

This closes the singleton right external collision at the second new value `z+a` for template T1.

Together with previous notes, every singleton external-child branch of T1 is now documented:

```text
T1-Lz-1,
T1-Rz-1,
T1-Lza-1,
T1-Rza-1.
```

---

## Remaining T1 work

The only remaining unworked branch for T1 is now:

```text
T1-Rza-long:
  right external collision at W=z+a with K length >= 2.
```

Based on the T1-Rz-long analysis, expect cross-bridge equations between `J` and the right tail `K'`. These should likely route into the bridge/gap framework rather than be treated as ordinary prefix descent.
