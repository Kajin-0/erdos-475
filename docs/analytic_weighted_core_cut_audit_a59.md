# Analytic weighted core cut audit A59

This note continues from A58.

A58 showed that the genuine weighted signed core

```text
sum(A)+2sum(B)+sum(C)=0
```

is equivalent to a nested zero-composite relation

```text
sum(A B C)+sum(B)=0.
```

It also showed that every proper cut

```text
B=P R
```

creates hidden three-piece identities.  This note audits those cut identities and records a negative but important point:

```text
The cut identities are nested/overlapping zero-composites, not immediately disjoint A28-style zero composites.
```

Therefore a simple cut of `B` alone does not close the genuine weighted core.

---

## Standing setup

Let a displayed segment be

```text
X A B C Y
```

with

```text
a=sum(A),
b=sum(B),
c=sum(C),
```

and assume the weighted core relation

```text
a+2b+c=0.
```

Assume also the A56 easy reductions are absent:

```text
b != 0,
a+b != 0,
b+c != 0,
a != c,
```

and no transported-prefix/tail artifact is known.

Cut

```text
B=P R
```

with

```text
p=sum(P),
r=sum(R),
b=p+r.
```

---

# 1. The two A58 cut identities

A58 proved the two identities:

```text
sum(A P)+sum(P R C)+sum(R)=0,
```

and

```text
sum(A P R)+sum(R C)+sum(P)=0.
```

Call these the left-cut and right-cut identities.

---

## Lemma A59.1: the left-cut identity has an overlap on P and R

The left-cut identity

```text
sum(A P)+sum(P R C)+sum(R)=0
```

uses the pieces:

```text
A P,
P R C,
R.
```

The first two pieces overlap on `P`; the second and third pieces overlap on `R`.

Therefore it is not a disjoint three-piece zero composite in the sense of A28--A33.

### Proof

The block `P` is contained in both `A P` and `P R C`.  The block `R` is contained in both `P R C` and `R`.  ∎

---

## Lemma A59.2: the right-cut identity has an overlap on P and R

The right-cut identity

```text
sum(A P R)+sum(R C)+sum(P)=0
```

uses the pieces:

```text
A P R,
R C,
P.
```

The first and second pieces overlap on `R`; the first and third pieces overlap on `P`.

Therefore it is also not a disjoint three-piece zero composite in the sense of A28--A33.

### Proof

Immediate from containment. ∎

---

# 2. Difference between the two cut identities

Although the cut identities are not directly disjoint, comparing them gives useful structure.

The left identity is

```text
(a+p)+(p+r+c)+r=0.
```

The right identity is

```text
(a+p+r)+(r+c)+p=0.
```

Subtracting the two expressions gives zero identically, so the two cut identities are algebraically the same weighted relation in two decompositions.

## Lemma A59.3: changing the cut does not create a new equation by itself

For any cut `B=P R`, the left-cut and right-cut identities are both exactly equivalent to

```text
a+2b+c=0.
```

Thus varying the cut of `B` alone does not create a new independent constraint.

### Proof

Both left and right expressions expand to

```text
a+2p+2r+c=a+2b+c.
```

∎

---

# 3. Proper cut endpoint collapses

Some endpoint values of `P` or `R` recover known reductions.

## Lemma A59.4: if a proper prefix P is zero, the weighted core reduces to a shorter weighted core or zero branch

If

```text
p=0,
```

then `P` is a zero-prefix/interior-zero branch depending on position.  Removing this zero block leaves the relation

```text
a+2r+c=0
```

over the shorter middle block `R`.

### Proof

Substitute `p=0` in `a+2p+2r+c=0`.  The zero-sum status of `P` follows from `p=0`. ∎

### Status

This is a collapse plus strict shortening of the doubled block.

---

## Lemma A59.5: if a proper tail R is zero, the weighted core reduces to a shorter weighted core or zero branch

If

```text
r=0,
```

then `R` is a zero-prefix/interior-zero branch depending on position.  Removing this zero block leaves

```text
a+2p+c=0
```

over the shorter middle block `P`.

### Proof

Symmetric to Lemma A59.4. ∎

---

# 4. Adjacent pair reductions from cuts

For a proper cut, the A56 adjacent-pair tests can apply to the smaller pieces.

## Lemma A59.6: if `A P` is zero, the residual becomes `P R C + R = 0`

If

```text
a+p=0,
```

then the left-cut identity gives

```text
sum(P R C)+sum(R)=0.
```

This is the nested zero relation for the shorter weighted core on middle block `R` with left context `P` and right context `C`.

### Proof

Substitute `a+p=0` into

```text
(a+p)+(p+r+c)+r=0.
```

∎

### Status

This is not a complete closure, but it shifts the doubled contribution toward a shorter tail block `R`.

---

## Lemma A59.7: if `R C` is zero, the residual becomes `A P R + P = 0`

If

```text
r+c=0,
```

then the right-cut identity gives

```text
sum(A P R)+sum(P)=0.
```

This shifts the doubled contribution toward the shorter prefix block `P`.

### Proof

Substitute into the right-cut identity. ∎

---

# 5. Equal-side cut reductions

## Lemma A59.8: if `A P` and `R C` have equal sums, the weighted core reduces to a midpoint-type relation between P and R

Assume

```text
sum(A P)=sum(R C).
```

That is,

```text
a+p=r+c.
```

Using the weighted core

```text
a+2p+2r+c=0,
```

substitute `a+p=r+c`:

```text
(r+c)+p+2r+c=0,
```

or

```text
p+3r+2c=0.
```

This is not generally a two-piece zero relation.  Therefore equal-side cuts do not directly mimic the equal-outer reduction A56.6 unless the outer pieces are exactly `A` and `C`, not `AP` and `RC`.

### Status

This is a negative result: the naive equal-side cut does not close the weighted core.

---

# 6. Genuine weighted cut residual

After the cut audit, a genuinely hard weighted residual must satisfy, for every proper cut `B=P R`:

```text
p != 0,
r != 0,
a+p != 0,
r+c != 0,
```

and must avoid any transported-prefix/tail context that would allow W1.

It may still be attacked by transformed-order moves, but not by static cut identities alone.

---

# 7. Candidate transformed move: swap P and R

The simplest non-static move is to swap the two pieces of `B`:

```text
X A P R C Y -> X A R P C Y.
```

This preserves the total segment sum but changes internal partial sums.

The next note should compute its exact obstruction equations.

Expected form:

```text
A P R C -> A R P C
```

with changed families:

```text
R-prefixes translated by a,
P-prefixes translated by a+r,
```

compared to old levels.

Potential outcomes:

```text
two-piece zero,
shorter weighted core,
transported-prefix artifact,
A34 forbidden recurrence.
```

---

## Target A60

Analyze the internal swap of a proper cut of the doubled block:

```text
A P R C -> A R P C.
```

This is the first genuinely dynamic operation on the weighted core.

For a cut `B=P R`, derive:

1. partial-sum families before/after;
2. collision equations;
3. forbidden-hit equations;
4. routing into known classes or a shorter weighted core.

---

## Current status

Proved here:

1. A58 cut identities are overlapping/nested, not disjoint A28-style composites;
2. varying the cut alone gives no independent equation;
3. zero prefix/tail cuts shorten the doubled block;
4. adjacent cut-zero cases shift to shorter nested weighted relations;
5. naive equal-side cuts do not close the core.

Not proved here:

1. dynamic cut-swap obstruction routing;
2. genuine weighted core elimination;
3. A34 global recurrence theorem;
4. endpoint avoidance theorem.
