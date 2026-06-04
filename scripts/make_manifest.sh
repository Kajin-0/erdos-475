#!/usr/bin/env bash
# Generate MANIFEST.sha256 from release/manifest_policy.json.
# Deterministic: sorted git-tracked files, filtered by policy.
set -euo pipefail

OUT="${1:-MANIFEST.sha256}"
POLICY="${2:-release/manifest_policy.json}"
SELF="make_manifest.sh"

if [[ ! -f "$POLICY" ]]; then
  echo "[$SELF] ERROR: manifest policy not found: $POLICY" >&2
  exit 2
fi

# Use Python to filter files by policy
python3 -c "
import json, sys, fnmatch
from pathlib import Path

policy = json.loads(Path('$POLICY').read_text())
never = set(policy.get('never_in_manifest', []))
excluded = policy.get('excluded_path_globs', [])
trusted = set(policy.get('trusted_release_files', []))

# Read git-tracked files from stdin
all_files = [l.strip() for l in sys.stdin if l.strip()]

selected = []
missing_trusted = list(trusted)

for f in all_files:
    if f in never:
        continue
    skip = False
    for pat in excluded:
        if fnmatch.fnmatch(f, pat):
            skip = True
            break
    if skip:
        continue
    selected.append(f)
    if f in missing_trusted:
        missing_trusted.remove(f)

if missing_trusted:
    for f in sorted(missing_trusted):
        print(f'MISSING TRUSTED FILE: {f}', file=sys.stderr)

selected.sort()
for f in selected:
    print(f)
" < <(git ls-files) > /tmp/manifest_files.txt

# Check if there were missing trusted files (script exited with message)
if grep -q 'MISSING TRUSTED FILE' /tmp/manifest_files.txt 2>/dev/null; then
  echo "[$SELF] ERROR: trusted files missing, see above" >&2
  cat /tmp/manifest_files.txt >&2
  exit 2
fi

# Generate sha256sum
xargs sha256sum < /tmp/manifest_files.txt > "$OUT"

# Count
total=$(wc -l < "$OUT")
echo "[$SELF] wrote $OUT ($total entries)"
echo "[$SELF] no MANIFEST.sha256 self-entry"

# Cleanup
rm -f /tmp/manifest_files.txt
