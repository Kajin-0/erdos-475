# S58. E2 exterior crossing interval routes to external bridge

This note formalizes E2 from S56.

## Purpose

In the endpoint-zone proof for

```text
R' = X B z q A Y,
```

we must dispose of zero intervals whose endpoints involve exterior zones:

```text
X | B | z | q | A | Y.
```

Such intervals are not hidden-support core intervals unless they have the specific form

```text
B_tail + z + q + A_prefix + Y_prefix = 0.
```

All other exterior-crossing zero intervals are external partial-sum coincidences and therefore route to the external-bridge machinery.

## Setup

Let the moved order be

```text
R' = r_1 r_2 ... r_n = X B z q A Y.
```

Define partial sums

```text
P_0 = 0,
P_j = r_1 + r_2 + ... + r_j.
```

A contiguous block

```text
r_{i+1} + ... + r_j
```

is zero if and only if

```text
P_i = P_j.
```

Let the active window be the local block produced by moving

```text
B z q A
```

and let exterior partial-sum indices be those lying outside this active window, i.e. in the prefix/suffix zones corresponding to `X` or exterior `Y`.

## Lemma E2

### Statement

Let `I` be a zero interval in `R' = X B z q A Y` with one endpoint outside the active window and the other endpoint inside or across the active window.

If `I` is not a target hidden-support interval of the form

```text
B_tail + z + q + A_prefix + Y_prefix = 0,
```

then `I` induces an external bridge relation:

```text
P_ext = P_active.
```

Consequently, the interval routes to one of the external bridge classes:

```text
EXTERNAL_BRIDGE,
LEFT_TERMINAL_BRIDGE,
RIGHT_TERMINAL_BRIDGE,
MIXED_TERMINAL_BRIDGE,
DISTRIBUTED_BRIDGE.
```

## Proof

A zero interval `I` is determined by a repeated partial-sum pair:

```text
P_i = P_j.
```

If one of `i,j` is exterior and the other lies in the active window, then by definition there is a partial-sum equality between an exterior state and an active-window state:

```text
P_ext = P_active.
```

This is precisely the external-bridge condition.

The side of the exterior endpoint determines the route label:

```text
P_ext left of active window   -> LEFT_TERMINAL_BRIDGE or EXTERNAL_BRIDGE,
P_ext right of active window  -> RIGHT_TERMINAL_BRIDGE or EXTERNAL_BRIDGE.
```

If more than one active-window bridge index appears, or if both left and right exterior endpoints occur, the route is distributed or mixed:

```text
multiple active bridge indices -> DISTRIBUTED_BRIDGE,
left and right exterior sides  -> MIXED_TERMINAL_BRIDGE.
```

Therefore any non-target exterior-crossing interval is not a new pure residual case.  It is an external bridge event.

## Relation to the classifier vocabulary

The existing classifier implements exactly this principle.  It tracks active-window partial sums and compares them against exterior partial sums.  Its route labels include:

```text
EXTERNAL_BRIDGE
LEFT_TERMINAL_BRIDGE
RIGHT_TERMINAL_BRIDGE
MIXED_TERMINAL_BRIDGE
DISTRIBUTED_BRIDGE
SHORT_TERMINAL_BRIDGE
LONG_TERMINAL_BRIDGE
```

The length flags `SHORT_TERMINAL_BRIDGE` and `LONG_TERMINAL_BRIDGE` refine terminal bridge geometry, but the underlying mechanism is still the same partial-sum equality:

```text
P_ext = P_active.
```

## Application to the two observed left-external cases

The endpoint taxonomy found two non-target `left_external_X` cases in p=23.

### Record 183

```text
X1 X2 X3 X4 X5 B1 B2 = 0.
```

This is a cross-window exterior interval because the left endpoint lies in the exterior `X` zone and the right endpoint reaches into the support block `B`.

Thus it gives

```text
P_ext = P_active.
```

It is an external bridge case.

The same record also contains a hidden-support target interval:

```text
B2 B3 z q A1 A2 = 0.
```

Hence it does not obstruct hidden-support extraction.

### Record 449

```text
X3 X4 B1 = 0.
```

Again, this is a cross-window exterior interval, hence an external bridge partial-sum equality.

The same record also contains the target interval:

```text
B3 z q A1 A2 Y1 = 0.
```

Thus it also does not obstruct hidden-support extraction.

## Use in Lemma A

In the endpoint-zone enumeration, E2 handles all cases in which a zero interval begins in `X` or otherwise has an exterior endpoint, unless it is one of the target forms with `Y_prefix` appended after `A`:

```text
B_tail + z + q + A_prefix + Y_prefix = 0.
```

Therefore exterior intervals can be discarded from the hidden-support existence proof because they are already routed or coexist with target intervals.

## Formal phrasing for the main proof

A compact proof sentence can be:

```text
Any non-target zero interval with an endpoint outside the active window gives a repeated partial-sum equality between an exterior index and an active-window index.  By definition this is an external bridge.  Since pure worse-only residuals exclude already-routed external bridges, such an interval cannot be the unresolved obstruction; and if it coexists with a target interval, the extraction lemma proceeds using the target interval.
```

## Status

```text
E2 is formalized as a partial-sum equality argument.
Remaining sublemmas: E3 and E4.
```
