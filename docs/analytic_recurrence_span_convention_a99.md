# Analytic recurrence span-convention audit A99

This note continues from A98.

A96 hardened the recurrence bounded-blocker theorem, but it explicitly left one audit item:

```text
R-span audit: verify span_src conventions in A65--A71 and final proof extraction.
```

A99 standardizes the span convention used for recurrence descent.  The goal is to ensure that every A5 adjacent atom correction is counted consistently, so that the bounded-blocker inequality really implies strict decrease of the first coordinate of the final measure.

---

## 1. Final span convention

Let an active source obstruction occupy a displayed atom interval

```text
I=[i_0,i_1]
```

in the current ordering.  The source span is

```text
span_src(O)=i_1-i_0+1.
```

Thus `span_src` counts atoms, not endpoint gaps.

If the local move or A5 recurrence uses the next atom after the forbidden hit, the source window must include that atom.  Therefore define the augmented source span:

```text
span_src^+(O)=length of the smallest atom interval containing:
  source support,
  moved atoms,
  A5 hit atom,
  A5 next atom correction.
```

The bounded-blocker descent condition in the final proof should be written using:

```text
span_blk^+(j,H) < span_src^+(O).
```

where `span_blk^+` includes the A5 correction atoms.

---

## 2. Blocker span convention

For a recurrent hit at transformed index `H`, with blocker index `j`, define:

```text
span_blk(j,H)=|H-j|.
```

Define augmented blocker support as the smallest transformed-order interval containing:

```text
1. the interval between j and H;
2. the hit-boundary atom;
3. the next atom z used by A5.
```

Then:

```text
span_blk^+(j,H)=length of that augmented interval.
```

The recurrence branch is bounded if:

```text
span_blk^+(j,H) < span_src^+(O).
```

It is long otherwise.

---

## 3. Why augmentation is necessary

A96 used equations:

Left blocker:

```text
sum(j,H-1] + z = 0.
```

Right blocker:

```text
y-z+sum(H,j] = 0.
```

The atom `z` and sometimes `y` may lie just outside the naive blocker interval.  If the source span does not include the corresponding adjacent atom, the inequality can be off by one.

Therefore the final proof must not use the unaugmented inequality unless the convention is explicitly endpoint-gap based.

---

## 4. H1 atom-insertion recurrence span

H1 recurrence comes from atom insertion around a zero-composite or atom-insertion source, schematically:

```text
P Q q  ->  P q Q
```

or an equivalent local form.

The source support is:

```text
P Q q
```

including the moved atom `q`.  If the recurrent hit occurs before the next atom after the moved window, include that next atom in `span_src^+`.

Recommended convention:

```text
span_src^+(H1)=length(enclosure(P,Q,q,next_after_hit)).
```

## Audit result A99.H1

The H1 bounded-blocker descent should be stated with `span_src^+(H1)`, not merely `|P|+|Q|`.

Long-blocker cases in A65--A66 remain valid as the complement of the augmented bounded case.

---

## 5. H2 atom-insertion recurrence span

H2 recurrence is the second atom-insertion orientation.  Its source support is again the full insertion window plus A5 correction atoms.

Recommended convention:

```text
span_src^+(H2)=length(enclosure(source window, hit atom, next atom z)).
```

## Audit result A99.H2

A67 should be extracted using the augmented source span.  Endpoint cases where the next atom lies outside the displayed source window must be routed to A95 external collision or A71 cyclic recurrence, not treated as internal bounded descent.

---

## 6. Pair-swap recurrence span

For a pair-swap source, the local move has form:

```text
... a b ... -> ... b a ...
```

possibly with a local prefix/tail block attached.

The source support must include:

```text
the swapped pair,
the active prefix/tail involved in the pair-difference equation,
the A5 hit atom,
the A5 next atom correction.
```

Recommended convention:

```text
span_src^+(pair)=length(enclosure(pair-swap active window, y, z)).
```

## Audit result A99.pair

A69's non-crossing blocker descent is valid only when the pulled-back pair-difference support is strictly contained in this augmented source window.  Crossing blockers route to bridge/equal/signed classes and should not be counted as bounded internal descent.

---

## 7. Singleton-prefix recurrence span

For singleton-prefix recurrence:

```text
x+B_i=f
```

with local block `B`, the relevant source support is not always all of `B`; it is the active prefix plus the boundary atoms used by A5.

Recommended convention:

```text
span_src^+(single)=length(enclosure(B_i, previous boundary atom, next boundary atom, A5 next atom)).
```

For the atom case:

```text
x+q=f,
```

use:

```text
span_src^+(atom-single)=length(enclosure(q, previous atom if used, next atom z)).
```

## Audit result A99.single

A70's suffix-zero and pair-difference prefix descents should be measured against this augmented singleton source.  If the blocker lies beyond the local tail, it is a bridge branch and routes by A95/A98, not bounded descent.

---

## 8. Cyclic-cut recurrence span

For cyclic recurrence, the local move is a basepoint change:

```text
P R -> R P.
```

The source span is the active cyclic block being rotated.  Since cyclic cuts can wrap, linear span alone is ambiguous.

Use cyclic span:

```text
cspan_src^+(cyc)=minimum cyclic interval length containing:
  active rotated block,
  recurrent hit endpoint,
  A5 next atom correction,
  blocker pullback support.
```

For final extraction, avoid relying on bounded internal descent for cyclic wrapping cases.  Instead:

```text
non-wrapping bounded blockers -> ordinary span descent;
wrapping blockers -> A71 cyclic branch or A95/A98 bridge branch.
```

## Audit result A99.cyclic

A71 should remain a routing theorem, not a bounded-span descent theorem, unless a formal cyclic-span measure is introduced.

---

## 9. Final recurrence boundedness definition

The final proof should use the following definition.

## Definition A99.1: final bounded recurrence blocker

A recurrent A5 blocker is finally bounded if its augmented blocker support is strictly contained in the augmented source support:

```text
Supp_blk^+ subsetneq Supp_src^+.
```

Equivalently, in span terms:

```text
span_blk^+ < span_src^+
```

with both spans measured in the same linear or cyclic enclosure convention.

If strict containment is not available, the branch is not called bounded; it is routed as long/crossing/bridge/cyclic.

---

## Lemma A99.2: final bounded recurrence gives strict enclosing-span descent

Under Definition A99.1, the pulled-back A5 obstruction has strictly smaller enclosing span than the source obstruction.

### Proof

The pulled-back obstruction support is contained in `Supp_blk^+`.  By final boundedness,

```text
Supp_blk^+ subsetneq Supp_src^+.
```

Therefore the enclosing span of the pulled-back obstruction is strictly smaller than the source enclosing span.  Since enclosing span is the first coordinate of `M_NW^*`, the measure strictly decreases. ∎

---

## 10. Recurrence source audit table

| Source | Use bounded descent? | Final span convention | Non-bounded routing |
|---|---:|---|---|
| H1 atom insertion | yes | augmented source window including moved atom and A5 correction | A65--A66 / A95 / A98 |
| H2 atom insertion | yes | augmented source window including hit and next atom | A67 / A95 / A98 |
| Pair-swap | yes | augmented pair-difference window | A69 / A95 / A98 |
| Singleton-prefix | yes | active prefix plus boundary atoms | A70 / A95 / A98 |
| Atom singleton | yes, only local | atom plus boundary/next atom | A70 / A95 |
| Cyclic-cut | only non-wrapping | cyclic enclosure or route directly | A71 / A95 / A98 |
| External bridge recurrence | no direct bounded descent | bridge/gap measure | A95 / A98 |

---

## 11. Required edits during final extraction

When extracting the final proof, replace phrases like:

```text
bounded blocker has smaller span
```

with:

```text
the augmented blocker support is a proper subinterval of the augmented source support, so the first coordinate of M_NW^* decreases.
```

Replace phrases like:

```text
long blocker
```

with:

```text
blocker not satisfying Definition A99.1; routed by the corresponding long/crossing theorem.
```

---

## 12. Status after A99

A99 resolves the span-convention ambiguity by making augmented support containment the final definition of bounded recurrence.

Remaining before final extraction:

```text
1. detailed sign/endpoint audit for A60/A65--A71/A81;
2. final proof extraction into compact lemmas F1--F13;
3. optional finite verification/certification cleanup.
```

---

## 13. Target A100

A100 should start the final proof extraction rather than adding new machinery.

Recommended title:

```text
Final proof extraction plan A100
```

Required output:

```text
1. list final lemmas F1--F13;
2. map each final lemma to hardened A-notes;
3. mark which final lemmas are ready versus still needing sign/endpoint audit;
4. define a clean manuscript order;
5. identify the shortest path to a public proof draft.
```
