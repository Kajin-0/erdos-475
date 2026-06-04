# Release Audit Report

**Date**: 2026-06-04
**Starting commit**: `994fe3a`
**Final commit**: determined on push
**Branch**: `main`
**Scope**: Third hardening pass: manifest policy, verifier self-containment, CI direct strict gate, Makefile
**Auditor**: Automated audit suite (ci_classify.sh + 7 audit scripts + verifiers)

## Summary

| Check                            | Status | Notes                                                                                                             |
| -------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------- |
| CI docs-only classification      | PASS   | `scripts/ci_classify.sh` whitelists safe low-risk docs; trusted release files never classified as docs-only       |
| Schema validation (strict)       | PASS   | `--strict` mode: no untrusted fields, no bool-as-int, no empty files, valid domain artifact classes               |
| Canonical count audit            | PASS   | `--require-canonical`: 247,416 rows, all canonical, no duplicates, full domain coverage                           |
| Manifest completeness            | PASS   | `scripts/check_manifest_completeness.py`: all MANIFEST.required entries present                                   |
| Manifest policy coverage         | PASS   | `scripts/check_sha256_manifest_completeness.py`: 43 trusted files from policy, all covered, all hashes match      |
| Claim boundary consistency       | PASS   | `scripts/check_claim_boundary_consistency.py`: declared domains match certificate coverage                        |
| Overclaim detection              | PASS   | `scripts/check_no_overclaiming.py`: no unsafe phrases found in high-risk docs                                     |
| Python verifier (self-contained) | PASS   | 247,416 rows, all domains covered, canonical coverage confirmed; strict type checks (no bool, no string coercion) |
| Rust verifier                    | SKIP   | No Rust toolchain in this environment; CI handles it                                                              |
| Regression tests                 | PASS   | pytest tests pass                                                                                                 |
| Release gate                     | PASS   | `STRICT_CERT=1 bash scripts/run_all_verification.sh` passes                                                       |
| Makefile targets                 | PASS   | `make verify-strict`, `make validate-schema`, `make audit-counts`, `make check-manifest`, `make test` all pass    |

## Verification Results

### Python verifier (self-contained)

- 247,416 total witness rows verified
- Full canonical coverage confirmed for: 17:3, 19:3-5, 23:3-9, 29:3-8, 31:3-6
- Strict type checking: rejects bool-as-int, string coercion, floats
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

Counts verified by `scripts/audit_canonical_counts.py --require-canonical --domain ...`.
Expected counts are the number of orbits of the multiplicative action of F_p^\* on k-subsets of {1,...,p-1}.

### Manifest and SHA256 checks

- `check_manifest_completeness.py`: all MANIFEST.required entries present
- `check_sha256_manifest_completeness.py`: 43 trusted files from `release/manifest_policy.json`, all present in MANIFEST.sha256, no hash mismatches, no self-entry
- `make_manifest.sh` reads `release/manifest_policy.json` deterministically and fails if a trusted file is missing

### Overclaim detection

- 14 high-risk files scanned for 9 unsafe phrases
- 0 unsafe phrases detected
- 20+ safe-context patterns recognized
- PASS overclaim detection

### Regression tests

- pytest tests pass
- Covers: invalid JSON, missing fields, wrong types, non-prime p, bool-as-int, string coercion, duplicate B, non-canonical B, wrong final_order, repeated partial sums, duplicate witnesses, incomplete coverage, missing domains, extra domains

## Known Issues

1. **Rust verifier not run locally**: No Rust toolchain available in this environment. CI handles it. Python-only verification confirms all 247,416 rows pass.

2. **Tier 1b external domains**: p=29 b=9-15 and p=31 b=7-17 use artifacts outside Git. Their verification depends on external artifact ledgers. See `docs/EXTERNAL_ARTIFACT_VERIFICATION_MODEL.md` for per-class reproducibility details.

3. **CI status not confirmed from this run**: CI must be confirmed after push by checking the GitHub Actions workflow run for the pushed commit.

## Changes Made in This Hardening Pass

- Created `release/manifest_policy.json` — Canonical manifest policy defining trusted files, excluded paths, and required coverage; consumed by both `make_manifest.sh` and `check_sha256_manifest_completeness.py`
- Rewrote `scripts/make_manifest.sh` — Reads `release/manifest_policy.json`, deterministic git ls-files output, no self-entry, fails if trusted files missing
- Rewrote `scripts/check_sha256_manifest_completeness.py` — Reads `release/manifest_policy.json`, verifies all trusted files included, no forbidden files, no excluded paths, no self-entry
- Hardened `scripts/verify_minimal_witnesses.py` — Strict type checking: `isinstance(x, int) and not isinstance(x, bool)` for p, B, final_order; rejects bools, floats, strings; rejects non-object root JSON values; rejects untrusted optional fields
- Hardened `scripts/audit_canonical_counts.py` — Independent row validation: strict int checks, prime validation, B subset check, duplicate B rejection; added `--fail-extra-domains` flag; improved JSON output with per-domain expected/observed/missing/extra
- Added tests for: bool-as-p, bool-in-B, bool-in-final_order, string-p, string-in-B, string-in-final_order, root array, float-p, non-prime p, noncanonical B, duplicate canonical, extra domains, malformed JSON
- Updated `.github/workflows/verify.yml` — Primary gate is now `STRICT_CERT=1 bash scripts/run_all_verification.sh`; redundant `sha256sum -c` step removed; independent duplicate steps retained as cross-checks; `residue-audit-smoke` job depends on `finite-certificate` passing
- Updated `scripts/ci_classify.sh` — Trusted release files (README, Makefile, manifest_policy, etc.) never classified as docs-only
- Updated `MANIFEST.required` — Added `.gitignore`, `Makefile`, `release/manifest_policy.json`, `scripts/make_manifest.sh`, `scripts/artifact_tools/` entries
- Added `Makefile` — Targets: `verify`, `verify-strict`, `verify-python`, `verify-rust`, `validate-schema`, `audit-counts`, `check-manifest`, `check-claims`, `test`, `manifest`, `release-audit`
- Updated `README.md` — Fixed duplicate heading, added Makefile reference, made CI wording conservative, updated release audit suite table
- Updated `docs/RELEASE_HARDENING_CHECKLIST.md` — Hash locking section references policy-driven checker
- Updated `docs/EXTERNAL_ARTIFACT_VERIFICATION_MODEL.md` — Per-class reproducibility details

## Commands Run

```bash
# Schema validation
python scripts/validate_certificate_schema.py --strict \
  certificates/minimal_witnesses.jsonl \
  certificates/witnesses_p29_b08.jsonl
# PASS

# Domain JSON validation
python scripts/validate_certificate_schema.py --domains \
  certificates/verified_domains.json
# PASS

# Canonical count audit
python scripts/audit_canonical_counts.py \
  certificates/minimal_witnesses.jsonl \
  certificates/witnesses_p29_b08.jsonl \
  --domain 17:3 --domain 19:3-5 --domain 23:3-9 \
  --domain 29:3-8 --domain 31:3-6 \
  --require-canonical
# PASS

# Manifest checks
python scripts/check_manifest_completeness.py
# PASS
python scripts/check_sha256_manifest_completeness.py
# PASS

# Claim checks
python scripts/check_claim_boundary_consistency.py
# PASS
python scripts/check_no_overclaiming.py
# PASS

# Tests
python -m pytest tests/ -v
# PASS

# Strict release gate
STRICT_CERT=1 bash scripts/run_all_verification.sh
# PASS
```

## Recommendations

- Confirm CI status after push by checking GitHub Actions workflow runs
- Before external outreach, ensure `STRICT_CERT=1 bash scripts/run_all_verification.sh` passes
- Update external artifact ledgers if Tier 1b domains change

## Claim Boundary Reminder

This audit report concerns finite-certificate verification infrastructure only. It does not claim:

- A complete proof of Erdős 475
- That the analytic residue is contained in the verified finite domain
- That Tier 1b external evidence is equivalent to committed CI verification
- That the problem is solved or a final proof exists

The repository remains a finite-certificate verification workspace and proof-engineering project.
