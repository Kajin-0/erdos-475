# S14. Terminal bridge reduction attack

This file attacks the dominant hard external-bridge residue identified in S13.

The empirical hard-record distribution says terminal bridges dominate the no-clean-descent `m>=3` cases.  Therefore the next analytic target is an endpoint-cancellation lemma, not generic additive-energy overlap.

## Setup

Let

```text
R = X Z q Y,
Z = z_1 ... z_m,
m >= 3,
sum(Z)=0,
```

and let

```text
x = sum(X),
T_0=0,
T_b=z_1+...+z_b,
T_m=0.
```

Assume `Z` is an active shortest zero interval for the `D_short` defect.

Then

```text
T_0,T_1,...,T_{m-1}
```

are pairwise distinct.

## Right terminal bridge

A right terminal bridge for the insertion of `q` into `Z` is the collision

```text
x + q + T_{m-1} = x + q + Y_s
```

where

```text
Y_s = y_1+...+y_s
```

is a nonempty prefix sum of the right external tail after `q`.

Since

```text
T_{m-1} = -z_m,
```

this gives

```text
z_m + Y_s = 0.
```

Thus terminal bridge is an endpoint-cancellation relation:

```text
last atom of Z + right external prefix = 0.
```

## Left terminal bridge

By reversing the order, a left terminal bridge is the analogous relation:

```text
L_s + z_1 = 0
```

where `L_s` is a suffix sum of the left external block before `Z`.

Thus both terminal bridge types say:

```text
an endpoint atom of Z cancels an adjacent external interval.
```

## Key observation

Terminal bridge does not involve the whole internal geometry of `Z`.

It isolates one endpoint atom:

```text
z_m   for right terminal bridge,
z_1   for left terminal bridge.
```

Therefore terminal bridges should be handled by endpoint absorption.

## Endpoint absorption move

For right terminal bridge, write

```text
Y = Y_s Y_r,
sum(z_m Y_s)=0.
```

Consider moving the block `Y_s` immediately before `z_m`, or equivalently rotating the boundary:

```text
X z_1 ... z_{m-1} z_m q Y_s Y_r
```

into one of:

```text
X z_1 ... z_{m-1} q z_m Y_s Y_r
X z_1 ... z_{m-1} z_m Y_s q Y_r
X z_1 ... z_{m-1} Y_s z_m q Y_r
```

The goal is to make the zero block

```text
z_m Y_s
```

contiguous while disrupting the old active interval `Z`.

If

```text
1 + |Y_s| < m,
```

then this creates a shorter zero interval candidate.

## Lemma S14.1: short terminal bridge creates a shorter cross-boundary zero block

Assume a right terminal bridge

```text
z_m + y_1+...+y_s = 0.
```

If

```text
1+s < m,
```

then the block

```text
z_m y_1 ... y_s
```

is a zero-sum block of length strictly less than `m`.

Likewise, a left terminal bridge with

```text
l_s+...+l_1+z_1 = 0
```

and length `<m` gives a shorter cross-boundary zero block.

### Proof

Immediate from the terminal bridge equality and length inequality. ∎

## Consequence for D_short minimality

If endpoint absorption can make this shorter block contiguous without increasing collision excess, then `D_short` decreases.

Therefore, in a `D_short`-minimal counterexample, every short terminal bridge must be protected by an additional obstruction:

```text
SIGNED_INTERVAL
PAIR_TRAP
DISTRIBUTED_BRIDGE
or another TERMINAL_BRIDGE.
```

## Lemma S14.2: short terminal bridge reduction fork

Let `R` be `D_short`-minimal.  Suppose a right terminal bridge has support length

```text
1+s < m.
```

Then endpoint absorption gives one of:

```text
1. D_short descent;
2. signed interval obstruction;
3. pair trap obstruction;
4. distributed bridge obstruction;
5. terminal-to-terminal chain continuation.
```

The same holds for left terminal bridge by reversal.

### Proof strategy

Endpoint absorption shifts a contiguous interval of partial sums.  New collisions are again of the form

```text
shifted local endpoint = old endpoint.
```

If the collision is internal to the modified endpoint window, it is a signed interval or pair-trap relation.  If it involves an external endpoint, it is another bridge.  If it uses two bridge indices, it becomes distributed bridge.  Otherwise the shorter cross-boundary zero interval decreases `D_short`.

This is the same structural mechanism as S07/S08, but with the endpoint block `z_m Y_s` replacing `qI`.

## Long terminal bridge

The remaining hard case is:

```text
1+s >= m.
```

A long terminal bridge says the endpoint atom of `Z` cancels an external interval at least as long as `Z` minus one.

This is expensive.  In a finite ordering, many such long terminal bridges cannot be disjoint.

Therefore repeated long terminal bridges should force overlap between external intervals, hence a distributed bridge or a shorter zero interval.

## Lemma S14.3: two same-side long terminal bridges overlap or consume length

Suppose two active shortest zero intervals or two adjacent q choices produce right terminal bridges

```text
z_m + Y_s = 0,
z'_m + Y'_{s'} = 0
```

with

```text
1+s >= m,
1+s' >= m'.
```

If the external supports `Y_s` and `Y'_{s'}` overlap, subtracting the two terminal equations gives an equal-difference relation between endpoint atoms and the non-overlapping tails.

This should route to distributed bridge or pair trap.

If they are disjoint, then their total support length is large, limiting how many such terminal bridges can exist in one ordering.

### Status

This is a counting/overlap lemma, not yet proved.

## Two-sided terminal bridge

If a shortest zero interval has terminal bridges on both sides:

```text
L_s + z_1 = 0,
z_m + Y_t = 0,
```

then adding these to `sum(Z)=0` gives:

```text
L_s + (z_1+...+z_m) + Y_t = 0
```

because `sum(Z)=0`, this reduces to

```text
L_s + Y_t = 0.
```

Therefore the left external suffix and right external prefix cancel each other.

This is a cross-external zero relation.

## Lemma S14.4: two-sided terminal bridge gives external zero relation

Assume

```text
L_s + z_1 = 0,
z_m + Y_t = 0,
sum(Z)=0.
```

Then

```text
L_s + (z_2+...+z_{m-1}) + Y_t = 0
```

and also, using `z_1+...+z_m=0`,

```text
L_s + Y_t = z_1 + z_m.
```

If additionally `z_1+z_m=0`, then `z_1 z_m` is a length-2 zero interval, contradicting `m>=3` shortestness.  Thus two-sided terminal bridge creates a nontrivial endpoint-sum relation.

### Correction note

The naive claim `L_s+Y_t=0` is false unless `z_1+z_m=0`.  The actual relation is:

```text
L_s = -z_1,
Y_t = -z_m,
so L_s+Y_t = -(z_1+z_m).
```

This is still useful because if both endpoints nearly cancel externally, their endpoint sum is represented externally.

## Immediate empirical need

The next script refinement should extract terminal bridge support lengths.

For each terminal bridge record, compute:

```text
terminal side: left/right
support length s
short_terminal: 1+s < m
long_terminal: 1+s >= m
```

Then summarize hard records by:

```text
short terminal count
long terminal count
two-sided terminal count
terminal + distributed mixed count
terminal + signed mixed count
```

## Next script patch

Update `scripts/test_external_bridge_overlap.py` to include for each terminal bridge:

```json
{
  "b": m-1,
  "terminal_support_lengths": [...],
  "short_terminal": true/false,
  "long_terminal": true/false
}
```

For right terminal bridge, if external endpoint index is `idx > q_index+1`, then support length is roughly:

```text
s = idx - (q_index+1)
```

For left terminal bridge, use reversed coordinates analogously.

## Proof priority

Terminal bridge should split into:

```text
T-short: endpoint absorption gives shorter zero candidate.
T-long: support-counting / overlap / two-sided bridge argument.
```

Attack order:

```text
1. T-short terminal absorption lemma.
2. Terminal support length mining.
3. T-long overlap-counting lemma.
4. Distributed bridge reduction.
```

## Status

```text
Terminal bridge is no longer a black box.
It is endpoint cancellation.
Short terminal bridges should reduce by endpoint absorption.
Long terminal bridges should be sparse or overlapping, hence reducible by counting/equal-difference.
```
