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

| Label | Meaning |
|---|---|
| `committed_ci_verified` | Raw artifact is in the repository and checked by Python and Rust in CI. |
| `external_jsonl_hash_backed` | Raw JSONL exists outside Git and is identified by SHA256, row count, expected count, and size. |
| `summary_only_digest` | Deterministic generation summary exists with processed, solved, failed, and aggregate SHA256. |
| `log_only` | Only pass logs or screenshots exist; not enough for durable artifact tracking. |

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
