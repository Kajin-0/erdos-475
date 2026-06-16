# Current Analytic Status Override

Last updated: 2026-06-04

Purpose:

```text
This file reconciles recent status drift across analytic documents.
If this file conflicts with older GREEN/completed language in handoff/checkpoint files,
use this file as the current conservative status until those older files are patched.
```

Claim boundary:

```text
No unconditional proof of Erdős 475 is claimed.
No unconditional proof of the SNS route is claimed.
No unconditional proof of endpoint avoidance is claimed.
```

---

## 0. Current operating mode

Primary working mode:

```text
Use ChatGPT + GitHub connector + public web/PDF extraction as the main agent environment.
Do not assume VPS access.
Do not instruct future agents to use the VPS except for genuinely necessary empirical runs or local script execution that cannot be done through GitHub/web tools.
```

Permitted from this environment:

```text
1. read and edit repository files through GitHub;
2. inspect public papers through web/PDF access;
3. add scripts, schemas, audit docs, and proof-workflow infrastructure;
4. commit conservative documentation and code hardening changes.
```

Avoid by default:

```text
1. asking the user to run scripts on the VPS;
2. assuming a local checkout is available;
3. making proof claims that depend on scripts that have not been run;
4. treating helper scripts as executed evidence merely because they were added to the repo.
```

Use local/VPS script execution only when:

```text
1. empirical data must be generated or regenerated;
2. a source bundle must be downloaded/extracted and cannot be accessed by web/PDF tools;
3. CI-style validation requires actual script execution;
4. the user explicitly makes the VPS available for that task.
```

---

## 1. Current primary route

The currently preferred high-level route is the phase-aware strong nonzero-sum repair program:

```text
arbitrary-ordering collision-defect minimization
  -> strong nonzero-sum ordering for sigma(S) != 0
  -> Erdős 475 by append-one-atom
  -> endpoint avoidance later as a strengthening through F12.
```

This is the route described in:

```text
docs/final/F00_SNS_C14_global_termination_status.md
docs/final/F00_SNS_C18_post_C7_status_and_red_items.md
```

The older F3--F12 endpoint-avoidance architecture remains useful infrastructure, but it should not be treated as the lead proof path unless explicitly revived.

---

## 2. Regression notes

Recent documentation contained several overstrong status statements. They should be interpreted conservatively.

### RGN-1. W-to-NW exit table row count

The W-to-NW exit table has:

```text
22 enumerated rows: E1--E22.
```

Older summaries that say:

```text
21 rows, 19 GREEN, 2 YELLOW
```

are stale.

Current conservative table:

```text
docs/analytic_weighted_to_nonweighted_exit_decrease_table.md
```

### RGN-2. W-to-NW table not final proof closure

The W-to-NW table is useful and substantially reduces risk, but it does not by itself close F11 or F9.

Current status:

```text
W-to-NW exits: enumerated and locally classified.
Final proof still needs lexicographic edge verification:
  enclosing_span nonincrease;
  gap_length nonincrease;
  then support/type/depth decrease;
  routed F6/F7/F8 exits consumed by final edge table.
```

Do not claim:

```text
Rule III is fully discharged,
all W-to-NW exits are already certified,
F11 is closed.
```

unless the final global edge table is complete.

### RGN-3. Insertion cut-cover GREEN language

Some handoff text marks insertion cut-cover as GREEN/all components closed.

Treat this as provisional unless the exact theorem statement, proof files, and empirical files are independently checked.

Conservative status:

```text
Insertion route: promising and apparently advanced, but must be audited against exact files.
Do not use it as a solved proof route without verifying the final statement and proof dependencies.
```

### RGN-4. Handoff main-route drift

Older sections of:

```text
docs/ANALYTIC_PROGRESS_HANDOFF.md
```

still emphasize the old endpoint/F9/F11 route. Newer SNS files pivot to the SNS route.

Current interpretation:

```text
SNS route is primary.
Endpoint/F9/F11 route is supporting infrastructure and historical context.
```

---

## 3. Current best roadmap

Use:

```text
docs/final/F00_SNS_C18_post_C7_status_and_red_items.md
```

as the current roadmap.

It lists remaining proof gaps as:

```text
R1. Formal finite-state neutral-excursion lemma.
R2. Explicit collision-profile decomposition.
R3. q-through-Z useful insertion theorem.
R4. Endpoint/sign tables.
R5. External/bridge finite-budget audit.
R6. Weighted cut-swap finite-budget audit.
R7. Boundary-rank consistency audit.
R8. Final global edge table.
```

Current shortest path:

```text
1. Prove finite-state neutral-excursion lemma.
2. Prove collision-profile decomposition.
3. Finish q-through-Z useful insertion theorem.
4. Build endpoint/sign appendix tables.
5. Audit external/bridge finite budgets.
6. Audit weighted cut-swap finite budgets.
7. Audit boundary-rank consistency.
8. Produce final global edge table.
9. Rewrite C8 as compact SNS theorem proof.
```

---

## 4. Current status labels

```text
Finite witness verification: GREEN for declared artifacts, subject to availability.
Endpoint/F3--F12 architecture: YELLOW/ORANGE, supporting route.
F9/F11 W-to-NW table: YELLOW/ORANGE, reconciled but not final closure.
SNS C14--C18 architecture: ORANGE, primary route.
SNS finite-state neutral-excursion lemma: RED/ORANGE.
SNS endpoint/sign/budget tables: ORANGE.
Analytic residue bridge: RED.
Insertion cut-cover route: provisional; audit before treating as GREEN.
```

---

## 5. Next file to create

Recommended next file:

```text
docs/final/F00_SNS_C19_finite_state_neutral_excursion.md
```

Goal:

```text
Formalize the minimal self-return / neutral-excursion lemma used by C15 and C16.
```

Minimum contents:

```text
1. define phase-aware state equivalence;
2. define neutral segment;
3. prove removable neutral segment lemma;
4. identify exceptions that produce routed obstruction;
5. state how the lemma consumes C15/C16 self-return loops.
```

---

## 6. Maintenance instruction

When older files are patched, remove or downgrade conflicting GREEN/completed language in:

```text
docs/ANALYTIC_PROGRESS_HANDOFF.md
docs/analytic_weighted_to_nonweighted_exit_decrease_table.md
any F00_SNS summary that overstates completion.
```

Until then, this file is the conservative status source.
