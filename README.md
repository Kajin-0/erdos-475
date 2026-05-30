# Erdős 475 finite-certificate workspace

This repository is a finite-certificate verification, analytic-reduction, and proof-engineering workspace for Erdős Problem 475, also known as Graham's rearrangement problem.

## Claim boundary

This repository should be read as a finite-certificate project unless and until the analytic reduction ledger and strict certificate artifacts are complete.

Safe current claim:

```text
The repository records and develops independently checkable finite-certificate verification infrastructure for declared finite complement domains.
```

Not claimed here:

```text
A complete proof of Erdős 475.
A disproof of Erdős 475.
A standalone analytic proof.
That the remaining analytic residue is contained in the verified finite domain.
```

The full theorem would require:

```text
external analytic reductions
+ verified finite certificate domain
+ proof that the analytic residue is contained in the verified finite domain
```

See:

```text
docs/CLAIM_BOUNDARY.md
docs/VERIFIED_DOMAIN.md
docs/FINITE_FRONTIER_STATUS.md
docs/EXTERNAL_REVIEW_PACKET.md
```

---

## Finite certificate notation

The package works with complements

```text
B = F_p^* \ A
```

where `A subset F_p^*`. A finite witness row records:

```text
p
B
final_order
```

where `final_order` is an ordering of

```text
A = F_p^* \ B.
```

A direct verifier checks that all nonempty partial sums of `final_order` are pairwise distinct modulo `p`.

---

## Verified domain source of truth

The machine-readable finite-domain ledger is:

```text
certificates/verified_domains.json
```

The explanatory ledgers are:

```text
docs/VERIFIED_DOMAIN.md
docs/FINITE_FRONTIER_STATUS.md
docs/EXTERNAL_ARTIFACT_LEDGER.md
docs/EXTERNAL_ARTIFACT_VERIFICATION_MODEL.md
```

The currently declared finite complement frontier is:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

The current committed CI-verified certificate covers:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..8
p = 31, |B| = 3..6
```

with:

```text
247,416 canonical finite instances
Python verifier pass
Rust verifier pass
MANIFEST.sha256 hash locking
GitHub Actions CI verification
```

The committed certificate artifacts are:

```text
certificates/minimal_witnesses.jsonl
certificates/witnesses_p29_b08.jsonl
```

The external/hash-backed finite evidence frontier records:

```text
p = 29, |B| = 9..15
p = 31, |B| = 7..17
```

with:

```text
36,219,267 canonical instances represented by committed plus external/hash-backed evidence
```

External/hash-backed evidence should not be presented as equivalent to committed CI verification unless the corresponding external-artifact verification model is explicitly accepted for that domain.

---

## Strict public-certificate standard

Before this repository is linked externally as a hardened finite-certificate workspace, the following should be true:

```text
1. Committed certificate artifacts exist and are nonempty.
2. Python verifier passes on committed certificate artifacts.
3. Rust verifier passes on committed certificate artifacts.
4. MANIFEST.sha256 exists and verifies critical artifacts.
5. CI fails if strict certificate artifacts are missing.
6. No empty trace placeholders are presented as evidence.
7. README.md, docs/CLAIM_BOUNDARY.md, docs/VERIFIED_DOMAIN.md, and docs/EXTERNAL_REVIEW_PACKET.md are synchronized.
8. certificates/verified_domains.json remains the single source of truth for finite-domain audit rules.
```

---

## Minimal witness certificates

The committed trusted artifacts are:

```text
certificates/minimal_witnesses.jsonl
certificates/witnesses_p29_b08.jsonl
```

with one JSON object per canonical complement representative:

```json
{"p":29,"B":[1,2,5],"final_order":[...]}
```

The verifier recomputes from scratch:

```text
p is prime;
B subset F_p^*;
B is canonical under multiplicative scaling;
final_order is a permutation of F_p^* \ B;
nonempty partial sums of final_order are pairwise distinct mod p;
declared canonical coverage is complete.
```

Trace files and descent certificates are provenance. Final witnesses are the smaller finite-existence kernel.

---

## Development verification

Run all configured development checks from the repository root:

```bash
bash scripts/run_all_verification.sh
```

Development verification may generate `certificates/minimal_witnesses.jsonl` from committed traces if the witness file is absent. This is useful for iteration, but it is not the same as strict release-grade certificate verification.

---

## Strict certificate verification

Strict mode requires committed witness artifacts and hash manifest to exist:

```bash
STRICT_CERT=1 bash scripts/run_all_verification.sh
```

Expected committed certificate result:

```text
verified_rows=247416
unique_instances=247416
PASS minimal witness verification
```

Strict mode should be used before external database-link outreach or release claims.

---

## Verify committed witnesses directly

Python:

```bash
python scripts/verify_minimal_witnesses.py \
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

Expected Rust result:

```text
verified_rows=247416
unique_instances=247416
PASS rust minimal witness verification
```

---

## External artifact review

Large witness JSONL artifacts are recorded by hash, count, and size rather than committed directly when they are hundreds of MiB to more than 1.5 GiB.

See:

```text
docs/EXTERNAL_ARTIFACT_LEDGER.md
docs/EXTERNAL_ARTIFACT_VERIFICATION_MODEL.md
local_artifacts/batch_manifest/local_jsonl_artifact_manifest.md
local_artifacts/batch_manifest/summary_only_artifact_manifest.md
```

The external ledger is evidence infrastructure. It is not a complete proof and does not establish analytic residue inclusion.

---

## Residue-audit and proof-mining tools

Finite-completion tooling:

```text
scripts/reduction_residue_audit.py
scripts/sweep_coverage_sandwich.py
```
