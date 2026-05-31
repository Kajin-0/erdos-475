# Analytic Theorem Note: Generic Interval Length-One Templates

This note packages the generic length-one interval templates used by the singleton blocker routing notes.

Claim boundary:

```text
This is a local template theorem note, not a complete proof of Erdős 475.
The global obstruction-tree termination theorem remains open.
```

---

## Purpose

The right singleton blocker template T3 routes its external children to primitive interval states such as

```text
Left(a-b),
Right(-a-b),
Left(a),
Right(-a).
```

The nonduplicate length-one cases need reusable local lemmas.

This note records the two generic length-one templates:

```text
GEN-L1: left length-one target T.
GEN-R1: right length-one target T.
```

All external outcomes are recorded in template-aware cancellation form, not as bare `Left(T)` / `Right(T)` states.

---

# GEN-L1: generic left length-one interval

## Setup

Local block:

```text
T, a, b, -a
```

where the singleton interval has target `T` and

```text
T notin {0,a,b,-a}
```

unless explicitly routed as a duplicate/impossible case.

Original relative partial sums:

```text
T,
T+a,
T+a+b,
T+b.
```

Forbidden relative value:

```text
F = T+a.
```

Active block total:

```text
E = T+b.
```

Candidate move:

```text
T,a,b,-a  ->  b,a,T,-a.
```

New relative partial sums:

```text
b,
a+b,
a+b+T,
b+T.
```

The values

```text
a+b+T = T+a+b,
b+T = T+b
```

already occurred in the original block. Therefore the genuinely new values are

```text
W_1=b,
W_2=a+b.
```

---

## Internal classification

### Forbidden hits

```text
b = T+a        -> T=b-a,
a+b = T+a      -> T=b,
```

where `T=b` is a duplicate-target case, excluded in the nonduplicate generic branch.

Thus the genuine nonduplicate obstruction is

```text
T=b-a.
```

### Zero hits

The new values or unchanged endpoint values hit relative zero only under:

```text
b=0             impossible,
a+b=0           -> b=-a, duplicate of local -a,
a+b+T=0         -> T=-a-b,
b+T=0           -> T=-b.
```

Thus genuine affine/singleton zero obstructions are

```text
T=-a-b,
T=-b.
```

### Internal collisions

Pairwise collisions among the new and unchanged local values force only:

```text
a=0,
T=0,
T=a,
T=-a,
```

or other duplicate/impossible conditions already excluded.

Therefore the GEN-L1 internal exceptional set is contained in

```text
T in {b-a, -a-b, -b}
```

plus duplicate/impossible cases.

---

## External collision normal forms

External failures can occur only at the genuinely new values

```text
W_1=b,
W_2=a+b.
```

### At W_1=b

Proposed split:

```text
A=(b),
B=(a,T,-a).
```

So

```text
sum(A)=b,
sum(B)=T.
```

External collision normal form gives:

```text
Left cancellation:
  K + (b) = 0,
  sum(K)=-b.

Right cancellation:
  (a,T,-a)+K = 0,
  sum(K)=-T.
```

Old shorthand:

```text
Left(-b),
Right(-T).
```

### At W_2=a+b

Proposed split:

```text
A=(b,a),
B=(T,-a).
```

So

```text
sum(A)=a+b,
sum(B)=T-a.
```

External collision normal form gives:

```text
Left cancellation:
  K+(b,a)=0,
  sum(K)=-a-b.

Right cancellation:
  (T,-a)+K=0,
  sum(K)=a-T.
```

Old shorthand:

```text
Left(-a-b),
Right(a-T).
```

---

## GEN-L1 theorem

For the nonduplicate left length-one template

```text
T,a,b,-a -> b,a,T,-a,
```

every failure is one of:

```text
1. affine/singleton condition:
     T in {b-a, -a-b, -b};
2. duplicate/impossible condition:
     T in {0,a,b,-a} or local nonzero/distinctness failure;
3. template-aware external cancellation:
     K+(b)=0,
     (a,T,-a)+K=0,
     K+(b,a)=0,
     (T,-a)+K=0.
```

No other local obstruction type occurs.

---

# GEN-R1: generic right length-one interval

## Setup

Local block:

```text
a,b,-a,T
```

where the singleton interval has target `T` and

```text
T notin {0,a,b,-a}
```

unless explicitly routed as a duplicate/impossible case.

Original relative partial sums:

```text
a,
a+b,
b,
b+T.
```

Forbidden relative value:

```text
F=a.
```

Active block total:

```text
E=b+T.
```

Candidate move:

```text
a,b,-a,T  ->  b,-a,T,a.
```

New relative partial sums:

```text
b,
b-a,
b-a+T,
b+T.
```

The values

```text
b,
b+T
```

already occurred in the original block. Therefore the genuinely new values are

```text
W_1=b-a,
W_2=b-a+T.
```

---

## Internal classification

### Forbidden hits

```text
b-a = a          -> b=2a,
b-a+T = a        -> T=2a-b,
b+T = a          -> T=a-b.
```

The condition `T=a-b` is already impossible in the original Graham-valid local block because the original endpoint

```text
b+T = a
```

would equal the forbidden/old partial value `a`.

Thus the genuine internal exceptional conditions are

```text
b=2a,
T=2a-b.
```

### Zero hits

```text
b-a=0            -> b=a, duplicate,
b-a+T=0          -> T=a-b, already impossible as above,
b+T=0            -> T=-b, original endpoint zero issue.
```

The `T=-b` case makes the original endpoint `b+T=0`, so it is impossible for an interior local block because it repeats the basepoint. Boundary cases must still be handled separately.

### Internal collisions

Pairwise collisions among the new and unchanged local values force only nonzero/duplicate/impossible conditions such as

```text
a=0,
T=0,
T=a,
T=-a.
```

Thus the GEN-R1 internal exceptional set is contained in

```text
b=2a,
T=2a-b,
```

plus duplicate/impossible/boundary cases.

---

## External collision normal forms

External failures can occur only at the genuinely new values

```text
W_1=b-a,
W_2=b-a+T.
```

### At W_1=b-a

Proposed split:

```text
A=(b,-a),
B=(T,a).
```

So

```text
sum(A)=b-a,
sum(B)=T+a.
```

External collision normal form gives:

```text
Left cancellation:
  K+(b,-a)=0,
  sum(K)=a-b.

Right cancellation:
  (T,a)+K=0,
  sum(K)=-T-a.
```

Old shorthand:

```text
Left(a-b),
Right(-a-T).
```

### At W_2=b-a+T

Proposed split:

```text
A=(b,-a,T),
B=(a).
```

So

```text
sum(A)=b-a+T,
sum(B)=a.
```

External collision normal form gives:

```text
Left cancellation:
  K+(b,-a,T)=0,
  sum(K)=a-b-T.

Right cancellation:
  (a)+K=0,
  sum(K)=-a.
```

Old shorthand:

```text
Left(a-b-T),
Right(-a).
```

---

## GEN-R1 theorem

For the nonduplicate right length-one template

```text
a,b,-a,T -> b,-a,T,a,
```

every failure is one of:

```text
1. scalar/affine condition:
     b=2a or T=2a-b;
2. duplicate/impossible/boundary condition:
     T in {0,a,b,-a}, T=a-b, T=-b, or local nonzero/distinctness failure;
3. template-aware external cancellation:
     K+(b,-a)=0,
     (T,a)+K=0,
     K+(b,-a,T)=0,
     (a)+K=0.
```

No other local obstruction type occurs.

---

## Consequence for T3 routing

The T3 external routing note sends:

```text
E3 -> Left(a-b),
E2 -> Right(-a-b).
```

If the canceling interval has length one and the target is nonduplicate, these are handled by GEN-L1 and GEN-R1.

If the target duplicates a local atom, it must route through duplicate-target templates.

If the canceling interval has length at least two, it routes to the generic splitting templates GEN-L and GEN-R, still to be packaged.

---

## Remaining interval modules

Still needed:

```text
GEN-L>=2:
  generic left interval splitting.

GEN-R>=2:
  generic right interval splitting.

DUP-L:
  duplicate-left interval target.

DUP-R:
  duplicate-right interval target.
```

These are the next local modules needed to close T3/T4 routing.
