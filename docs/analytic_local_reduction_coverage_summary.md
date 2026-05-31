# Analytic Coverage Summary: Local Reduction Modules

This file indexes the local-reduction modules produced during the template-aware proof reconstruction.

Claim boundary:

```text
This is a coverage/index note, not a proof of Erdős 475.
It records which local branches are now packaged and which global work remains.
```

---

## Main correction captured by this phase

The proof must use a fixed-ordering obstruction tree and template-aware external cancellations.

External collisions are not safely represented by bare labels such as:

```text
Left(T), Right(T).
```

They must retain the proposed prefix/suffix that collided.

The central normal form is:

```text
pi(H)=A,B.

Left external collision:
  K + A = 0.

Right external collision:
  B + K = 0.
```

where `K` is the adjacent real interval outside the active block.

This correction is documented in:

```text
docs/PROOF_PROGRESS_CHECKPOINT.md
docs/analytic_template_external_cancellation_t1.md
```

---

## Packaged first-blocker templates

### T1: right blocker, length at least two

Template:

```text
a,b,z,J -> z,a,b,J
```

with

```text
sum(J)=-a-z.
```

Status:

```text
Packaged as a complete local external-cancellation theorem.
```

Main file:

```text
docs/analytic_template_t1_external_cancellation_theorem.md
```

Subcase files:

```text
docs/analytic_template_external_cancellation_t1.md
docs/analytic_template_external_cancellation_t1_lz_long.md
docs/analytic_template_external_cancellation_t1_rz_singleton.md
docs/analytic_template_external_cancellation_t1_rz_long_attempt.md
docs/analytic_template_bridge_routing_t1_rz.md
docs/analytic_template_external_cancellation_t1_lza_singleton.md
docs/analytic_template_external_cancellation_t1_lza_long.md
docs/analytic_template_external_cancellation_t1_rza_singleton.md
docs/analytic_template_external_cancellation_t1_rza_long.md
```

Outcome menu:

```text
success,
affine/singleton,
proper prefix/suffix/internal subinterval,
further template-aware external cancellation,
smaller-enclosure bridge/gap,
impossible or boundary-sensitive condition.
```

---

### T2: left blocker, length at least two

Template:

```text
J,z,a,b -> J,a,b,z
```

with

```text
sum(J)=-b-z.
```

Status:

```text
Packaged by mirror symmetry from T1.
```

Main file:

```text
docs/analytic_template_t2_mirror_theorem.md
```

Outcome menu is the mirror of T1.

---

### T3: right singleton blocker

Template:

```text
a,b,-a -> -a,b,a
```

Status:

```text
Classified and routed.
```

Main files:

```text
docs/analytic_template_t3_right_singleton_blocker.md
docs/analytic_template_t3_external_routing.md
```

Branches:

```text
scalar branch:
  b=2a -> scalar absorption.

external branches:
  E1 -> duplicate-left   Left(a),
  E4 -> duplicate-right  Right(-a),
  E3 -> generic-left     Left(a-b),
  E2 -> generic-right    Right(-a-b).
```

External branches depend on the generic/duplicate interval modules below.

---

### T4: left singleton blocker

Template:

```text
-b,a,b -> b,a,-b
```

Status:

```text
Packaged by mirror symmetry from T3.
```

Main file:

```text
docs/analytic_template_t4_mirror_singleton_blocker.md
```

Branches:

```text
scalar branch:
  a=2b -> mirror scalar absorption.

duplicate branches:
  Left(-b), Right(b).

generic branches:
  Left(-a-b), Right(b-a).
```

---

## Packaged interval modules

### Generic length-one interval modules

Main file:

```text
docs/analytic_generic_interval_length_one_theorem.md
```

Templates:

```text
GEN-L1:
  T,a,b,-a -> b,a,T,-a.

GEN-R1:
  a,b,-a,T -> b,-a,T,a.
```

Status:

```text
Packaged with internal exceptional conditions and template-aware external outputs.
```

---

### Generic length-at-least-two interval splitting modules

Main file:

```text
docs/analytic_generic_interval_splitting_theorem.md
```

Templates:

```text
GEN-L>=2:
  z,J,a,b,-a -> z,a,b,J,-a.

GEN-R>=2:
  a,b,-a,z,J -> z,a,b,-a,J.
```

Status:

```text
Packaged with affine/singleton, subinterval, and external-cancellation outputs.
```

---

### Duplicate interval target modules

Main file:

```text
docs/analytic_duplicate_interval_target_theorem.md
```

Principle:

```text
If the interval target equals an atom already in the active local block,
then a length-one interval is impossible by distinctness of S.
Length at least two routes to GEN-L>=2 or GEN-R>=2.
```

Status:

```text
Packaged.
```

---

## Packaged scalar module

Main file:

```text
docs/analytic_scalar_absorption_theorem.md
```

Branches:

```text
b=2a,
a=2b mirror.
```

Status:

```text
Packaged.
```

The scalar branch uses:

```text
right-neighbor absorption,
left-neighbor absorption,
explicit boundary repairs,
whole-set repair,
external routing into template-aware cancellation states.
```

---

## Local coverage claim

Subject to the correctness of the individual notes, the first-blocker local system is now covered as follows:

```text
First forbidden-hit adjacent swap
  -> right blocker or left blocker.

Right blocker:
  |D|>=2 -> T1.
  |D|=1  -> T3 + scalar absorption / interval modules.

Left blocker:
  |L|>=2 -> T2.
  |L|=1  -> T4 + mirror scalar absorption / interval modules.
```

Every local branch is routed to one of:

```text
SUCCESS,
CONTRADICTION / impossible condition,
AFFINE_SINGLETON,
PROPER_SUBINTERVAL,
TEMPLATE_EXTERNAL_CANCELLATION,
BRIDGE_GAP_SMALLER_ENCLOSURE,
BOUNDARY_SENSITIVE_ZERO,
SCALAR_ABSORPTION.
```

---

## What this local coverage does not prove

This local coverage does **not** prove Erdős 475.

It also does **not** yet prove conditional endpoint avoidance.

The remaining hard part is global termination.

Specifically, the proof still needs a theorem showing that repeated routing among these local states cannot continue indefinitely.

---

## Next required theorem: global obstruction-tree termination

Needed objects:

```text
1. A fixed-ordering obstruction-tree state definition.
2. A well-founded measure.
3. Transition verification for each routed state type.
4. Boundary-sensitive zero handling.
5. Affine/singleton routing termination.
6. Bridge/gap smaller-enclosure integration.
7. Further external-cancellation recurrence control.
```

A candidate measure should refine the existing repo framework:

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

The crucial task is to prove that every local transition produced by the packaged modules either:

```text
1. terminates;
2. strictly decreases the measure;
3. routes to a finite-rank lower-priority state without increasing earlier coordinates;
4. triggers a contradiction to Graham-validity or distinctness.
```

---

## Recommended next file

Create:

```text
docs/analytic_global_obstruction_tree_termination_plan.md
```

It should define the state object and transition measure using the newly packaged local modules as inputs.
