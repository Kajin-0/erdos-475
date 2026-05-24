# F4 zero-composite, equal-interval, and pair-difference local descent theorem

This file continues the final-proof extraction phase.

F4 extracts the basic non-weighted local descent machinery used by F5--F9, mainly from:

```text
A20--A35  interval and zero-composite setup
A56       transported-prefix normalization hooks
A69       pair-difference recurrence hooks
A73/A78   non-weighted measure framework
A95/A98   external and bridge exits into local descent
```

F4 is the local algebraic sink for many later branches:

```text
zero-composite,
two-piece zero,
three-piece zero,
equal interval,
signed interval,
pair-difference boundary,
transported-prefix relation.
```

This is an extracted draft, not the final manuscript version.  The remaining risks are sign conventions, endpoint cases, and exact support/span inequalities.

---

## F4.1. Local interval notation

Let an ordering contain a displayed local window.  For an interval block `I`, write

```text
sum(I)
```

for the sum of its atoms.

An interval is nonempty unless explicitly stated otherwise.

For two displayed intervals `I,J`, their relative geometry is one of:

```text
disjoint,
proper-overlap,
one contains the other,
equal.
```

The enclosing span of an obstruction is the length of the smallest atom interval containing every participating atom.

---

## F4.2. Zero interval and zero-composite branches

A zero interval is a nonempty interval `Z` with

```text
sum(Z)=0.
```

A zero-composite is a relation

```text
sum(Z_1)+...+sum(Z_m)=0
```

where the participating pieces are displayed intervals or bounded atom corrections.

The most common cases are:

```text
two-piece zero:    U+V=0,
three-piece zero:  U+V+W=0.
```

---

## Lemma F4.1: zero interval is terminal contradiction

A nonempty zero interval in a claimed Graham-valid ordering is a contradiction.

### Proof

If `Z` is the interval between endpoints `S_i` and `S_j`, then

```text
S_j-S_i=sum(Z)=0.
```

Thus `S_i=S_j`, contradicting pairwise distinct partial sums. ∎

---

## Lemma F4.2: two-piece zero routes to local descent or collapse

If

```text
U+V=0
```

with nonempty displayed pieces `U,V`, then either:

```text
1. U and V combine to a nonempty zero interval, giving contradiction;
2. U and V are disjoint, giving a two-piece zero-composite branch with active support `U union V`;
3. U and V overlap/contain, and uncrossing gives a smaller zero/equal interval obstruction.
```

### Proof

If the pieces are adjacent and cover one interval, their union is zero.  If they are disjoint, the relation is a two-piece zero-composite.  If they overlap or one contains the other, cancel the common overlap or subtract the contained interval.  The resulting relation uses strictly smaller support or span. ∎

---

## Lemma F4.3: higher zero-composites reduce by uncrossing or enter bridge/gap routing

A zero-composite with three or more pieces either:

```text
1. contains a proper overlap/containment pair and reduces support/span by uncrossing;
2. contains adjacent pieces whose union gives a smaller zero-composite;
3. is separated into bridge/gap form and routes to F8;
4. contains a bounded atom correction and routes to pair-difference or signed interval machinery.
```

### Proof

Choose two pieces with minimal enclosing span.  If they overlap or contain each other, uncross.  If adjacent, merge them.  If every participating piece is separated from the others, the relation has bridge/gap form.  Bounded atom corrections are exactly pair-difference or signed-interval corrections. ∎

### Audit flag

The final manuscript should not rely on this as a black box unless the zero-composite table is included in an appendix.

---

## F4.3. Equal and signed interval branches

An equal-interval relation has form

```text
sum(U)=sum(V).
```

Equivalently:

```text
sum(U)-sum(V)=0.
```

A signed interval relation allows one or two bounded atom/pair corrections:

```text
sum(U)-sum(V)+E=0.
```

---

## Lemma F4.4: proper-overlap equal intervals descend

If two equal-sum intervals `U,V` properly overlap, then uncrossing gives an equal-interval or zero-composite obstruction with strictly smaller enclosing span.

### Proof

Write one orientation as

```text
U=U_0 O,
V=O V_1,
```

with nonempty overlap `O`.  Equality gives

```text
sum(U_0)=sum(V_1).
```

The overlap is removed, so the new enclosure is strictly smaller. ∎

---

## Lemma F4.5: proper-containment equal intervals descend

If one equal-sum interval properly contains another, then the complement has zero total and gives a zero interval or zero-composite of strictly smaller support.

### Proof

If

```text
U=L V R
```

and `sum(U)=sum(V)`, then

```text
sum(L)+sum(R)=0.
```

At least one of `L,R` is nonempty.  This is a zero interval if one side is empty and a two-piece zero-composite otherwise.  The contained interval `V` is removed from the active relation, so support decreases. ∎

---

## Lemma F4.6: disjoint equal intervals route to separated-equal machinery

If equal intervals are disjoint and neither endpoint degenerates, then the relation is a separated-equal branch routed by F5.

### Proof

Disjoint equal intervals have form

```text
U G V
```

or the reverse, with gap `G` possibly empty.  If the gap is empty, it is adjacent-equal/midpoint machinery.  If the gap is nonempty, it is separated-equal.  Both are handled by F5. ∎

---

## F4.4. Pair-difference boundary branches

A pair-difference obstruction has form

```text
alpha-beta+P=0
```

or

```text
P+alpha-beta=0,
```

where `alpha,beta` are boundary atoms and `P` is a displayed prefix/tail interval.

Pair-difference branches appear from adjacent swaps, right-blocker recurrence equations, signed external collisions, and atom-middle endpoint traps.

---

## Lemma F4.7: pair-difference with empty interval is atom equality/collapse

If

```text
alpha-beta=0,
```

then `alpha=beta`.  For a subset ordering of distinct atoms, this is impossible unless the two atom labels refer to the same atom, in which case the local move is degenerate and not a genuine branch.

### Proof

Immediate in the field.  Distinct subset atoms cannot have equal value. ∎

---

## Lemma F4.8: pair-difference with nonempty interval routes to signed interval or recurrence machinery

If

```text
alpha-beta+P=0
```

with `P` nonempty, then the branch is one of:

```text
1. signed interval with bounded correction;
2. two-piece zero-composite after absorbing a boundary atom;
3. pair-swap recurrence if produced by a recurrent transformed move;
4. external signed bridge if P crosses outside the local window.
```

### Proof

The correction `alpha-beta` is supported on two boundary atoms.  If both atoms are adjacent to `P`, absorbing one boundary atom gives an ordinary zero-composite or signed interval.  If the relation is produced by recurrence, it is exactly a pair-swap/pair-difference recurrence input for F7.  If `P` crosses the local window boundary, F6/F8 apply. ∎

---

## F4.5. Transported-prefix branches

A transported-prefix relation is an apparent coefficient-2 or signed relation caused by comparing the same prefix/tail after a local move.

It has schematic form

```text
A + 2P + C = 0
```

where one copy of `P` is not genuinely independent but transported from a containing interval.

---

## Lemma F4.9: transported-prefix relations normalize to non-weighted branches unless genuine weighted core remains

A transported-prefix/tail relation either:

```text
1. rewrites to an ordinary zero-composite;
2. rewrites to an equal/signed interval;
3. reduces to pair-difference boundary data;
4. or is a genuine weighted-core normal form routed by F10/F11.
```

### Proof

If the doubled piece is a transported copy of an interval already contained in a larger displayed interval, subtract the containing interval representation.  The coefficient-2 term disappears, leaving an ordinary zero/equal/signed relation.  If no such transported representation exists and all easy reductions fail, the branch is a genuine weighted core. ∎

### Audit flag

The exact transported-prefix hypotheses must be imported from F10/A56.

---

## F4.6. Local descent theorem

## Theorem F4.10: local zero/equal/pair descent theorem

Every local non-weighted obstruction of type

```text
zero interval,
two-piece zero,
higher zero-composite,
equal interval,
signed interval,
pair-difference boundary,
transported-prefix relation
```

one of:

```text
1. reaches contradiction by zero interval or atom equality;
2. strictly decreases enclosing span or support size;
3. routes to separated-equal/midpoint machinery F5;
4. routes to recurrence machinery F7;
5. routes to external/bridge machinery F6/F8;
6. routes to genuine weighted core F10/F11.
```

No local zero/equal/pair branch introduces a new obstruction species.

### Proof

Zero intervals are Lemma F4.1.  Two-piece and higher zero-composites are Lemmas F4.2--F4.3.  Equal intervals are Lemmas F4.4--F4.6.  Pair-difference branches are Lemmas F4.7--F4.8.  Transported-prefix relations are Lemma F4.9.  The listed alternatives exhaust these local obstruction types. ∎

---

## F4.7. Interface with F9

F4 supplies F9 with the basic strict-descent alternatives:

```text
proper overlap -> enclosing_span decreases;
proper containment -> support_size decreases;
zero interval -> contradiction;
transported-prefix -> lower-rank normal form or weighted core;
pair-difference -> signed interval/recurrence/external branch.
```

F4 does not prove global termination alone.  F9 assembles termination using F4--F8 and F10--F11.

---

## F4.8. Remaining extraction risks

Before final manuscript status:

```text
R1. Include explicit zero-composite uncrossing table.
R2. Include sign conventions for pair-difference branches.
R3. Clarify when transported-prefix routes to F4 versus F10.
R4. State all nonempty/empty endpoint cases.
R5. Ensure support/span decreases match M_NW^* coordinates.
```

---

## F4.9. Extraction status

```text
Status: extracted draft.
Risk: ORANGE.
Next recommended extraction: F5 separated-equal and midpoint routing.
```
