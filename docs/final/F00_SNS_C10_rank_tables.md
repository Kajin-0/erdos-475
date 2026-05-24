# F00.SNS.C10 rank tables for phase-aware termination

This file continues the strong nonzero-sum repair path.

C9 proposed the global phase-aware measure

```text
M_phase(Omega)=(
  D_SNS^*(R),
  phase_rank,
  M_loc,
  M_w,
  transition_budget
).
```

C9 also identified the next requirement:

```text
Make type_rank, boundary_rank, and local-depth ranks explicit.
```

C10 supplies those finite rank tables.  This file is still a draft: the tables make the termination framework checkable, but each edge must still be verified against the table.

---

## C10.1. Rank-table design rule

Ranks are not mathematical invariants by themselves.  They are finite tie-breakers used only after the dominant geometric coordinates have failed to decrease.

The intended priority is:

```text
1. D_SNS^*(R)
2. phase_rank
3. enclosing_span
4. gap_length
5. support_size
6. bridge/pair/separated depths
7. type_rank
8. boundary_rank
9. transition_budget
```

Thus `type_rank` and `boundary_rank` should only be invoked when span/gap/support coordinates are unchanged.

---

## C10.2. Phase rank

Use:

```text
phase_rank(COLLISION_FREE)=0
phase_rank(ARBITRARY)=1
```

`COLLISION_FREE` is terminal success for strong nonzero-sum, so this coordinate is mostly symbolic.

---

## C10.3. Obstruction type ranks

Use the following finite type-rank table in ARBITRARY phase.

| Type | rank | Meaning |
|---|---:|---|
| SUCCESS | 0 | collision-free terminal success |
| DEFECT_DESCENT | 1 | strict `D_SNS^*` descent |
| ZERO_DEFECT | 2 | zero interval repair state |
| LOCAL_ZERO_COMPOSITE | 3 | two/higher-piece zero repair |
| EQUAL_INTERVAL | 4 | overlap/containment/disjoint equal interval |
| SIGNED_INTERVAL | 5 | signed interval with bounded atom correction |
| PAIR_DIFFERENCE | 6 | atom-pair boundary relation |
| SEPARATED_EQUAL | 7 | disjoint equal interval with gap |
| MIDPOINT_ADJACENT | 8 | adjacent equal / midpoint branch |
| BRIDGE_GAP | 9 | external bridge or separated bridge repair |
| EXTERNAL_COLLISION | 10 | moved endpoint collides with external endpoint |
| TRANSPORTED_PREFIX | 11 | transported prefix/tail normalization |
| WEIGHTED_REPAIR | 12 | genuine coefficient-2 weighted repair |
| CYCLIC_WRAP | 13 | cyclic/wrapped collision data |
| BOUNDARY_DEGENERACY | 14 | endpoint/empty-block degeneracy |
| UNCLASSIFIED | 99 | should not appear in final proof |

The final proof should never use `UNCLASSIFIED`; it is a diagnostic sentinel.

---

## C10.4. Type-rank descent policy

The table is ordered so that normalization should generally move downward:

```text
WEIGHTED_REPAIR -> TRANSPORTED_PREFIX or local repair;
TRANSPORTED_PREFIX -> local zero/equal/signed repair;
EXTERNAL_COLLISION -> BRIDGE_GAP or local repair;
BRIDGE_GAP -> SEPARATED_EQUAL or local repair;
SEPARATED_EQUAL -> EQUAL_INTERVAL/local repair or SUCCESS;
SIGNED/PAIR -> LOCAL_ZERO/EQUAL/ZERO_DEFECT or DEFECT_DESCENT.
```

A transition is type-rank-valid only if either:

```text
1. a dominant coordinate decreases; or
2. type_rank decreases; or
3. the transition enters a finite subroutine with transition_budget decreasing.
```

---

## C10.5. Boundary rank

Boundary rank tracks endpoint degeneracy only after all dominant coordinates are fixed.

Use:

| Boundary status | rank | Meaning |
|---|---:|---|
| INTERIOR_USEFUL | 0 | all active pieces nonempty; insertion/cut occurs strictly inside block |
| ONE_FULL_PREFIX | 1 | one prefix/tail equals a full block |
| ONE_EMPTY_PREFIX | 2 | one prefix/tail is empty by endpoint convention |
| ADJACENT_ENDPOINT | 3 | equal blocks adjacent; midpoint/endpoint branch |
| OUTER_CONTEXT_EMPTY | 4 | `X`, `Y`, `A`, or `C` empty in a boundary-sensitive way |
| CYCLIC_ENDPOINT | 5 | endpoint wraps under cyclic representation |
| DEGENERATE_REWRITE | 6 | rewrite uses empty or full support in a non-generic way |
| BOUNDARY_UNCLASSIFIED | 99 | diagnostic sentinel |

Interior useful insertions in the q-through-Z repair have boundary rank `0`.

---

## C10.6. Depth ranks

Depth coordinates prevent repeated cycling at fixed span/gap/support/type.

Use:

```text
bridge_depth      = number of consecutive bridge/gap returns at fixed D_SNS^*, span, gap, support;
pair_depth        = number of consecutive pair/signed returns at fixed D_SNS^*, span, support;
separated_depth   = number of consecutive separated-equal returns at fixed D_SNS^*, gap, support;
weighted_depth    = number of consecutive weighted returns at fixed D_SNS^* and |B|;
cyclic_depth      = number of consecutive cyclic/wrapped returns at fixed D_SNS^*.
```

Each depth must be explicitly bounded by a finite number of local endpoint configurations.  A safe crude bound is:

```text
local_config_count <= 2^t * t^4
```

but the final proof should use smaller local bounds whenever possible.

---

## C10.7. Transition budget

For a finite displayed table or finite q-through-Z insertion sequence, define:

```text
transition_budget = number of untested local alternatives remaining.
```

Examples:

```text
q-through-Z useful insertions: m-1 positions;
cut-swap displayed collision table: finite moved-family pair comparisons;
gap-after table: finite E-branch comparisons;
direct-exchange table: finite D-branch comparisons.
```

Every table scan must either:

```text
1. find a descending/successful move;
2. find a routed obstruction;
3. exhaust the finite budget and produce a rigidity statement.
```

---

## C10.8. Rank assignment for C1--C7 outputs

| Source | Output | Type rank | Boundary rank policy |
|---|---|---:|---|
| C1 strongly clean insertion | DEFECT_DESCENT | 1 | unchanged or lower |
| C2 local cross collision | SIGNED_INTERVAL / PAIR_DIFFERENCE | 5/6 | interior if `1<=k<m` |
| C2 moved external collision | EXTERNAL_COLLISION | 10 | depends on context side |
| C2 useful insertion success | SUCCESS | 0 | interior useful |
| C4 moved-moved collision | LOCAL_ZERO / EQUAL / SIGNED | 3--5 | from endpoint case |
| C4 moved-unchanged collision | EQUAL / PAIR / TRANSPORTED | 4/6/11 | from endpoint case |
| C4 moved-external collision | EXTERNAL_COLLISION | 10 | context side |
| C5 zero output | ZERO_DEFECT | 2 | endpoint convention |
| C5 separated output | SEPARATED_EQUAL | 7 | gap nonempty |
| C5 bridge output | BRIDGE_GAP | 9 | bridge endpoint policy |
| C6 weighted output | WEIGHTED_REPAIR | 12 | cut endpoint policy |
| C7 pattern-rigid exit | ZERO_DEFECT | 2 | internal cut boundary |

---

## C10.9. Required descent checks by rank row

Each output row has a required proof obligation.

### ZERO_DEFECT

Must show one of:

```text
1. its span is smaller than the active zero interval, contradiction to minimality;
2. its span/location improves D_SNS^*;
3. it becomes the new active repair state with lower local measure.
```

### LOCAL_ZERO_COMPOSITE

Must show uncrossing or merging decreases:

```text
enclosing_span or support_size,
```

or routes to `ZERO_DEFECT` with controlled span.

### EQUAL_INTERVAL

Must show:

```text
proper overlap -> enclosing_span decreases;
proper containment -> support_size decreases;
disjoint -> SEPARATED_EQUAL with gap coordinate.
```

### SIGNED_INTERVAL / PAIR_DIFFERENCE

Must show bounded correction either:

```text
absorbs into local zero/equal data;
routes to pair repair with pair_depth decreasing;
routes to EXTERNAL_COLLISION if outside local window;
routes to WEIGHTED_REPAIR only if coefficient-2 form is genuine.
```

### SEPARATED_EQUAL / MIDPOINT

Must show direct exchange or gap-after move either:

```text
succeeds;
creates classified collision;
decreases gap/support;
uses finite transition_budget;
routes to BRIDGE_GAP or WEIGHTED_REPAIR with dominant coordinate controlled.
```

### BRIDGE_GAP / EXTERNAL_COLLISION

Must show:

```text
proper overlap/containment decreases local measure;
disjoint separated bridge decreases gap or enters finite rigid return;
external collision pullback does not increase D_SNS^* without producing a classified defect.
```

### WEIGHTED_REPAIR

Must show:

```text
easy reductions lower type_rank;
cut-swap collision exits to lower type_rank or smaller |B|;
weak cut-rigidity reduces to pattern-rigidity or defect descent;
pattern-rigidity exits to ZERO_DEFECT.
```

---

## C10.10. Finite-rank theorem, conditional

## Theorem C10.1: finite-rank framework

Assume every transition satisfies the required descent check for its rank row in C10.9.  Then the rank portion of `M_phase` cannot support an infinite same-profile repair path.

### Proof

The rank coordinates are finite nonnegative integers.  At fixed `D_SNS^*`, fixed span/gap/support, and fixed weighted length, a transition must either decrease a finite rank/depth coordinate or enter a finite transition-budget subroutine.  Such a process cannot be infinite. ∎

---

## C10.11. What C10 resolves

Resolved:

```text
1. explicit type_rank table;
2. explicit boundary_rank table;
3. explicit depth-rank definitions;
4. transition_budget convention;
5. rank-row proof obligations.
```

Not resolved:

```text
1. proving every edge satisfies its rank-row obligation;
2. hardening phase-aware weighted weak cut-rigidity;
3. completing the global SNS proof.
```

---

## C10.12. Recommended next file

The next file should verify the rank-row obligations for the non-weighted local classes first:

```text
docs/final/F00_SNS_C11_local_rank_descent_verification.md
```

Goal:

```text
Check ZERO_DEFECT, LOCAL_ZERO_COMPOSITE, EQUAL_INTERVAL, SIGNED_INTERVAL, PAIR_DIFFERENCE, and SEPARATED_EQUAL rows before touching weighted repair again.
```

---

## C10.13. Status

```text
Status: rank-table draft.
Risk: ORANGE.
Current remaining gap: rank-row descent verification.
```
