# Analytic status after weighted cut-swap A61

This note updates the proof-status map after A56--A60.

A56 isolated the genuinely weighted signed core.  A58 sharpened it as a nested zero-composite.  A59 showed that static cuts of the doubled block do not by themselves close the branch.  A60 then analyzed the first dynamic operation on the doubled block:

```text
A P R C -> A R P C,
```

where

```text
B=P R
```

inside the weighted core

```text
sum(A)+2sum(B)+sum(C)=0.
```

The main update is:

```text
weighted-core cut-swap displayed collisions are locally routed;
weighted-core cut selection remains open;
A34 recurrence remains open.
```

No complete proof is claimed here.

---

## 1. Weighted branch history

The weighted signed residual began as relations of the schematic form

```text
sum(A)+2sum(B)+sum(C)=0.
```

A56 introduced normal-form tests:

```text
W1 transported-prefix/tail artifact;
W2 doubled block zero;
W3 adjacent-pair zero;
W4 equal outer pieces;
W5 genuine weighted core.
```

A57 implemented these tests in:

```text
scripts/classify_weighted_signed_normal_form.py
```

A58 showed that the genuine weighted core is equivalent to the nested zero relation

```text
sum(A B C)+sum(B)=0.
```

A59 showed that static cuts of `B` expose overlapping/nested identities, not immediately disjoint A28-style zero composites.

A60 analyzed the dynamic cut swap

```text
A P R C -> A R P C.
```

---

## 2. What A60 closed locally

For a fixed proper cut

```text
B=P R,
```

A60 showed that the cut-swap changed only the internal `P` and `R` prefix families.

Every displayed collision equation routes to one of:

```text
two-piece zero,
three-piece zero,
higher composite-zero,
zero collapse.
```

Specifically:

| Collision family | Routed class |
|---|---|
| new `R` against `A` | two-piece zero |
| new `R` against `C` | three-piece zero |
| new `R` against `Y` | higher composite-zero |
| new `P` against `A` | three-piece zero |
| new `P` against `C` | two-piece zero |
| new `P` against `Y` | three-piece zero |
| new `R` against new `P` | two-piece zero |

Forbidden-hit equations from the cut-swap are A34 recurrence branches.

Thus:

```text
cut-swap displayed collisions: locally routed.
```

---

## 3. What remains open for weighted cores

A60 does not prove the weighted core is eliminated.

The missing theorem is a cut-selection theorem.

### Target theorem W-cut

In a genuine weighted core

```text
sum(A)+2sum(B)+sum(C)=0,
```

there exists a proper cut

```text
B=P R
```

such that the cut-swap

```text
A P R C -> A R P C
```

either:

```text
1. is Graham-valid and avoids the forbidden value;
2. gives a collision branch that descends under A28--A33/A34;
3. gives an earlier forbidden hit contradiction;
4. gives a non-earlier forbidden recurrence controlled by A34.
```

The displayed collision routing needed for item 2 is now available from A60.  The existence of a useful cut is not proved.

---

## 4. Relation to A34 recurrence

Many local branches now reduce to the same global issue:

```text
transformed-order forbidden hit not earlier than the original minimal hit.
```

This includes:

```text
atom insertion H1/H2;
separated-equal direct exchange forbidden hits;
gap-after forbidden hits;
midpoint forbidden hits;
weighted cut-swap forbidden hits.
```

All such branches require the A34 global recurrence theorem.

---

## 5. Current global proof obligations after A61

After A60, the open obligations are concentrated into three large items.

### O1. A34 global recurrence theorem

Prove that every transformed-order forbidden recurrence decreases a well-founded global obstruction measure or collapses.

This is the main bottleneck.

### O2. Weighted core cut-selection theorem

For a genuine weighted core, prove existence of a proper cut of `B` that makes the A60 cut-swap useful globally.

### O3. External-collision bookkeeping

For transformed block moves, collisions with partial sums outside the displayed local segment must be routed rigorously into the same interval/composite/recurrent framework.

A55 gave the midpoint version as a sketch.  A full proof needs a general external-collision lemma.

---

## 6. Branches now locally routed modulo A34

The following formerly hard local branches have been routed:

```text
separated equal direct-exchange D1--D5;
separated equal gap-after E1--E5;
D2 all ranges m<k, m=k, m>k;
midpoint displayed collisions;
weighted-core cut-swap displayed collisions.
```

The remaining difficulty is less about algebraic identities and more about global proof architecture.

---

## 7. Recommended A62 target

The next useful step should be a general external-collision lemma.

For a local block move that changes a displayed family from

```text
x+F_i
```

to

```text
x+t+F_i,
```

an external collision has the form

```text
x+t+F_i=S_u,
```

where `S_u` is an unchanged partial sum outside the displayed block.

A62 should prove that such a collision always defines one of:

```text
equal interval,
signed interval,
zero composite,
or A34 recurrence/local blocker state.
```

This would remove repeated hand-waving around external collisions.

---

## Current status

Closed locally:

```text
weighted cut-swap displayed collision routing.
```

Open:

```text
A34 recurrence theorem;
weighted cut-selection theorem;
general external-collision lemma;
endpoint avoidance theorem.
```
