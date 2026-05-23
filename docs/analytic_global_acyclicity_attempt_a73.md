# Analytic global acyclicity attempt A73

This note continues from A72.

A72 built the directed dependency graph of routed obstruction classes and identified the visible cycles.  The next step is to prove that the routed graph cannot cycle indefinitely under a well-founded measure.

This note starts that task for the subgraph excluding the genuine weighted core.  The weighted branch remains separated because A72 identified the open edge

```text
WEIGHTED_CORE -> WEIGHTED_CUT_SWAP
```

as the weighted cut-selection theorem.

No complete proof is claimed here.  The result is a partial acyclicity theorem for the non-weighted routed graph, conditional on edge-local span/support descent statements already established in the A-notes and on a recurrence-depth normalization.

---

## 1. Non-weighted subgraph

Exclude the node

```text
WEIGHTED_CORE
```

and the open edge

```text
WEIGHTED_CORE -> WEIGHTED_CUT_SWAP.
```

The remaining high-level nodes are:

```text
ZERO_COLLAPSE
PREFIX_ZERO
TWO_PIECE_ZERO
THREE_PIECE_ZERO
HIGHER_ZERO_COMPOSITE
ZERO_COMPOSITE_SURGERY
EQUAL_INTERVAL
SIGNED_INTERVAL
SEPARATED_EQUAL
MIDPOINT
PAIR_DIFFERENCE
SINGLETON_RECURRENCE
CYCLIC_RECURRENCE
FORBIDDEN_RECURRENCE
EXTERNAL_COLLISION
TRANSPORTED_PREFIX
SUCCESS
CONTRADICTION
```

The visible non-weighted cycles from A72 are:

```text
CYCLE 1: ZERO_COMPOSITE_SURGERY <-> PAIR_DIFFERENCE
CYCLE 2: SINGLETON_RECURRENCE -> PAIR_DIFFERENCE -> SINGLETON_RECURRENCE
CYCLE 3: CYCLIC_RECURRENCE -> SINGLETON_RECURRENCE -> CYCLIC_RECURRENCE
CYCLE 5: SEPARATED_EQUAL -> ZERO_COMPOSITE_SURGERY -> FORBIDDEN_RECURRENCE -> SEPARATED_EQUAL
```

---

## 2. Candidate non-weighted measure

For an active obstruction state `O`, define

```text
M_NW(O)=(
  span,
  support_size,
  recurrence_depth,
  pair_depth,
  separated_depth,
  type_rank,
  boundary_rank,
  h_excess
).
```

All coordinates are ordered lexicographically with the usual well-order on nonnegative integers.

Definitions:

- `span`: enclosing interval length of the active obstruction in the current ordering.
- `support_size`: number of participating atoms across all pieces.
- `recurrence_depth`: number of consecutive forbidden-recurrence routings since the last strict collision descent.
- `pair_depth`: number of consecutive pair-difference boundary routings since the last strict zero-composite or equal-interval descent.
- `separated_depth`: number of consecutive separated-equal routings since the last strict equal-interval or zero-composite descent.
- `type_rank`: obstruction class rank.
- `boundary_rank`: endpoint/boundary degeneracy rank.
- `h_excess`: first forbidden index of the recurrent ordering minus the globally minimal first forbidden index.

### Important design choice

Unlike A34's earliest measure, `h_excess` is last, not first.  A64 showed that first-hit minimality only forbids `h'<h`; it does not make a later recurrent hit structurally worse than a smaller obstruction.

---

## 3. Type ranks for the non-weighted graph

Use the following rank order for non-terminal classes:

```text
ZERO_COLLAPSE              0
PREFIX_ZERO                1
TWO_PIECE_ZERO             2
THREE_PIECE_ZERO           3
HIGHER_ZERO_COMPOSITE      4
EQUAL_INTERVAL             5
SIGNED_INTERVAL            6
SEPARATED_EQUAL            7
MIDPOINT                   8
ZERO_COMPOSITE_SURGERY     9
PAIR_DIFFERENCE           10
SINGLETON_RECURRENCE      11
CYCLIC_RECURRENCE         12
FORBIDDEN_RECURRENCE      13
EXTERNAL_COLLISION        14
TRANSPORTED_PREFIX        15
```

This type rank is deliberately placed after structural coordinates.  It is a tie-breaker, not the primary descent mechanism.

---

## 4. Terminal and normalizing classes

## Lemma A73.1: collapse classes are terminal

The classes

```text
ZERO_COLLAPSE,
PREFIX_ZERO
```

terminate in contradiction to Graham-validity or in an already impossible zero-prefix/interior-zero branch.

### Proof

This is the standard Graham-validity condition: repeated partial sums are impossible, and a nonempty zero interval produces repeated partial sums.  Prefix-zero is the same collision with the basepoint. ∎

---

## Lemma A73.2: transported-prefix classes are normalizing, not cyclic

A transported-prefix artifact rewrites an apparent coefficient-2 relation into a composite-zero relation without increasing span or support.

Thus

```text
TRANSPORTED_PREFIX -> ZERO_COMPOSITE_SURGERY
```

is non-increasing in `(span,support_size)` and strictly lowers `type_rank` after normalization.

### Proof

A56.1--A56.2 replace `2P+R` by `P+B` or `P+2R` by `B+R` for a known containing block `B=PR`.  No new support outside the original containing block is introduced.  The branch leaves the weighted/signed representation and enters ordinary composite-zero surgery. ∎

---

## 5. Zero-composite / pair-difference cycle

The main non-weighted local cycle is:

```text
ZERO_COMPOSITE_SURGERY -> PAIR_DIFFERENCE -> ZERO_COMPOSITE_SURGERY.
```

A31--A33 and A65--A70 show that pair-difference branches arise only as boundary branches of atom insertion, endpoint blocker pullbacks, or singleton/pair recurrence routing.

---

## Lemma A73.3: zero-composite to pair-difference increases boundary rank but preserves or lowers span

When zero-composite surgery routes to `PAIR_DIFFERENCE`, the pair-difference obstruction is supported on a boundary atom pair and a block/prefix contained in or adjacent to the source zero-composite support.  Its span is no larger than the source zero-composite span.

If the span is equal, the pair-depth increases by one and boundary rank records the endpoint-pair trap.

### Proof sketch

This is the common structure in A33, A47, A51--A53, A65--A70: the pair-difference relation has form

```text
q-q1=sum(P)
```

or a prefix variant where `P` is a side of the zero block or a proper prefix/tail generated by a blocker pullback.  The support is contained in the source window plus the adjacent atom pair already used by the surgery.  No external bridge is introduced unless the branch has already been routed to equal/signed interval or external collision. ∎

---

## Lemma A73.4: pair-difference returns to zero-composite only with smaller pair depth or smaller span

A pair-difference branch routed back to zero-composite surgery either:

```text
1. creates a smaller zero-composite/prefix obstruction;
2. routes to singleton recurrence;
3. routes to equal/signed interval;
4. remains in a boundary endpoint pair case with strictly lower boundary rank after one swap.
```

In cases 1 and 4, `M_NW` decreases.  In cases 2 and 3, the branch leaves the pair/zero-composite cycle.

### Proof sketch

A33 pair-swap analysis and A69 pair-swap recurrence show that non-crossing blockers descend, while crossing blockers route to equal/signed interval, zero-composite bridge, or singleton recurrence.  The only direct return to zero-composite uses a proper prefix/suffix or a lower boundary case. ∎

---

## Proposition A73.5: the zero-composite / pair-difference cycle is acyclic modulo recurrence routing

There is no infinite directed path using only

```text
ZERO_COMPOSITE_SURGERY
PAIR_DIFFERENCE
```

unless it passes through `FORBIDDEN_RECURRENCE` or an interval class.  Along every direct return edge inside the two-node cycle, `M_NW` decreases in span, support size, pair depth, or boundary rank.

### Proof

Combine Lemmas A73.3--A73.4.  Pair-depth and boundary-rank are tie-breakers for equal-span endpoint pair traps; proper prefix/suffix cases reduce span or support size. ∎

---

## 6. Singleton / pair recurrence cycle

The visible cycle is:

```text
SINGLETON_RECURRENCE -> PAIR_DIFFERENCE -> SINGLETON_RECURRENCE.
```

A70 shows singleton recurrence routes to pair-difference only through right-blocker endpoint or proper-prefix pair-difference branches.

---

## Lemma A73.6: singleton recurrence to pair-difference lowers local prefix support unless it is an endpoint boundary

In A70, a singleton-prefix recurrence `x+B_i=f` routes to pair-difference through

```text
b_- - b_+ + C_r=0.
```

If `C_r` is proper, support decreases.  If `C_r` is the full local tail, the branch is an endpoint pair-difference boundary with increased boundary rank but no larger span.

### Proof

This is A70.4--A70.6. ∎

---

## Lemma A73.7: pair-difference to singleton recurrence raises recurrence_depth only after bounded-blocker descent fails

A pair-difference branch can route to singleton recurrence only through a recurrent transformed ordering.  By A64, if the nearest blocker is bounded, span decreases.  If not, A69 routes the long-blocker case to bridge/equal/zero-composite branches or endpoint singleton recurrence.

Thus a direct pair-to-singleton return without span decrease must pass through a boundary-ranked endpoint case.

### Proof sketch

This is the A64 bounded-blocker theorem plus A69 endpoint recurrence classification. ∎

---

## Proposition A73.8: the singleton / pair recurrence cycle is controlled by span and boundary rank

There is no infinite cycle

```text
SINGLETON_RECURRENCE -> PAIR_DIFFERENCE -> SINGLETON_RECURRENCE
```

with fixed span, support size, and boundary rank.  Any nontrivial return either decreases span/support or increases boundary specificity until it reaches a zero atom, zero-composite, bridge interval, or cyclic recurrence branch.

### Proof sketch

Apply Lemmas A73.6--A73.7.  Boundary rank is finite; when it reaches the endpoint pair trap, A33/A69 route it away from the two-node cycle. ∎

---

## 7. Cyclic / singleton recurrence cycle

The cycle is:

```text
CYCLIC_RECURRENCE -> SINGLETON_RECURRENCE -> CYCLIC_RECURRENCE.
```

A71 shows cyclic recurrence routes to singleton recurrence only through wrapping bridge or translated endpoint-pair geometry.  A70 shows singleton bridge cases may route to cyclic geometry.

---

## Lemma A73.9: cyclic-to-singleton routing either creates an earlier rotated hit or a bridge composite

By A71, a cyclic recurrence branch either:

```text
1. creates an earlier rotated forbidden hit, contradicting minimality;
2. produces a midpoint/zero-collapse branch;
3. produces a non-wrapping interval obstruction;
4. produces a wrapping bridge zero/signed composite;
5. routes to singleton-prefix recurrence.
```

The singleton case occurs only from endpoint/bridge geometry of the rotation.

### Proof

This is A71.2--A71.8. ∎

---

## Lemma A73.10: singleton-to-cyclic routing increases cyclic specificity but exposes a bridge

A70 routes singleton bridge cases to cyclic-cut geometry only when the blocker crosses the local basepoint or endpoint.  Such a branch exposes an explicit bridge interval:

```text
L+B_i^-+b_+=0
```

or

```text
C+R+b_- - b_+=0.
```

Thus the return to cyclic recurrence carries a concrete bridge composite whose span is either smaller than the original recurrence support or is a wrapping interval subject to A71's earlier-hit criterion.

### Proof

This is A70.3, A70.6, and A71.7. ∎

---

## Proposition A73.11: cyclic / singleton cycling reduces to bridge-composite termination

The only possible non-descending cycle between cyclic and singleton recurrence is a repeated wrapping bridge composite.  Therefore this cycle is controlled if bridge composites have a strictly decreasing bridge span under repeated normalization.

### Proof

A73.9 and A73.10 show every return edge exposes bridge data.  If bridge span decreases, termination follows.  If bridge span does not decrease, the same cyclic cut geometry repeats, and A71.7 forces either an earlier forbidden hit or an identical endpoint-pair equation, which is a midpoint/separated-equal branch already routed. ∎

### Status

This is still conditional on a bridge-span monotonicity lemma.

---

## 8. Separated-equal / recurrence cycle

The visible cycle is:

```text
SEPARATED_EQUAL -> ZERO_COMPOSITE_SURGERY -> FORBIDDEN_RECURRENCE -> SEPARATED_EQUAL.
```

A36--A54 route separated-equal collision branches.  D2 routes to zero-composite surgery modulo A34.  Recurrence can re-enter separated-equal through external collisions or bridge equalities.

---

## Lemma A73.12: separated-equal collision routing never increases the original gap span

In the separated-equal setup

```text
X A G C Y,
sum(A)=sum(C),
```

the direct and gap-after collision equations route to equal intervals, two-piece zero, three-piece zero, or D2 zero composites supported inside the displayed span `A G C Y`.

Thus collision routing does not introduce a larger enclosing span unless an external bridge collision occurs, which is handled by A62.

### Proof sketch

This summarizes A36--A54 and A49. ∎

---

## Lemma A73.13: recurrence back into separated-equal must pass through an external bridge equality or midpoint boundary

If a forbidden recurrence from zero-composite surgery returns to separated-equal form, the equal blocks arise either from:

```text
1. a proper-overlap/equal-interval descent;
2. an external bridge collision A62;
3. a midpoint boundary A55/A71.
```

Cases 1 and 3 are routed locally; case 2 carries bridge span data.

### Proof sketch

External collisions pull back to interval geometry by A62.  Equal blocks are exactly equal-interval geometry, whose zero-gap boundary is midpoint and whose separated case is A36. ∎

---

## Proposition A73.14: separated-equal recurrence cycling reduces to bridge-span or A34 bounded-blocker descent

The cycle

```text
SEPARATED_EQUAL -> ZERO_COMPOSITE_SURGERY -> FORBIDDEN_RECURRENCE -> SEPARATED_EQUAL
```

cannot persist with fixed span unless every return to separated-equal comes from an external bridge of the same span.  In that tie case, the needed statement is a bridge-span monotonicity lemma.

### Proof sketch

Inside the displayed span, separated-equal routing does not increase span by Lemma A73.12.  Bounded recurrence descends by A64.  Therefore only external bridge return edges can tie the measure. ∎

---

## 9. Bridge-span monotonicity gap

A73 reduces the non-weighted acyclicity problem to one repeated theme:

```text
bridge-span monotonicity.
```

Bridge branches appear in:

```text
H1/H2 crossing blockers,
pair-swap crossing blockers,
singleton-prefix bridge blockers,
cyclic wrapping blockers,
external collisions,
separated-equal recurrence returns.
```

The required lemma is:

## Target bridge monotonicity lemma BML

If a recurrence/collision branch routes through an external bridge interval and then returns to a previously seen obstruction class without strict local descent, then the bridge span strictly decreases, or the branch collapses to midpoint/separated-equal/zero-composite with smaller support.

This is not proved in A73.

---

## 10. Partial non-weighted acyclicity theorem

## Theorem A73.15: non-weighted routed graph is acyclic modulo bridge-span monotonicity

Exclude `WEIGHTED_CORE`.  Assume the bridge monotonicity lemma BML.  Then the non-weighted obstruction dependency graph has no infinite directed path avoiding `SUCCESS` and `CONTRADICTION`.

### Proof sketch

Visible cycles from A72 are handled as follows:

- zero-composite/pair cycle: Proposition A73.5;
- singleton/pair cycle: Proposition A73.8;
- cyclic/singleton cycle: Proposition A73.11 plus BML;
- separated-equal/recurrent cycle: Proposition A73.14 plus BML;
- external collision cycles: A62 routes them into bridge composites, then BML applies.

All remaining edges are descending, collapsing, or normalizing into one of these cycles.  Since `M_NW` is lexicographic over finite nonnegative coordinates and BML supplies strict bridge descent in the only tie cases, infinite descent is impossible. ∎

---

## 11. What remains after A73

A73 does not complete the proof.  It reduces global acyclicity to two explicit missing pieces:

```text
1. bridge-span monotonicity lemma BML;
2. weighted core cut-selection theorem.
```

Together with a finite verification bridge, these are the remaining major proof obligations.

---

## 12. Target A74

A74 should attack bridge-span monotonicity.

Start from the generic bridge relation from A62/A70/A71:

```text
L + U = 0
```

or signed form

```text
L - U + atom corrections = 0,
```

where `L` is an external bridge crossing the boundary of the local source obstruction.

The goal is to show that if such a bridge returns to the same obstruction class, then either:

```text
span(L) decreases,
proper-overlap uncrossing gives smaller equal interval,
midpoint/separated-equal routing applies,
or zero-composite descent applies.
```

---

## Current status

Proved/argued here:

1. non-weighted graph measure `M_NW`;
2. zero-composite/pair cycle controlled modulo recurrence;
3. singleton/pair cycle controlled modulo boundary-rank descent;
4. cyclic/singleton cycle reduced to bridge-span monotonicity;
5. separated-equal/recurrent cycle reduced to bridge-span monotonicity;
6. partial non-weighted acyclicity theorem conditional on BML.

Not proved here:

1. bridge-span monotonicity BML;
2. weighted cut-selection;
3. finite verification bridge;
4. endpoint avoidance theorem.
