# S11. External bridge overlap attack

This file starts the final primitive obstruction after the S10 pair-trap reduction.

The current analytic chain is:

```text
q-through-Z failure
  -> signed interval or external bridge
  -> q-zero compression
  -> pair trap or external bridge
  -> pair-trap block move
  -> D_short descent or external bridge.
```

So the remaining hard case is:

```text
persistent external bridge overlap.
```

## Setup

Let `R` be an ordering of `S subset F_p^*` with `sigma(S) != 0`.

Let

```text
R = X Z q Y,
Z = z_1 ... z_m,
sum(Z)=0,
q outside Z,
```

and let

```text
x = sum(X),
T_0 = 0,
T_b = z_1 + ... + z_b,   1 <= b <= m.
```

Thus

```text
T_m = 0.
```

If `Z` is shortest, then

```text
T_0,T_1,...,T_{m-1}
```

are pairwise distinct.

The insertion of `q` after `z_k`, with `1 <= k < m`, has local endpoint set relative to basepoint `x`:

```text
E_k = {T_0,...,T_k} union {q+T_k,...,q+T_m}.
```

## Boundary endpoints must be excluded

The endpoint

```text
q+T_m = q
```

is the unchanged endpoint after `q` in the old ordering.

Therefore it must not count as a true external obstruction.

Likewise the duplicated active endpoint

```text
T_0 = T_m = 0
```

is the old active zero interval endpoint and must be handled separately.

## True external bridge definition

A true external bridge for insertion position `k` is a collision

```text
x + q + T_b = P_a
```

with

```text
k <= b <= m-1,
```

where `P_a` is an old extended partial sum outside the active local window and not one of the boundary endpoints already preserved by the move.

Equivalently, relative to `x`:

```text
q + T_b in E_ext,
```

where `E_ext` is the external endpoint set after removing the preserved boundary endpoints.

## Persistent bridge condition

If every useful insertion is blocked externally after signed/pair-trap reductions, then for every

```text
1 <= k < m
```

there exists some

```text
b in {k,k+1,...,m-1}
```

such that

```text
q + T_b in E_ext.
```

Define the blocker-index set:

```text
B_q = { b in {1,...,m-1} : q+T_b in E_ext }.
```

Then persistent external blocking is equivalent to:

```text
for every k in {1,...,m-1}, B_q intersects {k,...,m-1}.
```

Equivalently:

```text
max(B_q) = m-1.
```

This is a key discovery: a single terminal blocker `b=m-1` can formally block every insertion position if the obstruction definition is too weak.

Therefore the proof cannot rely merely on one bridge per insertion.

## New split: terminal bridge vs distributed bridge

External bridge must split into two regimes.

### Regime E1: terminal bridge

```text
q + T_{m-1} in E_ext.
```

Since

```text
T_{m-1} = -z_m,
```

this says

```text
q - z_m in E_ext.
```

This is a rigid endpoint relation involving only the atom adjacent to the right end of `Z`.

It should be attacked directly, not by additive-energy language.

### Regime E2: distributed bridge

There are multiple blocker indices:

```text
|B_q| >= 2
```

or better, blocker indices occur away from `m-1`.

Then the translated internal prefix set

```text
q + {T_b : b in B_q}
```

has genuine overlap with external endpoints, and differences between two blockers give:

```text
T_b - T_c = e_b - e_c.
```

This is a pair-trap-like equal-difference relation between an internal interval of `Z` and an external interval of the endpoint path.

## Terminal bridge analysis

Assume the external endpoint lies to the right of `q` in `Y`:

```text
P_a = x + q + Y_s,
```

where

```text
Y_s = y_1 + ... + y_s.
```

The terminal bridge equality is:

```text
x + q + T_{m-1} = x + q + Y_s.
```

So

```text
T_{m-1} = Y_s.
```

Since `T_{m-1}=-z_m`,

```text
z_m + Y_s = 0.
```

After inserting `q` before `z_m`, the block

```text
z_m y_1 ... y_s
```

is contiguous and has zero sum.

Its length is

```text
1+s.
```

If

```text
1+s < m,
```

this produces a shorter zero interval after the move and should force `D_short` descent unless another external bridge appears.

If

```text
1+s >= m,
```

then the bridge reaches far into the external path and should be charged to a long external support.

## Lemma S11.1: right-terminal bridge gives shorter cross-boundary zero unless long

Assume

```text
q+T_{m-1} = q+Y_s
```

with the external endpoint to the right of `q`. Then

```text
z_m + y_1 + ... + y_s = 0.
```

After moving `q` before `z_m`, this is a contiguous zero interval of length `1+s`.

Thus either:

```text
1. 1+s < m, giving a shorter zero interval candidate;
2. 1+s >= m, giving a long right bridge.
```

The first case should route to `D_short` descent or pair trap/external bridge by the already developed machinery.

## Left-terminal bridge analysis

If the external endpoint lies to the left of `Z`, write it as

```text
P_a = x - L_s,
```

where `L_s` is the sum of the suffix of `X` after `P_a` and before `Z`.

The bridge equality

```text
x + q + T_{m-1} = x - L_s
```

becomes

```text
L_s + q + T_{m-1} = 0.
```

Since `T_{m-1}=-z_m`,

```text
L_s + q - z_m = 0.
```

This is not immediately a zero interval in the old ordering, but after moving `q` near `z_m` it becomes a cross-boundary relation involving the left suffix and the right endpoint atom.

This is harder than the right bridge and should be recorded as `LEFT_TERMINAL_BRIDGE`.

## Distributed bridge analysis

Suppose there are two blocker indices:

```text
b<c,
q+T_b=e_b,
q+T_c=e_c.
```

Subtract:

```text
T_c - T_b = e_c - e_b.
```

The left side is the sum of the internal interval

```text
z_{b+1}+...+z_c.
```

The right side is a difference of external endpoints, hence the sum of an external interval along the old endpoint path, possibly with orientation.

Thus distributed bridges create an internal-external equal-interval-sum relation.

This is the external analogue of pair trap.

## Lemma S11.2: two bridge blockers give internal-external equal-difference

If

```text
q+T_b=e_b,
q+T_c=e_c,
b<c,
```

then

```text
T_c-T_b=e_c-e_b.
```

Therefore the internal interval `Z[b+1,c]` has the same oriented sum as an external endpoint interval.

### Consequence

A block exchange between the internal interval and the external interval should either:

```text
1. decrease D_short;
2. create an ordinary pair trap;
3. create a shorter zero interval crossing the boundary;
4. expose a terminal bridge.
```

## Strategic pivot

Persistent bridge is not one case. It splits into:

```text
E1R: right terminal bridge
E1L: left terminal bridge
E2: distributed bridge
```

The strongest next attack is E1R because it gives an explicit cross-boundary zero interval.

## Candidate theorem S11.3: terminal bridge reduction theorem

Let `R` be `D_short`-minimal and let `Z` be an active shortest zero interval. Suppose every useful q-through-Z insertion is externally blocked and the only blocker is the terminal blocker

```text
q+T_{m-1} in E_ext.
```

If the corresponding external endpoint lies to the right of `q`, then either:

```text
1. D_short descends after moving q before z_m;
2. a signed interval obstruction occurs and routes through S07;
3. a pair trap occurs and routes through S10;
4. the bridge support length is at least m-1.
```

Thus a pure right-terminal bridge cannot be short.

## Candidate theorem S11.4: distributed bridge reduction theorem

If persistent external bridge uses at least two blocker indices, then the bridge equations produce an internal-external equal-difference relation. A block exchange along that relation either decreases `D_short`, routes to pair trap, or reduces to terminal bridge.

## Low-compute test target

Create a script:

```text
scripts/test_external_bridge_overlap.py
```

The script should:

```text
1. sample defective orderings;
2. choose a shortest zero interval Z;
3. choose adjacent q on either side;
4. test useful q-through-Z insertions;
5. classify blockers as:
   - CLEAN
   - SIGNED_INTERVAL
   - PAIR_TRAP
   - RIGHT_TERMINAL_BRIDGE
   - LEFT_TERMINAL_BRIDGE
   - DISTRIBUTED_BRIDGE
6. count whether every blocked case routes to known branches.
```

## Current status

```text
External bridge is now the primitive hard case.
Major insight: naive persistent bridge reduces only to max(B_q)=m-1, so terminal bridge must be separated from distributed bridge.
Next priority: build the external bridge classifier and test terminal/distributed frequency.
```
