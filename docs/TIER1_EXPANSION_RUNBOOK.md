# Tier 1 expansion runbook

This runbook describes how to promote lower-trust finite domains into release-grade Tier 1 finite certificate artifacts.

The immediate target is to harden small-prime direct-witness domains before presenting the repository externally.

## 1. Current hardened Tier 1 domain

The current strict certificate covers:

```text
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

with:

```text
certificates/minimal_witnesses.jsonl
MANIFEST.sha256
Python verifier pass
Rust verifier pass
```

## 2. Next Tier 1 expansion target

The next target is:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
```

These are currently lower-trust domains in the verified-domain ledger. They should become Tier 1 only after direct witness rows are committed, hash-locked, and checked by both verifiers.

## 3. Generate direct witnesses

Run from the repository root:

```bash
python3 scripts/generate_direct_witnesses.py \
  --domain 17:3 \
  --domain 19:3-5 \
  --domain 23:3-9 \
  --out certificates/direct_witnesses_small_primes.jsonl \
  --max-trials 1000000 \
  --resume \
  --progress-every 1000
```

The generator is deterministic by default. It uses randomized search with a seed derived from `(p,B)`.

If a hard case fails, rerun with a different deterministic salt:

```bash
python3 scripts/generate_direct_witnesses.py \
  --domain 23:3-9 \
  --out certificates/direct_witnesses_small_primes.jsonl \
  --max-trials 2000000 \
  --resume \
  --salt 1 \
  --progress-every 1000
```

## 4. Verify direct-witness file independently

```bash
python3 scripts/verify_minimal_witnesses.py \
  certificates/direct_witnesses_small_primes.jsonl \
  --domain 17:3 \
  --domain 19:3-5 \
  --domain 23:3-9 \
  --require-canonical \
  --require-coverage
```

Rust:

```bash
cd rust-verifier
cargo run --release -- ../certificates/direct_witnesses_small_primes.jsonl \
  --domain 17:3 \
  --domain 19:3-5 \
  --domain 23:3-9 \
  --require-canonical \
  --require-coverage
cd ..
```

## 5. Merge into strict certificate

Only after both independent verifiers pass:

```bash
cat certificates/minimal_witnesses.jsonl \
    certificates/direct_witnesses_small_primes.jsonl \
  > certificates/minimal_witnesses.expanded.jsonl

mv certificates/minimal_witnesses.expanded.jsonl certificates/minimal_witnesses.jsonl
```

Then update strict verification domains in:

```text
scripts/run_all_verification.sh
.github/workflows/verify.yml
```

Expected domains after promotion:

```text
17:3
19:3-5
23:3-9
29:3-7
31:3-6
```

## 6. Regenerate manifest

```bash
bash scripts/make_manifest.sh
python scripts/check_sha256_manifest_completeness.py
```

## 7. Strict verification

```bash
STRICT_CERT=1 bash scripts/run_all_verification.sh
```

Rust:

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
cd ..
```

## 8. Promotion rule

A finite domain becomes Tier 1 only when all of the following are true:

```text
1. witness rows are committed;
2. every row is independently verified;
3. canonical coverage is complete;
4. MANIFEST.sha256 covers the witness file and verifier sources;
5. CI enforces the expanded domain;
6. docs/VERIFIED_DOMAIN.md and certificates/verified_domains.json agree.
```

Until then, it remains lower-trust evidence.
