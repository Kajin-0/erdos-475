# Analytic long-blocker uncrossing A67: atom-insertion H2

This note continues from A65--A66.

A65--A66 handled atom-insertion H1 recurrence:

```text
x+sum(P)+q=f.
```

The second atom-insertion forbidden branch is H2:

```text
x+sum(P)+q+Q_j=f.
```

where the forbidden hit occurs after an inserted atom and a nonempty prefix of the trailing zero-block side.  This note derives the H2 long-blocker pullback formulas and proves the non-crossing descent cases.

The bridge-crossing cases remain routed but not globally terminated; they reduce to equal/separated interval, zero-composite, or pair-difference machinery plus A34.

---

## 1. Standing atom-insertion setup

Start with a zero block

```text
P Q
```

with

```text
sum(P)+sum(Q)=0.
```

Insert an outside atom `q` between `P` and `Q`:

```text
X P Q q Y -> X P q Q Y.
```

Let

```text
p=sum(P),
q=sum(q),
Q=U V,
```

where

```text
U=prefix_j(Q),
V=tail_j(Q),
1 <= j < |Q| or j=|Q|.
```

Write

```text
u=sum(U),
v=sum(V),
u+v=sum(Q)=-p.
```

The H2 forbidden hit is the endpoint after

```text
P q U.
```

Thus H2 is

```text
x+p+q+u=f.
```

Assume the transformed ordering is Graham-valid and this forbidden hit is not earlier than the original minimal hit.

Let the source zero-block span be

```text
s=|P|+|Q|.
```

---

## 2. Applying A5 at the H2 hit

Let `H` be the endpoint after `P q U` in the transformed ordering.

The atom immediately after `H` is:

```text
v_1 = first atom of V,
```

if `V` is nonempty.

If `V` is empty, then H2 occurs at the endpoint after `P q Q`; this is an endpoint branch treated separately below.

By A64, because the transformed ordering is recurrent, A5 gives a blocker index `j'` such that

```text
S'_{H-1}+v_1=S'_{j'}.
```

Choose a nearest blocker.  The long-blocker condition is

```text
|j'-H|+1 >= s.
```

---

# 3. Non-endpoint case: V nonempty

Assume first that `V` is nonempty.

The transformed local segment is

```text
P q U V.
```

The H2 hit occurs after `P q U`; the next atom is `v_1`.

There are left and right blockers.

---

## Lemma A67.1: left blocker inside U gives suffix-zero descent

If the A5 blocker lies inside the prefix `U`, then the left-blocker relation pulls back to

```text
sum(tail(U from blocker))+v_1=0.
```

This is a two-piece zero composite supported on a proper suffix of `U` plus the first atom of `V`, hence strictly smaller than the source zero block `P Q`.

### Proof

For a left blocker, A64.2 gives

```text
sum'(j',H-1]+v_1=0.
```

If `j'` lies inside `U`, then `(j',H-1]` is a proper suffix of `U`.  Adding `v_1` gives the displayed two-piece zero relation.  Its support is contained in `U V`, and uses a proper suffix of `U`; it is strictly smaller than `P Q` unless `P` is empty and the suffix is all of `Q`, which cannot occur because the blocker lies inside `U` and `V` is nonempty. ∎

---

## Lemma A67.2: left blocker inside q is impossible

There is no distinct partial-sum endpoint strictly inside the inserted atom `q`.  Therefore a left A5 blocker cannot lie inside `q`.

### Proof

The ordering is discrete by atoms; endpoints occur only between atoms. ∎

---

## Lemma A67.3: left blocker inside P gives a three-piece zero descent

If the left blocker lies inside `P`, then the pullback relation is

```text
sum(tail(P from blocker))+q+U+v_1=0.
```

This is a zero composite using a proper suffix of `P`, the inserted atom, the prefix `U`, and the first atom of `V`.

It has smaller support than `P Q` unless `U` is almost all of `Q` and the suffix is almost all of `P`; the tied endpoint case is a boundary recurrence routed to A34.

### Proof

The interval `(j',H-1]` runs from inside `P` through the end of `P q U`.  Thus it is a proper suffix of `P`, followed by `q`, followed by `U`.  Add the A5 atom `v_1`. ∎

### Status

This is controlled by zero-composite surgery unless the support tie is exact; exact ties are boundary-rank cases in A64.

---

## Lemma A67.4: left blocker before P gives a left bridge zero composite

If the left blocker lies before `P`, then its pullback is

```text
L+P+q+U+v_1=0,
```

where `L` is the external bridge ending at the start of `P`.

### Proof

The interval from the blocker to `H-1` contains the left bridge, all of `P`, the inserted atom `q`, and all of `U`.  Add `v_1`. ∎

### Status

This is a crossing bridge branch.  It is not automatically smaller and must be uncrossed against the original zero relation `P+U+V=0`.

---

# 4. Right blockers in the non-endpoint case

For a right blocker, subtract the H2 endpoint.  From

```text
S'_{H-1}+v_1=S'_{j'},
```

and

```text
S'_H=S'_{H-1}+u_j
```

where the H2 endpoint atom is the last atom of `U`, it is cleaner to use the total prefix notation.  The interval from `H` to `j'` starts inside `V`.

Let `V_r` be the prefix of `V` ending at `j'` when `j'` lies inside `V`.

---

## Lemma A67.5: right blocker inside V gives a pair-difference prefix relation

If the right blocker lies inside `V`, and `V_r` is the prefix of `V` ending at the blocker, then

```text
V_r = v_1 - u_j,
```

where `u_j` is the last atom of `U`.

Equivalently,

```text
u_j - v_1 + V_r=0.
```

### Proof

The A5 relation compares the partial sum before the last atom of `U` plus `v_1` with a later endpoint inside `V`.  Moving from the H2 endpoint to the blocker accumulates a prefix of `V`.  The difference between the A5 atom `v_1` and the last hit atom `u_j` gives the displayed pair-difference prefix relation. ∎

### Endpoint cases

If the blocker is the first endpoint in `V`, then `V_r=v_1`, so the equation forces `u_j=0`, impossible.

If the blocker lies in a proper prefix of `V`, this is a smaller pair-difference/zero-composite branch.

If it uses all of `V`, it is an endpoint pair-difference branch involving `U` and `V`.

---

## Lemma A67.6: right blocker beyond V gives a right bridge zero/signed composite

If the right blocker lies after `V`, then the pullback has the form

```text
V + R = v_1-u_j,
```

where `R` is the external bridge after `Q` up to the blocker.

Equivalently,

```text
R+V+u_j-v_1=0.
```

### Proof

The interval from the H2 endpoint to the blocker contains all remaining `V` and the external bridge `R`.  Compare this interval to the A5 atom substitution `v_1-u_j`. ∎

### Status

This is the right bridge crossing branch.

---

# 5. Non-crossing descent for H2

Call a blocker non-crossing if its pullback lies inside:

```text
P,
U,
or a proper prefix of V.
```

Call it crossing if it reaches outside `P Q` or uses all of `V` in the endpoint pair-difference case.

## Proposition A67.7: non-crossing H2 blockers descend after pullback

In atom-insertion H2 recurrence with `V` nonempty, every non-crossing A5 blocker pulls back to a strictly smaller zero-composite or pair-difference obstruction, except for boundary-rank tie cases already covered by A64.

### Proof

Inside-`U` blockers descend by Lemma A67.1.  Inside-`P` blockers route to smaller zero-composite support by Lemma A67.3 except possible endpoint ties.  Proper inside-`V` blockers descend by Lemma A67.5. ∎

---

# 6. Crossing cases for H2

After Proposition A67.7, a genuine H2 long-blocker recurrence must be one of:

```text
D1. left bridge before P:       L+P+q+U+v_1=0;
D2. right bridge after V:       R+V+u_j-v_1=0;
D3. right blocker uses all V:   V+u_j-v_1=0.
```

These route as follows.

---

## Lemma A67.8: D3 is a pair-difference boundary branch

If the right blocker uses all of `V`, then

```text
V+u_j-v_1=0,
```

or

```text
v_1-u_j=sum(V).
```

This is a pair-difference boundary branch analogous to A33.

### Proof

This is the endpoint case of Lemma A67.5. ∎

---

## Lemma A67.9: D1 left bridge implies an equal/signed relation with the complementary tail of Q

Use the original zero relation

```text
P+U+V=0.
```

D1 is

```text
L+P+q+U+v_1=0.
```

Subtracting the original zero relation from D1 gives

```text
L+q+v_1-V=0.
```

Equivalently,

```text
V = L+q+v_1.
```

Thus D1 routes to a signed/equal interval relation between the right tail `V` and the left bridge plus two atoms.

### Proof

Subtract `P+U+V=0` from `L+P+q+U+v_1=0`. ∎

---

## Lemma A67.10: D2 right bridge is already a zero/signed composite

D2 has form

```text
R+V+u_j-v_1=0.
```

This is a bridge composite plus a pair-difference correction.  It routes to the pair-difference/zero-composite machinery.  If `V` is empty this case belongs to the endpoint branch below; if `V` is nonempty, the support contains a proper tail of `Q` and can be uncrossed with `P+U+V=0`.

### Proof

The equation is already in signed zero-composite form. ∎

---

# 7. Endpoint H2 branch: V empty

If `V` is empty, then H2 occurs after the endpoint

```text
P q Q.
```

The H2 hit is

```text
x+p+q+sum(Q)=x+q.
```

Since `P+Q=0`.

Thus endpoint H2 is simply the atom landing

```text
x+q=f.
```

## Lemma A67.11: endpoint H2 is a singleton recurrence branch

When `j=|Q|`, H2 reduces to

```text
x+q=f.
```

This is not a new atom-insertion branch.  It is a singleton-prefix forbidden recurrence of the type already present in A14/A17/A34.

### Proof

Use `sum(P)+sum(Q)=0`. ∎

---

# 8. H2 long-blocker theorem, partial

## Proposition A67.12: H2 long-blocker recurrence is routed modulo existing mechanisms

Every H2 long-blocker recurrence is one of:

```text
1. non-crossing descent by Proposition A67.7;
2. endpoint singleton recurrence by Lemma A67.11;
3. pair-difference boundary by Lemma A67.8;
4. bridge signed/equal relation by Lemma A67.9;
5. bridge zero/signed composite by Lemma A67.10.
```

Therefore H2 recurrence introduces no new local algebraic species beyond:

```text
zero-composite,
signed/equal interval,
pair-difference,
singleton recurrence,
A34 recurrence.
```

### Proof

The blocker cases partition into left/right and internal/external positions.  The lemmas above route each case. ∎

---

# 9. Consequence for A34 atom-insertion recurrence

Combining A64--A67:

```text
H1 recurrence is routed modulo existing global mechanisms;
H2 recurrence is routed modulo existing global mechanisms;
bounded blockers descend;
long blockers reduce to crossing equal/signed/composite/pair branches.
```

Thus atom-insertion recurrence is no longer an abstract A34 gap.  It is reduced to the same global termination problem for routed classes.

---

# 10. Target A68

A68 should update the recurrence status map:

```text
A34 recurrence obligations R1/R2 are routed modulo crossing uncrossing and global termination.
```

Then the next recurrence sources are:

```text
R3. A33 Q2 pair-swap forbidden recurrence;
R4. singleton-prefix recurrence;
R5. cyclic-cut recurrence.
```

The most natural next target is R3 because H1/H2 already route endpoint cases into A33 pair-difference machinery.

---

## Current status

Proved here:

1. H2 pullback formulas for left and right blockers;
2. non-crossing H2 blockers descend;
3. endpoint H2 reduces to singleton recurrence;
4. crossing H2 blockers route to signed/equal interval, zero-composite, or pair-difference machinery.

Not proved here:

1. full crossing bridge termination;
2. full A34 recurrence theorem;
3. weighted cut-selection theorem;
4. endpoint avoidance theorem.
