# F00.SNS.C7 phase-aware weak cut-rigidity

This file continues the strong nonzero-sum repair path.

C6 isolated the remaining weighted adaptation gap:

```text
Needed Lemma C6.5:
phase-aware weak cut-rigidity reduces to pattern-rigidity or defect descent.
```

This file translates the A90--A94 weak-to-pattern rigidity chain into SNS collision-defect language.

Status: repair draft.  It reduces the weighted SNS bottleneck to a combined pattern/defect rigidity statement.

---

## C7.1. Phase-aware weighted repair state

Work in `ARBITRARY` phase.  The current ordering may contain endpoint collisions.  The global defect measure is

```text
D_SNS^*(R)=(P_col(R),L_col^*(R),boundary_rank(R)).
```

A weighted repair state is a displayed relation

```text
X A B C Y
```

with

```text
a+2b+c=0,
```

where

```text
a=sum(A),
b=sum(B),
c=sum(C).
```

It is genuine if the phase-aware easy reductions of C6.1 do not apply.

The local weighted measure is

```text
M_W^SNS=(D_SNS^*, |B|, M_local).
```

The global collision-defect profile `D_SNS^*` dominates the local weighted measure.

---

## C7.2. Defect-preserving weighted self-return

A weighted cut-swap begins with a proper cut

```text
B=P R,
P,R nonempty,
```

and applies

```text
A P R C -> A R P C.
```

A phase-aware weighted self-return is a finite state path

```text
Omega_0 -> Omega_1 -> ... -> Omega_N
```

with

```text
Omega_0.C = WEIGHTED_REPAIR,
Omega_N.C = WEIGHTED_REPAIR.
```

It is non-descending if:

```text
D_SNS^*(Omega_N) >= D_SNS^*(Omega_0)
```

and, when the global defect is equal,

```text
|B_N| >= |B_0|.
```

A minimal non-descending weighted self-return is chosen lexicographically by:

```text
return path length,
number of endpoint-pattern changes,
number of changed collision-profile coordinates,
local weighted measure.
```

---

## C7.3. Phase-aware pattern-rigidity

Pattern data for the weighted middle block `B` consists of:

```text
middle support;
outer blocks A,C;
internal endpoint set E_B;
boundary endpoints;
endpoint labels / interval representations;
collision-profile contribution of the weighted window.
```

## Definition C7.1: phase-aware pattern-rigid return

A weighted self-return is phase-aware pattern-rigid if it preserves:

```text
1. outer blocks A,C;
2. middle support B;
3. internal endpoint set E_B;
4. boundary endpoints;
5. endpoint labels up to identical interval representation;
6. the contribution of the window to D_SNS^*.
```

The last condition is new relative to A90--A94.  It prevents a return from being algebraically pattern-rigid while secretly improving or worsening the collision-defect profile.

---

## C7.4. Non-pattern changes

If a weighted return is not phase-aware pattern-rigid, then at least one of the following changes:

```text
1. middle support;
2. outer blocks;
3. internal endpoint set;
4. boundary endpoints;
5. endpoint labels;
6. collision-profile contribution.
```

The first five are the A90--A94 pattern diagnostics.  The sixth is the SNS-specific addition.

---

## Lemma C7.2: collision-profile change is defect descent or rejected self-return

If a weighted self-return changes the window contribution to `D_SNS^*`, then either:

```text
1. D_SNS^* strictly decreases, giving defect descent;
2. D_SNS^* increases, so the path is not non-descending-minimal;
3. D_SNS^* is equal globally but the changed window contribution is exactly compensated elsewhere, producing a collision-transfer branch.
```

The collision-transfer branch is an external/bridge repair state routed by phase-aware F6/F8.

### Proof sketch

The collision profile is a global count by span and first-location tie-breaker.  A local weighted return can change only collisions involving endpoints in or adjacent to the active window, unless an external endpoint participates.  If the profile improves, this is descent.  If it worsens, the path is not a minimal non-descending repair path.  If a local improvement is compensated by an external worsening, the compensation requires equality between a moved window endpoint and an external endpoint, which is an external collision/bridge relation. ∎

### Status

Needs hardening.  This is the main SNS-specific bookkeeping point in C7.

---

## C7.5. First changed endpoint in SNS mode

Assume the weighted return preserves global defect profile and middle support but changes internal endpoint set:

```text
E_B(Omega_N) != E_B(Omega_0).
```

Let

```text
s_* = min{s : E_B(Omega_s) != E_B(Omega_0)}.
```

At the transition `s_*`, a moved endpoint value changes.

In endpoint-avoidance mode, A91 classified the first change as collision, forbidden hit, recurrence, smaller weighted middle, or progress.  In SNS mode, forbidden-hit recurrence is absent.

---

## Lemma C7.3: first changed endpoint in SNS mode gives collision-profile descent or repair obstruction

At the first internal endpoint-pattern change of a minimal non-descending weighted SNS self-return, one of the following occurs:

```text
1. a moved endpoint collision occurs, routed by C4/C5;
2. an external moved endpoint collision occurs, routed by C4/F6/F8;
3. the weighted middle length decreases;
4. D_SNS^* decreases;
5. the change is unobstructed and later undone, contradicting minimal return length;
6. the return becomes pattern-rigid.
```

### Proof sketch

The first endpoint change occurs at one state-machine transition.  If the changed endpoint collides, C4 classifies the collision.  If it changes the collision profile favorably, this is defect descent.  If it changes the weighted middle, weighted induction applies.  If it is unobstructed and later undone, remove the change/undo segment to get a shorter self-return.  If it is never undone, the final return is not a self-return with preserved pattern data. ∎

### Status

This is the SNS analogue of A91--A94.  The remove-change/undo argument must be made purely in terms of state equality and `D_SNS^*` equality.

---

## C7.6. Support, boundary, and label changes

The A90 diagnostics remain algebraically valid, but terminal interpretation changes.

## Lemma C7.4: non-endpoint-set pattern changes route to phase-aware repair

If a weighted SNS self-return changes middle support, outer blocks, boundary endpoints, or endpoint labels, then it produces one of:

```text
1. local zero/equal/signed repair C5;
2. pair-difference repair C5;
3. transported-prefix/easy weighted reduction C6;
4. external/bridge repair C5/F6/F8;
5. smaller weighted middle;
6. D_SNS^* descent.
```

### Proof sketch

Subtract the two displayed weighted equations or compare the old and new interval representations.  The doubled middle terms either cancel, leaving non-weighted zero/equal data, or expose transported-prefix boundary terms.  In ARBITRARY phase, zero outputs are repair states measured by `D_SNS^*`.  If the changed support crosses outside the old weighted window, it is an external/bridge branch. ∎

---

## C7.7. Phase-aware weak cut-rigidity theorem

## Theorem C7.5: phase-aware weak cut-rigidity reduces to pattern-rigidity or exit

Assume:

```text
1. C7.2 collision-profile change lemma;
2. C7.3 first changed endpoint lemma;
3. C7.4 non-endpoint pattern-change routing;
4. C6 fixed cut-swap collision classification;
5. phase-aware C5 local/external/bridge repair.
```

Then a phase-aware weak cut-rigid weighted repair state either:

```text
1. is phase-aware pattern-rigid;
2. decreases D_SNS^*;
3. routes to phase-aware non-weighted repair;
4. returns to smaller weighted middle;
5. reaches collision-free SNS success;
6. contradicts minimal non-descending self-return.
```

### Proof

Let a minimal non-descending weighted self-return be given.  If it is not phase-aware pattern-rigid, some pattern component changes.  Collision-profile changes are Lemma C7.2.  Internal endpoint-set changes are Lemma C7.3.  Support, boundary, outer-block, and label changes are Lemma C7.4.  Thus every non-pattern return exits or descends.  The only remaining case is phase-aware pattern-rigidity. ∎

---

## C7.8. Phase-aware pattern-rigid impossibility

C6 already recorded that algebraic pattern-rigid weighted self-return cannot persist as a genuine weighted repair state.

## Lemma C7.6: phase-aware pattern-rigid weighted return exits genuine weighted repair

For odd `p`, a phase-aware pattern-rigid weighted self-return either:

```text
1. produces a zero defect in B;
2. forces E_B=F_p and hence b=0;
3. exits to phase-aware local repair;
4. contradicts genuine weighted repair status.
```

### Proof

Pattern-rigidity gives the same internal translation invariance:

```text
E_B-T_k=E_B.
```

If `T_k=0`, then the cut prefix is a zero defect.  If `T_k!=0`, translation invariance over the prime additive group forces `E_B=F_p`.  Then the middle block fills the field endpoints, and the weighted equation reduces to `2b=0`; for odd `p`, `b=0`.  In ARBITRARY phase, `b=0` is a zero defect, not a terminal contradiction, but it exits genuine weighted repair by C6.1. ∎

---

## C7.9. Phase-aware weighted closure, conditional

## Theorem C7.7: phase-aware weighted repair closure, conditional

Assume Lemmas C7.2--C7.4 are hardened.  Then every phase-aware weighted repair state either:

```text
1. exits to phase-aware non-weighted repair;
2. decreases D_SNS^*;
3. returns to a smaller weighted middle under fixed D_SNS^*;
4. reaches collision-free success;
5. exits pattern-rigid persistence by zero defect;
6. terminates by induction on |B| inside the fixed defect profile.
```

### Proof

Use C6 fixed cut-swap classification.  If a cut exits or descends, done.  If all cuts are phase-aware weakly cut-rigid, Theorem C7.5 reduces to pattern-rigidity or exit.  Pattern-rigid persistence exits by Lemma C7.6.  Smaller weighted middle terminates by induction on `|B|`. ∎

---

## C7.10. What C7 resolves

Resolved at architecture level:

```text
1. weak cut-rigidity has been translated into SNS phase-aware language;
2. collision-profile preservation is now part of pattern-rigidity;
3. forbidden recurrence is not used;
4. pattern-rigid impossibility still exits weighted repair via zero defect.
```

Remaining hardening:

```text
1. C7.2 collision-profile change compensation lemma;
2. C7.3 first changed endpoint in SNS mode;
3. C7.4 support/boundary/label diagnostics in phase-aware form;
4. final integration into a strong nonzero-sum proof.
```

---

## C7.11. Recommended next file

The next file should integrate C1--C7 into a single conditional strong nonzero-sum theorem and list the remaining hardening lemmas explicitly:

```text
docs/final/F00_SNS_C8_conditional_strong_nonzero_sum_assembly.md
```

Goal:

```text
State exactly what remains before claiming an unconditional proof.
```

---

## C7.12. Status

```text
Status: phase-aware weak cut-rigidity draft.
Risk: ORANGE/RED.
Current remaining gap: harden C7.2--C7.4 and assemble SNS theorem conditionally.
```
