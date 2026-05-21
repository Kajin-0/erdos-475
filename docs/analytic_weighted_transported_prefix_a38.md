# Analytic weighted transported-prefix branch A38

This note continues from A37.

A37 classified the D5 proper-interior branch from separated equal-interval surgery as a weighted transported-prefix branch.  This note sharpens that conclusion.

The main new observation is:

```text
D5 proper-interior is not terminal weighted residue.
It is equivalent to a strict-span three-piece zero composite.
```

This is useful because it moves a branch previously marked hard into the composite-zero descent framework of A28--A33.

---

## Standing setup

Let a displayed segment be

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
A = P R,
C = K L,
```

where:

```text
P = prefix_i(A),
R = tail_i(A),
K = prefix_k(C),
L = tail_k(C).
```

Let

```text
p=sum(P)=A_i,
r=sum(R),
k=sum(K)=C_k,
ell=sum(L).
```

Then

```text
a=p+r=k+ell.
```

The proper-interior assumptions are

```text
1 <= i < |A|,
1 <= k < |C|,
```

so both `R` and `L` are nonempty.

---

# 1. D5 branch from A36/A37

The D5 obstruction equation is

```text
C_k = a + g + A_i.
```

In the notation above, this is

```text
k = a+g+p.
```

A37 rewrote this as a weighted transported-prefix relation.  The next lemma gives a cleaner equivalent form.

---

## Lemma A38.1: D5 proper-interior is equivalent to a three-piece zero composite

Under the standing setup, D5

```text
k=a+g+p
```

is equivalent to

```text
p+g+ell=0.
```

That is,

```text
sum(P)+sum(G)+sum(L)=0.
```

### Proof

Since `a=k+ell`, one has

```text
ell=a-k.
```

Using D5,

```text
ell=a-(a+g+p)=-g-p.
```

Therefore

```text
p+g+ell=p+g-g-p=0.
```

Conversely, if `p+g+ell=0`, then `ell=-p-g`.  Hence

```text
k=a-ell=a+p+g,
```

which is D5.  ∎

---

## Lemma A38.2: D5 proper-interior is strict span descent

The three-piece zero composite from Lemma A38.1 has support

```text
P, G, L.
```

Its enclosing span inside `A G C` is strictly smaller than the original displayed span unless `P=A` and `L=C`, which are excluded by the proper-interior assumptions.

More concretely, the original displayed support length is

```text
|A|+|G|+|C|.
```

The new composite support length is

```text
|P|+|G|+|L| = i + |G| + (|C|-k).
```

Since

```text
i<|A|,
k>=1,
```

we have

```text
i + |G| + (|C|-k) < |A|+|G|+|C|.
```

### Proof

Subtract the new support length from the original:

```text
(|A|+|G|+|C|) - (i+|G|+|C|-k)
= (|A|-i)+k.
```

Both terms are positive under `i<|A|` and `k>=1`.  ∎

---

## Lemma A38.3: D5 endpoint cases agree with A37

If `i=|A|`, then `P=A`, `R` is empty, and Lemma A38.1 gives

```text
sum(A)+sum(G)+sum(L)=0,
```

which is the A37 endpoint two-piece/composite branch involving `AG` and `tail(C)`.

If `k=|C|`, then `L` is empty, and Lemma A38.1 gives

```text
sum(P)+sum(G)=0,
```

which is the A37 endpoint two-piece zero branch involving `G` and a prefix of `A`.

### Proof

Set the corresponding tail or prefix to the full/empty block in Lemma A38.1.  ∎

---

# 2. Consequence for separated equal-interval surgery

The D5 branch from A36 is now controlled:

```text
D5 endpoint i=|A|   -> two/composite zero branch;
D5 endpoint k=|C|   -> two-piece zero branch;
D5 proper-interior -> strict-span three-piece zero branch.
```

Thus D5 should no longer be listed as a hard weighted transported-prefix residual.  It belongs to the composite-zero descent framework.

The remaining hard direct-exchange branch from A36 is therefore primarily D2, plus forbidden-hit recurrence.

---

# 3. D2 branch preview

For completeness, recall D2 from A36:

```text
C_k = 2a+g+Y_m.
```

Since the total sum of the displayed block `A G C` is

```text
2a+g,
```

D2 says:

```text
C_k = sum(A G C) + Y_m.
```

Equivalently,

```text
C_k - Y_m = sum(A G C).
```

Using `C=K L` with `sum(K)=C_k`, the complement relation is

```text
sum(A G) + sum(L) + Y_m = 0.
```

Indeed:

```text
sum(A G) + sum(L) + Y_m
= (a+g) + (a-C_k) + Y_m
= 2a+g+Y_m-C_k
=0.
```

So D2 also routes to a three-piece zero composite:

```text
A G + tail(C) + prefix(Y) = 0.
```

This is recorded formally next.

---

## Lemma A38.4: D2 routes to a three-piece zero composite

The D2 equation

```text
C_k = 2a+g+Y_m
```

is equivalent to

```text
sum(A G)+sum(tail_k(C))+Y_m=0.
```

### Proof

Let `L=tail_k(C)`, so `sum(L)=a-C_k`.  Then

```text
sum(A G)+sum(L)+Y_m
= (a+g)+(a-C_k)+Y_m
=2a+g+Y_m-C_k.
```

This vanishes exactly when D2 holds.  ∎

---

## Lemma A38.5: D2 proper-prefix branch is span-controlled unless the C-prefix is empty boundary

In the actual D2 collision family, `k>=1`.  If `k<|C|`, then `tail_k(C)` is a proper tail of `C`, and the composite

```text
A G + tail_k(C) + Y_m
```

has shorter support inside the original `A G C` portion than the full `A G C` block, before accounting for `Y_m`.

If `k=|C|`, then `tail_k(C)` is empty and D2 becomes

```text
sum(A G)+Y_m=0,
```

which is a two-piece zero composite.

### Proof

The endpoint statement follows immediately from Lemma A38.4.  For `k<|C|`, the `C` contribution is shortened from all of `C` to a proper tail.  ∎

### Status

D2 is not an irreducible weighted branch either.  It routes to a composite-zero branch.  The support may include a `Y` prefix, so the global measure must count whether the added `Y_m` support is offset by the removed `C_k` support.  This is a recurrence/descent accounting issue, not a new algebraic class.

---

# 4. Updated status of A36 direct-exchange collision families

A36 direct-exchange collision families were:

```text
D1: C_k = a+G_j,
D2: C_k = 2a+g+Y_m,
D3: A_i = G_j-g,
D4: A_i = a+Y_m,
D5: C_k = a+g+A_i.
```

Current routing:

| Branch | Status |
|---|---|
| D1 | equal-interval descent / endpoint zero collapse by A37 |
| D2 | three-piece zero composite by A38.4 |
| D3 | two-piece zero composite by A36 |
| D4 | two-piece zero composite by A36 |
| D5 | strict-span three-piece zero composite by A38.1--A38.2 |

Thus the direct-exchange collision side of separated equal-interval surgery no longer has an unclassified weighted branch.

The remaining issues are:

```text
1. composite-zero descent accounting for D2/D5;
2. forbidden-hit recurrences from A36.3;
3. gap-after move obstruction equations from A36.5;
4. terminal midpoint/separated-equal branches after normalization.
```

---

# 5. Target A39

A39 should update the symbolic classifier/status map to route D2 and D5 into composite-zero classes instead of weighted hard residuals.

Suggested additions:

```text
scripts/classify_separated_equal_surgery.py
```

Input:

```text
branch D1--D5,
lengths |A|, |G|, |C|,
indices i,j,k,m
```

Output:

```text
equal_interval_descent,
two_piece_zero,
three_piece_zero_strict_span,
zero_collapse,
forbidden_recurrence.
```

---

## Current status

Proved here:

1. D5 proper-interior is equivalent to `prefix(A)+G+tail(C)=0`;
2. D5 proper-interior is strict span descent;
3. D5 endpoint cases match A37;
4. D2 routes to `AG+tail(C)+prefix(Y)=0`;
5. direct-exchange separated-equal collision branches are now all routed to equal-interval or composite-zero classes.

Not proved here:

1. all composite-zero branches terminate;
2. forbidden recurrence descent;
3. gap-after move branch elimination;
4. endpoint avoidance theorem.
