# S105. Zero-sum routing lemma final draft

This note consolidates the zero-sum branch proof from:

```text
S102: endpoint-exhaustion proof,
S103: endpoint mapping lemma,
S104: exposing-cut existence lemma.
```

It provides a final proof-facing draft of Lemma Z.

## Lemma Z. Zero-sum routing

### Statement

Let `R` be a certified pure worse-only `m=3` right-terminal residual with local symbolic order

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0.
```

Suppose hidden-support extraction returns one of the zero-sum families:

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

Consequently, neither zero-sum family is a primitive obstruction.

## Certified evidence

From S97:

```text
Record-level route coverage:
  83/83 routed.

Representative route examples:
  24/24 extracted.

Attempt-level witnesses:
  24/24 matched.
```

Family split:

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

The selected matched attempts contain the route flags:

```text
CLEAN_DESCENT,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
SIGNED_INTERVAL,
LEFT_TERMINAL_BRIDGE,
RIGHT_TERMINAL_BRIDGE,
SHORT_TERMINAL_BRIDGE,
LONG_TERMINAL_BRIDGE.
```

## Definitions

Let `Z` be an active shortest zero interval:

```text
Z = (r_i, r_{i+1}, ..., r_{j-1}),
m = j-i.
```

Let local prefix sums be:

```text
T_0 = 0,
T_a = r_i + r_{i+1} + ... + r_{i+a-1},    1 <= a <= m.
```

Since `Z` is zero:

```text
T_m = 0.
```

Let global partial sums be:

```text
P_0 = 0,
P_t = r_0 + r_1 + ... + r_{t-1}.
```

Let:

```text
base = P_i.
```

Then active-window partial sums have form:

```text
P_{i+a} = base + T_a.
```

Let `Ext` denote the set of exterior partial-sum indices outside the active local window.

## Route types

### Clean descent

A cut `k` gives clean descent if:

```text
D_short(new_order(k)) < D_short(old_order).
```

### Signed interval

A cut `k` exposes a signed interval if there are active endpoints `a,b` such that:

```text
T_a = q + T_b.
```

Equivalently:

```text
q + (T_b - T_a) = 0.
```

### Bridge

A cut `k` exposes a bridge if there is an exterior index `e in Ext` and active endpoint depth `b` such that:

```text
base + q + T_b = P_e.
```

Bridge routes split by endpoint depth:

```text
at least two distinct b values -> DISTRIBUTED_BRIDGE,
single b < m-1                -> EXTERNAL_BRIDGE,
single b = m-1                -> TERMINAL_BRIDGE.
```

This split is exhaustive for bridge relations.

## Proof

Apply hidden-support extraction and suppose the extracted family is zero-sum.

There are two cases.

## Case 1. `B_tail + q = 0`

Write:

```text
B_tail = Bt Bt+1 ... Bs.
```

The equation is:

```text
q + Bt + Bt+1 + ... + Bs = 0.
```

By the endpoint map S103, when the relation is exposed by a candidate cut, the equality of endpoint partial sums has one of two forms:

```text
T_a = q + T_b,
```

or:

```text
base + q + T_b = P_e,  e in Ext.
```

By S104, an exposing cut exists among the admissible hidden-support bridge moves unless an earlier candidate already gives clean descent.

Thus:

```text
B_tail+q=0
  -> CLEAN_DESCENT or SIGNED_INTERVAL or BRIDGE.
```

If the route is signed, it exits through `SIGNED_INTERVAL`.

If the route is a bridge, the endpoint depth split gives exactly one of:

```text
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
TERMINAL_BRIDGE.
```

Therefore `B_tail+q=0` is routed.

## Case 2. `B_tail + q + Y_prefix = 0`

Write:

```text
Y_prefix = Y1 Y2 ... Yu.
```

The equation is:

```text
q + Bt + Bt+1 + ... + Bs + Y1 + ... + Yu = 0.
```

If `u=0`, this reduces to Case 1.

Assume `u>0`.  By the endpoint map S103, when exposed by a candidate cut, the repeated partial-sum equality again has one of two forms:

```text
T_a = q + T_b,
```

or:

```text
base + q + T_b = P_e,  e in Ext.
```

The nonempty `Y_prefix` naturally places the endpoint after `Y_u` on the right exterior side unless the relation collapses internally.  Therefore the exposed relation is either signed or bridge.

By S104, an exposing cut exists among the admissible hidden-support bridge moves unless an earlier candidate already gives clean descent.

Thus:

```text
B_tail+q+Y_prefix=0
  -> CLEAN_DESCENT or SIGNED_INTERVAL or BRIDGE.
```

Again, the bridge endpoint split gives:

```text
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
TERMINAL_BRIDGE.
```

Therefore `B_tail+q+Y_prefix=0` is routed.

## Handling MIXED labels

The certificate may label an attempt as:

```text
MIXED.
```

This is not a primitive branch.  It means that more than one closed branch flag occurs simultaneously.

Formally:

```text
MIXED -> at least one of CLEAN_DESCENT, SIGNED_INTERVAL, DISTRIBUTED_BRIDGE, EXTERNAL_BRIDGE, TERMINAL_BRIDGE.
```

In a proof, select any closed flag present in the mixed attempt.

## Exhaustion

For either zero-sum family, after an exposing cut is selected, exactly one of the following is true:

```text
1. D_short improves;
2. both repeated-sum endpoints are internal;
3. at least one repeated-sum endpoint is exterior.
```

These correspond respectively to:

```text
1. CLEAN_DESCENT;
2. SIGNED_INTERVAL;
3. BRIDGE.
```

Every bridge has endpoint depth `b` with:

```text
0 <= b < m.
```

The bridge endpoint split is exhaustive:

```text
at least two b values,
exactly one b<m-1,
exactly one b=m-1.
```

Therefore every bridge is one of:

```text
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
TERMINAL_BRIDGE.
```

Thus every zero-sum hidden-support residual routes through a closed mechanism.

## Conclusion

Both zero-sum families are nonprimitive:

```text
B_tail + q = 0                  -> routed,
B_tail + q + Y_prefix = 0       -> routed.
```

This proves Lemma Z at the proof-skeleton level.

## Current rigor status

This note combines the proof skeletons from S102-S104.  It remains certificate-backed rather than fully publication-grade until the following are written purely symbolically:

```text
1. exact definition of admissible hidden-support bridge moves;
2. proof that the support-tail endpoint determines an admissible exposing cut;
3. proof that non-clean exposing cuts necessarily reveal signed or bridge endpoint equalities;
4. references to the already-closed signed, distributed, external, and terminal bridge lemmas.
```

However, the empirical branch status is complete:

```text
83/83 zero-sum records routed,
24/24 route examples extracted,
24/24 attempt witnesses matched.
```

## Role in Theorem H

Together with Lemma C for equality branches, Lemma Z closes all four hidden-support extraction outputs:

```text
B_tail + q = 0                  -> zero_sum_routed,
B_tail + q + Y_prefix = 0       -> zero_sum_routed,
B_tail + q = A_complement       -> equality_tiebroken,
B_prefix = q                    -> equality_tiebroken.
```

Therefore Lemma Z is now ready to be referenced by the local hidden-support branch theorem S100.

## Status

```text
Zero-sum routing lemma final draft assembled.
Next local target: corrected equality tie-break symbolic endpoint proof, or repo-level VERIFIED_DOMAIN.md.
```
