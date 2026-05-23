# Analytic atom-middle weighted core A80

This note continues from A79.

A79 refined the weighted-core gap into two base problems:

```text
W-base. atom-middle weighted core A + 2q + C = 0;
W-rigid. cut-rigid weighted self-return for |B|>=2.
```

This note attacks W-base.

The atom-middle weighted core is the length-one middle case of

```text
A + 2B + C = 0.
```

It has the form

```text
sum(A)+2q+sum(C)=0,
```

where `q` is a single atom.  Because `|B|=1`, no proper middle cut exists, so the A60 cut-swap mechanism cannot be applied.

The result is partial but useful: the atom-middle core is routed to pair-difference, midpoint, two-piece zero, singleton recurrence, or a rigid atom-middle self-return.  The final rigid atom-middle self-return remains open.

---

## 1. Standing setup

Let the displayed local segment be

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

The A56 easy reductions are assumed absent:

```text
q != 0,
a+q != 0,
q+c != 0,
a != c,
no transported-prefix/tail rewrite.
```

Equivalently,

```text
sum(A q C)+q=0.
```

So the whole block `A q C` has sum `-q`.

---

# 2. Midpoint interpretation

Over odd prime fields,

```text
a+2q+c=0
```

is equivalent to

```text
q=-(a+c)/2.
```

Thus the atom `q` is the negative midpoint of the outer block sums `a` and `c`.

## Lemma A80.1: atom-middle weighted core is an outer-sum midpoint relation

In odd characteristic,

```text
a+2q+c=0
```

if and only if

```text
2(-q)=a+c.
```

### Proof

Rearrange the weighted equation:

```text
a+c=-2q.
```

∎

### Status

This is a block-sum midpoint relation, but not immediately the same as the partial-sum midpoint branch A55 unless `A` and `C` occur as endpoint intervals around a common center.

---

# 3. Swap q right with first atom of C

Assume `C` is nonempty and write

```text
C=c_1 C^+.
```

Try the adjacent swap

```text
A q c_1 C^+ -> A c_1 q C^+.
```

The changed local partial sums are:

Before:

```text
x+A_i,
x+a+q,
x+a+q+c_1,
x+a+q+C_k.
```

After:

```text
x+A_i,
x+a+c_1,
x+a+c_1+q,
x+a+c_1+q+C^+_r.
```

Only the endpoints between `q` and `c_1` change; endpoints after both atoms are unchanged.

---

## Lemma A80.2: right swap collision with the old q endpoint gives pair-difference

If the new endpoint after `A c_1` collides with the old endpoint after `A q`, then

```text
c_1=q,
```

which is impossible for distinct atoms.

If it collides with a translated prefix endpoint involving `C^+`, the collision equation has form

```text
c_1 - q + C^+_r=0
```

or a two-piece zero endpoint case.

### Proof

The new shifted family differs from the old shifted family by replacing `q` with `c_1`.  Any nontrivial equality of endpoints involving prefixes after the swap subtracts to a relation containing the atom difference `c_1-q` plus a prefix/tail of `C`. ∎

### Status

Right-swap displayed collisions route to pair-difference or zero-composite machinery.

---

## Lemma A80.3: right swap forbidden recurrence is singleton/pair recurrence

If

```text
A q c_1 C^+ -> A c_1 q C^+
```

is Graham-valid but recurrent, then the new forbidden hit occurs at either

```text
x+a+c_1=f
```

or another moved singleton/prefix endpoint.  This is singleton-prefix recurrence A70 or pair-difference recurrence A69.

### Proof

The only new displayed endpoint before the unchanged suffix is `x+a+c_1`.  Any later moved endpoint differs by the same adjacent atom transposition and hence is a moved-prefix recurrence. ∎

---

# 4. Swap q left with last atom of A

Assume `A` is nonempty and write

```text
A=A^- a_1
```

where `a_1` is the last atom of `A`.  Try the adjacent swap

```text
A^- a_1 q C -> A^- q a_1 C.
```

---

## Lemma A80.4: left swap displayed obstructions route to pair-difference or zero-composite branches

The left swap changes only the local endpoints around `a_1` and `q`.  Any displayed collision introduced by the swap has one of the forms

```text
a_1-q+P=0,
q-a_1+P=0,
P=0,
```

where `P` is a local prefix/tail of `A` or `C`.

Thus the obstruction routes to pair-difference, two-piece zero, or zero collapse.

### Proof

Adjacent transposition changes partial sums only in the interval between the two swapped atoms.  Subtracting an old or unchanged endpoint gives either an atom difference plus a local prefix/tail, or a zero-prefix relation. ∎

---

## Lemma A80.5: left swap forbidden recurrence routes by A69/A70

If the left swap is Graham-valid but recurrent, the forbidden hit is a moved singleton/prefix hit associated with the atom `q` or `a_1`.  Hence it routes to singleton-prefix recurrence A70 or pair-swap recurrence A69.

### Proof

The swap is an adjacent pair swap.  A69 and A70 classify recurrent forbidden hits created by such moved atom/prefix endpoints. ∎

---

# 5. Endpoint cases: A or C empty

If `A` is empty, the weighted equation is

```text
2q+c=0.
```

If `C` is empty, it is

```text
a+2q=0.
```

These are endpoint atom-middle branches.

## Lemma A80.6: endpoint atom-middle cores route to singleton/midpoint recurrence or zero-composite

If one outer block is empty, the relation

```text
2q+C=0
```

or

```text
A+2q=0
```

is a midpoint relation between the atom endpoint and the outer endpoint.  Swapping/moving `q` against the adjacent outer atom routes to pair-difference or singleton recurrence.  If the outer block has length one, the relation is a three-atom or two-atom zero-composite.

### Proof sketch

With one side empty, the equation says the nonempty outer block has sum `-2q`.  Over odd characteristic this is an endpoint midpoint condition.  Local adjacent swaps with the nearest atom produce pair-difference equations; endpoint forbidden hits are singleton recurrence. ∎

---

# 6. Rigid atom-middle self-return

The preceding swaps show that local motion of `q` left or right routes to non-weighted machinery unless the process reconstructs the same atom-middle weighted core.

## Definition A80.7: rigid atom-middle self-return

A rigid atom-middle self-return occurs when every adjacent swap of `q` with a neighboring atom either is blocked/recurrent and, after routing, reconstructs the same core

```text
A + 2q + C = 0
```

with the same middle atom `q` and same outer blocks `A,C`.

---

## Lemma A80.8: rigid atom-middle self-return forces both neighboring pair-difference boundaries

Assume both `A` and `C` are nonempty:

```text
A=A^- a_1,
C=c_1 C^+.
```

If both left and right adjacent swaps of `q` return rigidly to the same atom-middle core, then the routing must force boundary pair-difference relations of the form

```text
q-a_1 = sum(A')
```

or

```text
c_1-q = sum(C')
```

for suitable boundary subblocks `A'` or `C'` contained in `A` or `C`.

### Proof sketch

By Lemmas A80.2--A80.5, non-pair-difference collisions enter zero-composite or singleton recurrence, which are non-weighted and terminate by A78 unless they return to weighted core.  To reconstruct the exact same atom-middle core after an adjacent transposition, the only possible local obstruction preserving the middle atom is a boundary pair-difference trap. ∎

---

## Lemma A80.9: simultaneous left/right boundary pair traps imply an internal non-weighted obstruction unless both are endpoint rigid

If the boundary pair-difference traps from Lemma A80.8 use proper subblocks of `A` or `C`, then they are smaller pair-difference/zero-composite branches controlled by A78.

The only remaining case is when both pair traps use full endpoint blocks, giving endpoint rigidity:

```text
q-a_1 = sum(A),
```

or the analogous full-right condition.

### Proof sketch

Proper subblocks give smaller support/span and therefore enter the non-weighted acyclic graph.  Full endpoint cases preserve the atom-middle support and are the only possible rigid ties. ∎

---

# 7. Atom-middle reduction theorem

## Theorem A80.10: atom-middle weighted core routes modulo endpoint-rigid atom trap

A genuine atom-middle weighted core

```text
A+2q+C=0
```

routes to one of:

```text
1. pair-difference boundary machinery;
2. midpoint boundary machinery;
3. two-piece or higher zero-composite machinery;
4. singleton-prefix recurrence;
5. non-weighted acyclicity A78;
6. endpoint-rigid atom-middle self-return.
```

Thus atom-middle is not fully eliminated, but its only remaining tie is endpoint-rigid atom trap.

### Proof

If `A` or `C` is empty, use Lemma A80.6.  If both are nonempty, attempt left and right adjacent swaps.  Lemmas A80.2--A80.5 route all non-rigid failures to non-weighted mechanisms.  Lemmas A80.8--A80.9 isolate the only remaining rigid possibility. ∎

---

# 8. Consequence for weighted cut-selection

A79 left two weighted problems:

```text
W-base: atom-middle core;
W-rigid: cut-rigid self-return for |B|>=2.
```

A80 reduces W-base to:

```text
endpoint-rigid atom-middle self-return.
```

This is a smaller and more concrete base case.

---

# 9. Target A81

A81 should attack endpoint-rigid atom-middle self-return.

Setup:

```text
A^- a q c C^+
```

with

```text
sum(A)+2q+sum(C)=0.
```

Endpoint rigidity should impose pair-difference equations involving the full endpoint blocks.  Combine left and right endpoint equations with the weighted core equation and test whether they force:

```text
A+q=0,
q+C=0,
A=C,
q=0,
midpoint boundary,
or a smaller weighted core.
```

Those are precisely the forbidden A56 easy reductions or non-weighted branches.

---

## Current status

Proved/refined here:

1. atom-middle weighted core has midpoint/nested-zero interpretations;
2. adjacent swaps of q route displayed obstructions to pair-difference or zero-composite machinery;
3. adjacent-swap recurrences route to A69/A70;
4. atom-middle core is controlled except for endpoint-rigid atom-middle self-return.

Not proved here:

1. endpoint-rigid atom trap elimination;
2. cut-rigid weighted self-return for |B|>=2;
3. final endpoint avoidance theorem.
