# S66. Three-localization equality test plan

S65 reduced the equality tie-break proof to a finite symbolic alternative.

Write

```text
B = P T M,
```

where:

```text
P = support prefix before the extracted tail,
T = extracted B_tail,
M = remaining support suffix, usually empty in the current equality records.
```

The old local order is:

```text
A1 A2 z q P T M.
```

The candidate localizations are:

```text
L1 = A1 A2 z P q T M
L2 = A1 A2 z q T P M
L3 = A1 A2 z T q P M
```

All three put `q` adjacent to `T`; therefore all three force:

```text
S_tail = span_gap({q} union T) = 0.
```

The remaining question is which of these preserve `D_short`.

## New diagnostic

Add:

```text
scripts/test_equality_three_localizations.py
```

Inputs:

```text
--analysis logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
--equations logs/bzqa_hidden_support_equations_p17_v3.jsonl
```

and similarly for p=23.

The script should:

```text
1. select equality families;
2. split the order as X A z q B Y;
3. split B = P T M from the extracted B_tail indices;
4. construct L1, L2, L3;
5. compute D_short and S_tail for old and candidate orders;
6. summarize whether at least one candidate is D_short-neutral and S_tail=0.
```

## Desired result

The proof-ready result would be:

```text
p=17:
  equality records = 4
  has neutral localization = 4/4

p=23:
  equality records = 7
  has neutral localization = 7/7
```

If true, S65 becomes a clean finite alternative lemma:

```text
Among P q T M, q T P M, and T q P M, at least one is D_short-neutral.
```

## Status

```text
Equality tie-break reduced to explicit finite localizations.
Next: test all three symbolic localizations directly.
```
