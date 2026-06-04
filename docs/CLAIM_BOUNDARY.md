# Claim boundary

This repository is a finite-certificate verification, analytic-reduction, and proof-engineering workspace for Erdős Problem 475 / Graham's rearrangement problem.

## Safe current claim

The safe current claim is:

```text
The repository records and develops independently checkable finite-certificate verification infrastructure for declared finite complement domains.
```

The machine-readable finite-domain ledger is:

```text
certificates/verified_domains.json
```

The explanatory domain ledger is:

```text
docs/VERIFIED_DOMAIN.md
```

## Unsafe claims

The repository must not currently claim:

```text
The full Erdős 475 theorem is proved.
A standalone proof has been completed.
The problem should be marked solved.
The analytic residue is known to be contained in the verified finite domain.
Tier 3 log/digest evidence is release-grade independent verification.
```

## Required theorem bridge

The full theorem remains conditional until the following bridge is complete:

```text
external analytic coverage
+ verified finite certificate domain
+ proof that the analytic residue is contained in the verified finite domain
```

This bridge is tracked by:

```text
docs/EFFECTIVE_FINITE_COMPLETION_THEOREM.md
docs/COVERAGE_SANDWICH_LEMMA.md
docs/SOURCE_EXTRACTION_PRIME_FIELD.md
scripts/reduction_residue_audit.py
scripts/sweep_coverage_sandwich.py
```

## Finite certificate kernel

For a finite complement case, the intended trusted data are:

```text
p
B = F_p^* \ A
canonical complement representative B under nonzero multiplicative scaling
final witness ordering of A = F_p^* \ B
```

A verifier recomputes:

```text
1. p is prime;
2. B subset F_p^*;
3. B is canonical under multiplicative scaling, when canonical coverage is required;
4. final_order is a permutation of F_p^* \ B;
5. nonempty partial sums of final_order are pairwise distinct modulo p;
6. declared canonical coverage is complete, when coverage is required.
```

## Strict public-certificate standard

Before the repository is linked externally as a hardened finite-certificate workspace, the following should be true:

```text
1. certificates/minimal_witnesses.jsonl exists and is nonempty.
2. certificates/witnesses_p29_b08.jsonl exists and is nonempty.
3. Python verifier passes on committed certificate artifacts with self-contained strict type checks.
4. Rust verifier passes on committed certificate artifacts (when Rust toolchain is available).
5. release/manifest_policy.json exists and defines trusted files.
6. MANIFEST.sha256 exists and passes policy coverage check (no self-entry, no forbidden files).
7. CI runs STRICT_CERT=1 as the primary release gate.
8. No empty trace placeholders are presented as evidence.
9. README.md, docs/VERIFIED_DOMAIN.md, and this file are synchronized.
10. certificates/verified_domains.json remains the single source of truth for finite-domain audit rules.
```

## AI disclosure

Some documentation and code development used AI assistance. This does not change the intended proof standard: finite-certificate claims must be direct, machine-checkable witness-verification claims, and theorem-level claims require independently checkable artifacts plus the missing analytic residue inclusion.

## Recommended public wording

Use language such as:

```text
finite-certificate verification workspace
proof-engineering project
reduction-ledger workspace
direct witness verification
machine-checkable finite certificate
conditional finite-completion framework
```

Avoid language such as:

```text
complete proof
Erdős 475 solved
breakthrough proof
final global closure
standalone theorem proof
```

unless the global analytic residue inclusion and strict finite-certificate standards are complete.
