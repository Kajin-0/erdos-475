# Analytic singleton-prefix recurrence A70

This note continues from A69.

A68 reduced atom-insertion recurrence H1/H2 to existing mechanisms.  A69 reduced A33 pair-swap recurrence to existing mechanisms.  The next A34 recurrence source is singleton-prefix recurrence.

Singleton-prefix recurrence appears when a transformed ordering is Graham-valid but hits the forbidden value at a very small moved object:

```text
x+q=f
```

for an atom `q`, or more generally

```text
x+B_i=f
```

for a moved prefix `B_i`.

This note applies A5 at such a recurrent hit and routes the resulting blocker.  The result is partial but useful: non-crossing blockers descend, while crossing blockers route to bridge interval, zero-composite, pair-difference, or cyclic-cut recurrence.

No complete endpoint-avoidance proof is claimed.

---

## 1. Standing singleton-prefix setup

Let a transformed ordering contain a displayed moved prefix block

```text
B=B_i B^+
```

based at a partial sum value

```text
x=sum(X).
```

The singleton-prefix recurrence is

```text
x+B_i=f.
```

The atom case is the special case

```text
B_i=q.
```

Assume the transformed ordering is Graham-valid and that this forbidden hit is not earlier than the global minimal forbidden hit.

Let the source obstruction that produced this transformed ordering have span

```text
s=span(O).
```

By A64, if the nearest A5 blocker at the recurrent hit has span less than `s`, the recurrence descends.  Thus this note focuses on long-blocker or boundary cases.

---

## 2. Applying A5 at the singleton-prefix hit

Let `H` be the endpoint after `B_i`, so

```text
S'_H=x+B_i=f.
```

Assume `H` is not final.  This is automatic in endpoint avoidance because the final sum is `sigma(A) != f`.

Let the next atom be

```text
b_+=first atom after B_i.
```

A5 gives a blocker index `j'` such that

```text
S'_{H-1}+b_+=S'_{j'}.
```

There are two directions:

```text
left blocker:  j'<H;
right blocker: j'>H.
```

---

# 3. Left blockers

For a left blocker, A64.2 gives

```text
sum'(j',H-1]+b_+=0.
```

The interval `(j',H-1]` ends immediately before the last atom of `B_i`.

Write

```text
B_i = B_i^- b_-
```

where `b_-` is the last atom of the prefix `B_i`.

---

## Lemma A70.1: left blocker inside B_i gives suffix-zero descent

If the left blocker lies inside the moved prefix `B_i`, then the A5 relation pulls back to

```text
suffix(B_i before b_-)+b_+=0,
```

more explicitly:

```text
sum(tail of B_i ending before b_-)+b_+=0.
```

This is a two-piece zero composite using a proper suffix of `B_i` and the next atom `b_+`.

### Proof

The interval `(j',H-1]` is exactly a proper suffix of `B_i` ending before the final atom that created the endpoint `H`.  Adding `b_+` gives the displayed zero relation. ∎

### Status

This is strict support descent unless `B_i` is a single atom and the suffix is empty.  In that atom case, the equation gives `b_+=0`, impossible because atoms lie in `F_p^*`.

---

## Lemma A70.2: left blocker at the base of B_i is a two-atom or prefix-zero boundary

If the blocker is exactly the endpoint before `B_i`, then

```text
sum'(j',H-1]+b_+=B_i^-+b_+=0.
```

If `B_i` is an atom, then `B_i^-` is empty and the equation is `b_+=0`, impossible.

If `B_i` has length at least two, this is a shorter prefix-zero/two-piece zero branch inside `B_i` plus the next atom.

### Proof

Immediate from the left-blocker formula. ∎

---

## Lemma A70.3: left blocker before the base gives a bridge zero-composite

If the blocker lies before the basepoint `x`, then the pullback has form

```text
L+B_i^-+b_+=0,
```

where `L` is the external bridge ending at the start of `B_i`.

### Proof

The interval from the blocker to `H-1` consists of the external bridge followed by `B_i^-`.  Add `b_+`. ∎

### Status

This is a crossing bridge branch.  It routes to external-collision/equal-signed interval machinery by A62.  It is not automatically smaller.

---

# 4. Right blockers

For a right blocker, compare the interval after the recurrent hit with the A5 atom substitution.

Let `C_r` be the prefix after `H` ending at the right blocker.  If the blocker lies inside the continuation immediately after `B_i`, then `C_r` is a prefix of the local tail beginning with `b_+`.

The A5 equation gives a pair-difference type relation between the last atom `b_-` of `B_i` and the next atom `b_+`.

---

## Lemma A70.4: right blocker inside a proper following prefix gives pair-difference prefix descent

If the right blocker lies inside a proper prefix `C_r` of the tail after `B_i`, then

```text
C_r = b_+ - b_-.
```

Equivalently,

```text
b_- - b_+ + C_r=0.
```

### Proof

The A5 relation is

```text
S'_{H-1}+b_+=S'_{j'}.
```

Since `S'_H=S'_{H-1}+b_-`, subtracting `S'_H` gives

```text
S'_{j'}-S'_H=b_+-b_-.
```

The left side is the prefix `C_r` after the recurrent hit. ∎

### Endpoint cases

If `C_r=b_+`, then the equation gives `b_+=b_+-b_-`, hence `b_-=0`, impossible.

If `C_r` is proper and nontrivial, this is a smaller pair-difference/prefix branch.

---

## Lemma A70.5: right blocker using a full local tail is a pair-difference boundary

If the right blocker uses the full local tail `C`, then

```text
C=b_+-b_-.
```

This is an A33-type pair-difference boundary:

```text
b_- - b_+ + C=0.
```

### Proof

Endpoint case of Lemma A70.4. ∎

---

## Lemma A70.6: right blocker beyond the local tail gives a bridge signed composite

If the right blocker lies beyond the local tail, then the pullback has form

```text
C+R+b_- - b_+=0,
```

where `R` is the external bridge after the local tail.

### Proof

The interval from `H` to the blocker consists of the full local tail `C` plus the bridge `R`.  Use the pair-difference expression from Lemma A70.4. ∎

### Status

This is a bridge signed composite, routed by A62 and the signed/equal interval machinery.

---

# 5. Atom singleton branch

The pure singleton case is

```text
x+q=f.
```

Then the prefix `B_i` consists of one atom, so `b_-=q` and `B_i^-` is empty.

Left blockers inside `B_i` do not exist.  A left blocker at the base forces `b_+=0`, impossible.  Therefore any nontrivial blocker is either:

```text
1. left bridge before x;
2. right proper-prefix pair-difference;
3. right bridge signed composite;
4. right endpoint pair-difference.
```

## Proposition A70.7: atom singleton recurrence routes to bridge or pair-difference mechanisms

If `x+q=f` is a recurrent atom landing, then the transformed A5 blocker either:

```text
1. gives an impossible zero atom;
2. gives a left bridge zero-composite;
3. gives a smaller pair-difference prefix;
4. gives a pair-difference endpoint branch;
5. gives a right bridge signed composite.
```

Thus atom singleton recurrence introduces no new local algebraic species.

### Proof

Specialize Lemmas A70.1--A70.6 to `B_i=q`. ∎

---

# 6. General prefix recurrence routing

## Proposition A70.8: singleton-prefix recurrence is routed modulo existing mechanisms

Every singleton-prefix recurrence branch

```text
x+B_i=f
```

routes to one of:

```text
1. suffix-zero descent;
2. two-piece zero/prefix-zero collapse;
3. left bridge zero-composite;
4. pair-difference prefix descent;
5. pair-difference endpoint branch;
6. right bridge signed composite;
7. A34/global termination.
```

### Proof

Left blockers are classified by Lemmas A70.1--A70.3.  Right blockers are classified by Lemmas A70.4--A70.6.  The atom singleton subcase is Proposition A70.7. ∎

---

# 7. Relation to cyclic-cut recurrence

The bridge cases in A70 are close to cyclic-cut recurrence.

A left bridge relation

```text
L+B_i^-+b_+=0
```

or a right bridge relation

```text
C+R+b_- - b_+=0
```

may wrap around the basepoint if the local move is viewed cyclically.  Therefore some singleton recurrence branches naturally route into cyclic-cut geometry.

This is consistent with A34's remaining R5 obligation.

---

# 8. Recurrence status update

After A70, A34 recurrence obligations are:

| Source | Status |
|---|---|
| R1 H1 | routed modulo existing mechanisms |
| R2 H2 | routed modulo existing mechanisms |
| R3 pair-swap | routed modulo existing mechanisms |
| R4 singleton-prefix | routed modulo pair-difference / bridge / cyclic-cut |
| R5 cyclic-cut | still open |

Thus singleton recurrence is not standalone anymore.  The remaining explicitly separate recurrence source is cyclic-cut recurrence.

---

# 9. Target A71

A71 should attack cyclic-cut recurrence.

A34 listed special cyclic hits such as:

```text
S_alpha=2f,
S_beta=2f-sigma.
```

The likely route is:

```text
1. encode cyclic cut as a basepoint change;
2. show special hits either decrease the first-hit index in the rotated ordering;
3. or produce a separated equal interval / midpoint branch;
4. or route to bridge zero-composite handled by A62/A70.
```

---

## Current status

Proved here:

1. singleton-prefix recurrence A5 pullback formulas;
2. left internal blockers descend;
3. right proper-prefix blockers descend;
4. endpoint/right bridge cases route to pair-difference or signed composites;
5. atom singleton recurrence introduces no new local species.

Not proved here:

1. cyclic-cut recurrence;
2. weighted cut-selection;
3. final global termination theorem;
4. endpoint avoidance theorem.
