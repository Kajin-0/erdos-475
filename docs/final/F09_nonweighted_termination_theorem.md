# F9 non-weighted termination theorem

This file continues the final-proof extraction phase.

F9 extracts the non-weighted termination theorem from the A-notes and the already extracted final lemmas. It is mainly backed by:

```text
A72  obstruction dependency graph
A73  global acyclicity attempt
A78  non-weighted acyclicity theorem
A87  local lemma audit checklist
A88  formal dependency table
A92--A94 state-machine / progress hardening
A95--A99 hardening of external, recurrence, cut-swap, bridge/gap, and span conventions
F3   obstruction state machine
F4   local zero/equal/pair descent
F5   separated-equal and midpoint routing
F6   external collision theorem
F7   recurrence routing theorem
F8   bridge/gap descent theorem
F10  weighted normal form and fixed cut-swap theorem
F11  weighted cut-selection and termination theorem
```

F9 also uses the bridge-local subrank convention:

```text
docs/analytic_mbg_to_mnw_subrank_convention.md
```

F9 is an extracted draft, not yet the final manuscript version. Its main remaining risk is that the edge-by-edge class graph must be checked against the final F4--F8 and F10--F11 outputs.

---

## F9.1. Scope

F9 proves termination for the non-weighted obstruction graph.

The weighted class

```text
WEIGHTED_CORE
```

is not treated as a non-weighted node. When a non-weighted branch enters a genuine weighted core, the proof delegates to F10--F11. F11 then either returns to non-weighted machinery, succeeds/collapses, or decreases the weighted middle length.

Thus F9 is the non-weighted half of the global termination proof.

---

## F9.2. Non-weighted measure

Use the measure from F3:

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

The order is lexicographic over nonnegative integers.

The coordinate

```text
bridge_depth
```

contains the finite bridge-local subrank used by F8:

```text
bridge_depth_BG = (
  bridge_cycle_depth,
  bridge_length,
  internal_length,
  bridge_orientation_rank,
  bridge_endpoint_rank
).
```

Thus the F8-local coordinates

```text
bridge_length,
internal_length
```

are not new global coordinates; they are tie-breakers inside `bridge_depth` for `BRIDGE_GAP` states.

The final coordinate `h_excess` records the recurrent hit index relative to the globally minimal first forbidden hit. It is intentionally placed last.

---

## F9.3. Non-weighted class universe

The non-weighted obstruction classes are:

```text
ZERO_COLLAPSE,
PREFIX_ZERO,
TWO_PIECE_ZERO,
THREE_PIECE_ZERO,
HIGHER_ZERO_COMPOSITE,
ZERO_COMPOSITE_SURGERY,
EQUAL_INTERVAL,
SIGNED_INTERVAL,
SEPARATED_EQUAL,
MIDPOINT,
PAIR_DIFFERENCE,
TRANSPORTED_PREFIX,
SINGLETON_RECURRENCE,
CYCLIC_RECURRENCE,
FORBIDDEN_RECURRENCE,
EXTERNAL_COLLISION,
BRIDGE_GAP.
```

Terminal states are:

```text
SUCCESS,
CONTRADICTION.
```

The class `WEIGHTED_CORE` is treated as an exit to F10--F11, not as a non-weighted cycle node.

---

## F9.4. Local descent edges

## Lemma F9.1: local zero/equal/pair classes terminate or exit

Every obstruction in the local classes

```text
ZERO_COLLAPSE,
PREFIX_ZERO,
TWO_PIECE_ZERO,
THREE_PIECE_ZERO,
HIGHER_ZERO_COMPOSITE,
EQUAL_INTERVAL,
SIGNED_INTERVAL,
PAIR_DIFFERENCE,
TRANSPORTED_PREFIX
```

either:

```text
1. reaches contradiction;
2. strictly decreases enclosing span or support size;
3. exits to separated-equal/midpoint routing F5;
4. exits to recurrence routing F7;
5. exits to external/bridge routing F6/F8;
6. exits to weighted machinery F10/F11.
```

### Proof

This is exactly F4.10. Zero intervals are terminal contradictions. Proper-overlap equalities reduce enclosing span. Proper containment reduces support size. Pair-difference and transported-prefix cases either normalize to local classes, enter recurrence/external routing, or become genuine weighted-core candidates handled by F10--F11. ∎

---

## F9.5. Separated-equal and midpoint edges

## Lemma F9.2: separated-equal/midpoint classes terminate, descend, or exit

Every obstruction in

```text
SEPARATED_EQUAL,
MIDPOINT
```

either:

```text
1. succeeds;
2. reaches contradiction/collapse;
3. strictly decreases gap, span, or support;
4. exits to local descent F4;
5. exits to external collision F6;
6. exits to recurrence F7;
7. exits to bridge/gap descent F8;
8. exits to weighted machinery F10/F11 only if a genuine coefficient-2 normal form survives.
```

### Proof

This is F5.10. Direct exchange and gap-after moves have the success/collision/recurrent trichotomy. Successful gap-after reduces gap. Gap-preserving recurrence is rigid and routes through direct exchange, midpoint, recurrence, external, or bridge/gap machinery. ∎

---

## F9.6. External-collision edges

## Lemma F9.3: external collisions introduce no new class

Every obstruction in

```text
EXTERNAL_COLLISION
```

routes to one of:

```text
bridge zero-composite,
signed bridge composite,
equal/separated interval,
transported-prefix,
pair-difference,
cyclic recurrence,
singleton/prefix recurrence,
weighted-core normal form,
collapse or minimality contradiction.
```

Thus it exits to F4, F5, F7, F8, F10/F11, or terminal contradiction.

### Proof

This is F6.7. Left, right, unchanged-family, wrapped/cyclic, and external forbidden-hit cases exhaust external endpoints. ∎

---

## F9.7. Recurrence edges

## Lemma F9.4: recurrence classes descend or exit

Every obstruction in

```text
SINGLETON_RECURRENCE,
CYCLIC_RECURRENCE,
FORBIDDEN_RECURRENCE
```

either:

```text
1. strictly decreases M_NW^* by the augmented bounded-blocker criterion;
2. exits to local zero/equal/pair machinery F4;
3. exits to external collision F6;
4. exits to bridge/gap descent F8;
5. exits to weighted machinery F10/F11;
6. reaches collapse or minimality contradiction.
```

### Proof

This is F7.8. Bounded blockers strictly decrease enclosing span by augmented support containment. Long blockers are classified into H1/H2, pair-difference, singleton-prefix, cyclic, external, bridge, or weighted branches. ∎

---

## F9.8. Bridge/gap edges

## Lemma F9.5: bridge/gap classes descend or exit

Every obstruction in

```text
BRIDGE_GAP
```

either:

```text
1. decreases enclosing span by proper-overlap uncrossing;
2. decreases support size by proper-containment subtraction;
3. decreases gap by gap-after success or proper-gap recurrence;
4. decreases the finite bridge-local subrank stored in bridge_depth;
5. exits to local descent F4;
6. exits to separated-equal/midpoint routing F5;
7. exits to external collision F6;
8. exits to recurrence F7;
9. exits to weighted machinery F10/F11;
10. reaches collapse or success.
```

### Proof

This is F8.11 plus `analytic_mbg_to_mnw_subrank_convention.md`. Proper overlap, proper containment, disjoint separated equality, gap-after recurrence, and rigid same/exchange returns exhaust bridge/gap geometry. When span, gap, or support do not decrease, the bridge-local tuple inside `bridge_depth` supplies the F8 tie-breaker. Irreducible signed corrections exit to F10/F11. ∎

---

## F9.9. Weighted exits

## Lemma F9.6: weighted exits cannot create non-weighted cycles

If a non-weighted obstruction exits to a genuine weighted core, then F10--F11 ensure the weighted branch either:

```text
1. succeeds;
2. collapses;
3. exits back to non-weighted machinery;
4. returns to a genuine weighted core with smaller |B|;
5. terminates by induction on |B|.
```

Therefore weighted exits cannot support an infinite non-weighted obstruction cycle.

### Proof

F10 classifies the local weighted normal forms and fixed cut-swaps. F11 proves weighted cut-selection and termination by induction on the middle length `|B|`, with atom-middle base case, proper-middle cut-swap, weak-to-pattern rigidity reduction, and pattern-rigid impossibility. ∎

### Audit flag

This lemma inherits the risk status of F11. In the final manuscript, F11 must be fully hardened before F9 can be considered final.

---

## F9.10. Non-weighted acyclicity theorem

## Theorem F9.7: non-weighted obstruction graph terminates

Assume the extracted lemmas F3--F8 and F10--F11 are valid. Then every non-weighted obstruction path either:

```text
1. reaches SUCCESS;
2. reaches CONTRADICTION;
3. strictly decreases M_NW^* after finitely many routing steps;
4. exits to a weighted branch that terminates by F11.
```

In particular, there is no infinite non-weighted obstruction path avoiding success, contradiction, measure descent, and weighted termination.

### Proof

Let an obstruction state be nonterminal and non-weighted. Its class lies in the non-weighted universe of F9.3.

If it is local zero/equal/pair/transported-prefix, Lemma F9.1 applies. If it is separated-equal or midpoint, Lemma F9.2 applies. If it is external collision, Lemma F9.3 applies. If it is recurrence, Lemma F9.4 applies. If it is bridge/gap, Lemma F9.5 applies.

Every output either terminates, strictly decreases one of the coordinates of `M_NW^*`, enters another named class with a lower finite rank/depth tracked by `M_NW^*`, or exits to the weighted branch. Weighted exits terminate by Lemma F9.6.

Since `M_NW^*` is lexicographic over nonnegative integers, it admits no infinite strictly decreasing chain. Since finite type/depth returns are included in the measure coordinates and bridge/recurrence ties are broken by F7/F8, no same-measure cycle remains. Therefore no infinite non-weighted obstruction path exists. ∎

---

## F9.11. Interface with endpoint avoidance

F9 supplies F12 with the main termination fact:

```text
Starting from the initial A5 obstruction of a minimal endpoint-avoidance counterexample, the obstruction path must terminate in success or contradiction.
```

Weighted branches are included through F10--F11.

---

## F9.12. Remaining extraction risks

Before final manuscript status:

```text
R1. The edge-by-edge class graph should be included as a table.
R2. type_rank, boundary_rank, recurrence_depth, pair_depth, separated_depth, and bridge_depth need explicit finite orders.
R3. F11 must be hardened, because F9 depends on weighted termination.
R4. Verify no F4--F8 output class is missing from F9.3.
R5. Replace “lower finite rank/depth” with explicit rank inequalities in the final manuscript.
```

Resolved or reduced:

```text
F8 bridge_length/internal_length are embedded into bridge_depth by analytic_mbg_to_mnw_subrank_convention.md.
Endpoint branch class graph and measure checkpoint created in analytic_global_class_graph_measure_checkpoint.md.
```

---

## F9.13. Extraction status

```text
Status: extracted draft with bridge-local subrank convention added.
Risk: ORANGE, dependent on F11 and final edge-by-edge rank table.
Next recommended extraction: F10/F11 weighted-core audit.
```
