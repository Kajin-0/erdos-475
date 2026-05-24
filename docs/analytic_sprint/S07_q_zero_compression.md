# S07. q-zero compression and defect pivot

This file attacks the main gap left by S06.

S06 showed that a signed-interval obstruction exposes a shorter zero-sum structure involving the outside atom `q`:

```text
q + sum(I) = 0,
I a proper interval of Z,
|I| <= m-2.
```

The question is how to turn this into analytic progress.

## Key correction: the defect ordering must favor shorter active defects

The S01 working defect used an inverse shortest length coordinate:

```text
K_min = t + 1 - L_min.
```

This effectively made shorter zero intervals worse among equal collision-excess orderings.

That is counterproductive for the signed-interval attack.  S06 naturally produces a shorter zero interval involving `q`.  To exploit that as descent, the extremal ordering should instead minimize the shortest zero-interval length after minimizing collision excess.

Therefore the better analytic defect for this branch is:

```text
D_short(R) = (
  E(R),
  L_min(R),
  N_min(R),
  M(R)
)
```

with lexicographic minimization, where:

```text
E(R)     = collision excess of extended partial sums;
L_min(R) = shortest zero-interval length, with infinity if E=0;
N_min(R) = number of zero intervals of length L_min;
M(R)     = repeated partial-sum multiplicity profile.
```

Since `E=0` is terminal success, `L_min` is only relevant inside the defective regime `E>0`.

## Why this defect is stronger for a solo analytic attack

If a local move preserves `E` but creates a strictly shorter zero interval, then it improves `D_short`.

Thus S06's signed-interval output becomes useful rather than harmful.

This is the first major correction from reading the existing work and testing the proof shape.

## Setup

Let

```text
R = X Z q Y,
Z = A I C,
I = z_{a+1}...z_b,
sum(Z)=0,
q + sum(I)=0,
|I| <= m-2.
```

Here `Z` is a shortest zero interval in `R`, with length

```text
m = |Z|.
```

Because `|I| <= m-2`, the complement of `I` inside `Z` contains at least two atoms total.

Let

```text
r = |I|.
```

Then

```text
r + 1 <= m - 1.
```

The block `q I` has zero sum and length `r+1`, strictly shorter than `Z`.

## Move family: compress q onto I

There are two natural compression moves.

### Move C_left

Move `q` immediately before `I`:

```text
X A I C q Y  ->  X A q I C Y.
```

Then `q I` is contiguous and zero-sum.

### Move C_right

Move `q` immediately after `I`:

```text
X A I C q Y  ->  X A I q C Y.
```

Then `I q` is contiguous and zero-sum.

Both create a zero interval of length `r+1 < m`.

## Lemma S07.1: q-compression preserves total ordering support

Both `C_left` and `C_right` are permutations of the same set `S`, so they are admissible reorderings.

### Proof

Each move removes `q` from its old position and inserts it next to `I`.  No atom is added, removed, or duplicated. ∎

## Lemma S07.2: q-compression destroys the original Z interval unless q is inserted outside Z

If `q` is moved into the interior of `Z` next to `I`, then the original contiguous block `Z` is split by `q`, so the old zero interval `Z` is destroyed.

### Proof

The old block was

```text
A I C.
```

After compression it becomes either

```text
A q I C
```

or

```text
A I q C.
```

If both sides of the inserted `q` inside `Z` are not simultaneously empty, the old sequence `A I C` is no longer contiguous.  Since `I` is a proper interval and `|I| <= m-2`, at least one of `A,C` is nonempty, and the insertion is interior relative to the old `Z` unless `I` is an endpoint interval with all complement on one side.  Even in the endpoint case, inserting `q` adjacent to `I` but inside `Z` separates one side of `Z` from `I`. ∎

## Lemma S07.3: if compression does not increase collision excess, signed obstruction is impossible in a D_short-minimal ordering

Let `R` be `D_short`-minimal among all orderings of `S`.  Suppose a signed-interval obstruction gives an interval `I subset Z` with

```text
q + sum(I)=0,
|I| <= m-2.
```

If either `C_left` or `C_right` has collision excess at most `E(R)`, then `R` was not `D_short`-minimal.

### Proof

The compression move creates a zero interval `qI` or `Iq` of length

```text
|I|+1 <= m-1.
```

By assumption, the resulting ordering has collision excess at most `E(R)`.  Since `R` was chosen to minimize `E`, the collision excess cannot be less unless we are already done by contradiction.  Therefore it must equal `E(R)`.

But the new ordering has a zero interval of length `<m`, so its `L_min` is at most `|I|+1 < m = L_min(R)`.  Hence it is lexicographically smaller in `D_short`, contradicting minimality. ∎

## Consequence

In a `D_short`-minimal counterexample, every q-compression move arising from a signed-interval obstruction must increase collision excess.

Therefore the only way signed obstruction survives is by creating at least two new collisions for each destroyed old collision.

This is a much sharper statement.

## What new collision can compression create?

The compression move shifts a contiguous family of partial sums by `+q` or `-q`.

As in S02, new collisions must have form

```text
P_u ± q = P_v.
```

Equivalently:

```text
q = ±(P_v-P_u).
```

There are three types.

```text
LOCAL-LOCAL:
  both endpoints are inside the old Z-window.

LOCAL-EXTERNAL:
  one endpoint is inside the moved Z-window and one is outside.

EXTERNAL-EXTERNAL:
  impossible as a new collision, because external endpoints are unchanged.
```

The compression-created short zero interval is intentional.  Any additional collision must be local-local or local-external.

## Lemma S07.4: local-local extra collisions produce pair-trap equations

If q-compression creates a local-local collision besides the intentional short zero interval, then there are two interval sums inside `Z` with equal difference.  Equivalently, a pair-trap/equal-difference relation occurs.

### Proof sketch

A local-local collision after shifting one local block by `q` has form

```text
T_u + q = T_v
```

or

```text
T_u - q = T_v.
```

The signed obstruction already gives

```text
q = T_a - T_b.
```

Substituting gives

```text
T_u + T_a - T_b = T_v
```

or

```text
T_u - T_a + T_b = T_v.
```

Rearranging yields an equal-difference relation:

```text
T_u - T_v = T_b - T_a
```

or

```text
T_u - T_v = T_a - T_b.
```

These are exactly pair-trap equations among internal prefix sums of `Z`. ∎

## Lemma S07.5: local-external extra collisions are external bridge obstructions

If q-compression creates a collision involving one endpoint outside the old `Z q` window, then it is an external bridge obstruction.

### Proof

The external endpoint is unchanged.  The local endpoint moved by `±q`.  Therefore the new equality has form

```text
T_u ± q = e,
```

where `e` is an external endpoint.  This is exactly the external bridge pattern. ∎

## Theorem S07.6: signed obstruction compression theorem

Let `R` be `D_short`-minimal and let `Z` be a shortest zero interval.  Suppose a q-through-Z insertion is blocked by a signed-interval obstruction.

Then at least one of the following holds:

```text
1. contradiction to D_short-minimality;
2. pair-trap/equal-difference relation inside Z;
3. external bridge obstruction.
```

### Proof

By S06, the signed obstruction gives a proper interval `I subset Z` with

```text
q + sum(I)=0,
|I| <= m-2.
```

Apply `C_left` or `C_right`.  If either compression move does not increase collision excess, Lemma S07.3 gives contradiction to `D_short`-minimality.

Thus every compression move increases collision excess.  Any new extra collision is either local-local or local-external, since external-external endpoints are unchanged.  Local-local collisions yield pair-trap equations by Lemma S07.4.  Local-external collisions are external bridge obstructions by Lemma S07.5. ∎

## Strategic consequence

Signed-interval obstruction is no longer a primitive hard case.

It reduces to:

```text
PAIR_TRAP
or
EXTERNAL_BRIDGE.
```

Therefore the main theorem can focus on eliminating persistent external bridge and pair-trap obstructions.

## Why this is promising

This is exactly the type of compression that can beat brute force:

```text
many local failure cases -> two structural obstruction families.
```

The proof does not need large computation.  It needs careful endpoint bookkeeping and a clean defect choice.

## Required update to earlier sprint files

S01 should be amended:

```text
Replace D=(E,M,K_min,N_min) with D_short=(E,L_min,N_min,M)
for the signed-compression branch.
```

The older `K_min` version can remain as an alternate defect, but it should not drive the main analytic attack.

## Next target

Attack pair traps before external bridge.

Reason:

```text
Pair traps are internal to Z and likely easier.
External bridge involves the outside path and is the true hard case.
```

Next file:

```text
docs/analytic_sprint/S08_pair_trap_elimination.md
```

Target theorem:

```text
A pair-trap/equal-difference relation inside a shortest zero interval either
creates a shorter zero interval after a two-block exchange or gives a compression move reducing D_short.
```

## Status

```text
Status: promising proof skeleton.
Risk: ORANGE.
Main vulnerability: Lemma S07.3 requires precise accounting of collision excess under compression.
But the branch reduction is sharp and worth pursuing first.
```
