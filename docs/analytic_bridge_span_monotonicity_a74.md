# Analytic bridge-span monotonicity A74

This note continues from A73.

A73 reduced non-weighted global acyclicity to a bridge-span monotonicity lemma.  Bridge branches appear whenever a local move creates an obstruction whose pullback crosses the boundary of the local source support.  Typical forms are:

```text
L + U = 0,
L - U + atom corrections = 0,
R + U = 0,
R - U + atom corrections = 0,
```

where `L` or `R` is an external bridge interval and `U` is an internal piece of the source obstruction.

This note proves monotonicity for the proper-overlap and proper-containment bridge cases, and isolates the remaining tie: separated equal-span bridge return.  Thus A74 is partial but sharpens the BML gap.

No complete proof is claimed here.

---

## 1. Standing bridge setup

Let the original ordering contain a local source support interval

```text
S = [s_0,s_1]
```

with span

```text
|S| = s_1-s_0.
```

A bridge obstruction produced by pulling back a transformed blocker has one of the forms:

```text
B_left + U = 0,
B_right + U = 0,
B_left - U + E = 0,
B_right - U + E = 0,
```

where:

- `B_left` is an external bridge ending at or before the left boundary of `S`;
- `B_right` is an external bridge starting at or after the right boundary of `S`;
- `U` is an internal subblock or boundary piece of `S`;
- `E` is a finite atom/pair correction from a swap or insertion, usually support size 1 or 2.

The bridge span is the enclosing span of the bridge obstruction:

```text
span(B,U,E)=length(enclosure(B union U union E)).
```

---

## 2. Bridge relation as interval geometry

## Lemma A74.1: every bridge relation is an equal/signed interval relation after moving atom corrections into the internal side

A bridge equation of the form

```text
B - U + E = 0
```

can be rewritten as

```text
sum(B)=sum(U)-sum(E).
```

If `E` is empty, this is an equal-interval relation.  If `E` is nonempty, it is a signed/equal interval relation with a bounded atom correction.  In either case it belongs to the A20--A27 signed-interval framework plus the A56 transported-prefix tests.

### Proof

Rearrange the equation.  The only non-interval term is the bounded correction `E`, which is exactly the pair-difference/singleton correction already isolated in A65--A70. ∎

---

## 3. Proper-overlap bridge descent

A bridge may overlap the source support interval `S`, or it may be separated from it.

The easiest monotonicity case is proper overlap.

## Lemma A74.2: proper-overlap bridge relations give strict span descent

Suppose a bridge interval `B` and an internal interval `U \subseteq S` overlap properly: neither contains the other, and their intersection is nonempty and not equal to either interval.

If

```text
sum(B)=sum(U)
```

or the signed-correction form reduces to equality after transporting bounded atom corrections, then the proper-overlap uncrossing from A26/A27 produces a smaller interval/composite obstruction with span strictly less than

```text
max(span(B), span(U)).
```

### Proof sketch

For equal intervals `B` and `U`, decompose the overlap:

```text
B = B_0 O,
U = O U_1
```

or the opposite orientation.  Equality of sums gives

```text
sum(B_0)=sum(U_1)
```

or a zero-composite involving the non-overlapping tails.  The enclosing span of `B_0` and `U_1` is strictly smaller than the original overlapping pair because the common overlap `O` has been removed.  Signed-correction cases first apply the transported-prefix/pair-difference normalization, then the same uncrossing applies. ∎

### Status

Proper-overlap bridge branches descend.

---

## 4. Proper containment bridge descent

Now suppose one interval contains the other.

## Lemma A74.3: proper containment gives zero-composite descent

If an external bridge interval `B` properly contains an internal interval `U`, and

```text
sum(B)=sum(U),
```

then the complement

```text
B \ U
```

is a nonempty zero interval or a two-piece zero composite, depending on whether `U` lies internally or at an endpoint of `B`.

Its span is strictly smaller than `span(B)`.

### Proof

Write

```text
B = B_L U B_R
```

with at least one of `B_L`, `B_R` nonempty.  Equality `sum(B)=sum(U)` gives

```text
sum(B_L)+sum(B_R)=0.
```

If one side is empty, the other is a nonempty zero interval.  If both sides are nonempty, this is a two-piece zero composite.  The enclosing span excludes the contained interval `U`, hence is strictly smaller than `span(B)` unless the two outside pieces lie on both sides of `U`; in that case the active support size strictly decreases because `U` has been removed from the obstruction. ∎

---

## Lemma A74.4: internal interval containing bridge gives immediate smaller obstruction

If the internal interval `U \subseteq S` properly contains the bridge interval `B`, and

```text
sum(B)=sum(U),
```

then

```text
sum(U \ B)=0
```

as a zero interval or two-piece zero composite, with active support strictly smaller than `U` and hence smaller than the source support span.

### Proof

Same containment subtraction as Lemma A74.3. ∎

---

## 5. Separated bridge equality

The hard case is when the bridge and the internal piece are disjoint and separated:

```text
B  ...  U
```

or

```text
U  ...  B.
```

Then a relation

```text
sum(B)=sum(U)
```

is exactly a separated equal-interval branch.

## Lemma A74.5: separated bridge equality routes to separated-equal machinery

If a bridge interval `B` is disjoint from the internal interval `U` and

```text
sum(B)=sum(U),
```

then the branch is a separated equal interval.  It routes to A36--A54.

### Proof

This is the definition of separated equal intervals: two disjoint intervals with equal sum and a nonempty gap between them. ∎

### Status

This is locally routed modulo A34, but not an immediate bridge-span decrease.

---

## 6. Signed bridge relations with atom correction

Many bridge equations from A65--A70 have bounded corrections, for example:

```text
R + Q^+ + q = 0,
R + V + u_j - v_1 = 0,
L + q + v_1 - V = 0.
```

These are not pure equal-interval relations, but the correction is small and lies adjacent to the source support.

## Lemma A74.6: signed bridge relations either normalize to pair-difference or to separated equal intervals

Let

```text
B - U + E = 0
```

where `E` is supported on one or two boundary atoms adjacent to `U`.  Then one of the following holds:

```text
1. E combines with a boundary atom of U to form a pair-difference branch;
2. E combines with a prefix/tail of U to form a transported-prefix artifact;
3. the relation is a signed interval branch in the A20--A27 framework;
4. after normalization, it becomes a separated equal interval or zero-composite branch.
```

### Proof sketch

If `E` shares a boundary atom with `U`, absorb it into the adjacent prefix/tail and apply A56 transported-prefix tests.  If `E` is a difference of two atoms, isolate it as a pair-difference correction.  Otherwise regard the equation as a signed interval relation.  A20--A27 route signed interval relations to equal interval, weighted core, transported-prefix, or zero-composite normal forms. ∎

### Status

Signed bridge cases are not new, but they can enter the weighted-core branch if normalization fails.

---

## 7. Monotonicity theorem for non-separated bridge cases

## Proposition A74.7: non-separated bridge branches descend or normalize

If a bridge branch is not a separated bridge equality, then it either:

```text
1. gives strict span descent by proper-overlap uncrossing;
2. gives strict support descent by proper containment;
3. collapses to zero-prefix/interior-zero;
4. normalizes to pair-difference, transported-prefix, or zero-composite machinery with no larger active span.
```

### Proof

Proper-overlap cases are Lemma A74.2.  Proper-containment cases are Lemmas A74.3--A74.4.  Signed corrections are Lemma A74.6.  Zero endpoint cases collapse. ∎

---

## 8. Remaining equal-span separated bridge tie

The only bridge case not handled by strict local monotonicity is:

```text
B and U are disjoint separated intervals,
sum(B)=sum(U),
span(B,U) is not smaller than the source obstruction span.
```

This is not a new class.  It is exactly the separated-equal branch already routed in A36--A54.  However, it can preserve or increase the enclosing span because the bridge may extend outside the original source support.

## Definition A74.8: equal-span separated bridge return

An equal-span separated bridge return is a bridge relation

```text
sum(B)=sum(U)
```

where:

```text
B is external to the source support,
U is internal or boundary-adjacent,
B and U are disjoint,
span(enclosure(B,U)) >= span(source obstruction).
```

This is the remaining BML tie case.

---

## Lemma A74.9: equal-span separated bridge return carries a larger gap parameter

In an equal-span separated bridge return, the gap between `B` and `U` is nonempty.  If the enclosing span does not decrease, then the gap length is at least the amount by which the bridge extends beyond the source support.

### Proof

The enclosure consists of

```text
span(B)+gap(B,U)+span(U).
```

If `B` lies outside the source support and the total enclosure does not shrink, the non-overlap gap accounts for the missing overlap that would otherwise have produced descent. ∎

### Interpretation

The tie is not arbitrary: it converts bridge-span difficulty into a separated-equal gap difficulty.

This suggests adding a `gap` coordinate to the global measure for separated bridge returns.

---

## 9. Refined measure for bridge returns

A73 used

```text
M_NW=(span,support_size,recurrence_depth,pair_depth,separated_depth,type_rank,boundary_rank,h_excess).
```

A74 suggests refining it for bridge returns:

```text
M_bridge=(
  enclosing_span,
  bridge_gap,
  bridge_length,
  internal_length,
  support_size,
  type_rank,
  boundary_rank,
  h_excess
).
```

For most bridge cases, `enclosing_span` decreases.  In equal-span separated returns, the next target is to prove that `bridge_gap` decreases under separated-equal routing, or that the branch routes to D2/zero-composite with smaller support.

---

## 10. Partial bridge-span monotonicity theorem

## Theorem A74.10: bridge-span monotonicity holds except for equal-span separated bridge returns

Every bridge branch produced by the routed recurrence/collision machinery either:

```text
1. strictly decreases active span;
2. strictly decreases active support size;
3. collapses;
4. normalizes to pair-difference/transported-prefix/zero-composite machinery with no larger span;
5. routes to weighted-core normal form;
6. is an equal-span separated bridge return.
```

### Proof

Combine Propositions A74.7 and Lemma A74.5.  The only case excluded from strict descent/normalization is the separated disjoint equal-interval case with non-decreasing enclosure span, which is exactly Definition A74.8. ∎

---

## 11. Consequence for A73

A73 required a bridge-span monotonicity lemma BML.  A74 proves a partial version:

```text
BML holds except for equal-span separated bridge returns.
```

Thus non-weighted global acyclicity is reduced further to:

```text
1. equal-span separated bridge return termination;
2. weighted-core cut-selection;
3. final finite verification bridge.
```

The first item is now very specific and belongs to separated-equal/gap analysis, not generic bridge theory.

---

## 12. Target A75

A75 should attack equal-span separated bridge returns.

Setup:

```text
B G U,
sum(B)=sum(U),
B external bridge,
U internal source piece,
G nonempty gap,
span(B G U) >= source span.
```

Use the separated-equal machinery A36--A54.  The likely result is:

```text
separated-equal direct/gap-after surgery either decreases gap length,
routes to D2 zero-composite with smaller support,
or produces A34 recurrence already handled by A64--A71.
```

The key new measure coordinate should be:

```text
gap_length = |G|.
```

---

## Current status

Proved here:

1. bridge relations are equal/signed interval geometry;
2. proper-overlap bridge cases descend;
3. proper-containment bridge cases descend or collapse;
4. signed bridge relations normalize to known branches;
5. only equal-span separated bridge return remains as bridge monotonicity tie.

Not proved here:

1. equal-span separated bridge return termination;
2. weighted cut-selection;
3. final endpoint avoidance theorem.
