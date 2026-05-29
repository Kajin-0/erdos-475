# Claim boundary

This repository is currently a finite-certificate, analytic-reduction, and proof-engineering workspace for Erdős 475.

## Safe current claim

The strongest safe claim currently supported by the sprint artifacts is:

```text
The pure worse-only m=3 hidden-support branch is certified closed in the analyzed finite domain.
```

More specifically, the local hidden-support branch has certificate-backed coverage:

```text
zero_sum records: 83/83 routed
equality records: 11/11 tiebroken
combined hidden-support records: 94/94 covered
```

The zero-sum branch has:

```text
record-level route coverage: 83/83
representative route examples: 24/24
attempt-level witnesses: 24/24
```

The equality branch has:

```text
11/11 equality records tiebroken
2/2 primary-failure rows with corrected P_suffix+q mechanism
fallback creates no new shortest block in the certified primary-failure rows
```

## Unsafe claim

The repository must not currently claim:

```text
The full Erdős 475 theorem is proved.
```

The full theorem remains conditional until the global proof bridge is closed:

```text
analytic residue subset certified finite domain.
```

## Required distinction

The following are different statements and should not be conflated.

### Local certified branch closure

```text
A specific residual branch is closed in the analyzed finite domain by certificate-backed diagnostics and proof-facing lemmas.
```

This is the current status for the pure worse-only `m=3` hidden-support branch.

### Global theorem closure

```text
Every analytic residue required for Erdős 475 is proved to lie inside the verified finite domain, and every finite-domain artifact is reproducible and hash-locked.
```

This is not yet complete.

## Documentation rule

The README, proof notes, theorem drafts, and sprint documents should use language such as:

```text
certified in the analyzed finite domain
local branch closure
proof-facing draft
certificate-backed evidence
remaining symbolic proof obligation
```

They should avoid language such as:

```text
complete proof
Erdős 475 solved
the theorem is proved
final global closure
```

unless the global analytic residue inclusion and verified-domain synchronization are complete.

## Current local theorem package

The local hidden-support branch is summarized by:

```text
docs/analytic_sprint/S100_hidden_support_local_theorem_formalization.md
docs/analytic_sprint/S105_zero_sum_routing_lemma_final_draft.md
docs/analytic_sprint/S106_corrected_equality_tie_break_endpoint_proof.md
docs/analytic_sprint/S107_equality_tie_break_symbolic_gap_closure.md
docs/analytic_sprint/S108_final_local_hidden_support_closure_proof.md
```

These documents are proof-facing local theorem drafts.  They are not a completed full proof of Erdős 475.

## Remaining local proof obligations

The local branch still needs publication-grade symbolic conversion of certificate-backed lemmas:

```text
1. Lemma A: hidden-support extraction into the four families.
2. Lemma Z: zero-sum route classification without classifier language.
3. Lemma C: formal equality tie-break endpoint proof.
4. Refined-defect well-foundedness and induction compatibility.
```

## Remaining global proof obligations

Before any full-theorem claim, the repository needs:

```text
1. VERIFIED_DOMAIN.md as the single source of truth.
2. MANIFEST.sha256 for critical artifacts.
3. CI checks for required certificates and stale/missing artifacts.
4. Analytic residue inclusion: analytic residue subset certified finite domain.
5. Claim synchronization across README, proof.tex, theorem notes, and sprint docs.
```

## Merge guidance

A merge to `main` may be appropriate as a checkpoint if this claim boundary is preserved.

The recommended interpretation of such a merge is:

```text
Merge as proof-infrastructure and certified-local-branch progress.
Do not merge as a full proof claim.
```
