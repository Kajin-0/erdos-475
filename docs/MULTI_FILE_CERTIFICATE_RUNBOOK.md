# Multi-file certificate runbook

This runbook explains how to split finite-certificate artifacts across multiple JSONL files without weakening verification.

## Motivation

The current Tier 1 certificate already contains 136375 canonical finite instances. Future expansions such as `p = 29, |B| = 8..15` and `p = 31, |B| = 7..17` may be too large or inconvenient to maintain as one monolithic JSONL file.

The Python and Rust verifiers therefore support multiple certificate files in one verification call.

## Critical invariant

Splitting certificates must not weaken verification.

The verifiers enforce global duplicate detection across all input files. A canonical pair `(p, B)` may not appear twice across the combined input set.

## Python usage

```bash
python3 scripts/verify_minimal_witnesses.py \
  certificates/minimal_witnesses.jsonl \
  certificates/witnesses_p29_b08.jsonl \
  --domain 17:3 \
  --domain 19:3-5 \
  --domain 23:3-9 \
  --domain 29:3-8 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
```

## Rust usage

```bash
cd rust-verifier
cargo run --release -- \
  ../certificates/minimal_witnesses.jsonl \
  ../certificates/witnesses_p29_b08.jsonl \
  --domain 17:3 \
  --domain 19:3-5 \
  --domain 23:3-9 \
  --domain 29:3-8 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
cd ..
```

## Suggested future artifact layout

Prefer domain-split artifacts such as:

```text
certificates/witnesses_p17_b3.jsonl
certificates/witnesses_p19_b3_to_b5.jsonl
certificates/witnesses_p23_b3_to_b9.jsonl
certificates/witnesses_p29_b3_to_b7.jsonl
certificates/witnesses_p29_b8_to_b15.jsonl
certificates/witnesses_p31_b3_to_b6.jsonl
certificates/witnesses_p31_b7_to_b17.jsonl
```

A monolithic convenience file may still exist, but split files are easier to regenerate, review, hash-lock, and replace independently.

## Required release steps for a new split artifact

For each new certificate file:

```text
1. Generate witness rows deterministically or record the exact generation command.
2. Verify the file independently with Python.
3. Verify the file independently with Rust.
4. Verify the union of all Tier 1 files with Python and Rust.
5. Regenerate MANIFEST.sha256 if the artifact is committed.
6. Update certificates/verified_domains.json.
7. Update docs/VERIFIED_DOMAIN.md and docs/CERTIFICATE_SUMMARY.md if present.
8. Ensure CI verifies the relevant domain union.
```

## Non-claim boundary

Multi-file verification is only a scaling mechanism for finite certificates. It does not prove the analytic residue inclusion needed for a theorem-level result.
