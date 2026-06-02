# F8 bridge/gap descent theorem

This file continues the final-proof extraction phase.

F8 extracts the bridge/gap descent theorem from the A-notes, primarily:

```text
A74  bridge-span monotonicity
A75  equal-span separated bridge returns
A76  gap-preserving separated recurrence
A77  rigid separated self-return
A95  external collision hardening
A98  bridge/gap measure hardening
```

Recent hardening checkpoints:

```text
docs/analytic_bridge_gap_measure_hardening_a98.md
docs/analytic_f8_bridge_gap_hardening_checkpoint.md
docs/analytic_mbg_to_mnw_subrank_convention.md
docs/analytic_f7_h1_h2_sign_audit.md
docs/analytic_f7_pair_difference_endpoint_audit.md
docs/analytic_f7_singleton_endpoint_audit.md
docs/analytic_f7_cyclic_cut_midpoint_characteristic_audit.md
```

F8 is used by:

```text
F6  external collision theorem
F7  recurrence routing theorem
F9  non-weighted termination theorem
F10 weighted normal form and cut-swap theorem
F11 weighted cut-selection theorem
```

This is an extracted draft, not the final manuscript version. The bridge/gap class routing is mostly hardened, but F8 still depends on F4/F5/F6/F7/F10/F11/F9 for global termination.

---

## F8.1. Bridge/gap setup

A bridge obstruction appears when a local relation involves one piece inside the active local window and another piece outside it. Write the generic bridge relation as

```text
B_ext + U = 0
```

or, with bounded atom/pair correction,

```text
B_ext + U + E = 0,
B_ext - U + E = 0.
```

Here:

```text
B_ext = external bridge interval;
U     = internal source interval or local moved piece;
E     = bounded correction supported on boundary atoms, if present.
```

Let

```text
Enc(B_ext,U,E)
```

be the smallest atom interval containing all participating atoms.

---

## F8.2. Bridge/gap measure

Use the bridge/gap measure

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

Definitions:

```text
enclosing_span = length of Enc(B_ext,U,E);
bridge_gap     = number of atoms strictly between B_ext and U if disjoint, otherwise 0;
bridge_length  = |B_ext|;
internal_length= |U|;
support_size   = total number of participating atoms;
recurrence_depth = consecutive recurrence returns since last strict descent;
type_rank      = obstruction-class rank;
boundary_rank  = endpoint-degeneracy rank.
```

Embedding into `M_NW^*` follows:

```text
enclosing_span   -> enclosing_span;
bridge_gap       -> gap_length;
support_size     -> support_size;
recurrence_depth -> recurrence_depth;
type_rank        -> type_rank;
boundary_rank    -> boundary_rank.
```

The local coordinates

```text
bridge_length,
internal_length
```

are absorbed into the global `bridge_depth` coordinate using the finite bridge-local subrank convention in:

```text
docs/analytic_mbg_to_mnw_subrank_convention.md
```

Specifically:

```text
bridge_depth_BG = (
  bridge_cycle_depth,
  bridge_length,
  internal_length,
  bridge_orientation_rank,
  bridge_endpoint_rank
).
```

This removes the F8/F9 measure-notation ambiguity. The remaining task is to verify edge-by-edge that F8 transitions either decrease an earlier global coordinate, decrease this bridge-local subrank, exit to a destination theorem, or terminate.

---

## F8.3. Interval-geometry trichotomy

For intervals in a linear ordering, a bridge relation is one of:

```text
1. proper overlap;
2. proper containment;
3. disjoint separated relation;
4. identical/equal interval cancellation.
```

The first two give strict local descent. The third is the serious separated bridge/gap case. The fourth collapses or reduces to a smaller local class.

---

## Lemma F8.1: proper-overlap bridge decreases enclosing span

A proper-overlap bridge equality or signed bridge relation, after bounded correction normalization, produces an equal-interval or zero-composite obstruction whose enclosing span is strictly smaller than the original bridge enclosure.

### Proof

Write one orientation as

```text
B_ext = B_0 O,
U     = O U_1,
```

with nonempty overlap `O` and nonempty tails `B_0,U_1`. Cancelling `O` leaves an obstruction supported on `B_0,U_1`, possibly with bounded correction `E`. The overlap contains at least one atom and is removed from the active support, so the new enclosure is strictly smaller unless `E` lies outside the old enclosure. If `E` lies outside, the case is an external signed bridge classified by F6 before re-entering F8. ∎

---

## Lemma F8.2: proper containment decreases support or span

A proper-containment bridge equality produces one of:

```text
nonempty zero interval,
two-piece zero-composite,
signed zero-composite after bounded correction normalization.
```

The resulting obstruction has strictly smaller support size than the original bridge relation. If the complement lies on one side, the enclosing span also strictly decreases.

### Proof

If, for example,

```text
B_ext = L U R
```

with at least one of `L,R` nonempty, equality of `B_ext` and `U` gives

```text
sum(L)+sum(R)=0.
```

The contained block `U` is removed from the active relation, so support size strictly decreases. The other containment orientation is identical. ∎

---

## Lemma F8.3: disjoint bridge equality is separated-equal

A nontrivial disjoint bridge equality is a separated-equal or signed separated-equal branch, controlled by the gap coordinate.

### Proof

If the bridge and internal interval are neither overlapping nor contained, they are disjoint:

```text
B G U
```

or

```text
U G B,
```

where `G` is nonempty. Equality of `B` and `U` is exactly a separated-equal branch. ∎

---

## F8.4. Equal-span separated bridge return

Consider the separated-equal configuration

```text
B G U,
sum(B)=sum(U),
G nonempty.
```

Use the gap-after move:

```text
B G U -> B U G.
```

## Lemma F8.4: successful gap-after move decreases bridge gap to zero

If the gap-after move is Graham-valid and avoids the forbidden value `f`, then the active equal-block gap decreases from `|G|` to `0`.

### Proof

Before the move, `G` separates `B` from `U`. After the move, the equal-sum blocks are adjacent as `B U`. Therefore the separating gap is zero. ∎

---

## Lemma F8.5: gap-after collisions route out of the bridge/gap class

Any displayed collision in

```text
B G U -> B U G
```

routes to one of:

```text
two-piece zero,
three-piece zero,
equal-interval descent,
zero collapse,
pair-difference boundary,
external collision handled by F6.
```

### Extracted proof

The displayed collision equations are the gap-after table from A49--A54/A75/A98:

```text
prefix(U)+tail(B)=0,
G+tail(U)+prefix(Y)=0,
U+tail(B)+prefix(G)=0,
tail(G)+prefix(Y)=0,
B+prefix(G)=prefix(U).
```

The first four are zero-composite or zero-collapse branches. The last is equal-interval or pair-difference after uncrossing. Collisions involving endpoints outside the displayed table are external collisions handled by F6. ∎

### Remaining manuscript task

The final manuscript should inline this as an appendix-style table with endpoint cases. This is manuscript hardening, not a known new class.

---

## Lemma F8.6: recurrence is the only non-descending gap-after outcome

For an equal-span separated bridge return, the gap-after move gives exactly one of:

```text
success with bridge_gap -> 0;
displayed collision routed by Lemma F8.5;
external collision routed by F6;
forbidden recurrence routed by F7.
```

Thus the only possible non-descending continuation is recurrence.

### Proof

The transformed ordering is either Graham-valid and avoids `f`, non-Graham, or Graham-valid but recurrent. Non-Graham cases are displayed or external collisions. Recurrent cases route through F7. ∎

---

## F8.5. Gap-preserving recurrence

A recurrence after the gap-after move is gap-preserving only if the A5 blocker pullback reconstructs a separated-equal bridge with the same gap length.

## Lemma F8.7: proper use of old gap decreases bridge gap

If the recurrent A5 blocker pullback uses a proper prefix or proper tail of the old gap `G` as the new separating gap, then the new bridge gap length is strictly less than `|G|`.

### Proof

A proper prefix or proper tail of `G` contains fewer atoms than `G`. Since bridge gap counts the atoms strictly between the separated equal pieces, the gap coordinate strictly decreases. ∎

---

## Lemma F8.8: preserving bridge gap forces full endpoint alignment

If the recurrence pullback returns to a separated-equal bridge with the same gap length `|G|`, then the full old gap `G` is reused and both old gap endpoints are unchanged.

### Proof

Moving either endpoint inward shortens the gap. Moving either endpoint outward either increases the enclosing span or absorbs external material into the gap. The outward case is external bridge routing handled by F6/F8 before being considered a same-span separated return. Under equal-span and same-gap preservation, the old endpoints must be reused. ∎

---

## F8.6. Rigid separated self-return

By Lemma F8.8, a same-gap recurrence must be rigid: it reconstructs either

```text
B G U
```

or

```text
U G B
```

with the same gap endpoints.

## Lemma F8.9: same-orientation rigid return routes out or descends

A same-orientation rigid return to `B G U` either:

```text
uses a proper prefix/tail of B, G, or U and decreases support/gap;
uses endpoint U and routes to adjacent-equal/midpoint;
uses endpoint G and routes to cyclic/external recurrence;
produces zero collapse inside G.
```

Hence it does not preserve `M_BG` as a new bridge/gap state.

### Proof

Proper-prefix cases reduce support or gap length. Endpoint `U` places the equal blocks adjacent and gives the midpoint/adjacent-equal branch. Endpoint `G` is a post-segment or cyclic/external recurrence handled by F7/F6. Internal zero inside `G` is collapse. Recent F7 audits harden the endpoint-G branch:

```text
cyclic midpoint characteristic audit;
singleton endpoint table;
pair-difference endpoint table;
H1/H2 corrected sign conventions.
```

∎

### Remaining manuscript task

A final proof should add a compact rigid-return endpoint table. The expected destinations are already known:

```text
proper endpoints -> strict descent;
endpoint U -> F5/A55;
endpoint G -> F7/A71/F6;
zero in G -> collapse.
```

---

## Lemma F8.10: exchange-orientation rigid return factors through direct exchange

A rigid return to

```text
U G B
```

is exactly the direct-exchange target of the original separated-equal pair:

```text
B G U -> U G B.
```

If direct exchange succeeds, the obstruction path succeeds. If it collides, the separated-equal direct-exchange table routes it to non-weighted local classes. If it is recurrent, F7 routes it.

### Proof

The exchanged separated-equal state is definitionally the direct-exchange target. The success/collision/recurrent trichotomy is exhaustive. ∎

### Dependency

The direct-exchange collision table should be finalized in F5. This is now an inherited F5 dependency rather than a new F8-local class.

---

## F8.7. Signed bridge corrections

Signed bridge forms are:

```text
B_ext + U + E = 0,
B_ext - U + E = 0,
```

where `E` is a bounded atom/pair correction.

Routing convention:

```text
if E lies inside the bridge enclosure -> signed zero/equal/pair local class;
if E lies outside the bridge enclosure -> F6 external signed collision;
if coefficient-2/core remains -> F10/F11 weighted-core branch;
if bounded pair correction -> F7/F4 pair-difference machinery.
```

This remains a high-risk inherited dependency because F10/F11 weighted-core termination is not yet closed.

---

## F8.8. Bridge/gap descent theorem

## Theorem F8.11: bridge/gap descent theorem

Every bridge/gap obstruction produced by external-collision or recurrence machinery either:

```text
1. decreases enclosing span by proper-overlap uncrossing;
2. decreases support size by proper-containment subtraction;
3. decreases bridge gap by successful gap-after move or proper-gap recurrence;
4. routes to zero-composite/equal/signed interval machinery;
5. routes to recurrence handled by F7;
6. routes to external collision handled by F6;
7. routes to midpoint/adjacent-equal machinery;
8. factors through direct exchange and routes through separated-equal local tables;
9. exits to weighted-core machinery F10/F11 if a signed correction remains irreducible;
10. reaches collapse or success.
```

No bridge/gap branch creates a new obstruction species. A complete global termination proof still requires F9 to consume these exits and F10/F11 to terminate weighted-core branches.

### Proof

Proper overlap is Lemma F8.1. Proper containment is Lemma F8.2. Disjoint equality is Lemma F8.3. Equal-span separated returns are Lemmas F8.4--F8.6. Gap-preserving recurrence is Lemmas F8.7--F8.8. Rigid same-orientation and exchange-orientation returns are Lemmas F8.9--F8.10. Signed corrections route by F8.7. These cases exhaust interval geometry for bridge/gap relations. ∎

---

## F8.9. Interface with F9

F8 supplies F9 with the bridge/gap cycle-breaking statement:

```text
bridge/gap recurrence cannot preserve all coordinates of M_NW^* indefinitely,
provided the M_BG bridge-local subrank convention is applied and F10/F11 weighted exits terminate.
```

The convention is:

```text
M_BG.bridge_length/internal_length -> M_NW^*.bridge_depth
```

via the finite subrank:

```text
bridge_depth_BG = (
  bridge_cycle_depth,
  bridge_length,
  internal_length,
  bridge_orientation_rank,
  bridge_endpoint_rank
).
```

Bridge/gap exits go to:

```text
F4 zero/equal/pair local descent;
F5 separated-equal/midpoint routing;
F6 external collision;
F7 recurrence;
F10/F11 weighted branch if coefficient-2 normal form appears;
terminal success/collapse.
```

---

## F8.10. Remaining extraction risks

Before final manuscript status:

```text
R1. Put the gap-after collision table in an appendix with endpoint cases.
R2. Finalize direct-exchange table reference in F5.
R3. Prove or explicitly route all signed bridge correction exits through F6/F10 or bounded pair machinery.
R4. Add same-orientation rigid-return endpoint table.
R5. Close F10/F11 weighted-core termination for irreducible signed corrections.
```

Resolved or reduced:

```text
A98 supplies the bridge/gap measure-hardening architecture.
F7 recurrence endpoint/sign risks are substantially hardened.
Endpoint-local bridge outputs are class-routed into F8/F6/F9.
M_BG bridge_length/internal_length are embedded into M_NW^*.bridge_depth by analytic_mbg_to_mnw_subrank_convention.md.
```

---

## F8.11. Extraction status

```text
Status: bridge/gap class routing mostly hardened.
Risk: YELLOW, with one RED inherited dependency: F10/F11 weighted-core termination.
Next recommended extraction: F10/F11 weighted-core audit.
```
