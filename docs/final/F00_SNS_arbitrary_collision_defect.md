# F00.SNS arbitrary collision-defect start for strong nonzero-sum

This file continues the repair of the starting-ordering gap.

F00 and F00.C1 showed that proving full endpoint avoidance directly from arbitrary orderings introduces two simultaneous defect types:

```text
1. endpoint collisions;
2. forbidden endpoint hits.
```

F00.C1 suggested a cleaner non-circular route:

```text
First prove strong nonzero-sum for sigma(S) != 0 using arbitrary-ordering collision-defect minimization.
Then derive Erdős 475 using the append-one-atom reduction.
Then use F12 to strengthen Graham-valid existence to endpoint avoidance.
```

This file formulates that route.

Status: repair draft, not complete proof.

---

## SNS.1. Strong nonzero-sum target

Let `p` be prime and let

```text
S subset F_p^*
```

be finite with

```text
sigma(S) != 0.
```

The strong nonzero-sum theorem asks for an ordering

```text
R=(r_1,...,r_t)
```

such that the extended partial sums

```text
S_0=0,S_1,...,S_t=sigma(S)
```

are pairwise distinct.

Equivalently, there is no nonempty zero-sum interval in the ordering.

This version has no arbitrary forbidden endpoint `f`.  The only defect is collision of extended partial sums.

---

## SNS.2. Collision defect vector

For any ordering `R`, define endpoint collisions:

```text
0 <= i < j <= t,
S_i=S_j.
```

Each collision corresponds to a nonempty zero-sum interval

```text
r_{i+1}+...+r_j=0.
```

Since

```text
sigma(S)=S_t != S_0=0,
```

the whole ordering is not a zero interval.

Define:

```text
minspan(R)=minimum j-i over all endpoint collisions, or t+1 if none;
N_min(R)=number of collision pairs attaining minspan(R);
N_col(R)=total number of endpoint collision pairs.
```

Use the collision-defect vector

```text
D_SNS(R)=(
  t+1-minspan(R),
  N_min(R),
  N_col(R),
  active_left(R),
  active_right(R),
  boundary_rank(R)
).
```

The term `t+1-minspan(R)` makes increasing the shortest collision span into lexicographic descent.

The active collision is the lexicographically first collision pair attaining `minspan(R)`:

```text
(i,j) = argmin (j-i, i, j).
```

Set:

```text
active_left=i,
active_right=j.
```

---

## Lemma SNS.1: a collision-defect minimizer exists

Among all orderings of finite `S`, there exists an ordering minimizing `D_SNS(R)` lexicographically.

### Proof

There are finitely many orderings of `S`, and `D_SNS(R)` takes values in a finite set of integer tuples. ∎

---

## Lemma SNS.2: zero collision defect proves strong nonzero-sum

If an ordering has no endpoint collisions among

```text
S_0,S_1,...,S_t,
```

then it is a strong nonzero-sum ordering.

### Proof

This is exactly the definition: the extended partial sums are pairwise distinct. ∎

---

## SNS.3. Active shortest zero interval

Let `R` be a `D_SNS`-minimal ordering.  If it is not strong nonzero-sum, it has an active shortest collision

```text
S_i=S_j,
0<=i<j<=t.
```

Let

```text
Z=r_{i+1}...r_j=z_1...z_m,
m=j-i.
```

Then:

```text
sum(Z)=0.
```

Because `sigma(S) != 0`, `Z` is not the whole ordering.  Thus at least one adjacent outside atom exists.

By shortestness, `Z` has no proper nonempty zero-sum subinterval.

---

## Lemma SNS.3: shortest zero interval has no internal zero interval

If `Z` is the active shortest zero interval, then no proper nonempty subinterval of `Z` has sum zero.

### Proof

A proper zero subinterval would give a collision pair with shorter span than `m`, contradicting the definition of `minspan(R)`. ∎

---

## Lemma SNS.4: active zero interval is not the whole ordering

If `sigma(S) != 0`, then the active zero interval `Z` is not the whole ordering.

### Proof

If `Z` were the whole ordering, then `sum(Z)=sigma(S)=0`, contrary to hypothesis. ∎

---

## SNS.4. Adjacent outside atom

Since `Z` is not the whole ordering, choose an adjacent outside atom.  In one orientation:

```text
R = X Z q Y,
q in F_p^*.
```

The opposite orientation

```text
R = X q Z Y
```

is symmetric.

The repair move is to insert `q` into different positions inside `Z`:

```text
X z_1 ... z_k q z_{k+1} ... z_m Y,
0 <= k <= m.
```

The original ordering corresponds to `k=m`.

---

## SNS.5. Local endpoint formulas

Let

```text
T_k=z_1+...+z_k,
T_0=0,
T_m=0.
```

After inserting `q` after `z_k`, the local endpoints relative to the basepoint before `Z` are:

```text
T_0,T_1,...,T_k,
T_k+q,
T_k+q+z_{k+1},...,
T_k+q+z_{k+1}+...+z_m=q.
```

Equivalently, the suffix-side endpoints are:

```text
q + T_s - T_k,
for k <= s <= m.
```

Thus the old internal endpoint set of `Z` is partially preserved before `q` and translated by `q-T_k` after `q`.

---

## Lemma SNS.5: local internal collision during insertion routes to F4/F5/F7

If inserting `q` into `Z` creates a collision involving two local endpoints inside `Z q`, then the collision gives one of:

```text
1. proper zero subinterval of Z, impossible by shortestness;
2. zero interval containing q;
3. equal interval between a prefix of Z and shifted suffix of Z;
4. pair-difference/signed interval involving q;
5. recurrence-style moved-prefix obstruction if the collision appears only after a sequence of adjacent swaps.
```

Thus the case enters the F3 state machine through F4, F5, or F7.

### Proof

Compare the endpoint formulas in SNS.5.  If both endpoints are on the same side of `q`, the `q` term cancels, giving a zero subinterval of `Z`; by shortestness it cannot be proper.  If the endpoints are on opposite sides, subtracting gives a relation involving `q` and a prefix/suffix of `Z`, which is a zero-composite or signed pair relation.  Adjacent-swap derivations are routed as recurrence through F7. ∎

---

## Lemma SNS.6: external collision during insertion routes to F6/F8

If inserting `q` into `Z` creates a collision with an endpoint outside the local window `Z q`, then it is an external collision and routes through F6/F8.

### Proof

The local move reorders the atom window `Z q` while preserving its total sum.  Any collision with an endpoint in `X`, `Y`, or another unchanged displayed family is external in the sense of F6. ∎

---

## SNS.6. Clean insertion

Call an insertion position `k` clean if the ordering

```text
X z_1 ... z_k q z_{k+1} ... z_m Y
```

creates no new endpoint collision involving the local window `Z q`.

A clean insertion destroys the active zero interval `Z` as a contiguous zero block unless `k=m`, which is the original ordering.

---

## Lemma SNS.7: clean nontrivial insertion removes the active collision

If `0 <= k < m` is clean, then the active collision pair `(i,j)` corresponding to `Z` is removed and no new collision involving the local window is created.

### Proof

The atom `q` is inserted inside the interval `Z`, so the old contiguous block `Z` is interrupted.  Since `q != 0`, the full local block `Z q` has sum `q`, not zero.  By cleanliness, no replacement collision involving the moved local endpoints is created. ∎

---

## SNS.7. Location-refined descent

The refined defect vector includes the active collision location.  A clean nontrivial insertion should decrease the defect unless an earlier or equal active collision remains completely outside the local window.

This is the same issue isolated in F00.C1 as Lemma C1.8.

---

## Needed Lemma SNS.C1: clean insertion decreases the refined defect

Let `R` be `D_SNS`-minimal and let `Z` be the active shortest zero interval.  If there exists a clean nontrivial insertion of an adjacent outside atom `q` into `Z`, then the resulting ordering has strictly smaller `D_SNS`.

### Status

Open.  This is the central remaining combinatorial bookkeeping lemma.

### Why it is plausible

A clean insertion removes the active shortest collision and creates no local replacement collision.  Collisions outside the local window are unchanged.  Since the active collision was lexicographically first among shortest collisions, removing it should reduce either:

```text
N_min(R),
active_left(R),
active_right(R),
or N_col(R).
```

But the exact vector order must be chosen so this is always true.

---

## SNS.8. All insertions obstructed

If every nontrivial insertion position is not clean, then each insertion produces a local or external collision.

By Lemmas SNS.5 and SNS.6, every such obstruction enters F3 through:

```text
F4 local descent,
F5 separated-equal/midpoint,
F6 external collision,
F7 recurrence,
F8 bridge/gap,
F10/F11 weighted branch if coefficient-2 normal form survives.
```

Thus all-obstructed insertion is compatible with the existing obstruction engine.

---

## Theorem SNS.8: strong nonzero-sum start, conditional form

Assume Needed Lemma SNS.C1.  Let `S subset F_p^*` satisfy `sigma(S) != 0`.  Let `R` be a `D_SNS`-minimal ordering.

Then either:

```text
1. R is already strong nonzero-sum;
2. a clean insertion decreases D_SNS, contradicting minimality;
3. every insertion is obstructed and produces an F3 obstruction state handled by F4--F11.
```

### Proof

If no collision exists, Lemma SNS.2 applies.  Otherwise choose the active shortest zero interval `Z`.  It is not the whole ordering by Lemma SNS.4, so an adjacent outside atom `q` exists.  If some nontrivial insertion is clean, Needed Lemma SNS.C1 contradicts minimality.  If no insertion is clean, Lemmas SNS.5--SNS.6 route the obstruction into F3. ∎

---

## SNS.9. Remaining gap for strong nonzero-sum

The remaining gap is not the full previous Input G.  It is now the sharper statement:

```text
SNS.C1: clean insertion decreases the refined collision-defect vector.
```

If SNS.C1 is proved and the F3--F11 obstruction engine is fully hardened, then strong nonzero-sum for `sigma(S) != 0` follows.

Then F13 gives Erdős 475 for all prime fields:

```text
sigma(S) != 0: apply strong nonzero-sum directly;
sigma(S) = 0: remove x, order S\{x}, append x.
```

---

## SNS.10. Endpoint avoidance after strong nonzero-sum

Once Erdős 475 is established, Input G in F12 is resolved.  Then F12 gives endpoint avoidance as a strengthening:

```text
Graham-valid existence -> endpoint avoidance for every f != sigma(S).
```

Thus the recommended final theorem order becomes:

```text
1. prove strong nonzero-sum by collision-defect minimization;
2. derive Erdős 475;
3. derive endpoint avoidance as a corollary/strengthening.
```

This reverses the earlier intended endpoint-avoidance-first chain.

---

## SNS.11. Recommended next file

The next file should attack the bookkeeping lemma:

```text
docs/final/F00_SNS_C1_clean_insertion_defect_descent.md
```

Goal:

```text
Choose the final refined defect vector and prove that clean insertion of q into the active shortest zero interval strictly decreases it.
```

---

## SNS.12. Status

```text
Status: repair draft.
Risk: RED.
Progress: non-circular route reduced to SNS.C1 plus the already extracted obstruction engine.
```
