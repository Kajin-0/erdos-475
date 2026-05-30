# Verified domain

This file records the repository-level claim boundary for finite-domain verification in the Erdős 475 / Graham rearrangement workspace.

The machine-readable source of truth is:

```text
certificates/verified_domains.json
```

This Markdown file is explanatory only. If this file and `certificates/verified_domains.json` disagree, the JSON file controls the finite-domain audit tooling.

## Current status summary

```text
Repository role: finite-certificate verification and reduction-ledger workspace
Full Erdős 475 theorem: not claimed
Standalone proof: not claimed
```

The repository is intended to support direct finite witness verification for declared complement domains and to track the remaining analytic bridge needed for any theorem-level use.

## Notation

```text
A subset F_p^*
B = F_p^* \ A
b = |B| = p - 1 - |A|
t = |A|
```

A finite witness row has the form:

```json
{"p":29,"B":[...],"final_order":[...]}
```

where `final_order` is an ordering of

```text
A = F_p^* \ B.
```

A direct verifier checks that all nonempty partial sums of `final_order` are pairwise distinct modulo `p`.

## Declared finite complement domains

The currently declared finite complement domains are:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

These are recorded in `certificates/verified_domains.json` with method labels and trust tiers.

## Trust tiers

### Tier 1: committed or repository-generated witness certificate

A domain is Tier 1 only when the repository has committed witness artifacts, or deterministic trace artifacts from which those witnesses are generated during verification, and independent verifiers can check the result.

Current Tier 1 entries in `certificates/verified_domains.json` are:

```text
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

### Tier 2: reproducible external artifact

A domain is Tier 2 when raw witness artifacts are available externally or are reproducible from documented commands, with hashes and artifact locations recorded.

### Tier 3: log, digest, or external-artifact pending evidence

A domain is Tier 3 when evidence exists as logs, summaries, digests, or external artifacts that still require release-grade hardening.

Current Tier 3 entries include:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 8..15
p = 31, |B| = 7..17
```

Tier 3 entries should not be described as release-grade certificate artifacts until the required JSONL witnesses, hashes, and verifier checks are committed or otherwise made independently reproducible.

## Strict release-grade finite-certificate target

Before this repository is presented externally as a hardened finite-certificate workspace, the following must be true:

```text
1. certificates/minimal_witnesses.jsonl exists and is nonempty.
2. Python verification passes on the committed certificate file.
3. Rust verification passes on the committed certificate file.
4. MANIFEST.sha256 exists and hash-checks critical artifacts.
5. CI fails if required certificate files or hashes are missing.
6. No empty trace placeholders are presented as evidence.
7. README.md, docs/CLAIM_BOUNDARY.md, and this file agree on the claim boundary.
8. certificates/verified_domains.json remains the single source of truth for finite-domain audit rules.
```

## Current missing global bridge

The full theorem would require:

```text
external analytic coverage
+ verified finite certificate domain
+ proof that the remaining analytic residue is contained in the verified finite domain
```

This repository does not currently prove that bridge.

## Explicit non-claims

The repository does not currently claim:

```text
1. A complete proof of Erdős 475.
2. A disproof of Erdős 475.
3. A standalone analytic proof.
4. That the declared finite certificate domain contains the full analytic residue.
5. That Tier 3 evidence is release-grade independent verification.
```

## Related theorem-architecture documents

```text
docs/THEOREM_DOMAIN_LEDGER.md
docs/EFFECTIVE_FINITE_COMPLETION_THEOREM.md
docs/COVERAGE_SANDWICH_LEMMA.md
docs/SOURCE_EXTRACTION_PRIME_FIELD.md
docs/INSERTION_CUT_COVER_PROGRAM.md
```
