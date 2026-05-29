# Verified domain

This file is the repository-level source of truth for what is currently verified, what artifacts support it, and what remains outside the verified domain.

## Status summary

Current status:

```text
Local hidden-support branch closure: certificate-backed in the analyzed finite domain.
Full Erdős 475 theorem: not yet verified.
```

The current finite-domain local branch result is:

```text
The pure worse-only m=3 hidden-support branch is certified closed in the analyzed finite domain.
```

This file must be updated before any stronger theorem claim is made.

## Verified local branch

The currently verified local branch is:

```text
pure worse-only m=3 right-terminal hidden-support residual branch
```

with structural form:

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0.
```

The hidden-support extraction families are:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

Current coverage:

```text
zero_sum records: 83/83 covered
equality records: 11/11 covered
combined hidden-support records: 94/94 covered
```

## Prime/domain coverage represented by current sprint artifacts

The local hidden-support sprint artifacts currently report coverage for:

```text
p = 17
p = 23
```

The relevant local summaries include:

```text
p=17:
  pure worse records: 35
  zero_sum hidden-support records routed: 31
  equality records tiebroken: 4

p=23:
  pure worse records: 59
  zero_sum hidden-support records routed: 52
  equality records tiebroken: 7
```

Combined:

```text
p=17,p=23 hidden-support records: 94
```

This does not by itself imply a global theorem range.

## Core local proof notes

The local theorem package is documented in:

```text
docs/analytic_sprint/S98_corrected_hidden_support_branch_theorem.md
docs/analytic_sprint/S99_hidden_support_proof_dependency_ledger.md
docs/analytic_sprint/S100_hidden_support_local_theorem_formalization.md
docs/analytic_sprint/S105_zero_sum_routing_lemma_final_draft.md
docs/analytic_sprint/S106_corrected_equality_tie_break_endpoint_proof.md
docs/analytic_sprint/S107_equality_tie_break_symbolic_gap_closure.md
docs/analytic_sprint/S108_final_local_hidden_support_closure_proof.md
```

## Certificate and diagnostic artifact classes

The local branch closure depends on generated artifacts under `logs/`.  These are currently generated working artifacts, not yet hash-locked release artifacts.

Important artifact classes include:

```text
analysis JSONL files:
  logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
  logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl

hidden-support equation JSONL files:
  logs/bzqa_hidden_support_equations_p17_v3.jsonl
  logs/bzqa_hidden_support_equations_p23_v3.jsonl

bridge move JSONL files:
  logs/hidden_support_bridge_moves_p17_v5.jsonl
  logs/hidden_support_bridge_moves_p23_v5.jsonl

zero-sum route JSONL files:
  logs/route_bq_bqy_obstructions_p17_with_attempts.jsonl
  logs/route_bq_bqy_obstructions_p23_with_attempts.jsonl

zero-sum witness files:
  logs/zero_sum_route_examples_with_attempts.jsonl
  logs/zero_sum_attempt_witnesses_with_attempts.jsonl

summary JSON files:
  logs/summary_hidden_support_bridge_moves_p17_v5.json
  logs/summary_hidden_support_bridge_moves_p23_v5.json
  logs/summary_route_bq_bqy_obstructions_p17_with_attempts.json
  logs/summary_route_bq_bqy_obstructions_p23_with_attempts.json
  logs/summary_zero_sum_attempt_witnesses_with_attempts.json
```

## Required reproduction scripts

The sprint added or used scripts including:

```text
scripts/test_hidden_support_bridge_moves.py
scripts/route_bq_bqy_obstructions_with_attempts.py
scripts/extract_zero_sum_route_examples.py
scripts/extract_zero_sum_attempt_witnesses.py
scripts/make_zero_sum_route_certificate.py
scripts/verify_primary_failure_shape.py
scripts/taxonomize_fallback_local_intervals.py
scripts/make_pure_worse_certificate_table_v4.py
```

These scripts are part of the current proof-engineering workflow.

## Current certification checks

The current local branch certification checks are:

```text
zero-sum routing:
  83/83 routed
  24/24 route examples extracted
  24/24 attempt-level witnesses matched

equality tie-break:
  11/11 equality records tiebroken
  2/2 primary-failure rows are P_suffix+q
  0 fallback-new-short blocks in primary-failure rows

combined hidden-support branch:
  94/94 records covered
```

## Explicit non-verified items

The following are not yet verified by this file:

```text
1. Full Erdős 475 theorem.
2. Global analytic residue inclusion.
3. Exhaustive theorem range beyond the explicitly certified finite artifacts.
4. Publication-grade symbolic proofs of all certificate-backed local lemmas.
5. Hash-locked reproducibility of all logs and generated artifacts.
```

## Required before full-theorem claim

Before claiming the full theorem, the repository must include:

```text
1. A complete analytic-residue ledger.
2. A proof that analytic residue subset certified finite domain.
3. A checked finite-certificate manifest with hashes.
4. CI checks that fail on missing/stale critical artifacts.
5. Synchronized claim text across README.md, proof.tex, docs, and PR descriptions.
```

## Manifest status

Current status:

```text
MANIFEST.sha256: not yet present as a complete release artifact.
```

Until a manifest exists and CI enforces it, `logs/` artifacts should be treated as working certificates rather than release-grade locked evidence.

## Merge guidance

Merging the current PR to `main` is acceptable only as a checkpoint merge for:

```text
proof infrastructure,
finite-certificate workflow,
local hidden-support branch progress,
claim-boundary documentation.
```

It should not be presented as:

```text
full Erdős 475 proof merged.
```

## Update rule

Any future change that strengthens the claim must update this file in the same PR.

Any future change that modifies the certified finite domain must update:

```text
1. this file,
2. the relevant summary artifacts,
3. the manifest once it exists,
4. CI checks once they exist.
```
