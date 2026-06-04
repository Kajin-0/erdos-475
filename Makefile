# Makefile for finite-certificate verification
# All targets run from the repository root.

SHELL := /usr/bin/env bash
PYTHON := python3

.PHONY: verify verify-strict verify-python verify-rust validate-schema audit-counts
.PHONY: check-manifest check-claims test manifest release-audit


verify:
	bash scripts/run_all_verification.sh

verify-strict:
	STRICT_CERT=1 bash scripts/run_all_verification.sh

verify-python:
	$(PYTHON) scripts/verify_minimal_witnesses.py \
		certificates/minimal_witnesses.jsonl \
		certificates/witnesses_p29_b08.jsonl \
		--domain 17:3 --domain 19:3-5 --domain 23:3-9 \
		--domain 29:3-8 --domain 31:3-6 \
		--require-canonical --require-coverage

verify-rust:
	cd rust-verifier && cargo run --release -- \
		../certificates/minimal_witnesses.jsonl \
		../certificates/witnesses_p29_b08.jsonl \
		--domain 17:3 --domain 19:3-5 --domain 23:3-9 \
		--domain 29:3-8 --domain 31:3-6 \
		--require-canonical --require-coverage

validate-schema:
	$(PYTHON) scripts/validate_certificate_schema.py --strict \
		certificates/minimal_witnesses.jsonl \
		certificates/witnesses_p29_b08.jsonl
	$(PYTHON) scripts/validate_certificate_schema.py --domains \
		certificates/verified_domains.json

audit-counts:
	$(PYTHON) scripts/audit_canonical_counts.py \
		certificates/minimal_witnesses.jsonl \
		certificates/witnesses_p29_b08.jsonl \
		--domain 17:3 --domain 19:3-5 --domain 23:3-9 \
		--domain 29:3-8 --domain 31:3-6 \
		--require-canonical

check-manifest:
	$(PYTHON) scripts/check_manifest_completeness.py
	$(PYTHON) scripts/check_sha256_manifest_completeness.py

check-claims:
	$(PYTHON) scripts/check_claim_boundary_consistency.py
	$(PYTHON) scripts/check_no_overclaiming.py

test:
	$(PYTHON) -m pytest tests/ -v || $(PYTHON) -m unittest discover tests -v

manifest:
	bash scripts/make_manifest.sh

release-audit:
	@echo "=== Schema validation ===" && \
	$(PYTHON) scripts/validate_certificate_schema.py --strict \
		certificates/minimal_witnesses.jsonl \
		certificates/witnesses_p29_b08.jsonl && \
	echo "=== Domain JSON validation ===" && \
	$(PYTHON) scripts/validate_certificate_schema.py --domains \
		certificates/verified_domains.json && \
	echo "=== Canonical count audit ===" && \
	$(PYTHON) scripts/audit_canonical_counts.py \
		certificates/minimal_witnesses.jsonl \
		certificates/witnesses_p29_b08.jsonl \
		--domain 17:3 --domain 19:3-5 --domain 23:3-9 \
		--domain 29:3-8 --domain 31:3-6 \
		--require-canonical && \
	echo "=== Manifest checks ===" && \
	$(PYTHON) scripts/check_manifest_completeness.py && \
	$(PYTHON) scripts/check_sha256_manifest_completeness.py && \
	echo "=== Claim checks ===" && \
	$(PYTHON) scripts/check_claim_boundary_consistency.py && \
	$(PYTHON) scripts/check_no_overclaiming.py && \
	echo "=== Tests ===" && \
	$(PYTHON) -m pytest tests/ -v && \
	echo "=== VERIFICATION PASS ==="
