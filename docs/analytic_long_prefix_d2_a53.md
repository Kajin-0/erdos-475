# Analytic long-prefix D2 reduction A53

This note continues from A52.

A52 handled the balanced D2 branch

```text
m=k
```

by rewriting it as a zero-composite branch and routing it through the atom-insertion framework A31--A33, leaving only A34 recurrence.

This note handles the long-prefix D2 branch

```text
m>k.
```

The main point is that long-prefix D2 has the same zero-composite structure as balanced D2, except that the inserted `Y` prefix is longer.  The canonical atom-insertion cut is therefore even safer: the second side of the cut has length at least two, so the Q2 single-atom boundary is automatically avoided.

No complete proof of endpoint avoidance is claimed because A34 remains open.

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
K=prefix_k(C),
L=tail_k(C),
M=prefix_m(Y),
```

with

```text
m>k>=1.
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

The D2 equation is

```text
kappa = 2a+g+mu.
```

---

# 1. Long-prefix D2 zero-composite form

## Lemma A53.1: D2 is equivalent to `A G L M` being zero-sum

For any D2 branch, balanced or not, the equation

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
= a+g+ell+mu
= a+g+(a-kappa)+mu
= 2a+g+mu-kappa.
```

This is zero exactly when D2 holds.  ∎

### Interpretation

D2 always replaces the `C` prefix `K` by the `Y` prefix `M` and produces a zero composite:

```text
A G tail_k(C) prefix_m(Y).
```

The only difference between the regimes is support accounting:

```text
m<k  -> strict support descent,
m=k  -> support neutral,
m>k  -> support increase before surgery.
```

---

# 2. Support accounting

The original displayed support `A G C` has length

```text
|A|+|G|+|C|.
```

The D2 zero composite `A G L M` has length

```text
|A|+|G|+(|C|-k)+m.
```

Thus the support change is

```text
m-k.
```

## Lemma A53.2: long-prefix D2 increases first-order support by `m-k`

If

```text
m>k,
```

then the zero composite `A G L M` has support larger than the original displayed span `A G C` by exactly

```text
m-k.
```

### Proof

Subtract original support from new support:

```text
[|A|+|G|+|C|-k+m] - [|A|+|G|+|C|] = m-k.
```

∎

### Consequence

Long-prefix D2 cannot be closed by naive support descent.  It must be controlled by zero-composite surgery or by the global recurrence measure A34.

---

# 3. Splitting the long prefix

Because `m>k`, split

```text
M = M_0 E,
```

where

```text
|M_0|=k,
|E|=m-k>=1.
```

Then D2 becomes

```text
sum(A G L M_0 E)=0.
```

The balanced-length part is

```text
A G L M_0,
```

and the extra long-prefix tail is

```text
E.
```

## Lemma A53.3: long-prefix D2 is a balanced-transfer core plus an extra zero-complement tail

Let

```text
M=M_0E,
|M_0|=k.
```

Then long-prefix D2 is equivalent to

```text
sum(A G L M_0) + sum(E)=0.
```

### Proof

This is Lemma A53.1 with `M=M_0E`. ∎

### Interpretation

If `sum(E)=0`, then the extra tail itself is a zero-prefix/interior-zero branch.  Otherwise `A G L M_0` and `E` form a two-piece zero composite.

This shows that long-prefix D2 is not a new algebraic class.  It is a zero-composite extension of the balanced case.

---

# 4. Canonical exposure

Move `K` after `L M`:

```text
A G K L M N -> A G L M K N.
```

## Lemma A53.4: moving K after L M exposes the zero block `A G L M`

Under D2, the block move

```text
X A G K L M N -> X A G L M K N
```

makes

```text
A G L M
```

contiguous and zero-sum.

### Proof

By Lemma A53.1, `sum(A G L M)=0`.  After the move, those pieces are adjacent. ∎

## Lemma A53.5: raw exposure creates the standard zero-block endpoint collision

If the partial sum before `A` is nonbase, then the exposed zero block in

```text
X A G L M K N
```

creates a Graham collision between the endpoint before `A` and the endpoint after `A G L M`.

If the partial sum before `A` is the basepoint, this is a prefix-zero branch.

### Proof

This is the standard zero-block endpoint criterion. ∎

---

# 5. Canonical atom insertion

After exposure, set

```text
Z=A G L M.
```

The outside block is

```text
K=prefix_k(C).
```

Insert one atom of `K` into the canonical cut

```text
P=A G,
Q=L M.
```

The length of the second side is

```text
|Q|=|L|+m.
```

Since `m>k>=1`, we have

```text
m>=2
```

whenever `k>=1` and `m>k`.

Therefore

```text
|Q|>=2
```

regardless of whether `L` is empty.

---

## Lemma A53.6: long-prefix D2 automatically avoids the Q2 single-atom boundary for the canonical cut

For long-prefix D2, using the cut

```text
P=A G,
Q=L M,
```

one has

```text
|Q|=|L|+m>=2.
```

Thus the Q2 single-atom boundary from A31--A33 cannot occur.

### Proof

Since `m>k>=1`, `m>=2`.  Hence `|Q|=|L|+m>=2`. ∎

---

# 6. Main long-prefix D2 reduction

## Proposition A53.7: long-prefix D2 is controlled modulo A34 recurrence

Assume D2 with

```text
m>k>=1.
```

Then:

1. D2 gives the zero composite

```text
Z=A G tail_k(C) prefix_m(Y)
```

by Lemma A53.1;

2. exposing `Z` creates a standard zero-block endpoint collision by Lemmas A53.4--A53.5;

3. inserting an atom of `K=prefix_k(C)` into the canonical cut

```text
P=A G,
Q=tail_k(C) prefix_m(Y)
```

avoids the Q2 single-atom boundary by Lemma A53.6;

4. by A31--A33, all non-forbidden-hit insertion obstructions route to strict descent, equal-interval descent, zero collapse, or lower composite-zero branches;

5. the remaining non-descending obstruction is a forbidden-hit recurrence governed by A34.

Therefore long-prefix D2 is controlled modulo the A34 global recurrence theorem.

### Proof

Combine Lemmas A53.1--A53.6 with the atom-insertion descent framework A31--A33. ∎

---

# 7. Updated D2 status

Combining A40, A52, and A53:

| D2 range | Status |
|---|---|
| `m<k` | strict support descent by A40 |
| `m=k` | balanced zero-composite controlled modulo A34 by A52 |
| `m>k` | long-prefix zero-composite controlled modulo A34 by A53 |

Thus the D2 branch is fully routed modulo A34.

---

# 8. Consequence for separated equal-interval surgery

After A53, all direct-exchange collision branches D1--D5 from separated equal-interval surgery are controlled locally or modulo A34:

```text
D1 -> equal-interval descent / zero collapse;
D2 -> descent or zero-composite + A34 recurrence;
D3 -> two-piece zero / zero collapse;
D4 -> two-piece zero / zero collapse;
D5 -> strict-span three-piece zero or two-piece endpoint branch.
```

Together with A49, the separated-equal branch now has no unclassified local collision obstruction.

The remaining separated-equal difficulty is transformed-order forbidden recurrence, i.e. A34.

---

# 9. Remaining global obligations

After A53, the main open obligations are:

```text
O1. A34 global recurrence theorem.
O2. general weighted signed overlap/nesting from A20.
O3. midpoint boundary.
```

The D2 balanced and long-prefix branches are no longer standalone hard residuals.

---

# 10. Target A54

The next proof-status update should record that separated equal-interval surgery is locally routed modulo A34.

Then the next local target should be one of:

```text
1. midpoint boundary;
2. general weighted signed overlap/nesting;
3. direct attack on A34 recurrence.
```

The most promising local target is probably the midpoint boundary because A36 already identified it as the zero-gap boundary of separated equal intervals.

---

## Current status

Proved here:

1. D2 always gives zero composite `A G tail_k(C) prefix_m(Y)`;
2. long-prefix D2 support increases by `m-k` before surgery;
3. long-prefix D2 splits into balanced core plus extra prefix tail;
4. canonical exposure of the zero block;
5. canonical atom-insertion cut automatically avoids Q2 single-atom boundary;
6. long-prefix D2 controlled modulo A34 recurrence.

Not proved here:

1. A34 global recurrence theorem;
2. weighted signed and midpoint branches;
3. endpoint avoidance theorem.
