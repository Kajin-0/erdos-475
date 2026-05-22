# Analytic balanced D2 general theorem A52

This note continues from A51.

A47 controlled the atom-balanced D2 case

```text
k=m=1
```

modulo the global recurrence theorem A34.  A51 showed that the first proper balanced case

```text
k=m=2
```

has the same structure: it is a zero-composite branch that can be routed through the atom-insertion framework A31--A33, leaving only A34 recurrence.

This note proves the general balanced D2 reduction for all

```text
k=m=q >= 1.
```

No complete proof of endpoint avoidance is claimed, because the result still depends on A34.

---

## Standing setup

Let a separated equal-interval segment be

```text
X A G C Y
```

with

```text
sum(A)=sum(C)=a,
sum(G)=g.
```

Write

```text
C = K L,
Y = M N,
```

where

```text
K=prefix_q(C),
L=tail_q(C),
M=prefix_q(Y),
```

and

```text
|K|=|M|=q.
```

Let

```text
kappa=sum(K),
ell=sum(L),
mu=sum(M).
```

Since `sum(C)=a`,

```text
kappa+ell=a.
```

The balanced D2 equation is

```text
kappa = 2a+g+mu.
```

---

# 1. General zero-composite form

## Lemma A52.1: balanced D2 is equivalent to `A G L M` being zero-sum

For any `q>=1`, the balanced D2 equation

```text
sum(K)=2a+g+sum(M)
```

is equivalent to

```text
sum(A G L M)=0.
```

### Proof

Compute:

```text
sum(A G L M)
= a+g+ell+mu.
```

Since `ell=a-kappa`, this equals

```text
a+g+(a-kappa)+mu
=2a+g+mu-kappa.
```

This is zero exactly when

```text
kappa=2a+g+mu.
```

∎

### Interpretation

Balanced D2 replaces the `q`-atom prefix `K` of `C` by the equal-length prefix `M` of `Y`, producing the zero-composite

```text
A G tail_q(C) prefix_q(Y).
```

This unifies A46 (`q=1`) and A51 (`q=2`).

---

# 2. Support accounting

The original displayed support `A G C` has length

```text
|A|+|G|+|C|.
```

The balanced D2 zero composite `A G L M` has length

```text
|A|+|G|+(|C|-q)+q = |A|+|G|+|C|.
```

So the balanced branch is support-neutral before additional surgery.

## Lemma A52.2: balanced D2 is support-neutral before zero-composite surgery

For every `q`, the support length of `A G L M` equals the support length of `A G C`.

### Proof

The branch removes `K`, a block of length `q`, and inserts `M`, another block of length `q`. ∎

### Consequence

Balanced D2 cannot be closed by first-order support comparison.  It requires zero-composite surgery or global recurrence control.

---

# 3. Canonical zero-block exposure

The zero composite from Lemma A52.1 is

```text
Z=A G L M.
```

In the original order, the segment is

```text
A G K L M N
```

inside `A G C Y`.  The block `K` separates `G` from `L`.

Move `K` after `L M`:

```text
A G K L M N -> A G L M K N.
```

---

## Lemma A52.3: moving K after L M exposes the zero block `A G L M`

Under balanced D2, the block move

```text
X A G K L M N -> X A G L M K N
```

makes

```text
A G L M
```

contiguous and zero-sum.

### Proof

By Lemma A52.1, `sum(A G L M)=0`.  After the move, those pieces are adjacent. ∎

---

## Lemma A52.4: raw exposure creates a zero-block endpoint collision

If the partial sum before `A` is a nonbase partial sum, the moved ordering

```text
X A G L M K N
```

has a Graham collision between the endpoint before `A` and the endpoint after `A G L M`.

If the partial sum before `A` is the basepoint, this is a prefix-zero branch.

### Proof

This is the zero-sum interval criterion applied to the contiguous zero block `A G L M`. ∎

### Consequence

Exposure is diagnostic, not a final repair.  The zero block must be broken by inserting material from `K` or another outside block into its interior, exactly as in A29--A33.

---

# 4. Canonical atom insertion

After exposure, we have a zero block

```text
Z=A G L M
```

and an adjacent outside block

```text
K=(c_1,...,c_q).
```

A robust move is to insert one atom of `K`, say `c_1`, into the canonical cut

```text
P=A G,
Q=L M.
```

The cut is chosen because its second side is large unless the balanced transfer is a boundary case.

---

## Lemma A52.5: the canonical cut avoids the Q2 single-atom boundary except when `|L|=0` and `q=1`

For the cut

```text
P=A G,
Q=L M,
```

one has

```text
|Q|=|L|+q.
```

The Q2 single-atom boundary from A31--A33 occurs only when

```text
|Q|=1.
```

Since `q>=1`, this happens if and only if

```text
q=1 and |L|=0.
```

### Proof

`|Q|=|L|+|M|=|L|+q`.  This equals `1` exactly when `q=1` and `|L|=0`. ∎

---

## Lemma A52.6: the exceptional canonical-cut boundary is already lower-piece composite-zero

If

```text
q=1,
|L|=0,
```

then `C=K` is a single atom and balanced D2 reduces to

```text
sum(A G M)=0.
```

This is the A46.7 boundary and is already a composite-zero branch.

### Proof

Set `L` empty and `q=1` in Lemma A52.1. ∎

---

# 5. Main balanced D2 reduction

## Proposition A52.7: balanced D2 is controlled modulo A34 recurrence

Assume balanced D2 with `k=m=q>=1`.

Then:

1. balanced D2 gives the zero composite

```text
Z=A G tail_q(C) prefix_q(Y)
```

by Lemma A52.1;

2. exposing `Z` creates a standard zero-block endpoint collision by Lemmas A52.3--A52.4;

3. insert an atom of `K=prefix_q(C)` into the canonical cut

```text
P=A G,
Q=tail_q(C) prefix_q(Y);
```

4. except in the boundary `q=1, tail_q(C)=empty`, this cut has `|Q|>=2`, so it avoids the Q2 single-atom boundary;

5. by A31--A33, all non-forbidden-hit insertion obstructions route to strict descent, equal-interval descent, zero collapse, or lower composite-zero branches;

6. the remaining non-descending obstruction is a forbidden-hit recurrence governed by A34.

Thus balanced D2 is controlled modulo the A34 global recurrence theorem.

### Proof

Combine Lemmas A52.1--A52.6 with the atom-insertion descent framework A31--A33. ∎

---

# 6. Relation to A41 difference-walk residuals

A41 studied the paired difference walk

```text
D_r=sum(prefix_r(K))-sum(prefix_r(M)).
```

That analysis identified smaller balanced transfers and smaller separated equal intervals when intermediate walk values repeat or hit endpoints.

A52 does not contradict A41.  It bypasses the need to eliminate the residual injective difference walk locally by using the global zero-composite structure of the full balanced D2 equation.

In short:

```text
A41: tries to descend inside the transfer K <-> M.
A52: uses the whole zero composite A G L M and inserts material from K.
```

This is why the A42/A44 local residual examples do not block the proof program; they show only that the difference-walk subproblem is locally real, not that the surrounding zero-composite surgery fails.

---

# 7. Consequence for separated equal-interval surgery

D2 status now becomes:

| D2 range | Status after A52 |
|---|---|
| `m<k` | strict support descent by A40 |
| `m=k` | balanced zero-composite, controlled modulo A34 by A52 |
| `m>k` | long-prefix recurrence / A34 obligation |

Thus proper balanced D2 with `k=m>=2` is no longer a standalone hard residual.  It is absorbed into the zero-composite + A34 recurrence framework.

---

# 8. Remaining obligations after A52

A52 removes one major item from A50's open list.

Remaining:

```text
O1. A34 global recurrence theorem.
O2. long-prefix D2 with m>k.
O3. general weighted signed overlap/nesting from A20.
O4. midpoint boundary.
```

The proof increasingly depends on one global issue:

```text
prove recurrence descent for transformed-order forbidden hits.
```

---

# 9. Target A53

The next best target is long-prefix D2:

```text
m>k.
```

A40 showed this is the non-descending range where the introduced `Y` prefix is longer than the removed `C` prefix.

But A52 suggests a possible route:

```text
D2: A G tail_k(C) prefix_m(Y)=0.
```

For `m>k`, split

```text
prefix_m(Y)=M_1 M_2,
```

where `|M_1|=k` and `|M_2|=m-k`.

Then the branch is a balanced zero-composite part plus an extra long-prefix tail `M_2`.  The expected result is:

```text
long-prefix D2 routes to balanced D2 plus A34 recurrence or strict descent after cutting M_2.
```

---

## Current status

Proved here:

1. general balanced D2 zero-composite formula;
2. balanced D2 is support-neutral before surgery;
3. canonical zero-block exposure;
4. canonical atom-insertion cut avoids the Q2 single-atom boundary except for the already controlled q=1 endpoint;
5. balanced D2 controlled modulo A34 for all q>=1.

Not proved here:

1. A34 global recurrence theorem;
2. long-prefix D2 elimination;
3. weighted signed and midpoint branches;
4. endpoint avoidance theorem.
