# S86. Zero-sum Bq/BqY routing lemma plan

The equality branch is now consolidated in S85.  The next major dependency in the pure worse-only `m=3` branch theorem is the zero-sum routing lemma.

## Context

Lemma A extracts one of four reduced hidden-support families:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

The equality families are handled by the corrected equality tie-break theorem:

```text
B_tail + q = A_complement,
B_prefix = q.
```

The remaining zero-sum families are:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0.
```

These correspond to the target obstructions:

```text
Bq_zero,
BqY_zero.
```

## Goal

Prove or certify:

```text
Bq_zero  -> already-routed branch,
BqY_zero -> already-routed branch.
```

The route targets are among the already-closed branch mechanisms:

```text
CLEAN_DESCENT,
SIGNED_INTERVAL,
EXTERNAL_BRIDGE,
DISTRIBUTED_BRIDGE,
LEFT_TERMINAL_BRIDGE,
RIGHT_TERMINAL_BRIDGE,
SHORT_TERMINAL_BRIDGE,
LONG_TERMINAL_BRIDGE,
PAIR_TRAP,
support-tail trap.
```

## Current empirical certificate

The v4 certificate table records full zero-sum route coverage:

```text
p=17:
  B_tail+q              -> Bq_zero  -> 23/23 routed
  B_tail+q+Y_prefix     -> BqY_zero -> 8/8 routed

p=23:
  B_tail+q              -> Bq_zero  -> 20/20 routed
  B_tail+q+Y_prefix     -> BqY_zero -> 32/32 routed
```

Thus:

```text
p=17 zero-sum coverage = 31/31
p=23 zero-sum coverage = 52/52
combined zero-sum coverage = 83/83
```

## Lemma Z. Zero-sum routing lemma

### Draft statement

Let `R` be a pure worse-only `m=3` right-terminal residual.  Suppose Lemma A extracts a zero-sum hidden-support family:

```text
B_tail + q = 0
```

or

```text
B_tail + q + Y_prefix = 0.
```

Then `R` triggers an already-routed branch mechanism.  Therefore the zero-sum hidden-support case is not a primitive obstruction.

## Proof strategy

The zero-sum relation says that `q` completes a support tail, optionally with an exterior `Y` prefix:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0.
```

This creates a repeated partial-sum equality between:

```text
1. a support-tail endpoint; and
2. the position after q or after q plus Y_prefix.
```

Depending on whether `Y_prefix` is empty, internal, or exterior-crossing, the repeated partial sum should route as:

```text
Bq_zero:
  support-tail / signed / distributed route.

BqY_zero:
  support-tail plus exterior-prefix route, often external or terminal bridge.
```

## Needed diagnostic consolidation

The proof is currently distributed across route summaries.  Add a single route-certificate table for zero-sum records showing:

```text
p,
record_index,
family,
target_class,
reduced_equation,
route_label,
route_detail,
route_success.
```

Then summarize:

```text
route labels by family,
route labels by p,
failures,
representative examples.
```

## Proposed next script

Add:

```text
scripts/make_zero_sum_route_certificate.py
```

Inputs should include existing route summaries / route JSONL files when available:

```text
logs/summary_route_bq_bqy_obstructions_p17.json
logs/summary_route_bq_bqy_obstructions_p23.json
```

and, if detailed rows exist:

```text
logs/route_bq_bqy_obstructions_p17.jsonl
logs/route_bq_bqy_obstructions_p23.jsonl
```

The script should be robust to missing detailed JSONL files and still emit a summary-only certificate from the summary JSON files.

## Desired output

```text
logs/zero_sum_route_certificate.md
logs/zero_sum_route_certificate.json
```

with a table like:

```text
| p | family | target | records | routed | failures | dominant route labels |
|---|--------|--------|---------|--------|----------|-----------------------|
|17 | B_tail+q | Bq_zero | 23 | 23 | 0 | ... |
|17 | B_tail+q+Y_prefix | BqY_zero | 8 | 8 | 0 | ... |
|23 | B_tail+q | Bq_zero | 20 | 20 | 0 | ... |
|23 | B_tail+q+Y_prefix | BqY_zero | 32 | 32 | 0 | ... |
```

## Formal proof direction

After the route certificate is consolidated, the symbolic lemma should proceed by endpoint classification:

### Case 1. `B_tail + q = 0`

The interval is local to the active support/q region.  It gives a repeated partial-sum equality inside the active window.  If it is not immediately a clean descent, it should be a signed/support/distributed obstruction.

### Case 2. `B_tail + q + Y_prefix = 0`

If `Y_prefix` is nonempty, the interval crosses into the exterior `Y` side.  By the same partial-sum logic used in E2, it should route to an external or terminal bridge, unless it is already a local signed/support obstruction.

## Current status

```text
Equality branch: empirically closed and theorem-style consolidated in S85.
Zero-sum branch: empirically covered by v4 table, needs consolidated route certificate and symbolic routing lemma.
```

## Next action

Add a route-certificate summarizer for zero-sum families.
