# Analytic separated equal-interval surgery A36

This note continues from A35.

A35 identified separated equal intervals as one of the clean remaining hard residual classes.  This note computes the standard surgery formulas for a segment

```text
X A G C Y
```

with

```text
sum(A)=sum(C).
```

The goal is not to claim closure.  The goal is to show exactly where separated equal-interval surgery routes: midpoint, two-piece zero, weighted signed, prefix-zero, or smaller equal-interval structure.

---

## Standing setup

Let an ordering contain a displayed segment

```text
X A G C Y
```

where

```text
a=sum(A),
g=sum(G),
c=sum(C)=a.
```

Let

```text
x=sum(X).
```

Internal prefix sums are denoted by

```text
A_i,
G_j,
C_k,
Y_m.
```

The original displayed-region partial sums are

```text
x+A_i,
x+a+G_j,
x+a+g+C_k,
x+2a+g+Y_m.
```

---

# 1. Direct exchange of equal intervals

The most natural move is to exchange the two equal-sum blocks:

```text
X A G C Y  ->  X C G A Y.
```

Because `sum(A)=sum(C)`, the total displayed segment is unchanged.

---

## Lemma A36.1: direct exchange partial-sum formula

In the exchanged ordering

```text
X C G A Y,
```

the displayed-region partial sums are

```text
x+C_k,
x+a+G_j,
x+a+g+A_i,
x+2a+g+Y_m.
```

Thus:

1. the `G` family is unchanged;
2. the `Y` family is unchanged;
3. the `A` and `C` internal families swap their translation levels.

### Proof

Direct summation.  Since `sum(C)=a`, after `C` the running value is `x+a`, so the `G` family is `x+a+G_j`, the same as before.  After `CG`, the running value is `x+a+g`, so the following `A` family is `x+a+g+A_i`.  The endpoint after `CGA` is `x+2a+g`, the same as after `AGC`.  ∎

---

## Lemma A36.2: exact collision obstruction list for direct exchange

Assume the original ordering is Graham-valid.  The direct exchange `XAGCY -> XCGAY` can create a new collision only through one of the changed families:

```text
x+C_k,
x+a+g+A_i.
```

The possible new collision equations are:

### New C-family against unchanged G/Y families

```text
x+C_k = x+a+G_j,
x+C_k = x+2a+g+Y_m.
```

Equivalently:

```text
C_k = a+G_j,
C_k = 2a+g+Y_m.
```

### New A-family against unchanged G/Y families

```text
x+a+g+A_i = x+a+G_j,
x+a+g+A_i = x+2a+g+Y_m.
```

Equivalently:

```text
A_i = G_j-g,
A_i = a+Y_m.
```

### New C-family against new A-family

```text
x+C_k = x+a+g+A_i,
```

or

```text
C_k = a+g+A_i.
```

Internal collisions inside translated `A` or `C` families are inherited from old internal prefix collisions.

### Proof

Only the translated locations of the `A` and `C` internal families change.  Pairing those changed families with unchanged families and with each other gives the full list.  ∎

---

## Lemma A36.3: exact forbidden-hit obstruction list for direct exchange

Let `f` be the forbidden value.  If unchanged families avoid `f`, the direct exchange can hit `f` only if

```text
x+C_k=f,
x+a+g+A_i=f.
```

Equivalently:

```text
C_k=f-x,
A_i=f-x-a-g.
```

### Proof

Only the new translated `C` and `A` internal families can create a new forbidden hit.  ∎

---

# 2. Gap move: making the equal intervals adjacent

Another natural move is to move the gap after `C`:

```text
X A G C Y -> X A C G Y.
```

This makes the equal-sum intervals adjacent but does not make a zero block.  Instead, the adjacent block `AC` has sum

```text
2a.
```

---

## Lemma A36.4: gap-after move partial-sum formula

In the ordering

```text
X A C G Y,
```

the displayed-region partial sums are

```text
x+A_i,
x+a+C_k,
x+2a+G_j,
x+2a+g+Y_m.
```

Compared with the original ordering:

```text
x+A_i,
x+a+G_j,
x+a+g+C_k,
x+2a+g+Y_m,
```

the `A` and `Y` families are unchanged, while the `C` and `G` families are translated.

### Proof

Direct summation.  ∎

---

## Lemma A36.5: gap-after collision equations

The move

```text
X A G C Y -> X A C G Y
```

can create a new collision only through the changed values

```text
x+a+C_k,
x+2a+G_j.
```

The cross-collision equations are:

```text
C_k=A_i-a,
C_k=a+g+Y_m,
G_j=A_i-2a,
G_j=g+Y_m,
C_k=a+G_j.
```

### Proof

Pair the changed `C` and `G` families with unchanged `A`, unchanged `Y`, and with each other.  ∎

---

# 3. Relation to midpoint branch

If the gap is empty, the separated equal-interval relation becomes an adjacent equal-interval relation:

```text
X A C Y,
 sum(A)=sum(C).
```

Then the endpoints satisfy

```text
2S_y=S_x+S_v,
```

where `y` is the common boundary between `A` and `C`.

## Lemma A36.6: midpoint is the zero-gap boundary of separated equal intervals

The adjacent midpoint branch is exactly the boundary case `G=empty` of the separated equal-interval setup.

### Proof

If `G` is empty, the equality `sum(A)=sum(C)` is

```text
S_y-S_x=S_v-S_y,
```

which rearranges to

```text
2S_y=S_x+S_v.
```

∎

### Consequence

Midpoint branches and separated equal intervals should be treated together.  A successful separated-equal surgery theorem should include the adjacent midpoint case as its boundary.

---

# 4. Routing of direct-exchange obstructions

Each obstruction equation from Lemma A36.2 routes to a known class.

## D1: `C_k=a+G_j`

This is

```text
C_prefix = A_total + G_prefix.
```

Equivalently,

```text
sum(A G_j)=C_k.
```

Routed class:

```text
equal-interval relation between A+G_prefix and C_prefix.
```

If `G_j` is proper, the left interval span is smaller than the full `A G C` span.

## D2: `C_k=2a+g+Y_m`

Since `2a+g` is the sum of `A G C`, this relates a prefix of `C` to a post-`C` translated prefix.

Routed class:

```text
signed/equal interval depending on endpoint orientation;
potential old collision if both are old partial sums.
```

## D3: `A_i=G_j-g`

This is

```text
A_i + tail_j(G)=0.
```

Routed class:

```text
two-piece zero composite.
```

If `j<|G|`, this is a proper tail of the gap and usually smaller support.

## D4: `A_i=a+Y_m`

This is

```text
A_i - A_total = Y_m,
```

or

```text
tail_i(A)+Y_m=0.
```

Routed class:

```text
two-piece zero composite.
```

If `i<|A|`, the tail is proper and gives support descent.

## D5: `C_k=a+g+A_i`

This says

```text
C_prefix = A_total + G_total + A_prefix.
```

Routed class:

```text
equal-interval / signed composite relation.
```

This is one of the less trivial residual routes.

---

# 5. Immediate descent/collapse observations

## Lemma A36.7: D3 descends unless the G-tail is empty

For D3:

```text
A_i=G_j-g=-tail_j(G),
```

so

```text
A_i+tail_j(G)=0.
```

If `j<|G|`, then `tail_j(G)` is a proper nonempty tail of the gap, and the two-piece zero support is smaller than the full separated-equal support involving `A,G,C`.

If `j=|G|`, then `tail_j(G)=0`, so D3 gives

```text
A_i=0,
```

which is an interior-zero or prefix-zero branch depending on position.

### Proof

Immediate from `G_j-g=-tail_j(G)`.  ∎

## Lemma A36.8: D4 descends unless the A-tail is empty

For D4:

```text
A_i=a+Y_m,
```

so

```text
tail_i(A)+Y_m=0.
```

If `i<|A|`, this gives a two-piece zero composite with a proper tail of `A`.  If `i=|A|`, then `tail_i(A)=0`, so `Y_m=0`, a zero-prefix/interior-zero branch.

### Proof

Rearrange `A_i-a=Y_m`, i.e. `-tail_i(A)=Y_m`.  ∎

---

# 6. Current status of separated equal intervals

The separated equal branch is now partially routed.

Controlled or descending:

```text
D3 -> two-piece zero with G-tail, endpoint zero collapse;
D4 -> two-piece zero with A-tail, endpoint zero collapse;
midpoint recognized as zero-gap boundary.
```

Still open:

```text
D1 equal-interval relation A+G_prefix = C_prefix;
D2 post-C translated prefix relation;
D5 C_prefix = A+G+A_prefix;
gap-after move obstruction equations;
forbidden-hit recurrences from Lemma A36.3.
```

---

# 7. Target A37

A37 should focus on D1/D5 because they are the cleanest remaining equal-interval recurrences inside separated equal surgery.

Suggested target:

```text
D1/D5 span descent table
```

For each of D1 and D5:

1. rewrite as an interval relation with endpoints;
2. compare total support span to the original separated equal relation;
3. identify endpoint cases that collapse to prefix-zero/interior-zero;
4. identify proper-overlap cases reducible by A26/A27;
5. isolate only the terminal separated/midpoint branches.

---

## Current status

Proved here:

1. direct exchange partial-sum formula;
2. direct exchange collision and forbidden-hit obstruction equations;
3. gap-after move partial-sum and collision equations;
4. midpoint branch is zero-gap boundary of separated equal intervals;
5. D3 and D4 route to controlled two-piece zero/prefix-zero branches.

Not proved here:

1. D1/D2/D5 elimination;
2. gap-after obstruction elimination;
3. forbidden recurrence descent;
4. endpoint avoidance theorem.
