# Analytic external-collision hardening A95

This note continues from A94.

A93 isolated five remaining hardening obligations:

```text
U1. Strict progress lemma.
U2. Universal external-collision classification.
U3. Recurrence bounded-blocker measure.
U4. Cut-swap displayed collision table.
U5. Bridge/gap measure inequalities.
```

A94 addressed U1.  A95 addresses U2 by hardening the A62 external-collision theorem.

The goal is to make precise why a collision between a transformed local window and an endpoint outside that window always pulls back to one of the named obstruction classes:

```text
zero-composite,
equal/signed interval,
transported-prefix,
pair-difference,
forbidden recurrence,
bridge/separated-equal branch,
weighted core.
```

---

## 1. Local move setup

Let the original ordering be decomposed as

```text
R = X W Y
```

where:

```text
X = left external context,
W = active local window,
Y = right external context.
```

A local move replaces `W` by another ordering `W'` using the same atoms:

```text
R' = X W' Y.
```

The total window sum is preserved:

```text
sum(W') = sum(W) = w.
```

Let

```text
x=sum(X).
```

The left boundary endpoint of the window is `x`, and the right boundary endpoint is `x+w` in both orderings.

---

## 2. Internal versus external endpoints

An endpoint of `R'` is called internal to the move if it lies strictly inside the displayed transformed window `W'`.

It is external if it lies in:

```text
1. the left context X;
2. the right context Y;
3. a wrapped/cyclic copy of X or Y after a cyclic cut;
4. an unchanged displayed family outside W'.
```

A displayed collision table usually handles collisions among endpoints inside `W'`.  A62/A95 handles collisions between an internal moved endpoint and an external endpoint.

---

## 3. General internal endpoint form

Every internal moved endpoint has the form

```text
x + u
```

where `u` is the sum of a nonempty proper prefix of `W'`.

The external endpoint has one of two non-cyclic linear forms:

```text
left external:  x - L,
right external: x + w + R,
```

where:

```text
L = sum of a nonempty suffix of X ending at the window basepoint;
R = sum of a nonempty prefix of Y starting at the window endpoint.
```

The collision equation is:

```text
x+u = x-L
```

or

```text
x+u = x+w+R.
```

Thus:

```text
left external:  L+u=0;
right external: u-w-R=0.
```

Equivalently:

```text
right external: R+(w-u)=0.
```

where `w-u` is the complementary suffix of the transformed window.

---

## Lemma A95.1: left external collision pulls back to bridge zero-composite

If an internal moved endpoint `x+u` collides with a left external endpoint `x-L`, then

```text
L+u=0.
```

This is a zero-composite with one external bridge piece `L` and one internal moved-prefix piece `u`.

### Proof

Subtract `x` from the collision equation:

```text
u=-L.
```

Therefore `L+u=0`. ∎

### Classification

If `L` and the internal piece overlap after pullback, this is an equal/signed interval or proper-overlap bridge branch.  If they are disjoint, it is a separated bridge zero-composite.  Both are covered by A74--A77.

---

## Lemma A95.2: right external collision pulls back to bridge zero-composite

If an internal moved endpoint `x+u` collides with a right external endpoint `x+w+R`, then

```text
R+(w-u)=0.
```

Here `w-u` is the complementary suffix of the transformed window after the internal endpoint.

### Proof

The collision equation gives:

```text
u=w+R.
```

Hence:

```text
w-u+R=0.
```

∎

### Classification

This is again an external bridge zero-composite, routed by A74--A77 after pullback through the local move.

---

## 4. Signed local endpoint forms

Some local moves use signed or corrected internal endpoint expressions, for example:

```text
u = P+q,
u = P+q+U,
u = R-P+q-q1,
u = V+u_j-v_1.
```

These arise from atom insertion, pair-difference, singleton, or weighted normalizations.

An external collision then has form:

```text
L+u=0
```

or

```text
R+(w-u)=0.
```

where `u` itself may contain an atom correction or pair-difference correction.

---

## Lemma A95.3: signed external collisions route to signed bridge composites

If `u` contains a bounded atom correction `E`, then a left or right external collision becomes one of:

```text
L+U+E=0,
R+V+E=0,
L-U+E=0,
R-V+E=0.
```

This is a signed bridge composite.  It routes to:

```text
pair-difference,
transported-prefix,
signed interval,
equal interval,
zero-composite,
weighted-core normal form.
```

### Proof

Move all terms to one side.  The external bridge is contiguous outside the window; the internal contribution is a prefix/suffix of the moved window; the correction `E` is supported on one or two boundary atoms.  A56 and A74 classify such signed bridge relations. ∎

---

## 5. Collisions with unchanged displayed families

An endpoint outside the moved subwindow but inside a larger displayed formula may be unchanged by the local move.

Suppose the unchanged endpoint has value

```text
x+d
```

where `d` is a displayed prefix sum not affected by the move.  Collision with internal endpoint `x+u` gives

```text
u=d.
```

Then:

```text
u-d=0.
```

This is an equal-interval, pair-difference, or zero-composite depending on how `u` and `d` overlap.

---

## Lemma A95.4: collision with unchanged displayed family is an interval obstruction

If an internal moved endpoint collides with an unchanged displayed endpoint in the same local window or adjacent displayed family, then the pullback is one of:

```text
proper-overlap equal interval,
separated equal interval,
two-piece zero-composite,
pair-difference boundary,
transported-prefix relation.
```

### Proof

The collision is equality of two displayed interval sums based at the same external basepoint.  Subtracting the two interval expressions gives zero on the symmetric difference.  If the intervals overlap, uncrossing gives proper-overlap equal/zero branches.  If separated, it is separated-equal.  If they differ by boundary atoms, it is pair-difference or transported-prefix. ∎

---

## 6. Cyclic or wrapped external collisions

A cyclic cut changes the basepoint.  Let the original total sum be `sigma`.  After cutting at endpoint `S_c`, transformed endpoints have forms:

```text
S_i-S_c              for suffix endpoints,
sigma-S_c+S_i        for wrapped prefix endpoints.
```

An internal moved endpoint colliding with a wrapped external endpoint gives:

```text
u = sigma-S_c+S_i
```

relative to the new basepoint.

Moving terms gives an endpoint-pair equation:

```text
S_i-S_c = u-sigma
```

or one of the A71 cyclic forms:

```text
S_i-S_c=f,
S_i-S_c=f-sigma,
```

with `f` replaced by the moved endpoint value if this is a collision rather than recurrence.

---

## Lemma A95.5: wrapped external collision routes to cyclic-cut or bridge composite

A wrapped external collision after a cyclic cut pulls back to one of:

```text
cyclic endpoint-pair equation,
wrapping bridge zero-composite,
midpoint boundary,
separated equal interval,
external signed bridge composite.
```

### Proof

Use the cyclic partial-sum formula.  A collision equality between a suffix endpoint and a wrapped endpoint is an endpoint-pair difference equation.  If the corresponding interval does not wrap in the original order, it is an ordinary interval obstruction.  If it wraps, it splits into a suffix bridge plus prefix bridge, which is a wrapping bridge composite.  Special symmetric endpoint equations are midpoint boundary cases as in A71. ∎

---

## 7. External forbidden recurrence

Sometimes an ordering-changing move is Graham-valid but hits the forbidden value at an external endpoint that was not displayed in the local table.

If the endpoint was unchanged from the old ordering, this contradicts minimality or means the hit was already present.

If the endpoint moved only by a cyclic/basepoint translation or bridge transfer, it is a cyclic or singleton recurrence branch.

---

## Lemma A95.6: external forbidden hits route to recurrence or minimality contradiction

If a transformed ordering hits `f` at an external endpoint, then one of the following holds:

```text
1. the endpoint was unchanged and already hit f, contradicting first-hit/minimality assumptions;
2. the endpoint is translated by a cyclic cut, giving cyclic recurrence A71;
3. the endpoint is shifted by a moved prefix/singleton, giving singleton-prefix recurrence A70;
4. the endpoint lies across an external bridge, giving A5 recurrence plus external collision pullback.
```

### Proof

Classify how the endpoint value changed.  If it did not change, the hit preexisted.  If it changed by cyclic basepoint translation, use A71.  If it changed by insertion/swap of a moved prefix, use A70/A69.  If it is produced by a bridge interaction, apply A5 at the hit and pull back the blocker as in A64/A95. ∎

---

## 8. Measure effect

External collisions may enlarge the enclosing span because they include bridge material outside the original window.  Therefore A95 should not claim immediate span descent in all cases.

Instead, the measure effect is:

```text
1. if overlap/containment occurs, A74 gives span/support descent;
2. if separated equal-span bridge occurs, A75--A77 route gap-preserving ties;
3. if signed correction occurs, A56/A74 normalize it;
4. if cyclic wrapping occurs, A71 routes it;
5. if recurrence occurs, A64--A71 route it.
```

---

## Proposition A95.7: external collisions are nonterminal routing edges with controlled exits

Every external collision from a local transformed move pulls back to one of:

```text
1. bridge zero-composite;
2. signed bridge composite;
3. equal/separated interval;
4. transported-prefix relation;
5. pair-difference boundary;
6. cyclic-cut branch;
7. singleton/prefix recurrence;
8. weighted-core normal form;
9. collapse/minimality contradiction.
```

No external collision creates a new obstruction species outside the A72/A92 state machine.

### Proof

Left and right linear external collisions are Lemmas A95.1--A95.2.  Signed corrections are Lemma A95.3.  Unchanged displayed-family collisions are Lemma A95.4.  Wrapped collisions are Lemma A95.5.  External forbidden hits are Lemma A95.6.  These cases exhaust external endpoints. ∎

---

## 9. Hardened A62 theorem

## Theorem A95.8: universal external-collision classification

Let a local move replace `W` by `W'` inside `X W Y`, preserving the window atom multiset and total sum.  If a transformed internal endpoint of `W'` collides with any endpoint external to the displayed collision table, then the collision pullback is one of the named obstruction classes in the A72/A92 state machine and is routed by A74--A78, A56, A64--A71, or weighted induction.

### Proof

By the definition of external endpoint, the colliding endpoint is left external, right external, unchanged displayed-family external, cyclic/wrapped external, or an external forbidden-recurrence endpoint.  Lemmas A95.1--A95.6 classify these cases.  Proposition A95.7 maps each class into the state-machine outputs. ∎

---

## 10. What remains after A95

A95 hardens U2 at the classification level.  It still delegates measure descent for bridge/gap cases to A74--A77 and recurrence cases to A64--A71.

Remaining hardening items:

```text
U3. A64 recurrence bounded-blocker measure.
U4. A60 cut-swap displayed collision table.
U5. A74--A77 bridge/gap measure inequalities.
```

---

## 11. Target A96

A96 should harden A64:

```text
recurrence bounded-blocker measure.
```

Required output:

```text
1. define blocker span exactly;
2. prove nearest blocker exists from A5;
3. prove bounded blocker gives strict decrease in final measure;
4. classify long blocker as the only remaining recurrence branch;
5. connect long blockers to A65--A71.
```

---

## Current status after A95

Proved/recorded here:

```text
1. formal external collision definitions;
2. left/right external collision formulas;
3. signed correction external collisions;
4. unchanged displayed-family collision classification;
5. cyclic/wrapped external collision classification;
6. external forbidden-hit routing;
7. universal external collisions create no new state-machine species.
```

Still open:

```text
1. A64 bounded-blocker measure hardening;
2. A60 cut-swap displayed collision table hardening;
3. A74--A77 bridge/gap inequality hardening;
4. final extraction.
```
