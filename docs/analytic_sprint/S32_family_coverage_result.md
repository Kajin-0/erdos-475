# S32. Record-level symbolic family coverage result

This note records the result from:

```text
scripts/summarize_pure_worse_family_coverage.py
```

using:

```text
logs/summary_pure_worse_family_coverage_p17.json
logs/summary_pure_worse_family_coverage_p23.json
```

## p=17 result

```text
pure_worse_records = 35
```

The only universal family found is:

```text
B z q A -> B_tail+zq+A
```

Coverage:

```text
35 / 35 records
```

Representative symbolic blocks:

```text
support length 3: B3 z q A1 A2 Y1
support length 4: B3 B4 z q A1 A2
support length 5: B3 B4 B5 z q A1 A2
```

The algebraic reading is:

```text
B_tail + z + q + A = 0.
```

Since:

```text
A + z = 0,
```

this collapses to:

```text
B_tail + q = 0.
```

Thus for p=17, pure_worse_only records universally contain a hidden terminal-tail/signed relation exposed by the move:

```text
B z q A.
```

## p=23 result

```text
pure_worse_records = 59
```

No family is universal under the current family labels.

This does not mean the mechanism disappears.  The aggregate family output showed:

```text
B z q A:
  B_tail+zq+A      = 46
  B_A_z_q_Y_mixed  = 5
```

and the symbolic family summary showed `B_tail+zq+A` remains the dominant family in p=23.

Therefore the p=23 obstruction is likely one of:

```text
1. family classifier too narrow;
2. some records use an adjacent equivalent family involving Y or a B-prefix/tail boundary;
3. genuine support-length/boundary exception;
4. a small interior-X exception, since p=23 has X_length 4 or 5 in a few records.
```

## Current proof status

The p=17 data strongly suggests the pure worse-only proof route:

```text
B z q A creates hidden zero block B_tail z q A.
```

But p=23 prevents declaring this universal without another split.

## Next empirical task

Extract p=23 records where:

```text
perm = B z q A
family B_tail+zq+A is absent
```

and print their actual shortest symbolic non-tautological collision blocks.

The goal is to decide whether these missing records are:

```text
1. classifier aliases of B_tail+zq+A;
2. boundary/exterior Y cases;
3. interior-X cases;
4. genuinely different algebraic mechanisms.
```

## Next script

Add:

```text
scripts/extract_family_missing_cases.py
```

Inputs:

```text
logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl
```

Arguments:

```text
--perm "B z q A"
--family "B_tail+zq+A"
```

Output:

```text
logs/missing_BzqA_Btail_zqA_p23.jsonl
```

Compact fields:

```text
record_index
support_length
X_length
Y_length
A,z,q,B
all symbolic non-tautological blocks for that perm
family labels for those blocks
```

## Status

```text
p=17: universal hidden terminal-tail relation found.
p=23: dominant but not universal; need missing-case extraction.
```
