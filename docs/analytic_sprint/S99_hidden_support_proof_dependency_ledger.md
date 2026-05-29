# S99. Hidden-support proof dependency ledger

This note converts the S98 hidden-support branch theorem into a proof-dependency ledger.

The purpose is to separate:

```text
1. certificate-backed closures already established in the S17-S98 sprint;
2. local symbolic lemmas still needed for publication-grade proof;
3. global proof obligations outside the hidden-support branch.
```

## Safe claim boundary

The current safe claim is:

```text
The pure worse-only m=3 hidden-support branch is certified closed in the analyzed finite domain.
```

The current unsafe overclaim would be:

```text
The full Erdős 475 theorem is proved.
```

The full theorem still requires:

```text
analytic residue subset certified finite domain.
```

This note preserves that boundary.

## Branch theorem being supported

S98 assembled the corrected hidden-support branch theorem.

The four Lemma A families are:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

Certified branch closure:

```text
B_tail + q = 0                  -> zero_sum_routed,
B_tail + q + Y_prefix = 0       -> zero_sum_routed,
B_tail + q = A_complement       -> equality_tiebroken,
B_prefix = q                    -> equality_tiebroken.
```

Combined coverage:

```text
zero_sum records: 83/83 covered
equality records: 11/11 covered
combined hidden-support records: 94/94 covered
```

## Dependency graph

```text
Theorem H: Hidden-support branch closure
|
|-- Lemma A: hidden-support extraction
|   |-- output family 1: B_tail+q=0
|   |-- output family 2: B_tail+q+Y_prefix=0
|   |-- output family 3: B_tail+q=A_complement
|   |-- output family 4: B_prefix=q
|
|-- Lemma Z: zero-sum routing
|   |-- Bq_zero  -> closed route
|   |-- BqY_zero -> closed route
|
|-- Lemma C: corrected equality tie-break
|   |-- primary neutral -> S_tail descent
|   |-- primary worse -> P_suffix+q obstruction
|   |-- fallback q T P M -> D_short neutral and S_tail descent
|
|-- Verified-domain ledger
    |-- p=17 certified records
    |-- p=23 certified records
    |-- artifact hashes / reproducibility
```

## Certificate-backed closures

### C1. Zero-sum record-level routing

Source:

```text
S87, S97
```

Status:

```text
complete
```

Evidence:

```text
B_tail+q:
  p=17: 23/23 routed
  p=23: 20/20 routed
  combined: 43/43 routed

B_tail+q+Y_prefix:
  p=17: 8/8 routed
  p=23: 32/32 routed
  combined: 40/40 routed

Total:
  83/83 routed
```

### C2. Zero-sum representative examples

Source:

```text
S91, S97
```

Status:

```text
complete
```

Evidence:

```text
24/24 route examples extracted
2 families x 4 route labels x 3 examples
```

Route labels:

```text
CLEAN_DESCENT,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
MIXED.
```

### C3. Zero-sum attempt-level witnesses

Source:

```text
S95, S96, S97
```

Status:

```text
complete after rich-attempt rerun
```

Evidence:

```text
matched_route_object_rows = 24
matched_attempt_rows = 24
```

The previous `23/24` gap was caused by `attempts_first5` truncation and was closed by:

```text
scripts/route_bq_bqy_obstructions_with_attempts.py
scripts/extract_zero_sum_attempt_witnesses.py
```

### C4. Equality branch coverage

Source:

```text
S85
```

Status:

```text
complete in certified domain
```

Evidence:

```text
p=17:
  B_tail+q=A_complement: 4/4 tiebroken

p=23:
  B_tail+q=A_complement: 5/5 tiebroken
  B_prefix=q:            2/2 tiebroken

Total:
  11/11 equality records tiebroken
```

### C5. Equality primary-failure shape

Source:

```text
S80, S84, S85
```

Status:

```text
complete in certified primary-failure rows
```

Corrected failure mechanism:

```text
P_suffix + q = 0
```

not:

```text
T_prefix + q = 0.
```

Evidence:

```text
primary_failure_rows = 2
rows_with_only_Pq_new_short = 2
rows_with_non_Pq_new_short = 0
```

Primary new shortest blocks:

```text
p=17 record 739: B3 q
p=23 record 716: B3 B4 q
```

### C6. Equality fallback cleanliness

Source:

```text
S80, S85
```

Status:

```text
complete in certified primary-failure rows
```

Evidence:

```text
fallback_new_short_total = 0
fallback_new_short_symbols = {}
fallback_new_zone_histogram = {}
fallback_zone_histogram = {A+z: 2}
```

Thus fallback creates no new shortest block.

## Local symbolic lemmas still needed

### L1. Hidden-support extraction lemma

Need symbolic proof:

```text
Every pure worse-only m=3 right-terminal residual satisfying the structural hypotheses yields one of the four Lemma A families.
```

Target output:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

Current status:

```text
certified empirically in analyzed records; proof still needs clean symbolic writeup.
```

### L2. Zero-sum routing lemma

Need symbolic proof:

```text
Bq_zero  -> closed route,
BqY_zero -> closed route.
```

Closed routes include:

```text
CLEAN_DESCENT,
SIGNED_INTERVAL,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
terminal bridge.
```

Current status:

```text
83/83 certified; 24/24 attempt-level witnesses matched.
```

Proof conversion task:

```text
translate route labels into partial-sum equalities and endpoint cases.
```

### L3. Corrected equality tie-break lemma

Need symbolic proof:

```text
old:      q | P | T | M
primary:  P | q | T | M
fallback: q | T | P | M
```

Show:

```text
If primary is D_short-neutral, then S_tail descends.
If primary is D_short-worse, the only new shortest block is P_suffix+q.
Fallback removes P|q and creates no new shortest block.
```

Current status:

```text
11/11 certified equality records tiebroken;
2/2 primary-failure rows have P_suffix+q and clean fallback.
```

### L4. Refined defect well-foundedness

Need symbolic proof:

```text
D_ref = (D_short, S_tail)
```

is well-founded under the branch moves and compatible with the overall induction/minimal-counterexample scheme.

Current status:

```text
used locally; needs explicit statement in theorem proof.
```

## Global obligations outside this branch

### G1. Verified-domain synchronization

Need a single source of truth:

```text
docs/VERIFIED_DOMAIN.md
```

It should specify:

```text
prime range,
normal forms,
residual classes,
excluded branches,
certificate files,
hashes,
reproduction commands.
```

### G2. Artifact hash ledger

Need:

```text
MANIFEST.sha256
```

covering critical artifacts such as:

```text
minimal witnesses,
summary JSON files,
certificate JSONL files,
route outputs,
proof tables.
```

### G3. CI hardening

Need CI checks that fail if required certificate artifacts are missing or stale.

Minimum target:

```text
CI must fail if minimal_witnesses.jsonl or equivalent finite certificate input is absent.
```

### G4. Analytic residue inclusion

Need the main bridge:

```text
analytic residue subset certified finite domain.
```

This is the main full-theorem bottleneck.

### G5. Claim synchronization

Need consistency across:

```text
README.md,
proof.tex,
docs/FINITE_THEOREM.md,
docs/VERIFIED_DOMAIN.md,
analytic_sprint notes.
```

All should preserve the safe claim boundary.

## Recommended next work order

### Step 1. Local theorem cleanup

Write a concise final local theorem note:

```text
Theorem H: Hidden-support branch closure
```

with formal statements of:

```text
Lemma A,
Lemma Z,
Lemma C,
D_ref descent.
```

### Step 2. Route-label symbolic translation

Use the 24 rich attempt witnesses to translate:

```text
CLEAN_DESCENT,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
MIXED
```

into symbolic partial-sum cases.

### Step 3. Verified-domain doc

Create:

```text
docs/VERIFIED_DOMAIN.md
```

as the repo-level single source of truth.

### Step 4. Manifest

Create:

```text
MANIFEST.sha256
```

from the current critical logs and certificate files.

### Step 5. CI checks

Add tests/scripts that fail when the manifest or required artifacts are absent.

## Summary status

```text
Hidden-support pure worse-only branch:
  certified closed in analyzed finite domain.

Zero-sum branch:
  83/83 routed, 24/24 attempt witnesses matched.

Equality branch:
  11/11 tiebroken, corrected P_suffix+q fallback mechanism.

Full theorem:
  not yet closed until global analytic residue inclusion and verified-domain synchronization are complete.
```
