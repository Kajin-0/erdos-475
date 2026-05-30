# Finite frontier status

This document summarizes the current finite-certificate frontier represented by committed and external artifacts.

## Claim boundary

This is a finite-artifact status document only.

It does not claim a complete proof of Erdős 475. It does not claim that the analytic residue has been fully reduced to the finite domains listed here.

## Committed CI-verified finite certificates

The repository currently has committed JSONL certificates checked by both the Python and Rust verifiers in CI for:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..8
p = 31, |B| = 3..6
```

Current committed CI-verified total:

```text
247,416 canonical instances
```

## External/hash-backed finite-certificate evidence

The external artifact ledger records additional large artifacts for:

```text
p = 29, |B| = 9..15
p = 31, |B| = 7..17
```

The `p = 29, |B| = 8` source artifact is also recorded in the external ledger, but that domain is already committed separately as `certificates/witnesses_p29_b08.jsonl`.

Additional external evidence beyond the committed CI-verified total:

```text
p = 29, |B| = 9..15: 6,676,265 canonical instances
p = 31, |B| = 7..17: 29,295,586 canonical instances
```

Combined external evidence beyond committed CI-verified total:

```text
35,971,851 canonical instances
```

Committed CI-verified plus external/hash-backed finite evidence:

```text
36,219,267 canonical instances
```

## Full source-side frontier represented in the ledger

If one also counts the source-side `p = 29, |B| = 8` artifact already promoted into Git, the full source-side frontier represented by the external ledger is:

```text
p = 29, |B| = 8..15: 6,787,306 canonical instances
p = 31, |B| = 7..17: 29,295,586 canonical instances
```

Total source-side frontier represented by external artifacts:

```text
36,082,892 canonical instances
```

## Status by domain

| Domain | Canonical instances | Status |
|---:|---:|---|
| 17:3 | 35 | committed CI verified |
| 19:3..5 | 694 | committed CI verified |
| 23:3..9 | 49,913 | committed CI verified |
| 29:3..7 | 60,118 | committed CI verified |
| 29:8 | 111,041 | committed CI verified; source artifact also recorded externally |
| 29:9..15 | 6,676,265 | external JSONL hash-backed evidence |
| 31:3..6 | 25,615 | committed CI verified |
| 31:7..16 | 25,303,591 | external JSONL hash-backed evidence |
| 31:17 | 3,991,995 | summary-only deterministic digest evidence |

## Interpretation

The finite-certificate evidence is now substantial, but the theorem-level task remains separate.

The central remaining mathematical bridge is:

```text
Show that every analytic residue case required for Erdős 475 is contained in the verified finite frontier.
```

Until that bridge is proved, the repository should continue to describe itself as a finite-certificate verification workspace and proof-engineering project, not as a complete proof.
