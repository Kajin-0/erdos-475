# Erdos 475 Certified Finite Complement Check

This repository contains a computer-assisted certificate package for finite complement cases in Erdos Problem 475, also known as Graham's rearrangement problem.

## Claim boundary

This repository should be read as a finite-certificate project unless and until the external reduction ledger is completed.

Safe claim:

```text
The declared finite complement domains are checkable by direct witness verification.
```

Not claimed here yet:

```text
A complete standalone proof of Erdos 475 for all primes and all subsets.
```

The full theorem requires:

```text
external analytic reductions
+ verified finite certificate domain
+ proof that the analytic residue is contained in the verified finite domain
```

See:

```text
docs/REDUCTION_LEDGER.md
```

---

## Finite certificate target

The package works with complements

```text
B = F_p^* \ A
```

and targets the following complement domain, modulo nonzero multiplicative scaling:

```text
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

Equivalently, the original set sizes are:

```text
p = 29, |A| = 21..25
p = 31, |A| = 24..27
```

The finite theorem is certified only when `certificates/minimal_witnesses.jsonl` exists and passes the Python and Rust witness verifiers.

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

## Quick verification

Run all configured checks from the repository root:

```bash
bash scripts/run_all_verification.sh
```

This checks the minimal witness file if present.  If it is missing but the known trace files are present, the script attempts to generate it first.

---

## Generate minimal witnesses from traces

```bash
python scripts/extract_minimal_witnesses.py \
  --trace traces/p29_r3_to_r7_repair_traces_strict.jsonl \
  --trace traces/p31_r3_to_r6_repair_traces_strict.jsonl \
  --out certificates/minimal_witnesses.jsonl \
  --strict
```

Then verify:

```bash
python scripts/verify_minimal_witnesses.py \
  certificates/minimal_witnesses.jsonl \
  --domain 29:3-7 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
```

Independent Rust verification:

```bash
cd rust-verifier
cargo run --release -- ../certificates/minimal_witnesses.jsonl \
  --domain 29:3-7 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
```

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

## Repository layout

```text
docs/            proof drafts, finite theorem docs, trust model, reduction ledger
scripts/         Python verification and extraction scripts
rust-verifier/   independent Rust witness verifier
traces/          JSONL trace universes, if committed
certificates/    witness JSONL and CSV certificate tables
logs/            saved validation logs, if committed
.github/         CI workflow
```

---

## Main documents

```text
docs/FINITE_THEOREM.md
docs/TRUST_MODEL.md
docs/REDUCTION_LEDGER.md
docs/FINITE_CERTIFICATE_RUNBOOK.md
```

Older analytic and SNS proof drafts remain research notes unless explicitly promoted into a verified theorem chain.
