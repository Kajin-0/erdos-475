# Analytic bridge/gap measure hardening A98

This note continues from A97.

A93 isolated five hardening obligations:

```text
U1. Strict progress lemma.
U2. Universal external-collision classification.
U3. Recurrence bounded-blocker measure.
U4. Cut-swap displayed collision table.
U5. Bridge/gap measure inequalities.
```

A94 addressed U1.  A95 addressed U2.  A96 addressed U3.  A97 addressed U4.  A98 addresses U5 by hardening the bridge/gap measure inequalities from A74--A77.

The target is the bridge/gap chain:

```text
bridge-span monotonicity
  -> equal-span separated bridge return
  -> gap-preserving separated recurrence
  -> rigid separated self-return
  -> direct exchange / recurrence routing.
```

A98 makes the measure decreases explicit.

---

## 1. Bridge setup

Let a local source obstruction have active support interval

```text
S=[s_0,s_1].
```

A bridge obstruction consists of:

```text
B_ext  = external bridge interval;
U      = internal source piece;
E      = optional atom/pair correction.
```

Typical equations are:

```text
B_ext + U = 0,
B_ext - U + E = 0,
B_ext + U + E = 0.
```

The bridge enclosure is the smallest interval containing all participating atoms:

```text
Enc(B_ext,U,E).
```

---

## 2. Bridge/gap measure

Define the bridge/gap measure:

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

where:

```text
enclosing_span = length of Enc(B_ext,U,E);
bridge_gap     = number of atoms strictly between B_ext and U if disjoint, else 0;
bridge_length  = |B_ext|;
internal_length= |U|;
support_size   = total number of participating atoms;
recurrence_depth = consecutive recurrence returns since last strict descent;
type_rank      = obstruction-class rank;
boundary_rank  = endpoint-degeneracy rank.
```

The order is lexicographic over nonnegative integers.

For bridge/gap states inside the full proof, `M_BG` is embedded into `M_NW^*` by using:

```text
enclosing_span -> enclosing_span,
bridge_gap     -> gap_length,
support_size   -> support_size,
recurrence_depth -> recurrence_depth,
type_rank/boundary_rank -> same coordinates.
```

---

## 3. Proper-overlap descent

Two intervals `B_ext` and `U` properly overlap if:

```text
B_ext cap U nonempty,
B_ext not subset U,
U not subset B_ext.
```

Write, in one orientation,

```text
B_ext = B_0 O,
U     = O U_1,
```

where `O` is the nonempty overlap and `B_0,U_1` are nonempty tails.

If

```text
sum(B_ext)=sum(U),
```

then

```text
sum(B_0)=sum(U_1).
```

The overlap `O` is removed.

## Lemma A98.1: proper-overlap bridge decreases enclosing span

A proper-overlap bridge equality or signed bridge relation after bounded correction normalization produces an equal-interval or zero-composite obstruction whose enclosing span is strictly smaller than the original bridge enclosure.

### Proof

Cancel the common overlap.  The resulting active pieces are the non-overlapping tails `B_0` and `U_1`, or those tails plus bounded atom correction `E`.  The overlap contains at least one atom and is removed from the active support.  Therefore the new enclosure is strictly contained in the old enclosure, unless `E` lies outside the old enclosure.  If `E` lies outside, the case is not a proper-overlap internal bridge but an external signed bridge already classified by A95. ∎

---

## 4. Proper-containment descent

Suppose one interval properly contains the other.

Case 1:

```text
B_ext = L U R
```

with at least one of `L,R` nonempty.  Equality gives:

```text
sum(L)+sum(R)=0.
```

Case 2:

```text
U = L B_ext R
```

with at least one of `L,R` nonempty.  Equality gives the same kind of complement zero relation.

## Lemma A98.2: proper containment decreases support or span

A proper-containment bridge equality produces either:

```text
1. a nonempty zero interval;
2. a two-piece zero-composite;
3. a signed zero-composite after bounded correction normalization.
```

The resulting obstruction has strictly smaller support size than the original bridge relation.  If the complement lies on one side, it also has strictly smaller enclosing span.

### Proof

Subtract the contained interval from the containing interval.  The contained block is removed from the active relation.  Hence support size strictly decreases.  If only one complement side remains, the enclosing span also strictly decreases. ∎

---

## 5. Disjoint bridge equality

If `B_ext` and `U` are disjoint, the bridge relation is separated-equal or signed separated-equal.

Write:

```text
B_ext G U
```

or

```text
U G B_ext
```

where `G` is the nonempty gap.

If

```text
sum(B_ext)=sum(U),
```

then this is a separated-equal branch.

## Lemma A98.3: disjoint bridge equality is the only nonlocal span tie

If a bridge relation is not proper-overlap and not proper-containment, then the bridge and internal piece are disjoint.  The branch is separated-equal or signed separated-equal.  Its measure is governed by `bridge_gap=|G|`.

### Proof

For intervals in a linear order, the only alternatives are disjoint, proper overlap, containment, or equality.  Equality gives zero difference immediately or identical interval cancellation, so the nontrivial case is disjoint separated equality. ∎

---

## 6. Equal-span separated bridge return

An equal-span separated bridge return is:

```text
B G U,
sum(B)=sum(U),
G nonempty,
```

where the enclosing span does not decrease relative to the source obstruction.

Use the gap-after move:

```text
B G U -> B U G.
```

This makes `B` and `U` adjacent and moves the gap after them.

## Lemma A98.4: successful gap-after move decreases bridge_gap to zero

If the gap-after move is Graham-valid and avoids `f`, then the separated bridge gap decreases from `|G|` to `0` in the active equal-block configuration.

### Proof

Before the move, `G` lies strictly between `B` and `U`.  After the move, the displayed equal blocks are adjacent as `B U`.  Hence the separating gap is zero. ∎

---

## Lemma A98.5: gap-after collisions leave the equal-span bridge-return class

Any displayed collision of

```text
B G U -> B U G
```

routes to:

```text
two-piece zero,
three-piece zero,
equal-interval descent,
zero collapse,
external collision handled by A95.
```

Thus it either decreases `M_BG` or exits the bridge/gap class.

### Proof

This is the hardened form of the A49/A75 gap-after table.  Collision equations have one of the forms:

```text
prefix(U)+tail(B)=0,
G+tail(U)+prefix(Y)=0,
U+tail(B)+prefix(G)=0,
tail(G)+prefix(Y)=0,
B+prefix(G)=prefix(U).
```

The first four are zero-composite/equal-interval branches.  The last is equal-interval or pair-difference after uncrossing.  If an endpoint outside the displayed window is involved, A95 applies. ∎

---

## Lemma A98.6: gap-after recurrence is the only non-descending separated bridge outcome

For equal-span separated bridge return, the gap-after move gives exactly one of:

```text
1. success, with bridge_gap -> 0;
2. collision, routed by Lemma A98.5;
3. recurrence, handled by A64--A71;
4. external collision, handled by A95.
```

Thus the only possible non-descending continuation is recurrence.

### Proof

A transformed ordering is either Graham-valid and avoiding `f`, non-Graham, or Graham-valid and recurrent.  External collisions are non-Graham collisions outside the displayed table and are A95 cases. ∎

---

## 7. Gap-preserving separated recurrence

A recurrence after gap-after is gap-preserving only if the A5 blocker pullback recreates a separated-equal bridge with the same gap `G`.

A76 showed that using a proper prefix or proper tail of `G` strictly decreases the gap.

## Lemma A98.7: proper use of the gap decreases bridge_gap

If the recurrent A5 blocker pullback uses a proper prefix or proper tail of the old gap `G` as the new separating gap, then the new bridge gap length is strictly less than `|G|`.

### Proof

A proper prefix or proper tail of `G` contains fewer atoms than `G`.  Since `bridge_gap` counts atoms strictly between the separated equal pieces, replacing `G` by a proper subblock strictly decreases `bridge_gap`. ∎

---

## Lemma A98.8: preserving bridge_gap forces full-gap endpoint alignment

If the recurrence pullback returns to a separated-equal bridge with the same `bridge_gap=|G|`, then the full old gap `G` is reused and both gap endpoints are unchanged.

### Proof

If either endpoint moves inward, the gap is shortened.  If either endpoint moves outward, the enclosing span increases or external material is absorbed into the gap, which is an external bridge case handled by A95/A74.  Under equal-span preservation, neither outward move is allowed.  Hence the old endpoints are reused. ∎

---

## 8. Rigid separated self-return

By Lemma A98.8, a gap-preserving recurrence must be rigid: it reconstructs either

```text
B G U
```

or

```text
U G B
```

with the same gap endpoints.

## Lemma A98.9: same-orientation rigid return is endpoint/cyclic or decreases measure

A same-orientation rigid return to `B G U` either:

```text
1. uses a proper prefix/tail of B, G, or U and decreases support/gap;
2. uses endpoint U and routes to adjacent-equal/midpoint;
3. uses endpoint G and routes to cyclic/external recurrence;
4. produces zero collapse inside G.
```

Thus it cannot preserve `M_BG` as a new bridge/gap state.

### Proof

This is the hardened measure form of A77.3--A77.5.  Proper-prefix cases decrease support or `bridge_gap` by Lemma A98.7.  Endpoint U makes the equal blocks adjacent, so `bridge_gap=0`.  Endpoint G is no longer an internal separated bridge return; it is a cyclic/external recurrence classified by A71/A95. ∎

---

## Lemma A98.10: exchange-orientation rigid return factors through direct exchange

A rigid return to

```text
U G B
```

is exactly the direct-exchange target of the separated-equal pair:

```text
B G U -> U G B.
```

If direct exchange succeeds, the obstruction path succeeds.  If it collides, the A36--A54 direct-exchange table routes to non-weighted classes.  If it is recurrent, A70/A71 route it.

Therefore exchange-orientation rigid return does not preserve `M_BG` as a new bridge/gap state.

### Proof

The exchanged separated-equal state is definitionally the direct-exchange target.  The success/collision/recurrent trichotomy is exhaustive. ∎

---

## 9. Bridge/gap descent theorem

## Theorem A98.11: bridge/gap returns strictly descend or route out

Every bridge/gap obstruction produced by the A62/A95 external-collision or recurrence machinery either:

```text
1. decreases enclosing_span by proper-overlap uncrossing;
2. decreases support_size by proper-containment subtraction;
3. decreases bridge_gap by gap-after success or proper-gap recurrence;
4. routes to zero-composite/equal/signed interval machinery;
5. routes to recurrence A64--A71;
6. routes to external collision A95;
7. routes to midpoint/adjacent-equal machinery;
8. factors through direct exchange and routes by A36--A54;
9. reaches collapse or success.
```

In particular, no bridge/gap branch can cycle indefinitely with fixed `M_BG`.

### Proof

Proper overlap is Lemma A98.1.  Proper containment is Lemma A98.2.  Disjoint equality is Lemma A98.3.  Equal-span separated bridge returns are handled by Lemmas A98.4--A98.6.  Gap-preserving recurrence is handled by Lemmas A98.7--A98.8.  Rigid same-orientation and exchange-orientation returns are Lemmas A98.9--A98.10.  These cases exhaust bridge/gap geometry. ∎

---

## 10. Consequence for non-weighted acyclicity

A98 hardens U5.  Together with:

```text
A94 strict progress;
A95 external collision classification;
A96 bounded-blocker recurrence measure;
A97 weighted cut-swap displayed table;
```

the five A93 hardening obligations are now addressed at the architectural level.

Remaining before final extraction:

```text
1. span convention audit across recurrence sources;
2. line-by-line sign audit in A60/A65--A71/A81;
3. final proof extraction into compact lemmas F1--F13;
4. optional finite verification ledger/certificates.
```

---

## 11. Target A99

A99 should perform the recurrence span-convention audit.

Required output:

```text
1. define final span convention once;
2. check H1/H2 recurrence source spans;
3. check pair-swap recurrence source spans;
4. check singleton-prefix source spans;
5. check cyclic-cut source spans;
6. confirm adjacent atom corrections are included consistently;
7. identify any recurrence lemma needing rewritten inequalities.
```

---

## Current status after A98

Proved/recorded here:

```text
1. bridge/gap measure M_BG;
2. proper-overlap span descent;
3. proper-containment support/span descent;
4. equal-span separated bridge gap-after descent;
5. gap-preserving recurrence gap decrease unless full endpoint alignment;
6. rigid separated returns route to midpoint/cyclic/direct-exchange recurrence;
7. no bridge/gap branch cycles indefinitely with fixed M_BG.
```

Still open:

```text
1. recurrence span convention audit;
2. detailed sign/endpoint audit;
3. final extraction;
4. optional finite verification/certification cleanup.
```
