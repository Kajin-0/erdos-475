# S103. Zero-sum endpoint mapping lemma

S102 isolated the first remaining rigor gap for Lemma Z:

```text
Map B_tail/Y_prefix endpoints to active-window indices a,b and exterior index e.
```

This note drafts that endpoint-mapping lemma.

## Purpose

The zero-sum families are:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0.
```

S102 showed that Lemma Z follows once these relations can be expressed as either:

```text
internal signed relation:
  T_a = q + T_b,
```

or:

```text
active-to-exterior bridge relation:
  base + q + T_b = P_e.
```

This note gives the symbolic endpoint map that converts `B_tail` and `Y_prefix` into those forms.

## Global order

Work in the local symbolic order:

```text
R = X A z q B Y,
A = A1 A2.
```

The support block is:

```text
B = B1 B2 ... Bs.
```

A support tail has form:

```text
B_tail = Bt Bt+1 ... Bs
```

for some:

```text
1 <= t <= s.
```

A right exterior prefix has form:

```text
Y_prefix = Y1 Y2 ... Yu
```

for some:

```text
u >= 0.
```

The case `u=0` reduces `BqY_zero` to `Bq_zero`.

## Partial sums

Let global partial sums be:

```text
P_0 = 0,
P_r = R_1 + R_2 + ... + R_r.
```

For a contiguous block `R_{i+1} ... R_j`, the block sum is:

```text
P_j - P_i.
```

Thus a zero-sum block relation is equivalent to equality of its endpoint partial sums.

## Lemma M1. Bq endpoint map

### Statement

If

```text
B_tail + q = 0,
```

then there exist endpoint partial-sum indices `u < v` such that:

```text
P_u = P_v,
```

and the interval `(u,v]` consists exactly of:

```text
q plus B_tail,
```

possibly after the local insertion/rearrangement that exposes the relation.

Relative to an active interval `Z`, this repeated partial-sum equality has one of two forms:

```text
1. internal signed form:     T_a = q + T_b;
2. bridge form:             base + q + T_b = P_e, e in Ext.
```

### Proof sketch

The equation

```text
B_tail + q = 0
```

means:

```text
q + Bt + Bt+1 + ... + Bs = 0.
```

Let `u` be the partial-sum endpoint immediately before `q` in the exposed order, and let `v` be the partial-sum endpoint immediately after the final element of `B_tail`.  Then:

```text
P_v - P_u = q + Bt + ... + Bs = 0.
```

Therefore:

```text
P_u = P_v.
```

Now compare the two endpoints with the active window.

If both endpoints lie inside the active window, write:

```text
P_u = base + T_a,
P_v = base + q + T_b.
```

Then equality gives:

```text
T_a = q + T_b.
```

This is the signed relation.

If one endpoint lies outside the active window, write the exterior endpoint as:

```text
P_e, e in Ext.
```

The active endpoint has form:

```text
base + q + T_b.
```

Then equality gives:

```text
base + q + T_b = P_e.
```

This is the bridge relation.

Thus every exposed `B_tail+q=0` relation maps to either signed form or bridge form.

## Lemma M2. BqY endpoint map

### Statement

If

```text
B_tail + q + Y_prefix = 0,
```

then there exist endpoint partial-sum indices `u < v` such that:

```text
P_u = P_v,
```

and the interval `(u,v]` consists exactly of:

```text
q plus B_tail plus Y_prefix,
```

possibly after the local insertion/rearrangement that exposes the relation.

Relative to an active interval `Z`, this repeated partial-sum equality has one of two forms:

```text
1. internal signed form:     T_a = q + T_b;
2. bridge form:             base + q + T_b = P_e, e in Ext.
```

Moreover, when `Y_prefix` is nonempty and does not cancel internally, the bridge endpoint lies on the right exterior side.

### Proof sketch

The equation

```text
B_tail + q + Y_prefix = 0
```

means:

```text
q + Bt + Bt+1 + ... + Bs + Y1 + ... + Yu = 0.
```

Let `u` be the partial-sum endpoint immediately before `q` in the exposed order, and let `v` be the endpoint immediately after `Y_u`.  Then:

```text
P_v - P_u = q + Bt + ... + Bs + Y1 + ... + Yu = 0.
```

Therefore:

```text
P_u = P_v.
```

If both endpoints are represented inside the active window, the equality becomes:

```text
T_a = q + T_b,
```

which is signed.

If the endpoint after `Y_prefix` lies outside the active window, write it as:

```text
P_e, e in Ext.
```

Then the active endpoint has form:

```text
base + q + T_b,
```

and equality gives:

```text
base + q + T_b = P_e.
```

This is an external or terminal bridge depending on `b`.

Because `Y_prefix` is a right exterior prefix, the natural exterior endpoint lies to the right of the active window.  If additional cancellations move the visible equality fully inside the active window, the case is instead signed.

Thus every exposed `B_tail+q+Y_prefix=0` relation maps to signed form or bridge form.

## Endpoint classification after mapping

Once the relation has bridge form:

```text
base + q + T_b = P_e,
```

there are only three endpoint types.

### Distributed bridge

If the set of bridge depths has size at least two:

```text
|{b : base + q + T_b = P_e for some e in Ext}| >= 2,
```

then the route is:

```text
DISTRIBUTED_BRIDGE.
```

### External bridge

If there is exactly one bridge depth and it is nonterminal:

```text
b < m-1,
```

then the route is:

```text
EXTERNAL_BRIDGE.
```

### Terminal bridge

If there is exactly one bridge depth and it is terminal:

```text
b = m-1,
```

then the route is:

```text
TERMINAL_BRIDGE.
```

This endpoint split is exhaustive.

## Interaction with clean descent

The endpoint map only handles the non-clean case.

For any exposing insertion cut `k`, if:

```text
D_short(new_order(k)) < D_short(old_order),
```

then the branch exits by:

```text
CLEAN_DESCENT.
```

Otherwise, the repeated partial-sum equality supplied by M1 or M2 must be visible as signed or bridge.

Thus Lemma Z can be written as:

```text
zero-sum relation
  -> exposing cut k
  -> either clean descent or repeated-sum endpoint relation
  -> signed or bridge
  -> closed route.
```

## Remaining assumption: exposing cut

This note still assumes an exposing insertion/rearrangement exists that places `q` next to the relevant active support-tail endpoint.

That is the next formal sublemma:

```text
Lemma M3. Exposing-cut existence.
```

Expected form:

```text
For every zero-sum hidden-support family Bq_zero or BqY_zero, one of the bridge-move candidates tested by the certificate exposes the repeated partial-sum endpoints described in M1 or M2.
```

In the certificate this is exactly the successful route object condition:

```text
route_success = true
```

for:

```text
83/83 zero-sum records.
```

## Certificate alignment

The endpoint mapping agrees with the observed hidden equations:

```text
Bq_zero examples:
  B2 B3 q,
  B3 B4 q,
  B3 B4 B5 q,
  B4 B5 B6 q.

BqY_zero examples:
  B3 q Y1,
  B2 B3 q Y1,
  B3 B4 q Y1,
  B2 B3 q Y1 Y2 Y3,
  B3 B4 B5 B6 q Y1.
```

These are exactly contiguous sums whose endpoints become equal partial sums after the relevant exposure move.

## Status

```text
Endpoint mapping lemma drafted.
Bq and BqY zero equations now map to signed or bridge partial-sum forms.
Remaining local sublemma: exposing-cut existence.
```
