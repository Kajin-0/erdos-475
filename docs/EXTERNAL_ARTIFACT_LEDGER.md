# External artifact ledger

This document summarizes large local finite-certificate artifacts that are not committed directly to the repository because several witness JSONL files are hundreds of MiB to more than 1.5 GiB.

The ledger is derived from:

```text
local_artifacts/batch_manifest/local_jsonl_artifact_manifest.{csv,json,md}
local_artifacts/batch_manifest/summary_only_artifact_manifest.{csv,json,md}
local_artifacts/summary_only/p31_b17_summary_only_pass.txt
```

## Claim boundary

This ledger records external finite-certificate evidence only.

It does not claim a complete proof of Erdős 475. It does not claim that the analytic residue has been fully reduced to these finite domains. It also does not by itself make every external artifact a committed Tier 1 repository artifact.

A domain should be considered committed Tier 1 only when the witness artifact is committed or when the repository explicitly defines and accepts a hash-backed external-artifact verification model for that domain.

## Artifact classes

### Committed JSONL certificate shard

A witness JSONL file is committed directly to the repository. It can be checked by the Python and Rust verifiers in CI.

Current example:

```text
certificates/witnesses_p29_b08.jsonl
```

### External JSONL witness artifact

A witness JSONL file exists locally or externally, but is too large for ordinary Git storage. The repo records the filename, row count, expected canonical count, SHA256 digest, and size.

### Summary-only deterministic witness digest

A full JSONL witness file is not stored. Instead, a deterministic summary-only run records the number of canonical representatives processed, solved, failed, and an aggregate SHA256 digest over the canonical witness records that would have been written.

Current example:

```text
p31_b17_summary_only_pass.txt
```

## External JSONL artifact table

The following table records large local JSONL artifacts from `local_jsonl_artifact_manifest.md`.

| Domain | Rows | Expected canonical rows | Status | Size MiB | SHA256 | Filename |
|---:|---:|---:|---|---:|---|---|
| 23:5..9 | 49,508 | 49,508 | aggregate count matches | 12.657 | `8450a41c6d8176c3366cf1dde632a0a953f065948984cb453579a1a24a0faa41` | `p23_b5_to_b9_witness_traces.jsonl` |
| 29:8 | 111,041 | 111,041 | committed separately; source count matches | 35.915 | `db1fa613a0dc0e538d2310514bb21dd05d29eac40dfd25bb55133661e52511ea` | `p29_b8_witness_traces.jsonl` |
| 29:9 | 246,675 | 246,675 | count matches | 78.547 | `5c21d9b6d263f50f86276dd54d5b26858c58acbef67a8e7ba7d0e76cfa667740` | `p29_b9_witness_traces.jsonl` |
| 29:10 | 468,754 | 468,754 | count matches | 146.904 | `e4e6fd83edd567354ab824ab24eea240b3a4244cf1d261402e023b5f2c8e6fd5` | `p29_b10_witness_traces.jsonl` |
| 29:11 | 766,935 | 766,935 | count matches | 236.496 | `9abcb8c336d4baba0ff8908f91ec9ba267e7883542558097b7c32c92cb2b285a` | `p29_b11_witness_traces.jsonl` |
| 29:12 | 1,086,601 | 1,086,601 | count matches | 329.603 | `df336b98b2549e039b8fe450a48f5bc67674db6727322b77fdf186b0bc864094` | `p29_b12_witness_traces.jsonl` |
| 29:13 | 1,337,220 | 1,337,220 | count matches | 398.894 | `088a104112c49db7caf6b9b1af9e9ff1bb87a8e4eeda7dce69e1094c22953a99` | `p29_b13_witness_traces.jsonl` |
| 29:14 | 1,432,860 | 1,432,860 | count matches | 420.213 | `5fa3c39b0216d121308f898dbba19ca5de6040b0d37c3345852ef0b3cea1bfcf` | `p29_b14_witness_traces.jsonl` |
| 29:15 | 1,337,220 | 1,337,220 | count matches | 385.434 | `93b3b9f5411e1f5ca9728d2e8c7c52108252b79ed98c0a6aa9f3f840b9f14fc1` | `p29_b15_witness_traces.jsonl` |
| 31:7 | 67,860 | 67,860 | count matches | 23.823 | `5cbd4b88bd94e4f1a643596d0e55fa42244c644e5788c6659a132775d91e6fad` | `p31_b7_witness_traces.jsonl` |
| 31:8 | 195,143 | 195,143 | count matches | 67.518 | `a4f5338521e6815b305bf2eca623d75aaf0b7c5ff37cbce7348aa72d41387e59` | `p31_b8_witness_traces.jsonl` |
| 31:9 | 476,913 | 476,913 | count matches | 162.594 | `00bf8827f96bbcff0c07ff1aaf3e8ccba8b96f8e58322528d7f4cdf3ccf06637` | `p31_b9_witness_traces.jsonl` |
| 31:10 | 1,001,603 | 1,001,603 | count matches | 336.404 | `93fe86ab9940796e137e8941585a50a6e58402fcb7737c31d87f9fc90fc9bcf7` | `p31_b10_witness_traces.jsonl` |
| 31:11 | 1,820,910 | 1,820,910 | count matches | 602.340 | `1e7c8ebcbbe251706fe836d29631a4c694e8101e9ff7c7a8781124c993547d8f` | `p31_b11_witness_traces.jsonl` |
| 31:12 | 2,883,289 | 2,883,289 | count matches | 939.135 | `e490dcbec319ee120345661ce126159b46ecb5d2a8002e6ccb165a16ffbc8366` | `p31_b12_witness_traces.jsonl` |
| 31:13 | 3,991,995 | 3,991,995 | count matches | 1280.011 | `1ae060cec4c1105b7006b15b908ba509a93d8289e28687f6b395f81e9cdb3c18` | `p31_b13_witness_traces.jsonl` |
| 31:14 | 4,847,637 | 4,847,637 | count matches | 1529.761 | `f8c962d43473c126de76a7b4bb20c1fec1c91253a1f8b06e82b4f63a4b29259e` | `p31_b14_witness_traces.jsonl` |
| 31:15 | 5,170,604 | 5,170,604 | count matches | 1605.409 | `338c7baa987971c44f489191fb3b05f49aab6a2683676e0b40ab6ab948b01470` | `p31_b15_witness_traces.jsonl` |
| 31:16 | 4,847,637 | 4,847,637 | count matches | 1480.492 | `2d291655d113bcf0d1edae42367743c1eb3b92c793f8bfa2fba53bbab4368a82` | `p31_b16_witness_traces.jsonl` |

## Summary-only artifact table

| Domain | Processed | Solved | Failed | Expected canonical rows | Status | Aggregate SHA256 | Verdict | Filename |
|---:|---:|---:|---:|---:|---|---|---|---|
| 31:17 | 3,991,995 | 3,991,995 | 0 | 3,991,995 | PASS_SUMMARY_COUNT | `e1aa6a80e90560084d5538867d396d03057d1b777cde2e20dd7bcdebf4b4e2cb` | PASS | `p31_b17_summary_only_pass.txt` |

## Aggregate coverage represented by external artifacts

External or source-side artifacts recorded here cover the following additional finite domains beyond the originally committed small-prime/descent core:

```text
p = 29, |B| = 8..15
p = 31, |B| = 7..17
```

The JSONL artifacts for `p = 29, |B| = 8..15` contain:

```text
6,787,306 canonical instances
```

The JSONL plus summary-only artifacts for `p = 31, |B| = 7..17` contain:

```text
29,295,586 canonical instances
```

Combined with the currently committed Tier 1 core of 247,416 instances, the external ledger represents evidence for a much larger finite frontier. The repository should not treat the whole frontier as fully committed Tier 1 until an accepted external-artifact verification model is formalized.

## Recommended review protocol

For a domain recorded only by external JSONL:

```text
1. Obtain the exact artifact named in the ledger.
2. Check SHA256 against this ledger.
3. Check line count against the expected canonical count.
4. Run the Python verifier with --require-canonical and --require-coverage for feasible domains.
5. Run the Rust verifier independently for feasible domains.
6. For very large domains, run row-level verification and a scalable coverage audit, or use a deterministic summary-only digest protocol.
```

For a summary-only digest artifact:

```text
1. Check the summary log was generated with the declared parameters.
2. Confirm processed = solved = expected canonical count and failed = 0.
3. Confirm the aggregate SHA256 digest is recorded.
4. Preserve the generator version and command line needed to reproduce the digest.
5. Treat the evidence as hash-backed deterministic generation evidence, not as a directly committed witness JSONL.
```

## Current status

This ledger is evidence infrastructure. It is intended to support future promotion decisions without pushing multi-GB witness files into Git history.
