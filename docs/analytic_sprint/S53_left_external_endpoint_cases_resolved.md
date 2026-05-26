# S53. Left-external endpoint cases resolved

This note records the focused diagnostic for the only non-tautological, non-target endpoint-taxonomy residuals under the `B z q A` permutation.

## Input

Diagnostic:

```bash
python3 scripts/diagnose_bzqa_left_external_cases.py \
  logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl \
  --out logs/bzqa_left_external_cases_p23.jsonl \
  --summary-out logs/summary_bzqa_left_external_cases_p23.json
```

## Summary

```text
pure_records_seen = 59
records_with_left_external_X = 2
record_indices = [183, 449]
target_presence_in_left_external_records = {yes: 2}
target_class_counts_in_left_external_records = {hidden_full_A_tail_core: 2}
```

Therefore every record containing a `left_external_X` non-target interval also contains a valid hidden-support target interval.

## Record 183

Non-target interval:

```text
class          = left_external_X
symbolic_block = X1 X2 X3 X4 X5 B1 B2
numeric_block  = [1,8,13,14,4,11,18]
length         = 7
signature      = ext=ext:L7:cross_window_external
```

Candidate:

```text
support_length = 3
A = [10,21]
z = 15
q = 3
B = [11,18,2]
X_length = 5
Y_length = 0
```

Target interval also present:

```text
class          = hidden_full_A_tail_core
symbolic_block = B2 B3 z q A1 A2
numeric_block  = [18,2,15,3,10,21]
length         = 6
signature      = ext=after_BzqA:L6:internal_window
```

Algebraic reduction:

```text
B2 + B3 + z + q + A1 + A2 = 0
A1 + A2 + z = 0
--------------------------------
B2 + B3 + q = 0
```

So record 183 has a valid `B_tail+q` hidden-support equation.

## Record 449

Non-target interval:

```text
class          = left_external_X
symbolic_block = X3 X4 B1
numeric_block  = [9,19,18]
length         = 3
signature      = ext=ext:L3:cross_window_external
```

Candidate:

```text
support_length = 3
A = [20,12]
z = 14
q = 10
B = [18,16,21]
X_length = 4
Y_length = 1
```

Target interval also present:

```text
class          = hidden_full_A_tail_core
symbolic_block = B3 z q A1 A2 Y1
numeric_block  = [21,14,10,20,12,15]
length         = 6
signature      = ext=ext:L6:cross_window_external
```

Algebraic reduction:

```text
B3 + z + q + A1 + A2 + Y1 = 0
A1 + A2 + z = 0
--------------------------------
B3 + q + Y1 = 0
```

So record 449 has a valid `B_tail+q+Y_prefix` hidden-support equation.

## Interpretation

The `left_external_X` cases are not counterexamples to hidden-support extraction.  They are additional exterior collisions that coexist with the desired target interval.

For Lemma A, they can be handled by the following statement:

```text
The B z q A permutation may create exterior non-target intervals, but the extraction lemma only requires existence of at least one target hidden-support interval.  In all certified cases, such a target exists.
```

If the formal proof is strengthened to classify all new intervals, then `left_external_X` should route to the external-bridge branch.  If the proof only asserts existence of a hidden-support target, these cases need no special treatment beyond noting they do not eliminate the target interval.

## Endpoint taxonomy after resolution

The endpoint-taxonomy evidence now supports:

```text
p=17:
  target hidden-support present in 35/35.
  all non-target intervals are terminal zB tautologies.

p=23:
  target hidden-support present in 59/59.
  all non-target intervals are terminal zB tautologies or left-external intervals coexisting with hidden_full_A_tail_core.
```

## Status

```text
The left-external endpoint residuals are documented and do not obstruct Lemma A.
Endpoint-exclusion formalization can proceed.
```
