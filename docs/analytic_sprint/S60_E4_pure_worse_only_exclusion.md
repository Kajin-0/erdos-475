# S60. E4 pure worse-only excludes already-routed branches

This note formalizes E4 from S56.

## Purpose

The endpoint-zone proof for the hidden-support extraction lemma repeatedly uses the phrase:

```text
this interval routes to an earlier branch, so it is excluded from pure worse-only.
```

E4 makes this precise.

## Branch hierarchy

The proof search has progressively removed easier cases before isolating the pure worse-only `m=3` terminal residual.

The residual branch is reached only after excluding or routing intervals that trigger:

```text
CLEAN_DESCENT,
SIGNED_INTERVAL,
EXTERNAL_BRIDGE,
DISTRIBUTED_BRIDGE,
LEFT_TERMINAL_BRIDGE,
RIGHT_TERMINAL_BRIDGE,
MIXED_TERMINAL_BRIDGE,
SHORT_TERMINAL_BRIDGE,
LONG_TERMINAL_BRIDGE,
PAIR_TRAP,
support-tail trap,
Bq/BqY routed branch.
```

Thus `pure worse-only` is not merely a data label.  It is a reduction condition:

```text
A residual is pure worse-only only if all previously defined descent/routing mechanisms fail.
```

## Lemma E4

### Statement

Let `R` be a residual order currently under consideration in the pure worse-only branch.  If a local rearrangement or zero interval of `R` implies one of the already-routed branch labels

```text
CLEAN_DESCENT,
SIGNED_INTERVAL,
EXTERNAL_BRIDGE,
DISTRIBUTED_BRIDGE,
LEFT_TERMINAL_BRIDGE,
RIGHT_TERMINAL_BRIDGE,
MIXED_TERMINAL_BRIDGE,
SHORT_TERMINAL_BRIDGE,
LONG_TERMINAL_BRIDGE,
PAIR_TRAP,
support-tail trap,
Bq/BqY routed branch,
```

then `R` is not an unresolved pure worse-only residual.  It is either:

```text
1. already reduced by a descent;
2. routed to a prior branch lemma;
3. reduced by a refined tie-break inside a routed branch.
```

Therefore such a case may be excluded when proving the hidden-support extraction lemma for the unresolved pure worse-only branch.

## Proof

This is a definition-level reduction.

The pure worse-only branch is introduced only after the proof procedure attempts all previously defined local moves and branch classifiers.  If any such classifier succeeds, the record exits the pure residual branch.

Thus, by construction:

```text
pure worse-only = complement of previously closed/routed local branches
```

inside the chosen terminal normal form.

Equivalently, for any interval shape `I`, if

```text
I => already_routed_label,
```

then

```text
I is not an unresolved pure worse-only obstruction.
```

## Relation to E1-E3

E1-E3 identify interval classes and map them to existing branch labels.

### E1

A proper sub-terminal support interval inside `B z` implies a support-zero relation:

```text
proper B-subblock = 0
```

or

```text
proper B-prefix = 0.
```

This routes to a support/terminal branch.  By E4, it is excluded from pure worse-only.

### E2

An exterior-crossing interval gives a partial-sum equality:

```text
P_ext = P_active.
```

This routes to external bridge or terminal bridge labels.  By E4, it is excluded from pure worse-only.

### E3

A local active-window non-target interval gives a signed, pair-trap, support-tail, or distributed local obstruction.  By E4, it is excluded from pure worse-only.

## Use in Lemma A

In the moved order

```text
R' = X B z q A Y,
```

endpoint-zone enumeration leaves only these possibilities:

```text
1. terminal tautology B+z=0;
2. already-routed non-target interval;
3. hidden-support target interval.
```

E4 removes option 2 from the unresolved pure branch.  Option 1 is ignored as tautological.  Therefore any non-tautological unresolved interval must be a hidden-support target interval.

## Important nuance

The hidden-support extraction lemma is an existence lemma.  It does not require that every new zero interval be a target interval.

The p=23 records 183 and 449 show this nuance:

```text
left_external_X interval exists,
but hidden_full_A_tail_core also exists.
```

E4 says the left-external interval is already-routed, while the hidden-support target still supplies the extraction.  Thus already-routed intervals do not obstruct the existence proof.

## Formal proof phrase

A compact phrase for the main proof is:

```text
By the definition of the pure worse-only residual, any interval shape implying clean descent, signed interval, external bridge, distributed bridge, terminal bridge, pair trap, or routed support-tail obstruction has already exited the branch.  Hence, after discarding the terminal tautology, the only remaining non-tautological active-window intervals relevant to the unresolved branch are the hidden-support crossing forms.
```

## Status

```text
E4 formalized.
Endpoint-exclusion dependency chain E1-E4 is now complete at draft level.
Next: assemble Lemma A as a standalone proof using S55-S60.
```
