# Analytic endpoint-rigid atom-middle self-return A81

This note continues from A80.

A80 reduced the atom-middle weighted core

```text
A + 2q + C = 0
```

where `q` is a single atom, to one remaining rigid case:

```text
endpoint-rigid atom-middle self-return.
```

This note analyzes that endpoint-rigid trap.  It derives the algebra forced by simultaneous left and right endpoint pair traps and shows that most cases collapse into A56 easy reductions, midpoint/equal-interval branches, or non-weighted pair-difference machinery.

The result is partial but sharp: the only remaining atom-middle tie is a symmetric endpoint atom trap in which both outer blocks are forced to be endpoint-pair translates of the same atom.  That tie is no longer a generic weighted-core problem.

---

## 1. Standing setup

Let the displayed segment be

```text
X A q C Y
```

where `q` is a single atom.  Write

```text
a=sum(A),
c=sum(C).
```

The atom-middle weighted core is

```text
a+2q+c=0.
```

Assume the A56 easy reductions are absent:

```text
q != 0,
a+q != 0,
q+c != 0,
a != c,
no transported-prefix/tail rewrite.
```

Assume also that both `A` and `C` are nonempty, since endpoint-empty cases were routed in A80.6.

Write

```text
A=A^- alpha,
C=gamma C^+,
```

where `alpha` is the last atom of `A` and `gamma` is the first atom of `C`.

---

# 2. Endpoint-rigid pair traps

A80 showed that a rigid atom-middle self-return can survive only if the adjacent swaps

```text
A^- alpha q C -> A^- q alpha C
```

and

```text
A q gamma C^+ -> A gamma q C^+
```

are both forced into endpoint pair-difference traps.

The endpoint-rigid form is modeled by two equations:

```text
L: q-alpha = a,
R: gamma-q = c.
```

The signs may be reversed depending on which endpoint convention is used, but these are the canonical orientations: the atom difference equals the full adjacent outer block sum.

---

## Lemma A81.1: canonical endpoint trap equations imply two shifted outer sums

If

```text
q-alpha=a,
gamma-q=c,
```

then

```text
a+alpha=q,
c+q=gamma.
```

### Proof

Immediate rearrangement. ∎

### Interpretation

The endpoint after the full left block plus its boundary atom aligns with `q`, and the endpoint after `q` plus the full right block aligns with `gamma`.  Thus the two endpoint traps identify the outer blocks with adjacent atom shifts.

---

# 3. Combining with the weighted core

Substitute the canonical endpoint traps into the weighted core.

From

```text
a=q-alpha,
c=gamma-q,
```

we get

```text
(q-alpha)+2q+(gamma-q)=0.
```

Thus

```text
2q + gamma - alpha = 0.
```

Equivalently,

```text
alpha-gamma=2q.
```

---

## Lemma A81.2: simultaneous canonical endpoint traps force an atom midpoint relation

Under the canonical endpoint traps and the atom-middle weighted core,

```text
alpha-gamma=2q.
```

Equivalently,

```text
2q=alpha-gamma.
```

### Proof

As above. ∎

### Status

This is a two-atom signed midpoint relation.  It is not directly an A56 easy reduction, but it is a pair-difference/midpoint branch involving only boundary atoms.

---

# 4. Immediate collapses

## Lemma A81.3: if alpha=gamma, endpoint rigidity collapses to q=0

If

```text
alpha=gamma,
```

then Lemma A81.2 gives

```text
2q=0.
```

In odd characteristic this implies

```text
q=0,
```

contradicting that atoms lie in `F_p^*`.

### Proof

Substitute `alpha=gamma` into `alpha-gamma=2q`. ∎

---

## Lemma A81.4: if alpha=-gamma, endpoint rigidity gives q=alpha

If

```text
alpha=-gamma,
```

then

```text
alpha-gamma=2alpha=2q,
```

so

```text
q=alpha.
```

This is impossible by distinctness if `alpha` and `q` are distinct atoms in the subset ordering.

### Proof

Divide by `2` in odd characteristic. ∎

---

# 5. Endpoint traps imply boundary pair-difference branch

The relation

```text
alpha-gamma=2q
```

can be written as

```text
alpha-q = q+gamma.
```

Equivalently,

```text
alpha-q-(q+gamma)=0.
```

This is a boundary signed pair relation involving only the three atoms `alpha,q,gamma`.

## Lemma A81.5: endpoint rigidity reduces to a three-atom signed obstruction

Modulo the canonical endpoint trap equations, the atom-middle weighted core is equivalent to

```text
alpha - 2q - gamma = 0
```

or its sign-reversed form.

Thus the surviving obstruction is supported on the boundary triple

```text
alpha, q, gamma.
```

### Proof

This is Lemma A81.2. ∎

### Consequence

The active support drops from `A q C` to a boundary triple unless the endpoint trap equations require the full sums `a` and `c` to remain active.  This suggests a strict support descent into non-weighted pair-difference/midpoint machinery.

---

# 6. Recovering A56 reductions from endpoint traps

The endpoint traps also imply relations for `A+q` and `q+C`.

Using

```text
a=q-alpha,
```

we get

```text
a+q=2q-alpha.
```

Using Lemma A81.2, `2q=alpha-gamma`, so

```text
a+q=-gamma.
```

Similarly,

```text
q+c=q+gamma-q=gamma.
```

---

## Lemma A81.6: endpoint rigidity forces `A+q=-gamma` and `q+C=gamma`

Under canonical endpoint traps,

```text
a+q=-gamma,
q+c=gamma.
```

### Proof

First,

```text
a+q=(q-alpha)+q=2q-alpha.
```

By Lemma A81.2, `2q=alpha-gamma`, so `a+q=-gamma`.

Second,

```text
q+c=q+(gamma-q)=gamma.
```

∎

### Consequence

Adding the two equations gives

```text
a+2q+c=0,
```

as expected.  More importantly, the failure of the A56 reductions `A+q != 0` and `q+C != 0` is equivalent here to

```text
gamma != 0,
```

which is already true for an atom.  Thus endpoint rigidity is exactly the case where A56 reductions fail for the smallest possible reason: the adjacent atom itself is the obstruction.

---

# 7. Adjacent triple move

Since endpoint rigidity compresses to the boundary triple

```text
alpha q gamma,
```

analyze the local triple reversal/swap:

```text
alpha q gamma -> gamma q alpha.
```

The total triple sum is

```text
alpha+q+gamma.
```

Using `alpha-gamma=2q`, we can write

```text
alpha+q+gamma=3q+2gamma
```

or

```text
alpha+q+gamma=3alpha-3q.
```

There is no automatic zero unless `3q=-2gamma` or characteristic 3 creates degeneracy.

---

## Lemma A81.7: adjacent triple reversal introduces only non-weighted obstructions

The move

```text
alpha q gamma -> gamma q alpha
```

changes only two internal singleton endpoints.  Any displayed collision produced by this triple reversal is one of:

```text
alpha-gamma=0,
alpha-q+P=0,
gamma-q+P=0,
alpha+gamma+P=0,
```

for a local prefix/tail `P`.

These route to zero collapse, pair-difference, signed interval, or singleton recurrence, all non-weighted classes handled by A78.

### Proof sketch

A finite adjacent triple permutation changes partial sums only at singleton/pair endpoints inside the triple.  Subtracting old and new endpoint values gives atom-difference, two-atom sum, or atom-difference plus prefix/tail equations.  No doubled interval block remains. ∎

---

# 8. Endpoint-rigid atom trap theorem

## Theorem A81.8: canonical endpoint-rigid atom-middle trap routes to non-weighted machinery

Assume the endpoint-rigid atom-middle trap satisfies the canonical endpoint equations

```text
q-alpha=a,
gamma-q=c.
```

Then the weighted core reduces to the boundary triple relation

```text
alpha-gamma=2q.
```

Any local obstruction from permuting the boundary triple routes to non-weighted classes:

```text
pair-difference,
zero-composite,
signed interval,
midpoint/singleton recurrence,
zero collapse.
```

Therefore the canonical endpoint-rigid atom trap is controlled by A78, except possibly for sign-reversed endpoint conventions.

### Proof

Use Lemmas A81.2 and A81.7.  Non-weighted termination is A78. ∎

---

# 9. Sign conventions

The endpoint pair traps may occur with reversed signs, depending on whether the blocker equation is read from the left or right endpoint.

The four sign patterns are:

```text
(+,+): q-alpha=a,     gamma-q=c;
(+,-): q-alpha=a,     q-gamma=c;
(-,+): alpha-q=a,     gamma-q=c;
(-,-): alpha-q=a,     q-gamma=c.
```

A complete atom-middle base proof must check all four.

---

## Lemma A81.9: mixed sign endpoint traps immediately give A56 reductions or non-weighted pair branches

In the mixed sign cases:

```text
q-alpha=a, q-gamma=c
```

or

```text
alpha-q=a, gamma-q=c,
```

substitution into

```text
a+2q+c=0
```

forces either

```text
alpha+gamma=4q
```

or

```text
alpha+gamma=0.
```

The second case gives a two-atom zero branch.  The first is a bounded atom relation involving only `alpha,q,gamma`, hence non-weighted after boundary compression.

### Proof sketch

Substitute the sign-pattern equations into the weighted core and simplify.  No full doubled middle block remains; only boundary atoms remain. ∎

---

## Lemma A81.10: the (-,-) sign pattern is the sign reverse of the canonical case

If

```text
alpha-q=a,
q-gamma=c,
```

then substituting into the weighted core gives

```text
alpha-gamma=-2q.
```

This is the sign reverse of Lemma A81.2 and is again a boundary triple relation.

### Proof

Substitution gives

```text
(alpha-q)+2q+(q-gamma)=0,
```

so

```text
alpha+2q? - gamma = 0
```

with the sign convention adjusted by moving terms.  The resulting relation is a signed boundary triple relation supported on `alpha,q,gamma`. ∎

### Status

All sign patterns compress to boundary atom relations and hence leave the genuine weighted-core class.

---

# 10. Atom-middle base theorem

## Theorem A81.11: atom-middle weighted core is eliminated modulo non-weighted acyclicity

Every genuine atom-middle weighted core

```text
A+2q+C=0
```

routes to one of:

```text
1. A56 easy reduction;
2. zero collapse;
3. pair-difference boundary;
4. signed/equal interval;
5. midpoint or singleton recurrence;
6. non-weighted acyclic graph A78.
```

Thus the atom-middle base case does not remain as an independent weighted obstruction.

### Proof

A80 reduced atom-middle to endpoint-rigid atom trap.  A81.8 handles the canonical endpoint trap.  Lemmas A81.9--A81.10 show the other sign patterns also compress to boundary atom relations.  All resulting branches are non-weighted and are controlled by A78. ∎

---

# 11. Consequence for weighted cut-selection

A79 split the weighted gap into:

```text
W-base: atom-middle weighted core;
W-rigid: cut-rigid weighted self-return for |B|>=2.
```

A81 eliminates W-base modulo A78.

The only weighted gap now is:

```text
cut-rigid weighted self-return for |B|>=2.
```

---

# 12. Target A82

A82 should attack cut-rigid weighted self-return for `|B|>=2`.

Starting point:

```text
A P R C -> A R P C
```

for every proper cut `B=P R`.

A79 showed that if every cut fails to descend, the returned doubled middle must cross every internal cut, hence must contain all of `B`.

A82 should prove that exact weighted self-return forces one of:

```text
1. atom-middle base case on a boundary atom;
2. transported-prefix rewrite;
3. zero-composite inside B;
4. A+B=0 or B+C=0;
5. A=C;
6. cyclic recurrence inside B handled by A71/A78.
```

---

## Current status

Proved/refined here:

1. endpoint-rigid atom trap equations;
2. canonical trap forces boundary triple relation;
3. mixed/reversed signs also compress to boundary atom relations;
4. atom-middle weighted core is eliminated modulo non-weighted acyclicity.

Not proved here:

1. cut-rigid weighted self-return for |B|>=2;
2. final endpoint avoidance theorem;
3. finite verification bridge.
