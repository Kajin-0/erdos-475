# Research tooling inventory

This document records the curated local research tools promoted from the scratch Erdos 475 working folder.

The goal is to keep the main repository clean. Tools are promoted only if they support finite certificate verification, trace coverage auditing, reproducible large-artifact hashing, summary-only witness generation, strict repair-trace provenance, or extraction of reusable proof templates.

## Current promoted tools

| Path | Role | Status |
|---|---|---|
| scripts/artifact_tools/make_jsonl_manifest.py | Hashes local JSONL artifacts and writes jsonl_manifest_sha256.txt with SHA256, size, and filename. | artifact utility |
| scripts/artifact_tools/generate_witness_summary_only.py | Generates and validates witnesses over canonical complement representatives without writing large JSONL files; emits per-class and aggregate SHA256 digests. | large-artifact utility |

## Recommended next candidates

These are useful, but should be promoted in separate small PRs only when needed.

| Candidate | Reason |
|---|---|
| audit_erdos475_trace_coverage.py | Audits whether trace files cover the expected B-set universe under contains_one or canonical_scaling. |
| trace_erdos475_repairs_strict.py | Strict repair-trace generator and trace verifier. Starts from a full valid ordering Q_p, deletes B, repairs with bounded block moves, and records the actual move sequence. |
| verify_erdos475_certificates.py | Strong descent and escape CSV verifier from the scratch folder. Promote only when related CSV artifacts are also in scope. |

## Deliberately not promoted

The older uploaded verify_erdos475_certificate.py was not promoted because the repository already has the stronger active verifier scripts/verify_minimal_witnesses.py.

The current verifier checks canonical representatives, declared domain coverage, and the active finite-certificate schema. The older script only checks each JSONL record with fields p, B, and order, so it is useful historically but weaker than the current production verifier.

The many exploratory probe and early analyze scripts remain local scratch tools unless a future theorem step requires them explicitly.

## Clean-repo policy

A scratch script should enter the repository only if it is needed to reproduce a stated finite-certificate claim, audit a declared finite domain, hash external artifacts, or extract a reusable proof template. Otherwise it should remain outside the clean repo.
