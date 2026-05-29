# S102. Zero-sum endpoint-exhaustion proof for Lemma Z

This note drafts the endpoint-exhaustion proof for Lemma Z from S100-S101.

The goal is to convert the certificate-backed route labels into a symbolic case split over partial sums, active interval endpoints, and exterior indices.

## Lemma Z target

Let `R` be a certified pure worse-only `m=3` right-terminal residual.  Suppose hidden-support extraction returns one of the zero-sum families:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0.
```

Then `R` triggers at least one already-closed route mechanism:

```text
CLEAN_DESCENT,
SIGNED_INTERVAL,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
TERMINAL_BRIDGE.
```

Therefore the zero-sum families are not primitive obstructions.

## Certified status

From S97:

```text
Record-level route coverage: 83/83
Representative route examples: 24/24
Attempt-level witnesses: 24/24
```

Family coverage:

```text
B_tail+q:          43/43 routed
B_tail+q+Y_prefix: 40/40 routed
```

The endpoint proof below explains the symbolic shape behind those certificates.

## Notation

Let the active shortest zero interval be

```text
Z = (r_i, r_{i+1}, ..., r_{j-1})
```

with length

```text
m = j - i.
```

Let the local prefix sums of `Z` be

```text
T_0 = 0,
T_a = r_i + r_{i+1} + ... + r_{i+a-1},    1 <= a <= m.
```

Since `Z` is a zero interval,

```text
T_m = 0.
```

Let global partial sums be

```text
P_0 = 0,
P_t = r_0 + r_1 + ... + r_{t-1}.
```

Let

```text
base = P_i.
```

Then the global partial sums inside the active window are

```text
P_{i+a} = base + T_a.
```

Let `q` be the distinguished atom moved relative to the active interval.  A right insertion at cut `k` places `q` between

```text
Z_prefix(k) = (r_i, ..., r_{i+k-1})
Z_suffix(k) = (r_{i+k}, ..., r_{j-1}).
```

Here

```text
1 <= k <= m-1.
```

## Exterior partial sums

Define the exterior partial-sum index set by removing the active local window and the `q` endpoint from consideration:

```text
Ext = {0,1,...,n} \ local_window_indices.
```

A bridge occurs when an attempted insertion produces a partial sum equal to some exterior partial sum:

```text
base + q + T_b = P_e,
```

where

```text
e in Ext.
```

The value of `b` determines whether the bridge is nonterminal or terminal:

```text
b < m-1  -> nonterminal bridge,
b = m-1  -> terminal bridge.
```

## Route definitions

The route labels from S101 translate as follows.

### CLEAN_DESCENT

There is an insertion cut `k` such that

```text
D_short(new_order(k)) < D_short(old_order).
```

This is direct descent.

### SIGNED_INTERVAL

There exist indices

```text
0 <= a <= k <= b < m
```

such that

```text
T_a = q + T_b.
```

Equivalently,

```text
q + (T_b - T_a) = 0.
```

Thus `q` plus an internal signed subinterval of `Z` gives a zero relation.

### DISTRIBUTED_BRIDGE

There are at least two distinct bridge depths

```text
b_1 != b_2
```

such that

```text
base + q + T_{b_1} = P_e,
base + q + T_{b_2} = P_{e'}
```

for exterior indices

```text
e,e' in Ext.
```

Thus the obstruction is distributed across at least two active suffix depths.

### EXTERNAL_BRIDGE

There exists a nonterminal bridge depth

```text
b < m-1
```

and exterior index

```text
e in Ext
```

such that

```text
base + q + T_b = P_e.
```

### TERMINAL_BRIDGE

There exists an exterior index

```text
e in Ext
```

such that

```text
base + q + T_{m-1} = P_e.
```

The side and length of the support determine whether the terminal bridge is left, right, short, or long.

## Endpoint-exhaustion principle

For each insertion cut `k`, the classifier asks whether one of three things happens:

```text
1. the defect improves;
2. an internal signed relation appears;
3. an active-to-exterior bridge appears.
```

If none occur, the attempted insertion is not a routed exit.

The endpoint-exhaustion claim for Lemma Z is that the zero-sum hidden-support relations force at least one cut `k` for which one of these three outcomes occurs.

Equivalently:

```text
Bq_zero or BqY_zero
  -> exists k such that CLEAN_DESCENT or SIGNED_INTERVAL or BRIDGE.
```

The bridge case then splits exhaustively by bridge endpoint:

```text
multiple b values -> DISTRIBUTED_BRIDGE,
single b < m-1   -> EXTERNAL_BRIDGE,
single b = m-1   -> TERMINAL_BRIDGE.
```

This is the complete endpoint split.

## Case I. `B_tail + q = 0`

Assume

```text
B_tail + q = 0.
```

Let the extracted support tail correspond, after localization, to a suffix segment of the active support region.  In local prefix-sum notation this has the form

```text
q + (T_b - T_a) = 0
```

for suitable active-window endpoints `a,b`, unless one endpoint is represented by an exterior partial sum.

### I.1. Both endpoints internal

If both endpoints of the zero-sum tail lie inside the active window, then

```text
T_a = q + T_b.
```

This is exactly the signed route condition.

Therefore:

```text
B_tail+q internal -> SIGNED_INTERVAL.
```

### I.2. One endpoint exterior

If one endpoint of the support-tail relation lies outside the active window, then for some exterior index `e`,

```text
base + q + T_b = P_e.
```

This is a bridge route.

The bridge endpoint is then classified by `b`:

```text
at least two distinct b values -> DISTRIBUTED_BRIDGE,
b < m-1                      -> EXTERNAL_BRIDGE,
b = m-1                      -> TERMINAL_BRIDGE.
```

Therefore:

```text
B_tail+q exterior-crossing -> DISTRIBUTED/EXTERNAL/TERMINAL bridge.
```

### I.3. Defect improvement

If the insertion cut that exposes the relation also reduces the short defect, then the case exits even earlier:

```text
D_short(new) < D_short(old) -> CLEAN_DESCENT.
```

Thus all `B_tail+q=0` configurations route.

## Case II. `B_tail + q + Y_prefix = 0`

Assume

```text
B_tail + q + Y_prefix = 0.
```

The additional `Y_prefix` means the zero-sum relation extends into the right exterior side.  In global partial sums, this produces an equality between an active-window partial sum and a right-exterior partial sum.

Thus, unless the relation has already collapsed to a purely internal signed interval, it has the form

```text
base + q + T_b = P_e
```

with

```text
e in Ext.
```

### II.1. Internal collapse

If the `Y_prefix` contribution is empty or cancels so the relation is represented completely inside the active window, then:

```text
T_a = q + T_b.
```

This is a signed interval.

### II.2. Nonterminal exterior endpoint

If the exterior endpoint occurs before the terminal active suffix depth, then

```text
b < m-1.
```

This is an external bridge.

### II.3. Terminal exterior endpoint

If the bridge endpoint is the terminal suffix depth,

```text
b = m-1,
```

then this is a terminal bridge.

### II.4. Multiple exterior bridge depths

If the relation occurs at two or more distinct bridge depths, then

```text
|{b : base + q + T_b = P_e for some e in Ext}| >= 2.
```

This is a distributed bridge.

### II.5. Defect improvement

If the exposing insertion also improves the short defect, the case exits by clean descent.

Thus all `B_tail+q+Y_prefix=0` configurations route.

## Exhaustion of bridge endpoints

Every bridge relation has a bridge depth `b` satisfying

```text
0 <= b < m.
```

There are only three endpoint configurations:

```text
1. at least two distinct b values;
2. exactly one b value with b < m-1;
3. exactly one b value with b = m-1.
```

These are precisely:

```text
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
TERMINAL_BRIDGE.
```

Therefore the bridge cases are exhaustive.

## Exhaustion of route labels

For a zero-sum relation, after choosing a cut `k`, either:

```text
1. D_short improves;
2. no improvement occurs.
```

If improvement occurs, use CLEAN_DESCENT.

If no improvement occurs, the zero-sum relation either has both endpoints internal or at least one exterior endpoint.

```text
both endpoints internal -> SIGNED_INTERVAL,
exterior endpoint       -> bridge.
```

The bridge cases split into distributed, nonterminal external, and terminal.

Thus the full route split is:

```text
CLEAN_DESCENT,
SIGNED_INTERVAL,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
TERMINAL_BRIDGE.
```

This is exhaustive.

## Handling MIXED

`MIXED` is not a primitive route type.  It means more than one closed branch flag occurred for the same attempt.

Formally:

```text
MIXED -> at least one of CLEAN_DESCENT, SIGNED_INTERVAL, DISTRIBUTED_BRIDGE, EXTERNAL_BRIDGE, TERMINAL_BRIDGE.
```

In proof, choose any one closed flag and route through it.

## Lemma Z conclusion

Both zero-sum hidden-support families route:

```text
B_tail + q = 0            -> closed route,
B_tail + q + Y_prefix = 0 -> closed route.
```

Therefore neither zero-sum family is a primitive obstruction.

## Certificate alignment

The symbolic endpoint exhaustion aligns with the rich attempt witness data:

```text
record-level route coverage: 83/83
route examples: 24/24
attempt witnesses: 24/24
```

Attempt-level branch flags observed:

```text
CLEAN_DESCENT:       8
DISTRIBUTED_BRIDGE:  6
EXTERNAL_BRIDGE:     8
SIGNED_INTERVAL:     3
LONG_TERMINAL_BRIDGE: 4
RIGHT_TERMINAL_BRIDGE: 4
LEFT_TERMINAL_BRIDGE: 1
SHORT_TERMINAL_BRIDGE: 1
```

These are exactly the closed route categories used above.

## Remaining rigor gap

This note gives the endpoint-exhaustion proof skeleton.  A fully formal proof still needs the following details written without reference to the classifier:

```text
1. A precise map from B_tail and Y_prefix endpoints to active-window indices a,b and exterior index e.
2. A proof that the chosen insertion cut k always exists under the zero-sum hidden-support hypotheses.
3. A proof that if the cut does not give CLEAN_DESCENT, then the repeated-sum relation must be visible as signed or bridge.
4. A citation to the already-closed signed, distributed, external, and terminal bridge lemmas.
```

## Status

```text
Endpoint-exhaustion proof for Lemma Z drafted.
Zero-sum routing now has a symbolic route-case proof skeleton aligned with the 24/24 rich attempt witnesses.
```
