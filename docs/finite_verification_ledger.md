# Finite verification ledger for Erdos 475

This ledger records the verified finite complement-domain computations completed so far.

Notation:

```text
A subset F_p^*
B = F_p^* \ A
|B| = p - 1 - |A|
```

## Verification domains

The currently verified finite domain is:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

The classes split into two proof/certificate styles:

```text
1. Main descent certificate for p=29, |B|=3..7 and p=31, |B|=3..6.
2. Direct witness generation for the remaining finite residue classes listed below.
```

## Main descent certificate

The main descent certificate covers:

```text
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

It is organized into three internal descent mechanisms:

```text
Non-atomic branch:
  101385 total rows
  101384 multmax_halo4_len1 rows
  1 multmax_halo4_len2 row
  0 unresolved rows

Atomic branch:
  28717 atomic instances
  15160 local signatures
  14890 single-template signatures
  270 high-cover signatures
  0 uncovered signatures
  all certificate moves have block length 1 or 2

One-collision branch:
  39812 total states
  39424 depth-1 states
  383 depth-2 states
  5 depth-3 states
  0 unresolved states
```

Independent certificate verifier status:

```text
nonatomic: ok=101385 fail=0
onecollision: ok=39812 fail=0
atomic-instances-candidate: ok=28717 fail=0
atomic-signature-certs: ok=28717 fail=0
TOTAL ok=198631 fail=0
VERDICT: PASS
```

## Direct witness supplement: small-prime residue

File kept locally in the research sandbox:

```text
small_prime_residue_witness_traces_full.jsonl
```

Verification status:

```text
records = 50508
failures = 0
VERDICT: PASS
```

Per-class counts:

```text
p=17 |B|=3: 35
p=19 |B|=3: 46
p=19 |B|=4: 172
p=19 |B|=5: 476
p=23 |B|=3: 70
p=23 |B|=4: 201
p=23 |B|=5: 1197
p=23 |B|=6: 3399
p=23 |B|=7: 7752
p=23 |B|=8: 14550
p=23 |B|=9: 22610
```

## Direct witness supplement: p = 29 medium residue

The following classes were generated as direct witness JSONL files and verified by `verify_erdos475_trace_semantics.py`.

```text
p=29 |B|=8:  111041 records, failures=0, VERDICT: PASS
p=29 |B|=9:  246675 records, failures=0, VERDICT: PASS
p=29 |B|=10: 468754 records, failures=0, VERDICT: PASS
p=29 |B|=11: 766935 records, failures=0, VERDICT: PASS
p=29 |B|=12: 1086601 records, failures=0, VERDICT: PASS
p=29 |B|=13: 1337220 records, failures=0, VERDICT: PASS
p=29 |B|=14: 1432860 records, failures=0, VERDICT: PASS
p=29 |B|=15: 1337220 records, failures=0, VERDICT: PASS
```

These cover:

```text
p = 29, |B| = 8..15
p = 29, |A| = 20..13
```

Together with the main descent certificate, this verifies:

```text
p = 29, |B| = 3..15
```

## Direct witness supplement: p = 31 medium residue

The following classes were generated as direct witness JSONL files and verified by `verify_erdos475_trace_semantics.py`.

```text
p=31 |B|=7:  67860 records, failures=0, VERDICT: PASS
p=31 |B|=8:  195143 records, failures=0, VERDICT: PASS
p=31 |B|=9:  476913 records, failures=0, VERDICT: PASS
p=31 |B|=10: 1001603 records, failures=0, VERDICT: PASS
p=31 |B|=11: 1820910 records, failures=0, VERDICT: PASS
p=31 |B|=12: 2883289 records, failures=0, VERDICT: PASS
p=31 |B|=13: 3991995 records, failures=0, VERDICT: PASS
p=31 |B|=14: 4847637 records, failures=0, VERDICT: PASS
p=31 |B|=15: 5170604 records, failures=0, VERDICT: PASS
p=31 |B|=16: 4847637 records, failures=0, VERDICT: PASS
```

The final class was run in summary-only mode to avoid writing another multi-GB JSONL file.

```text
p=31 |B|=17
processed = 3991995
solved = 3991995
failed = 0
VERDICT: PASS
class_sha256 = e1aa6a80e90560084d5538867d396d03057d1b777cde2e20dd7bcdebf4b4e2cb
aggregate_sha256 = e1aa6a80e90560084d5538867d396d03057d1b777cde2e20dd7bcdebf4b4e2cb
elapsed_seconds = 42409.89
```

These cover:

```text
p = 31, |B| = 7..17
p = 31, |A| = 23..13
```

Together with the main descent certificate, this verifies:

```text
p = 31, |B| = 3..17
```

## Storage policy

Large witness JSONL files are not committed to the repository at this stage.

Current policy:

```text
1. Keep raw JSONL files in the local research sandbox only while actively needed.
2. Commit concise PASS logs, counts, and SHA256 digests instead of multi-GB witness files.
3. Decide later whether raw artifacts should be stored as compressed archives, GitHub releases, external storage, or regenerated from scripts.
```

## Current finite status

Under the current reduction-residue audit through `p <= 31`, all exposed finite residue classes are covered by either:

```text
1. the main three-branch descent certificate,
2. direct witness JSONL verification,
3. or summary-only witness verification with an aggregate digest.
```

The remaining global task is not more finite computation through `p <= 31`. The remaining task is the analytic reduction audit: identify the published theorem ranges that reduce the infinite problem to this verified finite domain, or list any additional residue cases not yet covered.
