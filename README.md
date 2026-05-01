# Erdős 475 Certified Finite Complement Check

This repository contains a certified finite-check package for complement cases of Erdős Problem 475.

## Result certified here

The package verifies large-set cases by working with small complements:

```text
B = F_p^* \ A
```

The certified complement domain is:

```text
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

Equivalently, the original Erdős set sizes are:

```text
p = 29, |A| = 21..25
p = 31, |A| = 24..27
```

## Main proof

See:

```text
docs/proof.tex
```

## Independent validation

Run these from the repository root.

### 1. Trace semantics

```bash
python scripts/verify_erdos475_trace_semantics.py   traces/p29_r3_to_r7_repair_traces_strict.jsonl   traces/p31_r3_to_r6_repair_traces_strict.jsonl
```

Expected:

```text
VERDICT: PASS
```

### 2. Certificate verification

```bash
python scripts/verify_erdos475_certificates.py   --trace-files     traces/p29_r3_to_r7_repair_traces_strict.jsonl     traces/p31_r3_to_r6_repair_traces_strict.jsonl   --nonatomic-csv     certificates/p29_nonatomic_descent_full.csv     certificates/p31_nonatomic_descent_full.csv   --onecollision-csv     certificates/p29_one_collision_deep_full.csv     certificates/p31_one_collision_deep_full.csv   --atomic-instances certificates/atomic_local_cert_instances.csv   --atomic-certs certificates/atomic_local_certs.csv   --require-onecollision-intermediates   --strict-csv
```

Expected:

```text
TOTAL ok=198631 fail=0
VERDICT: PASS
```

### 3. Coverage audit

```bash
python scripts/audit_erdos475_trace_coverage.py   traces/p29_r3_to_r7_repair_traces_strict.jsonl   traces/p31_r3_to_r6_repair_traces_strict.jsonl   --summary-csv certificates/trace_coverage_summary.csv
```

Expected in canonical-scaling mode:

```text
coverage=100.00%
missing=0
extra=0
```

## Scope

This repository verifies the finite complement cases listed above. To claim a complete solution of Erdős Problem 475, combine this certificate with the external analytic reduction showing these are exactly the remaining finite cases.
