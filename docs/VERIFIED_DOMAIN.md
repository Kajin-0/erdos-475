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

## Declared Tier 1 verified finite complement domains

The currently declared Tier 1 verified finite complement domains are:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

These are recorded in `certificates/verified_domains.json` with method labels, trust tiers, and artifact storage classes.

## Tier 1 artifact storage classes

Tier 1 means verified finite-certificate evidence exists for the declared domain. Artifact storage is recorded separately.

### Tier 1A: committed or repository-checkable artifacts

Tier 1A domains have committed or repository-generated artifacts available for routine CI/Python/Rust verification.

Current Tier 1A subset:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..8
p = 31, |B| = 3..6
```

The committed/repository-checkable artifacts currently contain:

```text
247416 canonical finite instances
```

with Python verification, Rust verification, and `MANIFEST.sha256` hash locking.

The Tier 1A `p=29, |B|=8` domain is stored as the committed shard:

```text
certificates/witnesses_p29_b08.jsonl
```

### Tier 1B: verified local/external artifacts

Tier 1B domains have verified local/external JSONL artifacts or verified summary-digest artifacts that are not committed to Git due to size.

Current Tier 1B verified local/external JSONL subset:

```text
p = 29, |B| = 9..15
p = 31, |B| = 7..16
```

Current Tier 1B verified summary-digest subset:

```text
p = 31, |B| = 17
```

Tier 1B artifacts should be described as verified finite evidence, but not as routine Git/CI-checkable artifacts until their raw files or reproducible artifact storage are available to independent reviewers.

### Tier 3: unhardened research evidence

Tier 3 is reserved for research-only evidence not yet suitable for release-grade finite-certificate claims.

No currently declared finite domain is intentionally classified as Tier 3 in `certificates/verified_domains.json` after the p=29 and p=31 verification status correction.

## Strict release-grade finite-certificate target

Before this repository is presented externally as a hardened finite-certificate workspace, the following must be true:

```text
1. certificates/minimal_witnesses.jsonl exists and is nonempty.
2. certificates/witnesses_p29_b08.jsonl exists and is nonempty.
3. Python verification passes on committed certificate files.
4. Rust verification passes on committed certificate files.
5. MANIFEST.sha256 exists and hash-checks critical artifacts.
6. CI fails if required certificate files or hashes are missing.
7. No empty trace placeholders are presented as evidence.
8. README.md, docs/CLAIM_BOUNDARY.md, and this file agree on the claim boundary.
9. certificates/verified_domains.json remains the single source of truth for finite-domain audit rules.
10. Tier 1B external/local artifacts have recorded hashes, locations, and reproduction or retrieval instructions before public release claims depend on them.
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
5. That Tier 1B external/local evidence is routine Git/CI-checkable without artifact retrieval.
```

## Related theorem-architecture documents

```text
docs/THEOREM_DOMAIN_LEDGER.md
docs/EFFECTIVE_FINITE_COMPLETION_THEOREM.md
docs/COVERAGE_SANDWICH_LEMMA.md
docs/SOURCE_EXTRACTION_PRIME_FIELD.md
docs/INSERTION_CUT_COVER_PROGRAM.md
```
