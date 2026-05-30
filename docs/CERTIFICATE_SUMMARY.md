# Certificate summary

This document gives a compact audit summary of the current Tier 1 finite-certificate artifact for Erdős Problem 475 / Graham's rearrangement problem.

It is intended for reviewers who want the exact finite scope without first reading the full JSONL witness file.

## Claim boundary

This is a finite-certificate verification summary. It is not a complete proof of Erdős 475 and does not assert that the remaining analytic residue is contained in the verified finite domain.

## Notation

```text
A subset F_p^*
B = F_p^* \ A
b = |B| = p - 1 - |A|
```

For each canonical complement representative `B`, the certificate stores a witness ordering of

```text
A = F_p^* \ B.
```

The verifiers check that all nonempty partial sums of the witness ordering are pairwise distinct modulo `p`.

## Tier 1 finite domains

The current strict Tier 1 certificate covers exactly:

| Prime p | Complement size | Canonical instances |
|---:|---:|---:|
| 17 | 3 | 35 |
| 19 | 3 | 46 |
| 19 | 4 | 172 |
| 19 | 5 | 476 |
| 23 | 3 | 70 |
| 23 | 4 | 335 |
| 23 | 5 | 1,197 |
| 23 | 6 | 3,399 |
| 23 | 7 | 7,752 |
| 23 | 8 | 14,550 |
| 23 | 9 | 22,610 |
| 29 | 3 | 117 |
| 29 | 4 | 735 |
| 29 | 5 | 3,510 |
| 29 | 6 | 13,468 |
| 29 | 7 | 42,288 |
| 31 | 3 | 136 |
| 31 | 4 | 917 |
| 31 | 5 | 4,751 |
| 31 | 6 | 19,811 |
| **Total** |  | **136,375** |

## Certificate artifacts

Primary witness certificate:

```text
certificates/minimal_witnesses.jsonl
```

Small-prime direct-witness source file:

```text
certificates/direct_witnesses_small_primes.jsonl
```

Hash manifest:

```text
MANIFEST.sha256
```

Current manifest hashes include:

```text
1da3cee4b41c3db753af7c50f0b981f1f62157297c075c5e970dff39668b47e1  certificates/direct_witnesses_small_primes.jsonl
8579a58db0d7539b71919fa8e90878ee7f47e20a394f8d823d785f4484dce573  certificates/minimal_witnesses.jsonl
ed7272e974ca3a091d89dce6fe8a9e1429f2d6dfe516645ba2988b53f3e865fd  certificates/verified_domains.json
```

## Verification commands

Strict Python verification:

```bash
STRICT_CERT=1 bash scripts/run_all_verification.sh
```

Independent Rust verification:

```bash
cd rust-verifier
cargo run --release -- ../certificates/minimal_witnesses.jsonl \
  --domain 17:3 \
  --domain 19:3-5 \
  --domain 23:3-9 \
  --domain 29:3-7 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
```

Expected verification summary:

```text
verified_rows=136375
unique_instances=136375
PASS minimal witness verification
PASS rust minimal witness verification
```

## What the verifiers check

For each witness row, the verifiers recompute:

```text
1. p is prime;
2. B subset F_p^*;
3. B is canonical under nonzero multiplicative scaling;
4. final_order is a permutation of F_p^* \ B;
5. all nonempty partial sums of final_order are pairwise distinct modulo p;
6. declared canonical coverage is complete for every requested domain.
```

## Remaining non-Tier-1 declared domains

The following declared domains remain lower-trust evidence until corresponding witness artifacts, hashes, and independent verifier checks are committed:

```text
p = 29, |B| = 8..15
p = 31, |B| = 7..17
```

## AI disclosure

Some documentation and code development used AI assistance. The finite-certificate claims summarized here are direct machine-checkable witness-verification claims over explicit finite data, not AI-authority claims.
