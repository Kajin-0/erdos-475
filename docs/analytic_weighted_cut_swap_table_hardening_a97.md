# Analytic weighted cut-swap table hardening A97

This note continues from A96.

A93 isolated five hardening obligations:

```text
U1. Strict progress lemma.
U2. Universal external-collision classification.
U3. Recurrence bounded-blocker measure.
U4. Cut-swap displayed collision table.
U5. Bridge/gap measure inequalities.
```

A94 addressed U1.  A95 addressed U2.  A96 addressed U3.  A97 addresses U4 by hardening the A60 weighted cut-swap displayed collision table.

The goal is to make explicit the collision equations for the weighted cut-swap

```text
A P R C -> A R P C
```

where `B=P R` is a proper cut of the weighted middle block in a genuine weighted core

```text
A + 2B + C = 0.
```

---

## 1. Standing weighted core

Let the original displayed segment be

```text
X A P R C Y
```

where

```text
B=P R,
P,R nonempty.
```

Write block sums

```text
a=sum(A),
p=sum(P),
r=sum(R),
c=sum(C),
b=p+r.
```

The genuine weighted core is

```text
a+2b+c=0,
```

or

```text
a+2p+2r+c=0.
```

The cut-swap is

```text
X A P R C Y -> X A R P C Y.
```

Let

```text
x=sum(X).
```

The total displayed segment sum is preserved:

```text
sum(A P R C)=sum(A R P C)=a+p+r+c.
```

---

## 2. Original displayed endpoint families

In the original order `A P R C`, displayed internal endpoint families are:

```text
A_i:         x + A_i,
P_j:         x + a + P_j,
R_k:         x + a + p + R_k,
C_l:         x + a + p + r + C_l.
```

Here `A_i`, `P_j`, `R_k`, and `C_l` denote nonempty prefixes of the corresponding blocks unless an endpoint case is explicitly included.

---

## 3. Transformed displayed endpoint families

In the transformed order `A R P C`, displayed endpoint families are:

```text
A_i:         x + A_i,                       unchanged
R_k':        x + a + R_k,
P_j':        x + a + r + P_j,
C_l':        x + a + r + p + C_l,           same as x+a+p+r+C_l
```

Thus the `A` and `C` endpoint families are unchanged as sets of field values relative to `x`, while the internal `P` and `R` families move.

Only collisions involving a moved `R_k'` or moved `P_j'` need to be displayed.  Collisions involving external endpoints are handled by A95.

---

## 4. Collision families to check

Displayed collisions in the transformed window can occur between:

```text
R_k' and A_i,
R_k' and original/unchanged C_l,
R_k' and transformed P_j',
P_j' and A_i,
P_j' and unchanged C_l,
P_j' and transformed R_k'.
```

The pair `R_k'` with `P_j'` is symmetric with `P_j'` with `R_k'`.

Collisions entirely within `A`, entirely within `P`, entirely within `R`, or entirely within `C` are inherited from the original Graham-valid ordering and are not new.

---

# 5. R-family collisions

## Lemma A97.1: collision `R_k' = A_i`

If

```text
x+a+R_k = x+A_i,
```

then

```text
a+R_k-A_i=0.
```

Equivalently, writing `A=A_i A^+` when `A_i` is a prefix of `A`,

```text
A^+ + R_k = 0.
```

if `A_i` is internal to `A` and `a-A_i=sum(A^+)`.

### Classification

This is a two-piece zero-composite supported on a tail of `A` and a prefix of `R`.  If `A_i=0` or `A_i=a` endpoint conventions are used, it becomes either:

```text
A+R_k=0,
R_k=0,
or tail(A)+R_k=0.
```

These route to zero-composite or zero-collapse machinery.

### Proof

Subtract `x`.  Then move `A_i` to the left and decompose `a-A_i` as the tail of `A`. ∎

---

## Lemma A97.2: collision `R_k' = C_l'`

If

```text
x+a+R_k = x+a+p+r+C_l,
```

then

```text
R_k=p+r+C_l.
```

Thus

```text
(p+r-R_k)+C_l=0.
```

Since `p+r-R_k` is `P` plus the tail of `R` after `R_k`, this is

```text
P + R^+_k + C_l = 0.
```

where `R=R_k R^+_k`.

### Classification

This is a two-piece or three-piece zero-composite involving `P`, a tail of `R`, and a prefix of `C`.

Endpoint cases:

```text
R_k=r       -> P + C_l = 0;
C_l=c       -> P + R^+_k + C = 0;
R_k=r,C_l=c -> P+C=0.
```

These route to zero-composite surgery or A56 adjacent-pair tests.

### Proof

Subtract the two endpoint expressions and decompose `r-R_k` as the tail of `R`. ∎

---

## Lemma A97.3: collision `R_k' = P_j'`

If

```text
x+a+R_k = x+a+r+P_j,
```

then

```text
R_k-r-P_j=0.
```

Equivalently,

```text
R^+_k + P_j = 0
```

with a sign convention, since `r-R_k=sum(R^+_k)`.

More explicitly:

```text
P_j + R^+_k = 0.
```

### Classification

This is a two-piece zero-composite across the cut boundary between `R` and `P` in the transformed order.  If one piece is empty, it is zero-collapse; if both are nonempty, it is controlled by zero-composite surgery.

### Proof

The equation gives `R_k-r=P_j`.  Since `R_k-r=-R^+_k`, this gives `P_j+R^+_k=0`. ∎

---

# 6. P-family collisions

## Lemma A97.4: collision `P_j' = A_i`

If

```text
x+a+r+P_j = x+A_i,
```

then

```text
a+r+P_j-A_i=0.
```

Writing `a-A_i=sum(A^+_i)`, this becomes

```text
A^+_i + R + P_j = 0.
```

### Classification

This is a two-piece or three-piece zero-composite involving a tail of `A`, all of `R`, and a prefix of `P`.

Endpoint cases route to:

```text
A+R+P_j=0,
R+P_j=0,
A^+_i+R+P=0,
```

all zero-composite or adjacent-pair branches.

### Proof

Subtract `x`, move `A_i`, and decompose `a-A_i`. ∎

---

## Lemma A97.5: collision `P_j' = C_l'`

If

```text
x+a+r+P_j = x+a+r+p+C_l,
```

then

```text
P_j=p+C_l.
```

Thus

```text
(p-P_j)+C_l=0.
```

Writing `P=P_j P^+_j`, this is

```text
P^+_j + C_l = 0.
```

### Classification

This is a two-piece zero-composite involving a tail of `P` and a prefix of `C`.

Endpoint cases:

```text
P_j=p       -> C_l=0, zero collapse;
C_l=c       -> P^+_j + C=0;
P_j=p,C_l=c -> C=0, zero collapse if C nonempty.
```

### Proof

Subtract the endpoint expressions and decompose `p-P_j` as the tail of `P`. ∎

---

## Lemma A97.6: collision `P_j' = R_k'`

This is the same as Lemma A97.3.  It gives

```text
P_j + R^+_k = 0.
```

### Classification

Two-piece zero-composite or zero-collapse.

---

# 7. Collision with original positions of moved families

The transformed moved families may also collide with old endpoint values that are not in the displayed transformed family but are present elsewhere in the original proof bookkeeping.

The two important comparisons are:

```text
x+a+R_k  vs old x+a+P_j,
x+a+r+P_j vs old x+a+p+R_k.
```

These are not collisions inside the final transformed ordering unless the old endpoint value is also present as an unchanged endpoint.  However, they occur in pullback calculations.

---

## Lemma A97.7: moved R against old P gives signed pair-difference

If

```text
x+a+R_k = x+a+P_j,
```

then

```text
R_k-P_j=0.
```

This is an equal-prefix relation between `R` and `P`.

### Classification

If the prefixes are disjoint, it is separated-equal inside `B`.  If adjacent or overlapping under a cut convention, it routes to midpoint/equal interval or zero-composite.

---

## Lemma A97.8: moved P against old R gives signed pair-difference

If

```text
x+a+r+P_j = x+a+p+R_k,
```

then

```text
r+P_j-p-R_k=0.
```

Equivalently,

```text
R^+_k + P_j = P^+_j + R_k
```

depending on tail decomposition.

### Classification

This is a signed interval relation across the cut.  It routes to equal/signed interval machinery, transported-prefix tests, or weighted-core return if the coefficient-2 pattern survives.

---

# 8. Forbidden-hit equations for the cut-swap

If the transformed ordering is Graham-valid but recurrent, the new forbidden hit must occur in a moved family:

```text
H_R(k): x+a+R_k=f,
H_P(j): x+a+r+P_j=f.
```

The unchanged `A` and `C` families cannot create new forbidden hits unless they already hit `f` before the move.

---

## Lemma A97.9: cut-swap recurrence is moved-prefix recurrence

Every new forbidden hit from the cut-swap is a moved-prefix hit of type `H_R` or `H_P`.

### Classification

Apply A5 at the hit.  The blocker pullback is then handled by:

```text
A64 bounded-blocker theorem;
A69 pair-swap / moved-prefix recurrence if atom-level;
A70 singleton-prefix recurrence;
A71 cyclic recurrence if the cut is interpreted cyclically;
A95 external collision if the blocker is external.
```

### Proof

Only `R_k'` and `P_j'` moved.  Therefore only those endpoint families can newly hit `f`. ∎

---

# 9. Weighted-core return equations

A displayed collision table can return to a weighted relation only if the collision equation contains a surviving coefficient-2 structure after zero-composite and transported-prefix tests fail.

The possible source is a signed relation comparing moved and old cut-boundary pieces, such as Lemma A97.8.

---

## Lemma A97.10: displayed cut-swap collisions produce weighted return only through signed boundary relations

The direct displayed collisions of transformed families with `A` or `C` endpoints produce zero-composite branches.  A genuine weighted-core return can only arise from signed boundary relations comparing moved `P` and `R` data, after A56 easy reductions fail.

### Proof

Lemmas A97.1--A97.6 produce equations with all coefficients `+1` after tail decomposition; these are zero-composites.  Coefficient-2 behavior can only appear when comparing old and new positions of cut pieces, where one side contains `P` or `R` in both the moved and original representation.  Those are signed boundary relations of Lemmas A97.7--A97.8. ∎

---

## 10. Displayed collision table summary

| Collision | Equation | Class |
|---|---|---|
| `R_k' = A_i` | `A_i^+ + R_k = 0` | zero-composite |
| `R_k' = C_l'` | `P + R_k^+ + C_l = 0` | zero-composite |
| `R_k' = P_j'` | `P_j + R_k^+ = 0` | two-piece zero |
| `P_j' = A_i` | `A_i^+ + R + P_j = 0` | zero-composite |
| `P_j' = C_l'` | `P_j^+ + C_l = 0` | two-piece zero |
| `P_j' = R_k'` | `P_j + R_k^+ = 0` | two-piece zero |
| moved `R` vs old `P` | `R_k=P_j` | equal interval / separated-equal |
| moved `P` vs old `R` | signed cut-boundary relation | signed interval / possible weighted return |
| moved family hits `f` | `x+a+R_k=f` or `x+a+r+P_j=f` | recurrence |

---

## 11. Endpoint and empty-block cases

The cut requires:

```text
P,R nonempty.
```

Prefixes such as `P_j`, `R_k`, `A_i`, `C_l` may be:

```text
proper nonempty prefixes in displayed collision tables;
full prefixes when endpoint cases are included;
empty only if boundary endpoint comparisons are explicitly added.
```

Endpoint cases route as follows:

```text
empty prefix causing equation 0=atom/block sum -> zero collapse or boundary branch;
full prefix causing tail empty -> lower-piece zero-composite;
A or C empty -> endpoint weighted case, handled by A80/A81 or A56.
```

No endpoint case creates a new transition type.

---

## 12. Hardened A60 theorem

## Theorem A97.11: weighted cut-swap displayed collisions are classified

For the weighted cut-swap

```text
A P R C -> A R P C,
```

with `P,R` nonempty, every displayed collision in the transformed window is one of:

```text
1. zero-composite;
2. two-piece zero;
3. equal/separated interval;
4. signed interval / transported-prefix candidate;
5. weighted-core return through signed boundary relation;
6. forbidden recurrence;
7. endpoint zero-collapse.
```

External collisions are not part of the displayed table and are handled by A95.

### Proof

The transformed moved endpoint families are `R_k'` and `P_j'`.  Collisions involving these families with displayed `A`, `C`, and each other are Lemmas A97.1--A97.6.  Pullback comparisons with old moved-family positions are Lemmas A97.7--A97.8.  New forbidden hits are Lemma A97.9.  Weighted returns are restricted by Lemma A97.10.  Endpoint cases are Section 11. ∎

---

## 13. Consequence for weighted proof

A97 hardens U4 at the displayed-table level:

```text
A60 cut-swap displayed collisions introduce no new obstruction species.
```

The only weighted-return channel is the signed boundary channel already isolated in A79--A94.

---

## 14. Remaining hardening item

Only one of the A93 hardening items remains:

```text
U5. A74--A77 bridge/gap measure inequalities.
```

Also still needed:

```text
span convention audit across recurrence sources;
final proof extraction.
```

---

## 15. Target A98

A98 should harden A74--A77:

```text
bridge/gap measure inequalities.
```

Required output:

```text
1. define bridge span, gap length, and support size consistently;
2. prove proper overlap decreases span;
3. prove proper containment decreases support/span;
4. prove equal-span separated bridge returns reduce gap or enter recurrence;
5. prove gap-preserving recurrence reduces to rigid separated self-return;
6. prove rigid separated self-return routes to direct exchange/recurrence without preserving the same measure.
```

---

## Current status after A97

Proved/recorded here:

```text
1. displayed endpoint families for A P R C -> A R P C;
2. all moved-family collision equations;
3. zero-composite classification for direct displayed collisions;
4. signed boundary channel for possible weighted return;
5. cut-swap recurrence equations;
6. endpoint/empty-block handling;
7. hardened A60 displayed collision theorem.
```

Still open:

```text
1. A74--A77 bridge/gap inequality hardening;
2. recurrence span convention audit;
3. final extraction.
```
