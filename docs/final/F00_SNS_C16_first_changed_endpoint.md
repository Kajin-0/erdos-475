# F00.SNS.C16 first changed endpoint in SNS mode

This file continues the strong nonzero-sum repair path.

C15 hardened the collision-profile compensation item C7.2.  The next remaining C7 item is:

```text
C7.3 first changed endpoint in SNS mode.
```

In the earlier endpoint-avoidance proof, first-changed-endpoint arguments allowed forbidden-hit recurrence.  In SNS mode there is no forbidden value `f`; every obstruction must be expressed as collision pullback, defect descent, external/bridge compensation, smaller weighted middle, or finite-state shortening.

Status: hardening draft.

---

## C16.1. Setup

Work in ARBITRARY phase.

Let

```text
Omega_0 -> Omega_1 -> ... -> Omega_N
```

be a minimal non-descending phase-aware weighted self-return with:

```text
Omega_0.C = WEIGHTED_REPAIR,
Omega_N.C = WEIGHTED_REPAIR.
```

Assume the path preserves global collision defect:

```text
D_SNS^*(Omega_N)=D_SNS^*(Omega_0),
```

and does not decrease weighted middle length:

```text
|B_N| >= |B_0|.
```

The path is minimal by:

```text
1. path length N;
2. number of endpoint-set changes;
3. number of collision-profile changes;
4. local weighted measure.
```

---

## C16.2. Internal endpoint set

For a weighted middle block `B`, let

```text
E_B(Omega)
```

be the set of internal endpoint values of `B`, measured relative to the basepoint before `B`.

A return preserves the internal endpoint set if:

```text
E_B(Omega_N)=E_B(Omega_0).
```

The first-changed-endpoint case assumes that at some intermediate state the internal endpoint set changes.

Define:

```text
s_* = min{s : E_B(Omega_s) != E_B(Omega_0)}.
```

The transition

```text
Omega_{s_*-1} -> Omega_{s_*}
```

is the first endpoint-changing transition.

---

## C16.3. First endpoint-changing transition types

By the phase-aware state machine, the first endpoint-changing transition is one of:

```text
T1 adjacent swap;
T2 block exchange;
T3 gap-after move;
T4 weighted cut-swap;
T5 cyclic cut;
T6 atom-insertion normalization;
T8 external collision pullback / local replacement;
T9 normal-form rewrite changing endpoint representation.
```

In SNS mode, there is no T7 forbidden-hit blocker recurrence.  Collision-producing transitions are handled by C4 collision pullback.

---

## Lemma C16.1: first endpoint change is witnessed by a moved endpoint

At the transition `s_*`, at least one internal endpoint of `B` changes value or representation because a moved atom/block crosses that endpoint.

### Proof

By definition, `E_B` changes at `s_*` and did not change before.  A normal-form rewrite may relabel interval representation, but a genuine endpoint-set change requires some endpoint value to be moved by the transition.  If no endpoint is moved, the endpoint set remains unchanged. ∎

---

## C16.4. Collision case

If the endpoint-changing transition creates a collision, C4 applies.

## Lemma C16.2: obstructed first endpoint change routes by collision pullback

If the first endpoint-changing transition is collision-producing, then it routes to one of:

```text
local zero/equal/signed repair C11;
external/bridge repair C12;
weighted lower-rank or smaller-middle repair C13;
collision-profile descent C15;
atom/subset contradiction.
```

### Proof

A collision-producing SNS transition has a moved-moved, moved-unchanged, or moved-external collision by C4.  Moved-moved and moved-unchanged collisions route to local rows verified in C11.  Moved-external collisions route to C12.  If the collision equation preserves genuine coefficient-2 structure, it routes to C13.  Collision-profile effects are handled by C15. ∎

---

## C16.5. Unobstructed first endpoint change

Suppose the first endpoint-changing transition is collision-free and does not decrease `D_SNS^*` or `|B|`.

Then the endpoint set has changed without immediate obstruction.

Since the full path is a self-return, either:

```text
1. the endpoint change persists to Omega_N;
2. the endpoint change is undone at a later first restoration time.
```

If it persists, the final state is not pattern-equivalent to the initial state and routes through support/boundary/label diagnostics C17.

If it is undone, the change/undo segment is a neutral excursion.

---

## Lemma C16.3: neutral change/undo excursion contradicts minimal path length

Assume an endpoint set changes at `s_*` and is first restored at

```text
r_* > s_*.
```

If every transition in the segment

```text
Omega_{s_*-1} -> ... -> Omega_{r_*}
```

is collision-free, preserves `D_SNS^*`, preserves `|B|`, and produces no local/external/weighted ranked exit, then the original self-return was not minimal.

### Proof sketch

The segment begins and ends with the same endpoint-set contribution, same global defect profile, and same weighted middle length.  If no transition in the segment produces a ranked exit, the segment is a finite neutral excursion.  Removing the excursion gives a shorter self-return with the same initial and final weighted repair data, contradicting minimality of path length. ∎

### Formalization needed

The final manuscript must define equivalence of states strongly enough that removing the segment preserves the validity of adjacent transitions.

---

## C16.6. Persistent first endpoint change

If the first endpoint change persists to the returned weighted state, then the self-return is not phase-aware pattern-rigid.

Persistent changes may affect:

```text
internal endpoint set;
endpoint labels;
boundary endpoints;
local collision-profile contribution;
weighted support representation.
```

These are routed to C17 support/boundary/label diagnostics.

## Lemma C16.4: persistent endpoint change exits pattern-rigid branch

A persistent first endpoint change either:

```text
1. changes collision profile, handled by C15;
2. changes support/boundary/labels, handled by C17;
3. creates local/external collision algebra, handled by C11/C12;
4. changes weighted middle length, handled by C13;
5. reaches collision-free success.
```

### Proof

If the endpoint change persists, then the final weighted repair state is not identical to the initial pattern.  The difference must appear in the collision profile, support, boundary, labels, or middle length.  These are exactly the phase-aware pattern components. ∎

---

## C16.7. First changed endpoint theorem

## Theorem C16.5: first changed endpoint in SNS mode

In a minimal non-descending phase-aware weighted self-return, the first internal endpoint-set change gives one of:

```text
1. local collision repair C11;
2. external/bridge repair C12;
3. weighted lower-rank or smaller-middle repair C13;
4. strict D_SNS^* descent C15;
5. neutral change/undo contradiction to minimality;
6. persistent non-pattern change routed to support/boundary/label diagnostics C17;
7. collision-free SNS success.
```

Therefore a minimal non-descending weighted self-return with no routed exit and no defect descent must preserve the internal endpoint set.

### Proof

Let `s_*` be the first endpoint-changing transition.  If the transition is collision-producing, Lemma C16.2 applies.  If it is collision-free and the change is later undone, Lemma C16.3 applies.  If it persists, Lemma C16.4 applies.  These alternatives exhaust the first endpoint-changing transition. ∎

---

## C16.8. Consequence for C7

C16 hardens C7.3 in the following form:

```text
First changed endpoint in SNS mode
  -> collision pullback, defect descent, weighted descent,
     neutral-excursion contradiction, or support/boundary/label diagnostic.
```

Forbidden recurrence is not used.

---

## C16.9. Remaining audit items

C16 leaves two formal tasks:

```text
R1. Define state equivalence for neutral-excursion removal.
R2. Prove the segment-removal operation preserves a valid self-return path.
```

The remaining C7 item is now:

```text
C7.4 support/boundary/label diagnostics.
```

---

## C16.10. Recommended next file

Next harden C7.4:

```text
docs/final/F00_SNS_C17_support_boundary_label_diagnostics.md
```

Goal:

```text
Show support, boundary, or label changes in weighted self-return produce local repair, external/bridge repair, defect descent, smaller middle, or transported-prefix/easy weighted reduction.
```

---

## C16.11. Status

```text
Status: C7.3 hardening draft.
Risk: ORANGE.
Remaining red item: C7.4 support/boundary/label diagnostics.
```
