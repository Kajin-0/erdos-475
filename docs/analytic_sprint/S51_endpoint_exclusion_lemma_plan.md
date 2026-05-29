# S51. Endpoint-exclusion lemma plan for hidden-support extraction

The pure worse-only branch is empirically closed by the v4 certificate table:

```text
zero-sum families -> target obstruction -> existing route
identity families -> D_short-neutral but q_tail_span_gap decreases
```

The next formalization target is Lemma A from S50:

```text
Hidden-support extraction lemma.
```

## Goal

Prove that if

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0,
D_short(R) = (1,3,1,[2]),
```

and `R` is in the pure worse-only `m=3` right-terminal branch, then the permutation

```text
A z q B -> B z q A
```

creates a non-tautological zero interval that reduces to one of exactly four families:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

## Formal endpoint taxonomy

Under the moved order

```text
X B z q A Y,
```

any new zero interval has endpoints in one of these zones:

```text
X | B | z | q | A | Y
```

The proof must show that all non-hidden-support forms either:

```text
1. are tautological;
2. are an old/expected collision;
3. route to an already-classified branch;
4. contradict pure worse-only minimality.
```

## Expected endpoint classes

### Tautological classes

```text
A1 + A2 + z = 0
B + z = 0
```

These do not create a new branch.

### Hidden-support classes

These are the target classes.

#### Full-A tail core

```text
B_tail + z + q + A1 + A2 + Y_prefix = 0
```

reduces to:

```text
B_tail + q + Y_prefix = 0.
```

If `Y_prefix` is empty:

```text
B_tail + q = 0.
```

#### Partial-A tail core

```text
B_tail + z + q + A_i + Y_prefix = 0
```

reduces to:

```text
B_tail + q + Y_prefix = A_complement.
```

In the current certificate this appears as:

```text
B_tail + q = A_complement.
```

#### Prefix core

```text
B_tail + z + q = 0.
```

Because

```text
B_prefix + B_tail + z = 0,
```

this reduces to:

```text
B_prefix = q.
```

## Classes to exclude or route

The endpoint-exclusion proof must dispose of:

```text
X-involving intervals
Y-only or exterior-only intervals
A/B intervals not crossing zq
A/q intervals not involving B_tail
B/q intervals not involving z/A/Y in the right pattern
mixed intervals with both X and Y
```

Expected routing:

```text
X-involving        -> external/left bridge or contradiction to pure branch
Y-involving only   -> external/right bridge
A/B no zq          -> signed/distributed bridge
B/q support-only   -> Bq/BqY route
other mixed forms  -> earlier classifier or impossibility
```

## Diagnostic needed

Add:

```text
scripts/summarize_bzqa_endpoint_taxonomy.py
```

It should read:

```text
logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl
```

and summarize all `new_zero_intervals` under permutation:

```text
B z q A
```

for pure worse-only records.

Output:

```text
1. zero interval symbolic class histogram;
2. per-record presence of target hidden-support classes;
3. per-record presence of non-target classes;
4. examples of each non-target class;
5. a reduced proof checklist:
   target_hidden_support_present = yes/no
   non_target_classes_seen = [...]
```

## Desired proof-facing output

The ideal result is:

```text
Every pure worse-only record has at least one hidden-support class.
All other classes are from a small finite list already routed by existing branch machinery.
```

Then Lemma A reduces to a finite endpoint-exclusion argument over that list.

## Status

```text
Pure worse branch is empirically closed.
Endpoint-exclusion taxonomy is the next formalization step.
```
