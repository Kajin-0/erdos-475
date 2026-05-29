# Theorem Domain Ledger

This document records the exact finite domains, verification methods, and artifact status for the Erdős 475 finite-certificate package.

## Claim boundary

This repository currently supports finite-domain verification claims only. A complete proof of Erdős 475 requires an analytic reduction showing that all remaining cases are contained in the verified finite domain.

## Verified finite domain

| Prime p | Complement size | Original size | Method | Artifact status |
|---:|---:|---:|---|---|
| 17 | 3 | 13 | direct witness | log / external artifact |
| 19 | 3..5 | 15..13 | direct witness | log / external artifact |
| 23 | 3..9 | 19..13 | direct witness | log / external artifact |
| 29 | 3..7 | 25..21 | descent certificate | committed / checkable |
| 29 | 8..15 | 20..13 | direct witness | log / external artifact |
| 31 | 3..6 | 27..24 | descent certificate | committed / checkable |
| 31 | 7..17 | 23..13 | direct witness / summary witness | log / digest / external artifact |

## Trust tiers

### Tier 1: committed witness certificate

A finite domain is Tier 1 only if all witness artifacts needed for verification are committed or otherwise available and both Python and Rust verifiers can check them.

### Tier 2: reproducible external artifact

A finite domain is Tier 2 if raw witness files are stored externally or regenerated deterministically, with hashes and commands recorded.

### Tier 3: log-only verification

A finite domain is Tier 3 if only PASS logs, counts, or local-file references exist. This is useful research evidence but not yet a public certificate artifact.

## Current theorem statement

For each finite complement domain listed above, the project records evidence that every canonical multiplicative-scaling representative B admits an ordering of A = F_p^* \ B whose nonempty partial sums are pairwise distinct modulo p.

## Not yet proved

The repository does not yet prove that the analytic residue of Erdős 475 is contained in the verified finite domain.

The missing bridge is:

published or internally proved analytic reductions
+ verified finite certificate domain
= complete theorem.
