# Analytic cyclic-cut recurrence A71

This note continues from A70.

A68--A70 routed the atom-insertion, pair-difference, and singleton-prefix recurrence sources into existing mechanisms.  The remaining recurrence source from A34 is cyclic-cut recurrence.

Cyclic-cut recurrence occurs when a rotation or cyclic basepoint change produces a Graham-valid ordering that still hits the forbidden value `f`, with no earlier hit.  Earlier cyclic-cut notes isolated special hits such as

```text
S_alpha=2f,
S_beta=2f-sigma.
```

This note gives a recurrence routing framework for cyclic cuts.  It is not a final termination proof, but it reduces cyclic recurrence to midpoint/separated-equal, bridge zero-composite, singleton-prefix recurrence, or A34/global termination.

---

## 1. Standing setup

Let an ordering be

```text
R=(r_1,...,r_t)
```

with partial sums

```text
S_i=r_1+...+r_i,
S_0=0,
S_t=sigma.
```

Assume

```text
S_h=f
```

is the first forbidden hit in a minimal counterexample, with

```text
f != sigma.
```

A cyclic cut at index `c` produces the rotated ordering

```text
R_c=(r_{c+1},...,r_t,r_1,...,r_c).
```

The partial sums of the rotated ordering are old partial sums translated by `-S_c` for the suffix, and by `sigma-S_c` for the wrapped prefix.

---

## 2. Cyclic partial-sum formula

## Lemma A71.1: rotated partial sums are translated old partial sums

For the cyclic cut at `c`, the rotated partial sums are:

For endpoints originally after `c`, i.e. `i>c`,

```text
S_i-S_c.
```

For wrapped endpoints originally at `i<=c`,

```text
sigma-S_c+S_i.
```

### Proof

The rotated ordering starts at endpoint `c`.  Suffix partial sums subtract the base value `S_c`.  After reaching the final endpoint, the accumulated value is `sigma-S_c`; wrapped prefix endpoints add `S_i`. ∎

---

## 3. Forbidden hit equations after rotation

A rotated forbidden hit can occur in two ways.

### Suffix hit

For some `i>c`,

```text
S_i-S_c=f.
```

Equivalently,

```text
S_i=S_c+f.
```

### Wrapped hit

For some `i<=c`,

```text
sigma-S_c+S_i=f.
```

Equivalently,

```text
S_i=S_c+f-sigma.
```

These are translated endpoint equations.

---

## Lemma A71.2: cyclic forbidden hits are translated endpoint-pair equations

Every forbidden hit after a cyclic cut is equivalent to one of:

```text
S_i-S_c=f,
S_i-S_c=f-sigma.
```

Thus cyclic recurrence is controlled by pairs of old endpoints whose difference is either `f` or `f-sigma`.

### Proof

Immediate from Lemma A71.1. ∎

---

## 4. Special self-hit equations

The special equations from earlier cyclic-cut analysis arise when one of the endpoints involved is the original first forbidden hit `h`, so `S_h=f`.

### Case 1: suffix self-hit

If `i=h` and `h>c`, the rotated suffix value is

```text
S_h-S_c=f-S_c.
```

For this to equal `f`, one needs

```text
S_c=0,
```

which is a prefix-zero/interior-zero collapse unless `c=0`.

### Case 2: wrapped self-hit

If `i=h` and `h<=c`, the rotated wrapped value is

```text
sigma-S_c+f.
```

For this to equal `f`, one needs

```text
S_c=sigma,
```

which means the interval `(c,t]` is zero, again a zero-collapse branch unless `c=t`.

Thus the original first hit itself does not normally persist under a nontrivial cyclic cut without a zero interval.

---

## Lemma A71.3: persistence of the same forbidden endpoint under nontrivial rotation forces zero collapse

If the old endpoint `h` remains a forbidden endpoint after a nontrivial cyclic rotation, then either

```text
S_c=0
```

or

```text
S_c=sigma.
```

Both give zero-prefix/interior-zero collapse branches.

### Proof

As above. ∎

---

## 5. The `2f` special hit

The equation

```text
S_c=2f
```

appears when the cut translates an old endpoint with value `S_i=f+S_c` or when the complementary translated value hits `f` symmetrically around `f`.

A clean way to express this is midpoint geometry.

If two endpoints satisfy

```text
S_i+S_j=2f,
```

then `f` is the midpoint of the two partial sums.

For `S_j=0`, this is `S_i=2f`.  For `S_j=sigma`, the wrapped analog becomes `S_i=2f-sigma`.

---

## Lemma A71.4: cyclic special hits are midpoint boundary equations

The cyclic special equations

```text
S_alpha=2f,
S_beta=2f-sigma
```

are endpoint-midpoint equations:

```text
2f=S_alpha+S_0,
2f=S_beta+S_t.
```

Therefore they route to the midpoint boundary framework A55.

### Proof

The first identity is immediate from `S_0=0`.  The second is immediate from `S_t=sigma`. ∎

### Status

A55 routed midpoint displayed collisions to zero-composite classes and forbidden hits to A34 recurrence.  Thus these special cyclic hits are not a separate local species.

---

## 6. A5 blocker after cyclic recurrence

Assume a cyclic cut gives a Graham-valid rotated ordering that still hits `f`, not earlier than the minimal first-hit index.

By A64, A5 applies at the recurrent hit.  The transformed A5 blocker is an interval in the rotated cyclic order.

Pulling this blocker back to the original linear order gives either:

```text
1. a non-wrapping interval blocker;
2. a wrapping interval blocker crossing the cyclic cut.
```

---

## Lemma A71.5: non-wrapping cyclic blockers reduce to ordinary interval/composite branches

If the A5 blocker interval in the rotated ordering does not cross the cyclic cut when pulled back to the original ordering, then it is an ordinary contiguous interval/atom zero-composite or signed interval branch.

### Proof

Without crossing the cyclic cut, the rotated interval is also contiguous in the original ordering, up to translation by the cut basepoint.  Equality of transformed partial sums gives zero sum over that interval plus the A5 adjacent atom, as in A64.2. ∎

### Status

This routes to zero-composite or signed/equal interval machinery.

---

## Lemma A71.6: wrapping cyclic blockers split into two bridge pieces

If the transformed A5 blocker interval crosses the cyclic cut, then its pullback to the original ordering is a union of two bridge intervals:

```text
right bridge after c  +  left bridge before c,
```

plus the A5 adjacent atom or pair-difference correction.

Thus it is a two-piece bridge zero-composite or signed composite.

### Proof

A contiguous interval in the rotated order that crosses the rotation endpoint corresponds in the original order to a suffix interval after `c` plus a prefix interval before or at `c`.  The A5 atom term is preserved. ∎

### Status

This routes to the external-collision lemma A62, singleton-prefix recurrence A70, or separated-equal bridge machinery depending on orientation.

---

## 7. Earlier-hit criterion for rotations

A cyclic rotation can sometimes produce an earlier forbidden hit simply by placing a shorter suffix/prefix endpoint before the old `h` in the rotated order.

## Lemma A71.7: cyclic recurrence only matters when every rotated forbidden endpoint lies at position at least h

If a cyclic cut produces any forbidden endpoint at rotated index `<h`, then the minimality of `h` is contradicted.  Therefore a cyclic recurrence branch must have all rotated forbidden endpoints at positions `>=h`.

### Proof

The rotated ordering is Graham-valid by recurrence assumption.  An earlier forbidden hit would contradict the global minimal choice of `h`. ∎

### Consequence

This imposes a strong positional constraint on cyclic recurrence: all endpoint-pair equations from Lemma A71.2 must occur late in the rotated order.  This is a global condition and belongs to the final termination theorem.

---

## 8. Cyclic recurrence routing theorem

## Proposition A71.8: cyclic-cut recurrence introduces no new local algebraic species

Every cyclic-cut recurrence branch routes to one of:

```text
1. zero-prefix/interior-zero collapse;
2. midpoint boundary A55;
3. ordinary interval/zero-composite branch;
4. wrapping bridge zero-composite or signed composite;
5. singleton-prefix recurrence A70;
6. A34/global termination.
```

### Proof

Rotated forbidden hits are endpoint-pair equations by Lemma A71.2.  Persistence of the old hit gives zero collapse by Lemma A71.3.  Special `2f` and `2f-sigma` hits are midpoint equations by Lemma A71.4.  A5 blockers after recurrence are non-wrapping or wrapping; these are routed by Lemmas A71.5--A71.6.  Earlier rotated hits contradict minimality by Lemma A71.7. ∎

---

## 9. Recurrence obligations after A71

A34 recurrence sources now have the following status:

| Source | Status |
|---|---|
| R1 H1 | routed modulo existing mechanisms |
| R2 H2 | routed modulo existing mechanisms |
| R3 pair-swap | routed modulo existing mechanisms |
| R4 singleton-prefix | routed modulo existing mechanisms |
| R5 cyclic-cut | routed modulo existing mechanisms |

This does not prove global termination.  It means the named recurrence sources no longer introduce new local algebraic species.

---

## 10. Remaining global problems

After A71, the proof bottlenecks are:

```text
1. final global termination theorem for the routed class graph;
2. weighted core cut-selection theorem;
3. certification/finite verification bridge;
4. assembly of endpoint avoidance theorem.
```

The local recurrence taxonomy is now largely closed, but the descent graph still needs a global acyclicity proof.

---

## 11. Target A72

A72 should build a directed dependency graph of all routed obstruction classes.

Nodes:

```text
ZERO_COLLAPSE,
TWO_PIECE_ZERO,
THREE_PIECE_ZERO,
EQUAL_INTERVAL,
SIGNED_INTERVAL,
SEPARATED_EQUAL,
MIDPOINT,
PAIR_DIFFERENCE,
WEIGHTED_CORE,
SINGLETON_RECURRENCE,
CYCLIC_RECURRENCE,
A34_RECURRENCE.
```

Edges should record reductions proved in A1--A71.

Goal:

```text
identify cycles in the reduction graph;
assign a measure that strictly decreases on every cycle edge;
locate the remaining unproved cut-selection edge for WEIGHTED_CORE.
```

This is the right next step before claiming a complete proof.

---

## Current status

Proved here:

1. cyclic partial-sum formulas;
2. cyclic forbidden hits are endpoint-pair equations;
3. persistence of the same forbidden endpoint forces zero collapse;
4. `2f` and `2f-sigma` special hits are midpoint boundary equations;
5. wrapping blockers are bridge zero/signed composites;
6. cyclic recurrence introduces no new local species.

Not proved here:

1. global acyclicity/termination;
2. weighted cut-selection;
3. final endpoint avoidance theorem.
