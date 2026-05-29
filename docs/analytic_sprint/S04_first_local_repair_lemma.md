# S04. First local repair lemma: q-through-Z insertion

This is the first analytic brick for the low-compute sprint.

It distills the existing C2 work into a smaller lemma that can be used outside the larger phase-aware state machine.

## Purpose

Given a shortest zero interval `Z` and an adjacent outside atom `q`, insert `q` into `Z`.

Either:

```text
1. the defect decreases, or
2. a fully explicit obstruction equation appears.
```

This is the correct first target because it gives a concrete algebraic object for every failed repair.

## Setup

Let

```text
S subset F_p^*,
sigma(S) != 0,
R = X Z q Y,
Z = z_1 ... z_m,
sum(Z)=0,
q notin Z.
```

Let

```text
x = sum(X),
T_0 = 0,
T_k = z_1 + ... + z_k,   1 <= k <= m.
```

Since `Z` is a shortest zero interval:

```text
T_m = 0,
T_0,T_1,...,T_{m-1} are pairwise distinct,
T_k != 0 for 1 <= k < m.
```

The whole ordering is not just `Z`, because `sigma(S) != 0`, so at least one outside atom exists.

## Insert q into Z

For each useful position

```text
1 <= k < m,
```

insert `q` after `z_k`:

```text
R^(k) = X z_1 ... z_k q z_{k+1} ... z_m Y.
```

The local endpoint set, relative to basepoint `x`, becomes:

```text
E_k = {T_0, T_1, ..., T_k} union {q+T_k, q+T_{k+1}, ..., q+T_m}.
```

This is the key formula.

## Lemma S04.1: useful insertion destroys the active zero block

For `1 <= k < m`, the original block `Z` is no longer contiguous in `R^(k)`.

### Proof

In `R^(k)`, the block appears as

```text
z_1 ... z_k q z_{k+1} ... z_m.
```

Both sides of `q` are nonempty because `1 <= k < m`.  Therefore the atoms of `Z` no longer form a contiguous block.  The original zero interval is destroyed. ∎

## Lemma S04.2: same-side local collisions are impossible

For useful `k`, two endpoints both in

```text
{T_0,...,T_k}
```

cannot collide unless `Z` has a proper zero subinterval.

Likewise, two endpoints both in

```text
{q+T_k,...,q+T_m}
```

cannot collide unless `Z` has a proper zero subinterval.

### Proof

If `T_a=T_b` with `0 <= a < b <= k`, then

```text
z_{a+1}+...+z_b = 0,
```

which is a proper zero subinterval of `Z`.

If `q+T_a=q+T_b` with `k <= a < b <= m`, then `T_a=T_b`, so the same argument applies.  Because `k>=1`, the duplicate `T_0=T_m` of the whole zero interval is not contained inside the shifted suffix side. ∎

## Lemma S04.3: every local collision is a signed-interval obstruction

For useful `k`, any local collision inside `E_k` must be cross-side:

```text
T_a = q + T_b
```

with

```text
0 <= a <= k,
k <= b <= m.
```

Equivalently,

```text
q = T_a - T_b.
```

Thus `q` is the signed sum of a proper interval of `Z`.

### Proof

Same-side collisions are impossible by Lemma S04.2.  Therefore any local collision is cross-side.

If `a=b`, then `q=0`, impossible because `q in F_p^*`.  If `a<b`, then

```text
q = -(z_{a+1}+...+z_b).
```

If `b<a`, then

```text
q = z_{b+1}+...+z_a.
```

The interval is nonempty because `a != b`.  It is proper because the useful insertion splits `Z` and the interval uses endpoints selected from a proper prefix/suffix interface. ∎

## External endpoint set

Let `E_ext` be the set of extended partial sums of `R` outside the active local window `X Z q` except for endpoints already identified with the active collision.

A moved local endpoint collision with the external path has one of the forms:

```text
T_a = e
```

or

```text
q + T_b = e
```

where `e in E_ext`.

The first type is an unchanged collision.  If it is same-or-shorter than `Z` and earlier than `Z`, it violates the choice of `Z`.  Otherwise it is not responsible for failure of the useful insertion at the active rank.

The second type is the real external obstruction:

```text
q = e - T_b.
```

## Lemma S04.4: non-descending useful insertion forces signed or external obstruction

Let `R` be minimal under the working defect `D(R)` from S01.  Let `Z` be an active shortest zero interval.  For a useful insertion `R^(k)`, if `D(R^(k))` does not improve, then at least one of the following holds:

```text
SIGNED_INTERVAL:
  q = T_a - T_b
  for 0 <= a <= k <= b <= m, a != b.

EXTERNAL_BRIDGE:
  q + T_b = e
  for some k <= b <= m and e in E_ext.

UNCHANGED_EARLY_COLLISION:
  an unchanged old collision is same-or-shorter and not later than Z.
```

The third case should be impossible by the active choice of `Z` once the tie-breaking convention is fixed.

### Proof

By Lemma S04.1, the active zero block is destroyed.  If no same-or-earlier defect is created and no earlier unchanged defect persists, the defect improves.

Any new collision involving only local endpoints is cross-side by Lemma S04.2, hence has the signed-interval form by Lemma S04.3.

Any new collision involving a moved endpoint and an external endpoint has form `q+T_b=e` after excluding unchanged-prefix collisions.  This is the external-bridge obstruction.

Therefore non-improvement forces one of the listed cases. ∎

## Why this is the first real brick

The lemma does not solve the problem, but it converts all failed local repairs into two algebraic obstruction families:

```text
1. q is a signed interval sum of Z;
2. q shifts an internal endpoint of Z onto the external endpoint path.
```

This is much smaller than the full C3--C18 state machine.

## Immediate attack split

The proof program should now split into two branches.

### Branch A: signed interval elimination

Try to show:

```text
If q equals a signed proper interval sum of shortest zero interval Z,
then a different insertion, rotation, or two-block exchange improves D.
```

This is likely the easier branch.

### Branch B: external bridge elimination

Try to show:

```text
If every useful insertion is externally blocked,
then the translated internal prefix set q+{T_k,...,T_m}
has too much overlap with the external endpoint path,
forcing either a shorter zero interval or a repairable pair trap.
```

This is likely the highest-value hard branch.

## AI prompt for the next proof attempt

```text
We are proving Erdős 475 via the strong nonzero-sum route.
Let Z=z_1...z_m be a shortest zero-sum interval in an ordering R, with internal prefix sums T_0=0,...,T_m=0 and no proper repeated T-values.
Let q be adjacent outside Z.
For useful insertion position 1<=k<m, local endpoints are
E_k={T_0,...,T_k} union {q+T_k,...,q+T_m}.

Prove or disprove:
If for every k the insertion is blocked only by local cross-side collisions T_a=q+T_b, then there is a two-block exchange or rotation that produces a shorter zero interval or decreases collision excess.
```

## Status

```text
Status: first local repair lemma drafted.
Risk: YELLOW for S04.1--S04.3; ORANGE for S04.4 due to defect/tie-breaking bookkeeping.
Next target: signed interval elimination or external bridge overlap.
```
