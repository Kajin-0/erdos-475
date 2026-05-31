# Theorem Domain Ledger

This document records the exact finite domains, verification methods, and artifact status for the Erdős 475 finite-certificate package.

## Claim boundary

This repository currently supports finite-domain verification claims only. A complete proof of Erdős 475 requires an analytic reduction showing that all remaining cases are contained in the verified finite domain.

## Verified finite domain

| Prime p | Complement size | Original size | Method | Trust tier | Artifact status |
|---:|---:|---:|---|---:|---|
| 17 | 3 | 13 | direct witness | 1 | committed / checkable |
| 19 | 3..5 | 15..13 | direct witness | 1 | committed / checkable |
| 23 | 3..9 | 19..13 | direct witness | 1 | committed / checkable |
| 29 | 3..7 | 25..21 | descent certificate | 1 | committed / checkable |
| 29 | 8 | 20 | direct witness | 1 | committed shard `certificates/witnesses_p29_b08.jsonl` |
| 29 | 9..15 | 19..13 | direct witness | 3 | log / external artifact |
| 31 | 3..6 | 27..24 | descent certificate | 1 | committed / checkable |
| 31 | 7..17 | 23..13 | direct witness / summary witness | 3 | log / digest / external artifact |

## Trust tiers

### Tier 1: committed witness certificate

A finite domain is Tier 1 only if all witness artifacts needed for verification are committed or otherwise available and both Python and Rust verifiers can check them.

Current Tier 1 domain summary:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..8
p = 31, |B| = 3..6
```

### Tier 2: reproducible external artifact

A finite domain is Tier 2 if raw witness files are stored externally or regenerated deterministically, with hashes and commands recorded.

### Tier 3: log-only verification

A finite domain is Tier 3 if only PASS logs, counts, or local-file references exist. This is useful research evidence but not yet a public certificate artifact.

Current Tier 3 domain summary:

```text
p = 29, |B| = 9..15
p = 31, |B| = 7..17
```

## Current theorem statement

For each finite complement domain listed above, the project records evidence that every canonical multiplicative-scaling representative B admits an ordering of A = F_p^* \ B whose nonempty partial sums are pairwise distinct modulo p.

Tier 1 domains are intended to be independently checkable by committed artifacts and Python/Rust verification.

Tier 3 domains are research evidence only and should not be described as release-grade finite certificates.

## Not yet proved

The repository does not yet prove that the analytic residue of Erdős 475 is contained in the verified finite domain.

The missing bridge is:

```text
published or internally proved analytic reductions
+ verified finite certificate domain
= complete theorem.
```
