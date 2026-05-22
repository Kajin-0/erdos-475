# Analytic midpoint boundary A55

This note continues from A54.

A54 identified the midpoint boundary as the next clean local branch after separated equal-interval surgery was routed modulo A34.

The midpoint branch is the zero-gap boundary of separated equal intervals:

```text
X A C Y,
sum(A)=sum(C)=a.
```

Equivalently, if the endpoints of `A C` are indexed as `x<y<v`, then

```text
S_y-S_x=S_v-S_y,
```

or

```text
2S_y=S_x+S_v.
```

This note analyzes the adjacent equal-block exchange

```text
X A C Y -> X C A Y
```

and routes its displayed collision equations into known obstruction classes.

No complete proof is claimed because forbidden-hit recurrences and external collisions still require A34/global handling.

---

## Standing setup

Let a displayed segment be

```text
X A C Y
```

where

```text
sum(A)=sum(C)=a.
```

Write

```text
x=sum(X).
```

Decompose prefixes as

```text
A=P R,
C=K L,
Y=M N,
```

where

```text
P=prefix_i(A),     R=tail_i(A),
K=prefix_k(C),     L=tail_k(C),
M=prefix_m(Y).
```

Let

```text
p=sum(P)=A_i,
r=sum(R)=a-p,
k=sum(K)=C_k,
ell=sum(L)=a-k,
mu=sum(M)=Y_m.
```

---

# 1. Adjacent equal-block exchange

The natural exchange is

```text
X A C Y -> X C A Y.
```

Original displayed-region partial sums are

```text
x+A_i,
x+a+C_k,
x+2a+Y_m.
```

After the exchange they are

```text
x+C_k,
x+a+A_i,
x+2a+Y_m.
```

Thus the `Y` family is unchanged, while the internal `A` and `C` families exchange translation levels.

---

## Lemma A55.1: adjacent exchange partial-sum formula

For the move

```text
X A C Y -> X C A Y,
```

the displayed changed partial-sum families are exactly

```text
x+C_k,
x+a+A_i.
```

The post-block family

```text
x+2a+Y_m
```

is unchanged.

### Proof

Direct summation.  Since `sum(C)=a`, after traversing `C` the running value is `x+a`; after traversing `C A` the running value is `x+2a`, the same endpoint as after `A C`. ∎

---

# 2. Displayed collision equations

Among the displayed families, possible new collisions are:

```text
M1: C_k=0,
M2: a+A_i=0,
M3: C_k=a+A_i,
M4: C_k=2a+Y_m,
M5: A_i=a+Y_m.
```

These correspond respectively to:

1. new `C` family hitting the base value before `A`;
2. new `A` family hitting the base value before `A`;
3. new `C` family colliding with new `A` family;
4. new `C` family colliding with unchanged `Y` family;
5. new `A` family colliding with unchanged `Y` family.

---

## Lemma A55.2: M1 is zero collapse

The equation

```text
C_k=0
```

is a zero-prefix of `C`.

Depending on the absolute position, it is either an interior zero interval or a prefix-zero branch.

### Proof

Immediate from the definition of `C_k`. ∎

---

## Lemma A55.3: M2 is a two-piece zero composite

The equation

```text
a+A_i=0
```

is equivalent to

```text
sum(C)+sum(prefix_i(A))=0.
```

Thus M2 is a two-piece zero composite involving all of `C` and a prefix of `A`.

### Endpoint case

If `i=|A|`, then M2 gives

```text
2a=0.
```

For odd prime fields, this implies

```text
a=0,
```

so `A` and `C` are zero-sum intervals, giving an interior-zero/prefix-zero branch.

### Proof

Use `a=sum(C)`.  If `i=|A|`, then `A_i=a`, so `a+A_i=2a`; over odd characteristic, `2a=0` implies `a=0`. ∎

---

## Lemma A55.4: M3 is a two-piece zero composite

The equation

```text
C_k=a+A_i
```

is equivalent to

```text
sum(prefix_i(A))+sum(tail_k(C))=0.
```

### Proof

Since `tail_k(C)` has sum

```text
ell=a-C_k,
```

substitute `C_k=a+A_i` to get

```text
ell=a-(a+A_i)=-A_i.
```

Hence

```text
A_i+ell=0.
```

∎

### Status

This routes directly to the A28--A33 two-piece zero-composite framework.

---

## Lemma A55.5: M4 is a three-piece zero composite

The equation

```text
C_k=2a+Y_m
```

is equivalent to

```text
sum(A)+sum(tail_k(C))+sum(prefix_m(Y))=0.
```

### Proof

Again `ell=a-C_k`.  If `C_k=2a+Y_m`, then

```text
ell=a-(2a+Y_m)=-a-Y_m.
```

Thus

```text
a+ell+Y_m=0.
```

Since `a=sum(A)`, this is the displayed three-piece zero composite. ∎

### Endpoint case

If `k=|C|`, then `ell=0`, so M4 gives

```text
sum(A)+Y_m=0,
```

a two-piece zero composite.

---

## Lemma A55.6: M5 is a two-piece zero composite

The equation

```text
A_i=a+Y_m
```

is equivalent to

```text
sum(tail_i(A))+sum(prefix_m(Y))=0.
```

### Proof

Since `tail_i(A)` has sum

```text
r=a-A_i,
```

substitute `A_i=a+Y_m` to get

```text
r=-Y_m.
```

Thus

```text
r+Y_m=0.
```

∎

### Endpoint case

If `i=|A|`, then `r=0`, so M5 gives

```text
Y_m=0,
```

which is a zero-prefix/interior-zero branch.

---

# 3. Forbidden-hit equations

The adjacent exchange can create a forbidden hit only through one of the changed displayed families:

```text
H1: x+C_k=f,
H2: x+a+A_i=f.
```

## Lemma A55.7: midpoint forbidden hits are A34 recurrence branches

If the exchanged ordering is Graham-valid and H1 or H2 occurs, then either the new forbidden hit is earlier than the original minimal forbidden hit, giving a contradiction, or it is a non-earlier transformed-order recurrence governed by A34.

### Proof

This is the standard recurrence mechanism: any Graham-valid transformed ordering with a forbidden hit either improves the first-hit index or re-enters the A5 local-blocker framework. ∎

---

# 4. External collisions

The displayed analysis above considers collisions among the moved segment families and the unchanged post-segment `Y` family.  A changed family can also collide with an unchanged partial sum lying strictly inside `X` or outside the displayed local segment.

Such collisions have the form

```text
x+C_k = S_u,
x+a+A_i = S_u,
```

for an external old partial sum `S_u`.

These are not new midpoint-specific algebraic objects.  They are ordinary transformed-order collision obstructions and must be routed through the same global framework used elsewhere:

```text
old collision/equal-interval relation,
local blocker recurrence,
A34 measure descent.
```

## Lemma A55.8: external midpoint collisions are global recurrence/equal-interval branches

Any collision of a changed midpoint-exchange family with an external unchanged partial sum defines either an equal-interval/signed-interval relation between a displayed prefix and an external interval, or a transformed-order collision recurrence.  It introduces no new local midpoint algebra.

### Proof sketch

Subtract the two partial sums.  The equality becomes a zero-sum relation over the interval between the external endpoint and the changed displayed endpoint.  Depending on orientation, this is an equal/signed interval relation already covered by A20--A27 or a transformed-order recurrence controlled only by the global measure. ∎

---

# 5. Midpoint branch status

The local displayed collision equations for the midpoint branch route as follows:

| Equation | Routed form | Status |
|---|---|---|
| `C_k=0` | zero-prefix/interior-zero | collapse |
| `a+A_i=0` | `C+prefix(A)=0` | two-piece zero |
| `C_k=a+A_i` | `prefix(A)+tail(C)=0` | two-piece zero |
| `C_k=2a+Y_m` | `A+tail(C)+prefix(Y)=0` | three-piece zero |
| `A_i=a+Y_m` | `tail(A)+prefix(Y)=0` | two-piece zero |
| `x+C_k=f` | forbidden landing | A34 recurrence |
| `x+a+A_i=f` | forbidden landing | A34 recurrence |

Thus the adjacent midpoint exchange introduces no new displayed local obstruction type.

---

# 6. Consequence

The midpoint branch is now locally routed modulo the same two unresolved global mechanisms:

```text
1. zero-composite descent/atom insertion framework A28--A33;
2. global forbidden-hit recurrence A34.
```

It is no longer a standalone local hard residual at the displayed-collision level.

---

# 7. Updated remaining obligations

After A55, the main remaining obligations are:

```text
O1. A34 global recurrence theorem.
O2. general weighted signed overlap/nesting from A20.
O3. rigorous global treatment of external collisions for transformed block moves.
```

The midpoint displayed-collision branch is locally routed.

---

# 8. Target A56

The next local target should be the general weighted signed overlap/nesting branch from A20.

Typical relation:

```text
sum(A)+2sum(B)+sum(C)=0.
```

A38 and A49 showed that some apparent coefficient-2 branches are transported-prefix artifacts that rewrite to composite-zero relations.  A56 should determine whether the remaining A20 weighted signed branches also rewrite to composite-zero after choosing the correct prefix/tail variables.

Suggested task:

```text
A56: weighted signed residual normal forms
```

For each A20 weighted class, express it in prefix/tail notation and test whether it is equivalent to:

```text
two-piece zero,
three-piece zero,
midpoint boundary,
equal-interval descent,
or a genuinely weighted relation.
```

---

## Current status

Proved here:

1. midpoint adjacent-exchange formulas;
2. displayed collision routing for M1--M5;
3. midpoint forbidden hits are A34 recurrences;
4. midpoint displayed-collision branch is locally routed.

Not proved here:

1. A34 global recurrence theorem;
2. full external-collision descent;
3. weighted signed residual elimination;
4. endpoint avoidance theorem.
