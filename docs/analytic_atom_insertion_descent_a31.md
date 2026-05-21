# Analytic atom-insertion descent A31: partial descent audit

This note continues from A30.

A30 routed atom-insertion obstruction equations into interval/composite classes.  The next question is whether that routing is a strict descent.  This note gives a partial answer.

It proves descent for some obstruction branches and marks the non-descending branches explicitly.

The goal is to avoid falsely claiming that the two-piece-zero branch is closed.  At present, atom insertion is a useful reduction tool, but not yet a complete descent mechanism.

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

Let

```text
a=sum(A),
sum(B)=-a.
```

The atom-insertion move is

```text
X A B q Y  ->  X A q B Y.
```

A29 gave the obstruction equations:

```text
(Q1) q=A_i-a,
(Q2) q=Y_m-a,
(Q3) B_j=A_i-a-q,
(Q4) B_j=Y_m-a,
(Q5) B_j=0.
```

A30 translated these into interval/composite objects.

---

# 1. Candidate measure

For a separated zero composite with pieces `A` and `B`, define

```text
M_0(A,B) = |A|+|B|.
```

For a multi-piece zero composite, define

```text
M(Z_1,...,Z_r) = (r, |Z_1|+...+|Z_r|)
```

ordered lexicographically first by number of pieces, then total support length.

The original exposed zero block `AB` has composite measure

```text
M(A,B) = (2, |A|+|B|).
```

A branch is a strict composite descent if it produces either:

```text
1. a zero composite with fewer pieces; or
2. a zero composite with the same number of pieces but strictly smaller total support.
```

---

# 2. Q1 descent

## Lemma A31.1: Q1 produces a strictly smaller two-piece zero composite unless the A-tail is all of A

Recall Q1:

```text
q=A_i-a.
```

A30 showed this is equivalent to

```text
q + tail_i(A)=0,
```

where

```text
tail_i(A) = (after the i-th element of A through the end of A).
```

If `i>=1`, then

```text
|tail_i(A)| < |A|.
```

Therefore the new two-piece zero composite

```text
(q, tail_i(A))
```

has total support

```text
1+|tail_i(A)| <= |A| < |A|+|B|,
```

provided `B` is nonempty.

### Proof

The equality `q+tail_i(A)=0` is A30.1.  Since `i>=1`, the tail after the `i`-th prefix omits at least one atom of `A`, so it is strictly shorter than `A`.  Adding the single atom `q` gives support at most `|A|`; the original support was `|A|+|B|`, with `|B|>=1`.  ∎

### Status

Q1 is a strict descent branch.

---

# 3. Q5 collapse

## Lemma A31.2: Q5 is immediate zero-interval collapse or prefix-zero branch

Recall Q5:

```text
B_j=0.
```

This is the zero-sum interval consisting of the first `j` entries of `B`.

If the interval is interior in the current auxiliary ordering, it contradicts Graham-validity of that auxiliary ordering.  If it begins at the basepoint, it is a prefix-zero branch.

### Proof

Immediate from the standard no-interior-zero-interval lemma.  ∎

### Status

Q5 is not a hard residual branch.  It is a collapse/prefix-zero branch.

---

# 4. Q4 equal-interval branch

## Lemma A31.3: Q4 routes to an equal-interval relation with support no larger than the original zero composite plus gap

Recall Q4:

```text
B_j=Y_m-a.
```

A30 showed this is equivalent to

```text
sum(A)+B_j=Y_m.
```

So the interval consisting of all of `A` plus the first `j` entries of `B` has the same sum as the first `m` entries of `Y`.

The left interval has length

```text
|A|+j <= |A|+|B|.
```

If `j<|B|`, this interval is strictly shorter than the original zero block `AB`.

If `j=|B|`, then `sum(A)+B_j=sum(A)+sum(B)=0`, so Q4 gives

```text
Y_m=0,
```

which is an interior-zero or prefix-zero branch.

### Proof

The equal-interval translation is A30.4.  The length comparison is immediate.  If `j=|B|`, then `A+B_j` is the whole zero block, hence has sum zero.  Therefore `Y_m=0`.  ∎

### Status

Q4 is controlled: it either gives a shorter/equal interval relation routed to A20/A26 or collapses to a zero-prefix branch at the endpoint case.

It is not yet a complete descent unless the equal-interval branch itself is fully normalized by A27 and subsequent terminal cases are eliminated.

---

# 5. Q2 equal-composite branch

Recall Q2:

```text
q=Y_m-a.
```

A30 showed this is equivalent to

```text
sum(A)+q=Y_m.
```

This relates the composite interval `Aq` to a prefix of `Y`.

## Lemma A31.4: Q2 is not automatically a span descent

The support length of `Aq` is

```text
|A|+1.
```

This may be smaller than, equal to, or larger than `|A|+|B|` depending on `|B|`.

If `|B|>=2`, then

```text
|A|+1 < |A|+|B|,
```

so Q2 gives a shorter left-side support than the original zero block.

If `|B|=1`, then the support lengths are equal:

```text
|A|+1 = |A|+|B|.
```

Thus Q2 is a strict span descent except in the boundary case where `B` is a single atom.

### Proof

Immediate from support counts.  ∎

### Status

Q2 is mostly descending, but has a genuine boundary case:

```text
|B|=1.
```

That boundary should be treated as a pair-trap/atom-trap case.

---

# 6. Q3 three-piece zero branch

Recall Q3:

```text
B_j=A_i-a-q.
```

A30 showed this is equivalent to

```text
q+B_j+tail_i(A)=0.
```

This is a three-piece zero composite.

## Lemma A31.5: Q3 has smaller total support but more pieces

The Q3 composite pieces are:

```text
q,
B_prefix_j,
tail_i(A).
```

Their total support length is

```text
1+j+(|A|-i).
```

The original two-piece composite `A+B` has support length

```text
|A|+|B|.
```

Thus Q3 has smaller support whenever

```text
1+j-i < |B|.
```

However, Q3 has three pieces instead of two, so it is not a descent under the lexicographic measure `(number_of_pieces,total_support)`.

It is a descent under the alternative measure

```text
(total_support, number_of_pieces)
```

whenever the displayed inequality holds.

### Proof

The support count is direct.  The piece-count observation is immediate.  ∎

### Status

Q3 is the first serious nontrivial branch.  It may still be controlled by a measure prioritizing total support before piece count, but not by the naive lexicographic measure prioritizing piece count.

Boundary/non-descent subcases satisfy

```text
1+j-i >= |B|.
```

These should be isolated as atom/pair traps.

---

# 7. Forbidden-hit branches H1/H2

A30 also recorded forbidden-hit equations:

```text
(H1) T_y+q=f,
(H2) T_y+q+B_j=f.
```

These are not zero-composite relations by themselves.  They are landing equations.

## Lemma A31.6: H1/H2 reduce to the earlier first-hit obstruction form

H1 is a single-atom forbidden landing after the endpoint `y`:

```text
T_y+q=f.
```

H2 is an atom-plus-prefix forbidden landing:

```text
T_y+q+B_j=f.
```

In either case, if the resulting ordering is Graham-valid, then endpoint-avoidance failure implies that this forbidden hit must be unavoidable.  Applying the A5 adjacent-swap obstruction at this new hit produces a local blocker equation of the same form as before.

### Proof

This is a structural reduction: the forbidden-hit equations put the transformed ordering back into the endpoint-avoidance failure setup.  The A5 right-swap lemma applies to any Graham-valid ordering with a forbidden hit not at the final endpoint.  ∎

### Status

H1/H2 are recurrence branches, not immediate descent branches.  They must be controlled by the global first-hit minimality measure.

---

# 8. Summary table

| Case | Routed object | Descent status |
|---|---|---|
| Q1 | `q+tail(A)=0` | strict support descent |
| Q2 | `A+q=prefix(Y)` | descent unless `|B|=1` boundary |
| Q3 | `q+B_prefix+tail(A)=0` | support descent only under `1+j-i<|B|`; otherwise residual |
| Q4 | `A+B_prefix=prefix(Y)` | equal-interval branch, endpoint collapses if `j=|B|` |
| Q5 | `B_prefix=0` | collapse / prefix-zero |
| H1 | `T_y+q=f` | recurrence to A5, controlled only by first-hit minimality |
| H2 | `T_y+q+B_prefix=f` | recurrence to A5, controlled only by first-hit minimality |

---

# 9. Consequence

Atom insertion gives substantial descent but not a closed proof.

The hard remaining atom-insertion branches are:

```text
Q2 with |B|=1,
Q3 in non-descent support range,
H1/H2 recurrence branches.
```

The next proof layer should isolate these boundary cases and see whether they correspond exactly to the earlier pair-trap boundary branches.

---

## Target A32

Formalize the boundary branches:

```text
1. Q2 with |B|=1;
2. Q3 with 1+j-i >= |B|;
3. H1/H2 recurrence with no first-hit decrease.
```

Prove that each either:

```text
1. is a pair trap;
2. gives an earlier forbidden hit;
3. gives a smaller support zero-composite after a second insertion;
4. is impossible by Graham-validity.
```

---

## Current status

Proved here:

1. Q1 strict support descent;
2. Q5 collapse/prefix-zero;
3. Q4 endpoint collapse and equal-interval routing;
4. Q2 strict descent except `|B|=1`;
5. Q3 support analysis and non-descent condition;
6. H1/H2 recurrence classification.

Not proved here:

1. all atom-insertion branches descend;
2. boundary pair-trap elimination;
3. endpoint avoidance theorem.
