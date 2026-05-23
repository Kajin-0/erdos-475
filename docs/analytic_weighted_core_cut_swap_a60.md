# Analytic weighted core cut-swap A60

This note continues from A59.

A59 showed that static cuts of the doubled block in a genuine weighted core expose nested identities but do not directly close the branch.  The next natural operation is dynamic: cut the doubled block

```text
B=P R
```

and swap the two pieces:

```text
A P R C -> A R P C.
```

This note derives the exact partial-sum formulas and routes the displayed collision equations.

No complete proof is claimed here.  The point is to determine whether this dynamic move introduces any new local obstruction type.

---

## Standing setup

Let a displayed segment be

```text
X A P R C Y
```

where

```text
B=P R,
a=sum(A),
p=sum(P),
r=sum(R),
c=sum(C),
b=p+r.
```

Assume the weighted core relation

```text
a+2b+c=0,
```

or equivalently

```text
a+2p+2r+c=0.
```

Assume the A56 easy reductions are absent unless explicitly mentioned:

```text
b != 0,
a+b != 0,
b+c != 0,
a != c.
```

Let prefixes be denoted by

```text
A_i,
P_u,
R_v,
C_k,
Y_m.
```

The cut-swap move is

```text
X A P R C Y -> X A R P C Y.
```

---

# 1. Partial-sum formula

## Lemma A60.1: cut-swap partial-sum families

In the original ordering

```text
X A P R C Y,
```

the displayed-region partial sums are

```text
x+A_i,
x+a+P_u,
x+a+p+R_v,
x+a+p+r+C_k,
x+a+p+r+c+Y_m.
```

In the swapped ordering

```text
X A R P C Y,
```

the displayed-region partial sums are

```text
x+A_i,
x+a+R_v,
x+a+r+P_u,
x+a+r+p+C_k,
x+a+r+p+c+Y_m.
```

Thus:

1. the `A` family is unchanged;
2. the `C` family is unchanged because `p+r=r+p`;
3. the `Y` family is unchanged;
4. the `P` and `R` internal families change translation levels.

### Proof

Direct summation.  The total sum of `P R` equals the total sum of `R P`, so everything after the full middle block has the same translation. ∎

---

# 2. Collision equations involving the new R-family

The new R-family is

```text
x+a+R_v.
```

It can collide with unchanged `A`, unchanged `C`, unchanged `Y`, or the new `P` family.

---

## Lemma A60.2: new R against A gives a two-piece zero composite

If

```text
x+a+R_v=x+A_i,
```

then

```text
R_v+tail_i(A)=0.
```

### Proof

The equality gives `R_v=A_i-a`.  Since `tail_i(A)` has sum `a-A_i`, the result follows. ∎

### Endpoint case

If `i=|A|`, this gives `R_v=0`, a zero-prefix/interior-zero branch inside `R`.

---

## Lemma A60.3: new R against C gives a three-piece zero composite

If

```text
x+a+R_v=x+a+p+r+C_k,
```

then

```text
sum(P)+sum(tail_v(R))+C_k=0.
```

### Proof

The equality gives

```text
R_v=p+r+C_k.
```

Since `tail_v(R)` has sum `r-R_v`,

```text
r-R_v = r-(p+r+C_k)=-p-C_k.
```

Thus

```text
p+tail_v(R)+C_k=0.
```

∎

### Endpoint case

If `v=|R|`, this gives

```text
p+C_k=0,
```

a two-piece zero composite between `P` and a prefix of `C`.

---

## Lemma A60.4: new R against Y gives a three-piece zero composite

If

```text
x+a+R_v=x+a+p+r+c+Y_m,
```

then

```text
sum(P)+sum(tail_v(R))+sum(C)+Y_m=0.
```

### Proof

The equality gives

```text
R_v=p+r+c+Y_m.
```

Therefore

```text
r-R_v=-p-c-Y_m.
```

So

```text
p+tail_v(R)+c+Y_m=0.
```

∎

---

# 3. Collision equations involving the new P-family

The new P-family is

```text
x+a+r+P_u.
```

---

## Lemma A60.5: new P against A gives a three-piece zero composite

If

```text
x+a+r+P_u=x+A_i,
```

then

```text
tail_i(A)+sum(R)+P_u=0.
```

### Proof

The equality gives

```text
A_i=a+r+P_u.
```

Thus

```text
a-A_i=-r-P_u.
```

So `tail_i(A)+R+P_u=0`. ∎

---

## Lemma A60.6: new P against C gives a two-piece zero composite

If

```text
x+a+r+P_u=x+a+p+r+C_k,
```

then

```text
tail_u(P)+C_k=0.
```

### Proof

The equality gives

```text
P_u=p+C_k.
```

Since `tail_u(P)` has sum `p-P_u`, we get `tail_u(P)=-C_k`. ∎

### Endpoint case

If `u=|P|`, this gives `C_k=0`, a zero-prefix/interior-zero branch.

---

## Lemma A60.7: new P against Y gives a three-piece zero composite

If

```text
x+a+r+P_u=x+a+p+r+c+Y_m,
```

then

```text
tail_u(P)+sum(C)+Y_m=0.
```

### Proof

The equality gives

```text
P_u=p+c+Y_m.
```

Therefore

```text
p-P_u=-c-Y_m.
```

So `tail_u(P)+C+Y_m=0`. ∎

---

## Lemma A60.8: new R against new P gives a two-piece zero composite

If

```text
x+a+R_v=x+a+r+P_u,
```

then

```text
tail_v(R)+P_u=0.
```

### Proof

The equality gives `R_v=r+P_u`, hence `r-R_v=-P_u`. ∎

---

# 4. Forbidden-hit equations

The cut-swap can create a new forbidden hit only through one of the changed families:

```text
H_R: x+a+R_v=f,
H_P: x+a+r+P_u=f.
```

## Lemma A60.9: cut-swap forbidden hits are A34 recurrence branches

If the swapped ordering is Graham-valid and either `H_R` or `H_P` occurs, then either the new forbidden hit is earlier than the original minimal forbidden hit, contradicting minimality, or it is a non-earlier transformed-order recurrence governed by A34.

### Proof

This is the standard A5/A34 recurrence mechanism applied to the transformed ordering. ∎

---

# 5. Summary table

| Cut-swap collision | Routed form | Status |
|---|---|---|
| `a+R_v=A_i` | `R_prefix+tail(A)=0` | two-piece zero |
| `a+R_v=a+p+r+C_k` | `P+tail(R)+C_prefix=0` | three-piece zero |
| `a+R_v=a+p+r+c+Y_m` | `P+tail(R)+C+Y_prefix=0` | three/four-piece zero |
| `a+r+P_u=A_i` | `tail(A)+R+P_prefix=0` | three-piece zero |
| `a+r+P_u=a+p+r+C_k` | `tail(P)+C_prefix=0` | two-piece zero |
| `a+r+P_u=a+p+r+c+Y_m` | `tail(P)+C+Y_prefix=0` | three-piece zero |
| `a+R_v=a+r+P_u` | `tail(R)+P_prefix=0` | two-piece zero |
| `x+a+R_v=f` | forbidden landing | A34 recurrence |
| `x+a+r+P_u=f` | forbidden landing | A34 recurrence |

---

# 6. Consequence for the genuine weighted core

The internal cut-swap introduces no new local collision type.

All displayed collision obstructions route to:

```text
two-piece zero,
three-piece zero,
higher composite-zero,
zero collapse.
```

The only nonlocal obstruction is forbidden-hit recurrence, again governed by A34.

This does not prove the weighted core is eliminated, because one still needs to prove that a suitable proper cut `B=P R` and the corresponding swap can be used in the global minimal-counterexample setting.  But it shows that, once the cut-swap is attempted, its displayed failures are controlled locally.

---

# 7. Remaining issue: choosing the cut

A60 analyzes a fixed proper cut `B=P R`.

To turn this into a full weighted-core reduction, one still needs a cut-selection theorem:

> In a genuine weighted core, there exists a proper cut `B=P R` such that the cut-swap either succeeds or all its obstruction branches descend under the global measure.

This is not proved here.

The most likely strategy is to choose the first cut of `B` for which one of the routed zero-composite branches has minimal support, then use A31--A33 plus A34 recurrence.

---

# 8. Target A61

A61 should update the status map:

```text
weighted core cut-swap displayed collisions: locally routed;
weighted core cut-selection theorem: open;
A34 recurrence theorem: open.
```

A possible follow-up A62 would implement a finite search for genuine weighted cores with all cut-swap displayed obstructions absent, to test whether the cut-selection theorem is plausible.

---

## Current status

Proved here:

1. exact partial-sum formulas for `A P R C -> A R P C`;
2. all displayed collision equations route to zero-composite or zero-collapse classes;
3. cut-swap forbidden hits are A34 recurrences.

Not proved here:

1. existence of a globally useful cut;
2. genuine weighted core elimination;
3. A34 global recurrence theorem;
4. endpoint avoidance theorem.
