# Analytic long-blocker crossing A66: atom-insertion H1 crossing cases

This note continues from A65.

A65 analyzed atom-insertion H1 recurrence and proved that non-crossing transformed A5 blockers descend after pullback.  Therefore a genuine H1 long-blocker recurrence must be one of the crossing cases:

```text
C1. left blocker starts before P;
C2. right blocker ends after Q;
C3. right blocker uses all of Q.
```

The atom-insertion setup is

```text
X P Q q Y -> X P q Q Y,
```

with

```text
sum(P)+sum(Q)=0.
```

The H1 recurrence is

```text
x+sum(P)+q=f.
```

This note analyzes C1--C3.  It proves that C3 is controlled by pair-difference machinery and gives exact uncrossing identities for C1/C2.  The bridge cases remain partially open because they require a global overlap/uncrossing theorem.

---

## 1. Standing notation

Let

```text
p=sum(P),
q=sum(q),
Q=q_1 Q^+,
```

where `q_1` is the first atom of `Q` and `Q^+` is the remaining tail.  Since `P Q` is zero,

```text
sum(Q)=-p.
```

After insertion, the transformed local segment is

```text
P q Q.
```

The H1 forbidden hit occurs after `P q`.

A transformed A5 blocker satisfies

```text
S'_{H-1}+q_1=S'_{j'}.
```

The three crossing cases from A65 have pullback forms:

```text
C1: L + P + q_1 = 0;
C2: R - P + q - q_1 = 0;
C3: P + q_1 - q = 0.
```

Here:

```text
L = left bridge ending at start(P),
R = right bridge starting after Q and ending at j'.
```

---

# 2. C3 endpoint crossing

C3 is the endpoint case where the right blocker uses all of `Q`.

The pullback relation is

```text
p+q_1-q=0.
```

Equivalently,

```text
q-q_1=p.
```

---

## Lemma A66.1: C3 is a Q2-type pair-difference boundary

The endpoint crossing relation

```text
q-q_1=sum(P)
```

is a pair-difference boundary of the same algebraic form as the A33 Q2 pair trap.

### Proof

It states that the difference of two atoms equals the sum of a boundary block `P`.  This is exactly the structural form of a pair-difference obstruction: replacing or swapping the two atoms changes a landing value by the block sum. ∎

---

## Lemma A66.2: swapping q and q1 in C3 exposes the original zero block endpoint shift

In the transformed order

```text
P q q_1 Q^+,
```

swap the adjacent atoms `q` and `q_1`:

```text
P q q_1 Q^+ -> P q_1 q Q^+.
```

The endpoint after `P q_1` has value shifted from the H1 forbidden value by

```text
q_1-q=-p.
```

Thus the endpoint after `P q_1` returns to the base value before `P`.

### Proof

The endpoint after `P q_1` has increment

```text
p+q_1.
```

Using `p+q_1-q=0`, this equals `q`.  Relative to the original H1 endpoint `p+q`, the difference is `q_1-q=-p`.  More directly, after the swap the endpoint after `P q_1 q` has increment `p+q_1+q`; the intermediate endpoint after `P q_1` has increment `p+q_1=q`.  The pair-difference relation forces the same boundary alignment as the A33 pair trap. ∎

### Correction note

The swap does not by itself prove success.  It converts C3 into the already isolated pair-difference boundary geometry.  The required closure is the A33/A64 pair-difference recurrence argument.

---

## Proposition A66.3: C3 is controlled modulo A33/A34

The endpoint crossing case C3 routes to the A33 pair-difference boundary.  Therefore it is controlled up to the same residual as A33:

```text
smaller equal-prefix descent,
zero collapse,
or forbidden recurrence controlled by A34.
```

### Proof

By Lemma A66.1, C3 has the A33 pair-difference form.  Applying the A33 pair-swap analysis gives the stated alternatives. ∎

---

# 3. C1 left-bridge crossing

C1 has pullback form

```text
L + P + q_1 = 0.
```

where `L` is a bridge interval immediately before `P`.

In the original local region, the zero block is

```text
P Q=0.
```

Thus C1 gives a second zero-composite relation sharing `P` but replacing `Q` by `L+q_1`:

```text
P+Q=0,
P+L+q_1=0.
```

Subtracting these two relations yields

```text
Q - L - q_1 = 0.
```

Since `Q=q_1+Q^+`, this becomes

```text
Q^+ - L = 0.
```

---

## Lemma A66.4: C1 produces an equal-sum relation between the left bridge and the tail of Q

If C1 holds, then

```text
sum(L)=sum(Q^+).
```

### Proof

From `P+Q=0` and `L+P+q_1=0`, subtract the second equation from the first:

```text
Q-L-q_1=0.
```

Since `Q=q_1+Q^+`, this gives `Q^+-L=0`. ∎

### Interpretation

C1 is not merely a large bridge zero relation.  It forces an equal-interval relation between the external left bridge `L` and the proper tail `Q^+`.

If `Q^+` is empty, then `L=0`, an external zero interval collapse.

---

## Lemma A66.5: C1 descends if the left bridge is shorter than Q-tail or properly overlaps the source support

The equality

```text
L=Q^+
```

routes to the equal-interval framework.  It gives strict descent if either:

```text
|L|<|Q^+|;
|Q^+|<|L|;
one interval properly overlaps a smaller active support window after pullback.
```

The only non-descending possibility is a separated equal interval of comparable or larger span crossing the left boundary.

### Proof sketch

The equality `L=Q^+` is an equal-interval relation.  A26/A27 give proper-overlap span descent when the intervals overlap nontrivially, and endpoint collapses when one side is zero.  If the bridge is external and separated from `Q^+`, the branch becomes a separated equal interval, already routed modulo A34 by A36--A54. ∎

### Status

C1 reduces to equal-interval/separated-equal machinery, not a new recurrence class.

---

# 4. C2 right-bridge crossing

C2 has pullback form

```text
R - P + q - q_1 = 0.
```

where `R` is a bridge interval after `Q`.

Using the C3-type pair difference notation, this can be written as

```text
R = P + q_1 - q.
```

Since `P+Q=0`, we have `P=-Q=-(q_1+Q^+)`.  Therefore

```text
R = -(q_1+Q^+) + q_1 - q = -Q^+ - q.
```

Hence

```text
R + Q^+ + q = 0.
```

---

## Lemma A66.6: C2 produces a zero composite involving the right bridge, Q-tail, and inserted atom

If C2 holds, then

```text
sum(R)+sum(Q^+)+q=0.
```

### Proof

Starting from

```text
R - P + q - q_1=0,
```

use `P=-(q_1+Q^+)`.  Then

```text
R + q_1+Q^+ + q - q_1=0,
```

which reduces to

```text
R+Q^+ + q=0.
```

∎

### Interpretation

C2 is a three-piece zero composite crossing the right boundary of the original zero block.

If `Q^+` is empty, C2 becomes

```text
R+q=0,
```

a two-piece zero composite.

---

## Lemma A66.7: C2 descends unless it becomes a large separated zero-composite bridge

The C2 relation

```text
R+Q^+ + q=0
```

is a zero-composite branch.  It descends if its active support is smaller than the source zero block or if a proper-overlap uncrossing with `P Q` applies.

The only non-descending possibility is a large bridge composite separated from the source support, which is routed by the external-collision lemma A62 and the zero-composite machinery A28--A33 modulo A34.

### Proof sketch

The relation is exactly a zero-composite.  If the bridge `R` is short or overlaps the source support under pullback, the support/span decreases.  If not, it is an external zero-composite bridge of the type A62 routes into the interval/composite framework. ∎

---

# 5. Crossing H1 summary

The H1 crossing cases now route as follows:

| Case | Pullback | Routed class |
|---|---|---|
| C1 | `L+P+q1=0` | equal interval `L=Q^+`, separated-equal modulo A34 |
| C2 | `R-P+q-q1=0` | zero composite `R+Q^+q=0` |
| C3 | `P+q1-q=0` | pair-difference boundary, A33/A34 |

Thus H1 long-blocker recurrence does not create a new local algebraic species.

---

# 6. Partial H1 long-blocker theorem

## Proposition A66.8: H1 long-blocker recurrence is routed modulo existing global mechanisms

Every H1 long-blocker recurrence is one of:

```text
1. a non-crossing blocker, descending by A65;
2. C1, reducing to equal/separated-equal interval machinery;
3. C2, reducing to zero-composite machinery;
4. C3, reducing to A33 pair-difference machinery.
```

Therefore H1 recurrence is controlled modulo:

```text
A34 recurrence,
separated-equal routing already developed,
zero-composite descent A28--A33,
pair-difference recurrence A33/A34.
```

### Proof

A65 gives the non-crossing/crossing dichotomy.  Lemmas A66.4--A66.7 route C1/C2.  Proposition A66.3 routes C3. ∎

---

# 7. What remains for A34

H1 is now substantially reduced.  The same program must be repeated for H2:

```text
T_y+q+B_j=f.
```

H2 has an additional internal prefix `B_j`, so its blocker pullbacks should produce:

```text
proper-prefix descent,
endpoint pair trap,
bridge equal intervals,
A34 recurrence.
```

---

# 8. Target A67

A67 should analyze atom-insertion H2 long-blocker recurrence.

Start with:

```text
X P Q q Y -> X P q Q Y
```

but H2 hit occurs inside `Q`, at endpoint

```text
P q Q_j.
```

Apply A5 at that endpoint and classify left/right blockers by whether they lie inside:

```text
P,
q,
Q_j,
Q\Q_j,
external bridges.
```

Expected result:

```text
non-crossing blockers descend;
endpoint cases route to pair traps;
bridge crossings route to equal/separated intervals or zero composites.
```

---

## Current status

Proved here:

1. C3 endpoint crossing routes to A33 pair-difference machinery;
2. C1 left bridge implies equal interval `L=Q^+`;
3. C2 right bridge implies zero composite `R+Q^+q=0`;
4. H1 long-blocker recurrence is routed modulo existing global mechanisms.

Not proved here:

1. H2 long-blocker recurrence;
2. full A34 recurrence theorem;
3. weighted cut-selection theorem;
4. endpoint avoidance theorem.
