# Analytic D2 composite-zero accounting A40

This note continues from A38/A39.

A38 showed that the D2 branch from separated equal-interval surgery routes to a composite-zero relation.  A39 correctly classified D2 as requiring descent accounting because the branch removes a prefix of `C` but adds a prefix of `Y`.

This note gives the exact descent condition.

---

## Standing setup

Let a displayed segment be

```text
X A G C Y
```

with

```text
sum(A)=sum(C)=a,
sum(G)=g.
```

Write

```text
C=K L,
Y=M N,
```

where:

```text
K=prefix_k(C),
L=tail_k(C),
M=prefix_m(Y).
```

Let

```text
|A|=r,
|G|=s,
|C|=c,
|K|=k,
|L|=c-k,
|M|=m.
```

The D2 obstruction equation from A36 is

```text
C_k=2a+g+Y_m.
```

A38 proved this is equivalent to the composite-zero relation

```text
sum(A G)+sum(L)+sum(M)=0.
```

That is,

```text
A G + tail_k(C) + prefix_m(Y) = 0.
```

---

# 1. Exact support comparison

The original displayed separated-equal object uses the span

```text
A G C
```

with support length

```text
r+s+c.
```

The D2 composite-zero object uses

```text
A G L M
```

with support length

```text
r+s+(c-k)+m.
```

---

## Lemma A40.1: D2 is strict support descent iff `m<k`

The D2 composite-zero branch has smaller support than the original displayed span `A G C` if and only if

```text
m<k.
```

It has equal support if and only if

```text
m=k.
```

It has larger support if and only if

```text
m>k.
```

### Proof

Subtract new support from old support:

```text
(r+s+c) - (r+s+c-k+m) = k-m.
```

Therefore the new support is smaller exactly when `k-m>0`, equal exactly when `k=m`, and larger exactly when `k-m<0`.  ∎

---

# 2. Endpoint cases

## Lemma A40.2: D2 with `k=|C|` is a two-piece zero branch

If

```text
k=c,
```

then `L` is empty, and D2 reduces to

```text
sum(A G)+sum(M)=0.
```

This is a two-piece zero composite involving `AG` and a prefix of `Y`.

It is strict support descent relative to `AGC` iff

```text
m<c.
```

### Proof

Set `L=empty` in the A38 D2 relation.  The support comparison is Lemma A40.1 with `k=c`.  ∎

---

## Lemma A40.3: D2 with `m=0` would be strict descent, but actual collision rows have `m>=1`

If one formally allows `m=0`, D2 becomes

```text
sum(A G)+sum(L)=0,
```

which is strict descent for every `k>=1`.

In the actual collision family, `Y_m` is a nonempty prefix, so

```text
m>=1.
```

### Proof

Immediate from Lemma A40.1.  ∎

---

# 3. Non-descending D2 range

The non-descending range is

```text
m>=k.
```

In this range, the prefix of `Y` introduced into the zero composite is at least as long as the prefix of `C` removed from the original span.

This is the exact residual accounting obstruction.

## Lemma A40.4: D2 non-descent is a long-prefix recurrence condition

If D2 does not strictly descend by support, then

```text
m>=k.
```

Equivalently, the added `Y` prefix has length at least the removed `C` prefix.

Thus every non-descending D2 case is a long-prefix branch, analogous to the long-prefix forbidden recurrence from A34.

### Proof

This is Lemma A40.1 restated.  ∎

---

# 4. Algebraic form of the equal-support boundary `m=k`

The boundary case

```text
m=k
```

is important because it preserves support size.

D2 says

```text
K = A+G+C+M
```

in sum notation, since `sum(AGC)=2a+g`.

Equivalently,

```text
sum(A G L M)=0.
```

where `|M|=|K|`.

This is a length-balanced transfer: the prefix `K` of `C` is replaced by an equally long prefix `M` of `Y`.

## Lemma A40.5: equal-support D2 is a balanced transfer from C-prefix to Y-prefix

If `m=k`, then the D2 zero composite

```text
A G L M
```

has the same support length as `A G C` and differs by replacing

```text
K=prefix_k(C)
```

with

```text
M=prefix_k(Y).
```

### Proof

The original span is `A G K L`; the D2 composite is `A G L M`.  When `|M|=|K|`, the lengths match exactly.  ∎

### Status

This is not closed.  It should be treated as a recurrence/balanced-transfer branch.  A possible next move is to compare the internal prefix structures of `K` and `M`, producing either a smaller equal interval or a midpoint-type relation.

---

# 5. Updating the D2 status

The D2 routing should now be:

| Condition | Routed class | Status |
|---|---|---|
| `m<k` | three-piece zero `AG+tail(C)+prefix(Y)=0` | strict support descent |
| `m=k` | balanced transfer | recurrence / measure tie |
| `m>k` | long-prefix composite | recurrence requiring A34 measure |
| `k=|C|`, `m<k` | two-piece zero `AG+prefix(Y)=0` | strict support descent |
| `k=|C|`, `m>=k` | long-prefix two-piece zero | recurrence |

---

# 6. Relation to global recurrence measure

A34 proposed the span-first obstruction measure

```text
M*(O)=(h, span, pieces, type_rank, boundary_rank).
```

A40 shows that D2 obeys this measure exactly in the range

```text
m<k.
```

The residual range

```text
m>=k
```

must be handled by the recurrence theorem A34.R or by a separate balanced-transfer argument.

---

# 7. Target A41

The next clean target is the balanced-transfer branch

```text
m=k.
```

Given equal-length prefixes

```text
K=prefix_k(C),
M=prefix_k(Y)
```

and the zero composite

```text
A G L M=0,
```

try to swap/compare `K` and `M` prefix-by-prefix.  The expected outcomes are:

```text
1. a smaller equal interval;
2. a midpoint branch;
3. a pair trap;
4. a strict descent after the first unequal internal prefix;
5. an impossible atom equality if all corresponding prefixes match.
```

---

## Current status

Proved here:

1. exact D2 support comparison;
2. strict descent iff `m<k`;
3. equal support iff `m=k`;
4. long-prefix non-descent iff `m>k`;
5. endpoint `k=|C|` status.

Not proved here:

1. balanced-transfer branch elimination;
2. long-prefix recurrence elimination;
3. endpoint avoidance theorem.
