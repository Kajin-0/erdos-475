# Multi-file certificate runbook

This runbook explains how to split finite-certificate artifacts across multiple JSONL files while preserving the same verification guarantees.

## Motivation

The current Tier 1 certificate already contains:

```text
136375 canonical finite instances
```

Future expansions such as

```text
p = 29, |B| = 8..15
p = 31, |B| = 7..17
```

may be too large or inconvenient to maintain as one monolithic JSONL file.

The Python and Rust verifiers therefore support multiple certificate files in one verification call.

## Critical invariant

Splitting certificates must not weaken verification.

The verifiers enforce global duplicate detection across all input files.  A canonical pair

```text
(p, B)
```

may not appear twice across the combined input set unless duplicate checking is explicitly disabled in the Python verifier for diagnostic use.

## Python usage

```bash
python3 scripts/verify_minimal_witnesses.py \
  certificates/minimal_witnesses.jsonl \
  certificates/direct_witnesses_small_primes.jsonl \
  --domain 17:3 \
  --domain 19:3-5 \
  --domain 23:3-9 \
  --domain 29:3-7 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
```

The verifier prints one per-file row count:

```text
certificate_file=<path> verified_rows=<n>
```

and then prints the combined totals:

```text
verified_rows=<total rows across all files>
unique_instances=<unique (p,B) pairs across all files>
PASS minimal witness verification
```

## Rust usage

```bash
cd rust-verifier
cargo run --release -- \
  ../certificates/minimal_witnesses.jsonl \
  ../certificates/direct_witnesses_small_primes.jsonl \
  --domain 17:3 \
  --domain 19:3-5 \
  --domain 23:3-9 \
  --domain 29:3-7 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
cd ..
```

The Rust verifier also enforces global duplicate detection across files.

## Suggested future artifact layout

If the remaining finite domains are promoted to Tier 1, prefer domain-split artifacts such as:

```text
certificates/witnesses_p17_b3.jsonl
certificates/witnesses_p19_b3_to_b5.jsonl
certificates/witnesses_p23_b3_to_b9.jsonl
certificates/witnesses_p29_b3_to_b7.jsonl
certificates/witnesses_p29_b8_to_b15.jsonl
certificates/witnesses_p31_b3_to_b6.jsonl
certificates/witnesses_p31_b7_to_b17.jsonl
```

A monolithic convenience file may still exist, but the split files should be easier to regenerate, review, and hash-lock independently.

## Required release steps for a new split artifact

For each new certificate file:

```text
1. Generate witness rows deterministically or record the exact generation command.
2. Verify the file independently with Python.
3. Verify the file independently with Rust.
4. Verify the union of all Tier 1 files with Python and Rust.
5. Regenerate MANIFEST.sha256.
6. Update certificates/verified_domains.json.
7. Update docs/VERIFIED_DOMAIN.md and docs/CERTIFICATE_SUMMARY.md.
8. Ensure CI verifies the relevant domain union.
```

## Non-claim boundary

Multi-file verification is only a scaling mechanism for finite certificates.  It does not prove the analytic residue inclusion needed for a theorem-level result.
