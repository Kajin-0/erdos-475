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

where the forbidden hit occurs after an inserted atom and a nonempty prefix of the trailing zero-block side.

This note derives the H2 long-blocker pullback formulas and proves the non-crossing descent cases.

Correction status:

```text
This version incorporates the H2 endpoint-convention correction from:

docs/analytic_f7_h1_h2_sign_audit.md
```

The key point is that A5 at the H2 hit uses the endpoint immediately before the last atom of the hit prefix. Therefore if

```text
U = U^- u_*,
```

then left-blocker pullbacks use `U^-`, not full `U`.

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
Q=U V.
```

For the non-endpoint H2 case, write

```text
U = U^- u_*,
V = v_1 V^+,
```

where:

```text
u_* = last atom of U,
v_1 = first atom of V.
```

Thus:

```text
sum(Q)=sum(U^-)+u_*+v_1+sum(V^+)=-p.
```

The H2 forbidden hit is the endpoint after

```text
P q U = P q U^- u_*.
```

Thus H2 is

```text
x+p+q+sum(U)=f.
```

Assume the transformed ordering is Graham-valid and this forbidden hit is not earlier than the original minimal hit.

Let the source zero-block span be

```text
s=|P|+|Q|.
```

---

## 2. Applying A5 at the H2 hit

Let `H` be the endpoint after `P q U` in the transformed ordering.

The atom immediately before the H2 endpoint is:

```text
u_*.
```

The atom immediately after `H` is:

```text
v_1.
```

if `V` is nonempty.

If `V` is empty, then H2 occurs at the endpoint after `P q Q`; this is an endpoint branch treated separately below.

By A64, because the transformed ordering is recurrent, A5 gives a blocker index `j'` such that

```text
S'_{H-1}+v_1=S'_{j'}.
```

But

```text
S'_H=S'_{H-1}+u_*.
```

Therefore all left-blocker intervals ending at `H-1` stop before `u_*`, while all right-blocker intervals compare `v_1` against `u_*`.

Choose a nearest blocker. The long-blocker condition is

```text
|j'-H|+1 >= s.
```

---

# 3. Non-endpoint case: V nonempty

Assume first that `V` is nonempty.

The transformed local segment is

```text
P q U^- u_* v_1 V^+.
```

The H2 hit occurs after `P q U^- u_*`; the next atom is `v_1`.

There are left and right blockers.

---

## Lemma A67.1: left blocker inside U^- gives suffix-zero descent

If the A5 blocker lies inside the prefix `U^-`, then the left-blocker relation pulls back to

```text
sum(tail(U^- from blocker))+v_1=0.
```

This is a two-piece zero composite supported on a proper suffix of `U^-` plus the first atom of `V`, hence strictly smaller than the source zero block `P Q`.

If the blocker is exactly at the endpoint before `u_*`, the relation is

```text
v_1=0,
```

which is impossible because atoms lie in `F_p^*`.

### Proof

For a left blocker, A64.2 gives

```text
sum'(j',H-1]+v_1=0.
```

Since `H-1` is the endpoint immediately before `u_*`, a blocker inside `U^-` gives a suffix of `U^-`; a blocker at the endpoint immediately before `u_*` gives the empty suffix and hence `v_1=0`. ∎

---

## Lemma A67.2: left blocker inside q is impossible

There is no distinct partial-sum endpoint strictly inside the inserted atom `q`. Therefore a left A5 blocker cannot lie inside `q`.

### Proof

The ordering is discrete by atoms; endpoints occur only between atoms. ∎

---

## Lemma A67.3: left blocker inside P gives a zero-composite descent

If the left blocker lies inside `P`, then the pullback relation is

```text
sum(tail(P from blocker))+q+U^-+v_1=0.
```

This is a zero composite using a proper suffix of `P`, the inserted atom, the prefix `U^-`, and the first atom of `V`.

It has smaller support than `P Q` unless an exact support-tie boundary case occurs. Such exact ties are boundary-rank cases in A64 and route to the global recurrence machinery.

### Proof

The interval `(j',H-1]` runs from inside `P` through the end of `P q U^-`. Thus it is a proper suffix of `P`, followed by `q`, followed by `U^-`. Add the A5 atom `v_1`. ∎

---

## Lemma A67.4: left blocker before P gives a left bridge zero composite

If the left blocker lies before `P`, then its pullback is

```text
L+P+q+U^-+v_1=0,
```

where `L` is the external bridge ending at the start of `P`.

### Proof

The interval from the blocker to `H-1` contains the left bridge, all of `P`, the inserted atom `q`, and all of `U^-`. Add `v_1`. ∎

### Status

This is a crossing bridge branch. It is not automatically smaller and must be uncrossed against the corrected original zero relation

```text
P+U^-+u_*+v_1+V^+=0.
```

---

# 4. Right blockers in the non-endpoint case

For a right blocker, subtract the H2 endpoint. From

```text
S'_{H-1}+v_1=S'_{j'},
```

and

```text
S'_H=S'_{H-1}+u_*,
```

we get

```text
S'_{j'}-S'_H=v_1-u_*.
```

The interval from `H` to `j'` starts inside `V`.

Let `V_r` be the prefix of `V` ending at `j'` when `j'` lies inside `V`.

---

## Lemma A67.5: right blocker inside V gives a pair-difference prefix relation

If the right blocker lies inside `V`, and `V_r` is the prefix of `V` ending at the blocker, then

```text
V_r = v_1-u_*.
```

Equivalently,

```text
u_* - v_1 + V_r=0.
```

### Proof

The A5 relation compares the partial sum before `u_*` plus `v_1` with a later endpoint inside `V`. Moving from the H2 endpoint to the blocker accumulates a prefix of `V`. The difference between the A5 atom `v_1` and the hit atom `u_*` gives the displayed pair-difference prefix relation. ∎

### Endpoint cases

If the blocker is the first endpoint in `V`, then `V_r=v_1`, so the equation forces

```text
u_*=0,
```

impossible because atoms lie in `F_p^*`.

If the blocker lies in a proper prefix of `V`, this is a smaller pair-difference/zero-composite branch.

If it uses all of `V`, then

```text
V+u_*-v_1=0.
```

Since

```text
V=v_1+V^+,
```

this reduces to

```text
V^+ + u_*=0.
```

Thus the all-of-`V` endpoint case is a proper zero composite unless `V^+` is empty, in which case it forces `u_*=0`, impossible.

---

## Lemma A67.6: right blocker beyond V gives a right bridge zero/signed composite

If the right blocker lies after `V`, then the pullback has the form

```text
V+R = v_1-u_*,
```

where `R` is the external bridge after `Q` up to the blocker.

Equivalently,

```text
R+V+u_*-v_1=0.
```

Since `V=v_1+V^+`, this reduces to

```text
R+V^+ + u_*=0.
```

### Proof

The interval from the H2 endpoint to the blocker contains all remaining `V` and the external bridge `R`. Compare this interval to the A5 atom substitution `v_1-u_*`. ∎

### Status

This is the right bridge crossing branch, now in ordinary zero-composite form with a proper tail `V^+` and the hit atom `u_*`.

---

# 5. Non-crossing descent for H2

Call a blocker non-crossing if its pullback lies inside:

```text
P,
U^-,
or a proper prefix of V.
```

Call it crossing if it reaches outside `P Q` or uses all of `V`.

## Proposition A67.7: non-crossing H2 blockers descend after pullback

In atom-insertion H2 recurrence with `V` nonempty, every non-crossing A5 blocker pulls back to a strictly smaller zero-composite or pair-difference obstruction, except for boundary-rank tie cases already covered by A64.

### Proof

Inside-`U^-` blockers descend by Lemma A67.1. Inside-`P` blockers route to smaller zero-composite support by Lemma A67.3 except possible endpoint ties. Proper inside-`V` blockers descend by Lemma A67.5. ∎

---

# 6. Crossing cases for H2

After Proposition A67.7, a genuine H2 long-blocker recurrence must be one of:

```text
D1. left bridge before P:       L+P+q+U^-+v_1=0;
D2. right bridge after V:       R+V^+ + u_*=0;
D3. right blocker uses all V:   V^+ + u_*=0.
```

These route as follows.

---

## Lemma A67.8: D3 is a proper zero-composite or zero-atom contradiction

If the right blocker uses all of `V`, then

```text
V^+ + u_*=0.
```

If `V^+` is empty, this gives

```text
u_*=0,
```

which is impossible. Otherwise it is a two-piece zero composite using a proper tail of `V` plus the hit atom `u_*`.

### Proof

This is the all-of-`V` endpoint case of Lemma A67.5 after writing `V=v_1+V^+`. ∎

---

## Lemma A67.9: D1 left bridge gives a signed/equal relation with the complementary tail of Q

Use the corrected original zero relation

```text
P+U^-+u_*+v_1+V^+=0.
```

D1 is

```text
L+P+q+U^-+v_1=0.
```

Subtracting the original zero relation from D1 gives

```text
L+q-u_*-V^+=0.
```

Equivalently,

```text
V^+ = L+q-u_*.
```

Thus D1 routes to a signed/equal interval relation between the right tail `V^+` and the left bridge plus the atom correction `q-u_*`.

### Proof

Subtract `P+U^-+u_*+v_1+V^+=0` from `L+P+q+U^-+v_1=0`. ∎

---

## Lemma A67.10: D2 right bridge is a zero composite

D2 has form

```text
R+V^+ + u_*=0.
```

This is a bridge zero-composite involving the right bridge, a proper tail of `V`, and the hit atom `u_*`.

If `V^+` is empty, it reduces to

```text
R+u_*=0,
```

a two-piece bridge zero-composite.

### Proof

This is Lemma A67.6 after writing `V=v_1+V^+`. ∎

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

This is not a new atom-insertion branch. It is a singleton-prefix forbidden recurrence of the type handled in:

```text
docs/analytic_f7_singleton_endpoint_audit.md
```

### Proof

Use `sum(P)+sum(Q)=0`. ∎

---

# 8. H2 long-blocker theorem, corrected

## Proposition A67.12: H2 long-blocker recurrence is routed modulo existing mechanisms

Every H2 long-blocker recurrence is one of:

```text
1. non-crossing descent by Proposition A67.7;
2. endpoint singleton recurrence by Lemma A67.11;
3. D3 proper zero-composite or zero-atom contradiction by Lemma A67.8;
4. D1 signed/equal relation by Lemma A67.9;
5. D2 bridge zero-composite by Lemma A67.10.
```

Therefore H2 recurrence introduces no new local algebraic species beyond:

```text
zero-composite,
signed/equal interval,
singleton recurrence,
bridge/gap or external-collision routing,
A34 recurrence.
```

### Proof

The blocker cases partition into left/right and internal/external positions. The lemmas above route each case. ∎

---

# 9. Consequence for A34 atom-insertion recurrence

Combining A64--A67:

```text
H1 recurrence is routed modulo existing global mechanisms;
H2 recurrence is routed modulo existing global mechanisms with the corrected U^- / u_* convention;
bounded blockers descend;
long blockers reduce to crossing equal/signed/composite branches or singleton recurrence.
```

Thus atom-insertion recurrence is no longer an abstract A34 gap. It is reduced to the same global termination problem for routed classes.

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

The most natural next target is R3 because H1/H2 already route endpoint cases into pair-difference, zero-composite, signed/equal, and singleton recurrence machinery.

---

## Current status

Proved here:

```text
1. corrected H2 pullback formulas for left and right blockers;
2. non-crossing H2 blockers descend;
3. endpoint H2 reduces to singleton recurrence;
4. crossing H2 blockers route to signed/equal interval or zero-composite machinery;
5. the previous full-U H2 convention has been corrected to U^- / u_*.
```

Not proved here:

```text
1. full crossing bridge termination;
2. full A34 recurrence theorem;
3. weighted cut-selection theorem;
4. endpoint avoidance theorem.
```
