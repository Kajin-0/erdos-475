# Analytic two-zero-block uncrossing A10: interval geometry and solid constraints

This note starts the two-zero-block uncrossing analysis suggested by A8/A9.

It does **not** prove the final uncrossing theorem.  It records the rigorous interval algebra and the key structural constraint imposed by Graham-validity: ordinary zero-sum intervals cannot occur away from the initial basepoint.

## Standing notation

Let

```text
R = (r_1, ..., r_t)
```

be an ordering of `A subset F_p^*`.  Write

```text
S_0 = 0,
S_i = r_1 + ... + r_i,    1 <= i <= t,
sigma = S_t.
```

For `0 <= u < v <= t`, define the linear interval

```text
(u,v] = (r_{u+1}, ..., r_v),
sum(u,v] = S_v - S_u.
```

A linear interval `(u,v]` is called **interior** if

```text
1 <= u < v <= t.
```

It is called a **prefix interval** if `u=0`.

For cyclic intervals, indices are taken on the cyclic edge order

```text
1,2,...,t,1,2,...
```

and a cyclic interval crossing the endpoint has the form

```text
(alpha,t] union (0,beta]
```

with `0 <= beta < alpha <= t`.

---

## Lemma A10.1: Graham-validity forbids interior zero-sum intervals

If `R` is Graham-valid, then there is no interior interval `(u,v]` with

```text
sum(u,v] = 0.
```

Equivalently, every nonempty linear zero-sum interval in a Graham-valid ordering must be a prefix interval `(0,v]`.

### Proof

If `1 <= u < v <= t` and `sum(u,v]=0`, then

```text
S_v - S_u = 0,
```

so

```text
S_v = S_u.
```

Both `S_u` and `S_v` are nonempty partial sums.  This contradicts Graham-validity.

If `u=0`, then `S_v=0`; this does not contradict Graham-validity because `S_0=0` is not included among the nonempty partial sums whose pairwise distinctness is required.  ∎

---

## Lemma A10.2: cyclic zero-sum intervals in a Graham-valid ordering must cross the basepoint, unless they are prefixes

Let `R` be Graham-valid.  Let `Z` be a nonempty cyclic interval whose total sum is zero.

If `Z` is represented as an ordinary linear interval `(u,v]`, then necessarily `u=0`.

Otherwise `Z` must cross the endpoint and can be written as

```text
(alpha,t] union (0,beta]
```

for some

```text
0 <= beta < alpha <= t.
```

### Proof

If the cyclic interval does not cross the endpoint, it is an ordinary linear interval `(u,v]`.  If `u>=1`, Lemma A10.1 gives a contradiction.  Therefore `u=0`.

If it is not an ordinary linear interval, then by cyclic interval geometry it crosses the endpoint and has the displayed form.  ∎

---

## Lemma A10.3: cross-collision cyclic block from A8 is necessarily basepoint-crossing

Assume `R` is Graham-valid and a cyclic-cut cross obstruction holds:

```text
S_alpha = sigma + S_beta,
```

with

```text
1 <= beta <= h < alpha <= t.
```

Then the cyclic complement

```text
Z_cyc = (alpha,t] union (0,beta]
```

has sum zero and crosses the basepoint.

### Proof

A8 already proves that the complement has sum zero:

```text
sum(alpha,t] + sum(0,beta] = 0.
```

Since `beta < alpha`, this is exactly a cyclic interval crossing the endpoint/basepoint.  ∎

---

## Lemma A10.4: proper-overlap algebra for two zero-sum linear intervals

Let two linear intervals satisfy

```text
I=(a,b],
J=(c,d],
```

with proper overlap

```text
a < c < b < d.
```

Decompose them into three consecutive pieces:

```text
A=(a,c],
B=(c,b],
C=(b,d].
```

If

```text
sum(I)=0,
sum(J)=0,
```

then

```text
sum(A)=sum(C)=-sum(B).
```

### Proof

The equations are

```text
sum(A)+sum(B)=0,
sum(B)+sum(C)=0.
```

Therefore

```text
sum(A)=-sum(B),
sum(C)=-sum(B),
```

so `sum(A)=sum(C)=-sum(B)`.  ∎

### Consequence

Proper overlap of two zero-sum intervals does not automatically create a smaller zero-sum interval.  It creates two disjoint intervals of equal sum.

This is why the final uncrossing argument cannot simply say "two zero intervals overlap, so a smaller zero interval exists."  A move or translation argument is still needed.

---

## Lemma A10.5: nested-interval algebra

Let two linear intervals satisfy

```text
I=(a,d],
J=(b,c],
```

with nesting

```text
a < b < c < d.
```

Decompose

```text
L=(a,b],
M=(b,c],
R=(c,d].
```

If

```text
sum(I)=0,
sum(J)=0,
```

then

```text
sum(L)+sum(R)=0.
```

### Proof

The equations are

```text
sum(I)=sum(L)+sum(M)+sum(R)=0,
sum(J)=sum(M)=0.
```

Subtracting gives

```text
sum(L)+sum(R)=0.
```

∎

### Consequence

Nested zero-sum intervals produce a **two-piece zero-sum complement** inside the larger interval.  This is not necessarily contiguous, but it is exactly the type of object that can become contiguous after a rotation or block move.

---

## Lemma A10.6: separated zero intervals cannot both be interior in a Graham-valid ordering

Let `R` be Graham-valid.  If two disjoint linear intervals are both zero-sum, then at least one of them is a prefix interval `(0,v]`.

### Proof

By Lemma A10.1, no interior linear interval can be zero-sum.  Therefore any zero-sum linear interval must be a prefix.  Two disjoint nonempty prefix intervals cannot both occur, but the stated weaker conclusion is enough.  ∎

---

## Application to the A8/A9 obstruction package

A minimal endpoint-avoidance counterexample produces:

1. a local zero block `Z_loc` in the swapped auxiliary ordering `R^swap`;
2. possibly a cyclic zero block `Z_cyc` in the original ordering `R` if the cyclic cut fails by cross-collision;
3. otherwise a special hit `S_alpha=2f` or `S_beta=2f-sigma`.

The key structural difference is:

```text
Z_loc lives in R^swap, not R;
Z_cyc lives in R and crosses the basepoint.
```

Therefore, a direct interval comparison between `Z_loc` and `Z_cyc` requires transporting one object into the same ordering as the other.

The adjacent swap `R -> R^swap` changes only one local pair.  Thus `Z_cyc` is usually still almost a cyclic zero block in `R^swap`, except when it crosses or touches the swapped pair `(a,b)`.

This gives the next finite case split.

---

## Target A11: transported cyclic block case split

Let `Z_cyc` be the cyclic zero block from A8 and let `R^swap` be the adjacent-swapped ordering from A9.

Analyze the position of the swapped pair `(a,b)` relative to `Z_cyc`.

### Case 1: swapped pair outside `Z_cyc`

Then `Z_cyc` remains a cyclic zero block in `R^swap`.

### Case 2: swapped pair entirely inside `Z_cyc`

Then `Z_cyc` remains a cyclic zero block in `R^swap`, but its internal order changes locally.

### Case 3: `Z_cyc` cuts between `a` and `b`

Then the transported cyclic block changes by replacing one of `a,b` with the other.  This is expected to produce a second punctured interval relation, hence a pair trap.

The desired theorem is that in each case, `Z_loc` and the transported `Z_cyc` either:

```text
1. yield a forbidden Graham collision contradiction;
2. can be uncrossed to produce an earlier first hit;
3. allow a zero-block relocation avoiding f;
4. force a short algebraic atom such as b=2a or a=2b.
```

---

## Current status

Proved here:

1. Graham-validity forbids interior zero-sum intervals;
2. cyclic zero-sum intervals must cross the basepoint unless they are prefixes;
3. cross-collision cyclic blocks are basepoint-crossing zero blocks;
4. proper-overlap and nested zero-interval algebra;
5. separated interior zero blocks are impossible in one Graham-valid ordering.

Not proved here:

1. transported cyclic block case split;
2. full two-zero-block uncrossing;
3. endpoint avoidance theorem.
