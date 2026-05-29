# S89. Zero-sum route example extraction plan

S87 consolidated the zero-sum route certificate:

```text
zero_sum_records = 83
routed_records = 83
all_rows_routed = true
```

S88 drafted the symbolic routing lemma.  The next step is to extract representative route examples so the lemma can be rewritten from route labels into explicit partial-sum equalities.

## Goal

For each zero-sum family and route label, extract compact examples containing:

```text
p,
record_index,
family,
target,
reduced_equation,
route_label,
active_symbolic_order,
zero interval or route witness,
partial-sum equality if available.
```

Families:

```text
B_tail+q              -> Bq_zero
B_tail+q+Y_prefix     -> BqY_zero
```

Route labels of interest:

```text
CLEAN_DESCENT,
MIXED,
EXTERNAL_BRIDGE,
DISTRIBUTED_BRIDGE.
```

## New script

Add:

```text
scripts/extract_zero_sum_route_examples.py
```

The script is intentionally tolerant because detailed route JSONL schemas may evolve.

Inputs:

```text
--analysis logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl \
           logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl
--equations logs/bzqa_hidden_support_equations_p17_v3.jsonl \
            logs/bzqa_hidden_support_equations_p23_v3.jsonl
--route-jsonl logs/route_bq_bqy_obstructions_p17.jsonl \
              logs/route_bq_bqy_obstructions_p23.jsonl
```

If detailed route JSONL files are missing, the script should fail softly and tell the user that only summary-level route coverage is available.

## Output

```text
logs/zero_sum_route_examples.jsonl
logs/summary_zero_sum_route_examples.json
```

The summary should include:

```text
examples_found,
examples_by_family,
examples_by_route_label,
missing_route_jsonl_files,
unmatched_route_rows.
```

## Proof use

The extracted examples will support the symbolic zero-sum routing proof:

```text
Bq_zero:
  local support/q repeated partial sum -> clean/signed/distributed route.

BqY_zero:
  active support/q plus Y prefix repeated partial sum -> external/mixed/distributed route.
```

## Status

```text
Zero-sum route certificate complete.
Next: extract representative route examples for symbolic proof translation.
```
