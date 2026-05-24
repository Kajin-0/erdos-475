# Analytic local lemma audit checklist A87

This note continues from A86.

A84 assembled the conditional endpoint-avoidance theorem.  A85 audited the theorem-level implication chain.  A86 handled finite and exceptional cases conservatively.  A87 records the local lemma audit checklist needed before any public claim of a complete proof.

The repository now contains a long sequence of analytic notes A1--A86.  Many are rigorous local derivations, but several later notes deliberately use language such as:

```text
proof sketch;
partial;
modulo;
routes to;
not proved here;
status;
expected;
should.
```

Those notes must be hardened before the proof is advertised as complete.

---

## 1. Audit objective

The objective is to classify every lemma/proposition/theorem in A1--A86 as one of:

```text
PROVED        self-contained proof complete;
ROUTING       algebraic transformation correct, but termination delegated;
CONDITIONAL   valid assuming named earlier lemmas;
SKETCH        proof sketch only, must be expanded;
GAP           explicitly not proved;
COMPUTATIONAL advisory or certified computation required;
OBSOLETE      replaced by later sharper note.
```

Only `PROVED` and explicitly chained `CONDITIONAL` statements should appear in the final public proof.

---

## 2. Audit-risk scan result

A repository search for high-risk terms such as:

```text
proof sketch partial not proved here modulo should routes to
```

returned multiple later files requiring priority audit, including:

```text
docs/analytic_bridge_span_monotonicity_a74.md
docs/analytic_atom_middle_weighted_core_a80.md
docs/analytic_endpoint_rigid_atom_middle_a81.md
docs/analytic_midpoint_boundary_a55.md
docs/analytic_global_acyclicity_attempt_a73.md
docs/analytic_long_blocker_crossing_h1_a66.md
docs/analytic_weighted_cut_selection_a79.md
docs/analytic_rigid_separated_self_return_a77.md
docs/analytic_status_after_weighted_cut_swap_a61.md
docs/analytic_cut_rigid_weighted_self_return_a82.md
```

This does not mean these notes are wrong.  It means they contain statements that must be converted from proof-program language into final-proof language.

---

## 3. Highest-priority audit targets

### Tier 1: final-architecture dependencies

These are critical because A84 depends on them globally.

```text
A73 global acyclicity attempt
A74 bridge-span monotonicity
A75 equal-span separated bridge returns
A76 gap-preserving separated recurrence
A77 rigid separated self-return
A78 non-weighted acyclicity theorem
A79 weighted cut-selection refinement
A80 atom-middle weighted core
A81 endpoint-rigid atom-middle
A82 cut-rigid weighted self-return
A83 internal cyclic rigidity
A84 endpoint-avoidance assembly
```

Audit requirement:

```text
Every proposition used in A78 and A83 must be backed by a complete proof, not a proof sketch.
```

---

### Tier 2: recurrence-routing dependencies

These feed the non-weighted acyclicity theorem.

```text
A64 recurrence theorem attempt
A65 H1 long-blocker uncrossing
A66 H1 crossing cases
A67 H2 long-blocker uncrossing
A68 recurrence status after atom insertion
A69 pair-difference recurrence
A70 singleton-prefix recurrence
A71 cyclic-cut recurrence
A72 obstruction dependency graph
```

Audit requirement:

```text
Every recurrence branch must have an explicit exhaustive case split and a strict measure decrease or named exit edge.
```

---

### Tier 3: separated-equal / midpoint / weighted local tables

These supply the main branch reductions.

```text
A36--A54 separated-equal direct and gap-after branches
A55 midpoint boundary
A56--A62 weighted and external-collision setup
```

Audit requirement:

```text
Each displayed collision equation must be checked for endpoint cases, empty-block cases, sign convention, and external collision handling.
```

---

### Tier 4: early reductions and definitions

These are likely easier but foundational.

```text
A1 strong nonzero-sum -> Erdős 475
A2 endpoint avoidance -> strong nonzero-sum
A3 path-external equivalence
A4/A5 adjacent forbidden-hit obstruction
A20--A35 interval and zero-composite setup
```

Audit requirement:

```text
Definitions must be consistent across all notes: Graham-valid, endpoint avoidance, partial sums, forbidden hit, support, span, route, recurrence.
```

---

## 4. Red-flag phrases to eliminate or formalize

The final proof should avoid using these phrases without a theorem reference:

```text
routes to
controlled by
modulo A34
expected
should
likely
proof sketch
status
partial
not proved here
locally routed
architecture-level
```

Replacement pattern:

```text
Instead of:  This routes to A78.
Use:         By Lemma X.Y, the branch is transformed into class C with measure M' < M.  Then Theorem A78.Z applies.
```

---

## 5. Required local proof template

Every lemma in the final proof should include:

```text
1. exact hypotheses, including nonempty blocks;
2. exact block decomposition;
3. exact partial-sum equation;
4. algebraic derivation line by line;
5. endpoint cases;
6. characteristic assumptions;
7. conclusion class;
8. explicit measure decrease or named terminal theorem.
```

For example, a routing lemma must not merely say:

```text
routes to zero-composite machinery.
```

It must say:

```text
The equation becomes X+Y=0 with X,Y nonempty and support contained in interval I of span s'<s.  Therefore this is a TWO_PIECE_ZERO obstruction with measure decrease in the first coordinate.
```

---

## 6. Empty-block audit

For every block expression such as:

```text
A B C,
P R,
U V,
B G U,
A q C,
X local Y
```

check whether each block is allowed to be empty.

The final proof should explicitly mark blocks as:

```text
nonempty by construction;
possibly empty;
empty endpoint case handled separately;
empty case impossible;
empty case collapses.
```

High-risk notes:

```text
A55 midpoint boundary;
A59/A60 weighted cuts;
A65--A67 H1/H2 blocker pullbacks;
A70 singleton-prefix recurrence;
A75--A77 separated bridge/gap cases;
A79--A83 weighted core induction.
```

---

## 7. Sign and orientation audit

Every equation derived from a collision must be checked under both orientations:

```text
left blocker vs right blocker;
prefix vs tail;
pre-segment external vs post-segment external;
cyclic wrapped vs non-wrapped;
swap forward vs swap inverse.
```

High-risk relations:

```text
A65 right-blocker pair-difference equations;
A67 H2 right-blocker equations;
A69 pair-swap recurrence equations;
A70 singleton right-blocker equations;
A81 endpoint-rigid sign patterns;
A82 returned weighted-middle comparisons.
```

For each sign pattern, the final proof should show the exact equation rather than relying on “sign-reversed similarly.”

---

## 8. Measure-decrease audit

A78 depends on the global measure:

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

For every edge in A72, verify one of:

```text
1. reaches SUCCESS;
2. reaches CONTRADICTION;
3. decreases M_NW^* immediately;
4. enters a finite subroutine whose every cycle decreases M_NW^*;
5. enters weighted induction and decreases |B|.
```

No edge may be justified only by “class complexity decreases” unless the class order is explicitly part of the measure.

---

## 9. Recurrence-depth audit

A64 changed the recurrence measure so that `h_excess` is last, not first.

Audit all recurrence notes for consistency with this decision:

```text
A64 bounded-blocker descent;
A65--A67 atom-insertion recurrence;
A69 pair-difference recurrence;
A70 singleton-prefix recurrence;
A71 cyclic-cut recurrence;
A78 global measure.
```

Required check:

```text
No recurrence argument should require h' < h except as an immediate contradiction.
No recurrence argument should use h' > h as a worsening primary coordinate.
```

---

## 10. Weighted-core audit

The weighted proof chain is now:

```text
A56 weighted normal forms
A58 nested zero-composite
A60 fixed cut-swap routing
A79 proper-cut induction split
A80--A81 atom-middle elimination
A82 cut-rigid self-return
A83 internal cyclic rigidity elimination
```

Audit requirements:

```text
1. A56 normal-form tests exhaustive for every signed/coefficient-2 branch.
2. A60 cut-swap collision table includes external collisions or correctly delegates to A62.
3. A79 induction on |B| is well-founded and cannot increase |B| before decreasing.
4. A81 sign-pattern algebra is checked explicitly.
5. A83 endpoint-set invariance is genuinely forced by exact self-return, not merely plausible.
6. Full-field endpoint-set case handles subsets smaller than F_p^* correctly.
```

The most critical single audit point is:

```text
A83.2: exact cyclic self-return implies E_B - T_k = E_B.
```

If this implication fails, the weighted closure is not complete.

---

## 11. External-collision audit

A62 is used to avoid redoing external collisions in later notes.  It must be made fully formal.

Audit requirements:

```text
1. define exactly what counts as external;
2. handle collisions before the local segment;
3. handle collisions after the local segment;
4. handle collisions inside unchanged displayed families;
5. handle cyclic/wrapping collisions;
6. show every pullback is one of the named classes;
7. prove the pullback does not increase measure unless bridge analysis A74--A77 applies.
```

---

## 12. Computational audit

A86 found that the referenced exact path:

```text
docs/finite_verification_ledger.md
```

was not found by repository search.

Required actions:

```text
1. locate existing finite verification artifacts under another name;
2. if absent, regenerate them;
3. add exact commands and hashes;
4. separate advisory searches from certified exhaustive verification;
5. add independent certificate checker.
```

No finite computation should be cited in the final proof unless the exact artifact is present and reproducible.

---

## 13. Suggested machine-check scripts

Add scripts for audit support:

```text
scripts/audit_risk_terms.py
scripts/audit_empty_block_cases.py
scripts/audit_measure_edges.py
scripts/verify_small_primes_endpoint_avoidance.py
scripts/verify_small_primes_erdos475.py
```

Minimum useful outputs:

```text
risk_terms_report.json
measure_edge_report.json
small_prime_endpoint_report.json
small_prime_erdos475_report.json
```

---

## 14. Proof extraction plan

After audit, extract a clean proof in this order:

```text
1. Definitions and theorem statements.
2. Endpoint avoidance minimal-counterexample setup.
3. Local obstruction generation via A5.
4. Non-weighted obstruction classes and measure.
5. Non-weighted termination theorem.
6. Weighted-core theorem.
7. Endpoint avoidance conclusion.
8. Endpoint avoidance -> strong nonzero-sum -> Erdős 475.
9. p=2 and empty-set cases.
```

The final proof should not include every exploratory A-note.  It should include only hardened lemmas required by the dependency graph.

---

## 15. Current status after A87

The proof program is now in audit/extraction mode.

Current status:

```text
Conditional proof architecture assembled.
Theorem dependency chain audited.
Finite exceptional cases identified.
Local lemma hardening still required.
```

Do not claim a complete proof until Tier 1 and Tier 2 audit items are resolved.

---

## 16. Target A88

A88 should create a formal dependency table mapping every final theorem to required A-notes.

Suggested columns:

```text
Final theorem/lemma;
Required notes;
Risk level;
Audit status;
Missing proof details;
Replacement final-proof lemma ID.
```

This will turn the proof program into a publishable proof-extraction roadmap.
