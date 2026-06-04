# Release Audit Report

**Date**: 2026-06-04
**Branch**: `main` at `6748fb3`
**Scope**: Second hardening pass for finite-certificate verification infrastructure
**Auditor**: Automated audit suite (ci_classify.sh + 6 audit scripts + verifiers)

## Summary

| Check                          | Status | Notes                                                                                                                 |
| ------------------------------ | ------ | --------------------------------------------------------------------------------------------------------------------- |
| CI docs-only classification    | PASS   | `scripts/ci_classify.sh` whitelists safe low-risk docs; verification jobs skipped for doc-only changes                |
| Schema validation (strict)     | PASS   | `--strict` mode: no untrusted fields, no bool-as-int, no empty files, valid domain artifact classes                   |
| Canonical count audit          | PASS   | `--require-canonical`: 247,416 rows, all canonical, no duplicates, full domain coverage                               |
| Manifest completeness          | PASS   | `scripts/check_manifest_completeness.py`: all MANIFEST.required entries present                                       |
| SHA256 manifest coverage       | PASS   | `scripts/check_sha256_manifest_completeness.py`: 38 trusted files, all covered, all hashes match                      |
| Claim boundary consistency     | PASS   | `scripts/check_claim_boundary_consistency.py`: declared domains match certificate coverage                            |
| Overclaim detection            | PASS   | `scripts/check_no_overclaiming.py`: no unsafe phrases found in 14 high-risk docs                                      |
| Python verifier                | PASS   | 247,416 rows, all domains covered, canonical coverage confirmed                                                       |
| Rust verifier                  | SKIP   | No Rust toolchain in this environment; CI handles it                                                                  |
| Regression tests               | PASS   | 19/19 pytest tests pass                                                                                               |
| .gitignore hardening           | PASS   | Patterns for `logs/*.jsonl`, `*.tmp`, `local_artifacts/**/*.{jsonl,zip,tar,tar.gz}`, `logs/*.log`                     |
| Literature notation correction | PASS   | `data/literature_coverage.json` fixed: "F_p\*" → "additive cyclic group F_p, with A subset F_p \ {0}"                 |
| Artifact manifest scripts      | PASS   | `batch_local_jsonl_manifest.py` and `parse_summary_only_artifacts.py` improved with `--allow-empty`/`--allow-unknown` |

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
|      19:3 |          46 |          46 | PASS         |
|      19:4 |         172 |         172 | PASS         |
|      19:5 |         476 |         476 | PASS         |
|      23:3 |          70 |          70 | PASS         |
|      23:4 |         335 |         335 | PASS         |
|      23:5 |       1,197 |       1,197 | PASS         |
|      23:6 |       3,399 |       3,399 | PASS         |
|      23:7 |       7,752 |       7,752 | PASS         |
|      23:8 |      14,550 |      14,550 | PASS         |
|      23:9 |      22,610 |      22,610 | PASS         |
|      29:3 |         117 |         117 | PASS         |
|      29:4 |         735 |         735 | PASS         |
|      29:5 |       3,510 |       3,510 | PASS         |
|      29:6 |      13,468 |      13,468 | PASS         |
|      29:7 |      42,288 |      42,288 | PASS         |
|      29:8 |     111,041 |     111,041 | PASS         |
|      31:3 |         136 |         136 | PASS         |
|      31:4 |         917 |         917 | PASS         |
|      31:5 |       4,751 |       4,751 | PASS         |
|      31:6 |      19,811 |      19,811 | PASS         |
| **Total** | **247,416** | **247,416** | **ALL PASS** |

Counts verified by `scripts/audit_canonical_counts.py --require-canonical --domain ...`. Expected counts are the number of orbits of the multiplicative action of F_p^\* on k-subsets of {1,...,p-1}.

### Manifest and SHA256 checks

- `check_manifest_completeness.py`: 54 entries in MANIFEST.required, all present
- `check_sha256_manifest_completeness.py`: 38 trusted files, all present in MANIFEST.sha256 (494 entries), no hash mismatches (MANIFEST.sha256 has no self-entry)

### Overclaim detection

- 14 high-risk files scanned for 9 unsafe phrases
- 0 unsafe phrases detected
- 20+ safe-context patterns recognized (e.g., "claims not made", "does not claim", "not a complete proof", "unsafe claims", "avoid language such as", etc.)
- Context window includes 5 preceding lines for section-header detection
- PASS overclaim detection

### Regression tests

- 19/19 tests pass
- Covers: invalid JSON, missing fields, wrong types, non-prime p, duplicate B, non-canonical B, wrong final_order, repeated partial sums, duplicate witnesses, incomplete coverage, missing domains

## Known Issues

1. **Rust verifier not run locally**: No Rust toolchain available in this environment. CI handles it. Python-only verification confirms all 247,416 rows pass.

2. **Tier 1b external domains**: p=29 b=9-15 and p=31 b=7-16 declared as `tier_1b_verified_external_jsonl`. p=31 b=17 declared as `tier_1b_verified_summary_digest`. These use artifacts outside Git. Their verification depends on artifact ledgers in `local_artifacts/batch_manifest/`. The JSONL files for these domains are not present in the repository.

3. **Strict mode schema validation now fails on untrusted fields** (changed from WARN to ERROR in this patch). This is intentional for release-grade verification.

## Changes Made in This Hardening Pass

- Created `scripts/ci_classify.sh` — CI docs-only classification with whitelist
- Created `scripts/check_sha256_manifest_completeness.py` — SHA256 manifest coverage checker
- Created `scripts/check_no_overclaiming.py` — Overclaim scanner for 14 high-risk docs with safe-context detection
- Rewrote `scripts/validate_certificate_schema.py` — Added `--strict`, `--allow-empty`, `--allow-unknown-class`, bool rejection; strict mode now **fails** on untrusted fields (not just warns)
- Rewrote `scripts/audit_canonical_counts.py` — Tracks noncanonical/malformed/duplicate rows, `--require-canonical`, `--json`
- Updated `.github/workflows/verify.yml` — Uses `scripts/ci_classify.sh`, new audit steps, pytest installation
- Updated `scripts/run_all_verification.sh` — Strict mode runs full audit suite; P29_B8_CERT existence checked before audit calls
- Updated `scripts/artifact_tools/batch_local_jsonl_manifest.py` — Input validation, `--allow-empty`, `--allow-unknown`
- Updated `scripts/artifact_tools/parse_summary_only_artifacts.py` — Same improvements
- Updated `.gitignore` — Added `logs/*.jsonl`, `logs/*.log`, `logs/*.tmp`, `*.tmp`, `local_artifacts/**/*.{jsonl,zip,tar,tar.gz}`
- Fixed `data/literature_coverage.json` — Corrected notation for Costa-Della Fiore-Fontana-Vena entry
- Updated `MANIFEST.required` — Added new scripts
- Updated `MANIFEST.sha256` — Regenerated (494 entries, no self-entry)
- Updated `README.md` — Added audit suite documentation
- Updated `docs/RELEASE_HARDENING_CHECKLIST.md` — Added schema, canonical, manifest, SHA256, overclaim items

## Recommendations

- Run `STRICT_CERT=1 bash scripts/run_all_verification.sh` as final gate before external outreach
- Ensure CI passes with the updated `.github/workflows/verify.yml`
- Update external artifact ledgers if Tier 1b domains change

## Claim Boundary Reminder

This audit report concerns finite-certificate verification infrastructure only. It does not claim:

- A complete proof of Erdős 475
- That the analytic residue is contained in the verified finite domain
- That Tier 1b external evidence is equivalent to committed CI verification

The repository remains a finite-certificate verification workspace and proof-engineering project.
