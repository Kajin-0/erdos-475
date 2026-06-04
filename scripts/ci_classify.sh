#!/usr/bin/env bash
# Reusable CI classification helper.
# Usage:
#   changed_files="$(git diff --name-only ...)"
#   source scripts/ci_classify.sh
#   echo "docs_only=$docs_only"
#
# Exits with docs_only=true if EVERY changed file is a safe low-risk doc
# that can skip heavy finite-certificate verification.
#
# Trusted release files (docs, scripts, certs, tests, CI, policy) are
# never classified as docs-only.

set -euo pipefail

docs_only=true
[[ -z "${changed_files:-}" ]] && { docs_only=false; return; }

while IFS= read -r path; do
  [[ -z "$path" ]] && continue
  safe=false
  case "$path" in
    # Low-risk analytic-development docs
    docs/analytic_*.md) safe=true ;;
    docs/analytic_sprint/*.md) safe=true ;;
    # Final proof-architecture docs (not claim-boundary docs)
    docs/final/*.md) safe=true ;;
    # LaTeX build artifacts
    docs/proof.*) safe=true ;;
    docs/current_status_*.md) safe=true ;;
    docs/file_manifest.md) safe=true ;;
    docs/RESEARCH_TOOLING_INVENTORY.md) safe=true ;;
    docs/submission_target_*.md) safe=true ;;
    docs/independent_analytic_program.md) safe=true ;;
    docs/literature_collection_protocol.md) safe=true ;;
    docs/literature_exact_thresholds.md) safe=true ;;
    docs/reduction_audit.md) safe=true ;;
    docs/source_theorem_ledger.md) safe=true ;;
    docs/legacy/source_theorem_ledger_2026_05_06.md) safe=true ;;
    docs/validation_protocol.md) safe=true ;;
    docs/AI_ASSISTED_STRATEGY.md) safe=true ;;
    docs/ANALYTIC_AI_FIRST_ROADMAP.md) safe=true ;;
    # Local artifact ledgers (metadata only)
    local_artifacts/*.md) safe=true ;;
    local_artifacts/*.csv) safe=true ;;
    local_artifacts/*.json) safe=true ;;
    local_artifacts/*.txt) safe=true ;;
    local_artifacts/*.log) safe=true ;;
  esac
  if ! $safe; then
    docs_only=false
    break
  fi
done <<< "$changed_files"
