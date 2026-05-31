# Analytic Note: T1 Right External Cancellation at W=z, Singleton K

This note continues the template-aware external cancellation program from:

```text
docs/PROOF_PROGRESS_CHECKPOINT.md
docs/analytic_template_external_cancellation_t1.md
docs/analytic_template_external_cancellation_t1_lz_long.md
```

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

This note treats the right external collision at

```text
W = z
```

when the right canceling interval is a singleton.

---

## External collision normal form at W=z

At the new prefix value `W=z`, the proposed permutation splits as

```text
pi(H) = A,B = z, (a,b,J).
```

The suffix has sum

```text
sum(B) = a+b+sum(J) = a+b-a-z = b-z.
```

A right external collision gives an interval `K` immediately right of the active block with

```text
sum(B) + sum(K) = 0.
```

Thus

```text
sum(K) = z-b.
```

In this note assume the singleton case:

```text
K = (z-b).
```

The combined original local block is

```text
a,b,z,J,z-b.
```

The total is

```text
a+b+z+sum(J)+z-b
= a+b+z-a-z+z-b
= z.
```

The original forbidden relative value is still

```text
a.
```

---

## Candidate repair

Move the singleton canceling atom to the front:

```text
a,b,z,J,z-b
   ->
z-b,a,b,z,J.
```

The new total is

```text
(z-b)+a+b+z+sum(J)
= z-b+a+b+z-a-z
= z.
```

The new relative partial sums are

```text
z-b,
z+a-b,
z+a,
a+2z,
a+2z+Y_s,
...,
z,
```

where `Y_s` ranges over proper prefix sums of `J`.

The endpoint `z` is unchanged.

The genuinely new values before the final endpoint are

```text
N_0 = z-b,
N_1 = z+a-b,
N_2 = z+a,
N_3 = a+2z,
N_s = a+2z+Y_s.
```

---

## Forbidden-value hits

The forbidden relative value is

```text
F = a.
```

New values hit `F` only if

```text
z-b = a          -> z = a+b,
z+a-b = a        -> z = b,
z+a = a          -> z = 0,
a+2z = a         -> z = 0,
a+2z+Y_s = a     -> Y_s = -2z.
```

The conditions `z=b` and `z=0` are impossible by distinctness / nonzero atom hypotheses.

Thus the genuine outcomes are:

```text
Affine/singleton:
  z = a+b.

Proper-prefix obstruction inside J:
  Y_s = -2z.
```

---

## Zero hits

New values hit zero only if

```text
z-b = 0          -> z=b, impossible,
z+a-b = 0        -> z=b-a,
z+a = 0          -> z=-a,
a+2z = 0         -> 2z=-a,
a+2z+Y_s = 0     -> Y_s=-a-2z.
```

The condition `z=-a` implies

```text
sum(J) = -a-z = 0.
```

Since `J` is nonempty in the parent T1 setting, this would create a nonempty zero-sum interval and contradict Graham-validity.

Thus genuine outcomes are:

```text
Affine/singleton:
  z = b-a,
  2z = -a.

Proper-prefix obstruction inside J:
  Y_s = -a-2z.
```

---

## Internal collisions among fixed new values

Among

```text
z-b,
z+a-b,
z+a,
a+2z,
```

collisions force one of:

```text
a=0,
b=0,
z=0,
z=-a-b,
z=-b,
a+b=0.
```

The first three are impossible. The cases

```text
z=-a-b,
z=-b
```

are affine/singleton obstructions.

The condition

```text
a+b=0
```

is boundary-sensitive. If the local block is interior, it makes the partial sum after `a,b` equal the basepoint before `a`, contradicting Graham-validity. If the active block starts at the beginning of the whole ordering, relative zero may require separate boundary handling. For this note it is recorded as a boundary-sensitive affine/degenerate condition, not silently discarded.

---

## Collisions involving proper prefixes of J

Collisions between

```text
N_s = a+2z+Y_s
```

and earlier fixed new values give proper-prefix targets inside `J`:

```text
N_s = z-b       -> Y_s = -a-z-b,
N_s = z+a-b     -> Y_s = -z-b,
N_s = z+a       -> Y_s = -z,
N_s = a+2z      -> Y_s = 0.
```

The case `Y_s=0` would repeat a partial sum inside the original `J`-tail and is impossible by Graham-validity.

Thus genuine proper-prefix targets include:

```text
Y_s in {
  -a-z-b,
  -z-b,
  -z
}.
```

Collisions between two values of the form

```text
a+2z+Y_s,
a+2z+Y_t
```

would imply `Y_s=Y_t`, impossible for distinct prefix positions by Graham-validity.

---

## Collisions with old J-prefix values

Old J-prefix values in the original block have form

```text
a+b+z+Y_t.
```

A collision

```text
a+2z+Y_s = a+b+z+Y_t
```

gives

```text
Y_t - Y_s = z-b.
```

This means a nonempty subinterval of `J` has sum

```text
z-b
```

or

```text
b-z,
```

depending on the order of the two prefix positions.

Therefore this is not a terminal obstruction; it is a proper subinterval obstruction inside `J`.

This is an important difference from the left-collision branch: the right-collision branch naturally creates internal subinterval conditions, not just single-prefix conditions.

---

## Full reduction statement

### Lemma T1-Rz-1

In template T1, suppose the right external collision at `W=z` has singleton canceling interval

```text
K = (z-b).
```

Then the move

```text
a,b,z,J,z-b
   ->
z-b,a,b,z,J
```

is total-preserving and removes the forbidden relative value `a`.

If it does not produce a valid endpoint-avoiding local repair, every failure is one of the following:

```text
1. affine/singleton obstruction involving z,a,b;
2. proper-prefix obstruction inside J;
3. proper subinterval obstruction inside J;
4. further external cancellation involving one of the new values;
5. impossible nonzero, duplicate-atom, Graham-validity, or boundary-sensitive zero condition.
```

This is a template-aware reduction. It does not treat the external collision as a bare interval state.

---

## Significance

The singleton right-cancellation branch at `W=z` is tractable but already shows a new phenomenon:

```text
cross-prefix collisions inside J create proper subinterval obstructions.
```

That is acceptable for a descent framework, but it must be explicitly tracked.

---

## Remaining T1-Rz case

Still needed:

```text
T1-Rz-long:
  right external collision at W=z with K length >= 2.
```

If

```text
K = y,K'
```

with

```text
sum(K)=z-b,
sum(K')=z-b-y,
```

the analogous move to test is

```text
a,b,z,J,y,K'
   ->
y,a,b,z,J,K'.
```

The expected new complication is cross-prefix interaction between `J` and `K'`. This should be documented rather than hidden.
