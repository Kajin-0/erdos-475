# External review packet for Erdős Problem 475

This repository is a finite-certificate verification workspace for Erdős Problem 475, also known as Graham's rearrangement problem.

It is not a proof announcement and does not request any problem-status change.

## Problem notation

Let `p` be prime and let

```text
A subset F_p^*
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
...
a_1 + ... + a_t
```

are pairwise distinct modulo `p`.

## Committed CI-verified finite certificates

The repository currently commits JSONL finite-certificate artifacts for all canonical complement representatives in the following domains:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..8
p = 31, |B| = 3..6
```

The committed certificate artifacts are:

```text
certificates/minimal_witnesses.jsonl
certificates/witnesses_p29_b08.jsonl
```

They contain, in union:

```text
247,416 canonical finite instances
```

Each witness row records at least:

```text
p
B
final_order
```

where `final_order` is an ordering of

```text
A = F_p^* \ B.
```

Some rows also contain provenance fields such as canonical scaling, source trace, source line, or search metadata.

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

The committed certificate set is checked by:

```text
Python verifier
Rust verifier
MANIFEST.sha256 hash manifest
GitHub Actions CI
```

## Reproduction commands

From the repository root:

```bash
STRICT_CERT=1 bash scripts/run_all_verification.sh
```

Independent Rust verification:

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
```

Expected result:

```text
verified_rows=247416
unique_instances=247416
PASS minimal witness verification
PASS rust minimal witness verification
```

## External/hash-backed finite evidence

The repository also records large external or source-side artifacts that are not committed directly as JSONL files because several are hundreds of MiB to more than 1.5 GiB.

The external artifact ledger records evidence for:

```text
p = 29, |B| = 9..15
p = 31, |B| = 7..17
```

Additional external evidence beyond the committed CI-verified set:

```text
p = 29, |B| = 9..15: 6,676,265 canonical instances
p = 31, |B| = 7..17: 29,295,586 canonical instances
```

Combined committed plus external/hash-backed finite evidence represented in the repository:

```text
36,219,267 canonical instances
```

Relevant documents:

```text
docs/EXTERNAL_ARTIFACT_LEDGER.md
docs/EXTERNAL_ARTIFACT_VERIFICATION_MODEL.md
docs/FINITE_FRONTIER_STATUS.md
```

## Status interpretation

The repository distinguishes between:

```text
committed_ci_verified
external_jsonl_hash_backed
summary_only_digest
log_only
```

Only the committed CI-verified domains are directly checked in repository CI.

The external/hash-backed frontier is evidence infrastructure for future review and promotion decisions. It is not automatically equivalent to committed CI-verified certificate status.

## Claim boundary

This repository does not claim:

```text
1. A complete proof of Erdős 475.
2. A disproof of Erdős 475.
3. A standalone analytic proof.
4. That the remaining analytic residue is contained in the verified finite frontier.
5. That every external/hash-backed artifact is equivalent to committed CI verification.
```

The theorem-level bridge remains:

```text
external analytic coverage
+ verified finite certificate frontier
+ proof that every remaining analytic residue case is contained in that frontier
```

Until that bridge is complete, this repository should be cited only as a finite-certificate verification workspace and proof-engineering project.

## AI disclosure

Some documentation and code development used AI assistance. The intended finite-certificate claims are not AI-authority claims. They are direct machine-checkable witness-verification claims from explicit finite data.

## Suggested database comment, if appropriate

```yaml
comments: "Finite-certificate verification workspace: https://github.com/Kajin-0/erdos-475"
```
