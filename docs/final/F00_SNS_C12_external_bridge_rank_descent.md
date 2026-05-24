# F00.SNS.C12 external and bridge/gap rank-descent verification

This file continues the strong nonzero-sum repair path.

C11 verified the non-weighted local rank rows modulo two major categories:

```text
1. EXTERNAL_COLLISION / BRIDGE_GAP rank-descent verification;
2. WEIGHTED_REPAIR rank-descent verification.
```

C12 handles the first category under the ARBITRARY-phase interpretation:

```text
zero intervals are collision defects measured by D_SNS^*, not terminal contradictions.
```

Status: verification draft.

---

## C12.1. Standing convention

Work in ARBITRARY phase.  The current ordering may contain endpoint collisions.

A zero interval produced by an external or bridge pullback is handled as:

```text
ZERO_DEFECT -> compare span/location with D_SNS^*.
```

It is not a contradiction unless the proof has already reached COLLISION_FREE phase.

The active measure is:

```text
M_phase=(D_SNS^*, phase_rank, M_loc, M_w, transition_budget).
```

For external/bridge states, the relevant local component is:

```text
M_bridge=(
  enclosing_span,
  bridge_gap,
  bridge_length,
  internal_length,
  support_size,
  bridge_depth,
  type_rank,
  boundary_rank_loc
).
```

---

## C12.2. External collision normal forms

A local move replaces

```text
R=X W Y
```

by

```text
R'=X W' Y,
```

with

```text
sum(W')=sum(W)=w.
```

Let

```text
x=sum(X).
```

A moved internal endpoint has form:

```text
x+u.
```

A left external endpoint has form:

```text
x-L.
```

A right external endpoint has form:

```text
x+w+R_+.
```

Therefore left and right external collisions give:

```text
L+u=0,
R_+ + (w-u)=0.
```

These are bridge zero-composites or signed bridge composites.

---

## Lemma C12.1: external collision enters bridge/local/weighted rows

Every moved-external collision in ARBITRARY phase routes to one of:

```text
ZERO_DEFECT,
LOCAL_ZERO_COMPOSITE,
EQUAL_INTERVAL,
SIGNED_INTERVAL,
PAIR_DIFFERENCE,
SEPARATED_EQUAL,
BRIDGE_GAP,
TRANSPORTED_PREFIX,
WEIGHTED_REPAIR,
CYCLIC_WRAP,
BOUNDARY_DEGENERACY.
```

### Proof

The external collision equations are bridge equations of the form

```text
external interval + internal interval + bounded correction = 0.
```

If the external and internal intervals merge into one interval, this is ZERO_DEFECT.  If they remain as multiple pieces, this is LOCAL_ZERO_COMPOSITE or BRIDGE_GAP.  Equal/signed/pair relations arise when comparing interval sums with bounded atom corrections.  Transported-prefix and weighted repair arise only if a coefficient-2 structure survives normalization.  Cyclic wrap and boundary degeneracy are endpoint convention cases. ∎

---

## C12.3. Proper-overlap bridge descent

Let the bridge and internal intervals properly overlap:

```text
B_ext=B_0 O,
U=O U_1,
```

with nonempty overlap `O`.

## Lemma C12.2: proper overlap decreases enclosing span

A proper-overlap bridge relation uncrosses to a relation with strictly smaller `enclosing_span`, unless a bounded correction lies outside the old enclosure, in which case the state is reclassified as an external signed bridge with larger displayed enclosure and finite boundary rank.

### Proof

Cancel the common overlap `O`.  Since `O` is nonempty, the active support loses at least one atom.  The new active enclosure is strictly smaller unless a correction term was outside the old enclosure.  That exceptional case is not a pure proper-overlap bridge; it is an external signed bridge and remains in the EXTERNAL_COLLISION/BRIDGE_GAP row with higher boundary rank but finite transition budget. ∎

### Measure effect

```text
enclosing_span decreases
```

or the case is routed to a finite boundary subcase.

---

## C12.4. Proper-containment bridge descent

Suppose one interval properly contains the other:

```text
B_ext=L U R
```

with at least one of `L,R` nonempty.

## Lemma C12.3: proper containment decreases support size

A proper-containment bridge relation produces a complement zero-composite

```text
L+R=0
```

with strictly smaller `support_size` than the original bridge relation.

### Proof

Subtract the contained interval `U` from both sides.  The active support no longer includes `U`; hence support size decreases.  If only one complement side is present, the result is a ZERO_DEFECT with controlled span. ∎

### Measure effect

```text
support_size decreases
```

or the state routes to ZERO_DEFECT with span/location comparison.

---

## C12.5. Disjoint bridge relation

If the bridge and internal interval are disjoint, write:

```text
B_ext G U
```

with gap `G`, possibly after reversing orientation.

The relation becomes separated bridge/equal data.

## Lemma C12.4: disjoint bridge relation is governed by bridge_gap

A nontrivial disjoint bridge relation routes to:

```text
SEPARATED_EQUAL,
SIGNED_INTERVAL,
BRIDGE_GAP,
or WEIGHTED_REPAIR if coefficient-2 survives.
```

If it remains in BRIDGE_GAP, its next descent coordinate is `bridge_gap=|G|`.

### Proof

Disjoint intervals cannot be uncrossed by overlap or containment.  The only remaining geometric datum is the gap separating the pieces.  Equal-sum relations become separated-equal; signed corrections become signed bridge; coefficient-2 survivors become weighted repair. ∎

---

## C12.6. Gap-after bridge descent

For a separated bridge/equal configuration:

```text
B G U,
sum(B)=sum(U),
G nonempty,
```

apply the gap-after move:

```text
B G U -> B U G.
```

## Lemma C12.5: successful gap-after decreases bridge gap

If the gap-after move produces no new collision, then `bridge_gap` decreases from `|G|` to `0`.

### Proof

After the move, `B` and `U` are adjacent.  The separating gap is empty. ∎

---

## Lemma C12.6: gap-after collision exits to verified rows

Any collision during gap-after bridge repair routes to:

```text
ZERO_DEFECT,
LOCAL_ZERO_COMPOSITE,
EQUAL_INTERVAL,
SIGNED_INTERVAL,
PAIR_DIFFERENCE,
EXTERNAL_COLLISION,
WEIGHTED_REPAIR.
```

The non-weighted local rows were verified in C11.  EXTERNAL_COLLISION re-enters C12 with finite transition budget.  WEIGHTED_REPAIR is deferred to the weighted verification file.

### Proof

The gap-after displayed collision equations are finite and have forms:

```text
prefix(U)+tail(B)=0,
G+tail(U)+prefix(Y)=0,
U+tail(B)+prefix(G)=0,
tail(G)+prefix(Y)=0,
B+prefix(G)=prefix(U).
```

These are zero/equal/signed/local/external forms. ∎

---

## C12.7. Rigid bridge return

A gap-preserving bridge return must reuse the same full gap endpoints.  Otherwise the gap decreases or the enclosing span changes.

## Lemma C12.7: same-gap bridge return is rigid or descending

If a bridge/gap branch returns with the same `enclosing_span`, same `bridge_gap`, and same `support_size`, then it is a rigid separated return.  It either:

```text
1. factors through direct exchange;
2. routes to midpoint/adjacent-equal;
3. creates local collision algebra;
4. creates external collision algebra;
5. enters weighted repair;
6. consumes finite transition budget and cannot repeat indefinitely without one of the above.
```

### Proof

If either gap endpoint moves inward, the gap decreases.  If either moves outward, the enclosing span increases or the branch is reclassified as external.  Thus same-gap preservation forces identical endpoints.  A same-orientation rigid return either uses a proper prefix/tail, giving support/gap descent, or an endpoint, giving midpoint/cyclic/external routing.  Exchange orientation is direct exchange. ∎

---

## C12.8. Cyclic/wrapped external data

Cyclic or wrapped external collisions are endpoint-coordinate artifacts.  In SNS mode they are collision equations, not forbidden recurrences.

## Lemma C12.8: cyclic wrap routes to bridge/local rows

A cyclic/wrapped collision routes to one of:

```text
ZERO_DEFECT,
EQUAL_INTERVAL,
SIGNED_INTERVAL,
PAIR_DIFFERENCE,
BRIDGE_GAP,
EXTERNAL_COLLISION,
BOUNDARY_DEGENERACY.
```

No separate forbidden recurrence is used in SNS mode.

### Proof

Write endpoints after a cyclic cut as suffix and wrapped prefix expressions.  Equality of two such expressions is either a non-wrapping interval equality, a wrapping suffix-plus-prefix bridge relation, or a boundary endpoint equality.  These are the listed rows. ∎

---

## C12.9. External/bridge rank-descent theorem

## Theorem C12.9: EXTERNAL_COLLISION and BRIDGE_GAP rows are verified modulo weighted repair

In ARBITRARY phase, every EXTERNAL_COLLISION or BRIDGE_GAP state either:

```text
1. decreases enclosing_span;
2. decreases bridge_gap;
3. decreases support_size;
4. routes to a C11-verified local row;
5. routes to SEPARATED_EQUAL/MIDPOINT rows verified in C11;
6. re-enters EXTERNAL_COLLISION with finite boundary/transition budget decrease;
7. routes to WEIGHTED_REPAIR;
8. reaches collision-free SNS success;
9. reaches atom/subset contradiction.
```

### Proof

External normal forms are Lemma C12.1.  Proper overlap descends by Lemma C12.2.  Proper containment descends by Lemma C12.3.  Disjoint bridge relations are Lemma C12.4.  Gap-after descent and collision exits are Lemmas C12.5--C12.6.  Rigid same-gap returns are Lemma C12.7.  Cyclic/wrapped data is Lemma C12.8.  These exhaust external/bridge geometry. ∎

---

## C12.10. Remaining obligations after C12

C12 leaves only one major rank row unverified:

```text
WEIGHTED_REPAIR.
```

Also still needed:

```text
1. explicit finite transition-budget bounds for external/cyclic boundary subcases;
2. endpoint/sign appendix tables;
3. verification that re-entered EXTERNAL_COLLISION cases consume budget rather than loop.
```

---

## C12.11. Recommended next file

The next file should verify the weighted repair rank row:

```text
docs/final/F00_SNS_C13_weighted_rank_descent_verification.md
```

Goal:

```text
Check WEIGHTED_REPAIR under SNS collision-defect mode, including easy reductions, fixed cut-swap, smaller middle, weak cut-rigidity, and pattern-rigid exit.
```

---

## C12.12. Status

```text
Status: external/bridge rank-descent verification draft.
Risk: ORANGE.
Remaining major row: WEIGHTED_REPAIR.
```
