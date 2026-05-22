# Analytic weighted signed residual normal forms A56

This note continues from A55.

After A55, the main remaining local obstruction class is the weighted signed overlap/nesting family first isolated in A20.  Typical relations have the form

```text
sum(A)+2sum(B)+sum(C)=0.
```

Earlier notes showed that several apparent coefficient-2 branches were not genuinely new:

```text
A38: D5 proper-interior -> prefix(A)+G+tail(C)=0;
A49: E3 -> C+tail(A)+prefix(G)=0;
A55: midpoint displayed equations -> two-/three-piece zero.
```

This note gives normal-form tests for deciding when a coefficient-2 expression is a transported-prefix artifact and when it is a genuine weighted residual.

No complete proof is claimed here.

---

## Standing convention

Let a block `B` be cut as

```text
B = P R
```

with

```text
p=sum(P),
r=sum(R),
b=sum(B)=p+r.
```

A coefficient `2p` often appears when the same transported prefix `P` occurs once as part of the original block sum and once again as a moved/compared prefix.

The guiding identity is:

```text
2p + r = p + b.
```

Thus any expression containing `2p+r` may sometimes be rewritten as `p+B`, removing the apparent coefficient `2`.

---

# 1. Transported-prefix coefficient-2 test

## Lemma A56.1: coefficient-2 on a prefix is removable when the complementary tail appears with coefficient 1

Let

```text
B=P R.
```

Then

```text
2sum(P)+sum(R)=sum(P)+sum(B).
```

Therefore a relation of the form

```text
2sum(P)+sum(R)+sum(U)=0
```

is equivalent to

```text
sum(P)+sum(B)+sum(U)=0.
```

### Proof

Since `sum(B)=sum(P)+sum(R)`,

```text
2sum(P)+sum(R)=sum(P)+[sum(P)+sum(R)]=sum(P)+sum(B).
```

∎

### Interpretation

If the coefficient-2 block is a prefix of a larger block and the complementary tail is also present with coefficient 1, the branch is not genuinely weighted.  It is a transported-prefix artifact.

---

## Lemma A56.2: coefficient-2 on a tail is removable when the complementary prefix appears with coefficient 1

Let

```text
B=P R.
```

Then

```text
sum(P)+2sum(R)=sum(B)+sum(R).
```

Thus

```text
sum(P)+2sum(R)+sum(U)=0
```

is equivalent to

```text
sum(B)+sum(R)+sum(U)=0.
```

### Proof

Same calculation with `R` as the doubled piece. ∎

---

# 2. Proper-overlap signed relation

The A20 signed-overlap residual arises from two signed interval relations whose supports overlap.  A schematic normal form is:

```text
A B  and  B C
```

with a signed equality that produces

```text
sum(A)+2sum(B)+sum(C)=0.
```

Here `B` is the overlap block.  Unlike Lemmas A56.1--A56.2, the complementary pieces `A` and `C` are not generally the two complementary pieces of a single larger block containing `B`.

---

## Lemma A56.3: pure signed-overlap is genuinely weighted unless A or C completes B to a larger known block

Consider

```text
sum(A)+2sum(B)+sum(C)=0.
```

If neither `A B` nor `B C` is a known larger block with known total that can replace `sum(A)+sum(B)` or `sum(B)+sum(C)`, then the coefficient `2sum(B)` cannot be removed by prefix/tail substitution alone.

### Proof

The identities in Lemmas A56.1--A56.2 require a decomposition of a known block into doubled piece plus complementary piece.  Without such a known containing block, `2sum(B)` has no algebraic replacement using only prefix/tail sums. ∎

### Status

This identifies the genuinely hard case:

```text
A, B, C are three independent consecutive pieces and B is doubled only because it is overlapped by two signed intervals.
```

---

# 3. Endpoint collapses for weighted signed relations

Even genuine weighted relations have endpoint collapses.

## Lemma A56.4: weighted relation collapses if the doubled block is zero

If

```text
sum(A)+2sum(B)+sum(C)=0
```

and

```text
sum(B)=0,
```

then

```text
sum(A)+sum(C)=0.
```

If `B` is an interior block in a Graham-valid ordering, `sum(B)=0` is impossible.  If `B` begins at the basepoint, it is a prefix-zero branch.

### Proof

Substitute `sum(B)=0`. ∎

---

## Lemma A56.5: weighted relation becomes two-piece zero if one outer piece cancels the doubled block halfway

If

```text
sum(A)+2sum(B)+sum(C)=0
```

and

```text
sum(A)+sum(B)=0,
```

then

```text
sum(B)+sum(C)=0.
```

Similarly, if

```text
sum(B)+sum(C)=0,
```

then

```text
sum(A)+sum(B)=0.
```

### Proof

Substitute `sum(A)=-sum(B)` in the first case:

```text
-sum(B)+2sum(B)+sum(C)=0,
```

so `sum(B)+sum(C)=0`.  The other case is symmetric. ∎

### Interpretation

If either adjacent pair already forms a zero composite, the weighted branch reduces to ordinary zero-composite surgery.

---

## Lemma A56.6: equal outer pieces produce midpoint-type reduction

If

```text
sum(A)+2sum(B)+sum(C)=0
```

and

```text
sum(A)=sum(C),
```

then over odd prime fields

```text
sum(A)+sum(B)=0.
```

### Proof

Substitute `sum(C)=sum(A)`:

```text
2sum(A)+2sum(B)=0.
```

Divide by `2`. ∎

### Status

This was already observed in A26.8.  It routes equal-outer weighted cases to two-piece zero.

---

# 4. Normal-form classification

Given a relation

```text
sum(A)+2sum(B)+sum(C)=0,
```

run the following tests.

## Test W1: transported-prefix/tail artifact

Check whether one of `A` or `C` is the complementary prefix/tail of a known block containing `B`.

If yes, rewrite using A56.1 or A56.2 into a composite-zero relation.

Status:

```text
controlled by A28--A33 plus A34 recurrence.
```

## Test W2: zero doubled block

If

```text
sum(B)=0,
```

then collapse by A56.4.

Status:

```text
zero collapse / prefix-zero / two-piece zero.
```

## Test W3: adjacent-pair zero

If

```text
sum(A)+sum(B)=0
```

or

```text
sum(B)+sum(C)=0,
```

then reduce by A56.5.

Status:

```text
two-piece zero.
```

## Test W4: equal outer pieces

If

```text
sum(A)=sum(C),
```

then reduce by A56.6.

Status:

```text
two-piece zero / midpoint boundary.
```

## Test W5: genuine weighted core

If none of W1--W4 applies, the branch remains genuinely weighted:

```text
A+B+B+C=0
```

with no known containing-block rewrite and no zero/equal endpoint collapse.

Status:

```text
HARD WEIGHTED RESIDUAL.
```

---

# 5. Relation to already controlled branches

## A38 D5 proper-interior

A38 had a relation of the form

```text
C_k = a+g+A_i.
```

At first this looked like a doubled transported prefix.  Writing

```text
A=P R,
C=K L
```

showed it was equivalent to

```text
P+G+L=0.
```

This is W1: a transported-prefix artifact.

## A49 E3

A49 had

```text
G_j=A_i-2a.
```

Using

```text
a=sum(C)=sum(A),
a-A_i=tail(A),
```

it became

```text
C+tail(A)+prefix(G)=0.
```

Again W1: the apparent coefficient `2a` was removed by using a known equal block `C` plus the tail of `A`.

## A55 midpoint equations

A55's coefficient-like branch

```text
C_k=2a+Y_m
```

became

```text
A+tail(C)+prefix(Y)=0.
```

Again not genuinely weighted.

---

# 6. Genuine weighted branch status

The only weighted signed branches that remain hard are those passing all normal-form tests W1--W4.

A genuine weighted core has:

```text
sum(A)+2sum(B)+sum(C)=0,
```

with:

```text
B != 0,
A+B != 0,
B+C != 0,
A != C,
no known containing-block rewrite for the doubled B.
```

These are the branches that require a new argument.

Possible approaches:

```text
1. split B into prefix/tail and search for a cut that creates W1;
2. insert an outside atom into B to break the doubled contribution;
3. use the odd-prime midpoint identity: 2B = (B+q)+(B-q) for a suitable atom/block q;
4. apply a finite search to see whether genuine weighted cores survive simultaneous Graham-validity constraints.
```

---

# 7. Target A57

A57 should implement a weighted normal-form classifier.

Suggested script:

```text
scripts/classify_weighted_signed_normal_form.py
```

Input:

```text
lengths of A,B,C,
optional information about containing blocks,
flags for known equalities such as A+C, A+B, B+C, B=0.
```

Output:

```text
transported_prefix_artifact,
zero_collapse,
two_piece_zero,
equal_outer_reduction,
genuine_weighted_core.
```

This will make the remaining weighted branch auditable and prevent reclassifying already-controlled transported-prefix cases as hard residuals.

---

## Current status

Proved here:

1. transported-prefix/tail coefficient-2 removal tests;
2. zero doubled-block collapse;
3. adjacent-pair zero reduction;
4. equal outer-piece reduction;
5. classification of genuine weighted core conditions.

Not proved here:

1. elimination of genuine weighted cores;
2. A34 global recurrence theorem;
3. endpoint avoidance theorem.
