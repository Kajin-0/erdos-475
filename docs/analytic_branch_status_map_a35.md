# Analytic branch status map A35

This note summarizes the current proof-program dependency graph after A1--A34.

It is intentionally conservative.  It separates branches into:

```text
PROVED / CLOSED
CONTROLLED DESCENT
RECURRENCE WITH MEASURE OBLIGATION
HARD RESIDUAL
```

No complete analytic proof is claimed here.

---

## 1. Main reduction chain

### A1: strong nonzero-sum implies Erdős 475

Status:

```text
PROVED
```

If every nonzero-sum subset admits an ordering with extended partial sums

```text
0,S_1,...,S_t
```

pairwise distinct, then Graham's rearrangement conjecture follows.

### A2/A3: endpoint avoidance equivalent/reduces to strong nonzero-sum

Status:

```text
PROVED REDUCTION
```

The main strengthened target is:

```text
For every A subset F_p^* and f != sigma(A),
there exists a Graham-valid ordering avoiding f.
```

This implies strong nonzero-sum by choosing `f=0` when `sigma(A) != 0`.

---

## 2. First-hit obstruction layer

### A5: first-hit right-swap obstruction

Status:

```text
PROVED
```

If endpoint avoidance fails and `S_h=f` is the earliest forbidden hit, then the right-adjacent swap at `h` is blocked:

```text
S_{h-1}+r_{h+1}=S_j,   j != h.
```

This produces either a backward or forward bypass zero-sum relation.

### A6: bypass rotation formulas

Status:

```text
PROVED FORMULAS / OPEN SUCCESS CLAIM
```

Forward and backward bypass rotations have exact partial-sum and obstruction equations.

Open:

```text
show one rotation or follow-up move always succeeds or descends.
```

### A9: punctured intervals and zero-block contiguization

Status:

```text
PROVED STRUCTURAL REFORMULATION
```

The blocked adjacent swap contiguizes a punctured zero-sum relation into an exposed zero block.

Open:

```text
general zero-block breaking / relocation success.
```

---

## 3. Cyclic-cut obstruction layer

### A7: cyclic cut formulas

Status:

```text
PROVED
```

Cutting after the forbidden hit gives exact criteria:

```text
cross collision: S_alpha=sigma+S_beta
forbidden hit:   S_alpha=2f or S_beta=2f-sigma
```

### A8: combined local + cyclic package

Status:

```text
PROVED ALTERNATIVE
```

Every minimal endpoint-avoidance counterexample has:

```text
local bypass package
+
cyclic obstruction package
```

### A11: transported cyclic block

Status:

```text
PROVED SPLIT
```

In the cyclic cross branch, the transported cyclic block under the adjacent swap:

```text
beta < h: remains a zero block
ess beta = h: becomes pair-difference b-a
```

Open:

```text
true two-zero-block uncrossing and boundary pair-trap repair.
```

---

## 4. Equal-sum special-hit layer

### A12: special-hit equal-sum traps

Status:

```text
PROVED
```

The non-cross cyclic branches become equal-sum traps:

```text
S_alpha=2f        -> sum(0,h]=sum(h,alpha]
S_beta=2f-sigma   -> sum(beta,h]=sum(h,t]
```

### A13: direct exchange formulas

Status:

```text
PROVED FORMULAS / NEGATIVE RESULT
```

Direct exchange of whole equal-sum blocks preserves an `f`-hit.  It cannot by itself prove endpoint avoidance.

### A14--A17: proper-prefix and singleton-prefix interleavings

Status:

```text
PROVED FORMULAS AND PRUNING
```

Proper-prefix and singleton-prefix moves have exact collision/forbidden-hit equations.  Many impossible equations are pruned by old-hit or old-collision arguments.

Open:

```text
complete prefix-trap dichotomy.
```

### A18/A19: residual singleton substitution and interval table

Status:

```text
PROVED REDUCTION
```

Remaining singleton traps reduce to:

```text
equal-interval traps,
signed-equal-interval traps,
prefix-zero branch.
```

---

## 5. Interval geometry and symbolic tooling

### A20: equal/signed interval geometry table

Status:

```text
PROVED GEOMETRY TABLE
```

Immediate collapses:

```text
shared endpoint old collision,
shared endpoint prefix-zero,
adjacent signed interior-zero.
```

Residual classes:

```text
proper-overlap equal outer pieces,
nested two-piece zero,
adjacent midpoint,
separated equal,
separated signed,
weighted signed overlap/nesting.
```

### A21--A24: classifiers and sweeps

Status:

```text
IMPLEMENTED PROOF-AUDIT TOOLS
```

Tools:

```text
scripts/classify_interval_traps.py
scripts/classify_a19_residual_row.py
scripts/batch_classify_a19_residuals.py
scripts/sweep_a23_residual_histograms.py
```

These are symbolic/positional tools, not proof engines.

### A25: sweep findings

Status:

```text
AUDIT RESULT
```

Main residual priorities after secondary constraints:

```text
reduction_equal_outer_pieces,
residual_two_piece_zero,
residual_separated_signed,
residual_signed_overlap_weighted,
residual_signed_nested_weighted,
residual_midpoint,
residual_separated_equal.
```

---

## 6. Composite interval surgery

### A26: composite interval surgery lemmas

Status:

```text
PARTIALLY CONTROLLED
```

Closed/controlled:

```text
proper-overlap equal intervals strictly lower total span;
two-piece zero composites can be contiguized;
separated signed composites are two-piece zero composites.
```

Open:

```text
relocation always succeeds or descends;
weighted signed branch;
midpoint branch.
```

### A27: normalization pass

Status:

```text
IMPLEMENTED CONTROLLED DESCENT
```

The tool:

```text
scripts/normalize_interval_relation.py
```

iterates equal-outer-piece descent until terminal geometry.

---

## 7. Two-piece zero and atom insertion

### A28: two-piece zero standard form

Status:

```text
PROVED FORMULAS
```

A two-piece zero composite has standard form:

```text
X A G C Y,
 sum(A)+sum(C)=0.
```

Moving the gap creates an exposed zero block and explicit obstruction equations.

### A29: zero-block breaking by insertion

Status:

```text
PROVED STRUCTURAL FACT AND FORMULAS
```

Internal reordering of a zero block cannot fix its endpoint collision.  One must insert outside material or move a subblock out.

Atom/block insertion formulas are exact.

### A30: atom-insertion obstruction table

Status:

```text
PROVED ROUTING TABLE
```

Atom-insertion failures route to:

```text
two-piece zero,
equal interval,
three-piece zero,
prefix/interior zero,
forbidden landing.
```

### A31: atom-insertion descent audit

Status:

```text
PARTIAL DESCENT
```

Closed/descending:

```text
Q1 strict support descent;
Q5 collapse/prefix-zero;
Q4 endpoint collapse and equal-interval routing;
Q2 descent except |B|=1;
Q3 non-descent isolated.
```

Open:

```text
Q2 |B|=1 pair boundary;
H1/H2 recurrence;
global recurrence measure.
```

### A32: boundary pair traps

Status:

```text
PARTIALLY CLOSED
```

Proved:

```text
Q3 non-descent forces i=1, j=|B| and hence q=A_1;
this is impossible in standard disjoint-atom insertion.
```

Remaining:

```text
Q2 pair-difference trap q-b_0=Y_m;
H1/H2 recurrence when not earlier.
```

### A33: Q2 pair-difference trap

Status:

```text
PARTIAL DESCENT
```

Proved:

```text
pair-swap reduces collision obstruction to smaller equal-prefix A_i=Y_m;
only forbidden-hit recurrence x+Y_m=f remains.
```

Remaining:

```text
recurrence branch if the new f-hit is not earlier.
```

---

## 8. Recurrence measure

### A34: global recurrence measure

Status:

```text
FRAMEWORK / OPEN THEOREM
```

Defines active obstruction states and a robust span-first measure:

```text
M*(O)=(h, span, pieces, type_rank, boundary_rank).
```

Open target:

```text
A34.R: every recurrence branch produces a new active obstruction O'
with M*(O') < M*(O), or collapses.
```

This is one of the main remaining proof obligations.

---

# 9. Current hard residuals

The proof is not complete.  The current hard residuals are:

## H1. Global recurrence descent

Need to prove A34.R for:

```text
A31 H1/H2,
A33 forbidden recurrence,
A14/A17 singleton-prefix recurrence,
A12 equal-sum exchange recurrence.
```

## H2. Weighted signed branches

Need to eliminate:

```text
residual_signed_overlap_weighted,
residual_signed_nested_weighted.
```

These have relations like:

```text
sum(A)+2sum(B)+sum(C)=0.
```

## H3. Midpoint branches

Need to eliminate adjacent equal-interval midpoint relations:

```text
2S_y=S_x+S_v.
```

## H4. Separated equal intervals

Need to eliminate terminal separated equal intervals not reducible by proper-overlap descent:

```text
sum(A)=sum(C)
```

with a genuine gap between them.

## H5. True two-zero-block uncrossing

Need to close the case where transported cyclic zero block and local zero block coexist in the same auxiliary ordering.

---

# 10. Recommended next target A36

The most promising next branch is H3/H4, because they are clean interval relations without coefficient `2` composites involving three pieces.

Suggested A36:

```text
Separated equal interval exchange formulas
```

Given:

```text
X A G C Y,
 sum(A)=sum(C),
```

compute the exact formulas for exchanging `A` and `C`, or moving `G`, and determine whether failure routes to:

```text
midpoint,
two-piece zero,
prefix-zero,
weighted signed,
or smaller equal interval.
```

This may also attack midpoint branches as a boundary case of separated equal intervals with zero gap.

---

## Bottom line

The proof program has made substantial structural progress, but a complete proof still requires closing the hard residuals listed above.  The current best next step is A36: separated equal interval surgery.
