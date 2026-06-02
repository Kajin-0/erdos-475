# Analytic Checkpoint: F8 Bridge/Gap Hardening

This checkpoint audits the F8 bridge/gap descent theorem after the endpoint-branch and F7 recurrence hardening work.

Claim boundary:

```text
This file is not a proof of Erdős 475.
It is a bridge/gap proof-status checkpoint.
It identifies which F8 risks are resolved architecturally, which are inherited dependencies, and which remain theorem blockers.
```

---

## Source files

Primary F8 draft:

```text
docs/final/F08_bridge_gap_descent_theorem.md
```

A98 bridge/gap hardening:

```text
docs/analytic_bridge_gap_measure_hardening_a98.md
```

Relevant recent recurrence hardening:

```text
docs/analytic_f7_h1_h2_sign_audit.md
docs/analytic_f7_pair_difference_endpoint_audit.md
docs/analytic_f7_singleton_endpoint_audit.md
docs/analytic_f7_cyclic_cut_midpoint_characteristic_audit.md
docs/final/F07_recurrence_routing_theorem.md
```

Relevant endpoint branch integration:

```text
docs/analytic_endpoint_branch_f9_measure_audit.md
docs/analytic_global_class_graph_measure_checkpoint.md
```

---

## F8 role in the global proof

F8 is the theorem that must prevent bridge/gap states from cycling indefinitely at equal measure.

It is used by:

```text
F6 external collision;
F7 recurrence routing;
F9 non-weighted termination;
F10/F11 weighted branches when bridge states appear as exits.
```

A bridge/gap state has measure:

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

Its global embedding into `M_NW^*` uses:

```text
enclosing_span   -> enclosing_span,
bridge_gap       -> gap_length,
support_size     -> support_size,
recurrence_depth -> recurrence_depth,
type_rank        -> type_rank,
boundary_rank    -> boundary_rank.
```

The coordinates:

```text
bridge_length,
internal_length
```

are bridge-local refinements and should be represented inside either:

```text
support_size,
type_rank,
or an F8-local subrank
```

when embedded into F9.

---

## F8 geometric cases

Every bridge relation has one of four interval-geometric forms:

```text
1. proper overlap;
2. proper containment;
3. disjoint separated relation;
4. identical/equal interval cancellation.
```

The first two are strict descent. The third is the only serious bridge/gap recurrence source. The fourth is collapse or cancellation into a smaller local class.

---

## Case audit table

| Case | F8/A98 route | Decrease / exit | Current status |
|---|---|---|---|
| proper overlap | F8.1 / A98.1 | enclosing_span decreases | architecturally closed |
| proper containment | F8.2 / A98.2 | support_size decreases, sometimes span | architecturally closed |
| disjoint bridge equality | F8.3 / A98.3 | becomes separated-equal with bridge_gap | class-routed |
| successful gap-after move | F8.4 / A98.4 | bridge_gap -> 0 | architecturally closed |
| gap-after displayed collision | F8.5 / A98.5 | exits to zero/equal/pair/F6 | class-routed, depends on F4/F5/F6 |
| gap-after recurrence | F8.6 / A98.6 | exits to F7 recurrence | class-routed, depends on F7/F9 |
| proper use of old gap | F8.7 / A98.7 | bridge_gap decreases | architecturally closed |
| same-gap return | F8.8 / A98.8 | forces rigid endpoint alignment | class-routed |
| same-orientation rigid return | F8.9 / A98.9 | support/gap decrease or exits to midpoint/cyclic/external | class-routed, depends on F5/F6/F7 |
| exchange-orientation rigid return | F8.10 / A98.10 | direct exchange success/collision/recurrence | class-routed, depends on F5/F7 |

---

## F8 risk R1: gap-after collision table

F8 listed risk:

```text
R1. Put the gap-after collision table in an appendix with endpoint cases.
```

A98 records the essential displayed equations:

```text
prefix(U)+tail(B)=0,
G+tail(U)+prefix(Y)=0,
U+tail(B)+prefix(G)=0,
tail(G)+prefix(Y)=0,
B+prefix(G)=prefix(U).
```

Routing:

```text
first four -> zero-composite / zero-collapse / equal-interval classes;
last one  -> equal-interval or pair-difference after uncrossing;
external endpoint collision -> F6.
```

Status:

```text
Architecturally routed, but not final-manuscript complete.
```

Remaining action:

```text
Create a compact appendix-style gap-after collision table with endpoint cases.
```

The table is not expected to create a new global class.

---

## F8 risk R2: direct exchange reference to F5

F8 listed risk:

```text
R2. Formalize direct exchange table reference to F5.
```

Exchange-orientation rigid return is:

```text
B G U -> U G B.
```

A98.10 says this is exactly the separated-equal direct exchange target.

Possible outcomes:

```text
success;
displayed collision -> direct-exchange table / F5;
external collision -> F6;
forbidden recurrence -> F7.
```

Status:

```text
Class-routed but dependent on F5 finalization.
```

Remaining action:

```text
Audit F5 separated-equal/midpoint theorem and ensure direct-exchange table endpoints are explicit.
```

This is now an F5 dependency, not a uniquely F8-local gap.

---

## F8 risk R3: signed bridge corrections

F8 listed risk:

```text
R3. Ensure signed bridge corrections are always routed through F6/F10 or bounded pair machinery.
```

Signed bridge forms are:

```text
B_ext + U + E = 0,
B_ext - U + E = 0,
```

where `E` is a bounded atom/pair correction.

Routing:

```text
if E lies inside the bridge enclosure -> signed zero/equal/pair local class;
if E lies outside the bridge enclosure -> F6 external signed collision;
if coefficient-2/core remains -> F10/F11 weighted-core branch;
if bounded pair correction -> F7/F4 pair-difference machinery.
```

Status:

```text
Still a high-risk inherited dependency because F10/F11 weighted-core termination is not closed.
```

This is one of the main theorem blockers.

Required final proof statement:

```text
Every signed bridge correction either reduces to a nonweighted F4/F5/F6/F7 class with measure descent,
or exits to F10/F11 with a separately well-founded weighted measure.
```

---

## F8 risk R4: same-orientation rigid return endpoint cases

F8 listed risk:

```text
R4. Check same-orientation rigid return endpoint cases line by line.
```

Same-orientation rigid return reconstructs:

```text
B G U
```

with the same gap endpoints.

A98.9 routes cases as:

```text
proper prefix/tail of B,G,U -> support/gap decrease;
endpoint U -> adjacent-equal / midpoint;
endpoint G -> cyclic/external recurrence;
zero inside G -> collapse.
```

Recent F7 hardening improves the endpoint-G branch:

```text
cyclic midpoint p=3 behavior audited;
singleton/pair endpoint recurrence audited;
H1/H2 and A69 endpoint conventions corrected.
```

Status:

```text
Substantially hardened, but final line-by-line rigid-return endpoint table is still missing.
```

Remaining action:

```text
Create an explicit rigid-return endpoint table or patch A98/F8 with it.
```

Expected result:

```text
No new class; endpoint U -> F5/A55, endpoint G -> F7/A71/F6, proper endpoints -> strict descent.
```

---

## F8 risk R5: M_BG embedding into M_NW^*

F8 listed risk:

```text
R5. Ensure M_BG embeds consistently into M_NW^*.
```

A98 gives the embedding:

```text
enclosing_span -> enclosing_span,
bridge_gap     -> gap_length,
support_size   -> support_size,
recurrence_depth -> recurrence_depth,
type_rank/boundary_rank -> same coordinates.
```

But F8 uses two local coordinates not explicitly named in `M_NW^*`:

```text
bridge_length,
internal_length.
```

These must be absorbed by a finite subrank.

Recommended final embedding:

```text
F8_subrank = (bridge_length, internal_length, local_orientation_rank)
```

and place it inside:

```text
type_rank
```

or refine `bridge_depth` in `M_NW^*` to include the F8 subrank.

Status:

```text
Partially resolved. Needs explicit final convention.
```

This is a real F9 integration requirement.

---

## F8 hardening status theorem

### Statement

F8 bridge/gap descent is class-routed as follows:

```text
1. overlap and containment cases strictly decrease span/support;
2. separated disjoint cases enter gap-after or direct-exchange routines;
3. successful gap-after reduces gap to zero;
4. gap-after collisions exit to F4/F5/F6;
5. gap-after recurrence exits to F7;
6. proper-gap recurrence decreases gap;
7. same-gap recurrence forces rigid endpoint alignment;
8. rigid returns either descend or exit to F5/F6/F7;
9. signed corrections either reduce to nonweighted classes or exit to F10/F11.
```

Therefore the only remaining F8 theorem blockers are:

```text
1. final endpoint tables for gap-after and rigid-return cases;
2. explicit M_BG -> M_NW^* subrank convention;
3. F10/F11 weighted-core termination for signed correction exits;
4. inherited F4/F5/F6/F7/F9 termination dependencies.
```

### Proof status

This is a checkpoint theorem, not a final proof. It records class routing and remaining exact obligations.

---

## Current risk level

```text
F8 class routing: mostly closed.
F8 measure embedding: partially closed, needs explicit subrank convention.
F8 signed correction exits: still high-risk because of F10/F11.
F8 endpoint tables: medium-risk manuscript hardening.
```

---

## Recommended next step

The best next action is:

```text
Patch F08 to reference A98, the F7 audits, and this checkpoint;
then create an explicit M_BG embedding convention note.
```

The most theorem-critical unresolved issue is still:

```text
F10/F11 weighted-core termination.
```

because F8, F6, and F7 can all exit to weighted-core machinery.
