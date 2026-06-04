#!/usr/bin/env bash
# Strict finite-certificate verification runner.
#
# Normal mode:
#   bash scripts/run_all_verification.sh
#
# Strict release-grade mode:
#   STRICT_CERT=1 bash scripts/run_all_verification.sh

set -euo pipefail

PYTHON="${PYTHON:-python3}"
CERT_FILE="${CERT_FILE:-certificates/minimal_witnesses.jsonl}"
P29_B8_CERT="${P29_B8_CERT:-certificates/witnesses_p29_b08.jsonl}"
STRICT_CERT="${STRICT_CERT:-0}"
TRACE_ARGS=()
CERT_ARGS=("$CERT_FILE")

if [[ -f MANIFEST.required ]]; then
  echo "[verify] checking required artifact manifest"
  "$PYTHON" scripts/check_required_artifacts.py MANIFEST.required
else
  echo "[verify] missing MANIFEST.required" >&2
  echo "[verify] add MANIFEST.required to declare required docs/scripts/certificate sources" >&2
  exit 2
fi

if [[ "$STRICT_CERT" == "1" ]]; then
  echo "[verify] strict mode enabled"

  if [[ ! -s "$CERT_FILE" ]]; then
    echo "[verify] strict mode requires nonempty $CERT_FILE" >&2
    exit 2
  fi

  if [[ ! -s "$P29_B8_CERT" ]]; then
    echo "[verify] strict mode requires nonempty $P29_B8_CERT" >&2
    exit 2
  fi

  if [[ ! -f MANIFEST.sha256 ]]; then
    echo "[verify] strict mode requires MANIFEST.sha256" >&2
    exit 2
  fi

  # ----- Strict-mode audit checks -----
  echo "[verify] validating certificate JSON schema"
  "$PYTHON" scripts/validate_certificate_schema.py --strict "$CERT_FILE" "$P29_B8_CERT"

  echo "[verify] validating verified_domains.json schema"
  "$PYTHON" scripts/validate_certificate_schema.py --domains certificates/verified_domains.json

  echo "[verify] auditing canonical B counts"
  "$PYTHON" scripts/audit_canonical_counts.py \
    "$CERT_FILE" "$P29_B8_CERT" \
    --domain 17:3 --domain 19:3-5 --domain 23:3-9 \
    --domain 29:3-8 --domain 31:3-6 \
    --require-canonical

  echo "[verify] checking manifest completeness"
  "$PYTHON" scripts/check_manifest_completeness.py

  echo "[verify] checking SHA256 manifest coverage"
  "$PYTHON" scripts/check_sha256_manifest_completeness.py

  echo "[verify] checking claim boundary consistency"
  "$PYTHON" scripts/check_claim_boundary_consistency.py

  echo "[verify] scanning for unsafe overclaims"
  "$PYTHON" scripts/check_no_overclaiming.py

  echo "[verify] running regression tests"
  "$PYTHON" -m pytest tests/ -v 2>/dev/null || "$PYTHON" -m unittest discover tests -v

  echo "[verify] checking hash manifest"
  sha256sum -c MANIFEST.sha256
else
  # ----- Development mode -----
  if [[ -f traces/p29_r3_to_r7_repair_traces_strict.jsonl ]]; then
    TRACE_ARGS+=(--trace traces/p29_r3_to_r7_repair_traces_strict.jsonl)
  fi
  if [[ -f traces/p31_r3_to_r6_repair_traces_strict.jsonl ]]; then
    TRACE_ARGS+=(--trace traces/p31_r3_to_r6_repair_traces_strict.jsonl)
  fi

  if [[ ! -f "$CERT_FILE" ]]; then
    if [[ ${#TRACE_ARGS[@]} -gt 0 ]]; then
      echo "[verify] generating $CERT_FILE from traces"
      "$PYTHON" scripts/extract_minimal_witnesses.py "${TRACE_ARGS[@]}" --out "$CERT_FILE" --strict
    else
      echo "[verify] missing $CERT_FILE and no known trace files are present" >&2
      echo "[verify] add certificates/minimal_witnesses.jsonl or trace files first" >&2
      exit 2
    fi
  fi

  if [[ -f MANIFEST.sha256 ]]; then
    echo "[verify] checking MANIFEST.sha256"
    sha256sum -c MANIFEST.sha256
  else
    echo "[verify] MANIFEST.sha256 not present; skipping hash check in development mode"
  fi
fi

if [[ ! -s "$CERT_FILE" ]]; then
  echo "[verify] certificate file is missing or empty: $CERT_FILE" >&2
  exit 2
fi

CERT_ARGS+=("$P29_B8_CERT")

echo "[verify] checking minimal witnesses"
"$PYTHON" scripts/verify_minimal_witnesses.py "${CERT_ARGS[@]}" \
  --domain 17:3 \
  --domain 19:3-5 \
  --domain 23:3-9 \
  --domain 29:3-8 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage

echo "[verify] PASS all configured finite-certificate checks"
