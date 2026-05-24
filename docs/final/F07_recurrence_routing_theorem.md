# F7 recurrence routing theorem

This file continues the final-proof extraction phase.

F7 extracts the recurrence-routing theorem from the A-notes, primarily:

```text
A5   adjacent blocker lemma
A64  recurrence theorem / bounded blocker framework
A65  H1 long-blocker uncrossing
A66  H1 crossing cases
A67  H2 long-blocker uncrossing
A68  recurrence status after atom insertion
A69  pair-difference recurrence
A70  singleton-prefix recurrence
A71  cyclic-cut recurrence
A95  external collision hardening
A96  recurrence bounded-blocker hardening
A99  recurrence span-convention audit
```

F7 is used by:

```text
F6  external collision theorem
F8  bridge/gap descent theorem
F9  non-weighted termination theorem
F10 weighted normal form and cut-swap theorem
F11 weighted cut-selection theorem
```

This is an extracted draft, not the final manuscript version.  The remaining risks are sign, endpoint, and long-blocker case audit.

---

## F7.1. Recurrence setup

Let a local move transform an ordering

```text
R -> R'
```

where `R'` is Graham-valid but hits the forbidden value `f`.

Let `H` be the first relevant forbidden-hit index in `R'`:

```text
S'_H=f.
```

Let the atom at the hit boundary be `y`, so

```text
S'_H=S'_{H-1}+y.
```

Let the next atom after the hit be

```text
z=r'_{H+1}.
```

Since the final endpoint is not forbidden, this next atom exists in the recurrence branch.

By the adjacent blocker lemma, there is a blocker endpoint `j` such that

```text
S'_{H-1}+z=S'_j.
```

This is the A5 blocker equation.

---

## F7.2. Augmented blocker convention

The final proof uses the augmented support convention from A99.

For a source obstruction `O`, define:

```text
Supp_src^+(O)=smallest atom interval containing the source support, moved atoms, hit atom, and A5 next atom correction.
```

For a blocker `j`, define:

```text
Supp_blk^+(j,H)=smallest atom interval containing the blocker interval, the hit-boundary atom, and the next atom z.
```

The blocker is bounded if:

```text
Supp_blk^+(j,H) subsetneq Supp_src^+(O).
```

Otherwise it is long/crossing and must be routed by the relevant long-blocker theorem.

---

## Lemma F7.1: bounded blocker gives strict measure descent

If a recurrent A5 blocker is bounded in the augmented-support sense, then the pulled-back obstruction has strictly smaller enclosing span than the source obstruction.

### Proof

The A5 blocker relation is pulled back onto support contained in `Supp_blk^+(j,H)`.  Since this support is a proper subinterval of `Supp_src^+(O)`, the enclosing span of the pulled-back obstruction is strictly smaller than the enclosing span of the source.  Enclosing span is the first coordinate of `M_NW^*`, so the measure strictly decreases. ∎

---

## F7.3. Left and right blocker equations

If `j < H`, then

```text
S'_{H-1}-S'_j+z=0.
```

Thus:

```text
sum'(j,H-1]+z=0.
```

This is a zero-composite relation.

If `j > H`, then subtracting the hit endpoint gives

```text
S'_j-S'_H=z-y.
```

Equivalently:

```text
y-z+sum'(H,j]=0.
```

This is a pair-difference or signed zero-composite relation.

---

## Lemma F7.2: A5 blocker pullbacks are zero/pair/signed obstructions

Every A5 blocker pullback is one of:

```text
zero-composite,
pair-difference boundary,
signed zero-composite,
external bridge composite,
cyclic wrapped composite.
```

The first three are internal.  The last two are routed by F6/F8 or cyclic recurrence.

### Proof

Use the left and right blocker equations above.  If the support remains inside the active local window, the equations are internal zero-composite or pair-difference relations.  If the support crosses the local window boundary, it is external and is routed by F6.  If the support wraps around a cyclic cut, it is routed by the cyclic recurrence branch. ∎

---

## F7.4. Recurrence dichotomy

## Lemma F7.3: recurrence dichotomy

Every recurrence branch is either:

```text
1. bounded, hence strictly descending by Lemma F7.1;
2. external/cyclic, hence routed by F6 or the cyclic recurrence theorem;
3. long internal, hence one of the long-blocker cases below.
```

### Proof

Choose a nearest A5 blocker, minimizing augmented blocker span.  If it is finally bounded, Lemma F7.1 applies.  If it crosses outside the local window or wraps cyclically, it is external/cyclic.  Otherwise it is long internal by definition. ∎

---

## F7.5. H1/H2 atom-insertion recurrence

Atom-insertion recurrence arises from local transformations of the form

```text
P Q q -> P q Q
```

or the opposite orientation.  These are H1 and H2 branches in A65--A67.

## Lemma F7.4: H1/H2 long blockers route to known classes

Every long-blocker recurrence arising from H1 or H2 atom insertion routes to one of:

```text
zero-composite descent,
pair-difference boundary,
equal/signed interval,
external bridge branch,
singleton-prefix recurrence,
cyclic recurrence,
collapse.
```

### Extracted proof

For H1 and H2, the A5 blocker pullback gives a zero relation using a long suffix/prefix of the insertion window plus one or two boundary atom corrections.  Non-crossing pullbacks produce zero-composite or pair-difference relations.  Crossing pullbacks produce bridge/equal/signed interval relations and are routed by F6/F8.  Endpoint pullbacks produce singleton-prefix or cyclic recurrence.  Collapse occurs when a nonempty zero interval or zero atom is forced.

This is the extracted content of A65--A67, using the augmented span convention of A99. ∎

### Audit flags

```text
The final manuscript must spell out the H1 and H2 orientations separately.
Right-blocker signs in H2 require line-by-line audit.
```

---

## F7.6. Pair-difference recurrence

Pair-difference recurrence arises when a moved pair or pair-corrected prefix creates a new forbidden hit.

## Lemma F7.5: pair-difference recurrence routes to descent or bridge/equal classes

Every pair-difference recurrence routes to one of:

```text
pair-difference prefix descent,
zero-composite descent,
equal/signed interval,
external bridge branch,
singleton-prefix recurrence,
cyclic recurrence,
collapse.
```

### Extracted proof

Apply A5 at the recurrent hit.  If the nearest blocker is bounded, Lemma F7.1 gives strict descent.  If the blocker is non-crossing but long, the pullback remains in the pair-difference window and gives a smaller pair-difference prefix or zero-composite branch.  If the blocker crosses the local boundary, F6/F8 classify it as external bridge, equal/signed interval, or cyclic recurrence.  Endpoint cases reduce to singleton-prefix recurrence or collapse. ∎

### Audit flags

```text
A69 endpoint and crossing cases must be expanded in the appendix.
```

---

## F7.7. Singleton-prefix recurrence

Singleton-prefix recurrence has a forbidden hit of the form

```text
x+B_i=f
```

or in the atom case:

```text
x+q=f.
```

## Lemma F7.6: singleton-prefix recurrence routes to known classes

Every singleton-prefix recurrence routes to one of:

```text
suffix-zero descent,
pair-difference prefix descent,
zero-composite branch,
external bridge branch,
cyclic recurrence,
collapse.
```

### Extracted proof

Apply A5 at the singleton/prefix hit.  A left blocker inside the active prefix gives suffix-zero descent.  A right blocker inside the active block gives pair-difference prefix descent.  A blocker outside the active block gives an external bridge branch handled by F6/F8.  Endpoint and wrapped cases give cyclic recurrence or collapse.  The bounded cases strictly decrease by Lemma F7.1. ∎

### Audit flags

```text
A70 atom-singleton endpoint cases need explicit final text.
```

---

## F7.8. Cyclic-cut recurrence

Cyclic recurrence arises when a cyclic cut or wrapped endpoint produces a new forbidden hit.

A cyclic cut at endpoint `S_c` transforms endpoint values into:

```text
S_i-S_c
```

for suffix endpoints and

```text
sigma-S_c+S_i
```

for wrapped prefix endpoints.

## Lemma F7.7: cyclic-cut recurrence routes to known classes

Every cyclic-cut recurrence routes to one of:

```text
earlier forbidden hit contradiction,
midpoint boundary,
zero-composite branch,
wrapping bridge branch,
singleton-prefix recurrence,
pair-difference branch,
collapse.
```

### Extracted proof

Use the cyclic endpoint formulas.  A recurrent wrapped endpoint either gives an earlier forbidden hit under the original basepoint, a symmetric endpoint equation producing midpoint boundary, or a wrapping interval equation.  Non-wrapping equations are zero-composite/equal-interval branches.  Wrapping equations split into suffix and prefix bridges handled by F6/F8.  Endpoint cases reduce to singleton-prefix or pair-difference recurrence. ∎

### Audit flags

```text
A71 special midpoint equations and p=3 behavior require audit.
No division by 3 should occur.
```

---

## F7.9. Recurrence routing theorem

## Theorem F7.8: recurrence routing theorem

Every forbidden recurrence produced by a local move routes to one of:

```text
1. strict M_NW^* descent by bounded blocker;
2. zero-composite / equal / signed interval machinery;
3. pair-difference machinery;
4. singleton-prefix recurrence with smaller active support;
5. cyclic-cut recurrence;
6. external bridge branch handled by F6/F8;
7. weighted-core branch handled by F10/F11;
8. collapse or minimality contradiction.
```

No recurrence branch introduces a new obstruction species outside the state machine.

### Proof

Apply the recurrence dichotomy Lemma F7.3.  Bounded blockers descend by Lemma F7.1.  External/cyclic blockers are routed by F6 or Lemma F7.7.  Long internal blockers are covered by the H1/H2, pair-difference, and singleton-prefix recurrence lemmas F7.4--F7.6.  Any weighted-core output is routed to F10/F11.  Collapse and contradiction are terminal. ∎

---

## F7.10. Interface with non-weighted termination

F7 is a routing theorem.  It does not alone prove global termination.  Its outputs are consumed by:

```text
F4 zero-composite/equal/pair descent;
F5 separated-equal/midpoint routing;
F6 external collision theorem;
F8 bridge/gap descent theorem;
F9 non-weighted termination theorem;
F10/F11 weighted branch.
```

The termination statement belongs to F9.

---

## F7.11. Remaining extraction risks

Before final manuscript status:

```text
R1. H1/H2 blocker equations must be written separately with signs.
R2. Pair-difference recurrence endpoint cases require explicit table.
R3. Singleton-prefix atom case requires explicit table.
R4. Cyclic-cut midpoint equations require characteristic audit.
R5. Each recurrence source must use the augmented span convention from A99.
R6. Exits to F6/F8/F10/F11 must be cross-referenced exactly.
```

---

## F7.12. Extraction status

```text
Status: extracted draft.
Risk: ORANGE.
Next recommended extraction: F8 bridge/gap descent theorem or F4 local descent theorem.
```
