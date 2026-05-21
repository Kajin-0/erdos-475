# Analytic combined obstructions A8: local blocker plus cyclic cut

This note combines the local first-hit obstruction from A5 with the cyclic-cut obstruction from A7.

The result is not yet the full endpoint-avoidance theorem.  It records several unconditional consequences that any minimal endpoint-avoidance counterexample must satisfy.

## Standing setup

Let `p` be prime.  Let

```text
A subset F_p^*
```

and let

```text
f in F_p,    f != sigma(A).
```

Assume the single-forbidden endpoint-avoidance theorem fails for `(A,f)`.

Thus every Graham-valid ordering of `A` hits `f` among its nonempty partial sums.

Choose a Graham-valid ordering

```text
R = (r_1, ..., r_t)
```

for which the unique forbidden hit occurs as early as possible:

```text
S_h = f,
```

where

```text
S_0=0,
S_i=r_1+...+r_i,
sigma=S_t.
```

Since `f != sigma`, one has `h<t`.

Write

```text
a = r_h,
b = r_{h+1},
P = S_{h-1}.
```

Then

```text
P+a=f.
```

---

## 1. Local blocker relation

By Lemma A5.1, the right-adjacent swap of `a,b` is blocked.  Therefore there exists

```text
j != h
```

such that

```text
P+b = S_j.
```

Equivalently,

```text
r_{h+1}=S_j-S_{h-1}.
```

This has two branches.

### Backward branch

If `j<h`, then

```text
r_{j+1}+...+r_{h-1}+b=0.
```

### Forward branch

If `j>h`, then

```text
a+r_{h+2}+...+r_j=0.
```

These are the bypass zero-sum relations from A5.

---

## 2. Cyclic cut obstruction

Cut the ordering after the forbidden hit:

```text
Rot_h(R) = (r_{h+1}, ..., r_t, r_1, ..., r_h).
```

By A7, the rotated ordering is Graham-valid and avoids `f` unless at least one of the following occurs:

```text
(CROSS)   S_alpha = sigma + S_beta
          for some h < alpha <= t, 1 <= beta <= h;

(FIRST)   S_alpha = 2f
          for some h < alpha <= t;

(SECOND)  S_beta = 2f - sigma
          for some 1 <= beta <= h.
```

More precisely:

- `(CROSS)` is exactly the obstruction to Graham-validity of the cyclic cut.
- `(FIRST)` or `(SECOND)` is exactly the obstruction to avoiding `f`, assuming the cyclic cut is Graham-valid.

---

## Lemma A8.1: cross obstruction is a cyclic zero-sum complement

If `(CROSS)` holds, then the cyclic complement of the interval `(beta, alpha]` has sum zero:

```text
r_{alpha+1}+...+r_t+r_1+...+r_beta = 0.
```

Here empty sums are allowed.

### Proof

The cross relation is

```text
S_alpha = sigma + S_beta.
```

Therefore

```text
S_alpha-S_beta = sigma.
```

But

```text
S_alpha-S_beta = r_{beta+1}+...+r_alpha.
```

Thus the interval `(beta,alpha]` has sum `sigma`, the total sum of all elements of `A`.  Subtracting this interval from the total sum gives

```text
r_{alpha+1}+...+r_t+r_1+...+r_beta = sigma-sigma=0.
```

∎

## Interpretation

A cross-collision in the cyclic cut is therefore not arbitrary.  It gives a cyclic zero-sum block crossing the endpoint of the original linear ordering.

This should be paired with the local bypass zero-sum block from A5.  A minimal counterexample must carry at least one local zero-sum bypass and, unless the cyclic cut remains Graham-valid, one global cyclic zero-sum complement.

---

## Lemma A8.2: minimality index constraints for a valid cyclic cut

Assume `Rot_h(R)` is Graham-valid.  Since endpoint avoidance fails, it must hit `f`.  Since `R` was chosen with minimal forbidden-hit index `h`, the first `f`-hit in `Rot_h(R)` must occur at an index at least `h`.

Consequently:

### First-side constraint

There is no index `alpha` satisfying

```text
h < alpha < 2h
```

and

```text
S_alpha=2f.
```

### Second-side constraint

There is no index `beta` satisfying

```text
1 <= beta < 2h-t
```

and

```text
S_beta=2f-sigma.
```

The second constraint is void if `2h-t <= 1`.

### Proof

By A7, a first-side hit `S_alpha=2f` becomes an `f`-hit in the rotated ordering at position

```text
alpha-h.
```

If `h<alpha<2h`, then

```text
0 < alpha-h < h,
```

so the rotated ordering would be Graham-valid and would hit `f` earlier than `h`, contradicting the minimal choice of `R`.

Similarly, a second-side hit `S_beta=2f-sigma` becomes an `f`-hit in the rotated ordering at position

```text
t-h+beta.
```

If `beta < 2h-t`, then

```text
t-h+beta < h,
```

again contradicting minimality.

∎

---

## Lemma A8.3: forced alternative for a minimal endpoint-avoidance counterexample

Under the standing setup, at least one of the following alternatives holds.

### Alternative I: cyclic zero-sum complement

There exist indices

```text
1 <= beta <= h < alpha <= t
```

such that

```text
r_{alpha+1}+...+r_t+r_1+...+r_beta=0.
```

Equivalently,

```text
S_alpha=sigma+S_beta.
```

### Alternative II: late first-side special hit

There exists

```text
alpha >= 2h,
alpha <= t,
```

such that

```text
S_alpha=2f.
```

### Alternative III: late second-side special hit

There exists

```text
1 <= beta <= h
```

with

```text
beta >= 2h-t
```

such that

```text
S_beta=2f-sigma.
```

### Proof

If the cyclic cut is not Graham-valid, then A7 gives a cross relation, and Lemma A8.1 gives Alternative I.

If the cyclic cut is Graham-valid, endpoint avoidance failure implies that it hits `f`.  By A7 this hit comes from either a first-side relation `S_alpha=2f` or a second-side relation `S_beta=2f-sigma`.  By Lemma A8.2, such a hit cannot occur earlier than index `h` in the rotated ordering.  This is exactly Alternative II or Alternative III.

∎

---

## Combined obstruction package

Every minimal endpoint-avoidance counterexample therefore has both:

### Local package

At least one local bypass zero-sum relation:

```text
j<h:  r_{j+1}+...+r_{h-1}+b=0,
```

or

```text
j>h:  a+r_{h+2}+...+r_j=0.
```

### Cyclic package

At least one cyclic obstruction:

```text
I.   cyclic zero-sum complement crossing the endpoint;
II.  late S_alpha=2f hit;
III. late S_beta=2f-sigma hit.
```

This is a much narrower target than the original conjecture.

---

## Next proof target A9

The next natural theorem is:

> No Graham-valid ordering can simultaneously satisfy the local package and the cyclic package under the earliest-hit minimality hypothesis.

A plausible proof route is interval uncrossing:

1. represent the local bypass zero-sum block and the cyclic zero-sum complement as intervals on the cycle;
2. if the intervals cross, uncross them to get a shorter zero-sum bypass or an earlier forbidden hit;
3. if they are nested/disjoint, rotate or reinsert one block to avoid `f` or force a smaller first hit.

This is structurally close to the atomic/interval classification already used in the finite certificate package.

---

## Current status

Proved here:

1. cross-collision gives cyclic zero-sum complement;
2. minimality imposes index inequalities on `2f` and `2f-sigma` hits;
3. every minimal endpoint-avoidance counterexample has both a local package and a cyclic package.

Not proved here:

1. interval uncrossing contradiction;
2. complete elimination of the simultaneous packages;
3. endpoint avoidance theorem.
