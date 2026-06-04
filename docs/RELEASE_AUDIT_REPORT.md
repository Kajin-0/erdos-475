# Release Audit Report

**Date**: 2026-06-04
**Scope**: Second hardening pass for finite-certificate verification infrastructure
**Auditor**: Automated audit suite (ci_classify.sh + 6 audit scripts + verifiers)

## Summary

| Check                          | Status  | Notes                                                                                                       |
| ------------------------------ | ------- | ----------------------------------------------------------------------------------------------------------- |
| CI docs-only classification    | PASS    | `scripts/ci_classify.sh` whitelists safe low-risk docs; verification jobs skipped for doc-only changes      |
| Schema validation (strict)     | PASS    | `--strict` mode: no untrusted fields, no bool-as-int, no empty files, valid domain artifact classes         |
| Canonical count audit          | PASS    | `--require-canonical`: 247,416 rows, all canonical, no duplicates, full domain coverage                     |
| Manifest completeness          | PASS    | `scripts/check_manifest_completeness.py`: all MANIFEST.required entries present                             |
| SHA256 manifest coverage       | PASS    | `scripts/check_sha256_manifest_completeness.py`: all trusted files covered in MANIFEST.sha256               |
| Claim boundary consistency     | PASS    | `scripts/check_claim_boundary_consistency.py`: declared domains match certificate coverage                  |
| Overclaim detection            | PASS    | `scripts/check_no_overclaiming.py`: no unsafe phrases found in 14 high-risk docs                            |
| Python verifier                | PASS    | 247,416 rows, all domains covered, canonical coverage confirmed                                             |
| Rust verifier                  | SKIP    | No Rust toolchain in this environment; CI handles it                                                        |
| Negative regression tests      | PASS    | 19/19 pytest tests pass                                                                                     |
| Hash manifest integrity        | PENDING | `sha256sum -c MANIFEST.sha256` to run before release commit                                                 |
| .gitignore hardening           | PASS    | Patterns added for `logs/*.jsonl`, `*.tmp`                                                                  |
| Literature notation correction | PASS    | `data/literature_coverage.json` fixed: "F_p\*" → "additive cyclic group F_p, with A subset F_p \ {0}"       |
| Artifact manifest scripts      | PASS    | `batch_local_jsonl_manifest.py` and `parse_summary_only_artifacts.py` improved with --allow-empty/--unknown |

## Verification Results

### Python verifier

- 247,416 total witness rows verified
- Full canonical coverage confirmed for: 17:3, 19:3-5, 23:3-9, 29:3-8, 31:3-6
- PASS minimal witness verification

### Schema validation (strict mode)

- `certificates/minimal_witnesses.jsonl` — 136,375 lines, all valid
- `certificates/witnesses_p29_b08.jsonl` — 111,041 lines, all valid
- `certificates/verified_domains.json` — valid schema, 9 domains declared with valid artifact classes
- No untrusted fields (partial_sums, trace_status, etc.) detected
- No bool-as-int values detected
- PASS strict schema validation

### Canonical count audit

|    Domain |    Expected |    Observed | Status       |
| --------: | ----------: | ----------: | :----------- |
|      17:3 |          35 |          35 | PASS         |
|      19:3 |          97 |          97 | PASS         |
|      19:4 |         291 |         291 | PASS         |
|      19:5 |         306 |         306 | PASS         |
|      23:3 |         253 |         253 | PASS         |
|      23:4 |       1,012 |       1,012 | PASS         |
|      23:5 |       2,530 |       2,530 | PASS         |
|      23:6 |       4,675 |       4,675 | PASS         |
|      23:7 |       7,150 |       7,150 | PASS         |
|      23:8 |      10,725 |      10,725 | PASS         |
|      23:9 |      23,568 |      23,568 | PASS         |
|      29:3 |         819 |         819 | PASS         |
|      29:4 |       4,095 |       4,095 | PASS         |
|      29:5 |      12,285 |      12,285 | PASS         |
|      29:6 |      27,300 |      27,300 | PASS         |
|      29:7 |      15,619 |      15,619 | PASS         |
|      29:8 |     111,041 |     111,041 | PASS         |
|      31:3 |       1,015 |       1,015 | PASS         |
|      31:4 |       6,090 |       6,090 | PASS         |
|      31:5 |      10,150 |      10,150 | PASS         |
|      31:6 |       8,360 |       8,360 | PASS         |
| **Total** | **247,416** | **247,416** | **ALL PASS** |

### Manifest and SHA256 checks

- `check_manifest_completeness.py`: 53 entries in MANIFEST.required, all present
- `check_sha256_manifest_completeness.py`: 37 trusted files checked against MANIFEST.sha256
- `sha256sum -c MANIFEST.sha256`: PENDING (will regenerate at release commit time)

### Overclaim detection

- 14 high-risk files scanned for 9 unsafe phrases
- 0 unsafe phrases detected
- 20+ safe-context patterns recognized (e.g., "claims not made", "does not claim", "not a complete proof", etc.)
- PASS overclaim detection

### Negative regression tests

- 19/19 tests pass
- Covers: invalid JSON, missing fields, wrong types, non-prime p, duplicate B, non-canonical B, wrong final_order, repeated partial sums, duplicate witnesses, incomplete coverage, missing domains

## Known Issues

1. **MANIFEST.sha256 is stale**: Pre-existing hash mismatches from docs modified after hash generation plus changes from this session. Will regenerate before release commit.

2. **Rust verifier not run locally**: No Rust toolchain available in this environment. CI will handle it. Python-only verification confirms all 247,416 rows pass.

3. **Tier 1b external domains**: p=29 b=9-15 and p=31 b=7-16 declared as `tier_1b_verified_external_jsonl`. p=31 b=17 declared as `tier_1b_verified_summary_digest`. These use artifacts outside Git. Their verification depends on artifact ledgers in `local_artifacts/batch_manifest/`. The JSONL files for these domains are not present in the repository.

4. **tests/**init**.py is empty**: This is intentional — it marks `tests/` as a Python package. Not a placeholder issue.

## Changes Made in This Hardening Pass

- Created `scripts/ci_classify.sh` — CI docs-only classification with whitelist
- Created `scripts/check_sha256_manifest_completeness.py` — SHA256 manifest coverage checker
- Created `scripts/check_no_overclaiming.py` — Overclaim scanner for 14 high-risk docs
- Rewrote `scripts/validate_certificate_schema.py` — Added `--strict`, `--allow-empty`, `--allow-unknown-class`, bool rejection
- Rewrote `scripts/audit_canonical_counts.py` — Tracks noncanonical/malformed/duplicate rows, `--require-canonical`, `--json`
- Updated `.github/workflows/verify.yml` — Uses `scripts/ci_classify.sh`, new audit steps, pytest installation
- Updated `scripts/run_all_verification.sh` — Strict mode runs full audit suite
- Updated `scripts/artifact_tools/batch_local_jsonl_manifest.py` — Input validation, `--allow-empty`, `--allow-unknown`
- Updated `scripts/artifact_tools/parse_summary_only_artifacts.py` — Same improvements
- Updated `.gitignore` — Added `logs/*.jsonl`, `*.tmp`
- Fixed `data/literature_coverage.json` — Corrected notation for Costa-Della Fiore-Fontana-Vena entry
- Updated `MANIFEST.required` — Added new scripts
- Updated `README.md` — Added audit suite documentation
- Updated `docs/RELEASE_HARDENING_CHECKLIST.md` — Added schema, canonical, manifest, SHA256, overclaim items

## Recommendations

- Regenerate MANIFEST.sha256 before release commit
- Update external artifact ledgers if Tier 1b domains change
- Run `STRICT_CERT=1 bash scripts/run_all_verification.sh` as final gate before external outreach
- Ensure CI passes with the updated `.github/workflows/verify.yml`

## Claim Boundary Reminder

This audit report concerns finite-certificate verification infrastructure only. It does not claim:

- A complete proof of Erdős 475
- That the analytic residue is contained in the verified finite domain
- That Tier 1b external evidence is equivalent to committed CI verification

The repository remains a finite-certificate verification workspace and proof-engineering project.
