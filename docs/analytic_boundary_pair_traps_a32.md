# Analytic boundary pair traps A32: non-descending atom-insertion branches

This note continues from A31.

A31 showed that most atom-insertion obstruction branches descend or collapse.  The remaining non-descending branches were isolated as:

```text
Q2 with |B|=1,
Q3 with 1+j-i >= |B|,
H1/H2 forbidden-hit recurrence branches.
```

This note analyzes those boundary cases.  It does not close them completely, but it records the exact algebra and separates true pair traps from recurrence branches.

---

## Standing setup

Work in an auxiliary ordering segment

```text
X A B q Y
```

where

```text
sum(A)+sum(B)=0,
q != 0.
```

Write

```text
a=sum(A),
sum(B)=-a.
```

The atom insertion move is

```text
X A B q Y -> X A q B Y.
```

A29/A30 gave obstruction equations:

```text
Q1: q=A_i-a,
Q2: q=Y_m-a,
Q3: B_j=A_i-a-q,
Q4: B_j=Y_m-a,
Q5: B_j=0,
H1: T_y+q=f,
H2: T_y+q+B_j=f.
```

A31 proved descent/collapse for Q1, Q4 endpoint cases, Q5, and most Q2 cases.  Q3 was only partially descending.

---

# 1. Q2 boundary: |B|=1

Assume

```text
|B|=1.
```

Let

```text
B=(b_0).
```

Since

```text
sum(A)+sum(B)=0,
```

we have

```text
b_0=-a.
```

The zero block is therefore

```text
A b_0,
```

where the final atom cancels the whole preceding block.

The Q2 obstruction is

```text
q=Y_m-a,
```

or

```text
a+q=Y_m.
```

## Lemma A32.1: Q2 boundary is a two-atom/block equal-sum trap

When `|B|=1`, the Q2 obstruction

```text
a+q=Y_m
```

is equivalent to

```text
q-b_0=Y_m.
```

### Proof

Since `b_0=-a`, we have `a=-b_0`.  Substitute into `a+q=Y_m` to get

```text
q-b_0=Y_m.
```

∎

### Interpretation

This branch is not a clean support descent because replacing the zero block `A b_0` by the composite `A q` preserves support length when `B` is one atom.

However, the obstruction now involves the pair `(q,b_0)` through the difference

```text
q-b_0.
```

This is a genuine pair-difference trap.  It should be attacked by swapping `q` and `b_0` or by inserting `q` before the final cancelling atom `b_0` and then applying the adjacent-pair obstruction analysis from A5.

---

## Lemma A32.2: if q=b_0 in the Q2 boundary, contradiction

In the Q2 boundary branch, if

```text
q=b_0,
```

then

```text
Y_m=0.
```

Thus the obstruction collapses to a zero-prefix/interior-zero branch.

### Proof

From Lemma A32.1, `Y_m=q-b_0`.  If `q=b_0`, then `Y_m=0`.  ∎

### Status

The only genuine Q2 boundary subcase has

```text
q != b_0
```

and is controlled by a pair difference `q-b_0`.

---

# 2. Q3 non-descent range

Recall Q3:

```text
B_j=A_i-a-q.
```

A30 rewrote this as

```text
q+B_j+tail_i(A)=0.
```

The support count of this three-piece zero composite is

```text
1+j+(|A|-i).
```

It is a strict support descent when

```text
1+j-i < |B|.
```

The non-descent range is therefore

```text
1+j-i >= |B|.
```

Equivalently,

```text
j >= |B|+i-1.
```

Because `1 <= j <= |B|` and `1 <= i <= |A|`, this imposes strong restrictions.

## Lemma A32.3: Q3 non-descent forces i=1 or j near the endpoint of B

If Q3 lies in the non-descent range

```text
1+j-i >= |B|,
```

then

```text
j >= |B|-1+i.
```

In particular:

- if `i=1`, then `j>=|B|` so `j=|B|`;
- if `i=2`, then `j>=|B|+1`, impossible unless the inequality is impossible;
- more generally, for every `i>=2`, the non-descent range is impossible.

Therefore the only possible Q3 non-descent case is

```text
i=1,
j=|B|.
```

### Proof

The inequality is

```text
1+j-i >= |B|.
```

Rearrange:

```text
j >= |B|+i-1.
```

Since always `j<=|B|`, this requires

```text
|B| >= |B|+i-1,
```

so

```text
i<=1.
```

Since `i>=1`, we get `i=1`.  Then the inequality gives `j>=|B|`; since `j<=|B|`, one has `j=|B|`.  ∎

## Lemma A32.4: Q3 non-descent collapses to an atom-pair zero relation

In the only possible Q3 non-descent case

```text
i=1,
j=|B|,
```

the Q3 zero composite

```text
q+B_j+tail_i(A)=0
```

becomes

```text
q+sum(B)+tail_1(A)=0.
```

Since

```text
sum(B)=-sum(A)=-(A_1+tail_1(A)),
```

this reduces to

```text
q-A_1=0.
```

Hence

```text
q=A_1,
```

where `A_1` is the first atom of `A`.

### Proof

Substitute `j=|B|`, so `B_j=sum(B)=-sum(A)`.  Write `sum(A)=A_1+tail_1(A)`.  The Q3 relation becomes

```text
q - (A_1+tail_1(A)) + tail_1(A)=0,
```

so `q-A_1=0`.  ∎

### Consequence

If the atom `q` is outside the zero block and entries are distinct, then `q=A_1` is impossible.

If `q` is not outside the original set but is a transported copy of an atom under a block move, then this is an atom-identification/pair-trap boundary that must be checked against the exact move semantics.

For the standard atom-insertion move where `q` is an atom disjoint from block `A`, Q3 non-descent is impossible.

---

# 3. H1 forbidden recurrence

H1 is

```text
T_y+q=f.
```

This means inserting `q` immediately after `A` lands on the forbidden value.

## Lemma A32.5: H1 produces an earlier forbidden hit if the insertion point is before the old first hit

Suppose the transformed ordering after insertion is Graham-valid.  If the position immediately after `Aq` is earlier than the original minimal forbidden-hit index `h`, then H1 contradicts the minimal choice of `R`.

### Proof

H1 states that the transformed ordering has a forbidden partial sum at the endpoint after `Aq`.  If that endpoint index is earlier than `h`, then the transformed Graham-valid ordering has an earlier forbidden hit, contradicting minimality.  ∎

### Status

H1 recurrence is controlled when the insertion creates an earlier hit.  The residual H1 branch occurs only when the new forbidden landing is at position at least `h`, or when the transformed ordering is not Graham-valid because of a separate collision equation already in Q1--Q5.

---

# 4. H2 forbidden recurrence

H2 is

```text
T_y+q+B_j=f.
```

This means the transformed ordering hits `f` after inserting `q` and then traversing a prefix of `B`.

## Lemma A32.6: H2 produces an earlier forbidden hit under the same index condition

Suppose the transformed ordering after insertion is Graham-valid.  If the endpoint after `AqB_j` lies before the original minimal forbidden-hit index `h`, then H2 contradicts minimality.

### Proof

Same as Lemma A32.5.  H2 identifies a forbidden partial sum in the transformed Graham-valid ordering.  If its index is earlier than `h`, minimality is contradicted.  ∎

---

# 5. Summary of boundary analysis

| Branch | Boundary condition | Outcome |
|---|---|---|
| Q2 | `|B|=1` | pair-difference trap `q-b_0=Y_m` |
| Q2 | `|B|=1`, `q=b_0` | zero-prefix/interior-zero collapse |
| Q3 | non-descent range | only possible when `i=1`, `j=|B|` |
| Q3 | `i=1`, `j=|B|` | forces `q=A_1`; impossible if atoms disjoint |
| H1 | new hit earlier than `h` | minimality contradiction |
| H2 | new hit earlier than `h` | minimality contradiction |

---

# 6. Consequence for A31

The Q3 non-descent branch is essentially eliminated in the standard disjoint-atom insertion setting.

The main unresolved atom-insertion boundary is therefore Q2 with `|B|=1`, which is a genuine pair-difference trap, plus H1/H2 recurrence when the new forbidden hit is not earlier than the original one.

---

## Target A33

The next step is to formalize the Q2 pair-difference trap.

Given a zero block

```text
A b_0
```

with

```text
sum(A)+b_0=0,
```

and an outside atom `q` satisfying

```text
q-b_0=Y_m,
```

prove that swapping or inserting the pair `(q,b_0)` either:

```text
1. creates a strict support descent;
2. gives an earlier forbidden hit;
3. collapses to zero-prefix/interior-zero;
4. reduces to the A5 adjacent pair obstruction.
```

---

## Current status

Proved here:

1. Q2 boundary becomes pair-difference trap;
2. Q2 boundary collapses if `q=b_0`;
3. Q3 non-descent only occurs at `i=1`, `j=|B|`;
4. Q3 non-descent forces `q=A_1`, impossible in standard disjoint-atom insertion;
5. H1/H2 recurrence branches are eliminated when they produce earlier forbidden hits.

Not proved here:

1. Q2 pair-difference trap elimination;
2. H1/H2 recurrence when the new hit is not earlier;
3. endpoint avoidance theorem.
