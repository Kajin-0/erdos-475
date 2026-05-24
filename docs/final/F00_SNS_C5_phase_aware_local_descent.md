# F00.SNS.C5 phase-aware local descent

This file continues the strong nonzero-sum repair path.

C3 introduced the phase-aware state machine:

```text
ARBITRARY phase:
  zero intervals are collision defects.

COLLISION_FREE phase:
  zero intervals are contradictions.
```

C4 supplied the SNS collision-pullback theorem without forbidden endpoints.  C5 now rewrites the local descent outputs of F4/F5/F6/F8 for the ARBITRARY phase.

The purpose is to prevent a false contradiction when a zero interval appears before strong nonzero-sum has been established.

Status: repair draft.

---

## C5.1. Phase-aware state

Use the phase-aware obstruction state

```text
Omega=(R,I,C,E,M,tag,phase)
```

where

```text
phase in {ARBITRARY, COLLISION_FREE}.
```

The strong nonzero-sum proof starts in `ARBITRARY` phase and attempts to reach `COLLISION_FREE` phase.

In `ARBITRARY` phase, the active measure is the refined collision-defect vector

```text
D_SNS^*(R)=(P_col(R),L_col^*(R),boundary_rank(R)).
```

In `COLLISION_FREE` phase, no endpoint collision exists and the strong nonzero-sum target has been reached.

---

## C5.2. Phase-aware zero interval rule

## Definition C5.1: zero interval handling

If a nonempty zero interval `Z` appears:

```text
phase=ARBITRARY:
  Z is a collision defect measured by D_SNS^*.

phase=COLLISION_FREE:
  Z is a terminal contradiction.
```

---

## Lemma C5.2: zero interval creates defect descent or active repair in ARBITRARY phase

Let `R` be `D_SNS^*`-minimal with active shortest zero interval of span `m`.  If a local move produces a zero interval `Z'` of span `m'`, then:

```text
1. if m'<m, this contradicts minimality of R;
2. if m'=m and Z' is lexicographically earlier than the active interval, this contradicts active choice;
3. if m'=m and Z' is the active interval, the move has not repaired the active defect;
4. if m'>m, then Z' is lower priority than the active defect and cannot block descent caused by repairing the active defect;
5. if Z' is the new routed active defect, it remains in ARBITRARY phase as ZERO_DEFECT.
```

### Proof

A zero interval is exactly an endpoint collision.  Its span and location are compared against the collision profile `P_col` and active-location coordinate `L_col^*`.  The listed cases are the lexicographic alternatives. ∎

---

## C5.3. Phase-aware F4 local outputs

F4 outputs include:

```text
zero interval,
two-piece zero,
higher zero-composite,
equal interval,
signed interval,
pair-difference,
transported-prefix.
```

In ARBITRARY phase these are not automatically contradictions.  They are converted into collision-defect repair states.

---

## Lemma C5.3: phase-aware zero/equal/pair local descent

In ARBITRARY phase, every F4 local output either:

```text
1. produces a zero interval compared by Lemma C5.2;
2. produces an equal interval whose uncrossing gives a zero defect of smaller support/span;
3. produces a signed interval or pair-difference relation routed as local collision algebra;
4. produces transported-prefix data routed to phase-aware weighted normal form;
5. produces defect descent in D_SNS^*;
6. remains as an active repair state in the phase-aware state machine.
```

### Proof

F4's algebraic classifications do not require collision-freeness.  What changes is only the terminal interpretation.  Every zero output is measured against `D_SNS^*`; equal and signed outputs are uncrossed or normalized into zero/equal/pair repair states; transported-prefix data either reduces to a non-weighted repair state or enters weighted normal form. ∎

---

## C5.4. Phase-aware F5 separated-equal outputs

F5 separated-equal/midpoint routing uses:

```text
direct exchange;
gap-after move;
rigid separated return;
adjacent-equal/midpoint branch.
```

In ARBITRARY phase, these moves are judged by collision-defect descent rather than forbidden-endpoint avoidance.

## Lemma C5.4: phase-aware separated-equal routing

In ARBITRARY phase, a separated-equal or midpoint branch either:

```text
1. decreases collision profile by removing a shortest zero/equal defect;
2. decreases gap/support/span in the local repair measure;
3. creates local collision algebra routed by C5.3;
4. creates external collision algebra routed by phase-aware F6/F8;
5. creates weighted normal form routed by phase-aware F10/F11;
6. reaches COLLISION_FREE phase.
```

### Proof

The direct-exchange and gap-after algebra from F5 remains valid.  A successful move is interpreted as reducing endpoint collision defects, not as avoiding a forbidden value.  Collisions produced by the move are classified by C4.  Gap/support/span decreases are retained as repair-measure decreases. ∎

---

## C5.5. Phase-aware F6 external outputs

F6 external collisions produce bridge zero-composites, signed bridge composites, equal/separated intervals, pair-difference data, and weighted normal forms.

## Lemma C5.5: phase-aware external collision routing

In ARBITRARY phase, every F6 external collision output either:

```text
1. creates a zero defect measured by D_SNS^*;
2. creates a bridge/gap repair state handled by phase-aware F8;
3. creates local equal/signed/pair data handled by C5.3;
4. creates weighted normal form handled by phase-aware F10/F11;
5. creates defect descent by reducing the active collision profile;
6. reaches collision-free success.
```

### Proof

The F6 pullback formulas are algebraic and do not require Graham-validity.  Left and right external collisions become bridge zero-composites.  Signed corrections become signed bridge composites.  Unchanged-family collisions become interval obstructions.  In ARBITRARY phase these are repair states rather than contradictions unless they violate atom distinctness or nonzero atom assumptions. ∎

---

## C5.6. Phase-aware F8 bridge/gap outputs

F8 bridge/gap routing relies on span, gap, and support descent.  Those remain valid in ARBITRARY phase, but zero outputs become defects.

## Lemma C5.6: phase-aware bridge/gap descent

In ARBITRARY phase, every F8 bridge/gap output either:

```text
1. decreases enclosing span, bridge gap, or support size;
2. creates a zero defect compared by Lemma C5.2;
3. routes to local equal/signed/pair repair via C5.3;
4. routes to separated-equal repair via C5.4;
5. routes to external collision repair via C5.5;
6. routes to weighted normal form;
7. reaches collision-free success.
```

### Proof

Proper-overlap and proper-containment uncrossing still decrease the geometric measure.  Gap-after success still reduces the separated gap.  Rigid separated returns still factor through direct exchange or local routing.  The only phase-dependent change is zero interval status. ∎

---

## C5.7. Phase-aware weighted outputs

Weighted normal forms may appear before collision-freeness.  They cannot be treated as endpoint-avoidance weighted cores with forbidden recurrence.  They must be interpreted as algebraic coefficient-2 repair states.

## Needed Lemma C5.W: phase-aware weighted repair theorem

In ARBITRARY phase, every weighted normal form either:

```text
1. reduces to non-weighted local repair by easy reductions;
2. performs a cut-swap whose collisions are classified by C4/F10 algebra;
3. decreases D_SNS^* or enters a smaller weighted repair state;
4. exits to phase-aware F4/F5/F6/F8 repair;
5. reaches COLLISION_FREE phase.
```

### Status

Open.  This is the main remaining phase-aware adaptation after C5.

The previous F10/F11 weighted proofs cannot be imported unchanged because they use endpoint-avoidance recurrence language.  The displayed collision algebra remains usable; the forbidden recurrence layer must be replaced by C4 collision-pullback logic.

---

## C5.8. Phase-aware local termination principle

## Theorem C5.7: phase-aware non-weighted local descent, conditional on weighted repair

Assume C5.W.  In ARBITRARY phase, every non-weighted local output produced by C4 either:

```text
1. strictly decreases D_SNS^*;
2. decreases an auxiliary local span/gap/support coordinate feeding into D_SNS^*;
3. routes to another phase-aware non-weighted repair class;
4. routes to phase-aware weighted repair;
5. reaches COLLISION_FREE success;
6. contradicts atom nonzero or distinctness assumptions.
```

### Proof

Local zero/equal/pair outputs are Lemma C5.3.  Separated-equal outputs are Lemma C5.4.  External outputs are Lemma C5.5.  Bridge/gap outputs are Lemma C5.6.  Weighted outputs are C5.W.  These exhaust C4 collision-pullback outputs. ∎

---

## C5.9. What C5 resolves

Resolved:

```text
1. F4/F5/F6/F8 outputs are reinterpreted in ARBITRARY phase;
2. zero intervals are measured as defects, not contradictions;
3. local and bridge/gap descent remain algebraically valid;
4. the next bottleneck is isolated as phase-aware weighted repair.
```

Not resolved:

```text
1. C5.W phase-aware weighted repair theorem;
2. full D_SNS^* descent proof for every phase-aware branch;
3. final strong nonzero-sum theorem.
```

---

## C5.10. Recommended next file

The next file should handle weighted outputs in ARBITRARY phase:

```text
docs/final/F00_SNS_C6_phase_aware_weighted_repair.md
```

Goal:

```text
Adapt F10/F11 weighted normal form and cut-selection to collision-defect mode without forbidden endpoint recurrence.
```

---

## C5.11. Status

```text
Status: phase-aware non-weighted repair draft.
Risk: ORANGE/RED.
Main remaining gap: phase-aware weighted repair theorem C5.W.
```
