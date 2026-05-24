# F00.SNS.C2 q-through-zero-interval obstruction

This file continues the strong nonzero-sum repair path.

The previous file `F00_SNS_C1_clean_insertion_defect_descent.md` proved:

```text
strongly clean insertion -> strict descent of D_SNS^*.
```

The remaining geometric lemma was:

```text
Needed Lemma C1.7:
Given an active shortest zero interval Z and adjacent outside atom q,
either some insertion of q into Z is strongly clean,
or every obstruction routes into F3--F11.
```

This file attacks that lemma by writing all insertion endpoint equations explicitly.

Status: repair draft.  It reduces the issue to a finite endpoint-set covering obstruction, but does not yet close the covering argument.

---

## C2.1. Setup

Let `S subset F_p^*` satisfy

```text
sigma(S) != 0.
```

Let `R` be a `D_SNS^*`-minimal ordering.  Suppose the active shortest collision is

```text
S_i=S_j,
0<=i<j<=t.
```

Let

```text
Z=r_{i+1}...r_j=z_1...z_m,
m=j-i,
sum(Z)=0.
```

By shortestness, `Z` has no proper nonempty zero subinterval.

Since `sigma(S) != 0`, `Z` is not the whole ordering.  Assume the right-adjacent case:

```text
R = X Z q Y
```

with

```text
q in F_p^*.
```

The left-adjacent case is symmetric.

Let

```text
x=sum(X).
```

Define internal prefix sums of `Z`:

```text
T_0=0,
T_k=z_1+...+z_k,
1<=k<=m.
```

Since `sum(Z)=0`,

```text
T_m=0.
```

Since `Z` has no proper zero subinterval, the endpoint values

```text
T_0,T_1,...,T_{m-1}
```

are pairwise distinct, and none of `T_1,...,T_{m-1}` is zero.

---

## C2.2. Inserting q after position k

For

```text
0<=k<m,
```

insert `q` after `z_k`:

```text
R^{(k)} = X z_1...z_k q z_{k+1}...z_m Y.
```

The local endpoint set inside the affected block `Z q` relative to basepoint `x` is:

```text
E_k = A_k union B_k,
```

where

```text
A_k={T_0,T_1,...,T_k},
B_k={T_k+q+T_s-T_k : k<=s<=m}={q+T_s : k<=s<=m}.
```

Thus

```text
E_k={T_0,...,T_k} union {q+T_k,q+T_{k+1},...,q+T_m}.
```

Because `T_m=0`, the final local endpoint after `Z q` is

```text
q.
```

---

## Lemma C2.1: same-side local collisions are impossible except the original zero interval

For fixed `k`, a collision within `A_k` or within `B_k` gives a proper zero subinterval of `Z`, unless it is the original equality `T_0=T_m` which is no longer present inside the same side for `0<=k<m`.

### Proof

If `T_a=T_b` with `0<=a<b<=k`, then `z_{a+1}+...+z_b=0`, a proper zero subinterval of `Z` because `b<=k<m`.

If `q+T_a=q+T_b` with `k<=a<b<=m`, then again `T_a=T_b`, giving zero subinterval `z_{a+1}+...+z_b`.  If `a=0,b=m`, that would be the whole `Z`, but both indices cannot lie in the suffix range `k<=a<b<=m` with `a=0` unless `k=0`; then the endpoint `q+T_0=q+T_m` is duplicated as the start and end of the shifted full `Z`, corresponding to `Z` remaining contiguous after `q` in the case `k=0`.  This endpoint duplicate must be treated as the left-side version of the original zero interval, not as repair. ∎

---

## C2.3. Cross-side local collision equation

A cross-side local collision has form

```text
T_a = q+T_b
```

with

```text
0<=a<=k,
k<=b<=m.
```

Equivalently:

```text
q = T_a-T_b.
```

This means `q` equals the sum of an oriented interval of `Z`:

```text
q = -(z_{a+1}+...+z_b)       if a<b,
q = z_{b+1}+...+z_a          if b<a.
```

When `a=b`, this gives `q=0`, impossible.

---

## Lemma C2.2: cross-side local collision gives signed interval involving q

Every cross-side local collision during q-insertion gives a signed interval relation

```text
q + I = 0
```

or

```text
q - I = 0
```

where `I` is a nonempty proper interval of `Z`.

This routes to the F3 state machine through F4/F7.

### Proof

The collision equation is `T_a=q+T_b`.  If `a<b`, then `T_b-T_a=sum(z_{a+1}...z_b)`, so

```text
q+sum(z_{a+1}...z_b)=0.
```

If `b<a`, then

```text
q-sum(z_{b+1}...z_a)=0.
```

The interval is nonempty because `a != b`; it is proper because `q` is outside `Z` and the collision occurs inside an insertion with `0<=k<m`.  This is a signed interval or pair-difference-style relation with atom correction `q`, routed by F4/F7. ∎

---

## C2.4. External collision equation

Let an external endpoint value relative to basepoint `x` be `e`.  A local endpoint in `E_k` collides externally if either

```text
T_a=e
```

for `0<=a<=k`, or

```text
q+T_b=e
```

for `k<=b<=m`.

The first type is an unchanged old endpoint collision.  Since `R` is fixed, it corresponds to a pre-existing collision involving a prefix of `Z`.

The second type gives

```text
q+T_b=e.
```

Thus the outside atom `q` plus a prefix/suffix of `Z` reaches an external endpoint.

---

## Lemma C2.3: moved external collisions route to F6/F8

If an external collision involves a moved endpoint of the form `q+T_b`, then it is an external collision in the sense of F6 and routes to F6/F8.

### Proof

The local window is `Z q`.  The endpoint `q+T_b` is moved by the insertion.  Any collision between it and an endpoint outside the displayed local window is exactly an external collision.  F6 classifies it as bridge zero-composite, signed bridge composite, separated-equal, recurrence, or weighted normal form. ∎

---

## C2.5. Pre-existing external collisions

A collision `T_a=e` involving an unchanged prefix-side endpoint may preexist in `R`.  Since the active collision `(i,j)` was chosen as the lexicographically first shortest collision, such a pre-existing collision must either:

```text
1. have larger span than m;
2. have span m but lexicographically after (i,j);
3. be the active collision itself;
4. contradict active-choice minimality.
```

The active collision itself is `T_0=T_m`, but for `0<=k<m`, both endpoints are not simultaneously in the unchanged prefix side unless `k=m`, which is excluded.

---

## Lemma C2.4: unchanged external collisions do not obstruct strong cleanliness unless they are same-or-shorter and earlier

An unchanged collision outside the local moved endpoint set affects strong cleanliness only if it has span `<=m` and is lexicographically at or before the active pair `(i,j)`.  Such a collision contradicts active-choice minimality unless it is the active collision itself.

### Proof

Unchanged collisions are already present in `R`.  Since `(i,j)` is the lexicographically first collision of minimum span `m`, no unchanged collision of smaller span exists, and no unchanged collision of span `m` appears before `(i,j)`.  The active collision is destroyed by nontrivial insertion. ∎

---

## C2.6. Bad insertion classification

Call an insertion position `k` bad if it is not strongly clean.

By Definition C1.4, badness means at least one of:

```text
B1. active collision is not destroyed;
B2. a new collision of span < m is created;
B3. a new collision of span m is created at or before the active location;
B4. an existing same-or-shorter earlier collision remains;
B5. boundary-rank worsens.
```

For nontrivial insertion `0<=k<m`, B1 is false except possibly `k=0`, where `Z` remains contiguous after `q` and the shifted duplicate `q+T_0=q+T_m` reproduces the zero interval after `q`.

B4 is impossible by Lemma C2.4.

Thus badness is caused by a local or external collision, except for boundary-rank bookkeeping.

---

## Lemma C2.5: every non-boundary bad insertion gives a routed obstruction

If a nontrivial insertion `R^{(k)}` is bad and the reason is not boundary-rank bookkeeping, then it creates one of:

```text
1. cross-side local collision routed by F4/F7;
2. same-side local collision contradicting shortestness or reproducing the zero block;
3. moved external collision routed by F6/F8;
4. weighted normal form routed by F10/F11.
```

### Proof

A bad insertion must create a new same-or-shorter collision or fail to destroy the active zero block.  Same-side local collisions are Lemma C2.1.  Cross-side local collisions are Lemma C2.2.  Moved external collisions are Lemma C2.3.  If the resulting signed relation preserves a coefficient-2 pattern after easy reductions fail, it is a weighted normal form handled by F10/F11. ∎

---

## C2.7. The k=0 endpoint issue

The insertion `k=0` gives

```text
X q Z Y.
```

The zero interval `Z` remains contiguous, merely shifted right of `q`.  Therefore `k=0` does not repair the active collision.

Similarly, if the adjacent atom is on the left and moved to the far right of `Z`, the zero block remains contiguous.

Thus the useful insertion positions are

```text
1<=k<m
```

when using the right-adjacent atom.

If `m=2`, there is only one useful insertion position:

```text
k=1.
```

---

## Lemma C2.6: useful insertion positions destroy the active zero block

For right-adjacent insertion, every position

```text
1<=k<m
```

places `q` strictly inside `Z`, so the original contiguous zero interval `Z` is destroyed.

### Proof

The block becomes

```text
z_1...z_k q z_{k+1}...z_m,
```

with both sides of `q` nonempty.  Hence `Z` is no longer contiguous. ∎

---

## C2.8. Candidate geometric theorem

## Theorem C2.7: q-through-Z obstruction theorem, conditional boundary form

Let `R` be `D_SNS^*`-minimal with active shortest zero interval `Z` of length `m>=2`, and let `q` be a right-adjacent outside atom.  Consider useful insertions `1<=k<m`.

If no useful insertion is strongly clean, then at least one useful insertion produces a routed obstruction of type:

```text
zero-composite,
signed interval,
pair-difference,
separated-equal,
external bridge,
recurrence,
weighted normal form,
or endpoint/boundary degeneracy.
```

### Proof

For each useful `k`, the active zero block is destroyed by Lemma C2.6.  Since the insertion is not strongly clean, and unchanged earlier same-or-shorter collisions are impossible by active minimality, badness must arise from a new local or external collision or from boundary-rank bookkeeping.  By Lemma C2.5, every non-boundary bad insertion gives a routed obstruction.  If all failures are boundary-rank failures, they form the endpoint/boundary degeneracy case. ∎

---

## C2.9. Remaining issue: existence of a useful insertion

If `m>=2`, useful positions `1<=k<m` exist.  Since `m=1` is impossible, every non-full active zero interval with right-adjacent `q` has at least one useful insertion.

Thus Theorem C2.7 produces a routed obstruction unless a useful insertion is strongly clean, which would contradict minimality by C1.9.

This is close to closing SNS.C1.

---

## C2.10. Boundary-rank degeneracy

The only residual non-algebraic failure mode is boundary-rank bookkeeping.  To eliminate it, define boundary rank so that moving `q` into the interior of `Z` cannot worsen boundary rank unless an endpoint collision, external collision, or recurrence is created.

Recommended convention:

```text
boundary_rank = 0 for interior insertion positions;
boundary_rank = 1 for endpoint-only insertion positions.
```

Since useful insertions are interior positions, this convention removes the boundary-rank exception.

---

## Lemma C2.8: interior useful insertions do not worsen boundary rank under interior-favored convention

With boundary rank defined by endpoint-degeneracy, every useful insertion `1<=k<m` has boundary rank no worse than the original endpoint-adjacent configuration.

### Proof

The original zero interval `Z` has `q` outside the interval boundary.  A useful insertion puts `q` strictly inside `Z`, away from the endpoint-only positions.  Under the convention that interior positions have minimal boundary rank, the boundary rank cannot worsen. ∎

---

## C2.11. Strong nonzero-sum start theorem, conditional on F3--F11

## Theorem C2.9: arbitrary collision-defect start enters the obstruction engine

Assume:

```text
1. sigma(S) != 0;
2. R is D_SNS^*-minimal;
3. boundary rank uses the interior-favored convention;
4. F3--F11 are valid.
```

If `R` is not already strong nonzero-sum, then the active shortest zero interval and an adjacent outside atom produce either:

```text
1. a strongly clean insertion, contradicting D_SNS^* minimality;
2. a routed obstruction handled by F3--F11;
3. terminal contradiction.
```

Therefore the arbitrary-ordering start can be connected to the existing obstruction engine.

### Proof

Let `Z` be the active shortest zero interval.  Since `sigma(S) != 0`, `Z` is not the whole ordering, so choose an adjacent outside atom `q`.  Since `m=1` is impossible, useful insertion positions exist.  If any useful insertion is strongly clean, C1.9 contradicts minimality.  If no useful insertion is strongly clean, Theorem C2.7 gives a routed obstruction or boundary degeneracy.  Boundary degeneracy is eliminated by Lemma C2.8. ∎

---

## C2.12. What remains after C2

C2 substantially sharpens the non-circular start.

Remaining tasks:

```text
1. Check that the definition of strong cleanliness exactly matches D_SNS^* descent.
2. Ensure every C2 routed obstruction matches an F3 class without assuming Graham-validity.
3. Decide whether zero intervals produced during C2 are defects or terminal contradictions.
4. Modify F4/F9 language so zero intervals from arbitrary-ordering start are treated as defect branches until the ordering is known collision-free.
5. Harden F3--F11 sign/endpoint audits.
```

The key conceptual issue is item 3: zero intervals are not terminal contradictions before strong nonzero-sum is established.  They are only contradictions inside a branch claiming a collision-free transformed ordering.

---

## C2.13. Recommended next file

The next file should reconcile the state machine with arbitrary-ordering starts:

```text
docs/final/F00_SNS_C3_state_machine_without_graham_validity.md
```

Goal:

```text
Allow zero-interval defects as repair states before Graham-validity is achieved,
without falsely treating them as contradictions.
```

---

## C2.14. Status

```text
Status: substantial repair draft.
Risk: ORANGE/RED.
Main remaining issue: adapt F3--F11 so initial zero-interval defects are repair states, not contradictions, until collision-freeness is established.
```
