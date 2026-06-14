# Agent Worklog

## Session: 2026-06-04 — Pham--Sauermann first proof-structure extraction

### Current objective

Move `docs/theorem_extraction/pham_sauermann_2026.md` from a scaffold to a first real theorem/proof dependency extraction using the arXiv HTML source.

### Files read

- `docs/source_theorems.yaml`
- `docs/theorem_extraction/pham_sauermann_2026.md`
- arXiv HTML for `2602.15797`

### Files changed

- `docs/theorem_extraction/pham_sauermann_2026.md` — upgraded to Level 2 provisional; added theorem/proof structure map, Section 5 constant-choice description, dependency graph, and precise blockers.
- `scripts/arxiv_html_section_snapshot.py` — new helper for reproducible arXiv HTML text snapshots.
- `docs/AGENT_WORKLOG.md` — added this session entry.

### Commands / external reads

```text
Read arXiv HTML for 2602.15797.
Inspected theorem map, Section 4 chain anticoncentration, and Section 5 proof skeleton.
```

### What worked

1. Confirmed Theorem 1.2 statement: for every `0<alpha<1`, there is `C_alpha` such that `C_alpha <= |S| <= p^(1-alpha)` implies a valid ordering.
2. Confirmed paper organization: Section 3 proves Theorem 1.3, Section 4 derives Corollary 1.4 and Corollary 4.2, Section 5 proves Theorem 1.2.
3. Confirmed Theorem 1.3 uses an explicit constant in the HTML text: Section 3 says it proves the anticoncentration theorem taking `C=2^24`.
4. Confirmed Section 5 uses Corollary 4.2 constants for `d=3` and `d=5`.
5. Confirmed Section 5 bad-event structure: Lemmas 5.1, 5.2, 5.3 bound three bad events, and their union probability is made < 1 to choose a starting bijection.
6. Identified that the proof is probably effective in principle: finite probabilistic estimates, union bounds, Chernoff/hypergeometric concentration, Fourier analysis, and Cauchy-Davenport are used. No non-effective compactness or infinitary regularity step was identified in this pass.

### What did not work

- arXiv HTML strips much of the displayed mathematics and does not preserve enough equations to compute constants.
- `C_alpha` is structurally located but not numerically or recursively extracted.
- Corollary 4.2 constants for `d=3` and `d=5` are not yet explicit in the repo.
- Lemma 5.1--5.6 probability bounds still need exact displayed inequalities from PDF/TeX source.

### Mathematical direction

Proof-audit extraction only. Do not mark Pham--Sauermann proof-mode effective yet.

### Claim boundary

No new proof claim. `pham_sauermann_2026_large_prime` remains `effective_status: non_effective` in `docs/source_theorems.yaml`.

### Next recommended small task

Fetch the arXiv TeX or PDF source for `2602.15797` and extract the displayed inequalities from:

```text
Theorem 1.3;
Corollary 1.4;
Corollary 4.2;
Lemmas 5.1--5.6;
Section 5 initial constant choice.
```

---

## Session: 2026-06-04 — construct A92 no-reentry certificate instances for E15, E18, E19

### Current objective

Construct concrete no-reentry certificate instances for the three confirmed support-containment W-to-NW exit rows: E15 (two-piece zero inside B), E18 (equal-prefix inside B), and E19 (equal-tail inside B). Each instance follows the schema from docs/analytic_a92_no_reentry_certificate_schema.md.

### Confirmed working path

/tmp/erdos-475

### Files read

- docs/AGENT_WORKLOG.md
- docs/analytic_a92_no_reentry_certificate_schema.md
- docs/analytic_a92_support_containment_analysis.md
- docs/analytic_weighted_to_nonweighted_exit_decrease_table.md
- docs/final/F11_weighted_cut_selection_extraction.md
- docs/final/F10_weighted_normal_form_cut_swap.md

### Files changed

- `docs/analytic_a92_no_reentry_certificate_instances.md` — new file (3 complete certificate instances for E15, E18, E19 with full C_no_reentry objects, exclusion bases, checked coordinates, blocked reentry types, theorem sources, verification status, comparison table, and A92 graph attachment mapping).
- `docs/AGENT_WORKLOG.md` — added this session entry.

### Commands run

```bash
python3 scripts/check_claim_boundary_consistency.py
python3 scripts/check_no_overclaiming.py
python3 scripts/check_manifest_completeness.py
python3 scripts/check_sha256_manifest_completeness.py
bash scripts/make_manifest.sh
```

### Tests passed

All 4 checks pass (boundary, overclaim, manifest, SHA256 after regeneration)

### Tests failed

None

### What worked

1. E15 certificate (R_k'=P_j', two-piece zero inside B): strict support_size(NW1) < m blocks same-middle without needing A89. Strongest candidate — support containment alone suffices for both j=m and j>m.
2. E18 and E19 certificates (equal-prefix/equal-tail): support_size(NW1) <= m blocks j>m unconditionally, and j=m is blocked by A89/F11.7 pattern-rigid impossibility. Correctly documented the A89 dependency.
3. All three certificates include detailed exclusion_basis with per-case coverage (same_middle vs larger_middle), checked_coordinates with PROPOSED status, blocked_reentry_types with structural reasoning for each weighted entry type (A56, A81, A97, F6, F7).
4. Comparison table shows the strength difference: E15 is strongest (no external theorem dependency for same-middle), E18/E19 are medium (need A89).
5. Attachment mapping defines the exact graph edge linkage for each certificate.

### What did not work

- All 3 instances are PROPOSED — none is PROVED. Each has missing_fields including per-instance measure coordinates and formal blocked-reentry proofs.
- Earlier-coordinate non-increase (enclosing_span, gap_length) is PROPOSED but not proved for any row.
- The blocked_reentry_types arguments are heuristic — they argue structural impossibility but are not formal proofs.
- E18 and E19 depend on A89/F11.7 for same-middle exclusion, which is a nontrivial external theorem dependency.

### Mathematical direction

no mathematical change — proof-audit documentation only

### Claim boundary

finite-certificate verification and proof-engineering workspace only. No-reentry certificates not proved, not claimed to exist.

### Next recommended small task

Verify the earlier-coordinate non-increase (enclosing_span, gap_length) for E15, E18, and E19 by tracing the concrete atom configuration of each exit type. This is the last prerequisite before these certificates can be promoted from PROPOSED to ASSERTED.

---

## Session: 2026-06-04 — analyze W-to-NW support containment for A92 no-reentry certificate

### Current objective

Analyze all 22 W-to-NW exit table rows to determine which have NW1 support strictly contained within B, the precondition for the support-containment no-reentry certificate basis. Classify each row, identify confirmed containment rows, and document the certificate potential for each.

### Confirmed working path

/tmp/erdos-475
