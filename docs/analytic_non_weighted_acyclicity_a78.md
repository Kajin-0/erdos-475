# Analytic non-weighted acyclicity theorem A78

This note continues from A77.

A72 built the obstruction dependency graph.  A73 reduced non-weighted global acyclicity to bridge-span monotonicity.  A74 reduced bridge-span monotonicity to equal-span separated bridge returns.  A75 reduced equal-span separated bridge returns to gap-preserving separated recurrence.  A76 reduced gap-preserving separated recurrence to rigid separated self-return.  A77 routed rigid separated self-return back into already-known recurrence, midpoint, separated-equal, zero-composite, or external/cyclic mechanisms.

This note records the resulting non-weighted acyclicity theorem.

The theorem is still conditional on the correctness of the local routing lemmas A1--A77 and on the exclusion of the genuine weighted-core branch.  It does not prove the full Erdős 475 endpoint-avoidance theorem because weighted cut-selection remains open.

---

## 1. Non-weighted graph

Remove the genuine weighted-core node and its open cut-selection edge:

```text
WEIGHTED_CORE -> WEIGHTED_CUT_SWAP.
```

The remaining obstruction classes are:

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
EXTERNAL_COLLISION.
```

Terminal classes are:

```text
SUCCESS,
CONTRADICTION.
```

---

## 2. Global non-weighted measure

Use the measure from A73, refined by the bridge/gap coordinates from A74--A76:

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

All coordinates are nonnegative integers, ordered lexicographically.

Definitions:

- `enclosing_span`: length of the smallest interval enclosing the active obstruction.
- `gap_length`: separated-equal gap length when applicable; otherwise `0`.
- `support_size`: number of participating atoms in the active obstruction.
- `recurrence_depth`: consecutive forbidden-recurrence routings since last strict collision descent.
- `pair_depth`: consecutive pair-difference boundary routings since last strict zero-composite/equal-interval descent.
- `separated_depth`: consecutive separated-equal routings since last strict gap/span descent.
- `bridge_depth`: consecutive bridge returns since last proper-overlap/containment descent.
- `type_rank`: obstruction class rank.
- `boundary_rank`: endpoint/boundary degeneracy rank.
- `h_excess`: recurrent first-hit index minus the globally minimal first-hit index.

As in A64, `h_excess` is placed last.  Minimality forbids `h'<h`; it does not make later recurrent hits primary complexity.

---

## 3. Terminal/collapse edges

## Lemma A78.1: zero-collapse and prefix-zero terminate

Any branch entering

```text
ZERO_COLLAPSE
```

or

```text
PREFIX_ZERO
```

contradicts Graham-validity unless it is the trivial empty/basepoint case already excluded.

### Proof

A nonempty zero interval produces equal partial sums.  A prefix-zero interval collides with the basepoint.  Graham-validity forbids both. ∎

---

## 4. Transported-prefix normalization

## Lemma A78.2: transported-prefix artifacts do not create cycles

A transported-prefix artifact rewrites an apparent coefficient-2 relation into a zero-composite relation without increasing `enclosing_span` or `support_size`, and strictly lowers the representation rank.

### Proof

This is A56.1--A56.2.  The rewrite uses a containing block already present in the support and removes the artificial doubled-prefix/tail representation. ∎

---

## 5. Zero-composite/pair-difference cycle

## Lemma A78.3: zero-composite and pair-difference cycling decreases `M_NW^*`

Any route

```text
ZERO_COMPOSITE_SURGERY -> PAIR_DIFFERENCE -> ZERO_COMPOSITE_SURGERY
```

strictly decreases one of:

```text
enclosing_span,
support_size,
pair_depth,
boundary_rank,
type_rank.
```

unless it exits to forbidden recurrence, equal/signed interval, singleton recurrence, or collapse.

### Proof

A73.3--A73.5 record the support containment and boundary-rank descent.  A33 and A69 show that non-crossing pair blockers descend, while crossing pair blockers route to equal/signed interval, zero-composite bridge, singleton recurrence, or endpoint recurrence.  In no case does the exact same pair/zero-composite state repeat with all coordinates fixed. ∎

---

## 6. Singleton/pair/cyclic recurrence cycles

## Lemma A78.4: singleton and pair recurrence cannot cycle with fixed measure

Any cycle through

```text
SINGLETON_RECURRENCE
PAIR_DIFFERENCE
```

strictly decreases `M_NW^*` or exits to zero-composite, bridge interval, cyclic recurrence, or collapse.

### Proof

A70 routes singleton-prefix recurrence to suffix-zero descent, pair-difference prefix descent, bridge signed composite, or endpoint pair-difference.  A69 routes pair-difference recurrence to non-crossing descent or crossing bridge/equal/signed/singleton mechanisms.  The only apparent return carries lower support or higher boundary specificity, which is bounded and then exits. ∎

---

## Lemma A78.5: cyclic and singleton recurrence cannot cycle with fixed bridge/gap data

Any cycle through

```text
CYCLIC_RECURRENCE
SINGLETON_RECURRENCE
```

either:

```text
1. creates an earlier rotated forbidden hit, contradiction;
2. collapses to midpoint/zero-composite;
3. produces a bridge whose span/gap decreases by A74--A77;
4. exits to pair-difference or separated-equal routing.
```

### Proof

A71 routes cyclic recurrence to midpoint, zero-composite, wrapping bridge, or singleton recurrence.  A70 routes singleton bridge cases back to cyclic geometry only with explicit bridge data.  A74--A77 eliminate non-decreasing bridge/gap returns except rigid separated self-return, which A77 routes to known recurrence mechanisms without introducing a new state. ∎

---

## 7. Separated-equal/recurrent cycle

## Lemma A78.6: separated-equal recurrence cannot preserve all global coordinates

Any cycle

```text
SEPARATED_EQUAL -> ZERO_COMPOSITE_SURGERY -> FORBIDDEN_RECURRENCE -> SEPARATED_EQUAL
```

either:

```text
1. decreases support/span through D1--D5 or E1--E5 routing;
2. enters D2 zero-composite surgery controlled by A52--A53;
3. reduces gap to zero via gap-after and enters midpoint A55;
4. routes through an external bridge handled by A74--A77;
5. exits to cyclic/singleton recurrence handled by A70--A71.
```

Thus it cannot repeat with fixed `M_NW^*`.

### Proof

A36--A54 route direct and gap-after separated-equal collisions.  A74--A77 handle the bridge-span/gap-preserving tie.  A55 handles midpoint. ∎

---

## 8. External collision edges

## Lemma A78.7: external collisions are routing edges, not cycle sources

Any external collision produced by a transformed move pulls back to:

```text
zero-composite,
equal interval,
signed interval,
transported-prefix artifact,
or forbidden recurrence.
```

It does not create a new obstruction class.

### Proof

This is A62. ∎

---

## 9. Main non-weighted acyclicity theorem

## Theorem A78.8: non-weighted obstruction graph is acyclic under `M_NW^*`

Assume the local routing lemmas A1--A77.  In the obstruction dependency graph with `WEIGHTED_CORE` removed, every directed path either:

```text
1. reaches SUCCESS;
2. reaches CONTRADICTION;
3. strictly decreases M_NW^* after finitely many routing steps.
```

Therefore there is no infinite non-weighted obstruction path avoiding success and contradiction.

### Proof

All terminal/collapse edges terminate by Lemma A78.1.  Transported-prefix edges normalize by Lemma A78.2.  The visible cycles from A72 are handled by Lemmas A78.3--A78.6.  External collisions are routing edges by Lemma A78.7.  Every other edge in the non-weighted graph is a local strict descent, a collapse, or an entry into one of the handled cycles.

Since `M_NW^*` is a lexicographic measure on nonnegative integer tuples, it is well-founded.  Thus infinite descent is impossible. ∎

---

## 10. Consequence

The non-weighted side of the proof program is now closed at the architectural level:

```text
If no genuine weighted core occurs, the routed obstruction process terminates.
```

This does not prove endpoint avoidance because genuine weighted signed cores remain possible.

The remaining analytic problem is now sharply isolated:

```text
weighted core cut-selection theorem.
```

---

## 11. Remaining weighted gap

The genuine weighted core has form

```text
A+2B+C=0
```

after all A56 easy reductions fail:

```text
B != 0,
A+B != 0,
B+C != 0,
A != C,
no transported-prefix/tail rewrite.
```

A58 rewrote it as nested zero-composite:

```text
ABC+B=0.
```

A59 showed static cuts of `B` do not close it.

A60 showed that for any chosen proper cut

```text
B=P R,
```

the dynamic cut-swap

```text
A P R C -> A R P C
```

has displayed collisions routed locally.

What is missing is:

```text
there exists a useful proper cut B=P R.
```

---

## 12. Target A79

A79 should attack weighted core cut-selection directly.

Suggested statement:

> In a genuine weighted core `A+2B+C=0`, either there exists a proper cut `B=P R` such that the A60 cut-swap gives descent/success/controlled recurrence, or the weighted core contains a smaller genuine weighted core on a strict subblock of `B`.

The key measure should be:

```text
middle_length = |B|.
```

If every cut fails, the failure pattern should impose enough constraints to force one of the A56 easy reductions after all:

```text
B=0,
A+B=0,
B+C=0,
A=C,
transported-prefix rewrite.
```

---

## Current status

Proved here:

1. non-weighted global measure `M_NW^*`;
2. zero-composite/pair cycle decreases;
3. singleton/pair/cyclic recurrence cycles decrease or route out;
4. separated-equal recurrence cycle decreases after A74--A77;
5. external collisions are routing edges;
6. non-weighted obstruction graph is acyclic conditional on A1--A77 local routings.

Not proved here:

1. weighted core cut-selection;
2. final endpoint avoidance theorem;
3. finite verification / exceptional characteristic bridge.
