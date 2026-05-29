#!/usr/bin/env bash
set -euo pipefail

CERT_FILE="${CERT_FILE:-certificates/minimal_witnesses.jsonl}"
TRACE_ARGS=()

if [[ -f MANIFEST.required ]]; then
  echo "[verify] checking required artifact manifest"
  python scripts/check_required_artifacts.py MANIFEST.required
else
  echo "[verify] missing MANIFEST.required" >&2
  echo "[verify] add MANIFEST.required to declare required docs/scripts/certificate sources" >&2
  exit 2
fi

if [[ -f traces/p29_r3_to_r7_repair_traces_strict.jsonl ]]; then
  TRACE_ARGS+=(--trace traces/p29_r3_to_r7_repair_traces_strict.jsonl)
fi
if [[ -f traces/p31_r3_to_r6_repair_traces_strict.jsonl ]]; then
  TRACE_ARGS+=(--trace traces/p31_r3_to_r6_repair_traces_strict.jsonl)
fi

if [[ ! -f "$CERT_FILE" ]]; then
  if [[ ${#TRACE_ARGS[@]} -gt 0 ]]; then
    echo "[verify] generating $CERT_FILE from traces"
    python scripts/extract_minimal_witnesses.py "${TRACE_ARGS[@]}" --out "$CERT_FILE" --strict
  else
    echo "[verify] missing $CERT_FILE and no known trace files are present" >&2
    echo "[verify] add certificates/minimal_witnesses.jsonl or trace files first" >&2
    exit 2
  fi
fi

echo "[verify] checking minimal witnesses"
python scripts/verify_minimal_witnesses.py "$CERT_FILE" \
  --domain 29:3-7 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage

if [[ -f MANIFEST.sha256 ]]; then
  echo "[verify] checking MANIFEST.sha256"
  sha256sum -c MANIFEST.sha256
else
  echo "[verify] MANIFEST.sha256 not present; skipping hash check"
fi

echo "[verify] PASS all configured finite-certificate checks"
