# Analytic proper-prefix interleaving A14: breaking equal-sum traps

This note continues from A12/A13.

A13 showed that exchanging whole equal-sum blocks does not avoid the forbidden value `f`; it merely moves the `f`-hit to a different block endpoint.  The natural next move is therefore to move only a **proper prefix** of one equal-sum block.

This note computes the exact partial-sum formulas and obstruction equations for that move.

It does not complete the proof, but it converts the equal-sum branch into a finite family of explicit equations involving proper-prefix sums.

---

## Standing setup

Let

```text
R=(r_1,...,r_t)
```

be a Graham-valid ordering of `A subset F_p^*`, with partial sums

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

---

# 1. FIRST branch: `sum(L)=sum(U)=f`

Assume the FIRST equal-sum trap from A12:

```text
R = L U V,
sum(L)=sum(U)=f,
```

where

```text
L=(r_1,...,r_h),
U=(r_{h+1},...,r_alpha),
V=(r_{alpha+1},...,r_t).
```

Let `U` be split into two nonempty pieces

```text
U = X Y
```

where `X` is a proper nonempty prefix of `U`.  Write

```text
x = sum(X),
sum(Y)=f-x.
```

The proper-prefix interleaving move is

```text
L X Y V  ->  X L Y V.
```

Since `XLY` and `LXY` have the same total sum `2f`, all tail partial sums after this region are unchanged.

---

## Lemma A14.1: FIRST proper-prefix interleaving partial sums

Let

```text
X_i = x_1+...+x_i,       1 <= i <= |X|,
L_j = l_1+...+l_j,       1 <= j <= |L|,
Y_k = y_1+...+y_k,       1 <= k <= |Y|,
V_m = v_1+...+v_m,       1 <= m <= |V|.
```

The nonempty partial sums of the interleaved ordering

```text
X L Y V
```

are

```text
X_i,
x + L_j,
x + f + Y_k,
2f + V_m.
```

The final value after `XLY` is `2f`, the same value as after `LXY` in the original ordering.

### Proof

Direct summation.  After `X`, the running sum is `x`.  Passing through `L` gives `x+L_j`.  After `XL`, the running sum is `x+f`.  Passing through `Y` gives `x+f+Y_k`.  Since `sum(Y)=f-x`, the endpoint after `XLY` is `2f`.  The tail therefore has the same translated values `2f+V_m` as in the original ordering after `alpha`.  ∎

---

## Lemma A14.2: FIRST proper-prefix forbidden-hit criterion

The interleaved ordering `XLYV` hits the forbidden value `f` if and only if one of the following holds:

```text
X_i = f,
L_j = f-x,
Y_k = -x,
V_m = -f.
```

The final condition `V_m=-f` cannot occur in the standing endpoint-avoidance counterexample, because it would imply an old second hit of `f` after `alpha`.

### Proof

Using Lemma A14.1:

- `X_i=f` gives a hit in the initial `X` block.
- `x+L_j=f` is equivalent to `L_j=f-x`.
- `x+f+Y_k=f` is equivalent to `Y_k=-x`.
- `2f+V_m=f` is equivalent to `V_m=-f`.

In the original ordering, tail partial sums after `alpha` are also `2f+V_m`.  Since the original ordering has unique `f`-hit at index `h<alpha`, no tail value can equal `f`.  Hence `V_m=-f` is impossible.  ∎

---

## Lemma A14.3: FIRST proper-prefix Graham-validity criterion

The interleaved ordering `XLYV` is Graham-valid if and only if no collision occurs among the four displayed families

```text
X_i,
x+L_j,
x+f+Y_k,
2f+V_m.
```

Internal collisions inside each family are ruled out if the corresponding original block-prefix family was internally collision-free; cross-collisions are exactly the equations:

```text
X_i = x+L_j,
X_i = x+f+Y_k,
X_i = 2f+V_m,
x+L_j = x+f+Y_k,
x+L_j = 2f+V_m,
x+f+Y_k = 2f+V_m.
```

Equivalently,

```text
X_i-x = L_j,
X_i-x-f = Y_k,
X_i-2f = V_m,
L_j-f = Y_k,
x+L_j-2f = V_m,
x+Y_k-f = V_m.
```

### Proof

Immediate from Lemma A14.1.  ∎

---

## Consequence for FIRST branch

A FIRST-branch escape is obtained if there exists a proper nonempty prefix `X` of `U` such that:

1. none of the forbidden-hit equations in Lemma A14.2 holds;
2. none of the collision equations in Lemma A14.3 holds.

If no such prefix exists, then every proper prefix sum

```text
x=sum(X)
```

is trapped by one of finitely many explicit equations against the internal prefix sets of `L`, `Y`, or `V`.

This is the precise version of the informal `large atom or pair trap` statement for the FIRST equal-sum branch.

---

# 2. SECOND branch: `sum(B)=sum(C)=sigma-f`

Assume the SECOND equal-sum trap from A12:

```text
R = A B C,
sum(B)=sum(C)=sigma-f,
```

where

```text
A=(r_1,...,r_beta),
B=(r_{beta+1},...,r_h),
C=(r_{h+1},...,r_t).
```

Let `C` be split into two nonempty pieces

```text
C = X Y
```

where `X` is a proper nonempty prefix of `C`.  Write

```text
x=sum(X),
sum(Y)=sigma-f-x.
```

The proper-prefix interleaving move is

```text
A B X Y  ->  A X B Y.
```

This moves a proper prefix of the tail block `C` immediately after `A`, before the block `B`.

---

## Lemma A14.4: SECOND proper-prefix interleaving partial sums

Let

```text
A_i = a_1+...+a_i,       1 <= i <= |A|,
X_j = x_1+...+x_j,       1 <= j <= |X|,
B_k = b_1+...+b_k,       1 <= k <= |B|,
Y_m = y_1+...+y_m,       1 <= m <= |Y|.
```

Let

```text
sA=sum(A)=S_beta=2f-sigma.
```

The nonempty partial sums of the interleaved ordering

```text
A X B Y
```

are

```text
A_i,
sA + X_j,
sA + x + B_k,
sA + x + (sigma-f) + Y_m.
```

Since `sA=2f-sigma`, the final family can also be written as

```text
f+x+Y_m.
```

### Proof

The `A` block is unchanged.  After `A`, the running sum is `sA`.  Passing through `X` gives `sA+X_j`.  After `AX`, the running sum is `sA+x`.  Passing through `B` gives `sA+x+B_k`.  Since `sum(B)=sigma-f`, the running sum after `AXB` is `sA+x+sigma-f=f+x`.  Passing through `Y` gives `f+x+Y_m`.  ∎

---

## Lemma A14.5: SECOND proper-prefix forbidden-hit criterion

The interleaved ordering `AXBY` hits the forbidden value `f` if and only if one of the following holds:

```text
A_i = f,
X_j = sigma-f,
B_k = sigma-f-x,
Y_m = -x.
```

The first condition cannot occur in the standing setup except at the original hit if `i=h`, but `A` ends at `beta <= h`; in the SECOND branch the original hit is not generally inside `A` unless `beta=h`.  The condition must therefore be retained explicitly.

### Proof

Using Lemma A14.4:

- `A_i=f` is direct.
- `sA+X_j=f` is equivalent to `X_j=f-sA=f-(2f-sigma)=sigma-f`.
- `sA+x+B_k=f` is equivalent to `B_k=f-sA-x=sigma-f-x`.
- `f+x+Y_m=f` is equivalent to `Y_m=-x`.

∎

---

## Lemma A14.6: SECOND proper-prefix Graham-validity criterion

The interleaved ordering `AXBY` is Graham-valid if and only if no collision occurs among the four displayed families

```text
A_i,
sA+X_j,
sA+x+B_k,
f+x+Y_m.
```

Equivalently, all cross-family equations are avoided:

```text
A_i = sA+X_j,
A_i = sA+x+B_k,
A_i = f+x+Y_m,
sA+X_j = sA+x+B_k,
sA+X_j = f+x+Y_m,
sA+x+B_k = f+x+Y_m.
```

After cancellation, these become

```text
A_i-sA = X_j,
A_i-sA-x = B_k,
A_i-f-x = Y_m,
X_j-x = B_k,
X_j-(f-sA)-x = Y_m,
sA+B_k-f = Y_m.
```

Since `f-sA=sigma-f`, the fifth equation may also be written

```text
X_j-(sigma-f)-x = Y_m.
```

### Proof

Immediate from Lemma A14.4.  ∎

---

## Consequence for SECOND branch

A SECOND-branch escape is obtained if there exists a proper nonempty prefix `X` of `C` such that:

1. none of the forbidden-hit equations in Lemma A14.5 holds;
2. none of the collision equations in Lemma A14.6 holds.

If no such prefix exists, then every proper prefix sum

```text
x=sum(X)
```

is trapped by one of finitely many explicit equations against the internal prefix sets of `A`, `B`, or `Y`.

---

# 3. Refined A15 target: prefix-trap dichotomy

Both FIRST and SECOND branches now have the same schematic form.

Let `P` be the set of proper prefix sums of the movable block.  For each `x in P`, a proper-prefix interleaving either succeeds or fails because `x` lies in one of finitely many forbidden fibers determined by already-existing prefix sets.

## Target A15

Prove a prefix-trap dichotomy:

> If every proper prefix of the movable equal-sum block is trapped by the equations in A14, then either:
>
> 1. a local zero-sum block is exposed, reducing to A9/A11;
> 2. a short algebraic atom occurs, such as `a=2b`, `b=2a`, or a two-term pair trap;
> 3. the movable block has a strong additive concentration impossible for a set in `F_p^*` under the minimal-counterexample hypotheses.

This is the next real mathematical gap.

---

## Current status

Proved here:

1. FIRST proper-prefix interleaving partial-sum formula;
2. FIRST forbidden-hit and collision criteria;
3. SECOND proper-prefix interleaving partial-sum formula;
4. SECOND forbidden-hit and collision criteria;
5. reduction of equal-sum branches to explicit prefix-trap equations.

Not proved here:

1. prefix-trap dichotomy;
2. elimination of all equal-sum traps;
3. endpoint avoidance theorem.
