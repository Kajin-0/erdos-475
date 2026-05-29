# S56. Endpoint-exclusion sublemma drafts

This note drafts the four proof dependencies isolated in S55:

```text
E1. Proper sub-terminal support interval exclusion.
E2. Exterior crossing interval routes to external bridge.
E3. Local q/A or A/B zero interval routes to signed/distributed branch.
E4. Pure worse-only excludes already-routed branches.
```

Together these support Lemma A:

```text
pure worse-only m=3 right-terminal residual
  -> B z q A exposes a hidden-support target interval.
```

## Common setup

Work in `Z/pZ`.  The hard residual has normal form

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0,
D_short(R) = (1,3,1,[2]).
```

The moved order is

```text
R' = X B z q A Y.
```

The endpoint zones are

```text
X | B | z | q | A | Y.
```

The target hidden-support interval families are:

```text
B_tail + z + q = 0,
B_tail + z + q + A_i + Y_prefix = 0,
B_tail + z + q + A1 + A2 + Y_prefix = 0.
```

These reduce to:

```text
B_prefix = q,
B_tail + q + Y_prefix = A_complement,
B_tail + q + Y_prefix = 0.
```

## E1. Proper sub-terminal support interval exclusion

### Statement

Let an interval `I` in the moved order `X B z q A Y` be contained in the block

```text
B z.
```

If `I` is a zero interval and `I` is not the full terminal block

```text
B + z = 0,
```

then `I` gives either:

```text
1. a shorter terminal support zero interval;
2. an internal support zero interval;
3. a terminal split that contradicts the minimal support choice for B.
```

Therefore such an interval cannot occur in a pure worse-only residual except as an already-routed terminal/support branch.

### Proof sketch

Write

```text
B = B_1 B_2 ... B_s.
```

An interval contained in `B z` has one of the forms:

```text
B_i + ... + B_j,
B_i + ... + B_s + z.
```

The first form is a proper internal support relation.  The second form implies

```text
B_i + ... + B_s + z = 0.
```

Since the full support satisfies

```text
B_1 + ... + B_s + z = 0,
```

subtracting gives

```text
B_1 + ... + B_{i-1} = 0.
```

Thus either a support prefix or support suffix is a zero interval.  This contradicts support minimality or routes to a support-terminal branch.

### Use in Lemma A

After E1, the only allowed interval wholly inside `B z` is the tautological full terminal relation:

```text
B + z = 0.
```

This is the observed class:

```text
tautology_terminal_zB.
```

## E2. Exterior crossing interval routes to external bridge

### Statement

Let `I` be a zero interval in `X B z q A Y` whose endpoints cross from an exterior zone into the active window, for example:

```text
X_suffix + B_prefix_or_more = 0,
X_suffix + B_prefix_or_more + z + ... = 0,
... + Y_prefix = 0
```

where `I` is not one of the target hidden-support blocks.

Then `I` gives an external bridge relation and is routed by the external-bridge classifier.

### Proof sketch

In the original residual, the active window is the terminal block around

```text
A z q B.
```

A zero interval using an exterior prefix/suffix means a partial sum outside the active local window coincides with a partial sum created by a local rearrangement.  This is exactly the external bridge situation:

```text
external partial sum = active-window partial sum.
```

Depending on which side the exterior endpoint lies on, the route is:

```text
left exterior  -> LEFT_TERMINAL_BRIDGE or EXTERNAL_BRIDGE,
right exterior -> RIGHT_TERMINAL_BRIDGE or EXTERNAL_BRIDGE,
both/multiple  -> DISTRIBUTED_BRIDGE or MIXED terminal bridge.
```

### Use in Lemma A

The p=23 endpoint taxonomy found two `left_external_X` cases:

```text
record 183: X1 X2 X3 X4 X5 B1 B2 = 0,
record 449: X3 X4 B1 = 0.
```

Both also contain a valid target interval:

```text
record 183: B2 B3 z q A1 A2 = 0,
record 449: B3 z q A1 A2 Y1 = 0.
```

Thus exterior intervals do not obstruct the existence extraction.  If full classification is required, they route to the external branch.

## E3. Local q/A or A/B zero interval routes to signed/distributed branch

### Statement

Let `I` be a zero interval in `X B z q A Y` that is local to the active window but is not a target hidden-support interval and is not a terminal tautology.  Examples include:

```text
q + A_prefix = 0,
A_subblock = 0,
A_prefix + B_suffix = 0,
B_subblock + q = 0,
A_prefix + B_subblock + q = 0.
```

Then `I` gives a signed interval, support-pair trap, or distributed bridge branch, hence is excluded from the pure worse-only residual.

### Proof sketch

Such an interval creates a repeated partial sum pair entirely inside the local active window after a local rearrangement.  Because it does not use the full `B z` tautology and does not use the hidden-support crossing form, it represents an additional local collision.

There are three possible mechanisms:

```text
1. signed interval:
   a local partial sum before insertion equals a shifted local partial sum after q insertion;

2. pair/support trap:
   a small support block involving q and part of B or A forms a zero pair/trap;

3. distributed bridge:
   two or more active-window partial sums connect to the same support/external structure.
```

All three are earlier-routed branches in the current classifier vocabulary.

### Use in Lemma A

This sublemma excludes local non-target shapes from the pure worse-only branch.  Therefore any remaining useful interval crossing `B | z | q | A | Y` must be one of the hidden-support crossing forms.

## E4. Pure worse-only excludes already-routed branches

### Statement

By definition, a pure worse-only residual is one in which all previously tested descent or routing mechanisms fail.  Therefore if a proposed interval shape implies one of the route labels

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
```

then that interval shape is excluded from the pure worse-only branch, or the branch is already closed by prior machinery.

### Proof sketch

This is a definition-level reduction.  The pure worse-only branch was introduced only after removing:

```text
1. clean D_short descent;
2. signed intervals;
3. external bridges;
4. distributed bridges;
5. terminal bridges;
6. pair/support traps;
7. known support-tail obstructions.
```

Therefore any interval shape implying such a label is not a new residual case.

### Use in Lemma A

E4 allows Lemma A to focus only on target hidden-support intervals after E1–E3 dispose of all other endpoint shapes.

## Lemma A dependency graph

The proof of Lemma A becomes:

```text
Endpoint-zone enumeration in X | B | z | q | A | Y
  -> Case contained in Bz: E1
  -> Case exterior crossing: E2
  -> Case local non-target active interval: E3
  -> Exclude routed cases by pure worse-only: E4
  -> Remaining case is B_tail crossing zq into A/Y
  -> hidden-support extraction families.
```

## Remaining work

The sublemmas above are still drafts.  To make them publication-grade:

```text
1. Define "pure worse-only" precisely in proof language.
2. Define support minimality for B.
3. Define active-window partial sums and external partial sums.
4. Prove E1 algebraically for arbitrary support length.
5. Translate E2/E3 route vocabulary into formal partial-sum equalities.
```

## Status

```text
Endpoint exclusion is now reduced to four named sublemmas.
Next: formalize E1 algebraically, since it is the cleanest fully mathematical sublemma.
```
