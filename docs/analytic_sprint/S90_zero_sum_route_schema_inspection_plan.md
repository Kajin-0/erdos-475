# S90. Zero-sum route JSONL schema inspection plan

S89 extracted representative zero-sum rows, but the resulting route label was:

```text
worse
```

for every example.

That is not the intended route label.  It is almost certainly a bridge/move class inherited from the hidden-support bridge file, not the actual route mechanism such as:

```text
CLEAN_DESCENT,
EXTERNAL_BRIDGE,
DISTRIBUTED_BRIDGE,
MIXED.
```

## Problem

The route summaries contain the useful route-label histograms:

```text
CLEAN_DESCENT,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
MIXED.
```

but the detailed JSONL schema is not yet known.  The current extractor guessed field names and picked up the wrong field.

## Goal

Inspect the detailed route JSONL schema directly.

We need to identify fields containing:

```text
1. record index;
2. reduced family;
3. actual route labels;
4. route witnesses or attempt records;
5. symbolic zero block / interval data if present.
```

## New script

Add:

```text
scripts/inspect_zero_sum_route_jsonl_schema.py
```

Inputs:

```text
logs/route_bq_bqy_obstructions_p17.jsonl
logs/route_bq_bqy_obstructions_p23.jsonl
```

The script should print:

```text
row count,
top-level key histogram,
field type histogram,
string value histograms for likely label fields,
nested list/dict key samples,
first few compact rows.
```

It should specifically inspect likely fields:

```text
class,
route_label,
route_class,
label,
result_counts,
route_label_counts,
attempt_label_counts,
attempt_flag_counts,
results,
routes,
attempts,
witnesses.
```

## Desired outcome

Once the actual schema is known, revise:

```text
scripts/extract_zero_sum_route_examples.py
```

so that it extracts true route examples such as:

```text
B_tail+q :: CLEAN_DESCENT
B_tail+q :: EXTERNAL_BRIDGE
B_tail+q+Y_prefix :: CLEAN_DESCENT
B_tail+q+Y_prefix :: MIXED
```

rather than examples labeled only as `worse`.

## Status

```text
Zero-sum route certificate is valid at summary level.
Detailed route example extraction needs schema inspection before symbolic witness extraction.
```
