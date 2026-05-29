# S35. B z q A missing-record prefix-core status

This note records the diagnosis of the two p=23 records that were missed by the first `B z q A` tail-core extractor.

## Input

The diagnostic run was:

```bash
python3 scripts/diagnose_missing_bzqa_tail_core.py \
  logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl \
  --out logs/missing_bzqa_tail_core_p23.jsonl \
  --summary-out logs/summary_missing_bzqa_tail_core_p23.json
```

Summary:

```text
pure_worse_records = 59
missing_tail_core_records = 2
missing_record_indices = [466, 688]
reason_counts = {missing_A: 2}
```

## Missing record 466

Data:

```text
p = 23
A = [6,14]
z = 3
q = 16
B = [11,8,7,13,12,15]
support_length = 6
```

The non-tautological block under `B z q A` is:

```text
B5 B6 z q = 0
```

Numerically:

```text
12 + 15 + 3 + 16 = 46 = 0 mod 23.
```

The full terminal relation is:

```text
B1+B2+B3+B4+B5+B6+z = 0.
```

Subtracting the detected equation gives:

```text
B1+B2+B3+B4 - q = 0.
```

Equivalently:

```text
B_prefix = q.
```

Indeed:

```text
11+8+7+13 = 39 = 16 = q mod 23.
```

## Missing record 688

Data:

```text
p = 23
A = [2,14]
z = 7
q = 4
B = [13,1,18,8,11,5,17,12]
support_length = 8
```

The non-tautological block under `B z q A` is:

```text
B8 z q = 0
```

Numerically:

```text
12 + 7 + 4 = 23 = 0 mod 23.
```

The full terminal relation is:

```text
B1+B2+B3+B4+B5+B6+B7+B8+z = 0.
```

Subtracting the detected equation gives:

```text
B1+B2+B3+B4+B5+B6+B7 - q = 0.
```

Equivalently:

```text
B_prefix = q.
```

Indeed:

```text
13+1+18+8+11+5+17 = 73 = 4 = q mod 23.
```

## Correct interpretation

The two missed records are not genuine exceptions. They are a complementary prefix-core case.

The first extractor searched for blocks of the form:

```text
B_tail + z + q + A + Y_prefix = 0.
```

which reduce by `A+z=0` to:

```text
B_tail + q + Y_prefix = 0.
```

The missed records instead have:

```text
B_tail + z + q = 0.
```

Using the full terminal relation:

```text
B_prefix + B_tail + z = 0,
```

this reduces to:

```text
B_prefix = q.
```

Thus every p=23 pure worse-only record still exposes a hidden terminal-support equation under the move:

```text
B z q A.
```

## Unified B z q A hidden-support equation

For every observed pure worse-only record, `B z q A` exposes one of two equations:

```text
1. Tail equation:
   B_tail + q + Y_prefix = 0.

2. Prefix equation:
   B_prefix = q.
```

The first occurred in:

```text
p=17: 35 / 35
p=23: 57 / 59
```

The second occurred in:

```text
p=23: 2 / 59
```

Therefore the correct universal statement is:

```text
Pure worse-only m=3 terminal residual
  => under B z q A, a hidden support-prefix/tail relation involving q exists.
```

## Proof consequence

The pure worse-only branch should no longer be treated as opaque.

It universally implies a support-internal relation:

```text
B_tail + q + Y_prefix = 0
```

or

```text
B_prefix = q.
```

Both are incompatible with a fully pure terminal obstruction unless the existing branch definitions are missing a terminal-tail/prefix bridge.

## Next script patch

Patch `scripts/extract_bzqa_tail_core_equations.py` so it extracts both:

```text
B_tail+q(+Y_prefix)
B_prefix=q
```

and reports a unified family histogram:

```text
B_tail+q
B_tail+q+Y_prefix
B_prefix=q
```

Expected after patch:

```text
p=17: extracted_records = 35, missing_records = 0
p=23: extracted_records = 59, missing_records = 0
```

## Status

```text
The two p=23 misses are resolved algebraically.
They are B_prefix=q cases.
Patch extractor to make the B z q A hidden-support equation universal.
```
