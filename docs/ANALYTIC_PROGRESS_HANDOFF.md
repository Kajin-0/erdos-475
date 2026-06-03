# Analytic Progress Handoff

Last audited: 2026-06-03

This is the single high-level context document for analytic proof progress in this repository.

Purpose:

```text
Give a new external agent enough context to resume work without chat history.
Record what worked, what failed, what was corrected, what remains open, and which next steps are highest leverage.
Separate proof-grade evidence from proof-architecture progress.
```

Claim boundary:

```text
This document is not a proof of Erdős 475.
The finite certificate layer is currently the most independently checkable evidence.
The analytic layer has made real progress, but global termination and residue inclusion are not closed.
```

---

## 0. One-page executive dashboard

### Current status

```text
Finite witness verification:       GREEN for declared domains, subject to artifact availability.
Endpoint-local analytic routing:   YELLOW/GREEN; mostly class-routed.
F7 recurrence routing:             YELLOW; endpoint/sign errors corrected, final span table pending.
F8 bridge/gap routing:             YELLOW; measure embedding clarified, endpoint tables pending.
F9 non-weighted termination:        ORANGE; edge-by-edge global rank table pending.
F10/F11 weighted termination:       ORANGE; controlled-exit form exists, W-to-NW exit table pending.
Analytic residue bridge:            RED; no effective theorem-to-finite-domain extraction yet.
Insertion cut-cover route:          PROMISING; analyzer exists, local-search/minimization layer pending.
```

### Main conclusion

```text
Do not restart endpoint-local case analysis unless a concrete algebraic error is found.
The current analytic blocker is global termination, especially the F9/F11 mutual-induction interface.
The highest-value next analytic artifact is:

  docs/analytic_weighted_to_nonweighted_exit_decrease_table.md

The highest-value independent experimental/math artifact is:

  a fully blocked insertion search over many valid orderings C of A\{x}.
```

### Most important known corrections

```text
1. Bare Left(T)/Right(T) external labels were unsafe.
   Use template-aware K+A=0 and B+K=0.

2. H2 and A69 used full U incorrectly.
   Correct convention: U = U^- u_*; left-blocker pullbacks use U^-.

3. A97 signed-boundary weighted-return channel was overbroad.
   r + P_j - p - R_k = 0 simplifies to R_k^+ = P_j^+.
   An isolated A97.8 equation is non-weighted equal-tail machinery.

4. F9/F11 interface was circular if stated as “F9 handles F11 exits” and “F11 handles F9 exits.”
   It now requires controlled mutual induction.

5. A56 transported-prefix/tail cannot be a bare Boolean.
   It requires a containing-block certificate D=BT or D=TB with complement present.
```

---

## 1. Problem context

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

The repo has two proof components:

```text
1. finite-certificate verification for declared small/complement domains;
2. analytic proof architecture attempting to reduce all remaining cases to known theory or finite verification.
```

Current honest status:

```text
The finite layer proves declared finite instances only.
The analytic layer is not yet a complete theorem proof.
A full result still needs global termination plus an analytic residue bridge.
```

---

## 2. External mathematical context, verified 2026-06-03

External progress bounds the project and prevents overclaiming.

### Bedert--Kravitz, 2024

```text
Graham's rearrangement conjecture beyond the rectification barrier
https://arxiv.org/abs/2409.07403
```

Verified abstract-level claim:

```text
Prime-field conjecture proved for |A| ≤ exp((log p)^(1/4)), improving log p / log log p.
```

### Pham--Sauermann, 2026

```text
On Graham's rearrangement conjecture
https://arxiv.org/abs/2602.15797
```

Verified abstract-level claim:

```text
For any α in (0,1), the prime-field conjecture is proved for |S| ≤ p^(1-α)
when |S| is sufficiently large relative to α.
Combined with earlier results, this gives a complete resolution for all sufficiently large primes p.
```

Repo implication:

```text
The repo should not claim a first asymptotic solution.
The most valuable external-facing goals are:
  1. extract effective residue bounds; or
  2. produce an independent finite/local structural theorem.
```

### Costa--Della Fiore--Fontana--Vena, 2026

```text
Graham conjecture on small sets in abelian groups
https://arxiv.org/abs/2603.20961
```

Verified abstract-level claim:

```text
Sequenceability for generic abelian-group subsets with |A| ≤ 20.
Zero-sum subsets improved to |A| ≤ 22.
```

Repo implication:

```text
A natural exact small-set target is |A|=21 in prime fields,
or a related insertion-extension boundary theorem.
```

### Bedert--Bucić--Kravitz--Montgomery--Müyesser, 2025

```text
On Graham's rearrangement conjecture over F_2^n
https://arxiv.org/abs/2508.18254
```

Verified abstract-level claim:

```text
Large-set theorem for general groups and essentially complete large-set result over F_2^n.
```

Repo implication:

```text
Large-set asymptotic routes are technically strong and crowded.
Small obstruction/certificate routes are likely better near-term contributions.
```

---

## 3. Computational layer status

The finite-certificate layer is the most proof-grade part of the repo.

Declared verified frontier:

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

Known preservation rule:

```text
p=29 and p=31 are intended Tier 1 verified domains.
Do not regress docs to older claims that omit p=29/p=31 high-|B| shards.
```

What finite verification proves:

```text
The declared finite instances have valid witness orderings.
```

What it does not prove:

```text
The analytic residue lies inside those finite verified domains.
```

Remaining finite/computational actions:

```text
1. Synchronize README, VERIFIED_DOMAIN.md, THEOREM_DOMAIN_LEDGER.md, verified_domains.json, proof.tex.
2. Make strict CI verify all Tier 1A artifacts.
3. Add retrieval/regeneration instructions for Tier 1B artifacts.
4. Harden Python witness parsing to reject non-integer JSON values.
5. Build final residue audit script after effective external ranges are extracted.
```

---

## 4. Main analytic architecture

Core modules:

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

Global non-weighted measure:

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

Bridge subrank convention:

```text
bridge_depth_BG = (
  bridge_cycle_depth,
  bridge_length,
  internal_length,
  bridge_orientation_rank,
  bridge_endpoint_rank
).
```

Main global theorem obligation:

```text
Every nonterminal obstruction edge must either:
  1. strictly decrease M_NW^*;
  2. terminate;
  3. enter weighted-core machinery under controlled mutual induction;
  4. or return with a formal no-reentry certificate.
```

---

## 5. Deep analytic progress timeline

Dates are workflow/session dates.

### 2026-06-03: endpoint branch locally class-routed

Key files:

```text
docs/analytic_endpoint_branch_status_final.md
docs/analytic_endpoint_branch_f9_measure_audit.md
docs/analytic_global_class_graph_measure_checkpoint.md
```

What worked:

```text
Endpoint-local outputs are mapped to global classes.
No known endpoint-local branch remains unclassified.
```

Status:

```text
YELLOW/GREEN locally.
Not a global proof.
```

Remaining blocker:

```text
Destination classes must terminate globally through F4--F11/F9.
```

---

### 2026-06-03: template-aware external collision correction

Unsafe old form:

```text
Left(T), Right(T)
```

Reason unsafe:

```text
It loses the proposed local permutation split and can misclassify external collisions.
```

Correct forms:

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

Status:

```text
GREEN for endpoint-specific embedding into F6.
YELLOW globally because F6 exits still depend on F4/F5/F7/F8/F10/F11/F9.
```

---

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
A69 pair-difference endpoint convention corrected.
Singleton-prefix atom endpoint cases routed.
Cyclic-cut midpoint characteristic p=3 behavior audited.
```

Real corrections:

```text
H2/A67:
  wrong: ... + U + v_1 = 0
  right: U = U^- u_* and ... + U^- + v_1 = 0

A69:
  same U^- / u_* endpoint convention issue in pair-difference recurrence.
```

Corrected H2 crossing cases:

```text
D1: L + P + q + U^- + v_1 = 0 -> L + q - u_* - V^+ = 0
D2: R + V^+ + u_* = 0
D3: V^+ + u_* = 0
```

Status:

```text
YELLOW.
Recurrence sources are class-routed.
F9 still must verify augmented span/measure decreases edge-by-edge.
```

---

### 2026-06-03: F8 bridge/gap measure hardening

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

Bridge-to-global embedding:

```text
M_BG.enclosing_span       -> M_NW^*.enclosing_span
M_BG.bridge_gap           -> M_NW^*.gap_length
M_BG.support_size         -> M_NW^*.support_size
M_BG.recurrence_depth     -> M_NW^*.recurrence_depth
M_BG.bridge-local subrank -> M_NW^*.bridge_depth
```

Status:

```text
YELLOW.
Measure notation ambiguity resolved.
Endpoint and direct-exchange tables still needed for final manuscript.
```

Remaining blocker:

```text
F8 rigid-return endpoint table.
F5 direct-exchange endpoint table.
F9 final edge-by-edge rank table.
```

---

### 2026-06-03: F9/F11 circularity found and controlled

Key file:

```text
docs/analytic_f9_f11_mutual_induction_convention.md
```

Problem:

```text
F9 says weighted exits terminate by F11.
F11 says non-weighted exits terminate by F9.
```

Required controlled output for:

```text
NW_0 -> W(m)
```

F11 may return only:

```text
SUCCESS;
CONTRADICTION/COLLAPSE;
W(m') with m' < m;
NW_1 with M_NW^*(NW_1) < M_NW^*(NW_0);
NW_1 with formal no-reentry certificate excluding W(j), j >= m.
```

Status:

```text
ORANGE.
Wording-level circularity is identified and controlled conceptually.
The W-to-NW exit table is still missing, so the theorem is not closed.
```

---

### 2026-06-03: weighted-core audits A81/A97/A56

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
A97 signed-boundary weighted-return channel simplified and patched.
A56 transported-prefix/tail exhaustiveness clarified by containing-block certificates.
F11 updated to controlled-exit form.
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
A genuine same-length weighted return requires persistent signed-boundary rigidity across cuts.
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

Status:

```text
ORANGE.
A81/A97/A56 local algebra is substantially improved.
Global weighted closure still depends on W-to-NW decrease/no-reentry and A90--A94 formalization.
```

Known stale follow-up:

```text
docs/final/F10_weighted_normal_form_cut_swap.md still contains older broad language about
transported-prefix exhaustiveness and signed-boundary return.
Patch F10 to cite A56/A97 audits and downgrade those risks.
```

---

### 2026-06-03: insertion cut-cover route audited

Key files:

```text
docs/INSERTION_CUT_COVER_PROGRAM.md
docs/INSERTION_BLOCK_ANALYZER_RUNBOOK.md
scripts/analyze_insertion_blocks.py
```

Core insertion obstruction:

```text
Given x in A and a Graham-valid ordering C of A\{x},
insert x into one of the cuts of C.
A minimal counterexample forces every insertion cut to be blocked.
```

Cut-cover mechanism:

```text
Endpoint obstruction: s_i + x = s_k for k <= i.
Crossing obstruction: s_j - s_k = -x, blocking every cut k <= i < j.
Cut-zero obstruction: cut 0 blocked if some nonempty partial sum of C equals 0.
```

What already exists:

```text
scripts/analyze_insertion_blocks.py computes Block(C,x), endpoint obstructions,
zero-partial cut-zero obstruction, crossing intervals, coverage multiplicities,
and minimal unblocked cuts.
```

Status:

```text
PROMISING / NOT YET RESULT-GRADE.
The diagnostic analyzer exists.
The missing experimental layer is local search over many valid orderings of A\{x}
to minimize the insertion obstruction measure M(C,x).
```

Recommended target:

```text
Classify fully blocked one-element insertion configurations.
Push insertion-extension boundary toward |A|=21 in prime fields.
```

---

## 6. What worked

```text
1. Finite witnesses are verified by checking final orderings, not trusting search traces.
2. Endpoint-local branches are now mostly class-routed.
3. External collisions now preserve local permutation/provenance data.
4. H2/A69 endpoint convention errors were found and corrected.
5. F7 recurrence endpoint/sign branches are much cleaner.
6. F8 bridge/gap local coordinates are embedded into the global measure.
7. Atom-middle |B|=1 weighted base case no longer looks like an independent weighted obstruction.
8. A97 isolated signed-boundary equations are non-weighted equal-tail relations.
9. A56 transported-prefix/tail now has a certificate model.
10. F9/F11 circularity is identified and has a required mutual-induction interface.
11. Insertion cut-cover route has a real diagnostic script and runbook.
```

---

## 7. What failed, was unsafe, or should not be repeated

### N1. Bare external labels

```text
Unsafe: Left(T), Right(T)
Safe:   K + A = 0, B + K = 0, with provenance.
```

### N2. Full-U endpoint pullbacks

```text
Unsafe: ... + U + v_1 = 0
Safe:   U = U^- u_* and ... + U^- + v_1 = 0
```

### N3. A97 signed-boundary as direct weighted return

```text
Unsafe: r + P_j - p - R_k = 0 -> weighted return
Safe:   r + P_j - p - R_k = 0 -> R_k^+ = P_j^+ non-weighted equal-tail
```

### N4. Unqualified F9/F11 delegation

```text
Unsafe: handled by F9 / handled by F11
Safe:   handled by mutual induction with explicit decrease or no-reentry condition
```

### N5. Bare transported-prefix Boolean

```text
Unsafe: --transported-prefix / --transported-tail with no provenance
Safe:   containing-block certificate D=BT or D=TB with complement present
```

### N6. Endless local routing notes without global closure

```text
Unsafe: more notes saying “routes to existing machinery” without measure-edge table
Safe:   class -> child class -> exact decreasing coordinate -> dependency
```

---

## 8. What remains to be tried

### R1. W-to-NW exit decrease/no-reentry table

Highest-value analytic task.

Expected file:

```text
docs/analytic_weighted_to_nonweighted_exit_decrease_table.md
```

Required columns:

```text
weighted exit type;
source F10/F11/A-note;
resulting NW class;
support relative to weighted entry window;
decreasing M_NW^* coordinate relative to NW_0;
can it re-enter W(j), j>=m?;
needed dependency.
```

### R2. Patch stale F10

```text
docs/final/F10_weighted_normal_form_cut_swap.md
```

needs to cite:

```text
docs/analytic_a56_transported_prefix_tail_exhaustiveness_audit.md
docs/analytic_a97_signed_boundary_weighted_return_audit.md
```

and replace older broad language about signed-boundary weighted returns.

### R3. A90--A94 minimal-path formalization

Need final proof that:

```text
weak cut-rigid same-middle return -> pattern-rigid or routed descent.
```

A89 proves only strong exact/pattern-rigid self-return impossible.

### R4. F9 edge-by-edge rank table

Need final table:

```text
class -> child class -> exact M_NW^* coordinate decrease -> dependency
```

Do not rely on prose such as:

```text
routes to existing machinery.
```

### R5. F8/F5 endpoint tables

Needed for final manuscript hardening:

```text
F8 rigid-return endpoint table.
F5 direct-exchange endpoint table.
```

### R6. Analytic residue bridge

Need exact extraction from external papers:

```text
published theorem ranges + verified finite frontier => residue_not_verified = 0
```

No such extraction exists yet.

### R7. Insertion obstruction search/minimization

The repo already has a direct analyzer. The missing step is search over many valid orderings:

```text
for each A, x:
  sample/enumerate valid orderings C of A\{x};
  compute Block(C,x);
  minimize M(C,x);
  record fully blocked examples or no-example evidence.
```

Target metric:

```text
M(C,x) = (
  |Block(C,x)|,
  total_blocking_multiplicity,
  crossing_interval_count,
  total_crossing_length,
  endpoint_obstruction_count,
  zero_partial_cut_zero_flag
).
```

---

## 9. Recommended next actions

### Immediate analytic action

```text
Create docs/analytic_weighted_to_nonweighted_exit_decrease_table.md.
```

Start with exits from:

```text
A56 easy reductions;
A81 atom-middle exits;
A97 direct cut-swap collisions;
A97 equal-prefix/equal-tail boundary relations;
F7 recurrence exits from cut-swap forbidden hits;
F6 external collision exits from weighted cut-swap.
```

### Immediate documentation action

```text
Patch F10 stale risk language.
Keep this handoff updated after every major analytic commit.
```

### Immediate experimental action

```text
Build local-search/minimization around scripts/analyze_insertion_blocks.py.
```

Output should include:

```text
minimum blocked cuts;
maximum blocked cuts;
fully blocked cases;
coverage multiplicity;
endpoint obstruction count;
crossing interval list;
zero-partial flag;
worst obstruction signatures.
```

---

## 10. Status labels

Use these labels consistently:

```text
GREEN  = independently checkable, finite, or terminal algebra closed.
YELLOW = class-routed but dependent on global termination.
ORANGE = plausible but needs edge-by-edge measure proof or mutual-induction table.
RED    = structural theorem blocker, possible circularity, or missing residue bridge.
```

Current labels:

```text
Finite witness verification:       GREEN, subject to artifact availability.
Endpoint local routing:            YELLOW/GREEN.
F7 recurrence class routing:        YELLOW.
F8 bridge/gap class routing:        YELLOW.
F9 global termination:              ORANGE.
F10 weighted local cut-swap:        ORANGE until F10 stale language is patched.
F11 weighted termination:           ORANGE.
F9/F11 W-to-NW exit table:          RED until created.
Analytic residue bridge:            RED.
Insertion cut-cover route:          PROMISING; analyzer exists, search layer pending.
```

---

## 11. File map

### Global checkpoints

```text
docs/ANALYTIC_PROGRESS_HANDOFF.md
docs/analytic_global_class_graph_measure_checkpoint.md
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

### Insertion cut-cover route

```text
docs/INSERTION_CUT_COVER_PROGRAM.md
docs/INSERTION_BLOCK_ANALYZER_RUNBOOK.md
scripts/analyze_insertion_blocks.py
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

After any major analytic commit, append or update a dated entry in Section 5 or Section 8.

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

Do not allow analytic context to live only in chat.
