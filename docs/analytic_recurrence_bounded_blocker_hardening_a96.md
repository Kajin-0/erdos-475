# Analytic recurrence bounded-blocker hardening A96

This note continues from A95.

A93 isolated five hardening obligations:

```text
U1. Strict progress lemma.
U2. Universal external-collision classification.
U3. Recurrence bounded-blocker measure.
U4. Cut-swap displayed collision table.
U5. Bridge/gap measure inequalities.
```

A94 addressed U1.  A95 addressed U2.  A96 addresses U3 by hardening the A64 recurrence bounded-blocker measure.

The goal is to make precise why a recurrent forbidden hit with a bounded A5 blocker gives strict descent, and why only long blockers require the special routing analyses A65--A71.

---

## 1. Recurrence setup

Let a local move transform an ordering

```text
R -> R'
```

where `R'` is Graham-valid but hits the forbidden value `f`.

Let `H` be the first forbidden-hit endpoint of `R'` relevant to the recurrence branch:

```text
S'_H=f.
```

Since the final endpoint is not forbidden, `H` is not final.  Let the next atom after the hit be

```text
z=r'_{H+1}.
```

Then A5 applies at `H` and gives a blocker endpoint `j` satisfying

```text
S'_{H-1}+z=S'_j.
```

This is the transformed A5 blocker equation.

---

## 2. Blocker span

## Definition A96.1: blocker interval and blocker span

Given a recurrent hit `H` and A5 blocker endpoint `j`, define the blocker interval in `R'` by:

```text
I(j,H)=
  (j,H-1]      if j < H,
  (H,j]        if j > H.
```

The blocker span is:

```text
span_blk(j,H)=|H-j|.
```

Equivalently, it is the number of atoms strictly traversed between the blocker endpoint and the hit endpoint, up to the A5 adjacent atom correction.

If `j=H`, then A5 gives `z=0`, impossible because atoms lie in `F_p^*`.  Thus `j != H`.

---

## 3. Source obstruction span

The recurrence came from a source obstruction `O` in the pre-move ordering.  Let

```text
span_src(O)
```

be the enclosing atom span of the active source window that generated the local move.

Examples:

```text
zero block P Q:             span_src=|P|+|Q|;
atom insertion P Q q:       span_src=|P|+|Q|;
pair swap P a b:            span_src=|P|+2;
singleton prefix B_i:       span_src=|B_i| plus local tail convention;
separated equal B G U:      span_src=|B|+|G|+|U|;
weighted core A B C:        span_src=|A|+|B|+|C|.
```

For each final-proof lemma, `span_src` must be specified explicitly.

---

## 4. Bounded versus long blockers

## Definition A96.2: bounded and long A5 blockers

An A5 blocker is bounded relative to the source obstruction `O` if

```text
span_blk(j,H) < span_src(O).
```

It is long if

```text
span_blk(j,H) >= span_src(O).
```

The bounded case should descend immediately.  The long case is not assumed to descend and must be routed separately.

---

## 5. Pullback of a left blocker

If `j < H`, then:

```text
S'_{H-1}-S'_j + z = 0.
```

Thus:

```text
sum'(j,H-1] + z = 0.
```

This is a zero relation supported on the blocker interval plus the next atom `z`.

## Lemma A96.3: left bounded blocker gives smaller zero-composite obstruction

If `j < H` and `span_blk(j,H) < span_src(O)`, then the pullback of the A5 blocker is a zero-composite obstruction with active span strictly less than `span_src(O)`, unless the adjacent atom correction `z` lies outside the blocker enclosure.  In that exception, the obstruction is a signed/bridge composite routed by A95 and A74--A77.

### Proof

The left-blocker equation is

```text
sum'(j,H-1]+z=0.
```

The interval `(j,H-1]` has span `span_blk(j,H)`.  If the adjacent atom `z` is contiguous to this interval, the active support has enclosing span at most `span_blk(j,H)+1`.  Under the final convention, the source span includes the corresponding adjacent atom in the local move window, so boundedness gives a strictly smaller active window.

If `z` is not contained in the same pulled-back enclosure because of a local move boundary or cyclic wrap, the pullback is a signed bridge or external composite.  A95 classifies this as an external collision/bridge branch, and A74--A77 handle its measure effect. ∎

### Audit note

The final proof should choose the span convention so the adjacent atom correction is included consistently.  Otherwise the inequality should be written as

```text
span_blk(j,H)+1 < span_src^+(O).
```

where `span_src^+` includes the A5 next atom.

---

## 6. Pullback of a right blocker

If `j > H`, subtract the hit endpoint.  Let `y` be the atom that ends at the hit endpoint, i.e.

```text
S'_H=S'_{H-1}+y.
```

From

```text
S'_{H-1}+z=S'_j
```

we get

```text
S'_j-S'_H=z-y.
```

Thus the interval after the hit up to the blocker satisfies

```text
sum'(H,j]=z-y.
```

or

```text
y-z+sum'(H,j]=0.
```

This is a pair-difference or signed zero-composite obstruction.

## Lemma A96.4: right bounded blocker gives smaller pair-difference/signed obstruction

If `j > H` and `span_blk(j,H) < span_src(O)`, then the pullback of the A5 blocker is a pair-difference or signed zero-composite obstruction with active span strictly less than the source span, except for boundary/cyclic cases routed by A95/A71.

### Proof

The right-blocker equation is

```text
y-z+sum'(H,j]=0.
```

The interval `(H,j]` has span `span_blk(j,H)`.  The atom correction `y-z` is supported at the hit boundary and the next-atom boundary.  If both atoms remain inside the local enclosure, the active obstruction has smaller span/support than the source.  If one atom correction crosses a local boundary or cyclic cut, A95/A71 classify it as signed bridge, pair-difference boundary, or cyclic recurrence. ∎

---

## 7. Measure for bounded recurrence

Use the global non-weighted measure from A78:

```text
M_NW^*=(
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

For weighted states use:

```text
M_total=(|B|, M_NW^*)
```

when the active class is `WEIGHTED_CORE`.

---

## Lemma A96.5: bounded blockers strictly decrease the active measure

Assume a recurrent transformed ordering has an A5 blocker with

```text
span_blk(j,H) < span_src(O)
```

under the final span convention including required adjacent atom corrections.  Then the pulled-back obstruction has strictly smaller `enclosing_span` than the source obstruction, unless it is routed to an external bridge/cyclic branch.  In those exceptional cases it enters the A95 external-collision classification or A71 cyclic classification and does not create a new recurrence species.

### Proof

Left blockers are Lemma A96.3.  Right blockers are Lemma A96.4.  In the ordinary non-wrapping case, the enclosing span is strictly bounded by the source span.  Since `enclosing_span` is the first coordinate of `M_NW^*`, the measure strictly decreases.  Boundary, bridge, and cyclic exceptions are not treated as bounded internal descent; they are routed to the already named classes. ∎

---

## 8. Nearest blocker convention

A5 may produce more than one blocker endpoint.  Choose one with minimal blocker span.

## Definition A96.6: nearest A5 blocker

A nearest blocker is an index `j` satisfying the A5 equation

```text
S'_{H-1}+z=S'_j
```

and minimizing

```text
span_blk(j,H)=|H-j|.
```

among all such blockers.

Since the ordering is finite, a nearest blocker exists whenever any blocker exists.

---

## Lemma A96.7: nearest blocker dichotomy

For every recurrent forbidden hit, the nearest A5 blocker is either bounded or long:

```text
span_blk(j,H) < span_src(O)
```

or

```text
span_blk(j,H) >= span_src(O).
```

### Proof

This is the law of trichotomy for integers, with equality included in the long case. ∎

---

## 9. Long blockers are the only recurrence cases needing special routing

If the nearest blocker is bounded, Lemma A96.5 gives descent or exits into already classified bridge/cyclic branches.

If the nearest blocker is long, local descent cannot be concluded from span alone.  These are exactly the cases handled by:

```text
A65--A66: H1 atom-insertion long blockers;
A67: H2 atom-insertion long blockers;
A69: pair-swap recurrence long blockers;
A70: singleton-prefix recurrence long blockers;
A71: cyclic-cut recurrence;
A74--A77: bridge/gap long-return ties.
```

---

## Theorem A96.8: recurrence bounded-blocker theorem

Let a recurrence branch arise from a source obstruction `O`, with first recurrent hit `H`.  Let `j` be a nearest A5 blocker.

Then exactly one of the following holds:

```text
1. bounded internal blocker: the pullback gives strict M_NW^* descent;
2. bounded boundary/bridge/cyclic blocker: the pullback routes by A95/A71/A74--A77;
3. long blocker: the branch enters the long-blocker routing analyses A65--A71.
```

In particular, bounded blockers introduce no new recurrence species and cannot support an infinite recurrence path with fixed measure.

### Proof

Existence and dichotomy are Definition A96.6 and Lemma A96.7.  Bounded left and right blockers are Lemmas A96.3--A96.5.  Long blockers are, by definition, those not covered by bounded descent and are assigned to the long-blocker routing notes. ∎

---

## 10. What A96 hardens

A96 replaces the informal A64 phrase:

```text
bounded blockers descend
```

with the precise theorem:

```text
nearest bounded blocker -> strict enclosing-span descent
or named bridge/cyclic routing.
```

The remaining requirement is to check that every recurrence source defines `span_src(O)` consistently with the adjacent atom correction.

---

## 11. Remaining hardening items

After A96, U3 is hardened at the framework level.

Remaining items:

```text
U4. A60 cut-swap displayed collision table.
U5. A74--A77 bridge/gap measure inequalities.
```

Also required:

```text
R-span audit: verify span_src conventions in A65--A71 and final proof extraction.
```

---

## 12. Target A97

A97 should harden A60:

```text
Cut-swap displayed collision table.
```

Required output:

```text
1. define weighted cut-swap A P R C -> A R P C;
2. list all transformed displayed endpoint families;
3. compare every pair of moved/unchanged families;
4. derive each collision equation;
5. classify each as zero-composite, equal/signed interval, transported-prefix, pair-difference, weighted-core return, or external collision;
6. check endpoint/empty-block cases.
```

---

## Current status after A96

Proved/recorded here:

```text
1. blocker span definition;
2. bounded vs long blocker dichotomy;
3. left bounded blocker pullback;
4. right bounded blocker pullback;
5. bounded blockers strictly decrease M_NW^* except named boundary/bridge/cyclic exits;
6. nearest blocker convention;
7. long blockers are exactly the cases routed by A65--A71.
```

Still open:

```text
1. A60 cut-swap displayed collision table hardening;
2. A74--A77 bridge/gap inequality hardening;
3. span convention audit across recurrence sources;
4. final proof extraction.
```
