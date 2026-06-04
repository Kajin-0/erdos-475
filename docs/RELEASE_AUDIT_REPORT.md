# Release Audit Report

**Date**: 2026-06-04
**Scope**: Finite-certificate verification infrastructure hardening
**Auditor**: Automated audit suite (T2–T14 checklist)

## Summary

| Check                           | Status  | Notes                                                                                                       |
| ------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------- |
| T1: Baseline inspection         | PASS    | Clean working tree, all expected files present                                                              |
| T2: Hardcoded Windows paths     | FIXED   | `batch_local_jsonl_manifest.py`, `parse_summary_only_artifacts.py` converted to argparse CLI                |
| T3: .gitignore hardening        | FIXED   | Added patterns for `*.jsonl.gz`, `local_artifacts/raw/`, `*_smoke.log`, venvs, tags, etc.                   |
| T4: Baseline verification       | PASS    | Python verifier: 247,416 rows, all domains covered. Rust verifier not run (no local toolchain).             |
| T5: Verification logic audit    | PASS    | Both verifiers implement identical checks (prime, canonical, subset, partial sums). No logic defects found. |
| T6: Schema validation           | CREATED | `scripts/validate_certificate_schema.py`                                                                    |
| T7: Canonical count audit       | CREATED | `scripts/audit_canonical_counts.py` (with LRU caching for performance)                                      |
| T8: Negative regression tests   | CREATED | `tests/` with 19 test cases across 3 test files                                                             |
| T9: Manifest completeness       | CREATED | `scripts/check_manifest_completeness.py` — found and fixed 4 missing entries in MANIFEST.required           |
| T10: Claim boundary consistency | CREATED | `scripts/check_claim_boundary_consistency.py` — PASS, all domains correctly mapped                          |
| T11: Release audit report       | CREATED | This document                                                                                               |
| T12: CI workflow update         | UPDATED | Added 5 new steps to `.github/workflows/verify.yml`                                                         |
| T13: Final verification         | PENDING | See below                                                                                                   |
| T14: Commit and push            | PENDING |                                                                                                             |

## Verification Results

### Python verifier

- 247,416 total witness rows verified
- Full canonical coverage confirmed for: 17:3, 19:3-5, 23:3-9, 29:3-8, 31:3-6
- PASS minimal witness verification

### Canonical count audit

- 22 domain/k combinations checked
- All expected vs. observed counts match
- PASS canonical count audit

### Claim boundary consistency

- 9 declared domains checked (5 tier_1a, 3 tier_1b_external_jsonl, 1 tier_1b_summary_digest)
- All tier_1a domains have committed certificate coverage
- All tier_1b domains have artifact ledger entries
- PASS claim boundary consistency check

### Schema validation

- `certificates/minimal_witnesses.jsonl` — 136,375 lines, all valid
- `certificates/witnesses_p29_b08.jsonl` — 111,041 lines, all valid
- `certificates/verified_domains.json` — valid schema, 9 domains declared
- PASS schema validation

### Negative regression tests

- 19/19 tests pass
- Covers: invalid JSON, missing fields, wrong types, non-prime p, duplicate B, non-canonical B, wrong final_order, repeated partial sums, duplicate witnesses, incomplete coverage, missing domains

## Known Issues

1. **MANIFEST.sha256 is stale**: 15 pre-existing hash mismatches (docs modified after hash generation) plus 2 from our script edits. Will regenerate before commit.
2. **Rust verifier not run locally**: No Rust toolchain available in this environment. CI will handle it.
3. **Tier 1b external domains**: p=29 b=9-15 and p=31 b=7-16 declared as `tier_1b_verified_external_jsonl`. These use artifacts outside Git. Their verification depends on artifact ledgers in `local_artifacts/batch_manifest/`. The JSONL files for these domains are not present in the repository.
4. **Tier 1b summary digest**: p=31 b=17 declared as `tier_1b_verified_summary_digest`. Summary-only verification log exists at `local_artifacts/summary_only/p31_b17_summary_only_pass.txt`.

## Recommendations

- Verify the 15 docs with stale hashes are intentional and regenerate MANIFEST.sha256 at release time
- Consider adding Rust CI job dependency on the new audit steps
- Document the external artifact provenance for tier_1b domains in more detail
