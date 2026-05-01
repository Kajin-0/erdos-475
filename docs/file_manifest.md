# File Manifest

This repository contains a certified finite-check package for complement cases of Erdős Problem 475.

## Essential files

### `docs/`

| File | Purpose |
|---|---|
| `proof.tex` | Main proof draft. |
| `validation_protocol.md` | Commands for independent verification. |
| `file_manifest.md` | This file. |

### `scripts/`

| File | Purpose |
|---|---|
| `verify_erdos475_trace_semantics.py` | Verifies `B` is the complement set and final orders are valid. |
| `verify_erdos475_certificates.py` | Independently verifies all descent and escape certificates. |
| `audit_erdos475_trace_coverage.py` | Audits canonical multiplicative-scaling coverage. |

### `traces/`

| File | Purpose |
|---|---|
| `p29_r3_to_r7_repair_traces_strict.jsonl` | Trace file for `p=29`, complement sizes `3..7`. |
| `p31_r3_to_r6_repair_traces_strict.jsonl` | Trace file for `p=31`, complement sizes `3..6`. |

### `certificates/`

| File | Purpose |
|---|---|
| `p29_nonatomic_descent_full.csv` | Non-atomic `E>=2` certificates for `p=29`. |
| `p31_nonatomic_descent_full.csv` | Non-atomic `E>=2` certificates for `p=31`. |
| `p29_one_collision_deep_full.csv` | One-collision escape certificates for `p=29`. |
| `p31_one_collision_deep_full.csv` | One-collision escape certificates for `p=31`. |
| `atomic_local_cert_instances.csv` | Atomic certificate instances. |
| `atomic_local_certs.csv` | Compressed atomic signature certificates. |
| `trace_coverage_summary.csv` | Coverage-audit summary. |

### `logs/`

| File | Purpose |
|---|---|
| `trace_semantics_pass.txt` | Output of trace-semantics verifier. |
| `certificate_verifier_pass.txt` | Output of independent certificate verifier. |
| `coverage_audit_pass.txt` | Output of coverage audit. |

## Optional files

Exploratory analyzers and sample CSVs are not required for final verification. They may be archived separately if desired.

## Files to omit from the final proof package

Omit old zip files, sample-only CSVs, unresolved intermediate CSVs, and exploratory scripts that are not needed to reproduce or verify the final certificate.
