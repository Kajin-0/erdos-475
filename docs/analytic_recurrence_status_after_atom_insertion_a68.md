# Analytic recurrence status after atom-insertion A68

This note updates the recurrence-status map after A64--A67.

A64 proved bounded-blocker recurrence descent and isolated the remaining long-blocker recurrence case.  A65--A66 analyzed atom-insertion H1 long-blocker recurrence.  A67 analyzed atom-insertion H2 long-blocker recurrence.

The main update is:

```text
Atom-insertion recurrence H1/H2 is no longer an abstract A34 gap.
It is routed into existing global mechanisms:
zero-composite, equal/signed interval, pair-difference, singleton recurrence, and A34 recurrence.
```

No complete endpoint-avoidance proof is claimed here.

---

## 1. Recurrence source: atom insertion

The atom-insertion setup is

```text
X P Q q Y -> X P q Q Y
```

with

```text
sum(P)+sum(Q)=0.
```

The atom `q` is inserted into the zero block `P Q` to break the zero-block endpoint collision.

The two forbidden-hit branches from A29--A30 are:

```text
H1: x+sum(P)+q=f;
H2: x+sum(P)+q+Q_j=f.
```

---

## 2. A64 bounded-blocker theorem

A64 showed that any recurrence ordering re-enters the A5 local-blocker framework.

If the nearest transformed A5 blocker has span smaller than the source obstruction, then recurrence descends under

```text
M_rec=(span,pieces,type_rank,boundary_rank,h_excess).
```

Thus only long-blocker recurrence remains:

```text
all transformed A5 blockers have span at least the source obstruction span.
```

---

## 3. H1 status after A65--A66

H1 occurs at the endpoint after

```text
P q.
```

A65 pulled back the transformed A5 blocker and proved:

```text
non-crossing H1 blockers descend.
```

The remaining crossing cases were:

```text
C1: left blocker starts before P;
C2: right blocker ends after Q;
C3: right blocker uses all of Q.
```

A66 routed these as:

| Case | Pullback | Routed class |
|---|---|---|
| C1 | `L+P+q1=0` | equal/separated interval via `L=Q^+` |
| C2 | `R-P+q-q1=0` | zero composite `R+Q^+q=0` |
| C3 | `P+q1-q=0` | A33 pair-difference boundary |

Therefore H1 introduces no new recurrence species.

Status:

```text
H1 routed modulo separated-equal, zero-composite, pair-difference, and A34.
```

---

## 4. H2 status after A67

H2 occurs at the endpoint after

```text
P q U
```

where

```text
Q=U V.
```

A67 pulled back the transformed A5 blocker and proved:

```text
non-crossing H2 blockers descend.
```

The crossing and endpoint cases route as:

| Case | Routed class |
|---|---|
| left bridge before P | signed/equal relation with `V` |
| right bridge after V | zero/signed composite |
| right blocker uses all V | pair-difference boundary |
| V empty endpoint | singleton recurrence `x+q=f` |

Therefore H2 also introduces no new recurrence species.

Status:

```text
H2 routed modulo equal/signed interval, zero-composite, pair-difference, singleton recurrence, and A34.
```

---

## 5. Atom-insertion recurrence conclusion

Combining A64--A67:

```text
bounded H1/H2 recurrence -> strict descent;
non-crossing long-blocker H1/H2 -> strict descent;
crossing long-blocker H1/H2 -> routed to existing global mechanisms.
```

Thus atom-insertion recurrence is locally controlled modulo the same global termination obligations already present elsewhere.

This removes A34 obligations R1 and R2 as standalone recurrence gaps.

---

## 6. Remaining recurrence sources

A34 originally listed the following recurrence obligations:

```text
R1. atom insertion H1;
R2. atom insertion H2;
R3. A33 Q2 pair-swap forbidden recurrence;
R4. singleton-prefix forbidden recurrence;
R5. cyclic-cut recurrence.
```

After A68:

| Recurrence source | Status |
|---|---|
| R1 H1 | routed modulo existing mechanisms |
| R2 H2 | routed modulo existing mechanisms |
| R3 pair-swap recurrence | open |
| R4 singleton-prefix recurrence | open |
| R5 cyclic-cut recurrence | open |

The next natural target is R3 because H1/H2 crossing cases route into pair-difference boundary machinery.

---

## 7. Pair-difference recurrence target

A33 pair-difference recurrence has schematic form:

```text
x+Y_m=f.
```

arising after a pair swap in a Q2 boundary configuration.

The expected A69 analysis should:

```text
1. apply A5 to the recurrent pair-swapped ordering;
2. pull the transformed blocker back through the pair swap;
3. prove non-crossing blockers descend;
4. route crossing blockers to equal interval, zero-composite, or smaller pair-difference branches.
```

This is formally parallel to A65--A67 but simpler because the move swaps two atoms instead of inserting one atom into a zero block.

---

## 8. Current global proof obligations after A68

The proof program now has these open global obligations:

```text
O1. Pair-difference recurrence R3.
O2. Singleton-prefix recurrence R4.
O3. Cyclic-cut recurrence R5.
O4. Weighted core cut-selection theorem.
O5. Final global termination theorem assembling all routed classes.
```

The highest-value next branch is R3.

---

## 9. Target A69

Analyze A33 Q2 pair-swap forbidden recurrence.

Start from a pair-difference boundary of form

```text
q-q1=sum(P)
```

or the equivalent A33 notation.

After pair swap, suppose a forbidden hit occurs at a prefix

```text
x+Y_m=f.
```

Apply A5 at that hit.  Pull back blockers through the pair swap.  Classify:

```text
left/right blockers inside the swapped pair neighborhood;
external bridge blockers;
endpoint pair traps;
proper-prefix descents.
```

Expected result:

```text
pair-difference recurrence routes to equal/separated interval,
zero-composite,
smaller pair-difference,
or singleton recurrence.
```

---

## Current status

Proved/recorded here:

1. atom-insertion recurrence H1/H2 status after A65--A67;
2. R1/R2 are no longer standalone A34 gaps;
3. remaining recurrence sources are R3--R5;
4. next target is pair-difference recurrence.

Not proved here:

1. pair-difference recurrence routing;
2. singleton-prefix recurrence routing;
3. cyclic-cut recurrence routing;
4. weighted cut-selection;
5. endpoint avoidance theorem.
