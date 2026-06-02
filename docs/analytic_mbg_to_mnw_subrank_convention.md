# Analytic Convention: Embedding `M_BG` into `M_NW^*`

This note fixes the bridge/gap subrank convention needed to integrate F8 into F9.

Claim boundary:

```text
This is a measure-convention note.
It is not a proof of Erdős 475.
It removes one ambiguity in the F8/F9 interface.
```

---

## Purpose

F8 uses a bridge/gap-local measure:

```text
M_BG = (
  enclosing_span,
  bridge_gap,
  bridge_length,
  internal_length,
  support_size,
  recurrence_depth,
  type_rank,
  boundary_rank
).
```

F9 uses the global non-weighted measure:

```text
M_NW^* = (
  enclosing_span,
  gap_length,
  support_size,
  recurrence_depth,
  pair_depth,
  separated_depth,
  bridge_depth,
  type_rank,
  boundary_rank,
  h_excess
).
```

The first three bridge/gap coordinates map naturally:

```text
enclosing_span -> enclosing_span,
bridge_gap     -> gap_length,
support_size   -> support_size.
```

But F8 also uses:

```text
bridge_length,
internal_length.
```

These are not standalone coordinates in `M_NW^*`. This file specifies how to absorb them without changing the global measure.

---

## Principle

Bridge-local refinements must only be used after the earlier global coordinates are tied.

Therefore `bridge_length` and `internal_length` may not outrank:

```text
enclosing_span,
gap_length,
support_size,
recurrence_depth,
pair_depth,
separated_depth.
```

They are tie-breakers inside the bridge/gap class only.

---

## Convention

For any obstruction state with global class:

```text
BRIDGE_GAP,
```

interpret the global coordinate:

```text
bridge_depth
```

as a finite lexicographic bridge subrank:

```text
bridge_depth_BG = (
  bridge_cycle_depth,
  bridge_length,
  internal_length,
  bridge_orientation_rank,
  bridge_endpoint_rank
).
```

Thus, inside a BRIDGE_GAP state:

```text
bridge_depth := encode_lex(bridge_depth_BG)
```

where `encode_lex` is any order-preserving embedding of a finite lexicographic tuple into a nonnegative integer over the fixed finite active support.

For non-bridge states, keep the ordinary meaning:

```text
bridge_depth = 0
```

unless the state is an inherited bridge-return state awaiting F8 routing.

---

## Components

### 1. `bridge_cycle_depth`

Counts consecutive bridge/gap returns since the last strict decrease in one of:

```text
enclosing_span,
gap_length,
support_size.
```

It is reset to zero after any strict decrease or exit to a non-bridge class.

### 2. `bridge_length`

For a bridge relation:

```text
B_ext + U + E = 0
```

or signed variant, define:

```text
bridge_length = |B_ext|.
```

This is a local tie-breaker only.

### 3. `internal_length`

Define:

```text
internal_length = |U|.
```

This is also a local tie-breaker only.

### 4. `bridge_orientation_rank`

Use finite orientation ranks:

```text
0. no bridge / exited bridge class;
1. overlap or containment bridge;
2. separated same-orientation bridge B G U;
3. separated exchange-orientation bridge U G B;
4. signed bridge correction;
5. weighted-core exit pending.
```

The exact numeric order may be changed in the final manuscript, but it must be finite and must place weighted-core exit outside nonweighted cycles.

### 5. `bridge_endpoint_rank`

Use finite endpoint ranks for rigid-return cases:

```text
0. no endpoint degeneracy;
1. proper prefix/tail endpoint;
2. endpoint U / adjacent-equal midpoint route;
3. endpoint G / cyclic-external route;
4. zero inside G;
5. signed correction endpoint.
```

Again, the final manuscript may choose a different finite order, but every rigid-return endpoint case must be assigned exactly one finite rank.

---

## Embedding into `M_NW^*`

The final global bridge/gap embedding is:

```text
M_BG.enclosing_span       -> M_NW^*.enclosing_span
M_BG.bridge_gap           -> M_NW^*.gap_length
M_BG.support_size         -> M_NW^*.support_size
M_BG.recurrence_depth     -> M_NW^*.recurrence_depth
M_BG.bridge-local subrank -> M_NW^*.bridge_depth
M_BG.type_rank            -> M_NW^*.type_rank
M_BG.boundary_rank        -> M_NW^*.boundary_rank
```

where:

```text
bridge-local subrank = (
  bridge_cycle_depth,
  bridge_length,
  internal_length,
  bridge_orientation_rank,
  bridge_endpoint_rank
).
```

Thus F8 does not require a new global measure. It refines the existing `bridge_depth` coordinate.

---

## Strict-decrease rules

An F8 transition is acceptable for F9 if it satisfies one of the following.

### Rule B1: earlier global coordinate decreases

One of:

```text
enclosing_span,
gap_length,
support_size,
recurrence_depth,
pair_depth,
separated_depth
```

decreases before `bridge_depth` is considered.

### Rule B2: bridge-local subrank decreases

All earlier global coordinates are unchanged, but:

```text
bridge_depth_BG(child) < bridge_depth_BG(parent)
```

lexicographically.

This applies to bridge-only tie-breaking cases such as:

```text
proper endpoint shortening,
smaller bridge interval,
smaller internal interval,
orientation normalization,
rigid endpoint-rank reduction.
```

### Rule B3: finite bridge return exits

The branch exits from `BRIDGE_GAP` to one of:

```text
F4 local descent,
F5 separated-equal/midpoint,
F6 external collision,
F7 recurrence,
F10/F11 weighted core,
SUCCESS,
CONTRADICTION.
```

Then F8 no longer owns the measure descent; the destination theorem must consume the edge.

### Rule B4: weighted exit

If the branch exits to:

```text
WEIGHTED_CORE,
```

then it is removed from the nonweighted graph and must terminate by F10/F11.

This is not an F8 closure by itself. It remains a theorem dependency.

---

## Application to F8 cases

### Proper overlap

Decrease:

```text
enclosing_span.
```

No subrank needed.

### Proper containment

Decrease:

```text
support_size
```

and sometimes:

```text
enclosing_span.
```

No subrank needed.

### Successful gap-after move

Decrease:

```text
gap_length: |G| -> 0.
```

No subrank needed.

### Proper-gap recurrence

Decrease:

```text
gap_length
```

because a proper prefix/tail of `G` is used.

No subrank needed.

### Same-gap rigid return

Earlier global coordinates may tie. Then use:

```text
bridge_depth_BG.
```

The final endpoint table must show that one of:

```text
bridge_length,
internal_length,
bridge_orientation_rank,
bridge_endpoint_rank
```

decreases, or that the branch exits to F5/F6/F7/F10/F11.

### Signed bridge correction

If the correction is bounded and remains nonweighted, assign a finite orientation/endpoint rank and route through F4/F6/F7.

If the correction is irreducibly weighted, use:

```text
WEIGHTED_EXIT_TO_F10_F11.
```

---

## Important limitation

This convention does not prove F8 or F9.

It only removes the ambiguity of where the F8-local coordinates live inside `M_NW^*`.

The remaining required proof is still:

```text
For every F8 edge, verify either:
  1. earlier global coordinate decrease;
  2. bridge_depth_BG subrank decrease;
  3. exit to a destination theorem;
  4. terminal success/contradiction;
  5. weighted exit to F10/F11.
```

---

## Consequence for F8/F9

After adopting this convention, F8 should cite:

```text
docs/analytic_mbg_to_mnw_subrank_convention.md
```

when discussing `M_BG` embedding.

F9 should cite the same file when interpreting:

```text
bridge_depth
```

inside the global measure.

---

## Status

This closes the measure-notation ambiguity:

```text
M_BG.bridge_length/internal_length are absorbed into M_NW^*.bridge_depth as finite bridge-local subrank.
```

It does not close:

```text
F10/F11 weighted-core termination;
F9 edge-by-edge global descent;
F8 rigid-return endpoint table;
F5 direct-exchange endpoint table.
```
