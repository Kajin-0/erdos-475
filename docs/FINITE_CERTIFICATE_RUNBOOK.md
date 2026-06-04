# Finite certificate runbook

This is the operational checklist for producing and verifying the finite certificate theorem.

The target artifact is:

```text
certificates/minimal_witnesses.jsonl
```

Each row should contain:

```json
{"p":29,"B":[1,2,5],"final_order":[...]}
```

---

## 1. Generate minimal witnesses from traces

If the strict trace files are present, run:

```bash
python scripts/extract_minimal_witnesses.py \
  --trace traces/p29_r3_to_r7_repair_traces_strict.jsonl \
  --trace traces/p31_r3_to_r6_repair_traces_strict.jsonl \
  --out certificates/minimal_witnesses.jsonl \
  --strict
```

If this extracts zero rows, inspect the trace schema and update the field paths in:

```text
scripts/extract_minimal_witnesses.py
```

The extractor is not trusted proof logic. It is only a converter from rich traces to the minimal witness format.

---

## 2. Verify witnesses with Python

Run:

```bash
python scripts/verify_minimal_witnesses.py \
  certificates/minimal_witnesses.jsonl \
  --domain 29:3-7 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
```

This recomputes:

```text
prime status;
B subset F_p^*;
canonical scaling representative;
final_order = F_p^* \ B;
partial sums mod p;
pairwise distinctness;
complete canonical coverage.
```

---

## 3. Verify witnesses with Rust

Run:

```bash
cd rust-verifier
cargo run --release -- ../certificates/minimal_witnesses.jsonl \
  --domain 29:3-7 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
```

This is an independent implementation of the same trusted kernel.

---

## 4. Run all configured verification

From repo root:

```bash
bash scripts/run_all_verification.sh
```

This will generate `minimal_witnesses.jsonl` from known trace names if the witness file is missing and the traces exist.

---

## 5. Generate manifest

After witnesses and verification artifacts are stable:

```bash
bash scripts/make_manifest.sh
```

Then verify the manifest:

```bash
python scripts/check_sha256_manifest_completeness.py
```

Commit the manifest only after the certificate files are final for the declared finite theorem.

---

## 6. GitHub Actions

The CI workflow runs:

```text
Python finite certificate verification
Rust independent verifier, if certificates/minimal_witnesses.jsonl is present
```

If `minimal_witnesses.jsonl` is not committed but trace files are committed, the Python runner attempts extraction first.

---

## 7. Claim boundary

Allowed after both Python and Rust pass:

```text
The declared finite complement domains are certified by direct witness verification.
```

Not allowed until `docs/REDUCTION_LEDGER.md` is complete:

```text
The full Erdős 475 theorem is proved.
```
