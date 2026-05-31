# Analytic Theorem Note: Generic Interval Splitting Templates

This note packages the length-at-least-two generic interval splitting templates used after singleton blocker routing.

Claim boundary:

```text
This is a local splitting theorem note, not a complete proof of Erdős 475.
External outputs are routed to template-aware cancellation states, not declared solved automatically.
```

---

## Purpose

Earlier notes introduced reusable length-one interval templates:

```text
GEN-L1: T,a,b,-a -> b,a,T,-a.
GEN-R1: a,b,-a,T -> b,-a,T,a.
```

This file packages the length-at-least-two analogues:

```text
GEN-L>=2: left interval I with sum T.
GEN-R>=2: right interval D with sum T.
```

These modules are needed by:

```text
T3 external routing,
T4 mirror routing,
affine/singleton routing,
future obstruction-tree termination packaging.
```

---

# GEN-L>=2: generic left interval splitting

## Setup

Local form:

```text
I, a, b, -a
```

with

```text
sum(I)=T,
|I|>=2.
```

Write

```text
I=z,J,
sum(J)=T-z.
```

Let `Y_s` denote a proper prefix sum of `J`.

Original relative partial sums include:

```text
z,
z+Y_s,
T,
T+a,
T+a+b,
T+b.
```

Forbidden relative value:

```text
F=T+a.
```

Candidate splitting move:

```text
z,J,a,b,-a
   ->
z,a,b,J,-a.
```

The active block total is preserved:

```text
T+b.
```

New relative partial sums:

```text
z,
z+a,
z+a+b,
z+a+b+Y_s,
T+a+b,
T+b.
```

The endpoint values

```text
T+a+b,
T+b
```

already occurred before.

The genuinely new fixed values are

```text
z+a,
z+a+b,
```

and the new prefix family is

```text
z+a+b+Y_s.
```

---

## GEN-L internal failure classification

Any internal failure must involve one of

```text
z+a,
z+a+b,
z+a+b+Y_s.
```

### Affine/singleton conditions

Collisions or forbidden/zero hits involving only `z,T,a,b` give a finite affine list. A conservative sufficient list is:

```text
z in {
  -a,
  -a-b,
  T,
  T-b,
  T-a,
  T-a-b,
  T+b,
  T+b-a
}.
```

Some entries are impossible or duplicate in special cases. The point is that they are singleton/affine routes, not new obstruction classes.

### Proper-prefix obstructions inside J

Collisions involving a proper prefix `Y_s` of `J` give targets contained in:

```text
Y_s in {
  -z-a-b,
  T-z-b,
  -a-b,
  -b,
  T-z-a-b,
  T-z-a
}.
```

Each such `Y_s` is a proper-prefix obstruction inside `J`, hence strictly smaller than the original left interval `I`.

### Cross-prefix collisions inside J

If two values of the new family

```text
z+a+b+Y_s,
z+a+b+Y_t
```

collide, then `Y_s=Y_t`, impossible for distinct prefix positions by Graham-validity of the original ordering.

If the new family collides with old interval-prefix values `z+Y_t`, then equations of the form

```text
z+a+b+Y_s = z+Y_t
```

give

```text
Y_t - Y_s = a+b.
```

This means a proper internal subinterval of `J` has sum `a+b` or `-a-b`, depending on prefix order.

Thus these collisions route to a proper internal subinterval obstruction inside `J`.

---

## GEN-L external outputs

External collision can occur at a newly created value. Using the template-aware normal form, each such collision is recorded by the proposed split `A,B`.

### At W=z+a

Proposed split:

```text
A=(z,a),
B=(b,J,-a).
```

The suffix sum is

```text
sum(B)=b+sum(J)-a = b+T-z-a.
```

External normal forms:

```text
Left cancellation:
  K+(z,a)=0,
  sum(K)=-z-a.

Right cancellation:
  (b,J,-a)+K=0,
  sum(K)=z+a-b-T.
```

Old shorthand:

```text
Left(-z-a),
Right(z+a-T-b).
```

### At W=z+a+b

Proposed split:

```text
A=(z,a,b),
B=(J,-a).
```

The suffix sum is

```text
sum(B)=T-z-a.
```

External normal forms:

```text
Left cancellation:
  K+(z,a,b)=0,
  sum(K)=-z-a-b.

Right cancellation:
  (J,-a)+K=0,
  sum(K)=z+a-T.
```

Old shorthand:

```text
Left(-z-a-b),
Right(z+a-T).
```

### At W=z+a+b+Y_s

Let `J_s^-` be the prefix of `J` with sum `Y_s`, and `J_s^+` be the suffix after that prefix.

Proposed split:

```text
A=(z,a,b,J_s^-),
B=(J_s^+,-a).
```

External normal forms:

```text
Left cancellation:
  K+(z,a,b,J_s^-)=0,
  sum(K)=-z-a-b-Y_s.

Right cancellation:
  (J_s^+,-a)+K=0,
  sum(K)=z+a+Y_s-T.
```

Old shorthand:

```text
Left(-z-a-b-Y_s),
Right(z+a+Y_s-T).
```

These are not bare interval states; they are template-aware cancellation states.

---

## GEN-L>=2 theorem

For the generic left splitting move

```text
z,J,a,b,-a -> z,a,b,J,-a,
```

with `sum(z,J)=T` and `|I|>=2`, every failure routes to one of:

```text
1. affine/singleton obstruction;
2. proper prefix or proper internal subinterval obstruction inside J;
3. template-aware external cancellation at one of the displayed new values;
4. impossible nonzero, duplicate-atom, Graham-validity, or boundary-sensitive condition.
```

No other local obstruction type occurs.

---

# GEN-R>=2: generic right interval splitting

## Setup

Local form:

```text
a, b, -a, D
```

with

```text
sum(D)=T,
|D|>=2.
```

Write

```text
D=z,J,
sum(J)=T-z.
```

Let `Y_s` denote a proper prefix sum of `J`.

Original relative partial sums:

```text
a,
a+b,
b,
b+z,
b+z+Y_s,
...,
b+T.
```

Forbidden relative value:

```text
F=a.
```

Candidate splitting move:

```text
a,b,-a,z,J
   ->
z,a,b,-a,J.
```

The active block total is preserved:

```text
b+T.
```

New relative partial sums:

```text
z,
z+a,
z+a+b,
z+b,
z+b+Y_s,
...,
b+T.
```

The tail values

```text
z+b,
z+b+Y_s,
...,
b+T
```

already occurred in the original ordering.

The genuinely new values are therefore

```text
z,
z+a,
z+a+b.
```

---

## GEN-R internal failure classification

Any internal failure must involve one of

```text
z,
z+a,
z+a+b.
```

### Affine/singleton conditions

A conservative sufficient affine list is:

```text
z in {
  a,
  -a,
  -b,
  -a-b,
  b,
  b-a,
  T,
  b+T,
  T-a,
  T-a-b
}.
```

Some entries are impossible or duplicate in special cases. They are recorded as affine/singleton routes, not terminal obstructions.

### Proper-prefix obstructions inside J

Collisions of new fixed values with the unchanged tail family

```text
z+b+Y_s
```

give:

```text
z = z+b+Y_s       -> Y_s=-b,
z+a = z+b+Y_s     -> Y_s=a-b,
z+a+b = z+b+Y_s   -> Y_s=a.
```

Thus proper-prefix targets inside `J` are:

```text
Y_s in {-b, a-b, a}.
```

These are strictly shorter than the original right interval `D`.

### Cross-prefix collisions inside J

The unchanged tail family is inherited from the original ordering. Collisions within it would already have existed in the original Graham-valid ordering, so they are impossible. Collisions among the three fixed new values give only affine/impossible cases already included above.

---

## GEN-R external outputs

Use template-aware external collision normal form.

The active block total is

```text
E=b+T.
```

### At W=z

Proposed split:

```text
A=(z),
B=(a,b,-a,J).
```

Suffix sum:

```text
sum(B)=b+T-z.
```

External normal forms:

```text
Left cancellation:
  K+(z)=0,
  sum(K)=-z.

Right cancellation:
  (a,b,-a,J)+K=0,
  sum(K)=z-b-T.
```

Old shorthand:

```text
Left(-z),
Right(z-b-T).
```

### At W=z+a

Proposed split:

```text
A=(z,a),
B=(b,-a,J).
```

Suffix sum:

```text
sum(B)=b-a+T-z.
```

External normal forms:

```text
Left cancellation:
  K+(z,a)=0,
  sum(K)=-z-a.

Right cancellation:
  (b,-a,J)+K=0,
  sum(K)=z+a-b-T.
```

Old shorthand:

```text
Left(-z-a),
Right(z+a-b-T).
```

### At W=z+a+b

Proposed split:

```text
A=(z,a,b),
B=(-a,J).
```

Suffix sum:

```text
sum(B)=T-z-a.
```

External normal forms:

```text
Left cancellation:
  K+(z,a,b)=0,
  sum(K)=-z-a-b.

Right cancellation:
  (-a,J)+K=0,
  sum(K)=z+a-T.
```

Old shorthand:

```text
Left(-z-a-b),
Right(z+a-T).
```

---

## GEN-R>=2 theorem

For the generic right splitting move

```text
a,b,-a,z,J -> z,a,b,-a,J,
```

with `sum(z,J)=T` and `|D|>=2`, every failure routes to one of:

```text
1. affine/singleton obstruction;
2. proper prefix obstruction inside J;
3. template-aware external cancellation at one of the displayed new values;
4. impossible nonzero, duplicate-atom, Graham-validity, or boundary-sensitive condition.
```

No other local obstruction type occurs.

---

## Consequence for T3/T4 routing

T3 routes external branches to primitive interval states:

```text
Left(a),
Left(a-b),
Right(-a-b),
Right(-a).
```

For nonduplicate targets with interval length at least two, GEN-L>=2 and GEN-R>=2 are the reusable splitting modules.

Duplicate targets still need dedicated duplicate modules, or a proof that they are special cases of GEN-L/GEN-R with stronger length-one exclusion.

---

## Remaining interval modules

Still needed:

```text
DUP-L:
  duplicate-left interval target, e.g. Left(a).

DUP-R:
  duplicate-right interval target, e.g. Right(-a).
```

These are expected to be special cases of the generic splitting modules plus the lemma that duplicate targets cannot have length one.
