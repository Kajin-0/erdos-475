# Analytic final proof extraction plan A100

This note continues from A99.

A1--A99 developed the proof program, dependency graph, weighted/non-weighted obstruction routing, state-machine model, and hardening notes.  A100 marks the transition from adding machinery to extracting a compact final proof.

The goal is now:

```text
convert the A-notes into a short final proof sequence F1--F13,
with every final lemma backed by hardened notes,
and every remaining risk explicitly marked.
```

No new obstruction class is introduced in A100.

---

## 1. Current proof-program status

The five major hardening obligations from A93 have architectural hardening notes:

```text
U1 strict progress lemma                 -> A94
U2 external collision classification     -> A95
U3 bounded-blocker recurrence measure    -> A96 + A99
U4 cut-swap displayed collision table    -> A97
U5 bridge/gap measure inequalities       -> A98
```

The theorem-level chain is already separated:

```text
endpoint avoidance -> strong nonzero-sum -> Erdős 475
```

by A85.

The exceptional case `p=2` is handled directly in A86.

Thus the remaining work is extraction and audit, not new branch discovery.

---

## 2. Final proof lemma sequence

Use the following final-proof lemma numbering.

```text
F1. Minimal counterexample and first forbidden-hit setup.
F2. Adjacent blocker lemma.
F3. Obstruction state machine and transition classes.
F4. Zero-composite, equal-interval, and pair-difference descent.
F5. Separated-equal and midpoint routing.
F6. External collision theorem.
F7. Recurrence routing theorem.
F8. Bridge/gap descent theorem.
F9. Non-weighted termination theorem.
F10. Weighted normal form and cut-swap theorem.
F11. Weighted cut-selection and termination theorem.
F12. Endpoint avoidance theorem.
F13. Endpoint avoidance implies Erdős 475, with exceptional cases.
```

This is the compact public-proof skeleton.

---

## 3. Final lemma dependency map

| Final lemma | Backing A-notes | Readiness | Remaining work |
|---|---|---:|---|
| F1 | A4, A5, A84 | YELLOW | state minimality hypotheses cleanly |
| F2 | A5, A96 | YELLOW | exact A5 blocker equation and endpoint cases |
| F3 | A72, A92, A93 | YELLOW | compress state tuple and transition list |
| F4 | A20--A35, A73, A78 | ORANGE | sign/endpoint audit for pair-difference cases |
| F5 | A36--A55, A75, A77 | ORANGE | D2 and midpoint endpoint audit |
| F6 | A62, A95 | YELLOW | convert A95 classifications into final theorem format |
| F7 | A64--A71, A96, A99 | ORANGE | long-blocker case split and span convention audit |
| F8 | A74--A77, A98 | YELLOW | rewrite as single bridge/gap theorem |
| F9 | A72, A78, A94--A99 | ORANGE | final measure proof edge-by-edge |
| F10 | A56--A62, A97 | ORANGE | weighted normal-form exhaustiveness |
| F11 | A79--A83, A89--A94, A97 | RED | weak-to-pattern rigidity chain must be written cleanly |
| F12 | A84 | YELLOW | replace conditional language with dependency-resolved proof |
| F13 | A85, A86 | GREEN | nearly extraction-ready |

Readiness labels:

```text
GREEN  nearly final;
YELLOW needs polishing/checking;
ORANGE needs proof hardening;
RED    highest-risk extraction target.
```

---

## 4. Highest-risk final lemmas

The highest-risk final lemmas are:

```text
F7. Recurrence routing theorem.
F9. Non-weighted termination theorem.
F10. Weighted normal form and cut-swap theorem.
F11. Weighted cut-selection and termination theorem.
```

The most important single proof chain is:

```text
weak cut-rigid weighted self-return
  -> pattern-rigid or routed descent          (A90--A94)
  -> strong exact internal cyclic self-return (A89)
  -> impossible                               (A89)
```

This must be written with no informal phrases such as:

```text
invisible return;
progress;
routes to;
should;
expected.
```

unless each is tied to a formal definition and measure decrease.

---

## 5. Manuscript order

Use this order in the final manuscript.

### Section 1. Definitions

Include:

```text
finite field notation;
subset S subset F_p^*;
partial sums;
Graham-valid ordering;
endpoint avoidance;
forbidden value f;
active interval/window;
span/support conventions.
```

### Section 2. Minimal counterexample machinery

Include F1--F2.

### Section 3. Obstruction state machine

Include F3 and the transition table.

### Section 4. Non-weighted local reductions

Include F4--F8.

### Section 5. Non-weighted termination

Include F9.

### Section 6. Weighted obstruction

Include F10--F11.

### Section 7. Endpoint avoidance

Include F12.

### Section 8. Erdős 475

Include F13.

### Appendix A. Exhaustive tables

Put long collision tables here:

```text
separated-equal D/E tables;
weighted cut-swap table;
recurrence source tables;
external collision table.
```

### Appendix B. Optional computation

Include only certified finite-verification output if regenerated.

---

## 6. Extraction rules

When extracting the final proof:

```text
1. Do not cite proof-program notes as if they are final lemmas.
2. Replace every “routes to” phrase with a named final lemma and measure effect.
3. Replace every “proof sketch” with explicit endpoint algebra.
4. Do not include advisory notes unless marked as heuristic.
5. Keep A59-style insufficiency notes out of the main proof unless logically needed.
6. State all nonempty/possibly empty block assumptions at the start of each lemma.
7. State characteristic assumptions whenever dividing by 2.
8. Use augmented support containment for recurrence boundedness.
9. Keep computational verification separate from analytic proof.
```

---

## 7. Shortest path to a public proof draft

The shortest path is:

```text
Step 1. Extract F13 from A85/A86.                GREEN
Step 2. Extract F6 from A95.                     YELLOW
Step 3. Extract F8 from A98.                     YELLOW
Step 4. Extract F2/F7 from A5/A96/A99/A64--A71.  ORANGE
Step 5. Extract F10 from A56/A97.                ORANGE
Step 6. Extract F11 from A79--A83/A89--A94.      RED
Step 7. Extract F9 from A72/A78 + F4--F8.        ORANGE
Step 8. Extract F12 from A84.                    YELLOW
Step 9. Merge all into manuscript skeleton.      FINAL DRAFT
```

Do not start with the full manuscript.  Start with the red/orange bottlenecks.

---

## 8. Immediate next hardening target

The next useful document after A100 should not be A101 with new theory.  It should begin extraction.

Recommended next file:

```text
docs/final/F11_weighted_cut_selection_extraction.md
```

Reason:

```text
F11 is the highest-risk final lemma.
If F11 fails, the proof is not complete regardless of the rest of the extraction.
```

Minimum content for that extraction:

```text
1. exact statement of weighted cut-selection;
2. atom-middle base case from A80--A81;
3. proper-middle cut-swap from A79/A97;
4. weak cut-rigidity reduction from A90--A94;
5. pattern-rigid impossibility from A89;
6. induction on |B|;
7. explicit statement of all exits to A78/F9.
```

---

## 9. Optional repository organization

Suggested structure:

```text
docs/final/
  F01_minimal_setup.md
  F02_adjacent_blocker.md
  F03_state_machine.md
  F04_nonweighted_local_descent.md
  F05_separated_midpoint.md
  F06_external_collision.md
  F07_recurrence_routing.md
  F08_bridge_gap.md
  F09_nonweighted_termination.md
  F10_weighted_normal_form_cut_swap.md
  F11_weighted_cut_selection.md
  F12_endpoint_avoidance.md
  F13_erdos475.md
  manuscript_outline.md
```

This avoids mixing exploratory A-notes with final proof lemmas.

---

## 10. Current status after A100

The proof program has reached extraction mode.

Current status:

```text
Architecture: assembled.
Major hardening notes: present.
Theorem dependency: clean.
p=2 exceptional case: handled.
Remaining risk: final extraction and sign/endpoint audit.
```

Do not claim a complete proof yet.

The next step is to extract and harden F11.
