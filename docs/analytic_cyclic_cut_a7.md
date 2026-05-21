# Analytic cyclic cut A7: rotating at a forbidden hit

This note adds a second global move to the endpoint-avoidance proof program: cyclic rotation of a Graham-valid ordering at the forbidden-hit position.

It is independent of the local adjacent-swap and bypass-rotation analysis in A5/A6.  Its value is that any failure of the rotated ordering is controlled by explicit equations involving the total sum `sigma(A)`.

## Setup

Let `p` be prime and let

```text
A subset F_p^*
```

with ordering

```text
R = (r_1, ..., r_t).
```

Write

```text
S_0 = 0,
S_i = r_1 + ... + r_i,    1 <= i <= t,
sigma = S_t.
```

Assume `R` is Graham-valid:

```text
S_1, ..., S_t
```

are pairwise distinct.

Let `f in F_p` satisfy

```text
f != sigma.
```

Suppose `R` hits `f` at index `h`:

```text
S_h = f.
```

Because `f != sigma = S_t`, one has `h<t`.

Define the cyclic cut after `h`:

```text
Rot_h(R) = (r_{h+1}, ..., r_t, r_1, ..., r_h).
```

Let the partial sums of the rotated ordering be denoted by

```text
T_1, ..., T_t.
```

---

## Lemma A7.1: cyclic cut partial-sum formula

For `1 <= m <= t-h`,

```text
T_m = S_{h+m} - S_h = S_{h+m} - f.
```

For `1 <= q <= h`,

```text
T_{t-h+q} = sigma - f + S_q.
```

### Proof

The first `m` terms of `Rot_h(R)` are

```text
r_{h+1}, ..., r_{h+m},
```

so their sum is `S_{h+m}-S_h = S_{h+m}-f`.

After the first `t-h` terms, the partial sum is

```text
S_t-S_h = sigma-f.
```

Adding the next `q` original terms contributes `S_q`, giving

```text
sigma-f+S_q.
```

∎

---

## Lemma A7.2: internal collisions cannot occur inside either side of the cut

The rotated partial sums cannot collide within the first side

```text
T_1, ..., T_{t-h},
```

and cannot collide within the second side

```text
T_{t-h+1}, ..., T_t.
```

Therefore every collision in the rotated ordering, if one occurs, is a cross-collision between the two sides of the cut.

### Proof

For the first side, `T_m=T_n` with `1 <= m<n <= t-h` gives

```text
S_{h+m}-f = S_{h+n}-f,
```

so `S_{h+m}=S_{h+n}`, contradicting Graham-validity of `R`.

For the second side, `T_{t-h+q}=T_{t-h+r}` with `1 <= q<r <= h` gives

```text
sigma-f+S_q = sigma-f+S_r,
```

so `S_q=S_r`, again contradicting Graham-validity.

∎

---

## Lemma A7.3: exact cross-collision criterion

The rotated ordering `Rot_h(R)` is Graham-valid if and only if there do not exist indices

```text
h < a <= t,
1 <= b <= h
```

such that

```text
S_a = sigma + S_b.
```

Equivalently, the only possible obstruction to Graham-validity of the cut rotation is an intersection

```text
{S_{h+1}, ..., S_t} ∩ (sigma + {S_1, ..., S_h}) != empty.
```

### Proof

By Lemma A7.2, any collision must be a cross-collision.  Write the first-side index as `a=h+m` and the second-side index as `b=q`.

The equality

```text
T_m = T_{t-h+q}
```

is

```text
S_a - f = sigma - f + S_b,
```

which is equivalent to

```text
S_a = sigma + S_b.
```

This proves the criterion.  ∎

---

## Lemma A7.4: exact forbidden-hit criterion after cyclic cut

The rotated ordering `Rot_h(R)` hits the same forbidden value `f` among its nonempty partial sums if and only if at least one of the following holds.

### First side

There exists `a` with

```text
h < a <= t
```

such that

```text
S_a = 2f.
```

### Second side

There exists `b` with

```text
1 <= b <= h
```

such that

```text
S_b = 2f - sigma.
```

### Proof

On the first side, using Lemma A7.1,

```text
T_m = f
```

is equivalent to

```text
S_{h+m}-f = f,
```

or

```text
S_{h+m}=2f.
```

On the second side,

```text
T_{t-h+q}=f
```

is equivalent to

```text
sigma-f+S_q = f,
```

or

```text
S_q = 2f-sigma.
```

∎

---

## Corollary A7.5: cyclic cut escape criterion

With the standing setup, the cyclic cut `Rot_h(R)` is a Graham-valid ordering avoiding `f` if and only if both conditions hold:

```text
{S_{h+1}, ..., S_t} ∩ (sigma + {S_1, ..., S_h}) = empty,
```

and

```text
2f notin {S_{h+1}, ..., S_t},
2f-sigma notin {S_1, ..., S_h}.
```

If endpoint avoidance fails, then every Graham-valid ordering `R` with forbidden hit `S_h=f` must violate at least one of these two conditions.

### Proof

Immediate from Lemmas A7.3 and A7.4.  ∎

---

## Consequence for a minimal forbidden-hit ordering

Assume endpoint avoidance fails for `(A,f)` and choose `R` so that the forbidden hit index `h` is minimal among all Graham-valid orderings.

The cyclic cut after `h` either:

1. is Graham-valid and avoids `f`, contradiction;
2. is Graham-valid but hits `f`, contradiction to avoidance failure only if it avoids; or
3. is not Graham-valid.

By Corollary A7.5, cases 2 and 3 force one of the following explicit obstructions:

```text
S_a = sigma + S_b      for some h<a<=t, 1<=b<=h,
S_a = 2f              for some h<a<=t,
S_b = 2f - sigma      for some 1<=b<=h.
```

Thus the endpoint-avoidance failure forces either:

```text
1. a sigma-translate cross-collision across the cut;
2. a first-side 2f hit;
3. a second-side (2f-sigma) hit.
```

This is a global alternative to the local right-swap obstruction from A5.

---

## Relation to the A5/A6 local obstruction program

A5/A6 analyze the adjacent swap at the first forbidden hit and produce bypass zero-sum relations.

A7 analyzes the global cyclic cut at the same hit and produces translate-hit relations.

The intended next step is to combine them:

```text
local obstruction:   S_{h-1}+r_{h+1}=S_j
cyclic obstruction:  S_a=sigma+S_b or S_a=2f or S_b=2f-sigma
```

The hope is that simultaneous local and cyclic obstructions force either a small explicit algebraic trap or a concentration/atom condition.  This should be more rigid than the local obstruction alone.

---

## Current status

Proved here:

1. exact cyclic cut partial-sum formula;
2. exact cross-collision criterion;
3. exact forbidden-hit criterion;
4. cyclic cut escape criterion.

Not proved here:

1. that the cyclic cut must succeed;
2. that combined local+cyclic obstructions are impossible;
3. the full endpoint-avoidance theorem.
