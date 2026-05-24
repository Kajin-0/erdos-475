# F00.SNS.C18 post-C7 status and remaining red items

This file updates the strong nonzero-sum repair program after the C7 hardening drafts:

```text
C15. collision-profile compensation;
C16. first changed endpoint in SNS mode;
C17. support, boundary, and label diagnostics.
```

The purpose is to reclassify the remaining gaps and identify the shortest path to a complete SNS proof draft.

No unconditional proof is claimed here.

---

## C18.1. Current proof architecture

The current non-circular route is:

```text
arbitrary-ordering collision-defect minimization
  -> strong nonzero-sum for sigma(S) != 0
  -> Erdős 475 by append-one-atom
  -> endpoint avoidance using F12 after Graham-valid existence is known.
```

The main measure is:

```text
M_phase=(D_SNS^*, phase_rank, M_loc, M_w, transition_budget).
```

where:

```text
D_SNS^* = collision profile + active collision location + boundary rank;
M_loc   = local span/gap/support/depth/type data;
M_w     = weighted middle length plus local weighted data.
```

The proof starts in ARBITRARY phase.  In this phase, zero intervals are repair defects.  They are not contradictions.

---

## C18.2. C7 hardening status

The previous highest-risk area was C7: phase-aware weak cut-rigidity.

Draft hardening now exists for:

```text
C7.2 collision-profile compensation -> C15;
C7.3 first changed endpoint          -> C16;
C7.4 support/boundary/label changes  -> C17.
```

The status is now:

```text
C7 architecture: hardened at draft level;
C7 appendix algebra: not yet complete;
C7 formal finite-state minimality: not yet complete.
```

---

## C18.3. Remaining red items

The remaining proof gaps are now more concrete.

### R1. Formal finite-state neutral-excursion lemma

Used by C15 and C16.

Need to prove:

```text
If a finite self-return path contains a change/undo segment preserving
D_SNS^*, |B|, endpoint pattern, and local state data, then the segment can be removed
or replaced by a lower-ranked routed obstruction.
```

Risk: RED/ORANGE.

Reason: this is a structural minimality argument.  It must be stated precisely enough to avoid handwaving.

---

### R2. Explicit collision-profile decomposition

Used by C15.

Need to decompose collision profile changes into:

```text
local-local endpoint collisions;
local-external endpoint collisions;
external-external unchanged collisions.
```

Need to prove compensation implies a moved-external collision.

Risk: ORANGE.

---

### R3. q-through-Z useful insertion theorem

Used by C2.

Need a formal proof that if no useful insertion is strongly clean, then a useful insertion produces classified local/external/weighted obstruction.

Risk: ORANGE.

Key formulas already exist:

```text
E_k={T_0,...,T_k} union {q+T_k,...,q+T_m}.
```

Need final endpoint-span/location bookkeeping.

---

### R4. Endpoint/sign tables

Used by C11, C13, C17.

Need explicit tables for:

```text
signed interval;
pair-difference;
gap-after E-branches;
direct-exchange D-branches;
atom-middle weighted endpoint trap;
boundary endpoint representation changes.
```

Risk: ORANGE.

---

### R5. External/bridge finite-budget audit

Used by C12.

Need to prove EXTERNAL_COLLISION re-entry cannot loop at fixed `M_phase`.

Risk: ORANGE/YELLOW.

Likely handled by finite endpoint-pair budget plus bridge gap/span descent.

---

### R6. Weighted cut-swap finite-budget audit

Used by C13.

Need explicit count of:

```text
proper cuts B=P R;
displayed moved-family comparisons;
weighted-return channels;
side-contained middle returns;
pattern-rigid exits.
```

Risk: ORANGE/YELLOW.

---

### R7. Boundary-rank consistency audit

Used globally.

Need every boundary-degeneracy output to map to C10 boundary ranks and prove boundary rank decreases or finite budget is consumed.

Risk: YELLOW/ORANGE.

---

### R8. Final global edge table

Need one final table showing every transition source maps to:

```text
strict D_SNS^* descent;
strict M_loc descent;
strict |B| descent;
finite transition_budget decrease;
COLLISION_FREE success;
atom/subset contradiction.
```

Risk: ORANGE.

---

## C18.4. Reclassified proof risk

Before C15--C17, the main risk was broad:

```text
weak cut-rigidity in SNS mode.
```

After C15--C17, the risk is narrower:

```text
formal finite-state minimality + explicit endpoint/sign/budget tables.
```

This is progress.  The remaining tasks are still substantial, but they are less conceptual and more audit-driven.

---

## C18.5. Shortest path to a complete SNS proof draft

Recommended order:

```text
Step 1. Prove finite-state neutral-excursion lemma.        R1
Step 2. Prove collision-profile decomposition.             R2
Step 3. Finish q-through-Z useful insertion theorem.       R3
Step 4. Build endpoint/sign appendix tables.               R4
Step 5. Audit external/bridge finite budgets.              R5
Step 6. Audit weighted cut-swap finite budgets.            R6
Step 7. Audit boundary-rank consistency.                   R7
Step 8. Produce final global edge table.                   R8
Step 9. Rewrite C8 as a compact theorem proof.             final SNS draft
```

Do not attempt the final manuscript before R1--R4 are resolved.

---

## C18.6. Recommended next file

The next file should address R1 first:

```text
docs/final/F00_SNS_C19_finite_state_neutral_excursion.md
```

Goal:

```text
Formalize the minimal self-return path argument used in C15 and C16.
```

Minimum contents:

```text
1. define phase-aware state equivalence;
2. define neutral segment;
3. prove removable neutral segment lemma;
4. identify exceptions that produce routed obstruction;
5. connect to C15/C16.
```

---

## C18.7. Status

```text
Status: post-C7 status draft.
Risk: ORANGE.
Main remaining red item: finite-state neutral-excursion lemma.
```
