# Analytic equal-sum exchange A13: exact obstruction equations

This note continues A12.

A12 showed that the two non-cross cyclic obstruction branches are equal-sum traps:

```text
FIRST:   sum(0,h] = sum(h,alpha] = f,
SECOND:  sum(beta,h] = sum(h,t] = sigma-f.
```

This note computes the exact partial-sum formulas and obstruction equations for the natural block exchanges associated to these traps.

The main warning is important: a direct equal-sum exchange generally does **not** avoid the forbidden value.  It usually moves the forbidden hit to another position.  Therefore the final proof needs a perturbation of one equal-sum block, not merely the exchange itself.

## Standing setup

Let

```text
R=(r_1,...,r_t)
```

be a Graham-valid ordering of `A subset F_p^*`, with

```text
S_0=0,
S_i=r_1+...+r_i,
sigma=S_t.
```

Assume endpoint avoidance fails for `(A,f)`, where

```text
f != sigma.
```

Choose `R` so that the unique forbidden hit occurs as early as possible:

```text
S_h=f.
```

---

# 1. FIRST equal-sum branch

Assume

```text
h < alpha <= t,
S_alpha=2f.
```

Decompose

```text
R = L U V
```

where

```text
L=(r_1,...,r_h),
U=(r_{h+1},...,r_alpha),
V=(r_{alpha+1},...,r_t).
```

Then

```text
sum(L)=sum(U)=f.
```

Let

```text
ell = |L| = h,
u = |U| = alpha-h,
```

and define internal prefix sums

```text
L_i = r_1+...+r_i,                 1 <= i <= ell,
U_j = r_{h+1}+...+r_{h+j},          1 <= j <= u,
V_k = r_{alpha+1}+...+r_{alpha+k}.  1 <= k <= |V|.
```

Thus

```text
L_ell=f,
U_u=f.
```

Consider the direct exchange

```text
L U V  ->  U L V.
```

Call the exchanged ordering `R_F`.

## Lemma A13.1: FIRST exchange partial sums

The nonempty partial sums of `R_F` are

```text
U_1, ..., U_u,
f+L_1, ..., f+L_ell,
2f+V_1, ..., 2f+V_|V|.
```

The final `V`-side values are exactly the original partial sums after `alpha`.

### Proof

In `R_F`, the first block is `U`, so its partial sums are `U_j`.  After all of `U`, the running value is `f`.  Passing through `L` gives `f+L_i`.  After `UL`, the running value is `2f`, the same as after `LU` in the original ordering, so the `V`-side partial sums are `2f+V_k`, identical to the original values after `alpha`.  ∎

## Lemma A13.2: FIRST exchange Graham-validity criterion

The exchange `LUV -> ULV` is Graham-valid if and only if all of the following hold:

1. `U_i` are pairwise distinct;
2. `f+L_i` are pairwise distinct;
3. the unchanged tail values `2f+V_k` are pairwise distinct;
4. no cross-collision occurs among the three families:

```text
U_i = f+L_j,
U_i = 2f+V_k,
f+L_j = 2f+V_k.
```

The first three conditions already hold because `R` is Graham-valid.  Thus the only possible failures of the direct FIRST exchange are the three cross-collision families above.

### Proof

The displayed families are exactly the three blocks of partial sums from Lemma A13.1.  Internal pairwise distinctness of each family follows from Graham-validity of the original ordering, because the original ordering had families

```text
L_i,
f+U_i,
2f+V_k,
```

with pairwise distinct entries inside each family.  Therefore only cross-family equalities can obstruct Graham-validity.  ∎

## Lemma A13.3: direct FIRST exchange never avoids `f`

The direct FIRST exchange `LUV -> ULV` always has a forbidden hit at the end of the first block `U`:

```text
U_u=f.
```

Therefore this exchange alone cannot prove endpoint avoidance.

If the exchange is Graham-valid, then minimality of `h` forces

```text
u >= h,
```

which is equivalent to

```text
alpha >= 2h.
```

### Proof

Since `sum(U)=f`, the partial sum after the first block in `R_F` is `f`.  If `R_F` is Graham-valid, then it is a Graham-valid ordering hitting `f` at position `u`.  Minimality of the original first-hit index `h` gives `u>=h`, i.e. `alpha-h>=h`.  ∎

---

# 2. FIRST perturbation criterion

Because direct exchange preserves an `f`-hit, the useful move is to replace `U` by an internal ordering `U'` with the same total sum but whose **proper** partial sums do not cause collisions and whose final partial sum is not too early or is subsequently broken by another move.

The following is only a bookkeeping lemma, but it identifies the exact obstruction to making `U` the first block.

Let `U'=(u'_1,...,u'_u)` be any ordering of the same set of entries as `U`.  Let

```text
U'_j=u'_1+...+u'_j.
```

Since `sum(U')=f`, one has `U'_u=f`.

## Lemma A13.4: FIRST internal perturbation criterion

The ordering

```text
U' L V
```

is Graham-valid if and only if:

1. `U'_1,...,U'_u` are pairwise distinct;
2. no cross-collision occurs:

```text
U'_i = f+L_j,
U'_i = 2f+V_k,
f+L_j = 2f+V_k.
```

It avoids `f` if and only if impossible condition `U'_u != f` holds, so an ordering beginning with the full equal-sum block `U'` can never itself avoid `f`.

### Proof

Same partial-sum computation as Lemma A13.1, replacing internal prefixes `U_i` by `U'_i`.  Since the total sum of `U'` remains `f`, the final partial sum of the first block is always `f`.  ∎

### Consequence

A FIRST-branch proof cannot simply reorder `U` and put it first.  It must either:

```text
1. split U into proper pieces and interleave another atom/block before the full sum f is reached;
2. move only a proper prefix of U;
3. pair the FIRST equal-sum trap with the local zero-block obstruction from A5/A9.
```

This narrows the next target considerably.

---

# 3. SECOND equal-sum branch

Assume

```text
1 <= beta <= h,
S_beta = 2f - sigma.
```

Decompose

```text
R = A B C
```

where

```text
A=(r_1,...,r_beta),
B=(r_{beta+1},...,r_h),
C=(r_{h+1},...,r_t).
```

Then

```text
sum(B)=sum(C)=sigma-f.
```

Let

```text
A_i = r_1+...+r_i,                       1 <= i <= beta,
B_j = r_{beta+1}+...+r_{beta+j},          1 <= j <= |B|,
C_k = r_{h+1}+...+r_{h+k},                1 <= k <= |C|.
```

The direct exchange is

```text
A B C  ->  A C B.
```

Call the exchanged ordering `R_S`.

## Lemma A13.5: SECOND exchange partial sums

The nonempty partial sums of `R_S` are

```text
A_1, ..., A_beta,
S_beta+C_1, ..., S_beta+C_|C|,
f+B_1, ..., f+B_|B|.
```

Here the endpoint after `A C` is

```text
S_beta + sum(C) = (2f-sigma)+(sigma-f)=f.
```

### Proof

The `A` block is unchanged.  After `A`, the running sum is `S_beta`.  Passing through `C` gives `S_beta+C_k`.  Since `sum(C)=sigma-f`, the running sum after `AC` is `f`.  Passing through `B` gives `f+B_j`.  ∎

## Lemma A13.6: SECOND exchange Graham-validity criterion

The exchange `ABC -> ACB` is Graham-valid if and only if the following cross-collisions are absent:

```text
A_i = S_beta+C_k,
A_i = f+B_j,
S_beta+C_k = f+B_j.
```

Internal collisions within each of the three displayed families are impossible by Graham-validity of the original ordering.

### Proof

Same reasoning as Lemma A13.2 using the partial-sum families in Lemma A13.5.  ∎

## Lemma A13.7: direct SECOND exchange preserves an `f`-hit

The direct SECOND exchange has a forbidden hit after the block `AC`, at position

```text
beta + |C| = beta + t - h.
```

If `R_S` is Graham-valid, minimality of `h` implies

```text
beta + t - h >= h,
```

or

```text
beta >= 2h-t.
```

### Proof

The endpoint after `AC` is `f` by Lemma A13.5.  If the exchanged ordering is Graham-valid, it is a Graham-valid ordering with an `f`-hit at position `beta+t-h`.  Minimality of `h` gives the inequality.  ∎

---

# 4. SECOND perturbation criterion

As in the FIRST branch, moving the entire equal-sum block `C` earlier cannot avoid `f` by itself.

Let `C'` be any internal ordering of the entries of `C`.  Since `sum(C')=sigma-f`, the ordering

```text
A C' B
```

still hits `f` after the full `C'` block.

Therefore the useful perturbations must split `C`, interleave material from `B`, or exploit the local bypass zero block.

---

# 5. Refined A14 target

The equal-sum branches do not reduce to endpoint avoidance by direct exchange.  Instead they reduce to a **nontrivial interleaving problem**.

## Target A14: equal-sum interleaving lemma

### FIRST branch

Given disjoint consecutive blocks `L,U,V` with

```text
sum(L)=sum(U)=f,
```

and with a local bypass obstruction at the first hit, prove that some nontrivial interleaving of `L` and `U`, or of a proper prefix of `U` with the adjacent pair `(a,b)`, gives either:

```text
1. a Graham-valid ordering avoiding f;
2. a Graham-valid ordering with an earlier f-hit;
3. an exposed zero-sum block already handled by A9/A11.
```

### SECOND branch

Given `A,B,C` with

```text
sum(B)=sum(C)=sigma-f,
```

prove that some nontrivial interleaving of `B` and `C`, or relocation of a proper prefix of `C`, gives one of the same three outcomes.

---

# 6. Current status

Proved here:

1. exact partial-sum formulas for the FIRST equal-sum exchange;
2. exact Graham-validity obstruction equations for the FIRST exchange;
3. direct FIRST exchange cannot avoid `f`;
4. exact partial-sum formulas for the SECOND equal-sum exchange;
5. exact Graham-validity obstruction equations for the SECOND exchange;
6. direct SECOND exchange cannot avoid `f`.

Not proved here:

1. equal-sum interleaving lemma;
2. reduction of all equal-sum traps to zero-block traps;
3. endpoint avoidance theorem.
