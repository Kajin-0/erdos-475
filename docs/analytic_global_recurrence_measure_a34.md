# Analytic global recurrence measure A34: preventing obstruction cycles

This note continues from A33.

A33 reduced the Q2 pair-difference boundary trap to:

```text
1. a smaller equal-interval descent, or
2. a forbidden-hit recurrence branch.
```

The recurrence branch occurs when a transformed ordering still hits the forbidden value `f`, but the hit is not earlier than the original minimal hit index `h`.  This note defines a global obstruction measure intended to control those recurrence branches.

This is a framework note.  It does not prove that every recurrence decreases the measure.  It identifies the exact measure and the verification obligations.

---

## 1. Motivation

The proof program repeatedly performs local moves:

```text
adjacent swap,
cyclic cut,
proper-prefix interleaving,
gap relocation,
atom insertion,
pair swap.
```

A move can fail in three broad ways:

```text
1. it creates a Graham collision;
2. it creates or preserves a forbidden hit;
3. it routes to a composite interval obstruction.
```

Earlier notes converted most failures into explicit obstruction objects:

```text
zero block,
two-piece zero composite,
equal interval,
signed equal interval,
weighted signed composite,
pair-difference trap,
forbidden landing.
```

The remaining danger is recurrence: a move produces a new Graham-valid ordering that still hits `f`, but not earlier than before.  A first-hit minimality argument alone does not eliminate that case.

A34 introduces a richer measure so that recurrence can still be descending.

---

## 2. Active obstruction state

An active obstruction state is a tuple

```text
O = (R, h, type, support, pieces, span, boundary_rank)
```

where:

- `R` is the current Graham-valid ordering;
- `h` is the first index with `S_h=f`;
- `type` records the active obstruction class;
- `support` is the set of indices participating in the obstruction;
- `pieces` is the number of separated interval/atom pieces in the obstruction;
- `span` is the total support length or enclosing interval length;
- `boundary_rank` records whether the obstruction touches a critical boundary such as `h`, `h+1`, the basepoint, or the final endpoint.

This is not meant to be unique.  It is a proof bookkeeping device: each reduction should specify the active obstruction it creates.

---

## 3. Obstruction type order

Define the following tentative type order, from simpler to harder:

```text
COLLAPSE
PREFIX_ZERO
ZERO_BLOCK
TWO_PIECE_ZERO
EQUAL_INTERVAL
SIGNED_EQUAL_INTERVAL
PAIR_DIFFERENCE
WEIGHTED_SIGNED
FORBIDDEN_RECURRENCE
```

For descent, we order states lexicographically by:

```text
M(O) = (
  h,
  type_rank,
  pieces,
  span,
  boundary_rank
)
```

but with the first coordinate ordered normally and all obstruction complexity coordinates ordered normally as well.  Thus a move is descending if it produces:

```text
1. smaller first forbidden-hit index h; or
2. same h but smaller type_rank; or
3. same h/type but fewer pieces; or
4. same h/type/pieces but smaller span; or
5. same all above but lower boundary rank.
```

### Important caveat

The type order above is provisional.  Some branches may require swapping `type_rank` and `span` in the lexicographic priority.  For example, A31 showed that Q3 can increase the number of pieces while decreasing support.  Such branches may need a measure of the form:

```text
(h, span, pieces, type_rank, boundary_rank)
```

rather than:

```text
(h, type_rank, pieces, span, boundary_rank).
```

The correct choice must be validated against every recurrence-producing branch.

---

## 4. Recommended robust measure

To handle Q3-type behavior, use the following robust measure:

```text
M*(O) = (
  h,
  span,
  pieces,
  type_rank,
  boundary_rank
)
```

This prioritizes reduction in support span before reduction in number of pieces.

The rationale is:

- A26.1 equal-outer-piece descent strictly lowers span.
- A31 Q1 strictly lowers support span.
- A31 Q2 lowers support span except for the `|B|=1` pair boundary.
- A32 eliminates Q3 non-descent in the standard disjoint-atom case.
- A33 reduces the Q2 boundary to smaller equal-prefix support unless it becomes a forbidden recurrence.

Thus span-first ordering appears better aligned with the actual reductions.

---

## 5. Boundary rank

Define boundary rank as a small integer encoding how attached the obstruction is to critical endpoints:

```text
0: no critical boundary contact;
1: touches ordinary internal block boundary;
2: touches first-hit boundary h or h+1;
3: touches basepoint or final endpoint;
4: boundary pair trap such as beta=h or |B|=1.
```

This rank is used only after `h`, `span`, `pieces`, and `type_rank` are tied.

The purpose is to classify cases such as:

```text
beta=h,
|B|=1,
j=h-1,
i=h,
i=h-1.
```

Most of these already collapsed or became pair-trap branches in A18/A32/A33.

---

## 6. Recurrence verification obligations

The following branches must be checked against `M*`.

### R1. A29/A30 atom insertion forbidden hit H1

Equation:

```text
T_y+q=f.
```

Obligation:

If the new hit is not earlier than the old `h`, show that the active obstruction support is smaller than the obstruction that produced the atom-insertion attempt.

Expected support drop:

```text
two-piece zero support -> atom landing support
```

or

```text
pair-difference support -> equal-prefix support.
```

### R2. A29/A30 atom insertion forbidden hit H2

Equation:

```text
T_y+q+B_j=f.
```

Obligation:

If the new hit is not earlier, show that the prefix `B_j` is proper, giving smaller support, or that the endpoint case collapses to a zero-prefix/interior-zero branch.

### R3. A33 Q2 pair-swap forbidden recurrence

Equation:

```text
x+Y_m=f.
```

Obligation:

If not earlier than old `h`, show that `Y_m` is a proper prefix whose support is smaller than the original pair-difference obstruction support.  If `m` reaches an endpoint, show zero-prefix/interior-zero or old-hit collision.

### R4. A14/A17 singleton-prefix forbidden recurrences

Equations of the form:

```text
new prefix landing = f.
```

Obligation:

If not earlier than old `h`, the moved prefix must be proper and should reduce span compared with the original equal-sum block.

### R5. Cyclic-cut recurrence

Special hits:

```text
S_alpha=2f,
S_beta=2f-sigma.
```

Obligation:

The secondary minimality choices in A15 must be incorporated so that repeated cyclic-cut recurrence cannot select the same-size special-hit branch indefinitely.

---

## 7. Local theorem schema

The desired recurrence theorem can be stated as follows.

### Target theorem A34.R

Let `O` be an active obstruction state in a minimal endpoint-avoidance counterexample.  Suppose a valid local move transforms `O` into another Graham-valid ordering that still hits `f`, and suppose the first hit is not earlier than the previous first hit.  Then the transformed ordering carries a new active obstruction `O'` such that

```text
M*(O') < M*(O)
```

lexicographically.

If no such `O'` exists, then the local move must have created one of the already classified collapse branches:

```text
old Graham collision,
interior zero interval,
prefix-zero branch,
boundary pair trap.
```

---

## 8. Why this would close several branches

If A34.R is proved for all recurrence branches, then all previously isolated recurrence cases become finite descent cases.

Specifically:

```text
A31 H1/H2 recurrence,
A33 Q2 forbidden recurrence,
A14/A17 singleton-prefix recurrence,
A12 equal-sum exchange recurrence.
```

would no longer be terminal gaps.

The remaining hard branches after that would be the genuinely weighted signed branches and midpoint/separated-equal terminal branches from A26/A27.

---

## 9. Current status

Defined here:

1. active obstruction state;
2. provisional type order;
3. robust span-first measure `M*`;
4. boundary rank;
5. recurrence verification obligations R1--R5;
6. target recurrence theorem A34.R.

Not proved here:

1. A34.R for all recurrence branches;
2. weighted signed branch elimination;
3. midpoint branch elimination;
4. endpoint avoidance theorem.
