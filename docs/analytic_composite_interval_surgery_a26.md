# Analytic composite interval surgery A26: first rigorous lemmas

This note starts the composite interval surgery stage identified in A25.

A24/A25 show that after all local, cyclic, equal-sum, and singleton-prefix reductions, the major surviving symbolic classes are composite interval classes:

```text
reduction_equal_outer_pieces
residual_two_piece_zero
residual_separated_signed
residual_signed_overlap_weighted
residual_signed_nested_weighted
residual_midpoint
```

This note proves the first reusable lemmas for those classes.  It does not close the theorem.

---

## Standing notation

Let

```text
R=(r_1,...,r_t)
```

be an ordering, with partial sums

```text
S_0=0,
S_i=r_1+...+r_i.
```

For `0 <= x < y <= t`, write

```text
(x,y]=(r_{x+1},...,r_y),
sum(x,y]=S_y-S_x,
span(x,y]=y-x.
```

For a pair of intervals define the total span

```text
Span((x,y],(u,v]) = (y-x)+(v-u).
```

---

# 1. Equal-outer-piece descent

A20 showed that a proper-overlap equal-interval trap

```text
sum(x,y]=sum(u,v],    x<u<y<v
```

reduces to

```text
sum(x,u]=sum(y,v].
```

The next lemma records that this is a strict descent in total span.

## Lemma A26.1: equal-outer-piece reduction strictly lowers total span

Assume

```text
x<u<y<v
```

and

```text
sum(x,y]=sum(u,v].
```

Then

```text
sum(x,u]=sum(y,v],
```

and

```text
Span((x,u],(y,v]) < Span((x,y],(u,v]).
```

### Proof

Decompose the overlapping intervals as

```text
A=(x,u],
B=(u,y],
C=(y,v].
```

The equality is

```text
sum(A)+sum(B)=sum(B)+sum(C),
```

so cancellation gives

```text
sum(A)=sum(C).
```

For the span comparison,

```text
Span((x,y],(u,v]) = (y-x)+(v-u),
Span((x,u],(y,v]) = (u-x)+(v-y).
```

Subtracting gives

```text
[(y-x)+(v-u)] - [(u-x)+(v-y)] = 2(y-u)>0.
```

Thus the outer-piece relation has strictly smaller total span.  ∎

### Consequence

Repeated proper-overlap equal-interval reduction must terminate.  It cannot generate an infinite descent.  The terminal equal-interval traps are therefore among:

```text
1. shared endpoint collapse;
2. adjacent midpoint branch;
3. separated equal intervals;
4. nested equal intervals / two-piece zero complement.
```

This makes the `reduction_equal_outer_pieces` class a controlled descent class rather than a genuinely new obstruction.

---

# 2. Two-piece zero composites

A nested equal-interval trap produces a two-piece zero composite:

```text
sum(A)+sum(C)=0
```

where `A` and `C` are separated intervals.

The basic operation is to move the middle gap away so that `A` and `C` become adjacent.

## Lemma A26.2: separated two-piece zero can be contiguized by moving the gap

Let an ordering segment decompose as

```text
A G C
```

where

```text
sum(A)+sum(C)=0.
```

Consider the block move

```text
A G C  ->  A C G.
```

Then `AC` is a contiguous zero-sum block in the moved ordering.

### Proof

The block `AC` is contiguous after the move and has sum

```text
sum(A)+sum(C)=0.
```

∎

### Warning

This move can create a Graham collision precisely because it creates a contiguous zero-sum block.  Therefore the move is not directly a repair.  Its value is diagnostic: every two-piece zero composite can be converted into the same exposed-zero-block object studied in A9.

---

## Lemma A26.3: gap relocation partial-sum formula for two-piece zero composites

Let a displayed segment of an ordering be

```text
X A G C Y
```

and assume

```text
sum(A)+sum(C)=0.
```

Let

```text
x=sum(X),
a=sum(A),
g=sum(G),
c=sum(C)=-a.
```

Move the gap `G` to the right of `C`:

```text
X A G C Y  ->  X A C G Y.
```

Then:

1. partial sums before `A` are unchanged;
2. partial sums after the displayed segment are unchanged;
3. internal partial sums of `A` are unchanged;
4. internal partial sums of `C` are translated by `-g`;
5. internal partial sums of `G` are translated by `c=-a` relative to their old position after `A`.

### Proof

In the original ordering `XAGC`, the running value before `A` is `x`.  During `A`, values are `x+A_i`.  During `G`, values are `x+a+G_j`.  During `C`, values are `x+a+g+C_k`.

In the moved ordering `XACG`, values during `A` are still `x+A_i`.  During `C`, values are `x+a+C_k`, which are the old `C`-internal values translated by `-g`.  During `G`, values are `x+a+c+G_j=x+G_j`, while old `G`-internal values were `x+a+G_j`; hence `G`-internal values are translated by `-a=c`.

The total displayed segment sum is

```text
a+g+c=g
```

both before and after, so all later partial sums are unchanged.  ∎

---

## Lemma A26.4: exact obstruction criterion for two-piece zero gap relocation

With the notation of Lemma A26.3, the move

```text
X A G C Y -> X A C G Y
```

can fail Graham-validity only through a collision involving one of the changed internal partial sums:

```text
x+a+C_k
```

or

```text
x+G_j.
```

It can create or preserve a forbidden hit `f` only if one of those changed values equals `f`, or if an unchanged value was already `f`.

### Proof

By Lemma A26.3, the only changed partial sums are internal values of `C` and internal values of `G`.  All other partial sums are unchanged.  Therefore any new collision or forbidden hit must involve the displayed changed values.  ∎

---

# 3. Separated signed composites

A separated signed composite has the form

```text
sum(A)=-sum(C)
```

for two separated intervals.  This is the same algebraic object as a two-piece zero composite.

## Lemma A26.5: separated signed composites are two-piece zero composites

If two separated intervals `A` and `C` satisfy

```text
sum(A)=-sum(C),
```

then

```text
sum(A)+sum(C)=0.
```

Thus every separated signed residual can be treated by Lemmas A26.2--A26.4.

### Proof

Immediate.  ∎

---

# 4. Midpoint branches

Adjacent equal intervals produce midpoint relations.

If

```text
sum(x,y]=sum(y,v],
```

then

```text
2S_y=S_x+S_v.
```

The following observation records when the midpoint branch collapses.

## Lemma A26.6: midpoint branch collapses when an endpoint equals the midpoint partial sum

Assume

```text
2S_y=S_x+S_v.
```

If `S_x=S_y` or `S_v=S_y`, then Graham-validity forces the corresponding endpoints to be equal, contradicting the strict adjacency geometry unless the interval is empty.

### Proof

If `S_x=S_y`, then `sum(x,y]=0`.  If `x>=1`, this is an interior zero-sum interval, impossible in a Graham-valid ordering.  If `x=0`, it is a prefix-zero branch.  The case `S_v=S_y` similarly gives `sum(y,v]=0`, an interior zero interval because `y>=1`.  ∎

### Status

General midpoint branches remain residual.  They probably require a two-point swap or averaging argument over `F_p`, using odd characteristic.

---

# 5. Weighted signed overlap/nesting

A20 showed that signed overlap/nesting produces weighted relations such as

```text
sum(A)+2sum(B)+sum(C)=0.
```

The coefficient `2` is the main obstruction to immediate zero-block surgery.

## Lemma A26.7: weighted signed relation becomes a two-piece zero if the middle block is zero

If

```text
sum(A)+2sum(B)+sum(C)=0
```

and

```text
sum(B)=0,
```

then

```text
sum(A)+sum(C)=0.
```

If `B` is an interior interval of a Graham-valid ordering, the hypothesis `sum(B)=0` is impossible.  If `B` is a prefix interval, this is a prefix-zero branch.

### Proof

Substitute `sum(B)=0`.  The Graham-validity statement follows from the standard no-interior-zero-interval lemma.  ∎

## Lemma A26.8: weighted signed relation becomes midpoint-type if outer pieces are equal

If

```text
sum(A)+2sum(B)+sum(C)=0
```

and

```text
sum(A)=sum(C),
```

then

```text
sum(A)+sum(B)=0.
```

### Proof

Substitute `sum(C)=sum(A)`:

```text
2sum(A)+2sum(B)=0.
```

For odd prime `p`, divide by `2` to obtain

```text
sum(A)+sum(B)=0.
```

For `p=2`, the problem is trivial or handled separately in finite verification.  ∎

### Status

This gives a collapse only when an additional equality of outer pieces is available.  Otherwise weighted signed branches remain genuine residuals.

---

# 6. Updated residual priority

After A26, the residual classes should be treated as follows.

## Controlled descent class

```text
reduction_equal_outer_pieces
```

This class strictly lowers total span and should be iterated until terminal.

## Zero-composite classes reducible to A9-style exposed zero blocks

```text
residual_two_piece_zero
residual_separated_signed
```

These can be contiguized by moving the gap, but the resulting exposed zero block must then be repaired using A9 relocation/descent.

## Still hard classes

```text
residual_signed_overlap_weighted
residual_signed_nested_weighted
residual_midpoint
residual_separated_equal
residual_shared_left_signed
residual_shared_right_signed
```

These require new arguments.

---

## Target A27

The next useful tool should implement a descent/normalization pass for residual interval traps:

1. repeatedly apply equal-outer-piece descent until terminal;
2. detect two-piece zero composites and convert them to a standard `A G C` relocation object;
3. leave midpoint and weighted signed branches as named residuals.

This will separate controlled reductions from genuinely hard classes.

---

## Current status

Proved here:

1. equal-outer-piece reduction strictly lowers total span;
2. two-piece zero composites can be contiguized by moving the gap;
3. exact gap-relocation partial-sum formula;
4. separated signed composites are two-piece zero composites;
5. elementary midpoint collapse cases;
6. elementary weighted signed collapse cases.

Not proved here:

1. relocation always succeeds;
2. midpoint branch elimination;
3. weighted signed branch elimination;
4. endpoint avoidance theorem.
