# S101. Zero-sum route-label symbolic translation

This note translates the zero-sum route labels from S97 into proof-facing symbolic cases for Lemma Z.

## Input

Lemma Z handles the zero-sum hidden-support families:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0.
```

These correspond to target classes:

```text
Bq_zero,
BqY_zero.
```

S97 established:

```text
record-level route coverage: 83/83
representative route examples: 24/24
attempt-level witnesses: 24/24
```

The relevant route labels are:

```text
CLEAN_DESCENT,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
MIXED.
```

The selected matched attempts also include branch flags:

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

## Common partial-sum setup

Let the active local order contain a shortest active interval

```text
Z = (r_i, r_{i+1}, ..., r_{j-1})
```

with length

```text
m = j-i.
```

Let `q` be the atom inserted across or into this active interval.  Define local prefix sums of `Z`:

```text
T_0 = 0,
T_a = r_i + ... + r_{i+a-1},  1 <= a <= m.
```

Let the global partial sums be:

```text
P_0 = 0,
P_t = r_0 + ... + r_{t-1}.
```

Let

```text
base = P_i.
```

A right insertion at local cut `k` compares:

```text
new_order = Z_prefix(k), q, Z_suffix(k).
```

The classifier detects the following relations.

## Symbolic route case 1. CLEAN_DESCENT

### Certificate label

```text
CLEAN_DESCENT
```

### Symbolic meaning

There exists a local insertion move such that

```text
D_short(new_order) < D_short(old_order).
```

This is a direct descent route.

### Proof use

If the zero-sum relation admits a `CLEAN_DESCENT` attempt, the branch exits immediately.  No further obstruction analysis is needed.

### Attempt-witness interpretation

The matched attempts include fields:

```text
old_defect,
new_defect,
branch_flags = [CLEAN_DESCENT] or containing CLEAN_DESCENT.
```

The symbolic proof only needs to show:

```text
new_defect < old_defect
```

in the lexicographic order defining `D_short`.

## Symbolic route case 2. SIGNED_INTERVAL

### Certificate branch flag

```text
SIGNED_INTERVAL
```

### Symbolic meaning

There exist indices

```text
0 <= a <= k <= b < m
```

such that

```text
T_a = q + T_b  mod p.
```

Equivalently,

```text
q + (T_b - T_a) = 0 mod p.
```

This means `q` and a nonempty internal signed subinterval of `Z` form a zero relation.

### Proof use

A signed interval is an already-routed local obstruction.  Therefore a zero-sum hidden-support family producing this relation is not primitive.

### Attempt-witness interpretation

The classifier stores signed witnesses in:

```text
signed = [{a,b,value}, ...]
```

where `value` is the repeated partial-sum value.

## Symbolic route case 3. DISTRIBUTED_BRIDGE

### Certificate label

```text
DISTRIBUTED_BRIDGE
```

### Symbolic meaning

There are at least two distinct suffix endpoints

```text
b_1 != b_2
```

such that the attempted insertion creates exterior bridge values:

```text
base + q + T_{b_1} = P_e,
base + q + T_{b_2} = P_{e'},
```

for exterior partial-sum indices `e,e'` outside the active local window.

Equivalently, the same insertion exposes bridge relations at multiple internal suffix depths.

### Classifier condition

The route classifier sets:

```text
DISTRIBUTED_BRIDGE
```

when:

```text
len({b : external bridge exists at b}) >= 2.
```

The stored fields are:

```text
external = [{b,value,indices,side_counts,...}, ...]
bridge_indices = sorted({b values})
```

### Proof use

A distributed bridge cannot remain a primitive pure worse-only obstruction because it creates multiple active-to-exterior repeated partial-sum equalities.  It routes to the already-closed distributed bridge machinery.

### Attempt-witness interpretation

The rich attempt extraction now has matched attempts for all `DISTRIBUTED_BRIDGE` examples, including the formerly missing `p=23, record_index=183` case.

The symbolic proof should cite the condition:

```text
|bridge_indices| >= 2.
```

## Symbolic route case 4. EXTERNAL_BRIDGE

### Certificate label

```text
EXTERNAL_BRIDGE
```

### Symbolic meaning

There exists at least one nonterminal bridge depth

```text
b < m-1
```

and an exterior partial-sum index `e` outside the active window such that

```text
base + q + T_b = P_e.
```

This is an active-to-exterior repeated partial-sum equality.

### Classifier condition

The route classifier sets:

```text
EXTERNAL_BRIDGE
```

when there is an exterior bridge at a nonterminal `b`, and the bridge is not distributed across multiple `b` values.

Stored fields:

```text
external = [{b,value,indices,side_counts,...}, ...]
bridge_indices = [b]
```

with:

```text
b != m-1.
```

### Proof use

An external bridge is already a closed branch.  Thus zero-sum relations that create such an equality are routed and not primitive.

## Symbolic route case 5. Terminal bridge

### Certificate branch flags

```text
RIGHT_TERMINAL_BRIDGE,
LEFT_TERMINAL_BRIDGE,
SHORT_TERMINAL_BRIDGE,
LONG_TERMINAL_BRIDGE,
MIXED_TERMINAL_BRIDGE.
```

### Symbolic meaning

There is an exterior bridge relation at the terminal suffix depth

```text
b = m-1.
```

That is,

```text
base + q + T_{m-1} = P_e
```

for an exterior index `e`.

The side of `e` determines left/right terminal classification:

```text
e < i      -> left terminal,
e > j      -> right terminal.
```

The terminal support length determines short/long terminal classification.

### Proof use

Terminal bridges are already handled by the earlier terminal bridge reductions.  Therefore a zero-sum route that triggers terminal bridge flags exits the primitive branch.

## Symbolic route case 6. MIXED

### Certificate label

```text
MIXED
```

### Symbolic meaning

The selected insertion attempt triggers more than one closed route flag.

For example:

```text
CLEAN_DESCENT + EXTERNAL_BRIDGE,
CLEAN_DESCENT + SIGNED_INTERVAL,
RIGHT_TERMINAL_BRIDGE + LONG_TERMINAL_BRIDGE,
CLEAN_DESCENT + terminal bridge flags.
```

### Proof use

`MIXED` is not a primitive route type.  It means at least one closed route flag is available.  In a formal proof, choose any closed flag in the mixed attempt and route through that branch.

Thus:

```text
MIXED -> OR of closed route cases.
```

## Lemma Z proof skeleton using route cases

### Lemma Z statement

If a pure worse-only `m=3` hidden-support residual satisfies either

```text
B_tail + q = 0
```

or

```text
B_tail + q + Y_prefix = 0,
```

then it triggers at least one of the closed route cases:

```text
CLEAN_DESCENT,
SIGNED_INTERVAL,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
TERMINAL_BRIDGE.
```

### Proof skeleton

1. Convert the hidden-support zero-sum equation into a repeated partial-sum relation.

For `B_tail+q=0`:

```text
sum(B_tail) + q = 0.
```

For `B_tail+q+Y_prefix=0`:

```text
sum(B_tail) + q + sum(Y_prefix) = 0.
```

2. Locate the relation relative to the active shortest interval `Z` and the exterior partial-sum set.

3. If a local insertion strictly improves `D_short`, use CLEAN_DESCENT.

4. Otherwise, classify the repeated partial-sum equality by endpoint type:

```text
internal signed relation      -> SIGNED_INTERVAL,
multiple bridge depths        -> DISTRIBUTED_BRIDGE,
nonterminal exterior bridge   -> EXTERNAL_BRIDGE,
terminal exterior bridge      -> TERMINAL_BRIDGE.
```

5. If several flags occur simultaneously, use the MIXED rule and select any closed branch.

Therefore the zero-sum family exits through already-closed branch machinery.

## Relation to certificates

The symbolic cases above are exactly the classifier conditions used in the rich attempt witness closure:

```text
record-level route coverage: 83/83
route examples: 24/24
attempt witnesses: 24/24
```

The route-label-to-symbolic-case map is:

```text
CLEAN_DESCENT       -> D_short(new) < D_short(old)
SIGNED_INTERVAL     -> exists a,b with T_a = q + T_b
DISTRIBUTED_BRIDGE  -> at least two bridge depths b
EXTERNAL_BRIDGE     -> nonterminal active-to-exterior bridge
TERMINAL_BRIDGE     -> terminal active-to-exterior bridge
MIXED               -> at least one closed route flag among several
```

## Remaining work

To make Lemma Z publication-grade, write the endpoint-exhaustion proof showing that every zero-sum hidden-support relation must fall into the listed symbolic cases.

The rich attempt witnesses supply the empirical guide, but the proof still needs a symbolic exhaustion argument over:

```text
active interval endpoints,
q insertion cut k,
exterior partial-sum indices,
terminal depth b=m-1 versus nonterminal b<m-1.
```

## Status

```text
Zero-sum route labels translated into symbolic partial-sum cases.
Next: write endpoint-exhaustion proof for Lemma Z.
```
