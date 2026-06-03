# Analytic Progress Handoff

Last updated: 2026-06-03

Purpose:

```text
This is the single high-level handoff document for analytic proof progress.
It is intended for a new external agent or reviewer who needs to regain context quickly.
It records what has been tried, what worked, what failed or was corrected, what remains open, and how the repo's analytic work relates to external progress on Graham/Erdős 475.
```

Claim boundary:

```text
This document is not a proof of Erdős 475.
It is a proof-engineering and mathematical-status handoff.
The finite certificate layer is currently the most independently checkable evidence.
The analytic layer has meaningful progress but remains incomplete at the global termination/residue-bridge level.
```

---

## 0. Problem context

The prime-field Graham rearrangement conjecture / Erdős 475 asks:

```text
For prime p and every subset A ⊂ F_p^*,
there exists an ordering a_1,...,a_t of A such that the nonempty partial sums

  a_1,
  a_1+a_2,
  ...,
  a_1+...+a_t

are pairwise distinct modulo p.
```

The repo has two broad proof components:

```text
1. finite-certificate verification for declared small/complement domains;
2. analytic proof architecture attempting to reduce all remaining cases to known theory or finite verification.
```

Current honest status:

```text
Finite evidence: strong for declared verified domains.
Analytic local routing: substantially improved.
Global analytic termination: not fully proved.
Analytic residue inclusion: not fully proved.
```

---

## 1. External mathematical context

External progress bounds the problem and should prevent the repo from overclaiming.

### Bedert--Kravitz, 2024

Paper:

```text
Graham's rearrangement conjecture beyond the rectification barrier
https://arxiv.org/abs/2409.07403
```

Claim from abstract:

```text
Prime-field conjecture proved for |A| ≤ exp((log p)^(1/4)), improving the previous log p / log log p bound.
```

### Pham--Sauermann, 2026

Paper:

```text
On Graham's rearrangement conjecture
https://arxiv.org/abs/2602.15797
```

Claim from abstract:

```text
For any α in (0,1), the conjecture is proved for |S| ≤ p^(1-α) once |S| is sufficiently large relative to α.
Combined with earlier results, this resolves the prime-field conjecture for all sufficiently large primes p.
```

Repo implication:

```text
The prime-field theorem may already be externally resolved asymptotically for all sufficiently large p.
The repo must therefore either:
  - extract effective finite residue ranges from the literature, or
  - produce an independent finite/local structural contribution.
```

### Costa--Della Fiore--Fontana--Vena, 2026

Paper:

```text
Graham conjecture on small sets in abelian groups
https://arxiv.org/abs/2603.20961
```

Claim from abstract:

```text
Sequenceability for subsets of generic abelian groups with |A| ≤ 20.
For zero-sum subsets, the bound improves to |A| ≤ 22.
```

Repo implication:

```text
A natural exact small-set target is |A|=21 in prime fields or related insertion-extension variants.
```

### Bedert--Bucić--Kravitz--Montgomery--Müyesser, 2025

Paper:

```text
On Graham's rearrangement conjecture over F_2^n
https://arxiv.org/abs/2508.18254
```

Relevant context from abstract:

```text
They prove a broad large-set theorem for general groups and an essentially complete result over F_2^n for sufficiently large sets.
```

Repo implication:

```text
Large-set asymptotic directions are crowded and technically strong.
A smaller certificate-friendly obstruction theorem may be the better near-term contribution.
```

---

## 2. Computational layer status

The finite-certificate layer remains the most externally credible part of the repo.

Current declared finite frontier:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

Important distinction:

```text
Tier 1A: committed / directly repo-checkable artifacts.
Tier 1B: verified local/external JSONL or summary digest, not necessarily fully committed due to size.
```

Known issue to preserve:

```text
p=29 and p=31 are intended to be Tier 1 verified domains.
Do not regress docs to older claims that omit p=29/p=31 high-|B| shards.
```

Finite verification proves only:

```text
The declared finite instances have valid witness orderings.
```

It does not prove:

```text
The analytic residue lies inside those finite verified domains.
```

Remaining finite/computational actions:

```text
1. Keep README, VERIFIED_DOMAIN.md, THEOREM_DOMAIN_LEDGER.md, verified_domains.json, proof.tex synchronized.
2. Make strict CI verify all Tier 1A artifacts.
3. Add retrieval/regeneration instructions for Tier 1B artifacts.
4. Harden Python witness parsing to reject non-integer JSON values.
5. Create final residue audit script once analytic theorem ranges are known.
```

---

## 3. Main analytic architecture

The analytic route uses an obstruction-state machine.

Core global modules:

```text
F3   obstruction state machine
F4   local zero/equal/pair descent
F5   separated-equal and midpoint routing
F6   external collision theorem
F7   recurrence routing theorem
F8   bridge/gap descent theorem
F9   non-weighted termination theorem
F10  weighted normal form and fixed cut-swap theorem
F11  weighted cut-selection and termination theorem
F12  final endpoint-avoidance / assembly target
```

Global measure:

```text
M_NW^* = (
  enclosing_span,
  gap_length,
  support_size,
  recurrence_depth,
  pair_depth,
  separated_depth,
  bridge_depth,
  type_rank,
  boundary_rank,
  h_excess
).
```

Current analytic bottleneck:

```text
Prove every nonterminal edge in the global obstruction graph strictly decreases M_NW^*,
or exits to weighted-core machinery that terminates by a non-circular F9/F11 induction.
```

---

## 4. High-level timeline of recent analytic progress

Dates are session/workflow dates, not publication dates.

### 2026-06-03: endpoint-branch local closure work

Created/updated endpoint branch notes:

```text
docs/analytic_endpoint_branch_status_final.md
docs/analytic_endpoint_branch_f9_measure_audit.md
docs/analytic_global_class_graph_measure_checkpoint.md
```

What worked:

```text
Endpoint-local outputs are now mapped to global classes.
No known endpoint-local branch remains unclassified.
```

What this did not prove:

```text
Global termination.
F10/F11 weighted-core termination.
Analytic residue inclusion.
```

### 2026-06-03: external-collision notation correction

Problem found:

```text
Bare labels Left(T), Right(T) were unsafe.
External collisions must retain the proposed local permutation split.
```

Correct normal forms:

```text
left external collision:  K + A = 0
right external collision: B + K = 0
```

Key files:

```text
docs/analytic_template_external_collision_embedding_f6.md
docs/analytic_fixed_ordering_formalism_lemma.md
docs/analytic_f6_edge_compatibility_audit.md
```

What worked:

```text
Template-aware external outputs now embed into F6.
```

### 2026-06-03: F7 recurrence hardening

Key files:

```text
docs/analytic_f7_h1_h2_sign_audit.md
docs/analytic_long_blocker_uncrossing_h2_a67.md
docs/analytic_f7_pair_difference_endpoint_audit.md
docs/analytic_pair_difference_recurrence_a69.md
docs/analytic_f7_singleton_endpoint_audit.md
docs/analytic_f7_cyclic_cut_midpoint_characteristic_audit.md
docs/final/F07_recurrence_routing_theorem.md
```

What worked:

```text
H1 signs audited and internally consistent.
H2 endpoint convention corrected.
Pair-difference recurrence endpoint convention corrected.
Singleton-prefix atom endpoint cases explicitly routed.
Cyclic-cut midpoint characteristic p=3 behavior audited.
```

Real corrections found:

```text
H2: use U = U^- u_* and left-blocker pullbacks use U^-, not full U.
A69 pair-difference recurrence has the same endpoint-convention issue.
```

Corrected H2 cases:

```text
D1: L + P + q + U^- + v_1 = 0 -> L + q - u_* - V^+ = 0
D2: R + V^+ + u_* = 0
D3: V^+ + u_* = 0
```

What remains:

```text
F7 is class-routed, but final F9 must still verify augmented span/measure decreases edge-by-edge.
```

### 2026-06-03: F8 bridge/gap hardening

Key files:

```text
docs/analytic_f8_bridge_gap_hardening_checkpoint.md
docs/analytic_mbg_to_mnw_subrank_convention.md
docs/final/F08_bridge_gap_descent_theorem.md
docs/final/F09_nonweighted_termination_theorem.md
```

What worked:

```text
F8 class routing mostly hardened.
M_BG bridge_length/internal_length ambiguity removed.
```

Bridge local subrank:

```text
bridge_depth_BG = (
  bridge_cycle_depth,
  bridge_length,
  internal_length,
  bridge_orientation_rank,
  bridge_endpoint_rank
).
```

Embedding:

```text
M_BG.bridge_length/internal_length -> M_NW^*.bridge_depth
```

What remains:

```text
F8 rigid-return endpoint table.
F5 direct-exchange endpoint table.
F9 final edge-by-edge rank table.
```

### 2026-06-03: F9/F11 circularity identified

Key file:

```text
docs/analytic_f9_f11_mutual_induction_convention.md
```

Problem found:

```text
F9 delegates weighted exits to F11.
F11 delegates non-weighted exits back to F9.
```

This is circular unless written as mutual induction.

Required weighted output rule:

```text
NW_0 -> W(m)
```

F11 may only return:

```text
SUCCESS;
CONTRADICTION/COLLAPSE;
W(m') with m' < m;
NW_1 with M_NW^*(NW_1) < M_NW^*(NW_0);
NW_1 with a formal no-reentry certificate excluding W(j), j >= m.
```

What remains:

```text
Build W-to-NW exit decrease/no-reentry table.
Patch final proof language everywhere to avoid unqualified “handled by F9/F11.”
```

### 2026-06-03: F10/F11 weighted-core audits

Key files:

```text
docs/analytic_f10_f11_weighted_core_closure_checkpoint.md
docs/analytic_weighted_atom_middle_a81_sign_audit.md
docs/analytic_endpoint_rigid_atom_middle_a81.md
docs/analytic_a97_signed_boundary_weighted_return_audit.md
docs/analytic_weighted_cut_swap_table_hardening_a97.md
docs/analytic_a56_transported_prefix_tail_exhaustiveness_audit.md
docs/final/F11_weighted_cut_selection_extraction.md
```

What worked:

```text
A81 atom-middle sign table audited and patched.
A97 signed-boundary weighted-return channel simplified.
A56 transported-prefix/tail exhaustiveness clarified by containing-block certificates.
```

A81 four-row table:

```text
(+,+):  a = q-alpha,     c = gamma-q    -> alpha-gamma=2q
(+,-):  a = q-alpha,     c = q-gamma    -> alpha+gamma=4q
(-,+):  a = alpha-q,     c = gamma-q    -> alpha+gamma=0
(-,-):  a = alpha-q,     c = q-gamma    -> alpha-gamma=-2q
```

A97 correction:

```text
r + P_j - p - R_k = 0
P = P_j P_j^+
R = R_k R_k^+
=> R_k^+ = P_j^+
```

Interpretation:

```text
An isolated A97.8 signed-boundary equation is non-weighted equal-tail/equal-interval machinery.
A genuine weighted same-length return requires persistent signed-boundary rigidity across cuts.
```

A56 certificate condition:

```text
A + 2B + C = 0
```

is transported-prefix/tail removable only if there is a containing-block certificate:

```text
D = B A,
D = B C,
D = A B,
or D = C B
```

where `D` is a known transported/containing block from the local move.

What remains:

```text
W-to-NW exit decrease/no-reentry table.
A90--A94 minimal-path formalization.
Final F9/F11 mutual-induction implementation.
```

---

## 5. What worked

### W1. Finite certificates

```text
Witness verification architecture is credible.
Verifier checks final orderings, not search traces.
Python and Rust independent checking are the right proof-engineering approach.
```

### W2. Local endpoint routing

```text
Endpoint-local branches are now largely classified into global obstruction classes.
```

### W3. Algebraic endpoint corrections

```text
H2 and A69 full-U formulas were unsafe; corrected to U^- / u_*.
A97 signed-boundary channel simplified to equal-tail R_k^+=P_j^+.
```

### W4. Measure interface clarification

```text
M_BG now embeds into M_NW^* through bridge_depth_BG.
```

### W5. Weighted base-case simplification

```text
Atom-middle |B|=1 does not remain an independent weighted-core obstruction after sign expansion.
```

### W6. Circularity detection

```text
F9/F11 dependency is now explicitly recognized as requiring mutual induction.
```

---

## 6. What did not work / unsafe routes

### N1. Bare external labels

Unsafe:

```text
Left(T), Right(T)
```

Reason:

```text
These lose the proposed local permutation split and can misclassify external collisions.
```

Replacement:

```text
K + A = 0,
B + K = 0.
```

### N2. Full-U endpoint convention in H2/A69

Unsafe:

```text
... + U + v_1 = 0
```

when A5 is applied before the last atom of `U`.

Replacement:

```text
U = U^- u_*,
... + U^- + v_1 = 0.
```

### N3. Treating A97 signed boundary as direct weighted return

Unsafe:

```text
r + P_j - p - R_k = 0 -> possible weighted return
```

Correct simplification:

```text
R_k^+ = P_j^+.
```

Thus isolated A97.8 is non-weighted.

### N4. Unqualified “handled by F9/F11”

Unsafe:

```text
weighted exits handled by F11;
non-weighted exits handled by F9.
```

Reason:

```text
Circular unless a mutual-induction decrease/no-reentry condition is stated.
```

### N5. Treating transported-prefix/tail as a bare Boolean

Unsafe:

```text
--transported-prefix
--transported-tail
```

without interval-provenance certificate.

Replacement:

```text
Containing-block certificate D = BT or D = TB with complement present in relation.
```

---

## 7. What remains to be tried

### R1. W-to-NW exit decrease/no-reentry table

Highest-value analytic task.

Need table:

```text
weighted exit type -> resulting NW class -> decreasing coordinate relative to NW_0 -> can it re-enter W(j), j>=m?
```

Required by:

```text
docs/analytic_f9_f11_mutual_induction_convention.md
```

### R2. A90--A94 minimal-path formalization

Need final proof that:

```text
weak cut-rigid same-middle return -> pattern-rigid or routed descent.
```

A89 only proves strong exact/pattern-rigid self-return impossible.

### R3. F9 edge-by-edge rank table

Need final table:

```text
class -> child class -> exact M_NW^* coordinate decrease -> dependency
```

Do not rely on prose such as:

```text
routes to existing machinery.
```

### R4. F8/F5 endpoint tables

Needed for final manuscript completeness:

```text
F8 rigid-return endpoint table.
F5 direct-exchange endpoint table.
```

### R5. Analytic residue bridge

Need exact theorem extraction from external literature:

```text
published asymptotic/large/small set results
+ finite verified domain
=> residue_not_verified = 0
```

This is still unresolved.

### R6. Insertion obstruction project

External audit recommends pivoting to a smaller, testable problem:

```text
Classify fully blocked one-element insertion configurations.
```

Problem:

```text
Given x in A and a Graham-valid ordering C of A\{x},
can every insertion cut for x be blocked?
```

Why useful:

```text
Small, testable, falsifiable, certificate-friendly.
Could yield a rigorous intermediate theorem even if full analytic closure remains hard.
```

Suggested boundary target:

```text
|A| = 21 in prime fields
```

because external small-set work reaches |A|<=20 in generic abelian groups and |A|<=22 for zero-sum subsets.

---

## 8. Recommended next actions

### Immediate analytic action

```text
Create W-to-NW exit decrease/no-reentry table.
```

Expected file:

```text
docs/analytic_weighted_to_nonweighted_exit_decrease_table.md
```

### Immediate computational/experimental action

```text
Implement or run fully blocked insertion search.
```

Expected outputs:

```text
minimum |Block(C,x)|;
maximum |Block(C,x)|;
full-cover examples or no-example certificates;
coverage multiplicity;
endpoint obstruction count;
crossing interval list;
zero-partial flag.
```

### Immediate documentation action

```text
Keep this handoff file updated after each major analytic checkpoint.
Use date-stamped entries.
Do not let analytic context live only in chat.
```

---

## 9. Suggested status labels

Use these labels consistently:

```text
GREEN  = independently checkable or terminal/finite algebra closed.
YELLOW = class-routed but dependent on global termination.
ORANGE = plausible but needs edge-by-edge measure proof.
RED    = structural theorem blocker or possible circularity.
```

Current labels:

```text
Finite witness verification: GREEN for declared Tier 1A/Tier 1B domains, subject to artifact availability.
Endpoint local routing: YELLOW/GREEN depending on branch.
F7 recurrence class routing: YELLOW.
F8 bridge/gap class routing: YELLOW.
F9 global termination: ORANGE.
F10/F11 weighted termination: ORANGE, formerly RED before mutual-induction convention.
F9/F11 W-to-NW exit table: RED until completed.
Analytic residue bridge: RED.
Insertion obstruction project: promising, not started or not yet integrated.
```

---

## 10. Single-page summary for a new agent

```text
Do not restart endpoint-local case analysis unless a concrete algebraic error is found.
Endpoint-local branches are now mostly class-routed.

The main analytic proof blocker is not local routing.
It is global termination, especially F9/F11 mutual induction.

The most important next analytic artifact is a W-to-NW exit decrease/no-reentry table.

The best near-term independent mathematical target may be the fully blocked insertion problem.

The finite certificate layer is the strongest proof-grade evidence, but it does not prove residue inclusion.

External results likely solve the prime-field conjecture for sufficiently large primes, so the repo should avoid overclaiming and either extract an effective residue or produce a smaller structural/certificate theorem.
```

---

## 11. File map

### Global checkpoints

```text
docs/analytic_global_class_graph_measure_checkpoint.md
docs/ANALYTIC_PROGRESS_HANDOFF.md
```

### Endpoint/F7/F8/F9

```text
docs/analytic_endpoint_branch_status_final.md
docs/analytic_endpoint_branch_f9_measure_audit.md
docs/analytic_f7_h1_h2_sign_audit.md
docs/analytic_f7_pair_difference_endpoint_audit.md
docs/analytic_f7_singleton_endpoint_audit.md
docs/analytic_f7_cyclic_cut_midpoint_characteristic_audit.md
docs/analytic_f8_bridge_gap_hardening_checkpoint.md
docs/analytic_mbg_to_mnw_subrank_convention.md
docs/final/F07_recurrence_routing_theorem.md
docs/final/F08_bridge_gap_descent_theorem.md
docs/final/F09_nonweighted_termination_theorem.md
```

### Weighted/F10/F11

```text
docs/analytic_f10_f11_weighted_core_closure_checkpoint.md
docs/analytic_f9_f11_mutual_induction_convention.md
docs/analytic_weighted_atom_middle_a81_sign_audit.md
docs/analytic_endpoint_rigid_atom_middle_a81.md
docs/analytic_a97_signed_boundary_weighted_return_audit.md
docs/analytic_weighted_cut_swap_table_hardening_a97.md
docs/analytic_a56_transported_prefix_tail_exhaustiveness_audit.md
docs/final/F10_weighted_normal_form_cut_swap.md
docs/final/F11_weighted_cut_selection_extraction.md
```

### Computational/finite layer

```text
certificates/verified_domains.json
certificates/witnesses_*.jsonl
scripts/run_all_verification.sh
scripts/verify_witnesses.py
rust_verifier/
MANIFEST.sha256
```

---

## 12. Maintenance rule

After any major analytic commit, append a dated note to this file under Section 4 or Section 7.

Minimum entry format:

```text
YYYY-MM-DD: short title
Files changed:
  - ...
What worked:
  - ...
What failed/was corrected:
  - ...
Remaining blocker:
  - ...
Next action:
  - ...
```
