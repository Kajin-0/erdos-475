# p29, |B| = 8 promotion protocol

This document gives a local-first protocol for promoting the finite domain

```text
p = 29, |B| = 8
```

from local large-artifact evidence to a Tier 1 candidate certificate domain.

It assumes the large witness trace file exists on a local machine and may be too large to upload or commit directly.

## Goal

Promote exactly one new finite domain:

```text
p = 29, |B| = 8
```

Expected canonical count under nonzero multiplicative scaling:

```text
111041
```

Current Tier 1 row count before promotion:

```text
136375
```

Expected Tier 1 row count after promotion:

```text
247416
```

## Non-claim boundary

This protocol only promotes one finite certificate domain. It does not prove Erdős 475 and does not prove analytic residue inclusion.

## Input artifact

Expected local rich trace artifact, name may vary:

```text
p29_b8_witness_traces.jsonl
```

Each row should contain at least:

```text
p
B
final_order
```

Rows may also contain provenance fields such as:

```text
Q_p
initial_order
final_partial_sums
move trace metadata
```

The minimal certificate verifier ignores fields other than `p`, `B`, and `final_order`.

## Step 1: hash the local source artifact

From the directory containing the local large JSONL:

```bash
sha256sum p29_b8_witness_traces.jsonl > p29_b8_witness_traces.sha256
wc -l p29_b8_witness_traces.jsonl
ls -lh p29_b8_witness_traces.jsonl
```

Record:

```text
source_sha256
source_line_count
source_file_size
```

Expected source line count if the file is exactly one row per canonical `B`:

```text
111041
```

## Step 2: extract a minimal certificate shard

A minimal certificate row should have exactly the fields needed for independent verification:

```json
{"p":29,"B":[...],"final_order":[...]}
```

Recommended output path:

```text
certificates/witnesses_p29_b08.jsonl
```

If the rich trace file already uses the active minimal schema, it may be copied directly. Otherwise extract only the needed fields using a streaming script.

Example Python one-liner:

```bash
python3 - <<'PY'
import json
src = 'p29_b8_witness_traces.jsonl'
out = 'certificates/witnesses_p29_b08.jsonl'
with open(src, 'r', encoding='utf-8') as f, open(out, 'w', encoding='utf-8') as g:
    for line in f:
        if not line.strip():
            continue
        r = json.loads(line)
        m = {'p': int(r['p']), 'B': r['B'], 'final_order': r['final_order']}
        g.write(json.dumps(m, separators=(',', ':'), sort_keys=True) + '\n')
PY
```

## Step 3: verify the p29-b8 shard alone with Python

```bash
python3 scripts/verify_minimal_witnesses.py \
  certificates/witnesses_p29_b08.jsonl \
  --domain 29:8 \
  --require-canonical \
  --require-coverage
```

Expected result:

```text
certificate_file=certificates/witnesses_p29_b08.jsonl verified_rows=111041
domain p=29 |B|=8 observed=111041
domain p=29 |B|=8 expected_canonical=111041 missing=0 extra=0
verified_rows=111041
unique_instances=111041
PASS minimal witness verification
```

## Step 4: verify the p29-b8 shard alone with Rust

```bash
cd rust-verifier
cargo run --release -- ../certificates/witnesses_p29_b08.jsonl \
  --domain 29:8 \
  --require-canonical \
  --require-coverage
cd ..
```

Expected result:

```text
certificate_file=../certificates/witnesses_p29_b08.jsonl verified_rows=111041
domain p=29 |B|=8 observed=111041
domain p=29 |B|=8 expected_canonical=111041 missing=0 extra=0
verified_rows=111041
unique_instances=111041
PASS rust minimal witness verification
```

## Step 5: verify the union with the existing Tier 1 certificate

Python union verification:

```bash
python3 scripts/verify_minimal_witnesses.py \
  certificates/minimal_witnesses.jsonl \
  certificates/witnesses_p29_b08.jsonl \
  --domain 17:3 \
  --domain 19:3-5 \
  --domain 23:3-9 \
  --domain 29:3-8 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
```

Rust union verification:

```bash
cd rust-verifier
cargo run --release -- \
  ../certificates/minimal_witnesses.jsonl \
  ../certificates/witnesses_p29_b08.jsonl \
  --domain 17:3 \
  --domain 19:3-5 \
  --domain 23:3-9 \
  --domain 29:3-8 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
cd ..
```

Expected combined result:

```text
verified_rows=247416
unique_instances=247416
```

## Step 6: decide committed vs external artifact

### Option A: committed certificate shard

Use this if the shard is small enough for ordinary GitHub review.

Commit:

```text
certificates/witnesses_p29_b08.jsonl
MANIFEST.sha256
certificates/verified_domains.json
docs/VERIFIED_DOMAIN.md
```

Then run:

```bash
bash scripts/make_manifest.sh
STRICT_CERT=1 bash scripts/run_all_verification.sh
```

### Option B: external artifact

Use this if the shard is too large for normal repository use.

Do not commit the JSONL. Instead commit a small manifest such as:

```text
certificates/external_artifacts/p29_b08_manifest.json
```

The manifest should include:

```json
{
  "domain": "29:8",
  "p": 29,
  "b": 8,
  "expected_canonical": 111041,
  "verified_rows": 111041,
  "missing": 0,
  "extra": 0,
  "source_artifact_name": "p29_b8_witness_traces.jsonl",
  "source_sha256": "...",
  "minimal_artifact_name": "witnesses_p29_b08.jsonl",
  "minimal_sha256": "...",
  "compressed_artifact_name": "witnesses_p29_b08.jsonl.zst",
  "compressed_sha256": "...",
  "python_verifier": "PASS",
  "rust_verifier": "PASS",
  "union_verified_rows": 247416,
  "union_unique_instances": 247416
}
```

## Step 7: update claim boundary

If the domain is promoted, state only:

```text
The finite certificate workspace verifies p = 29, |B| = 8 as a Tier 1 finite domain, subject to the artifact availability model used for the shard.
```

Do not state:

```text
Erdős 475 is solved.
The analytic residue is closed.
The remaining p = 29 or p = 31 domains are verified.
```

## Promotion checklist

```text
[ ] source artifact line count recorded
[ ] source artifact SHA256 recorded
[ ] minimal shard extracted or identified
[ ] minimal shard SHA256 recorded
[ ] Python shard verification passes
[ ] Rust shard verification passes
[ ] Python union verification passes
[ ] Rust union verification passes
[ ] artifact availability model selected: committed or external
[ ] verified_domains.json updated only if artifact availability is acceptable
[ ] claim boundary preserved
```
