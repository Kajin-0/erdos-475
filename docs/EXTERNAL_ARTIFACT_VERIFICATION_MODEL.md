# External artifact verification model

This document defines how large finite-certificate artifacts should be represented when the raw witness JSONL files are too large for ordinary Git storage.

## Purpose

Several finite-certificate witness files are hundreds of MiB to more than 1.5 GiB. Committing all raw artifacts directly would make the repository difficult to clone and review.

The repository therefore distinguishes between:

```text
1. committed CI-verified certificate artifacts;
2. hash-backed external JSONL artifacts;
3. summary-only deterministic witness digests.
```

This model is evidence infrastructure. It does not prove Erdős 475 and does not assert analytic residue inclusion.

## Artifact classes

### Class A: committed CI-verified certificate artifact

A committed certificate artifact is stored directly in the repository and checked by both independent verifiers in CI.

Required properties:

```text
- raw JSONL artifact is committed;
- every row contains p, B, and final_order;
- Python verifier passes with --require-canonical and --require-coverage;
- Rust verifier passes with --require-canonical and --require-coverage;
- MANIFEST.sha256 covers the artifact;
- certificates/verified_domains.json declares the domain.
```

Interpretation:

```text
This is the strongest repository-native finite-certificate status.
```

### Class B: hash-backed external JSONL artifact

A hash-backed external artifact is too large to commit directly, but is identified exactly by filename, size, row count, expected canonical count, and SHA256 digest.

Required properties:

```text
- domain p:b is specified;
- filename is recorded;
- byte size is recorded;
- SHA256 digest is recorded;
- row count is recorded;
- expected canonical count is recorded;
- row count equals expected canonical count;
- original generation and verification workflow is described;
- artifact can be obtained or regenerated for independent checking.
```

Recommended independent checks:

```text
1. Obtain the exact external JSONL file.
2. Verify SHA256.
3. Verify line count.
4. Run Python row-level witness verification.
5. Run Rust row-level witness verification.
6. Run full --require-coverage verification when computationally feasible.
```

Interpretation:

```text
This is strong external finite-certificate evidence, but not equivalent to a committed CI-verified artifact unless the external verification protocol is explicitly accepted for that domain.
```

### Class C: summary-only deterministic witness digest

A summary-only artifact records a deterministic generation run without storing every witness row. It records processed count, solved count, failure count, and an aggregate SHA256 digest over canonical witness records.

Required properties:

```text
- domain p:b is specified;
- generator parameters are recorded;
- processed equals expected canonical count;
- solved equals expected canonical count;
- failed equals 0;
- aggregate SHA256 digest is recorded;
- verdict is PASS;
- generator version and command should be recoverable.
```

Interpretation:

```text
This is compact deterministic generation evidence. It is weaker than a directly checkable committed JSONL artifact, but valuable for domains where raw JSONL would be too large to handle conveniently.
```

## Trust labels

The following labels should be used consistently in documentation.

| Label                        | Meaning                                                                                        |
| ---------------------------- | ---------------------------------------------------------------------------------------------- |
| `committed_ci_verified`      | Raw artifact is in the repository and checked by Python and Rust in CI.                        |
| `external_jsonl_hash_backed` | Raw JSONL exists outside Git and is identified by SHA256, row count, expected count, and size. |
| `summary_only_digest`        | Deterministic generation summary exists with processed, solved, failed, and aggregate SHA256.  |
| `log_only`                   | Only pass logs or screenshots exist; not enough for durable artifact tracking.                 |

## Per-class reproducibility details

### Class: tier_1a_committed_repo_checkable (committed CI-verified)

- **Artifact class**: tier_1a_committed_repo_checkable (also referred to as committed_ci_verified)
- **Domain p, |B| range**: 17:3, 19:3-5, 23:3-9, 29:3-8, 31:3-6
- **Expected filename**: `certificates/minimal_witnesses.jsonl` and `certificates/witnesses_p29_b08.jsonl`
- **Expected byte size**: varies per commit; recorded in MANIFEST.sha256
- **Expected SHA256**: recorded in MANIFEST.sha256
- **Expected row count**: 247,416 total (136,375 + 111,041)
- **Storage location**: committed in Git repository
- **Local placement path**: same as filename
- **Exact row-count command**: `wc -l certificates/minimal_witnesses.jsonl certificates/witnesses_p29_b08.jsonl`
- **Exact hash-check command**: `sha256sum certificates/minimal_witnesses.jsonl certificates/witnesses_p29_b08.jsonl`
- **Exact Python verifier command**:
  ```bash
  python scripts/verify_minimal_witnesses.py \
    certificates/minimal_witnesses.jsonl \
    certificates/witnesses_p29_b08.jsonl \
    --domain 17:3 --domain 19:3-5 --domain 23:3-9 \
    --domain 29:3-8 --domain 31:3-6 \
    --require-canonical --require-coverage
  ```
- **Exact Rust verifier command**:
  ```bash
  cd rust-verifier && cargo run --release -- \
    ../certificates/minimal_witnesses.jsonl \
    ../certificates/witnesses_p29_b08.jsonl \
    --domain 17:3 --domain 19:3-5 --domain 23:3-9 \
    --domain 29:3-8 --domain 31:3-6 \
    --require-canonical --require-coverage
  ```
- **Full coverage checking**: feasible and required
- **Row-level verification**: feasible and required
- **Publication claims may depend on it**: yes, for the committed domain subset
- **Weaker than committed CI verification**: N/A — this is the committed CI standard

### Class: tier_1b_verified_external_jsonl (external JSONL hash-backed)

- **Artifact class**: tier_1b_verified_external_jsonl
- **Domain p, |B| range**: 29:9-15, 31:7-16
- **Expected filename**: varies per domain (see `docs/EXTERNAL_ARTIFACT_LEDGER.md`)
- **Expected byte size**: recorded in external artifact ledger
- **Expected SHA256**: recorded in external artifact ledger
- **Expected row count**: recorded in external artifact ledger
- **Storage location**: local filesystem or external storage; NOT committed to Git
- **Local placement path**: `local_artifacts/` directory convention
- **Exact row-count command**: `wc -l <artifact_path>.jsonl`
- **Exact hash-check command**: `sha256sum <artifact_path>.jsonl`
- **Exact Python verifier command**:
  ```bash
  python scripts/verify_minimal_witnesses.py \
    <artifact_path>.jsonl \
    --domain <p>:<b_min>-<b_max> \
    --require-canonical --require-coverage
  ```
- **Exact Rust verifier command** (if artifact is locally available and Rust toolchain is installed):
  ```bash
  cd rust-verifier && cargo run --release -- \
    ../<artifact_path>.jsonl \
    --domain <p>:<b_min>-<b_max> \
    --require-canonical --require-coverage
  ```
- **Full coverage checking**: feasible when the artifact is locally available
- **Row-level verification**: feasible when the artifact is locally available
- **Publication claims may depend on it**: yes, for the full declared frontier
- **What remains weaker than committed CI verification**: the artifact is not in Git and cannot be verified by CI without manual artifact placement; hash integrity is recorded but not automatically rechecked by CI

### Class: tier_1b_verified_summary_digest (summary-only deterministic digest)

- **Artifact class**: tier_1b_verified_summary_digest
- **Domain p, |B|**: 31:17
- **Expected filename**: `p31_b17_summary_only_pass.txt`
- **Expected byte size**: small (text summary)
- **Expected SHA256**: recorded in external artifact ledger
- **Expected row count**: processed=3,991,995, solved=3,991,995, failed=0
- **Storage location**: `local_artifacts/summary_only/` or external; NOT committed to Git
- **Local placement path**: `local_artifacts/summary_only/p31_b17_summary_only_pass.txt`
- **Exact row-count command**: parsed from summary log (processed line)
- **Exact hash-check command**: `sha256sum p31_b17_summary_only_pass.txt`
- **Exact Python verifier command**: not applicable (no raw JSONL); verifier used during generation
- **Exact Rust verifier command**: not applicable
- **Full coverage checking**: not feasible from summary alone; deterministic regeneration required
- **Row-level verification**: not feasible from summary alone
- **Publication claims may depend on it**: only if the deterministic generation protocol is accepted as sufficient evidence
- **What remains weaker than committed CI verification**: no committed raw artifact; no independent row-level rechecking without regenerating the entire artifact; relies on generator correctness

## Promotion rules

A domain may be promoted from external evidence to committed CI-verified status only if:

```text
1. the artifact is committed directly, or
2. the repository adopts an explicit external-artifact CI/review mechanism for that domain.
```

Without such a promotion, external artifacts should be described as:

```text
hash-backed external finite-certificate evidence
```

not as fully committed Tier 1 repository certificates.

## Claim boundary

This model concerns finite artifacts only. It does not establish the analytic reduction needed to solve Erdős 475. The theorem-level bridge remains a separate mathematical requirement.
