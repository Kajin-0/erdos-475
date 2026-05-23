# Analytic cut-rigid weighted self-return A82

This note continues from A81.

A79 split the weighted obstruction into two problems:

```text
W-base: atom-middle weighted core |B|=1;
W-rigid: cut-rigid weighted self-return for |B|>=2.
```

A80--A81 eliminated the atom-middle base case modulo the non-weighted acyclic graph A78.

This note attacks the remaining weighted case:

```text
cut-rigid weighted self-return for |B|>=2.
```

The result is partial but sharp.  It proves that any non-descending cut-rigid return must preserve the entire middle block `B` across every internal cut.  This forces the return to be an internal cyclic or reversal symmetry of `B`.  Non-symmetric returns descend to a smaller weighted core or route to non-weighted machinery.

No complete endpoint-avoidance proof is claimed here.

---

## 1. Standing weighted core

Let the displayed segment be

```text
X A B C Y
```

with block sums

```text
a=sum(A),
b=sum(B),
c=sum(C).
```

The genuine weighted core is

```text
a+2b+c=0.
```

Assume all A56 easy reductions fail:

```text
b != 0,
a+b != 0,
b+c != 0,
a != c,
no transported-prefix/tail rewrite.
```

Assume also

```text
|B|>=2.
```

Write a proper cut as

```text
B=P R,
P,R nonempty.
```

The A60 cut-swap is

```text
A P R C -> A R P C.
```

A cut-rigid weighted self-return means that for every proper cut, the cut-swap and its routed obstruction process does not give success, collapse, non-weighted termination, or a smaller weighted core.  Instead, it returns to a genuine weighted core whose doubled middle is not shorter than `B`.

---

## 2. Cut-rigidity recap

A79 proved:

```text
If a returned weighted core doubles only P or only R,
then the weighted middle length strictly decreases.
```

Therefore a non-descending return for the cut `B=P R` must have a doubled middle that crosses the cut or contains material outside `B`.

---

## Lemma A82.1: non-descending return crosses the active cut

For a cut-rigid weighted self-return at the cut `B=P R`, the returned doubled middle cannot be contained in `P` or `R`.  It must cross the cut or contain all of `P R` plus outside material.

### Proof

If the returned doubled middle is contained in `P` or `R`, A79.3 gives strict decrease of the leading weighted measure coordinate `|B|`.  That contradicts cut-rigidity. ∎

---

## 3. Adjacent cut forcing

Write

```text
B=b_1 b_2 ... b_n,
n>=2.
```

Consider the adjacent cut after `b_i`:

```text
P_i=b_1...b_i,
R_i=b_{i+1}...b_n.
```

A non-descending return must cross every adjacent cut.

---

## Lemma A82.2: crossing every adjacent cut forces containment of all of B

If an interval block `M` intersects both sides of every adjacent cut of `B`, then `M` contains all atoms of `B`.

### Proof

For each cut after `b_i`, crossing means `M` contains at least one atom among `b_1,...,b_i` and at least one atom among `b_{i+1},...,b_n`.  If some atom `b_j` were missing from `M`, then an interval `M` either lies entirely to the left of `b_j`, entirely to the right, or skips an atom, impossible for an interval.  More directly, an interval crossing the first cut contains atoms on both sides of `b_1|b_2...b_n`; crossing the last cut contains atoms on both sides of `b_1...b_{n-1}|b_n`; interval convexity then forces every intermediate atom. ∎

---

## Lemma A82.3: cut-rigid all-cuts return has doubled middle containing B

If a weighted core is cut-rigid for every adjacent cut of `B`, then every common non-descending returned doubled middle contains all of `B`.

### Proof

Apply Lemma A82.1 to each adjacent cut and then Lemma A82.2. ∎

---

# 4. Outside-material alternatives

If the returned doubled middle properly contains `B`, then it must include material from `A`, `C`, or external bridge material.

There are three cases:

```text
M = A_tail B,
M = B C_prefix,
M = A_tail B C_prefix.
```

or variants involving external bridge material after a transformed move.

These are not true self-returns of the same weighted core; they are larger-middle returns.

---

## Lemma A82.4: returned middle properly containing B creates transported-prefix or adjacent-pair zero tests

If a returned genuine weighted core has doubled middle `M` properly containing `B`, then one of the following occurs:

```text
1. the added left material combines with A to form a transported-prefix/tail rewrite;
2. the added right material combines with C to form a transported-prefix/tail rewrite;
3. an adjacent-pair zero relation A+B=0 or B+C=0 appears after subtracting the original weighted equation;
4. the returned core has strictly larger support and must have arisen from an external bridge, hence routes by A62/A74--A78 unless it reduces back to separated-equal recurrence.
```

### Proof sketch

Compare the original equation

```text
a+2b+c=0
```

with the returned equation

```text
a'+2m+c'=0,
```

where `m=b+d` and `d` is the added material.  Subtracting gives

```text
(a'-a)+2d+(c'-c)=0.
```

If `d` is adjacent prefix/tail material from `A` or `C`, this is exactly the transported-prefix coefficient-2 pattern of A56.  If the added material is not adjacent, it is an external bridge/signed interval branch.  If the returned support is not larger, the only way to absorb `d` is through an adjacent zero/equal relation. ∎

### Consequence

A true cut-rigid self-return cannot have a strictly larger middle unless it routes out of the genuine weighted class by A56 or into the non-weighted acyclic graph A78.

---

# 5. Exact-middle self-return

Thus the only remaining rigid case is exact-middle self-return:

```text
returned doubled middle = B.
```

The cut-swap changes the internal order of `B` from

```text
P R
```

to

```text
R P.
```

For the returned doubled middle to be exactly `B=P R`, the routing must restore the original internal order or identify a cyclically equivalent internal order.

---

## Definition A82.5: exact weighted self-return

An exact weighted self-return is a cut-rigid return in which the returned weighted core is

```text
A + 2B + C = 0
```

with the same outer blocks and the same middle block `B`, after the cut-swap at `B=P R`.

---

## Lemma A82.6: exact self-return at a cut requires internal reversal/cyclic return of B

For the cut `B=P R`, the cut-swap gives internal middle order `R P`.  If the returned weighted core has middle `P R` again, then the routed process must contain either:

```text
1. a direct reversal of the cut-swap R P -> P R;
2. a cyclic rotation of B identifying R P with P R under a basepoint change;
3. an internal equality/zero-composite inside B allowing P and R to commute at the level of partial sums;
4. a midpoint/equal-interval boundary between P and R.
```

### Proof sketch

The atom order is changed only by transposing the two consecutive blocks `P` and `R`.  To restore the original middle block without moving material outside `B`, the process must undo that transposition, rotate the middle block cyclically, or make the distinction between `P R` and `R P` irrelevant through an internal equality/zero relation. ∎

---

# 6. Internal equality and zero cases

If `P` and `R` interact nontrivially, the weighted core leaves the genuine rigid case.

## Lemma A82.7: if sum(P)=0 or sum(R)=0, cut-rigidity collapses

If

```text
sum(P)=0
```

or

```text
sum(R)=0,
```

then there is a zero-prefix/interior-zero branch inside `B`, contradicting Graham-validity or routing to collapse.

### Proof

`P` and `R` are nonempty blocks.  A zero-sum nonempty block gives repeated partial sums. ∎

---

## Lemma A82.8: if sum(P)=sum(R), cut-rigidity routes to midpoint/separated-equal machinery

If

```text
sum(P)=sum(R),
```

then the middle block `B=P R` contains adjacent equal-sum blocks.  This is the zero-gap midpoint/adjacent-equal branch A55 inside `B`.

### Proof

The two equal blocks are adjacent.  A55 applies to adjacent equal blocks. ∎

---

## Lemma A82.9: if P+R has an internal two-piece zero, cut-rigidity routes to zero-composite surgery

If there exist nonempty internal pieces `P0` and `R0` on opposite sides of the cut with

```text
sum(P0)+sum(R0)=0,
```

then the branch enters two-piece zero-composite surgery A28--A33 and hence the non-weighted acyclic graph A78.

### Proof

This is exactly a two-piece zero composite supported strictly inside `B` or across its cut boundary. ∎

---

# 7. Cyclic internal return

The difficult exact self-return alternative is an internal cyclic recurrence of `B`.

The cut-swap

```text
P R -> R P
```

is exactly a cyclic rotation of the block `B` by the cut after `P`.

Thus exact weighted self-return across all cuts implies that every cyclic rotation of `B` is recurrent or blocked in a way that restores the same weighted core.

---

## Lemma A82.10: cut-swap on B is internal cyclic rotation of B

For every cut

```text
B=P R,
```

the swapped middle

```text
R P
```

is the cyclic rotation of `B` based at the cut after `P`.

### Proof

Immediate from the definition of cyclic rotation. ∎

---

## Lemma A82.11: exact all-cuts self-return implies internal cyclic rigidity of B

If exact weighted self-return occurs for every proper cut of `B`, then every nontrivial cyclic rotation of `B` is either:

```text
1. blocked by an internal zero/equal/pair obstruction inside B;
2. recurrent and routed by cyclic-cut machinery A71;
3. restores the same weighted core with identical outer blocks.
```

### Proof

Use Lemma A82.10 for each cut.  The cut-swap is exactly the internal cyclic rotation.  A60/A62 route collisions; A71 routes cyclic recurrence.  If neither collision nor recurrence routes out, exact self-return means the same weighted core is restored. ∎

---

# 8. Internal cyclic rigidity forces either constant cyclic sums or smaller obstruction

For a block `B` with nonzero total `b`, not every cyclic rotation can preserve all internal partial-sum obstruction data unless the internal partial sums of `B` have a symmetry.

That symmetry yields equal intervals inside `B`.

## Lemma A82.12: nontrivial internal cyclic symmetry of B gives an internal equal-interval branch

If two distinct cyclic rotations of `B` produce the same internal partial-sum pattern relative to the same outer blocks, then `B` contains two nonempty intervals with equal sum, or a nonempty zero interval.

### Proof sketch

Equality of internal partial-sum patterns means there exist two endpoints in `B` whose translated partial sums coincide under different basepoints.  Subtracting the endpoint equations gives either zero sum over the interval between the two endpoints or equality of two separated subinterval sums. ∎

### Status

This routes to zero collapse, equal-interval, separated-equal, or midpoint machinery, all non-weighted by A78.

---

# 9. Cut-rigid weighted theorem, partial

## Theorem A82.13: cut-rigid weighted self-return reduces to internal cyclic rigidity

Let

```text
A+2B+C=0,
|B|>=2,
```

be a genuine weighted core after A56 reductions and after atom-middle elimination A81.

If the core is cut-rigid, then one of the following holds:

```text
1. a returned weighted core has smaller middle length;
2. the branch routes to transported-prefix, zero-composite, equal/signed interval, midpoint, pair-difference, singleton/cyclic recurrence, or other non-weighted machinery;
3. an atom-middle weighted core appears at a boundary and is eliminated by A81;
4. B is internally cyclic-rigid: every nontrivial cyclic rotation of B preserves the same weighted core without producing an internal equal/zero obstruction.
```

Thus the only remaining weighted tie is internal cyclic rigidity of the middle block `B`.

### Proof

For each cut, Lemmas A82.1--A82.4 handle smaller-middle and outside-material returns.  Exact-middle returns are Lemma A82.6.  Internal zero/equal cases route by Lemmas A82.7--A82.9.  Since cut-swap is cyclic rotation by Lemma A82.10, all-cuts exact self-return gives Lemma A82.11.  Any nontrivial cyclic symmetry with endpoint coincidence routes by Lemma A82.12.  The only remaining case is internal cyclic rigidity without visible equal/zero obstruction. ∎

---

# 10. Remaining weighted tie

After A82, the weighted problem is narrowed to:

```text
internal cyclic rigidity of B.
```

This means:

```text
B has length >=2,
B has no internal zero interval,
B has no internal equal-interval/midpoint obstruction,
every nontrivial cyclic rotation of B is blocked/recurrent but restores the same weighted core.
```

This is a strong finite combinatorial condition on the internal partial sums of `B`.

---

# 11. Target A83

A83 should attack internal cyclic rigidity of `B`.

Potential route:

1. Treat `B` as a standalone Graham-valid block with nonzero total `b`.
2. Study all cyclic rotations of `B`.
3. Show that if every rotation preserves the same external weighted relation

```text
A + 2B + C = 0,
```

then either:

```text
B has an internal zero interval,
B has two equal internal intervals,
B has an atom-middle boundary core,
or B has all atoms equal under translation, impossible for distinct subset atoms.
```

A finite verification script may also be useful here: search for blocks `B` with no zero/equal internal intervals but cyclic-rigid partial-sum structure.

---

## Current status

Proved/refined here:

1. non-descending weighted returns must cross every cut;
2. crossing every adjacent cut forces returned middle to contain all of B;
3. larger-middle returns route to transported-prefix/external/non-weighted mechanisms;
4. exact-middle returns are internal cyclic rotations of B;
5. internal zero/equal cases route to non-weighted acyclicity;
6. remaining weighted tie is internal cyclic rigidity of B.

Not proved here:

1. internal cyclic rigidity elimination;
2. final endpoint avoidance theorem;
3. finite verification bridge.
