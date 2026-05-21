# Analytic pruned prefix traps A16: eliminating old-hit and old-collision families

This note continues from A14/A15.

A14 gave exact proper-prefix interleaving formulas for the two equal-sum branches.  A15 pruned some forbidden-hit equations using secondary minimality.  This note prunes further: several remaining equations are impossible because they would already have produced either a second old `f`-hit or an old Graham collision in the original ordering.

The result is a smaller set of genuine prefix-trap equations.

---

## Standing setup

Let

```text
R=(r_1,...,r_t)
```

be a Graham-valid ordering of `A subset F_p^*`, with

```text
S_0=0,
S_i=r_1+...+r_i,
sigma=S_t.
```

Assume endpoint avoidance fails for `(A,f)`, where

```text
f != sigma.
```

Choose `R` so that its unique forbidden hit occurs as early as possible:

```text
S_h=f.
```

Since `R` is Graham-valid, the value `f` occurs among the nonempty partial sums exactly once.

---

# 1. FIRST branch pruning

Assume the FIRST equal-sum branch:

```text
R=LUV,
sum(L)=sum(U)=f,
```

where

```text
L=(r_1,...,r_h),
U=(r_{h+1},...,r_alpha),
V=(r_{alpha+1},...,r_t),
S_alpha=2f.
```

Choose `alpha` minimal among indices `>h` with `S_alpha=2f`, as in A15.

Let `U=XY`, where `X` is a nonempty proper prefix of `U`.  Write

```text
x=sum(X),
U_i = r_{h+1}+...+r_{h+i},       1 <= i <= |U|.
```

If `X` has length `q`, then

```text
x=U_q,
Y_k=U_{q+k}-U_q.
```

The proper-prefix interleaving is

```text
L X Y V -> X L Y V.
```

A14 gave the new partial-sum families:

```text
U_i                       for 1 <= i <= q,
U_q + L_j                 for 1 <= j <= |L|,
f + U_s                   for q < s <= |U|,
2f + V_m                  for 1 <= m <= |V|.
```

Here the third family uses `x+f+Y_k=f+U_{q+k}`.

---

## Lemma A16.1: FIRST equation `Y_k=-x` is impossible

In the FIRST proper-prefix interleaving, the forbidden-hit equation

```text
Y_k=-x
```

cannot occur.

### Proof

Since `x=U_q` and `Y_k=U_{q+k}-U_q`, the equation `Y_k=-x` gives

```text
U_{q+k}-U_q=-U_q,
```

hence

```text
U_{q+k}=0.
```

But then the original partial sum at index `h+q+k` is

```text
S_{h+q+k}=S_h+U_{q+k}=f+0=f.
```

Since `q+k>=1` and `q+k<=|U|-1` for a proper `Y` prefix, this is a second occurrence of `f` after index `h`, contradicting uniqueness of the forbidden hit in the original Graham-valid ordering.  ∎

---

## Lemma A16.2: FIRST collision family `f+U_s = 2f+V_m` is impossible

For `q < s <= |U|`, the collision equation

```text
f+U_s = 2f+V_m
```

cannot occur.

### Proof

In the original ordering `LUV`, the partial sum corresponding to `U_s` is

```text
S_{h+s}=f+U_s.
```

The partial sum corresponding to `V_m` is

```text
S_{alpha+m}=2f+V_m.
```

Thus the displayed equation is an equality of two old nonempty partial sums of `R`.  Since the indices are distinct, it contradicts Graham-validity.  ∎

---

## Lemma A16.3: FIRST equation `V_m=-f` is impossible

The forbidden-hit equation

```text
V_m=-f
```

cannot occur.

### Proof

If `V_m=-f`, then the old tail partial sum is

```text
S_{alpha+m}=2f+V_m=f,
```

which is a second occurrence of the forbidden value after the original hit at `h`.  ∎

---

## FIRST branch: genuinely remaining trap equations

For a proper prefix length `q` of `U`, the interleaving `XLYV` can fail only through the following remaining equations.

### Forbidden-hit family

```text
U_q + L_j = f.
```

Equivalently,

```text
U_q = f - L_j.
```

### Collision families

```text
U_i = U_q + L_j,                 1 <= i <= q,
U_i = f + U_s,                   1 <= i <= q < s <= |U|,
U_i = 2f + V_m,
U_q + L_j = f + U_s,             q < s <= |U|,
U_q + L_j = 2f + V_m.
```

The family

```text
f+U_s = 2f+V_m
```

has been eliminated by Lemma A16.2.

This is the pruned FIRST prefix-trap system.

---

# 2. SECOND branch pruning

Assume the SECOND equal-sum branch:

```text
R=ABC,
sum(B)=sum(C)=sigma-f,
```

where

```text
A=(r_1,...,r_beta),
B=(r_{beta+1},...,r_h),
C=(r_{h+1},...,r_t),
S_beta=2f-sigma.
```

Let `C=XY`, where `X` is a nonempty proper prefix of `C`.  Write

```text
x=sum(X),
C_i = r_{h+1}+...+r_{h+i},       1 <= i <= |C|.
```

If `X` has length `q`, then

```text
x=C_q,
Y_m=C_{q+m}-C_q.
```

The proper-prefix interleaving is

```text
A B X Y -> A X B Y.
```

Let

```text
sA=sum(A)=S_beta=2f-sigma.
```

A14 gave the new partial-sum families:

```text
A_i,
sA + C_i                    for 1 <= i <= q,
sA + C_q + B_k,
f + C_s                     for q < s <= |C|.
```

---

## Lemma A16.4: SECOND equation `Y_m=-x` is impossible

In the SECOND proper-prefix interleaving, the forbidden-hit equation

```text
Y_m=-x
```

cannot occur.

### Proof

Since `x=C_q` and `Y_m=C_{q+m}-C_q`, the equation gives

```text
C_{q+m}=0.
```

Then the old partial sum at index `h+q+m` is

```text
S_{h+q+m}=S_h+C_{q+m}=f.
```

Because `C` is the tail after `h`, this is a second occurrence of the forbidden value unless `q+m=0`, impossible.  Also `q+m<|C|` for a proper prefix inside `Y`; at the endpoint `|C|`, one has `C_|C|=sigma-f != 0`.  Thus the equation contradicts uniqueness of the old `f`-hit.  ∎

---

## Lemma A16.5: SECOND collision family `A_i = f+C_s` is impossible

For `q < s <= |C|`, the collision equation

```text
A_i = f+C_s
```

cannot occur.

### Proof

The value `A_i` is an old partial sum in the initial block `A`.  The value `f+C_s` is the old partial sum at index `h+s` in the tail `C`.  Equality would give a collision between two old nonempty partial sums of the Graham-valid ordering `R`.  ∎

---

## Lemma A16.6: SECOND equation `X_j=sigma-f` is impossible for proper prefixes

For a proper prefix of `C`, no prefix value `C_i` with `1 <= i < |C|` equals `sigma-f`.

### Proof

This is Lemma A15.3.  If `C_i=sigma-f` for some `i<|C|`, then

```text
S_{h+i}=f+C_i=sigma=S_t,
```

contradicting Graham-validity.  ∎

---

## SECOND branch: genuinely remaining trap equations

Away from the boundary case `beta=h`, the interleaving `AXBY` can fail only through the following remaining equations.

### Forbidden-hit family

```text
sA + C_q + B_k = f.
```

Equivalently, since `f-sA=sigma-f`,

```text
C_q = sigma-f-B_k.
```

The families

```text
C_i=sigma-f,
Y_m=-C_q
```

have been eliminated.

### Collision families

```text
A_i = sA + C_j,                  1 <= j <= q,
A_i = sA + C_q + B_k,
sA + C_j = sA + C_q + B_k,       1 <= j <= q,
sA + C_j = f + C_s,              1 <= j <= q < s <= |C|,
sA + C_q + B_k = f + C_s,        q < s <= |C|.
```

The family

```text
A_i = f+C_s
```

has been eliminated by Lemma A16.5.

If `beta=h`, then `A` itself ends at the original forbidden hit and this branch must be treated as a boundary pair-trap case.

---

# 3. Refined A17 target

The pruned prefix-trap dichotomy is now more explicit.

## FIRST pruned system

Every proper prefix `U_q` is trapped only by:

```text
U_q = f-L_j,
U_i = U_q+L_j,
U_i = f+U_s,
U_i = 2f+V_m,
U_q+L_j = f+U_s,
U_q+L_j = 2f+V_m.
```

## SECOND pruned system

Every proper prefix `C_q` is trapped only by:

```text
C_q = sigma-f-B_k,
A_i = sA+C_j,
A_i = sA+C_q+B_k,
C_j = C_q+B_k,
sA+C_j = f+C_s,
sA+C_q+B_k = f+C_s.
```

The next goal is to show that complete trapping of all proper prefixes by these equations forces either:

```text
1. an old Graham collision;
2. a local zero-sum block / punctured interval;
3. a boundary pair trap;
4. an impossible additive concentration of proper prefix sums.
```

---

## Current status

Proved here:

1. additional FIRST forbidden families `Y_k=-x` and `V_m=-f` are impossible;
2. additional FIRST old-collision family `f+U_s=2f+V_m` is impossible;
3. additional SECOND forbidden family `Y_m=-x` is impossible;
4. additional SECOND old-collision family `A_i=f+C_s` is impossible;
5. the prefix-trap systems are reduced to smaller explicit lists.

Not proved here:

1. full trapping impossibility;
2. complete equal-sum branch elimination;
3. endpoint avoidance theorem.
