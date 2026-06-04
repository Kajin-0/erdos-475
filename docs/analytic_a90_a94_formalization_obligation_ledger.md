# A90-A94 formalization obligation ledger

## Purpose

This ledger extracts the exact proof obligations needed to formalize the persistent cut-rigidity branch in F11. The persistent cut-rigidity branch is the last unresolved exit type from the F11 proper-middle cut-swap (Lemma F11.3, outcome 6): when every proper cut of B produces a weighted return that is not terminal, not a routed non-weighted exit, and not a smaller-middle return, the core is weakly cut-rigid. A90-A94 are the A-note program that reduces weak cut-rigidity to pattern-rigidity (impossible by A89/F11.7) or routed descent. Formalizing this reduction is required to close the F9/F11 mutual-induction interface.

## Claim boundary

This document does not prove A90-A94, does not close F11, and does not prove Erdős 475. It records which statements exist, which are missing, and what gap types remain. No obligation listed here is marked PROVED unless the corresponding proof is explicitly present in the docs read this session.

## Parent obstruction context

The F9/F11 mutual-induction interface (defined in `docs/analytic_f9_f11_mutual_induction_convention.md`) requires that every exit from a weighted branch W(m) back to non-weighted machinery satisfies one of:

1. SUCCESS;
2. CONTRADICTION / COLLAPSE;
3. W(m') with m' < m;
4. NW1 with M_NW*(NW1) < M_NW*(NW0), where NW0 is the non-weighted parent state that entered W(m);
5. NW1 with a formal no-reentry certificate excluding W(j), j >= m, at equal-or-larger M_NW\*.

The key difficulty is that the W-to-NW exit decrease table (`docs/analytic_weighted_to_nonweighted_exit_decrease_table.md`) compares NW1 against the weighted window Wwin, not against NW0. The mutual-induction interface requires comparison against NW0. A90-A94 must supply the missing comparison for the persistent cut-rigidity branch — the case where no proper cut produces a terminal, routed, or descending weighted return.

## Required F9/F11 return certificate

For the persistent cut-rigidity branch, the F9/F11 return certificate must prove that for a weakly cut-rigid weighted core entered from NW0, the eventual exit satisfies one of:

- SUCCESS / CONTRADICTION / COLLAPSE (terminal);
- W(m') with m' < m (smaller middle);
- NW1 with M_NW*(NW1) < M_NW*(NW0) (strict measure decrease relative to entering parent);
- NW1 with formal no-reentry certificate excluding W(j), j >= m.

A90-A94 collectively claim that weak cut-rigidity reduces to pattern-rigidity (impossible by A89/F11.7) or routed descent. If routed descent produces NW1, the decrease must be measured against NW0, not merely against the weighted window.

## A90-A94 extraction table

| ID  | Statement location                                                                                            | Short statement                                                                                                                                                                                                                                                       | Inputs                                                                                                        | Output / conclusion                                                                         | Depends on                                                                                                      | Needed for F9/F11 interface                                                                                                         | Current status     | Gap type                                                                                         | Notes                                                                                                                                                                                                                                                                            |
| --- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A90 | `docs/final/F11_weighted_cut_selection_extraction.md` §F11.0 (dependency list) and §F11.7 (Lemma F11.6 proof) | Weak cut-rigid to pattern-rigid diagnostic: if a weighted self-return is weakly cut-rigid, then either it is pattern-rigid or it produces a routed/descending exit.                                                                                                   | Weakly cut-rigid weighted core with                                                                           | B                                                                                           | >=2 entered from NW0.                                                                                           | Either pattern-rigid (→ A89/F11.7 for impossibility) or routed/descending (→ A91, A92, A94).                                        | A91, A92, A94, A89 | Establishes the dichotomous reduction that is the core of Lemma F11.6.                           | ASSERTED                                                                                                                                                                                                                                                                         | case_split_gap                                          | The diagnostic is stated as a claim in Lemma F11.6 but no separate A90 formal lemma exists in the final docs. The proof sketch in F11.7 appeals to A90 as an A-note, not as an extracted lemma.                                                                                                                                                 |
| A91 | `docs/final/F11_weighted_cut_selection_extraction.md` §F11.7 (Lemma F11.6 proof)                              | First-changed-endpoint lemma: along a finite self-return path of a weakly cut-rigid core, the first position where an internal endpoint of B changes creates a routed obstruction, smaller weighted middle, recurrence, external collision, or unobstructed progress. | Weakly cut-rigid weighted core; finite return path from A92; first index where internal endpoint set changes. | The changed endpoint produces a routed non-weighted obstruction or smaller weighted return. | A92 (finite return-path model)                                                                                  | Provides the routed descent branch of the A90 dichotomous reduction.                                                                | ASSERTED           | definition_gap                                                                                   | A91 is described in prose within the Lemma F11.6 proof sketch. No separate statement of A91 as a lemma with explicit inputs, outputs, and proof exists in the final docs. "First-changed-endpoint" is not formally defined (what constitutes a change, how the path is ordered). |
| A92 | `docs/final/F11_weighted_cut_selection_extraction.md` §F11.0, §F11.7, §F11.11                                 | Finite return-path formalization: every weakly cut-rigid weighted self-return can be modeled as a finite sequence of intermediate states, each corresponding to a cut of B, with bounded length.                                                                      | Weakly cut-rigid weighted core with                                                                           | B                                                                                           | >=2.                                                                                                            | The self-return has a finite path model of length bounded by a function of                                                          | B                  | and p.                                                                                           | None (foundational)                                                                                                                                                                                                                                                              | Provides the finite-path framework used by A91 and A94. | ASSERTED                                                                                                                                                                                                                                                                                                                                        | definition_gap | A92 is listed as a dependency in F11.0 but no formal model is extracted. The "finite return-path model" is mentioned in the Lemma F11.6 hypothesis and in F11.11 R3, but no explicit definition, bound, or construction exists in the final docs. |
| A93 | `docs/final/F11_weighted_cut_selection_extraction.md` §F11.0                                                  | State-machine coverage: the finite return-path model from A92 is covered by the F3 obstruction state machine classes.                                                                                                                                                 | Finite return path from A92; F3 state machine classification.                                                 | Every intermediate state in the return path maps to a known F3 obstruction class.           | A92, F3                                                                                                         | Ensures the return path does not introduce new obstruction species.                                                                 | ASSERTED           | dependency_gap                                                                                   | A93 is listed only as a dependency in F11.0. No extracted statement, proof sketch, or even a claim exists in the final docs about what this lemma asserts or proves. Its status is purely as a named A-note.                                                                     |
| A94 | `docs/final/F11_weighted_cut_selection_extraction.md` §F11.7 (Lemma F11.6 proof), §F11.11 R3                  | Strict progress lemma: in a minimal non-descending self-return of a weakly cut-rigid core, unobstructed first changes cannot occur.                                                                                                                                   | Minimal (under                                                                                                | B                                                                                           | and M_NW\*) non-descending self-return; finite return-path model (A92); first-changed-endpoint detection (A91). | The first changed endpoint produces a routed obstruction or descent, not unobstructed progress (which would contradict minimality). | A91, A92           | Rules out the "unobstructed progress" branch of A91, forcing routed descent or pattern-rigidity. | ASSERTED                                                                                                                                                                                                                                                                         | decrease_gap                                            | A94 is cited in F11.7 to rule out unobstructed first changes. It is also listed in F11.11 R3 as needing "final formal minimal-path language." No extracted lemma exists. The word "progress" is ambiguous: it is not clear whether "unobstructed progress" means a strict M_NW\* decrease relative to NW0, a terminal state, or something else. |

## Minimal-path objects

The following definitions are used by A90-A94 but are not extracted in the final docs read this session. Their status is recorded below.

| Object                       | Used by                                      | Current status | Gap type       | Notes                                                                                                                                                                                           |
| ---------------------------- | -------------------------------------------- | -------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Weak cut-rigid weighted core | A90, A91, A92, A94, F11.6                    | PARTIAL        | definition_gap | Definition F11.5 exists: "for every proper cut B=P R, the cut-swap return has doubled middle length at least                                                                                    | B   | and no routed exit has terminated or satisfied the mutual-induction decrease condition." However, "doubled middle" and "routed exit" are not formally defined. |
| Finite return-path model     | A92, A91, A94                                | MISSING        | definition_gap | Referenced as an assumption in Lemma F11.6 and as a dependency in F11.11 R3. No explicit definition, construction, or bound exists in the final docs.                                           |
| First changed endpoint       | A91, A94                                     | MISSING        | definition_gap | Used in the Lemma F11.6 proof sketch but not defined. It is unclear whether "first" refers to position along the B ordering, index in the return path, or some other ordering.                  |
| Self-return path minimality  | A94                                          | MISSING        | definition_gap | A94 assumes a "minimal non-descending self-return" but no definition of what minimal means (minimum                                                                                             | B   | ? minimum M_NW\*? minimum path length?) is extracted.                                                                                                          |
| No-reentry certificate       | F9/F11 interface                             | MISSING        | no_reentry_gap | The mutual-induction interface permits a no-reentry certificate as alternative to M_NW\* decrease. No definition or formal certificate structure exists anywhere in the docs read this session. |
| Parent-support annotation    | F11 atom-middle exit, F11 proper-middle exit | MISSING        | decrease_gap   | F11.11 R2 says W-to-NW exits need "parent-support intervals and final decrease/no-reentry certificates." No parent-support annotation formalism exists.                                         |

## Dependency graph

```
A92 (finite return-path model)
  |
  v
A91 (first-changed-endpoint lemma)
  |
  v
A90 (weak-to-pattern-rigid diagnostic)  ──→  A89 (pattern-rigid impossible)
  |
  v
A93 (state-machine coverage)
  |
  v
A94 (strict progress lemma)
  |
  v
F11.6 (weak cut-rigid return is pattern-rigid or routed)
  |
  v
F11.1 (weighted core controlled-exit theorem)
  |
  v
F9/F11 mutual-induction interface (decrease relative to NW0 or no-reentry certificate)
```

An arrow A → B means "A is required by B."

## Required lemmas to prove next

1. **A92 finite return-path model** — Most foundational: define what a finite return-path is for a weakly cut-rigid core, construct it from the sequence of proper cuts, and prove its length is bounded. Without A92, A91 and A94 have no formal object to work on.

2. **A91 first-changed-endpoint lemma** — Once A92 exists, define what "first changed endpoint" means along the return path and prove that the change produces a routed exit, a smaller weighted return, or progress. This is the engine of the A90 reduction.

3. **A94 strict progress lemma** — Define what "unobstructed progress" means (likely a strict M_NW\* decrease relative to NW0 or a terminal state) and prove that in a minimal counterexample, the first changed endpoint from A91 cannot produce unobstructed progress.

## Findings

### What is already proved

- **A89 / F11.7**: Pattern-rigid self-return is impossible (strong exact internal cyclic self-return argument). This is the only PROVED component of the A90-A94 chain.
- **F11.5 (Definition)**: Weak cut-rigidity is defined, though the definition partially depends on informal terms.
- **F11.3 (Lemma)**: Fixed cut-swap exits are classified; persistent cut-rigidity is the only unclosed exit type.
- **F11.4 (Lemma)**: Side-contained weighted returns descend in |B|.
- **F11.8 (Lemma)**: Weighted descent terminates by well-foundedness of positive integers.

### What is only asserted

- **A90**: The dichotomous reduction (weak → pattern-rigid or routed) is ASSERTED in Lemma F11.6. The proof sketch appeals to A90-A94 as A-notes. No extracted formal lemma exists.
- **A91**: First-changed-endpoint behavior is described in prose within the F11.7 proof. No separate lemma exists.
- **A92**: Finite return-path model is listed as a dependency and assumed in Lemma F11.6. No definition, construction, or bound exists.
- **A93**: State-machine coverage is listed as a dependency in F11.0. No statement or proof exists.
- **A94**: Strict progress lemma is cited in the F11.7 proof and listed in F11.11 R3. No formal lemma exists.

### What exact missing statement blocks the F9/F11 interface

The F9/F11 mutual-induction interface requires that every W(m) → NW1 exit satisfies M_NW*(NW1) < M_NW*(NW0) or carries a no-reentry certificate. The persistent cut-rigidity branch in F11 is the only major exit type without this certification. To close it, the following chain must be formalized:

1. A92: construct a finite return-path model for a weakly cut-rigid core (MISSING)
2. A91: along this path, the first changed endpoint produces a routed/descending/terminal outcome (ASSERTED)
3. A94: in a minimal self-return, the outcome is routed descent, not progress — and the descent is a strict M_NW\* decrease relative to NW0 (ASSERTED, decrease_gap)
4. A90: therefore weak cut-rigidity yields either pattern-rigidity (impossible) or routed descent satisfying the mutual-induction interface (ASSERTED)

The critical decrease_gap is: even if A91-A94 are formalized, they must prove that the resulting NW1 has M_NW*(NW1) < M_NW*(NW0), not merely that it is "routed" to some non-weighted class. The W-to-NW exit table currently compares against Wwin, not NW0. Parent-support annotations (F11.11 R2) are needed to bridge this gap.

### Whether A90-A94 currently provide a valid NW0-relative decrease certificate

No. A90-A94 are A-note summaries only. None of A90, A91, A92, A93, or A94 exists as an extracted lemma in the final docs. The proof of Lemma F11.6 (which depends on them) is a prose sketch that appeals to unpublished A-note material. The W-to-NW exit table, which does exist as an extracted document, compares against the weighted window Wwin and explicitly acknowledges that NW0 comparison is still needed.

## Required follow-up

One targeted next task: formalize A92 (finite return-path model) as a standalone definition + existence lemma, since it is the most foundational missing piece — A91 and A94 cannot be formalized without it.
