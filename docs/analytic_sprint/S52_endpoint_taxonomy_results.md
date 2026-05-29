# S52. Endpoint taxonomy results for B z q A

This note records the output of:

```text
scripts/summarize_bzqa_endpoint_taxonomy.py
```

using:

```text
logs/summary_bzqa_endpoint_taxonomy_p17.json
logs/summary_bzqa_endpoint_taxonomy_p23.json
```

## Main result

The hidden-support target is present in every pure worse-only record.

```text
p=17: target_presence yes = 35 / 35
p=23: target_presence yes = 59 / 59
```

This strongly supports Lemma A:

```text
pure worse-only m=3 right-terminal residual
  -> B z q A exposes a hidden-support equation.
```

## p=17 endpoint taxonomy

Records and blocks:

```text
records = 35
blocks  = 81
```

Block classes:

```text
hidden_full_A_tail_core     33
hidden_partial_A_tail_core   8
hidden_prefix_core           5
tautology_terminal_zB       35
```

Every record has a target hidden-support class:

```text
target_presence yes = 35 / 35
```

The only non-target class is:

```text
tautology_terminal_zB = 35 / 35
```

Thus for p=17 the endpoint-exclusion burden is minimal:

```text
all non-target intervals are the expected B+z terminal tautology.
```

## p=23 endpoint taxonomy

Records and blocks:

```text
records = 59
blocks  = 152
```

Block classes:

```text
hidden_full_A_tail_core     65
hidden_partial_A_tail_core  16
hidden_prefix_core          10
left_external_X              2
tautology_terminal_zB       59
```

Every record has a target hidden-support class:

```text
target_presence yes = 59 / 59
```

The only non-target classes are:

```text
tautology_terminal_zB = 59 records
left_external_X       = 2 records
```

The non-target combo histogram is:

```text
tautology_terminal_zB                 57
left_external_X|tautology_terminal_zB  2
```

Therefore the only endpoint-exclusion residual is the pair of p=23 `left_external_X` cases.

## Interpretation

The endpoint taxonomy reduces Lemma A to a very small finite exclusion problem.

### Target classes

The observed target classes are exactly the hidden-support families used in the v4 certificate:

```text
hidden_full_A_tail_core
hidden_partial_A_tail_core
hidden_prefix_core
```

These reduce to:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

### Non-target classes

The non-target classes are:

```text
tautology_terminal_zB
left_external_X
```

`tautology_terminal_zB` is expected from:

```text
sum(B) + z = 0.
```

`left_external_X` appears only twice in p=23 and should route to the external/left bridge branch or be ignored because each such record already has a valid hidden-support target.

## Lemma A status

Empirical endpoint-exclusion support:

```text
p=17: complete, only terminal tautology outside target.
p=23: complete target presence, only two left-external non-target residuals.
```

Proof burden now:

```text
1. Prove terminal_zB is tautological.
2. Prove left_external_X is covered by an external branch or irrelevant to extraction because target hidden-support still exists.
3. Prove the target interval forms algebraically reduce to the four v4 families.
```

## Recommended next diagnostic

Add a focused diagnostic for the two p=23 `left_external_X` cases:

```text
scripts/diagnose_bzqa_left_external_cases.py
```

It should print:

```text
record_index,
symbolic_block,
numeric_block,
candidate,
all target classes also present in that record,
whether external-bridge route flags exist.
```

## Status

```text
Endpoint taxonomy supports Lemma A strongly.
Only two p=23 left-external non-target cases need documentation.
```
