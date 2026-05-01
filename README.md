# Erdos 475 Certified Finite Complement Check

This repository contains a computer-assisted certificate package for finite complement cases in Erdos Problem 475, also known as Graham's rearrangement problem.

## Certified result

The package works with complements

```text
B = F_p^* \ A
```

and verifies the following complement domain, modulo nonzero multiplicative scaling:

```text
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

Equivalently, the original set sizes are:

```text
p = 29, |A| = 21..25
p = 31, |A| = 24..27
```

## Status

This repository verifies the finite complement cases above. It does not independently prove the external analytic reduction from the full Erdos 475 problem to these finite cases.

If the known analytic reductions leave exactly these complement cases, then this repository completes that finite check.

## Main proof

See:

```text
docs/proof.tex
```

A compiled PDF may also be included as:

```text
docs/proof.pdf
```

## Independent validation

Run all commands from the repository root.

### 1. Trace semantics

This confirms that `B` is the complement set and that the ordered set is `A = F_p^* \ B`.

```bash
python scripts/verify_erdos475_trace_semantics.py \
  traces/p29_r3_to_r7_repair_traces_strict.jsonl \
  traces/p31_r3_to_r6_repair_traces_strict.jsonl
```

Expected:

```text
VERDICT: PASS
```

### 2. Certificate verification

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

Expected:

```text
TOTAL ok=198631 fail=0
VERDICT: PASS
```

### 3. Coverage audit

```bash
python scripts/audit_erdos475_trace_coverage.py \
  traces/p29_r3_to_r7_repair_traces_strict.jsonl \
  traces/p31_r3_to_r6_repair_traces_strict.jsonl \
  --summary-csv certificates/trace_coverage_summary.csv
```

Expected in canonical-scaling mode:

```text
coverage=100.00%
missing=0
extra=0
```

## Repository layout

```text
docs/          proof draft, manifest, validation protocol
scripts/       independent verification scripts
traces/        JSONL trace universes
certificates/  CSV certificate tables
logs/          saved validation logs
```

## Remaining mathematical task

The remaining proof obligation is to verify the external reduction boundary:

```text
Do known analytic reductions leave exactly
p = 29, |B| = 3..7 and p = 31, |B| = 3..6?
```

See:

```text
docs/reduction_audit.md
```
