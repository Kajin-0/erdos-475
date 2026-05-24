# F00.SNS.C4 collision pullback without forbidden endpoints

This file continues the strong nonzero-sum repair path.

C3 isolated the next required theorem:

```text
SNS collision-pullback theorem:
A transformed move in strong nonzero-sum mode either decreases D_SNS^*,
creates endpoint collision algebra,
creates external collision algebra,
creates weighted normal form,
or reaches collision-free success.
```

Unlike the endpoint-avoidance proof, there is no forbidden value `f` in the strong nonzero-sum start.  Therefore the recurrence machinery based on forbidden hits must be replaced by collision-only pullback logic.

Status: repair draft.

---

## C4.1. SNS mode

In strong nonzero-sum mode, the target is:

```text
S_0,S_1,...,S_t pairwise distinct.
```

There is no distinguished forbidden value `f`.

Thus every transformed local move has only two ordering outcomes:

```text
1. collision-free;
2. collision-producing.
```

The earlier endpoint-avoidance trichotomy

```text
success / collision / forbidden recurrence
```

becomes the SNS dichotomy

```text
collision-free success / collision pullback.
```

---

## C4.2. Local move setup

Let the ordering be decomposed as

```text
R = X W Y
```

and let a local move replace `W` by `W'`:

```text
R' = X W' Y.
```

Assume:

```text
sum(W')=sum(W).
```

Let

```text
x=sum(X),
w=sum(W).
```

The boundary endpoints of the window are unchanged:

```text
x,
x+w.
```

Only internal endpoint values inside `W` may move.

---

## C4.3. SNS collision types

A collision in `R'` is an equality

```text
S'_a=S'_b,
0<=a<b<=t.
```

There are four types:

```text
L1. both endpoints unchanged from R;
L2. both endpoints moved inside W';
L3. one moved endpoint, one unchanged displayed endpoint inside the local table;
L4. one moved endpoint, one external endpoint outside the displayed local table.
```

Type L1 is a pre-existing collision.  In defect-minimal arguments it must be compared to the active collision profile.

Types L2--L4 are new collision data and must be pulled back.

---

## Lemma C4.1: unchanged collisions are defect-profile data

If a transformed collision uses only endpoints unchanged from the original ordering, then it is already present in `R`.  It cannot be the first new obstruction caused by the local move.

### Proof

Unchanged endpoints have the same values before and after the local move.  Therefore their equality existed before the move. ∎

### Use

In arbitrary-start SNS mode, unchanged collisions are not contradictions.  They are measured by the collision profile `P_col(R)` and location tie-breaker `L_col^*(R)`.

---

## C4.4. Internal moved-moved collisions

Every moved internal endpoint has form

```text
x+u
```

where `u` is a displayed prefix expression in `W'`.

A moved-moved collision is

```text
x+u=x+v.
```

Thus

```text
u-v=0.
```

## Lemma C4.2: moved-moved collision gives local zero/equal/signed data

A collision between two moved internal endpoints pulls back to one of:

```text
zero interval;
equal interval;
signed interval;
pair-difference boundary;
zero-composite;
weighted normal form if coefficient-2 data survives normalization.
```

### Proof

Subtract the two endpoint expressions.  The difference is a relation among displayed prefixes/suffixes of `W'`.  If the intervals overlap, uncrossing gives zero/equal interval data.  If they are disjoint, it is separated-equal or zero-composite.  If the endpoint expressions include bounded atom corrections, the output is signed interval or pair-difference.  If a genuine coefficient-2 pattern survives all transported-prefix reductions, it is a weighted normal form. ∎

---

## C4.5. Moved-unchanged displayed collisions

A moved endpoint has value

```text
x+u.
```

An unchanged displayed endpoint in the local table has value

```text
x+d.
```

Collision gives

```text
u=d.
```

or

```text
u-d=0.
```

## Lemma C4.3: moved-unchanged displayed collision gives interval obstruction

A collision between a moved endpoint and an unchanged displayed endpoint inside the local table pulls back to:

```text
proper-overlap equal interval;
separated equal interval;
two-piece zero-composite;
pair-difference boundary;
transported-prefix relation;
weighted normal form if coefficient-2 data survives.
```

### Proof

The two endpoint values are represented by displayed interval sums based at the same local basepoint.  Equality gives equality of interval sums.  Overlap/containment uncrosses to smaller zero/equal data; disjointness gives separated-equal; boundary corrections give pair-difference or transported-prefix.  A surviving genuine coefficient-2 relation is routed to weighted normal form. ∎

---

## C4.6. Moved-external collisions

A moved endpoint colliding with an endpoint outside the displayed local table is an external collision.

## Lemma C4.4: moved-external collision routes to phase-aware F6/F8

A moved-external collision pulls back to one of:

```text
bridge zero-composite;
signed bridge composite;
equal/separated interval;
transported-prefix relation;
pair-difference boundary;
weighted normal form;
cyclic/wrapped collision data.
```

In ARBITRARY phase, zero intervals produced by this pullback are zero defects, not contradictions.

### Proof

This is the F6 external-collision classification, with the phase-aware interpretation from C3.  The algebra does not require the whole ordering to be collision-free. ∎

---

## C4.7. Collision-free transformed ordering

If `R'` has no endpoint collisions among

```text
S'_0,S'_1,...,S'_t,
```

then `R'` is a strong nonzero-sum ordering.

## Lemma C4.5: collision-free transformed ordering is SNS success

In SNS mode, a transformed ordering with no endpoint collisions is terminal success.

### Proof

The strong nonzero-sum target is exactly pairwise distinctness of the extended partial sums. ∎

---

## C4.8. Collision-pullback theorem

## Theorem C4.6: SNS collision-pullback theorem

Let a local move replace `W` by `W'` inside `X W Y`, preserving the window sum.  In SNS mode, the transformed ordering either:

```text
1. is collision-free, giving strong nonzero-sum success;
2. has only unchanged collisions, which are pre-existing defect-profile data;
3. has a moved-moved collision routed by Lemma C4.2;
4. has a moved-unchanged displayed collision routed by Lemma C4.3;
5. has a moved-external collision routed by Lemma C4.4.
```

Thus every new collision caused by the move enters the phase-aware F3 state machine without using forbidden-hit recurrence.

### Proof

If the transformed ordering has no collisions, Lemma C4.5 gives success.  Otherwise choose a collision pair.  If both endpoints are unchanged, Lemma C4.1 applies.  If both are moved, Lemma C4.2 applies.  If exactly one is moved and the other is displayed locally, Lemma C4.3 applies.  If exactly one is moved and the other is outside the displayed table, Lemma C4.4 applies.  These cases exhaust endpoint pairs. ∎

---

## C4.9. Defect descent interface

The collision-pullback theorem does not by itself prove descent of `D_SNS^*`.  It provides the algebraic branch.  The descent claim must be handled by the phase-aware local lemmas.

Required phase-aware rule:

```text
A zero interval in ARBITRARY phase must be compared to the active collision profile.
If it has smaller span, contradiction to minimality.
If it has equal span and earlier location, contradiction to active choice.
If it has equal/larger span but arises from the transformed move, it is the active routed obstruction.
If it has larger span, it cannot block descent of the active shortest defect.
```

---

## C4.10. Relation to F7

F7 remains necessary for endpoint avoidance after a Graham-valid ordering has been obtained.  But F7 is not the correct primitive for the arbitrary-start SNS proof because F7 is organized around forbidden endpoint recurrence.

In SNS mode, replace F7 calls with:

```text
C4 collision pullback;
phase-aware F4/F5/F6/F8/F10/F11;
defect-profile comparison.
```

Once the proof reaches `COLLISION_FREE` phase, F12/F7 can be used for endpoint avoidance strengthening.

---

## C4.11. Remaining phase-aware rewrites

C4 proves the collision-pullback classification.  The following files still need phase-aware versions or annotations:

```text
F4 local descent: zero intervals are defects in ARBITRARY phase;
F5 separated-equal: gap reduction should decrease D_SNS^* or route algebraically;
F6 external collision: zero outputs are defects in ARBITRARY phase;
F8 bridge/gap: bridge zero outputs are defects until collision-free;
F10/F11 weighted branch: weighted success/collision language must be translated to defect descent or SNS success.
```

---

## C4.12. Conditional SNS start theorem update

## Theorem C4.7: SNS arbitrary start, collision-pullback version

Assume:

```text
1. C2 q-through-zero-interval obstruction theorem;
2. C4 SNS collision-pullback theorem;
3. phase-aware F4/F5/F6/F8/F10/F11;
4. D_SNS^* descent for strongly clean insertion.
```

Then a `D_SNS^*`-minimal ordering with `sigma(S) != 0` either:

```text
1. is strong nonzero-sum;
2. admits a strongly clean insertion, contradicting minimality;
3. enters the phase-aware obstruction engine through collision algebra;
4. reaches contradiction of atom/subset assumptions.
```

### Proof

If the ordering is collision-free, it is strong nonzero-sum.  Otherwise choose the active shortest zero interval and adjacent outside atom.  Strongly clean insertion contradicts minimality by C1.  Non-clean insertion produces a collision.  The collision is classified by Theorem C4.6 and routed to the phase-aware obstruction engine. ∎

---

## C4.13. What C4 resolves

Resolved:

```text
1. forbidden-hit recurrence is removed from the arbitrary-start SNS proof;
2. transformed local moves now have a collision-free/collision dichotomy;
3. every new collision has a pullback classification;
4. F7 is deferred until endpoint avoidance strengthening after collision-free ordering exists.
```

Remaining:

```text
1. phase-aware versions of F4/F5/F6/F8/F10/F11;
2. proof that every phase-aware branch decreases D_SNS^* or reaches SNS success;
3. weighted branch interpretation in ARBITRARY phase;
4. full strong nonzero-sum theorem.
```

---

## C4.14. Recommended next file

The next file should add phase-aware annotations to the local descent theorem:

```text
docs/final/F00_SNS_C5_phase_aware_local_descent.md
```

Goal:

```text
Rewrite F4/F5/F6/F8 zero/equal/signed outputs so they decrease D_SNS^* in ARBITRARY phase instead of being treated as contradictions.
```

---

## C4.15. Status

```text
Status: collision-pullback repair draft.
Risk: ORANGE/RED.
Main remaining gap: phase-aware descent for local and bridge outputs.
```
