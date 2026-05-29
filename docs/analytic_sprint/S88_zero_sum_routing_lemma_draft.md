# S88. Zero-sum Bq/BqY routing lemma draft

This note drafts the symbolic routing lemma for the zero-sum hidden-support branch.

## Context

Lemma A extracts one of four hidden-support families:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

The equality families are handled by S85.  This note handles the zero-sum families:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0.
```

These correspond to target obstruction classes:

```text
Bq_zero,
BqY_zero.
```

## Lemma Z. Zero-sum routing lemma

### Statement

Let `R` be a pure worse-only `m=3` right-terminal residual.  Suppose hidden-support extraction gives one of:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0.
```

Then `R` triggers an already-routed branch mechanism.  Hence the zero-sum hidden-support branch is not a primitive obstruction.

## Certified coverage

The consolidated zero-sum route certificate gives:

```text
zero_sum_records = 83
target_classified_records = 83
routed_records = 83
all_rows_routed = true
```

Family-level coverage:

```text
B_tail+q:
  p=17: 23/23 routed
  p=23: 20/20 routed
  combined: 43/43 routed

B_tail+q+Y_prefix:
  p=17: 8/8 routed
  p=23: 32/32 routed
  combined: 40/40 routed
```

Dominant route labels are:

```text
CLEAN_DESCENT,
MIXED,
EXTERNAL_BRIDGE,
DISTRIBUTED_BRIDGE.
```

## Symbolic mechanism

### Case 1. `B_tail + q = 0`

The relation

```text
B_tail + q = 0
```

means a suffix of the support block `B` is completed by `q` to form a zero interval.

In partial-sum language, this is a repeated local active-window sum:

```text
P_before_B_tail = P_after_q.
```

Thus the obstruction is internal to the support/q region.  It must produce one of:

```text
1. clean descent under a local rearrangement;
2. signed interval;
3. support-tail trap;
4. distributed active-window bridge.
```

These correspond to the routed labels observed in the certificate:

```text
CLEAN_DESCENT,
MIXED,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE.
```

The `EXTERNAL_BRIDGE` labels can occur when the same local partial-sum equality also lines up with an exterior state.  That does not make the case primitive; it strengthens routing.

### Case 2. `B_tail + q + Y_prefix = 0`

The relation

```text
B_tail + q + Y_prefix = 0
```

extends the local support/q zero relation into the right exterior side.

If `Y_prefix` is nonempty, the corresponding repeated partial-sum equality crosses from the active support/q window into the `Y` exterior zone:

```text
P_active = P_right_exterior.
```

By the same partial-sum mechanism used in E2, this is an external or terminal bridge unless it has already become a clean descent or local signed/support obstruction.

Thus the possible routes include:

```text
CLEAN_DESCENT,
EXTERNAL_BRIDGE,
DISTRIBUTED_BRIDGE,
MIXED.
```

This matches the certificate histograms.

## Proof skeleton

### Step 1. Convert zero-sum relation to partial-sum equality

For `B_tail+q=0`, the equality is local:

```text
sum(B_tail)+q = 0.
```

For `B_tail+q+Y_prefix=0`, the equality crosses into `Y`:

```text
sum(B_tail)+q+sum(Y_prefix)=0.
```

In both cases, there are repeated partial sums in the local or active-plus-exterior window.

### Step 2. Apply branch classification

A repeated partial sum of this kind is exactly one of the existing route mechanisms:

```text
local repeated active sum    -> signed/support/distributed branch;
active-exterior repeated sum -> external/terminal bridge;
descent-producing sum        -> CLEAN_DESCENT.
```

### Step 3. Exclude primitive obstruction status

Since pure worse-only residuals exclude already-routed branches, a zero-sum hidden-support record cannot remain primitive.  It exits through the existing route mechanism.

## Certificate interpretation

The certificate table verifies both target classification and route success:

```text
| p | family | target | records | target_coverage | route_coverage | status |
|---|--------|--------|---------|-----------------|----------------|--------|
|17 | B_tail+q | Bq_zero | 23 | 23/23 | 23/23 | zero_sum_routed |
|17 | B_tail+q+Y_prefix | BqY_zero | 8 | 8/8 | 8/8 | zero_sum_routed |
|23 | B_tail+q | Bq_zero | 20 | 20/20 | 20/20 | zero_sum_routed |
|23 | B_tail+q+Y_prefix | BqY_zero | 32 | 32/32 | 32/32 | zero_sum_routed |
```

Thus the empirical branch closure is complete for the zero-sum families.

## Remaining formal proof obligation

A publication-grade proof must replace the route-certificate statement with a symbolic classifier lemma:

```text
Bq_zero  -> CLEAN_DESCENT or SIGNED/DISTRIBUTED/EXTERNAL route,
BqY_zero -> CLEAN_DESCENT or SIGNED/DISTRIBUTED/EXTERNAL route.
```

The key formal work is to define the existing route labels directly in terms of partial-sum equalities and then prove the implication from the two zero-sum relations.

## Recommended next diagnostic

Extract representative examples by route label for each zero-sum family:

```text
family = B_tail+q, route label = CLEAN_DESCENT
family = B_tail+q, route label = EXTERNAL_BRIDGE
family = B_tail+q+Y_prefix, route label = CLEAN_DESCENT
family = B_tail+q+Y_prefix, route label = MIXED
```

For each example, print:

```text
record_index,
reduced_equation,
route label,
active symbolic order,
zero interval causing route,
partial-sum equality.
```

This will help convert the route lemma from label-level to symbolic partial-sum-level.

## Status

```text
Zero-sum routing lemma drafted.
Empirical route coverage: 83/83.
Remaining symbolic work: define route labels by partial-sum equalities and prove Bq/BqY imply them.
```
