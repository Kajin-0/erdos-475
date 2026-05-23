# Analytic weighted cut-selection A79

This note continues from A78.

A78 closed the non-weighted obstruction graph at the architectural level and isolated the remaining analytic gap:

```text
weighted core cut-selection.
```

The weighted core has form

```text
sum(A)+2sum(B)+sum(C)=0.
```

After A56 reductions fail, the core is genuine:

```text
B != 0,
A+B != 0,
B+C != 0,
A != C,
no transported-prefix/tail rewrite.
```

A58 rewrote this as a nested zero-composite

```text
ABC + B = 0.
```

A59 showed that static cuts of `B` do not automatically close the branch.  A60 showed that once a proper cut

```text
B=P R
```

is chosen, the dynamic cut-swap

```text
A P R C -> A R P C
```

has displayed collisions locally routed.

This note sharpens the cut-selection gap.

Main correction:

```text
A universal proper-cut theorem cannot cover |B|=1.
```

Therefore the weighted branch must split into:

```text
1. atom-middle weighted core: |B|=1;
2. proper middle weighted core: |B|>=2.
```

A79 proves that the proper-middle branch is controlled once any proper cut is allowed, modulo possible return to a smaller weighted core.  The remaining weighted base case is the atom-middle core.

No complete proof is claimed here.

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

Assume the A56 easy reductions fail:

```text
b != 0,
a+b != 0,
b+c != 0,
a != c,
```

and no transported-prefix/tail rewrite applies.

The active weighted measure is

```text
M_W=(|B|, span(A B C), support_size, boundary_rank).
```

The leading coordinate is the middle length `|B|`.

---

# 2. Atom-middle obstruction

If

```text
|B|=1,
```

then no proper nonempty cut

```text
B=P R
```

exists.

Thus the A60 cut-swap mechanism cannot even be applied.

## Lemma A79.1: weighted cut-selection requires `|B|>=2`

A proper cut-selection theorem for

```text
B=P R,
P,R nonempty,
```

can apply only when

```text
|B|>=2.
```

### Proof

A block of length one has no nonempty proper prefix and nonempty proper tail. ∎

### Consequence

The weighted proof cannot be completed solely by A60 cut-swaps.  It also requires a base-case theorem for atom-middle weighted cores:

```text
A + 2q + C = 0,
q atom.
```

---

# 3. Proper-middle cut-swap trichotomy

Assume now

```text
|B|>=2.
```

Choose any proper cut

```text
B=P R,
P,R nonempty.
```

Apply the cut-swap

```text
X A P R C Y -> X A R P C Y.
```

The transformed ordering has three possible outcomes:

```text
1. success: Graham-valid and avoids f;
2. collision: not Graham-valid;
3. recurrence: Graham-valid but hits f.
```

A60 routed displayed collisions.  A62 routes external collisions.  A78 handles non-weighted recurrence and non-weighted collision routing.

---

## Lemma A79.2: any fixed proper cut is useful unless it returns to a genuine weighted core

For a fixed proper cut `B=P R`, the cut-swap outcome is either:

```text
1. success;
2. collapse/contradiction;
3. non-weighted obstruction controlled by A78;
4. forbidden recurrence controlled by the non-weighted recurrence graph unless it returns to WEIGHTED_CORE;
5. a new genuine weighted core.
```

### Proof

A60 routes displayed collisions from the cut-swap to zero-composite, equal/signed interval, or recurrence classes.  A62 routes external collisions to the same interval/composite framework.  A78 terminates the non-weighted graph.  Therefore the only way a fixed cut is not immediately useful is if the routing path enters `WEIGHTED_CORE` again. ∎

### Interpretation

The real weighted problem is not selecting a cut that avoids all obstruction.  Any cut enters the routed graph.  The only dangerous possibility is recurrence into another genuine weighted core.

---

# 4. Smaller weighted core from a cut

Suppose the cut-swap routing returns to a genuine weighted core.

A useful cut-selection theorem should prove that the returned weighted core has smaller middle length than `B`.

The cut

```text
B=P R
```

creates two candidate smaller middle blocks:

```text
P,
R.
```

If a returned weighted relation doubles only `P` or only `R`, then `M_W` strictly decreases.

---

## Lemma A79.3: cut-local weighted returns with doubled P or doubled R descend

If a cut-swap obstruction returns to a genuine weighted relation whose doubled middle block is contained in either `P` or `R`, then

```text
|B_new| < |B|.
```

Therefore the weighted measure `M_W` decreases.

### Proof

Since `P` and `R` are both nonempty proper subblocks of `B`, each has length strictly smaller than `|B|`. ∎

---

## Lemma A79.4: a non-descending weighted return must double material crossing the cut

If a cut-swap obstruction returns to a genuine weighted core with middle length not smaller than `|B|`, then its doubled middle block cannot be contained wholly in `P` or wholly in `R`.  It must cross the cut between `P` and `R`, or include material outside `B`.

### Proof

Contrapositive of Lemma A79.3. ∎

### Consequence

A non-descending weighted return is highly constrained: the doubled part must straddle the very cut being swapped, or absorb external material.  Such a return is not an arbitrary weighted core.

---

# 5. All-cuts failure pattern

Assume every proper cut fails to produce success, collapse, non-weighted termination, or a smaller weighted core.

Then by Lemma A79.4, for every cut

```text
B=P R,
```

any returned genuine weighted core must have doubled middle crossing the cut or involving external material.

This implies a strong rigidity condition.

## Definition A79.5: cut-rigid weighted core

A genuine weighted core is cut-rigid if for every proper cut

```text
B=P R,
```

the A60 cut-swap routes back, if at all, only to weighted cores whose doubled middle crosses the cut or includes external material, never to a doubled middle contained in `P` or `R`.

---

## Lemma A79.6: cut-rigidity forces every adjacent cut of B to be crossing-rigid

It is enough to check adjacent cuts

```text
B = B_{<i} B_{3i}
```

or equivalently cuts between consecutive atoms of `B`.

If any adjacent cut returns a weighted core doubled on one side, then weighted descent occurs.  Therefore a cut-rigid weighted core must be crossing-rigid at every internal boundary of `B`.

### Proof

Every proper cut is a union of adjacent internal cuts.  In particular, if a descent exists for any proper prefix/tail split, it exists for an adjacent boundary.  Thus failure for all cuts implies failure for each adjacent cut. ∎

---

# 6. Consequence of adjacent crossing-rigidity

Let

```text
B=b_1 b_2 ... b_n,
n>=2.
```

For each internal cut after `b_i`, a non-descending weighted return must have a doubled middle that crosses that cut.

A single returned doubled interval cannot cross all cuts unless it contains all of `B`.

Thus if every cut returns the same non-descending weighted core, the doubled middle must be `B` itself.

---

## Lemma A79.7: common non-descending return forces the same doubled middle B

Suppose the same weighted core is returned for every adjacent cut of `B`, and suppose no returned doubled middle is smaller than `B`.  Then the doubled middle of the returned core contains all of `B`.

If the returned core has the same support size as the original, its doubled middle is exactly `B`.

### Proof

To cross every internal cut of `B`, an interval must contain atoms on both sides of every cut.  Hence it contains all atoms of `B`.  If support size is unchanged, it cannot properly contain `B` plus outside atoms, so it is exactly `B`. ∎

### Interpretation

The worst case is a true self-return of the same weighted core, analogous to the rigid separated self-return from A77.

---

# 7. Weighted self-return

A weighted self-return would mean that after a cut-swap and routing, the exact same genuine weighted core

```text
A + 2B + C = 0
```

reappears with the same middle block `B`.

For a fixed cut `B=P R`, the move is

```text
A P R C -> A R P C.
```

If the same core reappears, the operation must effectively undo itself or route through a direct exchange of `P` and `R`.

But the swapped order has middle block

```text
R P,
```

not

```text
P R.
```

Thus same-core return requires either:

```text
1. the cut-swap is reversed by recurrence/collision pullback;
2. P and R have equal-sum structure allowing a separated-equal or midpoint branch;
3. internal zero-composite collapse inside B;
4. a cyclic rotation of B preserving the weighted relation.
```

---

## Lemma A79.8: weighted self-return forces internal structure in B

If a cut-swap at `B=P R` returns to the same weighted core with middle block `B=P R`, then at least one of the following must occur:

```text
1. sum(P)=0 or sum(R)=0;
2. sum(P)=sum(R);
3. sum(A P)=0 or sum(R C)=0;
4. the return is a cyclic recurrence inside B;
5. the return is an exact two-step reversal of the cut-swap.
```

### Proof sketch

A60 collision equations for the cut-swap are all of the form:

```text
tail(A)+R+prefix(P)=0,
tail(P)+prefix(C)=0,
P+tail(R)+prefix(C)=0,
tail(R)+prefix(P)=0,
```

or bridge variants.  For the exact same middle block `P R` to be restored after `R P`, the obstruction must identify a boundary relation between `P` and `R`, or move through a bridge/cyclic reversal.  The listed alternatives are precisely the zero/equal/cyclic possibilities at the cut boundary. ∎

### Status

This lemma is structural, not a complete proof.  It shows that all-cuts failure should force A56 easy reductions or cyclic recurrence inside `B`.

---

# 8. Partial cut-selection theorem

## Theorem A79.9: proper-middle weighted core reduces unless it is cut-rigid or atom-middle

Let

```text
A+2B+C=0
```

be a genuine weighted core with

```text
|B|>=2.
```

Then for any proper cut `B=P R`, the A60 cut-swap either:

```text
1. succeeds;
2. collapses;
3. routes into the non-weighted acyclic graph A78;
4. returns to a genuine weighted core with smaller middle length;
5. or participates in a cut-rigid weighted self-return.
```

Thus the only weighted cases not yet controlled are:

```text
atom-middle weighted core |B|=1;
cut-rigid weighted self-return for |B|>=2.
```

### Proof

For a fixed cut, use Lemma A79.2.  If a returned weighted core has middle inside `P` or `R`, Lemma A79.3 gives descent.  If no cut gives such descent, the core is cut-rigid by Definition A79.5.  If the returned core is common across all cuts and non-descending, Lemma A79.7 identifies the self-return structure. ∎

---

# 9. Implications for the proof program

A79 refines the weighted gap.  The missing theorem is no longer simply:

```text
there exists a useful cut.
```

It is now split into two sharper base problems:

```text
W-base. atom-middle weighted core A+2q+C=0;
W-rigid. cut-rigid weighted self-return for |B|>=2.
```

If both are eliminated, then weighted core cut-selection follows by induction on `|B|`.

---

# 10. Target A80

A80 should attack the atom-middle weighted core:

```text
A + 2q + C = 0.
```

Key observations:

```text
A+q and q+C are both nonzero by A56;
A != C;
q != 0;
ABC+q=0 gives A q C + q = 0.
```

Potential moves:

```text
1. swap q with first atom of C;
2. swap q with last atom of A;
3. move q outside A C and compare midpoint equations;
4. use odd characteristic to write q=-(A+C)/2;
5. test whether atom-middle implies midpoint boundary for endpoints around q.
```

Expected routes:

```text
pair-difference boundary,
midpoint branch,
two-piece zero,
singleton recurrence,
non-weighted acyclicity.
```

---

## Current status

Proved/refined here:

1. proper-cut selection cannot cover |B|=1;
2. any fixed proper cut is useful unless it returns to WEIGHTED_CORE;
3. weighted returns with doubled middle inside P or R strictly descend in middle length;
4. all-cuts failure forces cut-rigidity;
5. common non-descending all-cuts return forces weighted self-return;
6. weighted gap splits into atom-middle and cut-rigid self-return.

Not proved here:

1. atom-middle weighted core elimination;
2. cut-rigid weighted self-return contradiction;
3. final endpoint avoidance theorem.
