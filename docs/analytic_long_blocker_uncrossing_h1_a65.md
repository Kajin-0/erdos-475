# Analytic long-blocker uncrossing A65: atom-insertion H1

This note continues from A64.

A64 reduced the A34 recurrence theorem to two parts:

```text
1. bounded-blocker recurrence descent;
2. long-blocker uncrossing.
```

A64 proved the bounded-blocker part.  The remaining case is a long-blocker recurrence: a local move creates a recurrent forbidden hit, and every A5 blocker for the recurrent ordering lies at least as far away as the support scale of the source obstruction.

This note analyzes the simplest recurrence source:

```text
atom insertion H1.
```

The goal is to pull the far A5 blocker back through the insertion and identify the crossing geometry forced by long-blocker recurrence.

This note is partial.  It gives the exact pullback formulas and proves the non-crossing cases descend.  The true crossing case remains as the next target.

---

## 1. Standing atom-insertion setup

Start with a zero block decomposed as

```text
P Q
```

with

```text
sum(P)+sum(Q)=0.
```

Let

```text
p=sum(P),
q=sum(q_atom),
```

where `q_atom` is an outside atom inserted between `P` and `Q`.

The atom-insertion move is

```text
X P Q q_atom Y -> X P q_atom Q Y.
```

Let

```text
x=sum(X).
```

After insertion, the changed endpoint after `P q_atom` is

```text
x+p+q.
```

The H1 forbidden recurrence is:

```text
x+p+q=f.
```

Assume the transformed ordering is Graham-valid and this forbidden hit is not earlier than the original minimal forbidden hit.

Let the source obstruction span be

```text
s=|P|+|Q|.
```

---

## 2. Transformed ordering notation

The transformed local segment is

```text
P q_atom Q.
```

Let the H1 forbidden hit be at endpoint

```text
H = end(P q_atom).
```

The atom immediately after the forbidden hit in the transformed ordering is the first atom of `Q`, denoted

```text
q_1.
```

assuming `Q` is nonempty.  If `Q` is empty, the original zero block was only `P`, which is a zero-block collapse and is not the atom-insertion case.

By A64, A5 applied to the transformed ordering gives a blocker index `j'` satisfying

```text
S'_{H-1}+q_1=S'_{j'}.
```

Choose a nearest blocker.  In the long-blocker case,

```text
|j'-H|+1 >= s.
```

---

# 3. Left blocker pullback

First suppose the transformed A5 blocker lies to the left of the H1 hit:

```text
j'<H.
```

Then A64.2 gives

```text
sum'(j',H-1]+q_1=0.
```

Because `H-1` is the endpoint after `P`, the interval `(j',H-1]` is a suffix of the transformed prefix ending at `P`.

There are two subcases:

```text
L0: j' lies inside X or before P;
L1: j' lies inside P.
```

---

## Lemma A65.1: left blocker inside P gives strict suffix-zero descent

If `j'` lies inside `P`, then the left-blocker relation pulls back to

```text
sum(tail(P from j')) + q_1 = 0.
```

This is a two-piece zero composite supported on a proper suffix of `P` plus the first atom of `Q`.

Its support span is strictly smaller than

```text
|P|+|Q|.
```

### Proof

When `j'` lies inside `P`, the transformed interval `(j',H-1]` is exactly a proper suffix of `P`, since `H-1` is the endpoint after `P`.  The A5 relation is that suffix plus `q_1` sums to zero.  The support length is at most `|P|-1+1=|P|`, which is strictly less than `|P|+|Q|` because `Q` is nonempty. ∎

### Status

This branch descends by A64 bounded-blocker logic after pullback, even if the transformed blocker was long relative to the transformed endpoint metric.

---

## Lemma A65.2: left blocker before P produces an external bridge zero composite

If `j'` lies before the start of `P`, then the left-blocker relation pulls back to

```text
sum(j', start(P)] + sum(P) + q_1 = 0.
```

Equivalently, it is an external bridge interval plus the block `P` plus the first atom of `Q`.

### Proof

The transformed interval `(j',H-1]` runs from the external endpoint through the start of `P` and ends after `P`.  Therefore it is the bridge from `j'` to the start of `P`, followed by all of `P`.  Add the A5 atom `q_1`. ∎

### Status

This is a zero-composite crossing the left boundary of the source zero block.  It is not automatically smaller.  It is the first genuine long-blocker geometry.

---

# 4. Right blocker pullback

Now suppose the transformed A5 blocker lies to the right of the H1 hit:

```text
j'>H.
```

Then the A5 blocker relation is a signed interval/atom relation.  Since the atom after the forbidden hit is `q_1`, the relation may be written as

```text
sum'(H,j'] = q_1
```

up to the convention of whether `(H,j']` includes `q_1`.  More explicitly, from

```text
S'_{H-1}+q_1=S'_{j'},
```

and `S'_H=S'_{H-1}+q`, note that `H` is after the inserted atom `q_atom`, while `q_1` is after `H`.  Thus the interval from `H` to `j'` begins in `Q`.

The useful expression is:

```text
S'_{j'}-S'_{H-1}=q_1.
```

But

```text
S'_H-S'_{H-1}=q.
```

so

```text
S'_{j'}-S'_H = q_1-q.
```

Thus the right blocker creates a pair-difference relation between the inserted atom and the first atom of `Q` over a prefix of the post-H interval.

---

## Lemma A65.3: right blocker inside Q gives a pair-difference prefix relation

If `j'` lies inside `Q`, let `Q_r` be the prefix of `Q` ending at `j'`.  Then the right-blocker relation gives

```text
Q_r = q_1 - q.
```

Equivalently,

```text
q - q_1 + Q_r = 0.
```

### Proof

The interval from after the inserted atom to `j'` is a prefix `Q_r` of `Q`.  As above,

```text
S'_{j'}-S'_H=q_1-q.
```

Hence `Q_r=q_1-q`. ∎

### Endpoint cases

If `r=1`, then `Q_r=q_1`, so the equation gives

```text
q_1=q_1-q,
```

hence

```text
q=0,
```

impossible because atoms lie in `F_p^*`.

If `r<|Q|`, this is a proper-prefix pair-difference branch with support smaller than the source zero block.

If `r=|Q|`, then using `sum(Q)=-p`, the relation becomes

```text
-p=q_1-q,
```

or

```text
p+q_1-q=0.
```

This is a boundary pair-difference branch involving the whole `Q`.

---

## Lemma A65.4: right blocker inside Q descends unless it uses all of Q

In the setup of Lemma A65.3, if `j'` lies inside a proper prefix of `Q`, then the blocker pulls back to a smaller pair-difference/zero-composite obstruction.

Only the endpoint case `j'=end(Q)` can tie the original support scale.

### Proof

For a proper prefix `Q_r`, the support is `r+2` at worst, involving `Q_r` and two atoms.  Since `r<|Q|`, this is smaller than the full source support `|P|+|Q|` except possibly in degenerate cases with very small `P`.  If `P` is empty or length one, the source zero block is already a boundary case handled by zero-block collapse or A31 boundary analysis. ∎

---

## Lemma A65.5: right blocker beyond Q creates a bridge crossing the right boundary

If `j'` lies after the end of `Q`, then the right-blocker relation pulls back to

```text
sum(Q)+sum(after-Q bridge to j') = q_1-q.
```

Using `sum(Q)=-p`, this is

```text
sum(after-Q bridge to j') - p + q - q_1 = 0.
```

### Proof

The interval from after the inserted atom to `j'` contains all of `Q` and then the external bridge after `Q`.  Use `sum(Q)=-p` and the right-blocker formula. ∎

### Status

This is a zero/signed composite crossing the right boundary of the source zero block.  It is the right-side analog of Lemma A65.2 and is not automatically smaller.

---

# 5. Non-crossing descent theorem for H1

Call a transformed A5 blocker non-crossing if its pullback lies entirely inside `P` or entirely inside a proper prefix of `Q`.

Call it crossing if it reaches outside the original source zero block on the left or right, or uses all of `Q` in the right-blocker endpoint case.

## Proposition A65.6: non-crossing H1 long blockers descend after pullback

For atom-insertion H1 recurrence, any non-crossing transformed A5 blocker pulls back to a strictly smaller two-piece zero, pair-difference, or prefix obstruction.

Therefore a genuine long-blocker tie must be crossing.

### Proof

Left-inside-`P` blockers descend by Lemma A65.1.  Right-inside-proper-`Q` blockers descend by Lemmas A65.3--A65.4.  These are exactly the non-crossing cases. ∎

---

# 6. Remaining crossing cases

After Proposition A65.6, the only H1 long-blocker cases are:

```text
C1. left blocker starts before P;
C2. right blocker ends after Q;
C3. right blocker uses all of Q.
```

Their pullback forms are:

```text
C1: left_bridge + P + q_1 = 0;
C2: right_bridge - P + q - q_1 = 0;
C3: P + q_1 - q = 0.
```

C3 is the cleanest.  It is a pair-difference relation between the inserted atom `q`, the first atom of `Q`, and the whole prefix block `P`.

---

## Lemma A65.7: endpoint crossing C3 is a pair-difference boundary branch

If the right blocker uses all of `Q`, then

```text
P + q_1 - q = 0.
```

Equivalently,

```text
q-q_1=sum(P).
```

This is a pair-difference boundary branch analogous to A33, with pair difference equal to the first-side block sum.

### Proof

This is the endpoint case of Lemma A65.3 using `sum(Q)=-sum(P)`. ∎

### Status

C3 should be attacked using the A33 pair-difference machinery.

---

# 7. What A65 proves and what remains

A65 proves that atom-insertion H1 long-blocker recurrence is not arbitrary.

It reduces to crossing pullbacks:

```text
left bridge crossing,
right bridge crossing,
endpoint pair-difference boundary.
```

The non-crossing cases descend.

This is a genuine refinement of A64.LB for the H1 source.

---

# 8. Target A66

A66 should attack the crossing cases C1--C3.

Recommended order:

```text
1. C3 endpoint pair-difference boundary, using A33-style pair swap.
2. C1/C2 bridge crossings, using proper-overlap uncrossing with the original zero block P Q.
```

Expected routes:

```text
smaller equal interval,
two-piece zero descent,
pair trap controlled by A33,
A34 recurrence with smaller span,
or contradiction to Graham-validity.
```

---

## Current status

Proved here:

1. exact pullback of left H1 blockers;
2. exact pullback of right H1 blockers;
3. non-crossing H1 blockers descend;
4. genuine long-blocker H1 recurrence must cross the source support;
5. endpoint crossing is a pair-difference boundary branch.

Not proved here:

1. crossing bridge uncrossing;
2. endpoint pair-difference closure in this context;
3. full A34 recurrence theorem;
4. endpoint avoidance theorem.
