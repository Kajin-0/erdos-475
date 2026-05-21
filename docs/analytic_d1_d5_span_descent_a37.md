# Analytic D1/D5 span descent A37

This note continues from A36.

A36 analyzed the separated equal-interval residual

```text
X A G C Y,
```

with

```text
sum(A)=sum(C)=a.
```

The direct exchange

```text
X A G C Y -> X C G A Y
```

produced five collision families.  A36 already routed D3 and D4 to controlled two-piece-zero branches.  This note focuses on the two clean remaining equal-interval families:

```text
D1: C_k = a + G_j,
D5: C_k = a + g + A_i.
```

The goal is to prove endpoint collapses and identify strict span descent where available.

---

## Standing setup

Let

```text
X A G C Y
```

be a displayed segment in an ordering.  Write

```text
sum(A)=sum(C)=a,
sum(G)=g,
x=sum(X).
```

Let internal prefix sums be

```text
A_i,
G_j,
C_k,
Y_m.
```

Let lengths be

```text
|A|=r,
|G|=s,
|C|=r_C.
```

The original separated equal-interval relation has active support

```text
A and C
```

and enclosing span

```text
|A|+|G|+|C|.
```

---

# 1. D1: `C_k = a + G_j`

D1 is

```text
C_k = a + G_j.
```

Equivalently,

```text
sum(A)+G_j = C_k.
```

That is, the interval consisting of all of `A` plus the first `j` entries of `G` has the same sum as the first `k` entries of `C`.

---

## Lemma A37.1: D1 is an equal-interval relation

D1 is equivalent to

```text
sum(A G_{[1,j]}) = sum(C_{[1,k]}).
```

In interval notation, if `A=(p,q]`, `G=(q,r]`, and `C=(r,s_end]`, then D1 is

```text
sum(p,q+j] = sum(r,r+k].
```

### Proof

The left side has sum `a+G_j`; the right side has sum `C_k`.  This is exactly D1.  ∎

---

## Lemma A37.2: D1 endpoint `j=0` is the original separated equal relation restricted to a C-prefix

If one formally allows `j=0`, then D1 becomes

```text
a=C_k.
```

If `k=|C|`, this is the original equality `sum(A)=sum(C)`.  If `k<|C|`, then a proper prefix of `C` has the full sum of `C`, so the tail of `C` has sum zero:

```text
sum(C_{k+1},...,C_{|C|})=0.
```

This is an interior-zero or prefix-zero branch depending on position.

### Proof

If `C_k=a=sum(C)`, then `sum(C)-C_k=0`, giving the stated tail-zero relation.  ∎

### Note

In the actual collision equation from A36, `j>=1`, but this endpoint observation explains the limiting geometry.

---

## Lemma A37.3: D1 endpoint `k=|C|` collapses to a gap-prefix zero branch

If `k=|C|`, then `C_k=a`, so D1 gives

```text
a=a+G_j.
```

Hence

```text
G_j=0.
```

This is a zero-prefix of the gap block `G`.  If the gap prefix is interior in the current ordering, it contradicts Graham-validity.  If it begins at the basepoint, it is a prefix-zero branch.

### Proof

Substitute `C_k=a` into `C_k=a+G_j`.  ∎

---

## Lemma A37.4: D1 with proper `j` and proper `k` is a shorter separated equal-interval relation

Assume

```text
1 <= j <= |G|,
1 <= k < |C|.
```

Then D1 gives an equal-interval relation between:

```text
A plus a prefix of G,
proper prefix of C.
```

Its enclosing span is at most

```text
|A|+j + k,
```

while the original separated equal structure involved the full span

```text
|A|+|G|+|C|.
```

If either `j<|G|` or `k<|C|`, this is a strict support/enclosing-span reduction relative to the full displayed segment.  Since `k<|C|` by hypothesis, D1 is a strict descent unless the proof measure counts only the original active pieces `A,C` and ignores the gap.

### Proof

The new left interval uses `|A|+j` atoms; the new right interval uses `k` atoms.  Since `k<|C|`, the new right side is strictly shorter than the original `C`.  ∎

### Status

D1 is controlled modulo the measure convention.  Under enclosing-span or total-support measure including the gap-prefix actually used, it descends.  If using only active-piece support `|A|+|C|`, D1 may increase the left side by adding a gap prefix, so the measure must be span-aware as in A34.

---

# 2. D5: `C_k = a + g + A_i`

D5 is

```text
C_k = a + g + A_i.
```

Equivalently,

```text
C_k - A_i = a+g.
```

The quantity `a+g` is the sum of the interval `A G`.

---

## Lemma A37.5: D5 is an equal-interval relation after moving A-prefix to the opposite side

D5 is equivalent to

```text
sum(A G) + A_i = C_k.
```

Equivalently,

```text
sum(A G A_{[1,i]}) = C_k
```

as a formal composite relation.

It is not, in the original linear order, a single ordinary interval on the left unless a copy/transport of `A_i` is made adjacent by a block move.

### Proof

Directly rewrite `a+g+A_i=C_k`.  ∎

### Interpretation

D5 is more difficult than D1 because it repeats a prefix of `A` in the algebraic expression.  It is not merely an equality between two disjoint ordinary intervals in the original order.

This is a weighted/transported equal-interval branch, closely related to the weighted signed residuals.

---

## Lemma A37.6: D5 endpoint `i=|A|` collapses to a C-prefix/gap-tail relation

If `i=|A|`, then `A_i=a`, so D5 gives

```text
C_k = 2a+g.
```

Since the total sum of `A G C` is

```text
2a+g,
```

we get

```text
C_k = sum(A G C).
```

Therefore the complement of `C_k` inside the displayed segment has sum zero:

```text
sum(A G) + sum(C_{k+1},...,C_{|C|}) = 0.
```

### Proof

Substitute `A_i=a`.  Then subtract `C_k` from the total sum `2a+g` of `AGC`.  ∎

### Status

Endpoint `i=|A|` routes to a two-piece zero composite involving `AG` and the tail of `C`.

If `k=|C|` also, then `C_k=a`, so D5 gives

```text
a=2a+g,
```

or

```text
a+g=0,
```

meaning `AG` is a zero block/composite.

---

## Lemma A37.7: D5 endpoint `k=|C|` gives an A-prefix/gap zero relation

If `k=|C|`, then `C_k=a`, and D5 gives

```text
a=a+g+A_i.
```

Hence

```text
G+A_i=0.
```

That is,

```text
G_total + A_i = 0.
```

This is a two-piece zero composite between the whole gap `G` and a prefix of `A`.

### Proof

Substitute `C_k=a` and cancel.  ∎

---

## Lemma A37.8: D5 proper-interior case is a transported-prefix weighted branch

Assume

```text
i<|A|,
k<|C|.
```

Then D5 can be rewritten as

```text
C_k - A_i = a+g.
```

Since

```text
a-A_i = tail_i(A),
```

we also have

```text
C_k = A_i+g+A_i+tail_i(A),
```

or

```text
C_k - tail_i(A) - g = 2A_i.
```

Thus the proper-interior D5 branch is a weighted relation involving coefficient `2` on the transported prefix `A_i`.

### Proof

Use `a=A_i+tail_i(A)` in `C_k=a+g+A_i`.  ∎

### Status

D5 proper-interior does not close by simple span descent.  It routes to the weighted signed / midpoint family.  It should be grouped with the hard weighted branches H2 from A35.

---

# 3. Summary table

| Branch | Endpoint/proper case | Outcome |
|---|---|---|
| D1 | `k=|C|` | `G_j=0`, zero-prefix/interior-zero |
| D1 | `k<|C|` | shorter equal-interval relation using `A+G_prefix` and `C_prefix` |
| D5 | `i=|A|` | two-piece zero: `AG + tail(C)=0` |
| D5 | `k=|C|` | two-piece zero: `G + A_prefix=0` |
| D5 | `i<|A|`, `k<|C|` | transported-prefix weighted branch |

---

# 4. Consequence for A36

D1 is essentially controlled under the span-first measure from A34.

D5 is controlled at endpoints but has a genuinely hard proper-interior branch.  This hard branch is not separate from the existing weighted signed obstruction class; it is another manifestation of it.

Thus separated equal-interval surgery reduces mostly to:

```text
equal-interval descent,
two-piece zero composites,
weighted transported-prefix branches,
forbidden recurrences.
```

---

# 5. Target A38

A38 should attack the weighted transported-prefix branch:

```text
C_k = a+g+A_i,
```

with

```text
i<|A|,
k<|C|.
```

This should be analyzed together with the A20 weighted signed relations

```text
sum(A)+2sum(B)+sum(C)=0.
```

The likely useful move is a midpoint/pair-swap operation that specifically targets the doubled prefix term.

---

## Current status

Proved here:

1. D1 endpoint collapse `k=|C| -> G_j=0`;
2. D1 proper-prefix branch is shorter/span-controlled equal interval;
3. D5 endpoint `i=|A|` routes to two-piece zero;
4. D5 endpoint `k=|C|` routes to two-piece zero;
5. D5 proper-interior routes to weighted transported-prefix branch.

Not proved here:

1. D5 proper-interior elimination;
2. D2 elimination;
3. forbidden recurrence descent;
4. endpoint avoidance theorem.
