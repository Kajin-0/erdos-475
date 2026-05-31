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
docs/EFFECTIVE_FINITE_COMPLETION_THEOREM.md
```

---

## Finite certificate notation

The package works with complements

```text
B = F_p^* \ A
```

where `A subset F_p^*`.  A finite witness row records:

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

The explanatory ledger is:

```text
docs/VERIFIED_DOMAIN.md
```

The currently declared Tier 1 verified finite complement domains are:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

Artifact storage is split into classes:

```text
Tier 1A: committed or repository-generated artifacts are available for routine CI/Python/Rust verification.
Tier 1B: verified local/external JSONL or summary-digest artifacts exist, but are not committed to Git due to size.
```

The current Tier 1A committed/repository-checkable subset is:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..8
p = 31, |B| = 3..6
```

with:

```text
247416 canonical finite instances
Python verifier pass
Rust verifier pass
MANIFEST.sha256 hash locking
```

The current Tier 1B verified local/external artifact subset is:

```text
p = 29, |B| = 9..15
p = 31, |B| = 7..16
```

and the current Tier 1B summary-digest subset is:

```text
p = 31, |B| = 17
```

Tier 1B artifacts should be described as verified finite evidence, but not as routine Git/CI-checkable artifacts until their raw files or reproducible artifact storage are available to independent reviewers.

---

## Strict public-certificate standard

Before this repository is linked externally as a hardened finite-certificate workspace, the following should be true:

```text
1. certificates/minimal_witnesses.jsonl exists and is nonempty.
2. certificates/witnesses_p29_b08.jsonl exists and is nonempty.
3. Python verifier passes on committed certificate artifacts.
4. Rust verifier passes on committed certificate artifacts.
5. MANIFEST.sha256 exists and verifies critical artifacts.
6. CI fails if strict certificate artifacts are missing.
7. No empty trace placeholders are presented as evidence.
8. README.md, docs/CLAIM_BOUNDARY.md, and docs/VERIFIED_DOMAIN.md are synchronized.
9. certificates/verified_domains.json remains the single source of truth for finite-domain audit rules.
10. Tier 1B external/local artifacts have recorded hashes, locations, and reproduction or retrieval instructions before public release claims depend on them.
```

---

## Minimal witness certificate

The preferred trusted artifact is:

```text
certificates/minimal_witnesses.jsonl
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

Trace files and descent certificates are provenance.  Final witnesses are the smaller finite-existence kernel.

The Tier 1A `p=29, |B|=8` domain is stored as a committed shard:

```text
certificates/witnesses_p29_b08.jsonl
```

---

## Development verification

Run all configured development checks from the repository root:

```bash
bash scripts/run_all_verification.sh
```

Development verification may generate `certificates/minimal_witnesses.jsonl` from committed traces if the witness file is absent.  This is useful for iteration, but it is not the same as strict release-grade verification of Tier 1B external/local artifacts.

---

## Strict certificate verification

Strict mode requires the committed witness files and hash manifest to exist:

```bash
STRICT_CERT=1 bash scripts/run_all_verification.sh
```

Strict mode currently verifies the Tier 1A committed/repository-checkable subset. Tier 1B external/local artifacts require their own artifact retrieval or local-path verification commands.

---

## Generate minimal witnesses from traces

```bash
python scripts/extract_minimal_witnesses.py \
  --trace traces/p29_r3_to_r7_repair_traces_strict.jsonl \
  --trace traces/p31_r3_to_r6_repair_traces_strict.jsonl \
  --out certificates/minimal_witnesses.jsonl \
  --strict
```

Then verify the current Tier 1A committed/repository-checkable subset:

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
cargo run --release -- ../certificates/minimal_witnesses.jsonl ../certificates/witnesses_p29_b08.jsonl \
  --domain 17:3 \
  --domain 19:3-5 \
  --domain 23:3-9 \
  --domain 29:3-8 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
```

---

## Residue-audit and proof-mining tools

Finite-completion tooling:

```text
scripts/reduction_residue_audit.py
scripts/sweep_coverage_sandwich.py
```
