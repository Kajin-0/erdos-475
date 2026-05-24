# F00.SNS.C17 support, boundary, and label diagnostics

This file continues the strong nonzero-sum repair path.

C15 hardened collision-profile compensation.  C16 hardened the first-changed-endpoint branch.  The remaining C7 item is:

```text
C7.4 support/boundary/label diagnostics.
```

The goal is to show that if a phase-aware weighted self-return changes support, boundary, or endpoint-label data, then it cannot remain an invisible non-descending weighted return.  It must produce local repair, external/bridge repair, defect descent, smaller weighted middle, transported-prefix/easy weighted reduction, or collision-free success.

Status: hardening draft.

---

## C17.1. Setup

Work in ARBITRARY phase.

Let a weighted repair state have displayed form

```text
X A B C Y
```

with weighted relation

```text
a+2b+c=0.
```

A phase-aware weighted self-return is a finite path

```text
Omega_0 -> Omega_1 -> ... -> Omega_N
```

with weighted repair at both ends.

Assume:

```text
D_SNS^*(Omega_N)=D_SNS^*(Omega_0),
|B_N| >= |B_0|,
```

and no branch has already exited through C11, C12, C13, C15, or C16.

---

## C17.2. Diagnostic data

The weighted pattern data consists of:

```text
1. outer support blocks A,C;
2. middle support block B;
3. internal endpoint set E_B;
4. left and right boundary endpoints of A,B,C;
5. endpoint labels / interval representations;
6. collision-profile contribution of the weighted window.
```

C15 handles item 6.  C16 handles item 3.  C17 handles items 1, 2, 4, and 5.

---

## C17.3. Middle support change

Suppose the returned weighted state has middle block `B'` different from `B`.

There are four geometric cases:

```text
1. B' subsetneq B;
2. B subsetneq B';
3. B' properly overlaps B;
4. B' is disjoint from B.
```

---

## Lemma C17.1: smaller middle support gives weighted descent

If

```text
B' subsetneq B,
```

then the weighted measure decreases by `|B'|<|B|`.

### Proof

The first coordinate of the weighted submeasure is middle length.  Proper containment gives strict length decrease. ∎

---

## Lemma C17.2: enlarged middle support exposes local or external repair

If

```text
B subsetneq B',
```

then subtracting the old and new weighted relations produces a nonzero complement relation outside the old middle.  This routes to one of:

```text
LOCAL_ZERO_COMPOSITE;
EQUAL_INTERVAL;
SIGNED_INTERVAL;
BRIDGE_GAP;
EXTERNAL_COLLISION;
TRANSPORTED_PREFIX.
```

### Proof sketch

Write `B'=L B R` in the containment case.  Compare

```text
a+2b+c=0
```

with the returned relation

```text
a'+2b'+c'=0.
```

The extra doubled contribution from `L` and/or `R` must be balanced by changes in the outer blocks.  If those changes lie inside the same displayed window, subtraction gives local zero/equal/signed repair.  If they cross the old window boundary, it is external/bridge repair.  If the balancing contribution is a transported copy of an old prefix/tail, it is transported-prefix. ∎

---

## Lemma C17.3: proper-overlap middle support uncrosses

If `B` and `B'` properly overlap, then comparing the two weighted relations and canceling the common overlap produces either:

```text
1. smaller weighted middle;
2. local equal/signed interval repair;
3. bridge/gap repair;
4. transported-prefix repair.
```

### Proof sketch

Write

```text
B=B_0 O,
B'=O B_1
```

or the reverse orientation, with nonempty overlap `O`.  Subtract the two weighted relations.  The doubled common overlap cancels.  The remaining doubled pieces are strictly shorter than the original middle or are balanced by outer-block changes.  Local balancing gives C11 rows; external balancing gives C12 rows. ∎

---

## Lemma C17.4: disjoint middle support gives separated/bridge repair

If `B` and `B'` are disjoint, then the return crosses a nonempty gap.  The comparison routes to:

```text
SEPARATED_EQUAL;
BRIDGE_GAP;
EXTERNAL_COLLISION;
WEIGHTED_REPAIR with finite cut-budget;
D_SNS^* descent if collision profile improves.
```

### Proof sketch

Disjoint middle supports cannot cancel by containment or overlap.  The gap between them becomes a separated bridge datum.  Equal or signed balancing of the two middle contributions is separated-equal or bridge/gap repair.  Cross-window balancing is external collision. ∎

---

## C17.4. Outer block change

Suppose the middle support is fixed but one of the outer blocks changes:

```text
A' != A
```

or

```text
C' != C.
```

---

## Lemma C17.5: outer block change gives local or transported-prefix repair

If `B` is fixed and `A` or `C` changes, then subtracting the old and new weighted relations cancels the doubled middle term and produces:

```text
LOCAL_ZERO_COMPOSITE;
EQUAL_INTERVAL;
SIGNED_INTERVAL;
PAIR_DIFFERENCE;
TRANSPORTED_PREFIX;
EXTERNAL_COLLISION if the change crosses window boundary.
```

### Proof

Subtract

```text
a+2b+c=0
```

and

```text
a'+2b+c'=0.
```

The doubled middle cancels, leaving

```text
(a-a')+(c-c')=0.
```

The differences `a-a'` and `c-c'` are interval differences or boundary atom corrections.  Local differences are C11 rows.  Boundary-crossing differences are C12 rows.  If one difference is a transported copy of a prefix/tail, it is transported-prefix repair. ∎

---

## C17.5. Boundary endpoint change

Suppose the supports `A,B,C` are the same but a boundary endpoint representation changes.  This means one endpoint is represented by a different interval decomposition after the return.

---

## Lemma C17.6: boundary endpoint change gives pair/signed repair or external collision

A changed boundary endpoint representation produces one of:

```text
PAIR_DIFFERENCE;
SIGNED_INTERVAL;
TRANSPORTED_PREFIX;
EXTERNAL_COLLISION;
BOUNDARY_DEGENERACY;
D_SNS^* descent.
```

### Proof sketch

Two representations of the same boundary endpoint differ by an interval sum plus at most a bounded atom correction.  Equality of the two endpoint values gives a pair/signed/transported-prefix relation.  If one representation uses atoms outside the displayed window, it is external.  If an endpoint becomes empty/full, it is a boundary-degeneracy row.  If the representation change removes a collision contribution, C15 gives defect descent. ∎

---

## C17.6. Endpoint-label change

Suppose endpoint values and supports are preserved, but labels or interval representations are permuted.

---

## Lemma C17.7: endpoint-label change is either harmless relabeling or repair data

An endpoint-label change with unchanged endpoint values is either:

```text
1. a harmless relabeling preserving phase-aware pattern data;
2. a pair-difference relation between two interval labels;
3. a transported-prefix relation;
4. a local collision-profile change handled by C15;
5. a finite-state symmetry already included in transition_budget.
```

### Proof sketch

If two labels denote the same interval representation, the change is harmless.  If they denote different representations of the same endpoint value, subtract the representations.  The result is zero/equal/pair/transported-prefix repair.  If the label exchange changes which collision pair is first in the local profile, C15 applies.  If it is a finite symmetry of the same representation, the transition budget controls repetition. ∎

---

## C17.7. Support/boundary/label diagnostic theorem

## Theorem C17.8: support-boundary-label changes route or descend

In a minimal non-descending phase-aware weighted self-return, any change in middle support, outer support, boundary endpoints, or endpoint labels gives one of:

```text
1. strict D_SNS^* descent;
2. smaller weighted middle |B|;
3. local repair row verified by C11;
4. external/bridge repair row verified by C12;
5. weighted easy reduction or transported-prefix repair verified by C13;
6. boundary-degeneracy row with finite rank decrease;
7. finite-label symmetry consumed by transition_budget;
8. collision-free SNS success.
```

Therefore, if no such exit occurs, the weighted self-return preserves all support, boundary, and label data required for phase-aware pattern-rigidity.

### Proof

Middle support changes are Lemmas C17.1--C17.4.  Outer block changes are Lemma C17.5.  Boundary endpoint changes are Lemma C17.6.  Endpoint-label changes are Lemma C17.7.  These cases exhaust support, boundary, and label changes. ∎

---

## C17.8. Consequence for C7

C17 hardens C7.4:

```text
support/boundary/label change
  -> local repair, external/bridge repair, weighted reduction,
     D_SNS^* descent, smaller middle, finite-rank decrease, or success.
```

Together with C15 and C16, this completes the architecture-level hardening of C7.

---

## C17.9. Remaining audit items

C17 still requires appendix-level expansion for public proof quality:

```text
R1. Write explicit subtraction formulas for each middle-support geometry.
R2. Write boundary endpoint sign table.
R3. Define harmless endpoint relabeling precisely.
R4. Define finite-label symmetry budget.
R5. Verify every boundary-degeneracy output maps to C10 boundary ranks.
```

---

## C17.10. Recommended next file

Now that C7.2--C7.4 have hardening drafts, the next file should update the global status:

```text
docs/final/F00_SNS_C18_post_C7_status_and_red_items.md
```

Goal:

```text
Reclassify the remaining proof gaps after C15--C17 and identify the shortest path to a complete SNS proof draft.
```

---

## C17.11. Status

```text
Status: C7.4 hardening draft.
Risk: ORANGE.
C7 architecture is now hardened at draft level, but appendix-level algebra remains.
```
