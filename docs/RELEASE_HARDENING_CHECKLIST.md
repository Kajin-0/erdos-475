# Release hardening checklist

This checklist must be satisfied before presenting this repository externally as a hardened finite-certificate workspace for Erdős Problem 475.

The current target is responsible finite-certificate verification, not a full theorem claim.

## 1. Certificate artifacts

```text
[ ] certificates/minimal_witnesses.jsonl exists.
[ ] certificates/minimal_witnesses.jsonl is nonempty.
[ ] Every row is valid JSONL.
[ ] Every row contains p, B, and final_order.
[ ] Every final_order is a permutation of F_p^* \ B.
[ ] Every final_order has pairwise distinct nonempty partial sums modulo p.
[ ] Canonical complement coverage is complete for declared Tier 1 domains.
```

## 2. Independent verification

```text
[ ] Python verifier passes on committed certificate artifacts.
[ ] Rust verifier passes on committed certificate artifacts.
[ ] Python and Rust domains agree.
[ ] Verifiers require canonical representatives when canonical coverage is claimed.
[ ] Verifiers require coverage when finite-domain coverage is claimed.
```

Required commands:

```bash
python scripts/verify_minimal_witnesses.py \
  certificates/minimal_witnesses.jsonl \
  --domain 29:3-7 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage

cd rust-verifier
cargo run --release -- ../certificates/minimal_witnesses.jsonl \
  --domain 29:3-7 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
```

## 3. Hash locking

```text
[ ] MANIFEST.sha256 exists.
[ ] MANIFEST.sha256 includes certificates/minimal_witnesses.jsonl.
[ ] MANIFEST.sha256 includes certificates/verified_domains.json.
[ ] MANIFEST.sha256 includes verifier source files.
[ ] scripts/check_sha256_manifest_completeness.py passes.
```

Required command:

```bash
python scripts/check_sha256_manifest_completeness.py
```

## 4a. Schema validation

```text
[ ] scripts/validate_certificate_schema.py --strict passes on all certificate files.
[ ] No untrusted fields (partial_sums, trace_status, etc.) in committed certificates.
[ ] No bool-as-int values in certificate files.
[ ] certificates/verified_domains.json has valid domain structure.
[ ] No unknown artifact classes in verified_domains.json.
```

Required command:

```bash
python scripts/validate_certificate_schema.py \
  certificates/minimal_witnesses.jsonl \
  certificates/witnesses_p29_b08.jsonl \
  certificates/verified_domains.json \
  --strict
```

## 4b. Canonical count audit

```text
[ ] scripts/audit_canonical_counts.py --require-canonical passes for all domains.
[ ] No noncanonical rows in committed certificates.
[ ] No malformed rows.
[ ] No duplicate canonical representatives.
[ ] Expected counts match observed counts for every domain.
```

Required command:

```bash
python scripts/audit_canonical_counts.py \
  certificates/minimal_witnesses.jsonl \
  certificates/witnesses_p29_b08.jsonl \
  --require-canonical
```

## 4c. Manifest and SHA256 checks

```text
[ ] scripts/check_manifest_completeness.py passes.
[ ] scripts/check_sha256_manifest_completeness.py passes.
[ ] Every required file from MANIFEST.required is present.
[ ] Every trusted file from the SHA256 check list is covered in MANIFEST.sha256.
```

Required commands:

```bash
python scripts/check_manifest_completeness.py
python scripts/check_sha256_manifest_completeness.py
```

The SHA256 checker reads `release/manifest_policy.json` and verifies all trusted files, no forbidden files, no excluded paths, and no self-entry.

Required command (regenerate manifest from policy):

```bash
bash scripts/make_manifest.sh
```

## 4d. Overclaim detection

```text
[ ] scripts/check_no_overclaiming.py passes.
[ ] No high-risk doc contains unsafe phrases like "complete proof", "solved", "final proof".
```

Required command:

```bash
python scripts/check_no_overclaiming.py
```

## 4e. CI behavior

```text
[ ] Development CI passes.
[ ] Strict certificate mode fails if certificates/minimal_witnesses.jsonl is missing.
[ ] Strict certificate mode fails if certificates/minimal_witnesses.jsonl is empty.
[ ] Strict certificate mode fails if MANIFEST.sha256 is missing.
[ ] Strict certificate mode fails if schema validation fails.
[ ] Strict certificate mode fails if canonical count audit fails.
[ ] Strict certificate mode fails if manifest completeness check fails.
[ ] Strict certificate mode fails if SHA256 coverage check fails.
[ ] Strict certificate mode fails if overclaim detection fails.
[ ] CI docs-only classification works (scripts/ci_classify.sh used).
[ ] Strict certificate mode passes after release artifacts are committed.
```

Strict local command:

```bash
STRICT_CERT=1 bash scripts/run_all_verification.sh
```

## 5. Documentation synchronization

```text
[ ] README.md claim boundary matches docs/CLAIM_BOUNDARY.md.
[ ] docs/VERIFIED_DOMAIN.md matches certificates/verified_domains.json.
[ ] docs/THEOREM_DOMAIN_LEDGER.md matches certificates/verified_domains.json.
[ ] docs/EFFECTIVE_FINITE_COMPLETION_THEOREM.md states the theorem-level claim conditionally.
[ ] No document claims a complete proof of Erdős 475.
[ ] No document claims the problem is solved.
[ ] Tier 3 evidence is not described as release-grade verification.
```

## 6. Trace and log hygiene

```text
[ ] No empty trace placeholders are presented as evidence.
[ ] Logs are clearly distinguished from trusted certificate artifacts.
[ ] Generated logs either have hashes or are marked as working artifacts.
[ ] Any external artifacts have stable URLs and hashes.
```

## 7. AI disclosure

```text
[ ] README.md contains AI assistance disclosure.
[ ] docs/CLAIM_BOUNDARY.md contains AI assistance disclosure.
[ ] Any external issue or PR discloses AI assistance.
[ ] Certificate claims are described as direct machine-checkable witness verification, not AI-derived mathematical authority.
```

## 8. Makefile targets

```text
[ ] make verify passes
[ ] make verify-strict passes
[ ] make verify-python passes
[ ] make validate-schema passes
[ ] make audit-counts passes
[ ] make check-manifest passes
[ ] make check-claims passes
[ ] make test passes
[ ] make manifest regenerates MANIFEST.sha256 from policy
[ ] make release-audit passes (full suite)
```

## 9. External database-link readiness

Before opening an issue or PR in `teorth/erdosproblems`, the recommended minimum is:

```text
[ ] certificates/minimal_witnesses.jsonl exists and is nonempty.
[ ] Python verifier passes.
[ ] Rust verifier passes.
[ ] release/manifest_policy.json exists and is valid.
[ ] MANIFEST.sha256 exists and passes policy coverage check.
[ ] STRICT_CERT=1 bash scripts/run_all_verification.sh passes.
[ ] README.md and docs/CLAIM_BOUNDARY.md explicitly say this is not a complete proof.
```

If these are not satisfied, the repository may still be useful research infrastructure, but it should not yet be advertised as a hardened finite-certificate workspace.
