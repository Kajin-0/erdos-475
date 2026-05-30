#!/usr/bin/env bash
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
  echo "[verify] strict certificate mode enabled"

  if [[ ! -s "$CERT_FILE" ]]; then
    echo "[verify] strict mode requires nonempty $CERT_FILE" >&2
    exit 2
  fi

  if [[ ! -f MANIFEST.sha256 ]]; then
    echo "[verify] strict mode requires MANIFEST.sha256" >&2
    exit 2
  fi
else
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
fi

if [[ ! -s "$CERT_FILE" ]]; then
  echo "[verify] certificate file is missing or empty: $CERT_FILE" >&2
  exit 2
fi

if [[ -f "$P29_B8_CERT" ]]; then
  CERT_ARGS+=("$P29_B8_CERT")
else
  echo "[verify] missing optional p29 b8 certificate shard: $P29_B8_CERT" >&2
  echo "[verify] p29 b8 is declared Tier 1; add this shard or set P29_B8_CERT" >&2
  exit 2
fi

echo "[verify] checking minimal witnesses"
"$PYTHON" scripts/verify_minimal_witnesses.py "${CERT_ARGS[@]}" \
  --domain 17:3 \
  --domain 19:3-5 \
  --domain 23:3-9 \
  --domain 29:3-8 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage

if [[ -f MANIFEST.sha256 ]]; then
  echo "[verify] checking MANIFEST.sha256"
  sha256sum -c MANIFEST.sha256
else
  if [[ "$STRICT_CERT" == "1" ]]; then
    echo "[verify] strict mode requires MANIFEST.sha256" >&2
    exit 2
  fi
  echo "[verify] MANIFEST.sha256 not present; skipping hash check in development mode"
fi

echo "[verify] PASS all configured finite-certificate checks"
