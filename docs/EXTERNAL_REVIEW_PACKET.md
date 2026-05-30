# External review packet for Erdős Problem 475

This repository is a finite-certificate verification workspace for Erdős Problem 475, also known as Graham's rearrangement problem.

It is not a proof announcement and does not request any status change.

## Problem notation

Let `p` be prime and let

```text
A subset F_p^*.
```

Write

```text
B = F_p^* \ A.
```

A witness is an ordering

```text
a_1, ..., a_t
```

of `A` such that the nonempty partial sums

```text
a_1,
a_1 + a_2,
...,
a_1 + ... + a_t
```

are pairwise distinct modulo `p`.

## Hardened Tier 1 finite certificate

The current release-grade artifact verifies all canonical complement representatives in the following finite domains:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

The certificate artifact is:

```text
certificates/minimal_witnesses.jsonl
```

It contains:

```text
136375 canonical finite instances
```

Each row records:

```text
p
B
canonical_scale_lambda
final_order
source
source_line or search metadata
```

where `final_order` is an ordering of

```text
A = F_p^* \ B.
```

## Verification standard

For each certificate row, the verifiers check:

```text
1. p is prime;
2. B subset F_p^*;
3. B is canonical under nonzero multiplicative scaling;
4. final_order is a permutation of F_p^* \ B;
5. all nonempty partial sums of final_order are pairwise distinct modulo p;
6. declared canonical coverage is complete.
```

The certificate has been checked by:

```text
Python verifier
Rust verifier
MANIFEST.sha256 hash manifest
```

## Reproduction commands

From the repository root:

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

Expected result:

```text
verified_rows=136375
unique_instances=136375
PASS minimal witness verification
PASS rust minimal witness verification
```

## Current Tier 1 scope

The current Tier 1 scope is finite and explicit:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

The remaining declared lower-trust domains are:

```text
p = 29, |B| = 8..15
p = 31, |B| = 7..17
```

These are not currently presented as release-grade Tier 1 certificate artifacts unless and until corresponding witness artifacts, hashes, and verifier checks are committed.

## Claim boundary

This repository does not claim:

```text
1. A complete proof of Erdős 475.
2. A disproof of Erdős 475.
3. A standalone analytic proof.
4. That the remaining analytic residue is contained in the verified finite domain.
5. That lower-trust Tier 3 evidence is release-grade independent verification.
```

The full theorem would require:

```text
external analytic coverage
+ verified finite certificate domain
+ proof that the remaining analytic residue is contained in the verified finite domain
```

## AI disclosure

Some documentation and code development used AI assistance. The intended finite-certificate claims are not AI-authority claims. They are direct machine-checkable witness-verification claims from explicit finite data.

## Suggested database comment, if appropriate

```yaml
comments: "Finite-certificate verification workspace: https://github.com/Kajin-0/erdos-475"
```
