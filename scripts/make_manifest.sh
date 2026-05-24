#!/usr/bin/env bash
set -euo pipefail

OUT="${1:-MANIFEST.sha256}"

paths=()
for dir in certificates traces scripts docs rust-verifier .github/workflows; do
  if [[ -d "$dir" ]]; then
    paths+=("$dir")
  fi
done

if [[ ${#paths[@]} -eq 0 ]]; then
  echo "no manifest input directories found" >&2
  exit 2
fi

find "${paths[@]}" -type f \
  ! -name 'MANIFEST.sha256' \
  ! -path '*/target/*' \
  ! -path '*/.git/*' \
  | sort \
  | xargs sha256sum > "$OUT"

echo "wrote $OUT"
wc -l "$OUT"
