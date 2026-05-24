# F00.SNS.C14 global termination status

This file consolidates the phase-aware strong nonzero-sum repair program after C9--C13.

The current objective is no longer endpoint avoidance first.  The non-circular route is:

```text
arbitrary-ordering collision-defect minimization
  -> strong nonzero-sum for sigma(S) != 0
  -> Erdős 475 by append-one-atom
  -> endpoint avoidance as a later strengthening via F12.
```

C14 states the current conditional global termination theorem and the remaining red items.

No unconditional proof is claimed here.

---

## C14.1. Inputs assembled so far

The phase-aware SNS repair program now has the following components.

```text
C1. Refined collision-defect vector and strongly clean insertion descent.
C2. q-through-zero-interval obstruction classification.
C3. Phase-aware state machine without assuming Graham-validity.
C4. SNS collision-pullback theorem without forbidden endpoints.
C5. Phase-aware local descent for F4/F5/F6/F8 outputs.
C6. Phase-aware weighted repair framework.
C7. Phase-aware weak cut-rigidity draft.
C8. Conditional strong nonzero-sum assembly.
C9. Global phase-aware measure.
C10. Finite rank tables.
C11. Local rank-descent verification.
C12. External/bridge rank-descent verification.
C13. Weighted rank-descent verification conditional on C7 hardening.
```

The main phase-aware measure is:

```text
M_phase(Omega)=(
  D_SNS^*(R),
  phase_rank,
  M_loc,
  M_w,
  transition_budget
).
```

where:

```text
D_SNS^*(R) = (P_col(R), L_col^*(R), boundary_rank(R));
M_loc      = local enclosing span/gap/support/depth/type data;
M_w        = (|B|, M_loc) for weighted repair states.
```

---

## C14.2. Conditional global termination theorem

## Theorem C14.1: conditional phase-aware SNS termination

Assume the following hardening items are valid:

```text
H1. C2 useful-insertion obstruction theorem is fully formal.
H2. C4 collision-pullback equations are checked line by line.
H3. C11 local rank-descent rows are completed with endpoint/sign tables.
H4. C12 external/bridge re-entry cases consume finite budget.
H5. C13 weighted rank-descent row is completed.
H6. C7.2 collision-profile compensation is hardened.
H7. C7.3 first changed endpoint in SNS mode is hardened.
H8. C7.4 support/boundary/label diagnostics are hardened.
H9. All finite rank and boundary-rank conventions are fixed.
```

Then no ARBITRARY-phase SNS repair path can be infinite.  Consequently, for every finite `S subset F_p^*` with `sigma(S) != 0`, a strong nonzero-sum ordering exists.

### Proof

Choose a `D_SNS^*`-minimal ordering of `S`.  If it has no endpoint collisions, it is already strong nonzero-sum.

Otherwise, choose the active shortest zero interval.  Since `sigma(S) != 0`, the active zero interval is not the whole ordering, so an adjacent outside atom exists.  Move the outside atom through useful interior positions.

A strongly clean insertion strictly decreases `D_SNS^*`, contradicting minimality.  If no useful insertion is strongly clean, C2 and C4 produce local, external, bridge, or weighted repair data.  C11 verifies the local non-weighted rows, C12 verifies external/bridge rows, and C13 verifies weighted rows conditional on C7.

Under H1--H9, every nonterminal transition strictly decreases `M_phase` or enters a finite-budget table whose exhaustion produces either descent, success, or a classified lower-rank branch.  Since `M_phase` is well-founded, an infinite repair path is impossible.

The only remaining alternatives are collision-free success or contradiction of the fixed assumptions `S subset F_p^*`, distinct atom support, or `sigma(S) != 0`.  Therefore a strong nonzero-sum ordering exists. ∎

---

## C14.3. Consequence for Erdős 475, conditional

If Theorem C14.1 is made unconditional by proving H1--H9, then Erdős 475 follows.

For `sigma(S) != 0`, strong nonzero-sum directly gives a Graham-valid ordering.

For `sigma(S)=0`, choose `x in S` and set:

```text
T=S\{x}.
```

Then:

```text
sigma(T)=-x != 0.
```

Order `T` strongly, then append `x`.  The final partial sum becomes zero, while the previous extended partial sums for `T` were pairwise distinct and nonzero.  Hence the appended ordering is Graham-valid for `S`.

---

## C14.4. Consequence for endpoint avoidance, conditional

Once Erdős 475 is established, Input G in F12 is resolved.

Then the F12 conditional endpoint-avoidance theorem becomes an unconditional strengthening:

```text
for every f != sigma(S),
there exists a Graham-valid ordering avoiding f.
```

Thus endpoint avoidance should be presented after Erdős 475, not before it.

---

## C14.5. Remaining red items

The proof is not complete until the following are hardened.

### R1. C2 useful-insertion obstruction theorem

Need a formal proof that if no useful insertion of adjacent `q` into active shortest zero interval `Z` is strongly clean, then a useful insertion produces a routed obstruction, not an unclassified profile-neutral failure.

### R2. C4 collision-pullback equations

Need a complete table for moved-moved, moved-unchanged, and moved-external collisions in SNS mode.

### R3. C11 endpoint/sign appendix

Need explicit sign and endpoint tables for:

```text
SIGNED_INTERVAL;
PAIR_DIFFERENCE;
SEPARATED_EQUAL direct exchange;
gap-after table;
MIDPOINT_ADJACENT cases.
```

### R4. C12 external/bridge finite-budget proof

Need to prove external/bridge re-entry cannot loop at fixed `M_phase`.

### R5. C13 atom-middle endpoint-trap table

Need a complete sign table for atom-middle weighted repair.

### R6. C7.2 collision-profile compensation

Need a rigorous proof that local collision-profile changes in a weighted self-return either decrease `D_SNS^*`, disqualify the return, or create an external/bridge compensation branch.

### R7. C7.3 first changed endpoint in SNS mode

Need a formal minimal-path proof without forbidden recurrence.

### R8. C7.4 support/boundary/label diagnostics

Need line-by-line subtraction/comparison of weighted equations under support, boundary, or label changes.

### R9. Final rank consistency audit

Need to verify all outputs in C11--C13 map to the C10 rank table and never to `UNCLASSIFIED` or `BOUNDARY_UNCLASSIFIED`.

---

## C14.6. Current status classification

```text
Architecture: strong.
Input G circularity: replaced by SNS repair program.
Global measure: proposed.
Local non-weighted rank rows: mostly verified.
External/bridge rows: conditionally verified.
Weighted row: conditionally verified.
Critical open area: C7 weak cut-rigidity in SNS mode.
Proof status: not complete.
```

The bottleneck is now sharply localized:

```text
C7.2--C7.4 + endpoint/sign tables + finite-budget audit.
```

---

## C14.7. Recommended next file

The next file should attack the highest-risk C7 item first:

```text
docs/final/F00_SNS_C15_collision_profile_compensation.md
```

Goal:

```text
Harden C7.2: local collision-profile change in a weighted self-return either gives defect descent, invalidates non-descending return, or creates an external/bridge compensation branch.
```

---

## C14.8. Status

```text
Status: global termination status draft.
Risk: ORANGE/RED.
Main remaining proof bottleneck: C7.2 collision-profile compensation.
```
