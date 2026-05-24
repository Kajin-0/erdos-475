# Analytic first-changed-endpoint lemma A91

This note continues from A90.

A90 reduced the remaining weighted bottleneck to the first-changed-endpoint lemma:

```text
same outer blocks + same middle support + changed internal endpoint set
    -> internal non-weighted obstruction or smaller weighted core.
```

A91 formulates and partially hardens this lemma.

The main point is structural.  A changed internal endpoint pattern cannot be invisible if the return is realized through a finite sequence of local moves, each of which is either Graham-valid or has a first collision/forbidden hit.  The first endpoint-pattern change produces one of:

```text
internal zero interval,
internal equal interval,
pair-difference boundary,
singleton/prefix recurrence,
external collision,
or a smaller weighted-middle return.
```

This is enough to support the A90 weak-to-pattern reduction, provided the return process is explicitly represented as such a finite local-move path.

---

## 1. Standing weighted setup

Let

```text
X A B C Y
```

be a genuine weighted core:

```text
a+2b+c=0,
```

with

```text
a=sum(A),
b=sum(B),
c=sum(C),
|B|>=2.
```

Let

```text
B=b_1...b_n.
```

Internal partial sums of `B` are

```text
T_0=0,
T_i=b_1+...+b_i,
1<=i<=n.
```

The internal endpoint set is

```text
E_B={T_0,...,T_n}.
```

Assume `B` has no internal zero interval, so these endpoints are distinct.

---

## 2. Return-path model

A weak cut-rigid return is produced by:

```text
1. choosing a proper cut B=P R;
2. applying the cut-swap P R -> R P;
3. following the routed obstruction process until a weighted core returns.
```

For A91, model the routed process as a finite sequence of displayed local states:

```text
Omega_0, Omega_1, ..., Omega_N.
```

Here:

```text
Omega_0 = original weighted core state on A B C;
Omega_1 = cut-swapped state on A R P C;
Omega_N = returned weighted core state with same A,C and same middle support B.
```

Each transition is one of:

```text
adjacent atom swap;
block swap;
cyclic cut;
atom insertion/removal surrogate used in routing;
A5 blocker pullback normalization;
external collision pullback.
```

This model must be made explicit in the final proof.  A91 assumes such a finite return path exists.

---

## 3. Internal endpoint patterns along the return path

For each state `Omega_s`, define the internal endpoint set of the current middle support `B` relative to the same outer basepoint:

```text
E_s={T^{(s)}_0,...,T^{(s)}_n}.
```

The support set is the same middle interval `B`, but its internal order or endpoint pattern may change during the return.

Assume:

```text
E_0 != E_N.
```

Then there is a first index

```text
s_* = min{s : E_s != E_0}.
```

Thus

```text
E_{s_*-1}=E_0,
E_{s_*} != E_0.
```

---

## Lemma A91.1: first endpoint-pattern change exists

If a weak return has the same middle support but changed internal endpoint set, then a first endpoint-pattern change `s_*` exists.

### Proof

The return path is finite and `E_0 != E_N`.  Therefore the set of indices with `E_s != E_0` is nonempty and has a least element. ∎

---

# 4. What can cause the first endpoint change?

At the first change, the transition

```text
Omega_{s_*-1} -> Omega_{s_*}
```

changes at least one internal endpoint value of `B`.

There are only four structural mechanisms:

```text
M1. a local swap changes the order of two adjacent internal pieces;
M2. a cyclic cut changes the basepoint of the internal order;
M3. a normalization changes which interval is regarded as the doubled middle;
M4. a collision/recurrence pullback changes endpoint labels without changing support.
```

A91 handles each mechanism as a routing source.

---

## 5. Adjacent local swap endpoint change

Suppose the first endpoint change is caused by swapping adjacent blocks or atoms inside `B`:

```text
L M -> M L.
```

Before the swap, the local internal endpoints include:

```text
u,
u+sum(L),
u+sum(L)+sum(M).
```

After the swap, they include:

```text
u,
u+sum(M),
u+sum(M)+sum(L).
```

The only changed internal endpoint is the middle one unless

```text
sum(L)=sum(M).
```

---

## Lemma A91.2: internal adjacent swap changing endpoint set gives pair/equal obstruction or moved-prefix recurrence

If an internal adjacent swap `L M -> M L` changes the endpoint set, then either:

```text
1. sum(L)=sum(M), giving an internal equal-interval / midpoint branch;
2. the new endpoint collides with an old internal endpoint, giving internal zero/equal interval;
3. the new endpoint is forbidden, giving singleton/prefix recurrence;
4. the new endpoint is neither collision nor forbidden, in which case the transformation strictly progresses and cannot be the first step of an invisible self-return.
```

### Proof

The new endpoint is `u+sum(M)`.  If it equals `u+sum(L)`, then `sum(L)=sum(M)`.  If it equals another old endpoint, subtracting endpoints gives a zero interval or equal interval inside `B`.  If it equals `f` in the global ordering, this is forbidden recurrence.  If none occurs, then the transformed state remains Graham-valid and avoids the forbidden value at the changed endpoint; the change is visible but not obstructive, so the return path cannot claim the endpoint change is hidden. ∎

### Status

The final alternative requires a progress/minimality statement in the final proof: an unobstructed first endpoint change should be treated as success/progress, not as a self-return obstruction.

---

# 6. Cyclic cut endpoint change

Suppose the first endpoint change is caused by a cyclic cut of the internal middle block `B` at `T_k`.

Then the endpoint set is translated by `-T_k` under the convention of A89:

```text
E_{new}=E_old-T_k.
```

---

## Lemma A91.3: internal cyclic endpoint change either preserves pattern strongly or creates routed cyclic recurrence

For an internal cyclic cut at `T_k`, either:

```text
1. E_old-T_k=E_old, giving strong exact cyclic self-return and hence contradiction by A89;
2. T_k=0, giving internal zero collapse;
3. E_old-T_k != E_old, so some new endpoint is outside the old pattern.
```

In case 3, the first such new endpoint either collides externally/internally, hits `f`, or is unobstructed progress.

### Proof

The cyclic endpoint formula is A89.  If the translated set equals the old set, A89 applies.  If `T_k=0`, the cut prefix is zero.  Otherwise the symmetric difference is nonempty; take the first new endpoint in cyclic order and apply the collision/forbidden/progress trichotomy. ∎

---

# 7. Normalization changes the doubled middle

A normalization may return to a weighted form by changing which interval is doubled.

If the doubled middle changes while the support `B` is said to be the same, then some boundary material has been transferred between outer and middle pieces, or the internal decomposition of `B` has changed.

---

## Lemma A91.4: normalization endpoint change gives A56 or smaller middle

If the first endpoint-pattern change is caused by changing the doubled-middle normalization, then one of the following occurs:

```text
1. the doubled middle is a proper subblock of B, giving smaller weighted middle;
2. boundary material is transferred between A/B or B/C, giving A56 transported-prefix/easy reduction;
3. the normalization subtracts two weighted equations and yields a non-weighted zero/equal interval.
```

### Proof sketch

Compare the weighted equations before and after normalization:

```text
a+2b+c=0,
a'+2b'+c'=0.
```

If `b'` is a proper subblock of `b`, the weighted measure decreases.  If `b'=b+d` with boundary material `d`, the difference equation has a coefficient-2 boundary term and is exactly A56-type transported-prefix/easy reduction.  If `b'=b` but `a'` or `c'` changes, the doubled terms cancel and produce `(a'-a)+(c'-c)=0`, a non-weighted branch. ∎

---

# 8. Endpoint-label change without endpoint-set change

A90 separated endpoint-set changes from label changes.  Still, the first changed endpoint may be a label change that later causes an endpoint-set change.

If the endpoint value is the same but represented by a different interval, subtracting the two interval representations gives a zero/equal relation.

---

## Lemma A91.5: endpoint label change gives internal zero/equal or pair-difference branch

If an internal endpoint value is preserved but its representing interval changes, then the difference between the old and new interval representations is one of:

```text
internal zero interval;
internal equal interval;
pair-difference boundary;
transported-prefix relation.
```

### Proof

Let the same endpoint value be represented as

```text
u+sum(I)=u+sum(J).
```

Then

```text
sum(I)-sum(J)=0.
```

If `I` and `J` overlap, uncrossing gives a zero interval or smaller equal interval.  If they are separated, it is separated-equal.  If they differ by boundary atoms, it is pair-difference or transported-prefix. ∎

---

# 9. First-changed-endpoint theorem

## Theorem A91.6: first changed internal endpoint produces a routed obstruction or progress

Assume a weak cut-rigid return has:

```text
same outer blocks A,C;
same middle support B;
changed internal endpoint set E_N != E_0;
a finite return-path model Omega_0,...,Omega_N.
```

Let `s_*` be the first endpoint-pattern change.  Then the transition at `s_*` produces one of:

```text
1. internal zero collapse;
2. internal equal/separated interval;
3. pair-difference boundary;
4. singleton/prefix recurrence;
5. cyclic recurrence handled by A71/A89;
6. A56 transported-prefix/easy reduction;
7. smaller weighted middle;
8. unobstructed progress, contradicting invisible self-return minimality.
```

Thus changed internal endpoint pattern cannot be invisible.

### Proof

By Lemma A91.1 the first change exists.  The transition causing it is one of the mechanisms M1--M4.  Adjacent swaps are Lemma A91.2.  Internal cyclic cuts are Lemma A91.3.  Normalization changes are Lemma A91.4.  Endpoint-label changes are Lemma A91.5.  These cases exhaust possible first endpoint-pattern changes in the return-path model. ∎

---

## Corollary A91.7: weak cut-rigid return is pattern-rigid modulo routed obstructions

Assume the finite return-path model and the progress/minimality principle for unobstructed first changes.

Then every weak cut-rigid return either:

```text
1. is pattern-rigid;
2. enters the non-weighted acyclic graph A78;
3. enters A56 easy reduction;
4. returns to a smaller weighted middle;
5. collapses;
6. succeeds/progresses, contradicting self-return.
```

### Proof

If the endpoint set is unchanged and boundary/label data are unchanged, the return is pattern-rigid.  If not, Theorem A91.6 or A90.8--A90.12 applies. ∎

---

# 10. Weighted closure, conditional on return-path formalization

## Theorem A91.8: weighted core closes under finite return-path formalization

Assume:

```text
1. every weak cut-rigid return admits the finite return-path model of Section 2;
2. unobstructed first endpoint changes give progress/success and cannot be part of a minimal self-return;
3. A78 non-weighted acyclicity and A89 strong exact impossibility hold.
```

Then every genuine weighted core is controlled: it either routes to A78, collapses, succeeds, or descends to a smaller weighted middle.

### Proof

By A79, the weighted core either is atom-middle, has a useful cut, or is weakly cut-rigid.  Atom-middle is handled by A80--A81.  A useful cut routes to A78, collapse, success, or smaller weighted middle.  If weakly cut-rigid, Corollary A91.7 gives either pattern-rigid or routed obstruction.  Pattern-rigid is impossible by A90.7 and A89.  Routed obstructions are handled by A78/A56 or weighted descent. ∎

---

# 11. Remaining formalization tasks

A91 hardens the conceptual first-changed-endpoint argument, but two proof-engineering tasks remain.

## Task T1: define the return-path model rigorously

Need a formal statement that every routed weighted self-return can be decomposed into the finite state sequence:

```text
Omega_0,...,Omega_N
```

with allowed transitions M1--M4.

## Task T2: prove the progress/minimality principle

Need a formal lemma:

```text
An unobstructed first internal endpoint change in a minimal counterexample cannot be part of a self-return; it gives either success or a strictly smaller obstruction state.
```

These are now the remaining weighted-proof engineering points.

---

# 12. Revised proof status after A91

A91 provides a usable route from weak cut-rigidity to pattern-rigidity, but still conditional on formalizing the return path.

The remaining bottleneck is no longer algebraic.  It is proof-architecture formalization:

```text
routed weighted self-return must be represented as finite local transitions,
and unobstructed first changes must be declared progress/descent.
```

---

# 13. Target A92

A92 should formalize the return-path model.

Suggested title:

```text
Finite return-path formalization for routed obstructions A92
```

Goal:

```text
Define an obstruction state machine whose transitions are exactly the local moves used in A1--A91.
```

Minimum deliverables:

```text
1. state tuple definition;
2. allowed transition list;
3. proof that every A-note routing step is one transition or finite sequence;
4. progress/descent criterion for unobstructed endpoint changes;
5. connection to A91.
```
