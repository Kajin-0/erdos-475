# Validation Protocol

This document gives the exact commands needed to validate the Erdős 475 finite complement certificate.

Run all commands from the repository root.

## 1. Trace semantics

This verifies that the trace variable `B` is the complement/defect set and that the actual ordered set is:

```text
A = F_p^* \ B
```

Command:

```bash
python scripts/verify_erdos475_trace_semantics.py   traces/p29_r3_to_r7_repair_traces_strict.jsonl   traces/p31_r3_to_r6_repair_traces_strict.jsonl
```

Expected result:

```text
VERDICT: PASS
```

This check confirms:

- `Q_p` is a permutation of `F_p^*`.
- `initial_order = Q_p \ B`.
- `final_order` is a permutation of `initial_order`.
- `final_partial_sums` are correctly computed.
- `final_partial_sums` are pairwise distinct.

## 2. Certificate verification

This independently checks every claimed descent or escape certificate.

Command:

```bash
python scripts/verify_erdos475_certificates.py   --trace-files     traces/p29_r3_to_r7_repair_traces_strict.jsonl     traces/p31_r3_to_r6_repair_traces_strict.jsonl   --nonatomic-csv     certificates/p29_nonatomic_descent_full.csv     certificates/p31_nonatomic_descent_full.csv   --onecollision-csv     certificates/p29_one_collision_deep_full.csv     certificates/p31_one_collision_deep_full.csv   --atomic-instances certificates/atomic_local_cert_instances.csv   --atomic-certs certificates/atomic_local_certs.csv   --require-onecollision-intermediates   --strict-csv
```

Expected result:

```text
TOTAL ok=198631 fail=0
VERDICT: PASS
```

The verifier recomputes `E`, `P`, `L`, and `Phi=(E,P,L)` from scratch.

## 3. Coverage audit

This checks that all canonical multiplicative-scaling representatives in the audited complement domain are present.

Command:

```bash
python scripts/audit_erdos475_trace_coverage.py   traces/p29_r3_to_r7_repair_traces_strict.jsonl   traces/p31_r3_to_r6_repair_traces_strict.jsonl   --summary-csv certificates/trace_coverage_summary.csv
```

Expected canonical-scaling result for every audited `(p, |B|)` pair:

```text
coverage=100.00%
missing=0
extra=0
```

## 4. Save logs

Save outputs to:

```text
logs/trace_semantics_pass.txt
logs/certificate_verifier_pass.txt
logs/coverage_audit_pass.txt
```

PowerShell example:

```powershell
python scripts/verify_erdos475_trace_semantics.py `
  traces/p29_r3_to_r7_repair_traces_strict.jsonl `
  traces/p31_r3_to_r6_repair_traces_strict.jsonl `
  | Tee-Object logs/trace_semantics_pass.txt
```

Repeat similarly for the certificate verifier and coverage audit.
