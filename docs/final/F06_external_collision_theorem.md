# F6 external collision theorem

This file continues the final-proof extraction phase.

F6 extracts the universal external-collision theorem from the A-notes, primarily:

```text
A62  external collision routing concept
A74--A77 bridge/gap routing dependencies
A95  external collision hardening
A98  bridge/gap measure hardening
```

F6 is used by:

```text
F7  recurrence routing theorem
F8  bridge/gap descent theorem
F10 weighted normal form and cut-swap theorem
F11 weighted cut-selection theorem
```

This is an extracted draft, not yet the final manuscript version.

---

## F6.1. Local move setup

Let the current ordering be decomposed as

```text
R = X W Y
```

where:

```text
X = left external context,
W = active local window,
Y = right external context.
```

A local move replaces `W` by another ordering `W'` of the same atoms:

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

Then the left boundary endpoint of the window is `x`, and the right boundary endpoint is `x+w` in both `R` and `R'`.

An internal moved endpoint of the transformed window has form

```text
x+u
```

where `u` is the sum of a nonempty proper prefix of `W'`, possibly with a bounded atom/pair correction in signed-normalized branches.

---

## F6.2. External endpoint types

An endpoint is external to the displayed collision table if it lies in one of:

```text
1. the left context X;
2. the right context Y;
3. an unchanged displayed endpoint family outside the actively moved family;
4. a cyclic/wrapped context after a cyclic cut;
5. an external endpoint at which a forbidden recurrence occurs.
```

Displayed collision tables handle collisions internal to `W'`.  F6 handles all other collisions involving at least one moved endpoint.

---

## F6.3. Left external collision

A left external endpoint has form

```text
x-L
```

where `L` is the sum of a nonempty suffix of `X` ending at the window basepoint.

If

```text
x+u = x-L,
```

then

```text
L+u=0.
```

## Lemma F6.1: left external collision is a bridge zero-composite

A collision between an internal moved endpoint and a left external endpoint pulls back to

```text
L+u=0.
```

This is a bridge zero-composite or signed bridge composite.

### Proof

Subtract `x` from the collision equation.  The external suffix `L` and the internal moved-prefix contribution `u` have zero total.  If `u` includes a bounded correction, the same equation is a signed bridge composite. ∎

---

## F6.4. Right external collision

A right external endpoint has form

```text
x+w+R
```

where `R` is the sum of a nonempty prefix of `Y` starting after the window.

If

```text
x+u = x+w+R,
```

then

```text
R+(w-u)=0.
```

Here `w-u` is the complementary suffix of the transformed window after the internal endpoint.

## Lemma F6.2: right external collision is a bridge zero-composite

A collision between an internal moved endpoint and a right external endpoint pulls back to

```text
R+(w-u)=0.
```

This is a bridge zero-composite or signed bridge composite.

### Proof

Subtract `x` and rearrange:

```text
u=w+R,
```

so

```text
w-u+R=0.
```

∎

---

## F6.5. Signed correction case

Some internal moved endpoints have signed or corrected forms, e.g.

```text
u=U+E
```

where `E` is a bounded correction supported on one or two boundary atoms.

Then left and right external collisions become equations of the form:

```text
L+U+E=0,
R+V+E=0,
L-U+E=0,
R-V+E=0.
```

## Lemma F6.3: signed external collisions route to signed bridge composites

External collisions involving bounded atom/pair corrections route to:

```text
pair-difference,
transported-prefix,
signed interval,
equal interval,
zero-composite,
weighted-core normal form.
```

### Proof

Move all terms to one side.  The external contribution is a contiguous suffix or prefix outside the active window.  The internal contribution is a moved prefix/suffix of the transformed window.  The correction is supported on boundary atoms.  This is exactly a signed bridge composite.  The normal-form classification is the weighted/signed-interval analysis used in F4, F8, and F10. ∎

---

## F6.6. Collision with unchanged displayed family

Suppose the moved endpoint `x+u` collides with an unchanged displayed endpoint `x+d` from the same larger displayed region.

Then

```text
u=d.
```

Equivalently,

```text
u-d=0.
```

## Lemma F6.4: collision with unchanged displayed endpoint is an interval obstruction

A collision between a moved endpoint and an unchanged displayed endpoint pulls back to one of:

```text
proper-overlap equal interval,
separated equal interval,
two-piece zero-composite,
pair-difference boundary,
transported-prefix relation.
```

### Proof

Both endpoints are represented by displayed interval sums based at the same basepoint.  Equality of endpoint values gives equality of two interval sums.  If the represented intervals overlap, uncrossing yields a zero interval or a smaller equal interval.  If they are disjoint, the result is a separated-equal relation.  If they differ only by boundary atoms or a repeated transported prefix, the branch is pair-difference or transported-prefix. ∎

---

## F6.7. Cyclic or wrapped external collision

A cyclic cut changes endpoint coordinates by subtracting the cut endpoint.  If the total sum is `sigma` and the cut is at `S_c`, endpoints after the cut have forms:

```text
S_i-S_c
```

for suffix endpoints and

```text
sigma-S_c+S_i
```

for wrapped prefix endpoints.

## Lemma F6.5: wrapped external collisions route to cyclic or bridge branches

A collision between an internal moved endpoint and a cyclic/wrapped external endpoint pulls back to one of:

```text
cyclic endpoint-pair equation,
wrapping bridge zero-composite,
midpoint boundary,
separated equal interval,
external signed bridge composite.
```

### Proof

Use the cyclic partial-sum formula.  A collision between a suffix endpoint and a wrapped endpoint gives an endpoint-pair difference equation.  If the corresponding interval is non-wrapping in the original order, it is an ordinary equal/zero interval.  If it wraps, it splits into a suffix bridge plus prefix bridge.  Symmetric endpoint equations are midpoint cases. ∎

---

## F6.8. External forbidden recurrence

A transformed ordering may be Graham-valid but hit `f` at an endpoint not listed in the displayed local table.

## Lemma F6.6: external forbidden hits route to recurrence or minimality contradiction

If a transformed ordering hits `f` at an external endpoint, then one of the following holds:

```text
1. the endpoint was unchanged and already hit f, contradicting first-hit/minimality assumptions;
2. the endpoint changed by cyclic translation, giving cyclic recurrence;
3. the endpoint changed by a moved prefix/singleton, giving singleton-prefix or pair-swap recurrence;
4. the endpoint lies across an external bridge, giving A5 recurrence plus external collision pullback.
```

### Proof

Classify how the endpoint value changed.  If it did not change, the hit preexisted.  If it changed by cyclic basepoint translation, use the cyclic recurrence theorem.  If it changed by a moved prefix or singleton, use the recurrence routing theorem.  If it arises through bridge interaction, apply the adjacent-blocker lemma at the new forbidden hit and pull back the blocker as a bridge/external collision. ∎

---

## F6.9. External collision theorem

## Theorem F6.7: universal external-collision theorem

Let a local move replace `W` by `W'` inside `X W Y`, preserving the atom multiset and total sum of the window.  If a transformed moved endpoint collides with any endpoint outside the displayed local collision table, then the collision pulls back to one of:

```text
1. bridge zero-composite;
2. signed bridge composite;
3. equal/separated interval;
4. transported-prefix relation;
5. pair-difference boundary;
6. cyclic-cut branch;
7. singleton/prefix recurrence;
8. weighted-core normal form;
9. collapse or minimality contradiction.
```

No new obstruction class appears.

### Proof

By F6.2, external endpoints are left external, right external, unchanged displayed-family endpoints, cyclic/wrapped endpoints, or external forbidden-recurrence endpoints.

Left and right external collisions are Lemmas F6.1 and F6.2.  Signed-correction cases are Lemma F6.3.  Unchanged displayed-family collisions are Lemma F6.4.  Cyclic/wrapped collisions are Lemma F6.5.  External forbidden hits are Lemma F6.6.  These cases exhaust all endpoints external to the displayed collision table. ∎

---

## F6.10. Measure effect and exits

External collisions may enlarge the immediate enclosure because they include bridge material outside the local window.  F6 therefore does not claim immediate span descent in every case.

Instead:

```text
bridge zero/signed composites       -> F8 bridge/gap descent theorem;
equal/separated interval            -> F4/F5 local descent;
transported-prefix                  -> F10/F4 normal-form rewrite;
pair-difference                     -> F4/F7 routing;
cyclic-cut branch                    -> F7 recurrence routing;
singleton/prefix recurrence          -> F7 recurrence routing;
weighted-core normal form            -> F10/F11 weighted branch;
collapse/minimality contradiction    -> terminal contradiction.
```

Thus F6 is a routing theorem, not a direct termination theorem.

---

## F6.11. Remaining extraction risks

Before final manuscript status:

```text
R1. Define “displayed collision table” uniformly in F3.
R2. Ensure signed correction terms are always bounded by one or two atoms.
R3. Ensure wrapped/cyclic endpoint formulas use the same convention as F7.
R4. Tie every F6 exit explicitly to F4, F5, F7, F8, F10, or F11.
R5. Check empty-context cases X=empty or Y=empty.
```

---

## F6.12. Extraction status

```text
Status: extracted draft.
Risk: YELLOW.
Next recommended extraction: F7 recurrence routing theorem.
```
