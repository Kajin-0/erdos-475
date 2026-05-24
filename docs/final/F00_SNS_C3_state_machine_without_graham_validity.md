# F00.SNS.C3 state machine without Graham-validity

This file continues the strong nonzero-sum repair path.

The previous draft `F00_SNS_C2_q_through_zero_interval_obstruction.md` identified a structural issue:

```text
F3--F11 currently treat zero intervals as contradictions.
But in the arbitrary-ordering start, zero intervals are defects, not contradictions.
```

C3 repairs the state-machine interface by distinguishing two phases:

```text
Phase I: arbitrary-ordering repair phase, where zero intervals are collision defects;
Phase II: Graham-valid / collision-free phase, where zero intervals are contradictions.
```

This distinction is necessary to avoid circularly assuming Graham-validity.

Status: repair draft.

---

## C3.1. Two-phase state model

Extend the obstruction state from F3:

```text
Omega=(R,I,C,E,M,tag)
```

by adding a validity phase:

```text
Omega=(R,I,C,E,M,tag,phase)
```

where

```text
phase in {ARBITRARY, COLLISION_FREE}.
```

The meaning is:

```text
ARBITRARY       = the current ordering may contain endpoint collisions;
COLLISION_FREE  = the current ordering has no endpoint collisions among S_0,...,S_t.
```

For strong nonzero-sum, `COLLISION_FREE` is already success.

For endpoint avoidance, `COLLISION_FREE` means the ordering is Graham-valid, and one may then minimize forbidden endpoint hits.

---

## C3.2. Zero interval interpretation by phase

## Definition C3.1: phase-dependent zero interval status

A nonempty zero interval has different status depending on phase.

```text
ARBITRARY phase:
  zero interval = collision defect / repair state.

COLLISION_FREE phase:
  zero interval = contradiction.
```

This prevents the arbitrary-ordering repair from falsely terminating when it merely discovers the defect it is trying to remove.

---

## Lemma C3.2: zero interval is contradiction only in COLLISION_FREE phase

If `phase=COLLISION_FREE`, then a nonempty zero interval contradicts the phase assumption.  If `phase=ARBITRARY`, a zero interval is a legitimate defect state.

### Proof

A nonempty zero interval between positions `i<j` gives `S_i=S_j`.  In `COLLISION_FREE` phase, such endpoint equality is forbidden.  In `ARBITRARY` phase, endpoint collisions are allowed and are exactly the defects being repaired. ∎

---

## C3.3. Arbitrary-phase obstruction classes

In `ARBITRARY` phase, add the following repair classes:

```text
ZERO_DEFECT,
SHORTEST_ZERO_DEFECT,
Q_INSERTION_REPAIR,
LOCAL_COLLISION_REPAIR,
EXTERNAL_COLLISION_REPAIR,
DEFECT_DESCENT,
DEFECT_TERMINAL_SUCCESS.
```

These are not new mathematical obstruction species.  They are wrappers around the existing F3 classes with different terminal interpretation.

Mapping:

```text
ZERO_DEFECT              -> zero interval collision defect;
SHORTEST_ZERO_DEFECT     -> active minimal zero interval Z;
Q_INSERTION_REPAIR       -> insert adjacent q into Z;
LOCAL_COLLISION_REPAIR   -> routes to F4/F5/F7-style algebra;
EXTERNAL_COLLISION_REPAIR-> routes to F6/F8-style bridge algebra;
DEFECT_DESCENT           -> D_SNS^* strictly decreases;
DEFECT_TERMINAL_SUCCESS  -> no endpoint collisions remain.
```

---

## C3.4. Phase-aware terminal states

For strong nonzero-sum:

```text
phase=COLLISION_FREE -> SUCCESS.
```

For arbitrary phase:

```text
DEFECT_DESCENT -> restart minimization with smaller D_SNS^*;
DEFECT_TERMINAL_SUCCESS -> enter COLLISION_FREE -> SUCCESS;
zero interval -> not contradiction;
nonzero atom violation -> contradiction;
distinct subset atom violation -> contradiction.
```

---

## C3.5. Arbitrary-phase transition types

The existing F3 transitions still apply:

```text
T1 adjacent swap;
T2 block exchange;
T3 gap-after move;
T4 weighted cut-swap;
T5 cyclic cut;
T6 atom-insertion normalization;
T7 A5 blocker pullback;
T8 external collision pullback;
T9 normal-form rewrite.
```

Add one phase-specific repair transition:

```text
T0 q-insertion repair through shortest zero interval.
```

T0 is not a new algebraic move.  It is a finite sequence of T1 adjacent swaps moving an adjacent outside atom through a shortest zero interval.

---

## Lemma C3.3: T0 decomposes into adjacent swaps

The q-insertion repair transition is a finite sequence of adjacent swaps, hence is already covered by the F3 state-machine move set at the local algebra level.

### Proof

Moving `q` from one side of `Z=z_1...z_m` to an interior position after `z_k` is performed by repeatedly swapping `q` with adjacent atoms `z_m,z_{m-1},...,z_{k+1}`. ∎

---

## C3.6. Routing local collisions in ARBITRARY phase

When q-insertion creates a local collision, it gives a zero interval or signed interval.  In `COLLISION_FREE` phase, a zero interval is contradiction.  In `ARBITRARY` phase, it must be compared to the active defect measure.

## Lemma C3.4: local collision repair either descends or enters existing algebra

In `ARBITRARY` phase, a local collision created during q-insertion either:

```text
1. has smaller collision span than the active shortest zero interval, contradicting minimality;
2. has the same span but earlier/equal location, contradicting strong cleanliness unless routed as the active obstruction;
3. has larger span and is lower priority than the active repaired defect;
4. produces signed/equal/pair data routed by F4/F5/F7.
```

### Proof

Every local collision is equality of two local endpoint formulas.  Same-side collisions give zero subintervals of `Z`, impossible with smaller span by shortestness.  Cross-side collisions contain `q` and produce signed/equal/pair data.  Equal-span collisions are controlled by the collision profile and location tie-breaker from C1. ∎

---

## C3.7. External collisions in ARBITRARY phase

External collisions created during q-insertion remain external collisions.  Their interpretation does not require Graham-validity, except that zero intervals produced by the pullback are repair states rather than contradictions.

## Lemma C3.5: external collision repair routes to bridge/gap or defect descent

In `ARBITRARY` phase, a moved external collision during q-insertion routes to:

```text
1. bridge/equal/signed interval repair handled by F6/F8 algebra;
2. zero defect with smaller or controlled span;
3. weighted normal form handled by F10/F11;
4. recurrence-style moved-prefix data if a forbidden endpoint is also tracked later.
```

### Proof

F6 classifies the external collision algebra without needing the whole ordering to be collision-free.  The only phase-sensitive output is zero interval status: in `ARBITRARY` phase it is a zero defect to be measured by `D_SNS^*`. ∎

---

## C3.8. Weighted outputs in ARBITRARY phase

A weighted normal form may appear during arbitrary-phase repair.  This is acceptable only if the weighted branch is interpreted as algebraic routing and not as relying on prior Graham-validity.

## Audit flag C3.W

F10/F11 use collision/recurrence terminology inherited from Graham-valid transformations.  Before using F10/F11 in ARBITRARY phase, verify:

```text
1. displayed collision algebra in F10 does not require global collision-freeness;
2. weighted cut-swap success means decrease of D_SNS^* or collision-free success, not merely Graham-valid endpoint avoidance;
3. recurrence language involving forbidden f is omitted in pure strong nonzero-sum mode;
4. zero-collapse outputs are returned to ZERO_DEFECT unless collision-free phase has been reached.
```

This is a significant audit item.

---

## C3.9. Pure strong nonzero-sum mode

For the SNS proof, there is no forbidden value `f`.

Therefore recurrence classes involving `f` should be disabled or reinterpreted as collision-only classes.

In SNS mode:

```text
FORBIDDEN_RECURRENCE is absent;
SINGLETON_RECURRENCE involving f is absent;
CYCLIC_RECURRENCE involving f is absent unless it produces endpoint collision data;
A5 blocker pullback is used only after a collision-producing transformed move.
```

This means F7 cannot be imported unchanged into the SNS arbitrary-start proof.  It needs an SNS-specialized recurrence/collision-pullback version.

---

## Needed Lemma C3.6: SNS collision-pullback theorem

A transformed move in SNS mode either:

```text
1. decreases D_SNS^*;
2. creates an endpoint collision with explicit zero/equal/signed interval algebra;
3. creates an external collision routed by F6/F8 algebra;
4. creates weighted normal form F10/F11;
5. reaches collision-free success.
```

No forbidden-hit recurrence is used.

### Status

Open.  This replaces the F7 recurrence theorem for the pure SNS start.

---

## C3.10. Revised non-circular SNS architecture

The non-circular strong nonzero-sum proof should use this architecture:

```text
1. Choose D_SNS^*-minimal ordering.
2. If no collisions, success.
3. Else choose active shortest zero interval Z.
4. Choose adjacent outside atom q.
5. Move q into useful interior positions of Z.
6. Strongly clean insertion contradicts minimality.
7. Non-clean insertion creates collision algebra.
8. Collision algebra is routed by SNS-specific versions of F4/F5/F6/F8/F10/F11.
9. Every route either decreases D_SNS^*, reaches collision-free success, or contradicts atom/subset assumptions.
```

This avoids the forbidden-endpoint recurrence machinery until Graham-validity has been established.

---

## C3.11. Conditional theorem

## Theorem C3.7: arbitrary-start state-machine interface, conditional

Assume:

```text
1. C2 q-through-zero-interval obstruction theorem;
2. C3.6 SNS collision-pullback theorem;
3. phase-aware versions of F4/F5/F6/F8/F10/F11;
4. every zero interval in ARBITRARY phase is measured as a defect rather than contradiction.
```

Then the arbitrary-ordering start for strong nonzero-sum enters a well-founded repair state machine without assuming Graham-validity.

### Proof

C2 sends every non-clean insertion to local/external/weighted algebra.  C3 reinterprets zero intervals as repair defects in `ARBITRARY` phase.  C3.6 replaces forbidden recurrence with collision-pullback routing.  The phase-aware final lemmas consume every output either by defect descent, collision-free success, or contradiction of atom/subset assumptions. ∎

---

## C3.12. What C3 resolves

Resolved:

```text
1. zero intervals are no longer falsely treated as contradictions before Graham-validity;
2. arbitrary-ordering repair is separated from endpoint-avoidance recurrence;
3. q-insertion repair is identified as adjacent-swap machinery;
4. the need for an SNS-specific collision-pullback theorem is isolated.
```

Not resolved:

```text
1. SNS collision-pullback theorem C3.6;
2. phase-aware rewriting of F4/F5/F6/F8/F10/F11;
3. weighted outputs in ARBITRARY phase;
4. final proof of strong nonzero-sum.
```

---

## C3.13. Recommended next file

The next file should define the SNS-specific collision-pullback theorem:

```text
docs/final/F00_SNS_C4_collision_pullback_no_forbidden.md
```

Goal:

```text
Replace forbidden-hit recurrence with collision-pullback routing suitable for strong nonzero-sum mode.
```

Minimum contents:

```text
1. transformed move trichotomy in SNS mode: success or collision;
2. local collision pullback equations;
3. external collision pullback equations;
4. weighted normal-form outputs;
5. proof that every output decreases D_SNS^* or enters phase-aware F4/F5/F6/F8/F10/F11.
```

---

## C3.14. Status

```text
Status: architectural repair draft.
Risk: RED.
Main remaining gap: SNS collision-pullback theorem and phase-aware final lemmas.
```
