# F00.SNS.C6 phase-aware weighted repair

This file continues the strong nonzero-sum repair path.

C5 isolated the remaining phase-aware bottleneck:

```text
C5.W phase-aware weighted repair theorem.
```

The issue is that F10/F11 were extracted for the endpoint-avoidance proof, where transformed moves had the trichotomy:

```text
success / collision / forbidden recurrence.
```

In the arbitrary-start strong nonzero-sum proof there is no forbidden endpoint `f`.  The corresponding dichotomy is:

```text
collision-free success / collision pullback.
```

C6 adapts the weighted normal-form and cut-selection branch to this collision-defect mode.

Status: repair draft.

---

## C6.1. Phase-aware weighted setup

Work in `ARBITRARY` phase.  The current ordering may contain endpoint collisions.  Therefore zero intervals are not terminal contradictions; they are collision defects measured by

```text
D_SNS^*(R)=(P_col(R),L_col^*(R),boundary_rank(R)).
```

A weighted repair state is an algebraic relation in a displayed window

```text
X A B C Y
```

with block sums

```text
a=sum(A),
b=sum(B),
c=sum(C),
```

satisfying

```text
a+2b+c=0.
```

The weighted relation is interpreted as a repair obstruction, not yet as a contradiction or endpoint-avoidance recurrence.

---

## C6.2. Phase-aware easy weighted reductions

The easy weighted reductions from F10 remain algebraically valid.

## Lemma C6.1: easy weighted reductions become phase-aware local repair states

If a weighted relation satisfies one of

```text
b=0,
a+b=0,
b+c=0,
a=c,
transported-prefix/tail rewrite applies,
```

then in `ARBITRARY` phase it routes to one of:

```text
ZERO_DEFECT,
TWO_PIECE_ZERO repair,
EQUAL_INTERVAL repair,
SIGNED_INTERVAL repair,
PAIR_DIFFERENCE repair,
TRANSPORTED_PREFIX repair,
BRIDGE_GAP repair.
```

These outputs are consumed by phase-aware C5 rather than treated as immediate contradictions.

### Proof

The algebra is the same as F10.  The only difference is terminal interpretation.  For example, `b=0` gives a zero interval in the displayed middle block.  In `COLLISION_FREE` phase this is contradiction; in `ARBITRARY` phase it is a zero defect measured by the collision profile.  The other easy reductions are ordinary zero/equal/signed/transported-prefix relations and are phase-aware repair states. ∎

---

## C6.3. Genuine phase-aware weighted core

A phase-aware weighted core is genuine if none of the easy reductions in Lemma C6.1 applies.

Use the weighted repair measure

```text
M_W^SNS=(|B|, D_SNS^*, M_local)
```

where `M_local` records the local span/gap/support ranks used by C5/F4--F8.

The leading weighted coordinate is still `|B|`, but it must be interpreted as a nested repair coordinate.  A decrease in `D_SNS^*` is globally decisive; a decrease in `|B|` only controls the weighted subroutine once the same global defect context is fixed.

---

## C6.4. Phase-aware fixed cut-swap

Assume

```text
|B|>=2,
B=P R,
P,R nonempty.
```

Use the same cut-swap as F10:

```text
A P R C -> A R P C.
```

In SNS mode, after the cut-swap exactly one of the following occurs:

```text
1. the transformed ordering is collision-free, giving SNS success;
2. the transformed ordering has only unchanged collisions, compared by D_SNS^*;
3. the transformed ordering creates a displayed collision;
4. the transformed ordering creates an external collision;
5. the displayed collision algebra returns to weighted form.
```

There is no forbidden-recurrence case.

---

## Lemma C6.2: phase-aware cut-swap collision table

For the cut-swap

```text
A P R C -> A R P C,
```

every new displayed collision routes to one of:

```text
ZERO_DEFECT repair,
TWO_PIECE_ZERO repair,
EQUAL_INTERVAL repair,
SIGNED_INTERVAL repair,
PAIR_DIFFERENCE repair,
TRANSPORTED_PREFIX repair,
smaller weighted repair,
weighted self-return candidate.
```

### Proof

Use the F10/F97 displayed endpoint families:

```text
A_i:   x+A_i,
R_k':  x+a+R_k,
P_j':  x+a+r+P_j,
C_l':  x+a+r+p+C_l.
```

Direct moved-family collisions give equations such as

```text
A_i^+ + R_k=0,
P+R_k^+ + C_l=0,
P_j+R_k^+=0,
A_i^+ + R+P_j=0,
P_j^+ + C_l=0.
```

In `ARBITRARY` phase these are zero/equal/signed repair states, not contradictions.  Signed old/new boundary comparisons may preserve a coefficient-2 pattern and therefore remain in weighted repair. ∎

---

## Lemma C6.3: phase-aware external collisions from cut-swap route through C4/C5

Any moved endpoint collision with an endpoint outside the displayed cut-swap table routes to phase-aware external repair C5/F6/F8.

### Proof

The cut-swap is a local sum-preserving move.  A moved endpoint colliding externally is exactly a C4 moved-external collision.  C5 reinterprets zero outputs as defects and bridge outputs as repair states. ∎

---

## C6.5. No forbidden recurrence in weighted SNS mode

Endpoint-avoidance weighted recurrence cases must be removed from the SNS weighted branch.

## Lemma C6.4: weighted SNS cut-swap has no forbidden-recurrence output

In strong nonzero-sum mode, a cut-swap output is either collision-free or collision-producing.  Therefore every non-success output is classified by collision pullback, not by forbidden recurrence.

### Proof

There is no distinguished forbidden value `f`.  The only failure mode for strong nonzero-sum is an endpoint collision. ∎

---

## C6.6. Weak cut-rigidity in SNS mode

F11 used weak cut-rigidity and pattern-rigidity to rule out non-descending weighted self-return.  In SNS mode, this must be reformulated.

A phase-aware weak cut-rigid weighted repair is a genuine weighted repair state such that every proper cut-swap either:

```text
1. creates only collision outputs that route back to weighted repair without decreasing D_SNS^*;
2. returns to a weighted repair state with middle length at least |B|;
3. does not produce collision-free success;
4. does not produce phase-aware local defect descent.
```

This is stronger than the old weak cut-rigidity because it must preserve the global collision-defect profile.

---

## Needed Lemma C6.5: phase-aware weak cut-rigidity reduces to pattern-rigidity or defect descent

A phase-aware weak cut-rigid weighted repair either:

```text
1. is pattern-rigid in the sense of A90--A94;
2. decreases D_SNS^*;
3. routes to phase-aware non-weighted repair C5;
4. returns to smaller weighted middle;
5. reaches collision-free success.
```

### Status

Open.  This is the central weighted adaptation gap.

The old F11/A90--A94 proof may still apply to the pattern data, but all uses of forbidden recurrence and zero-collapse must be translated into collision-profile descent or phase-aware repair.

---

## C6.7. Pattern-rigid impossibility remains mostly unchanged

The A89 pattern-rigid impossibility is algebraic and does not depend on forbidden endpoint recurrence.

## Lemma C6.6: pattern-rigid weighted self-return is still impossible in SNS mode

Assume `p` is odd.  A genuine weighted repair state cannot have a pattern-rigid self-return under an internal cut.

### Proof

Pattern-rigidity gives the same endpoint-set translation invariance as F11/A89:

```text
E_B-T_k=E_B.
```

If `T_k=0`, then there is a zero interval in `B`; in ARBITRARY phase this is a zero defect, so the branch exits weighted repair to phase-aware local repair.  If `T_k != 0`, translation invariance forces `E_B=F_p`.  Then `|B|=p-1`, leaving no outside atoms in the subset ordering.  The weighted relation reduces to `2b=0`, hence `b=0` for odd `p`, again a zero defect.  Thus pattern-rigid weighted self-return cannot persist as a genuine weighted repair state. ∎

### Important distinction

In endpoint-avoidance mode, `b=0` is contradiction.  In ARBITRARY SNS mode, it is a zero defect.  Either way, it exits the genuine weighted state.

---

## C6.8. Phase-aware weighted repair theorem, conditional

## Theorem C6.7: phase-aware weighted repair theorem, conditional form

Assume Needed Lemma C6.5.  In `ARBITRARY` phase, every weighted repair state either:

```text
1. reduces by an easy weighted reduction to phase-aware non-weighted repair;
2. performs a fixed cut-swap whose collisions route through C4/C5;
3. decreases D_SNS^*;
4. returns to a smaller weighted middle;
5. reaches collision-free SNS success;
6. exits pattern-rigid self-return by Lemma C6.6.
```

Therefore weighted repair cannot create a new obstruction species outside the phase-aware state machine.

### Proof

If the weighted relation is nongenuine, Lemma C6.1 applies.  If it is genuine and `|B|=1`, the atom-middle argument from F11 must be interpreted phase-aware: all zero/equal/pair outputs go to C5 repair states, and no forbidden recurrence is used.  If `|B|>=2`, choose a proper cut.  Lemmas C6.2--C6.4 classify the cut-swap outputs.  If all cuts are weakly cut-rigid, Needed Lemma C6.5 reduces to pattern-rigidity, defect descent, non-weighted repair, smaller middle, or success.  Pattern-rigid persistence is impossible by Lemma C6.6. ∎

---

## C6.9. What remains after C6

Resolved:

```text
1. fixed weighted cut-swap algebra is reusable in SNS mode;
2. forbidden recurrence is removed from the weighted cut-swap outcome list;
3. zero-collapse outputs are reinterpreted as zero defects;
4. pattern-rigid impossibility remains available as weighted-state exit.
```

Remaining:

```text
1. Needed Lemma C6.5 phase-aware weak cut-rigidity reduction;
2. phase-aware atom-middle weighted case;
3. proof that weighted exits decrease D_SNS^* or |B| under fixed global defect context;
4. integration into a final SNS termination theorem.
```

---

## C6.10. Recommended next file

The next file should attack Needed Lemma C6.5:

```text
docs/final/F00_SNS_C7_phase_aware_weak_cut_rigidity.md
```

Goal:

```text
Translate A90--A94 weak-to-pattern rigidity into ARBITRARY/SNS phase language.
```

Minimum contents:

```text
1. define phase-aware pattern-rigidity;
2. define defect-preserving weighted self-return;
3. first-changed-endpoint argument without forbidden recurrence;
4. show endpoint-pattern changes produce collision-profile descent or phase-aware repair;
5. conclude pattern-rigid or exit.
```

---

## C6.11. Status

```text
Status: phase-aware weighted repair draft.
Risk: RED/ORANGE.
Main remaining gap: phase-aware weak cut-rigidity reduction C6.5.
```
