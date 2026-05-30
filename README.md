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

The currently declared finite complement domains are:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

The current strict Tier 1 certificate covers:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

with:

```text
136375 canonical finite instances
Python verifier pass
Rust verifier pass
MANIFEST.sha256 hash locking
```

The remaining declared Tier 3 domains are:

```text
p = 29, |B| = 8..15
p = 31, |B| = 7..17
```

Tier 3 log/digest/external-artifact-pending evidence should not be presented as release-grade independent verification.

---

## Strict public-certificate standard

Before this repository is linked externally as a hardened finite-certificate workspace, the following should be true:

```text
1. certificates/minimal_witnesses.jsonl exists and is nonempty.
2. Python verifier passes on committed certificate artifacts.
3. Rust verifier passes on committed certificate artifacts.
4. MANIFEST.sha256 exists and verifies critical artifacts.
5. CI fails if strict certificate artifacts are missing.
6. No empty trace placeholders are presented as evidence.
7. README.md, docs/CLAIM_BOUNDARY.md, and docs/VERIFIED_DOMAIN.md are synchronized.
8. certificates/verified_domains.json remains the single source of truth for finite-domain audit rules.
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

---

## Development verification

Run all configured development checks from the repository root:

```bash
bash scripts/run_all_verification.sh
```

Development verification may generate `certificates/minimal_witnesses.jsonl` from committed traces if the witness file is absent.  This is useful for iteration, but it is not the same as strict release-grade certificate verification.

---

## Strict certificate verification

Strict mode requires the committed witness file and hash manifest to exist:

```bash
STRICT_CERT=1 bash scripts/run_all_verification.sh
```

Strict mode should be used before external database-link outreach or release claims.

---

## Generate minimal witnesses from traces

```bash
python scripts/extract_minimal_witnesses.py \
  --trace traces/p29_r3_to_r7_repair_traces_strict.jsonl \
  --trace traces/p31_r3_to_r6_repair_traces_strict.jsonl \
  --out certificates/minimal_witnesses.jsonl \
  --strict
```

Then verify the current strict Tier 1 certificate:

```bash
python scripts/verify_minimal_witnesses.py \
  certificates/minimal_witnesses.jsonl \
  --domain 17:3 \
  --domain 19:3-5 \
  --domain 23:3-9 \
  --domain 29:3-7 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
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

---

## Residue-audit and proof-mining tools

Finite-completion tooling:

```text
scripts/reduction_residue_audit.py
scripts/sweep_coverage_sandwich.py
```

Insertion/cut-cover proof-mining tooling:

```text
scripts/analyze_insertion_blocks.py
scripts/search_insertion_reorderings.py
```

Small-prime counterexample sanity tooling:

```text
scripts/search_small_counterexamples.py
```

These tools support research and audit workflows.  They do not by themselves prove the full theorem.

---

## Existing trace/certificate validation

The repository may also contain richer trace and CSV certificate checks.

### Trace semantics

```bash
python scripts/verify_erdos475_trace_semantics.py \
  traces/p29_r3_to_r7_repair_traces_strict.jsonl \
  traces/p31_r3_to_r6_repair_traces_strict.jsonl
```

### Certificate verification

```bash
python scripts/verify_erdos475_certificates.py \
  --trace-files \
    traces/p29_r3_to_r7_repair_traces_strict.jsonl \
    traces/p31_r3_to_r6_repair_traces_strict.jsonl \
  --nonatomic-csv \
    certificates/p29_nonatomic_descent_full.csv \
    certificates/p31_nonatomic_descent_full.csv \
  --onecollision-csv \
    certificates/p29_one_collision_deep_full.csv \
    certificates/p31_one_collision_deep_full.csv \
  --atomic-instances certificates/atomic_local_cert_instances.csv \
  --atomic-certs certificates/atomic_local_certs.csv \
  --require-onecollision-intermediates \
  --strict-csv
```

### Coverage audit

```bash
python scripts/audit_erdos475_trace_coverage.py \
  traces/p29_r3_to_r7_repair_traces_strict.jsonl \
  traces/p31_r3_to_r6_repair_traces_strict.jsonl \
  --summary-csv certificates/trace_coverage_summary.csv
```

---

## Hash manifest

After certificates are finalized:

```bash
bash scripts/make_manifest.sh
sha256sum -c MANIFEST.sha256
```

---

## AI disclosure

Some documentation and code development used AI assistance.  The intended finite-certificate claims are direct machine-checkable witness-verification claims.  Theorem-level claims require independently checkable artifacts plus a completed analytic residue inclusion.

---

## Repository layout

```text
docs/            proof drafts, finite theorem docs, trust model, reduction ledger
scripts/         Python verification, audit, and proof-mining scripts
rust-verifier/   independent Rust witness verifier
traces/          JSONL trace universes, if committed
certificates/    witness JSONL and CSV certificate tables
logs/            saved validation logs, if committed
.github/         CI workflow
```

---

## Main documents

```text
docs/CLAIM_BOUNDARY.md
docs/VERIFIED_DOMAIN.md
docs/THEOREM_DOMAIN_LEDGER.md
docs/EFFECTIVE_FINITE_COMPLETION_THEOREM.md
docs/COVERAGE_SANDWICH_LEMMA.md
docs/SOURCE_EXTRACTION_PRIME_FIELD.md
docs/INSERTION_CUT_COVER_PROGRAM.md
docs/TIER1_EXPANSION_RUNBOOK.md
```

Older analytic and proof drafts remain research notes unless explicitly promoted into a verified theorem chain.
