# Analytic gap-after obstruction routing A49

This note continues from A36 and A48.

A36 introduced the gap-after move for the separated equal-interval branch:

```text
X A G C Y -> X A C G Y
```

under the standing hypothesis

```text
sum(A)=sum(C)=a,
sum(G)=g.
```

A48 listed the five gap-after collision equations that still needed routing:

```text
E1: C_k = A_i - a
E2: C_k = a + g + Y_m
E3: G_j = A_i - 2a
E4: G_j = g + Y_m
E5: C_k = a + G_j
```

This note routes all five equations into already known obstruction classes.

Main conclusion:

```text
The gap-after collision equations introduce no new local obstruction type.
They route to two-piece zero, three-piece zero, equal-interval descent, or zero collapse.
```

Forbidden-hit recurrences from the same move still require the global A34 recurrence theorem.

---

## Standing setup

Let

```text
X A G C Y
```

be a displayed segment with

```text
sum(A)=sum(C)=a,
sum(G)=g.
```

Write decompositions by prefixes:

```text
A = P R,
G = U V,
C = K L,
Y = M N,
```

where

```text
P=prefix_i(A),     R=tail_i(A),
U=prefix_j(G),     V=tail_j(G),
K=prefix_k(C),     L=tail_k(C),
M=prefix_m(Y).
```

Let their sums be denoted by lowercase letters:

```text
p=sum(P)=A_i,
r=sum(R)=a-p,
u=sum(U)=G_j,
v=sum(V)=g-u,
k=sum(K)=C_k,
ell=sum(L)=a-k,
m=sum(M)=Y_m.
```

---

# 1. E1 route: `C_k=A_i-a`

The equation is

```text
k = p-a.
```

Since

```text
r=a-p,
```

this becomes

```text
k+r=0.
```

That is,

```text
sum(K)+sum(R)=0.
```

## Lemma A49.1: E1 is a two-piece zero composite

The equation

```text
C_k=A_i-a
```

is equivalent to

```text
sum(prefix_k(C))+sum(tail_i(A))=0.
```

### Endpoint cases

If `i=|A|`, then `R` is empty, so E1 gives

```text
C_k=0,
```

which is a zero-prefix/interior-zero branch.

If `k=|C|`, then E1 gives

```text
sum(C)+sum(tail_i(A))=0.
```

This is still a two-piece zero composite unless the tail is empty, in which case it reduces to `a=0`.

### Status

```text
two-piece zero / zero collapse
```

This routes to A28--A33.

---

# 2. E2 route: `C_k=a+g+Y_m`

The equation is

```text
k=a+g+m.
```

Since

```text
ell=a-k,
```

we get

```text
g+ell+m=0.
```

That is,

```text
sum(G)+sum(tail_k(C))+sum(prefix_m(Y))=0.
```

## Lemma A49.2: E2 is a three-piece zero composite

The equation

```text
C_k=a+g+Y_m
```

is equivalent to

```text
sum(G)+sum(tail_k(C))+sum(prefix_m(Y))=0.
```

### Endpoint cases

If `k=|C|`, then `L` is empty and E2 becomes

```text
sum(G)+sum(prefix_m(Y))=0,
```

a two-piece zero composite.

If `m=0` were allowed formally, it would become

```text
sum(G)+sum(tail_k(C))=0.
```

In actual collision rows, `m>=1`.

### Status

```text
three-piece zero / two-piece endpoint
```

This is analogous to D2 from A38/A40, but without the leading `A` block.

---

# 3. E3 route: `G_j=A_i-2a`

The equation is

```text
u=p-2a.
```

Rearrange:

```text
2a-p+u=0.
```

But

```text
2a-p = a+(a-p)=sum(C)+sum(R).
```

Therefore

```text
sum(C)+sum(tail_i(A))+sum(prefix_j(G))=0.
```

## Lemma A49.3: E3 is a three-piece zero composite

The equation

```text
G_j=A_i-2a
```

is equivalent to

```text
sum(C)+sum(tail_i(A))+sum(prefix_j(G))=0.
```

### Endpoint cases

If `i=|A|`, then `R` is empty and E3 becomes

```text
sum(C)+sum(prefix_j(G))=0,
```

a two-piece zero composite.

If `j=|G|`, then E3 becomes

```text
sum(C)+sum(tail_i(A))+sum(G)=0.
```

This remains composite-zero and may be compared against the original displayed span.

### Status

```text
three-piece zero / two-piece endpoint
```

This is not a genuinely weighted branch; the apparent coefficient `2a` is absorbed by using both `C` and `tail_i(A)`.

---

# 4. E4 route: `G_j=g+Y_m`

The equation is

```text
u=g+m.
```

Since

```text
v=g-u,
```

we obtain

```text
v+m=0.
```

That is,

```text
sum(tail_j(G))+sum(prefix_m(Y))=0.
```

## Lemma A49.4: E4 is a two-piece zero composite

The equation

```text
G_j=g+Y_m
```

is equivalent to

```text
sum(tail_j(G))+sum(prefix_m(Y))=0.
```

### Endpoint cases

If `j=|G|`, then `tail_j(G)` is empty and E4 gives

```text
Y_m=0,
```

a zero-prefix/interior-zero branch.

### Status

```text
two-piece zero / zero collapse
```

---

# 5. E5 route: `C_k=a+G_j`

The equation is

```text
k=a+u.
```

This is exactly the same algebraic form as D1 from the direct-exchange analysis:

```text
sum(A)+sum(prefix_j(G))=sum(prefix_k(C)).
```

## Lemma A49.5: E5 is an equal-interval branch

The equation

```text
C_k=a+G_j
```

is equivalent to

```text
sum(A prefix_j(G)) = sum(prefix_k(C)).
```

### Endpoint cases

If `k=|C|`, then `C_k=a`, so E5 gives

```text
G_j=0,
```

a zero-prefix/interior-zero branch.

If `k<|C|`, this is the same controlled equal-interval descent branch as D1 in A37.

### Status

```text
equal-interval descent / zero collapse
```

---

# 6. Gap-after forbidden-hit equations

The gap-after move changes the internal `C` and `G` families to

```text
x+a+C_k,
x+2a+G_j.
```

Thus a new forbidden hit can occur only if

```text
H1: x+a+C_k=f,
H2: x+2a+G_j=f.
```

These are not collision equations.  They are forbidden-landing recurrences.

## Lemma A49.6: gap-after forbidden hits are A34 recurrence branches

If the gap-after moved ordering is Graham-valid and one of `H1` or `H2` occurs, then either the new forbidden hit is earlier than the original minimal hit, contradicting minimality, or it is a non-earlier forbidden recurrence governed by the A34 global recurrence measure.

### Proof

This is the same recurrence mechanism used in A31--A34: any transformed Graham-valid ordering with a forbidden hit either violates the minimal first-hit choice or re-enters the local-blocker framework by A5. ∎

### Status

```text
recurrence with A34 measure obligation
```

---

# 7. Summary table

| Gap-after equation | Routed form | Status |
|---|---|---|
| `C_k=A_i-a` | `prefix(C)+tail(A)=0` | two-piece zero |
| `C_k=a+g+Y_m` | `G+tail(C)+prefix(Y)=0` | three-piece zero |
| `G_j=A_i-2a` | `C+tail(A)+prefix(G)=0` | three-piece zero |
| `G_j=g+Y_m` | `tail(G)+prefix(Y)=0` | two-piece zero |
| `C_k=a+G_j` | `A+prefix(G)=prefix(C)` | equal-interval descent |
| `x+a+C_k=f` | forbidden landing | A34 recurrence |
| `x+2a+G_j=f` | forbidden landing | A34 recurrence |

---

# 8. Consequence for A48

The gap-after move is now routed at the same level as the direct-exchange move.

The gap-after collision side introduces no new local obstruction type.  It routes to:

```text
two-piece zero,
three-piece zero,
equal-interval descent,
zero collapse.
```

The remaining gap-after difficulty is purely recurrence:

```text
forbidden-hit recurrences H1/H2,
controlled only by A34.
```

---

# 9. Updated global obligations

After A49, the major remaining obligations are further concentrated:

```text
G1. A34 global recurrence theorem.
G2. proper balanced D2 with k=m>=2 under global structure.
G3. long-prefix D2 with m>k.
G4. general weighted signed overlap/nesting from A20 not yet routed.
G5. midpoint boundary.
```

The previous open routing task

```text
Gap-after move obstruction equations
```

is now closed at the local collision-routing level.

---

## Target A50

A50 should update the proof-status map and then choose the next highest-value branch.

Given A49, the next highest-value analytic target is probably:

```text
proper balanced D2 with k=m>=2,
```

because:

```text
1. k=1 is controlled modulo A34 by A47;
2. m<k is strict descent by A40;
3. m>k is recurrence/long-prefix;
4. the remaining equal case k=m>=2 is the only balanced local branch not yet routed.
```

---

## Current status

Proved here:

1. E1 routes to two-piece zero;
2. E2 routes to three-piece zero;
3. E3 routes to three-piece zero, not a hard weighted branch;
4. E4 routes to two-piece zero;
5. E5 routes to equal-interval descent;
6. gap-after forbidden hits are A34 recurrence branches.

Not proved here:

1. A34 global recurrence theorem;
2. proper balanced D2 elimination;
3. endpoint avoidance theorem.
