# S68. Three-localization worse-condition plan

S67 closed the equality branch empirically by the finite alternative:

```text
old: A z q P T M

L1:  A z P q T M
L2:  A z q T P M
L3:  A z T q P M
```

For every equality record, at least one of `L1`, `L2`, `L3` is `D_short`-neutral and has

```text
S_tail = span_gap({q} union T) = 0.
```

The remaining symbolic proof target is:

```text
prove L1, L2, and L3 cannot all be worse simultaneously.
```

## Goal

Diagnose why each localization is worse when it fails.

We need to know whether a worse candidate is worse because of:

```text
1. smaller minimum zero interval length;
2. same minimum length but more shortest intervals;
3. larger collision multiplicity profile;
4. a specific new symbolic zero block.
```

## New diagnostic

Add:

```text
scripts/diagnose_three_localization_worse_conditions.py
```

Inputs:

```text
--analysis logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
--equations logs/bzqa_hidden_support_equations_p17_v3.jsonl
--localizations logs/equality_three_localizations_p17.jsonl
```

and similarly for p=23.

The script should:

```text
1. rebuild old, L1, L2, L3 symbolic orders;
2. compute D_short for each;
3. list shortest zero intervals for each candidate;
4. identify zero intervals present in candidate but absent in old;
5. summarize symbolic block classes for worse candidates;
6. report whether the worse reason is shared or mutually exclusive across candidates.
```

## Proof-facing target

A useful output would be a table of implications:

```text
L1 worse -> condition C1
L2 worse -> condition C2
L3 worse -> condition C3
```

Then prove:

```text
not (C1 and C2 and C3)
```

under the equality hidden-support assumptions.

## Expected structure

From the current data:

```text
P_q_T_M is usually neutral.
q_T_P_M and T_q_P_M are often worse.
```

So the proof may reduce to:

```text
If P_q_T_M is worse, then one of q_T_P_M or T_q_P_M is neutral.
```

This is stronger and more tractable than analyzing all three symmetrically.

## Status

```text
Equality branch closed empirically.
Next: diagnose symbolic conditions for failed localizations.
```
