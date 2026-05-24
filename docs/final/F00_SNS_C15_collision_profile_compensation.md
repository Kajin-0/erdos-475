# F00.SNS.C15 collision-profile compensation

This file continues the strong nonzero-sum repair path.

C14 identified the highest-risk remaining item:

```text
C7.2 collision-profile compensation:
A local collision-profile change in a weighted self-return either gives defect descent,
invalidates the non-descending self-return, or creates an external/bridge compensation branch.
```

C15 sharpens that statement and gives a proof framework.

Status: hardening draft.

---

## C15.1. Setup

Work in ARBITRARY phase with global defect profile

```text
D_SNS^*(R)=(P_col(R),L_col^*(R),boundary_rank(R)).
```

Let a weighted repair self-return be a finite path

```text
Omega_0 -> Omega_1 -> ... -> Omega_N
```

where:

```text
Omega_0.C = WEIGHTED_REPAIR,
Omega_N.C = WEIGHTED_REPAIR.
```

The path is non-descending if:

```text
D_SNS^*(Omega_N) >= D_SNS^*(Omega_0),
```

and if equality holds in `D_SNS^*`, then the weighted middle length does not decrease:

```text
|B_N| >= |B_0|.
```

A minimal non-descending self-return is chosen by:

```text
1. shortest path length N;
2. fewest local collision-profile changes;
3. fewest endpoint-pattern changes;
4. smallest local weighted measure.
```

---

## C15.2. Local and external collision support

A transition has local collision support if every endpoint collision changed by the transition has both endpoints in the active displayed window.

A transition has external collision support if at least one changed collision involves one endpoint outside the active displayed window.

A profile compensation is external if a local decrease in `P_col` or `L_col^*` is offset by a new or worsened collision involving an external endpoint.

---

## Lemma C15.1: purely local profile improvement gives D_SNS^* descent

If a weighted self-return transition changes only collisions supported inside the active window and strictly improves the local contribution to `D_SNS^*`, with no external collision change, then the global `D_SNS^*` strictly decreases.

### Proof

The global collision profile is the sum of local-window, external, and cross-window collision contributions by span/location.  If only local-window contributions change and the first changed profile coordinate improves, while all other contributions are unchanged, then the global profile improves at the same first changed coordinate.  Thus `D_SNS^*` decreases. ∎

---

## Lemma C15.2: purely local profile worsening invalidates non-descending minimality

If a weighted self-return transition changes only local-window collisions and worsens `D_SNS^*`, then the path cannot be part of a minimal non-descending self-return unless a later transition reverses that exact worsening.  In that case the change/undo segment can be shortened or replaced by a lower-ranked local repair branch.

### Proof sketch

If the global defect worsens and is never undone, the final state is not non-descending in the required minimal sense.  If it is undone later, take the first transition that restores the previous collision-profile coordinate.  The segment between the first worsening and first restoration changes only local endpoint data while returning the global profile.  By minimality of path length, such a neutral local excursion is forbidden unless one of its endpoints creates a classified local repair obstruction.  That obstruction is handled by C11/C13 and exits the self-return. ∎

### Audit note

The replacement/shortening argument must be written as a formal finite-state lemma in the manuscript.

---

## C15.3. Compensation requires cross-window collision

Suppose a local transition improves the collision profile inside the active window but the global profile does not improve.  Then another collision contribution must worsen at the same or earlier profile coordinate.

If that worsening is not local, it is necessarily cross-window or external.

## Lemma C15.3: profile compensation produces an external collision branch

If a local profile improvement in a weighted repair transition is exactly compensated so that global `D_SNS^*` does not decrease, then there exists a changed collision involving at least one endpoint outside the active weighted window.  This collision is a moved-external collision and routes to EXTERNAL_COLLISION / BRIDGE_GAP.

### Proof

A local improvement reduces some count `N_s` or improves the first-location coordinate at the first affected span/location.  If the global profile does not improve, then some other collision pair of span `<=s` must be created or moved earlier.  Since the purely local contribution improved, the compensating pair cannot be fully internal to the same local endpoint set unless it contradicts the assumed local improvement.  Therefore at least one endpoint lies outside the active window or in an unchanged family crossing the boundary.  Because the transition changed the collision status, at least one endpoint of the compensating pair is moved.  Hence it is a moved-external collision in the sense of C4/C12. ∎

---

## C15.4. Compensation cannot be invisible

A profile compensation cannot occur without a detectable endpoint equality.

## Lemma C15.4: no invisible profile compensation

Every change in `P_col` or `L_col^*` is witnessed by an explicit endpoint equality appearing or disappearing:

```text
S_a=S_b.
```

If the equality appears or disappears because of a local weighted transition, then at least one of `S_a,S_b` is a moved endpoint.

### Proof

Collision profile coordinates count endpoint-equality pairs.  Changing a count or first-location coordinate means some equality pair was added, removed, or shifted.  Unmoved endpoints retain their values and positions relative to each other, so any changed equality must include a moved endpoint. ∎

---

## C15.5. Compensation theorem

## Theorem C15.5: collision-profile compensation theorem

In a phase-aware weighted repair self-return, any collision-profile change along the path gives one of:

```text
1. strict D_SNS^* descent;
2. disqualification of the path as a minimal non-descending self-return;
3. a removable local change/undo excursion contradicting minimality;
4. a moved-external collision routed to EXTERNAL_COLLISION / BRIDGE_GAP;
5. a local collision routed to C11 local repair;
6. a weighted lower-rank/smaller-middle branch routed by C13.
```

Thus a minimal non-descending weighted self-return with no routed exit must preserve the collision-profile contribution of the active weighted window.

### Proof

If the profile change is purely local and improves the global profile, Lemma C15.1 gives descent.  If it worsens and is not later corrected, the path is not a valid minimal non-descending return; if it is later corrected, Lemma C15.2 applies.  If local improvement is compensated globally, Lemma C15.3 gives a moved-external collision, routed by C12.  If the changed equality is internal, it is a local collision routed by C11.  If the change also alters weighted middle support or boundary data, C13 handles it as a lower-rank or smaller-middle weighted branch. ∎

---

## C15.6. Consequence for C7

C15 hardens C7.2 in the following form.

## Corollary C15.6: profile preservation in minimal weighted self-return

A minimal phase-aware weak cut-rigid weighted self-return that does not descend and does not route to local/external/weighted lower-rank repair must preserve:

```text
1. global D_SNS^*;
2. local collision-profile contribution of the weighted window;
3. first-collision location contribution of the weighted window;
4. boundary-rank contribution of the weighted window.
```

Therefore phase-aware pattern-rigidity may legitimately include collision-profile preservation as one of its required components.

---

## C15.7. Remaining audit items

C15 reduces the C7.2 red item to two formal writeups:

```text
R1. Formal finite-state change/undo shortening lemma for Lemma C15.2.
R2. Explicit decomposition of collision profile into local, external, and cross-window contributions for Lemma C15.3.
```

The conceptual compensation branch is now classified:

```text
compensation -> moved-external collision -> C12 EXTERNAL_COLLISION/BRIDGE_GAP.
```

---

## C15.8. Recommended next file

Next harden C7.3:

```text
docs/final/F00_SNS_C16_first_changed_endpoint.md
```

Goal:

```text
Prove the first-changed-endpoint lemma in SNS mode without forbidden recurrence.
```

---

## C15.9. Status

```text
Status: C7.2 hardening draft.
Risk: ORANGE.
Remaining red items: C7.3 first changed endpoint and C7.4 support/boundary/label diagnostics.
```
