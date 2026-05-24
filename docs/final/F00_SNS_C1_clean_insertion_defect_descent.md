# F00.SNS.C1 clean insertion defect descent

This file continues the strong nonzero-sum repair path from `F00_SNS_arbitrary_collision_defect.md`.

The remaining bookkeeping lemma was:

```text
SNS.C1:
clean insertion of an adjacent outside atom q into the active shortest zero interval
strictly decreases the refined collision-defect vector.
```

This file sharpens the defect vector and proves the clean-insertion descent under a precise definition of clean insertion.  It also identifies the exact remaining issue: if an unchanged shortest collision exists elsewhere, the defect vector must prioritize the active collision location in a way that still gives descent.

Status: repair draft, partially hardened.

---

## C1.1. Collision data

Let

```text
R=(r_1,...,r_t)
```

be an ordering of `S`, with extended partial sums

```text
S_0=0,
S_i=r_1+...+r_i,
1<=i<=t.
```

A collision is a pair

```text
(i,j), 0<=i<j<=t,
```

such that

```text
S_i=S_j.
```

Its span is

```text
span(i,j)=j-i.
```

Its zero interval is

```text
Z(i,j)=r_{i+1}...r_j.
```

---

## C1.2. Collision profile

Instead of tracking only the shortest span and number of shortest collisions, define the full collision profile.

## Definition C1.1: collision profile

For an ordering `R`, define

```text
P_col(R)=(N_1(R),N_2(R),...,N_t(R)),
```

where

```text
N_s(R)=number of collision pairs (i,j) with j-i=s.
```

Thus:

```text
R is strong nonzero-sum iff P_col(R)=(0,0,...,0).
```

Order collision profiles lexicographically from small spans to large spans:

```text
P_col(R) < P_col(R')
```

if at the first span `s` where they differ,

```text
N_s(R)<N_s(R').
```

This prioritizes eliminating the shortest zero intervals first.

---

## C1.3. Location refinement

If two orderings have the same collision profile, use the lexicographically first collision location as a tie-breaker.

Define:

```text
L_col(R)=lexicographically first collision pair (i,j)
         among all collision pairs of minimum positive span,
```

with sentinel value

```text
L_col(R)=(t+1,t+1)
```

if no collision exists.

The location order is lexicographic:

```text
(i,j)<(i',j') iff i<i' or (i=i' and j<j').
```

For minimization, we prefer larger location after profile equality only when the earlier active collision has been eliminated.  To keep ordinary lexicographic minimization over nonnegative integers, define the reversed location coordinate:

```text
L_col^*(R)=(t+1-i, t+1-j).
```

Then moving the first remaining shortest collision to the right decreases `L_col^*`.

---

## C1.4. Refined SNS defect vector

## Definition C1.2: final refined collision-defect vector

Define

```text
D_SNS^*(R)=(
  P_col(R),
  L_col^*(R),
  boundary_rank(R)
).
```

The order is lexicographic, where `P_col` is itself lexicographic from span `1` to span `t`.

Since there are finitely many orderings and finitely many possible profiles, a minimizer exists.

## Lemma C1.3: refined minimizer exists

Among all orderings of finite `S`, there exists an ordering minimizing `D_SNS^*`.

### Proof

There are finitely many orderings.  Each `D_SNS^*` is a finite tuple of nonnegative integers. ∎

---

## C1.5. Active shortest zero interval

Let `R` be a `D_SNS^*`-minimal ordering.  If `R` is not strong nonzero-sum, let

```text
(i,j)=L_col(R)
```

be the active shortest collision, and set

```text
Z=r_{i+1}...r_j=z_1...z_m,
m=j-i.
```

Then:

```text
sum(Z)=0.
```

If `sigma(S) != 0`, then `Z` is not the whole ordering.  Therefore at least one adjacent outside atom exists.

Assume the right-adjacent orientation:

```text
R=X Z q Y.
```

The left-adjacent orientation is symmetric.

---

## C1.6. Insertion operation

For `0<=k<m`, define `R^{(k)}` by inserting `q` after the prefix `z_1...z_k`:

```text
R^{(k)} = X z_1...z_k q z_{k+1}...z_m Y.
```

The case `k=m` is the original ordering and is excluded from repair.

Let the affected atom window be

```text
W=Z q.
```

All atoms outside `W` remain in the same relative order and at the same positions outside the changed window.

---

## C1.7. Clean insertion, strong form

The earlier definition of clean insertion only forbade collisions involving the local window.  For defect descent, use a stronger definition.

## Definition C1.4: strongly clean insertion

An insertion `R^{(k)}` is strongly clean if:

```text
1. the active collision interval Z is destroyed;
2. no new collision pair of span <= m is created;
3. no collision pair of span < m is created;
4. every collision pair of span m in R^{(k)} is either an unchanged collision from R outside W or occurs strictly to the right of the old active pair location (i,j).
```

This definition is designed exactly to guarantee descent of `D_SNS^*`.

---

## Lemma C1.5: strongly clean insertion decreases D_SNS^*

If `R^{(k)}` is a strongly clean nontrivial insertion into the active shortest zero interval of `R`, then

```text
D_SNS^*(R^{(k)}) < D_SNS^*(R).
```

### Proof

Let `m` be the active shortest collision span of `R`.

Since `R` is active-minimal, there are no collisions of span `<m` in `R`.  By strong cleanliness, none are created in `R^{(k)}`.  Thus

```text
N_s(R^{(k)})=N_s(R)=0
```

for all `s<m`.

The active collision pair `(i,j)` of span `m` is destroyed.  Strong cleanliness creates no new span-`m` collision at or before `(i,j)`.  Therefore either:

```text
N_m(R^{(k)})<N_m(R),
```

or `N_m` is unchanged but the lexicographically first span-`m` collision has moved strictly to the right, which decreases `L_col^*`.

If `N_m` decreases, the collision profile `P_col` decreases.  If `N_m` is unchanged but the first span-`m` collision moves right, then `P_col` is unchanged and `L_col^*` decreases.  In either case, `D_SNS^*` strictly decreases. ∎

---

## C1.8. Weak clean insertion is insufficient

A weakly clean insertion, meaning only “no collision involving the local window,” is not enough to guarantee `D_SNS^*` decreases if unchanged earlier shortest collisions remain elsewhere.

## Lemma C1.6: weak cleanliness does not imply defect descent

If there is an unchanged collision of the same minimum span lexicographically before the active collision, then removing the active collision does not improve the location tie-breaker.

### Proof

The collision profile may decrease only if the active collision was the unique shortest collision.  If another same-span collision remains and is lexicographically earlier, then the active location does not move right.  Thus no strict descent follows from weak cleanliness alone. ∎

### Consequence

The active collision must be chosen as the lexicographically first shortest collision, and the insertion must not create any new same-or-shorter collision at or before that location.

---

## C1.9. What must be proved geometrically

The actual geometric repair lemma should therefore be stated as follows.

## Needed Lemma C1.7: existence of obstruction or strongly clean insertion

Let `R` be `D_SNS^*`-minimal with active shortest zero interval `Z`, and let `q` be an adjacent outside atom.  Then either:

```text
1. some nontrivial insertion of q into Z is strongly clean;
2. every nontrivial insertion creates an internal collision routed by F4/F5/F7;
3. every nontrivial insertion creates an external collision routed by F6/F8;
4. the insertion process creates a weighted normal form routed by F10/F11;
5. or a structural contradiction occurs.
```

### Status

Open.  This is now the exact remaining geometric lemma for the strong nonzero-sum start.

---

## C1.10. Internal collision classification remains valid

If an insertion is not strongly clean because it creates a same-or-shorter collision involving the local window, the previous F00.SNS classification applies.

## Lemma C1.8: local failure of strong cleanliness routes to F3

If an insertion of `q` into `Z` creates a collision of span `<=m` involving at least one endpoint inside the affected local window, then the collision routes to one of:

```text
zero-composite,
equal interval,
signed interval,
pair-difference,
separated-equal,
recurrence,
external collision,
weighted normal form.
```

### Proof

Use the local endpoint formulas from F00.SNS.  Same-side endpoint collisions give proper zero subintervals of `Z`, impossible by shortestness unless they involve the full active interval.  Cross-side collisions include `q` and yield signed or pair-difference relations.  Collisions with endpoints outside the window are external.  If the obstruction appears only after moving `q` stepwise, the adjacent swap recurrence machinery applies. ∎

---

## C1.11. Nonlocal unchanged collisions

The only obstruction not controlled by local algebra is an unchanged collision elsewhere.  But unchanged collisions are already included in the profile of `R`.

If the insertion destroys the active collision and does not create any same-or-shorter local collision, then unchanged collisions cannot make the profile worse.  They can only prevent the profile from improving enough unless the active collision was unique or the location tie-breaker improves.

This is why `D_SNS^*` uses both collision profile and reversed first-collision location.

---

## C1.12. Conditional descent theorem

## Theorem C1.9: clean insertion descent, conditional on strong cleanliness

Let `R` be a `D_SNS^*`-minimal ordering with active shortest zero interval `Z`.  If there exists a strongly clean nontrivial insertion of an adjacent outside atom `q` into `Z`, then `R` was not defect-minimal.

### Proof

By Lemma C1.5, the strongly clean insertion produces an ordering with strictly smaller `D_SNS^*`, contradicting the minimality of `R`. ∎

---

## C1.13. Conditional strong nonzero-sum start

## Theorem C1.10: SNS arbitrary start, reduced form

Assume Needed Lemma C1.7.  Let `S subset F_p^*` satisfy `sigma(S) != 0`.  Then either a strong nonzero-sum ordering exists, or the F3--F11 obstruction engine produces a terminal contradiction/success.

### Proof

Choose a `D_SNS^*`-minimal ordering.  If it has no collisions, it is strong nonzero-sum.  If it has a collision, choose the active shortest zero interval `Z`.  Since `sigma(S) != 0`, `Z` is not the whole ordering, so an adjacent outside atom exists.  Apply Needed Lemma C1.7.  A strongly clean insertion contradicts minimality by Theorem C1.9.  All obstructed insertion alternatives enter the F3 state machine and terminate by F9/F11 once those are fully hardened. ∎

---

## C1.14. What is actually solved here

Solved here:

```text
1. weak cleanliness was shown insufficient;
2. a stronger clean-insertion definition was introduced;
3. strongly clean insertion was proved to decrease the refined defect vector;
4. the remaining geometric burden was isolated as Needed Lemma C1.7.
```

Not solved here:

```text
Needed Lemma C1.7: existence of either strongly clean insertion or routed obstruction.
```

---

## C1.15. Recommended next file

The next file should attack Needed Lemma C1.7 geometrically:

```text
docs/final/F00_SNS_C2_q_through_zero_interval_obstruction.md
```

Minimum contents:

```text
1. endpoint formulas for all q insertion positions;
2. prove if no position is strongly clean, then a local collision or external collision exists;
3. classify first failed insertion;
4. derive explicit obstruction equations;
5. connect to F4--F11.
```

---

## C1.16. Status

```text
Status: partially hardened repair lemma.
Risk: RED.
Current remaining gap: Needed Lemma C1.7.
```
