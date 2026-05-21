# Analytic pair-difference trap A33: Q2 boundary formulas

This note continues from A32.

A32 isolated the main non-descending atom-insertion boundary case from A31:

```text
Q2 with |B|=1.
```

In that case the exposed zero block has the form

```text
A b_0
```

with

```text
sum(A)+b_0=0,
```

and the obstruction equation becomes the pair-difference trap

```text
q-b_0=Y_m.
```

This note computes the exact formulas for the natural pair moves involving `q` and `b_0`.  It does not fully eliminate the branch.

---

## Standing setup

Work in an auxiliary ordering segment

```text
X A b_0 q Y
```

where

```text
sum(A)+b_0=0,
q != 0,
b_0 != 0,
q != b_0
```

unless explicitly stated otherwise.

Write

```text
x=sum(X),
a=sum(A),
b_0=-a.
```

Let internal prefix sums be

```text
A_i,
Y_m.
```

The Q2 boundary obstruction is

```text
q-b_0=Y_m.
```

Equivalently,

```text
q+a=Y_m.
```

Since the block `A b_0` is zero-sum, the original segment has an exposed zero-block endpoint:

```text
x+a+b_0=x.
```

---

# 1. The direct adjacent swap of b_0 and q

The first natural move is

```text
X A b_0 q Y -> X A q b_0 Y.
```

This is exactly the atom insertion move from A29 with `B=(b_0)`.  It breaks the zero endpoint because `q != 0`.

## Lemma A33.1: direct pair-swap partial sums

In the original segment `X A b_0 q Y`, the displayed partial sums are

```text
x+A_i,
x,
x+q,
x+q+Y_m.
```

In the swapped segment `X A q b_0 Y`, the displayed partial sums are

```text
x+A_i,
x+a+q,
x+q,
x+q+Y_m.
```

Thus the only changed endpoint value is

```text
x  ->  x+a+q = x+q-b_0.
```

### Proof

Original order: after `A_i` the value is `x+A_i`; after `A b_0` it is `x+a+b_0=x`; after `A b_0 q` it is `x+q`; after `Y_m` it is `x+q+Y_m`.

Swapped order: after `A_i` it is `x+A_i`; after `A q` it is `x+a+q`; after `A q b_0` it is `x+a+q+b_0=x+q`; after `Y_m` it is `x+q+Y_m`. ∎

---

## Lemma A33.2: Q2 obstruction means the changed endpoint lands on an old Y-prefix endpoint

If

```text
q-b_0=Y_m,
```

then the changed endpoint in Lemma A33.1 satisfies

```text
x+a+q = x+Y_m.
```

### Proof

Since `a=-b_0`,

```text
a+q=q-b_0=Y_m.
```

Add `x`. ∎

### Interpretation

The direct pair-swap breaks the zero-block endpoint, but under Q2 its new endpoint equals the running value obtained by going through the corresponding `Y_m` prefix from `x`.

This is not automatically a collision in the swapped ordering, because the old `Y_m` family in the swapped ordering is translated by `x+q`, not by `x`.  The equation instead identifies a latent equal-sum relation:

```text
sum(A)+q = Y_m.
```

---

# 2. Collision and forbidden-hit equations for direct pair swap

## Lemma A33.3: direct pair-swap collision obstruction list

Assume the auxiliary ordering is collision-free except for the exposed zero-block endpoint being studied.  The swapped segment `X A q b_0 Y` can create a new Graham collision only if the changed value

```text
x+a+q
```

collides with one of the unchanged displayed families:

```text
x+A_i,
x+q,
x+q+Y_m.
```

Thus the possible equations are:

```text
(C1) a+q=A_i,
(C2) a=0,
(C3) a=Y_m.
```

### Proof

By Lemma A33.1, the only changed partial sum is `x+a+q`.  Pairing it with the unchanged families gives:

- `x+a+q=x+A_i`, so `a+q=A_i`;
- `x+a+q=x+q`, so `a=0`;
- `x+a+q=x+q+Y_m`, so `a=Y_m`.

∎

## Lemma A33.4: C2 is impossible and C3 implies q=0 under Q2

In the standing setup, `(C2)` is impossible because

```text
a=-b_0 != 0.
```

Under the Q2 relation `q+a=Y_m`, equation `(C3)` implies

```text
q=0,
```

which is impossible.

Therefore, under Q2, the only possible direct pair-swap collision is

```text
(C1) a+q=A_i.
```

### Proof

C2 says `a=0`, hence `b_0=0`, impossible.  C3 says `a=Y_m`; Q2 says `a+q=Y_m`; subtracting gives `q=0`, impossible. ∎

---

## Lemma A33.5: direct pair-swap forbidden-hit obstruction

Let `f` be the forbidden value.  If unchanged displayed families avoid `f`, the direct pair-swap can hit `f` only if

```text
x+a+q=f.
```

Using Q2, this is equivalent to

```text
x+Y_m=f.
```

### Proof

Only `x+a+q` changes.  Under Q2, `a+q=Y_m`. ∎

### Status

This is a forbidden landing at the latent `Y_m` prefix translated from the pre-`A` basepoint.  If this landing occurs earlier than the original first forbidden hit in the transformed order, it is eliminated by minimality; otherwise it remains a recurrence branch.

---

# 3. The remaining C1 obstruction

Under Q2, the only possible Graham collision for the direct pair-swap is

```text
a+q=A_i.
```

Using Q2 again, this becomes

```text
Y_m=A_i.
```

## Lemma A33.6: the only direct pair-swap collision is an equal-prefix relation A_i=Y_m

Under Q2 and the standing nonzero assumptions, the direct pair-swap fails Graham-validity only if

```text
A_i=Y_m
```

for some proper prefix of `A`.

### Proof

By Lemma A33.4 only C1 remains.  C1 is `a+q=A_i`; Q2 gives `a+q=Y_m`.  Hence `A_i=Y_m`. ∎

### Interpretation

The Q2 boundary branch has been reduced to an equal-prefix relation between a prefix of `A` and a prefix of `Y`.

This routes back to the equal-interval machinery from A20/A26.  It is not a new obstruction type.

---

# 4. Descent status of the equal-prefix obstruction

The equal-prefix obstruction is

```text
A_i=Y_m.
```

The original zero block was

```text
A b_0
```

with support length

```text
|A|+1.
```

The equal-prefix relation has left support length `i` and right support length `m`.

## Lemma A33.7: equal-prefix obstruction descends if i<|A| or m<|Y_m target span|

At minimum, if

```text
i<|A|,
```

then the left side of the equal-prefix relation is a strict proper prefix of `A`, so its support is smaller than the `A` side of the original zero block.

If `i=|A|`, then `A_i=a`, and `A_i=Y_m` combined with Q2 `a+q=Y_m` gives

```text
q=0,
```

impossible.

Therefore any genuine equal-prefix obstruction must have

```text
i<|A|,
```

and is a strict support descent on the left side.

### Proof

If `i=|A|`, then `A_i=a`.  Since `A_i=Y_m` and Q2 says `a+q=Y_m`, one gets `a=a+q`, hence `q=0`.  Thus `i<|A|`. ∎

### Status

The direct pair-swap obstruction descends to a smaller equal-interval problem.

---

# 5. Consequence for Q2 boundary

Combining the lemmas above:

1. If `q=b_0`, Q2 collapses to a zero-prefix/interior-zero branch by A32.
2. If `q!=b_0`, the direct pair-swap `A b_0 q -> A q b_0` breaks the zero-block endpoint.
3. Under Q2, the only possible new Graham collision is `A_i=Y_m`.
4. That collision is a smaller equal-interval problem.
5. The only possible new forbidden hit is `x+Y_m=f`, which is controlled by first-hit minimality if earlier; otherwise it is a recurrence branch.

Thus the Q2 pair-difference trap is reduced to:

```text
smaller equal-interval descent
+
forbidden-hit recurrence branch.
```

---

## Target A34

The remaining issue is the recurrence branch:

```text
x+Y_m=f
```

when it is not earlier than the original first forbidden hit.

A34 should formalize a global recurrence measure incorporating:

```text
1. first forbidden-hit index;
2. total support span of the active obstruction;
3. number of pieces in the active composite;
4. whether the obstruction is equal-interval, zero-composite, or weighted signed.
```

The goal is to show that every recurrence branch decreases this global measure even when the forbidden-hit index does not decrease.

---

## Current status

Proved here:

1. direct pair-swap formulas for Q2 boundary;
2. Q2 makes the changed endpoint equal to latent `x+Y_m`;
3. all direct pair-swap collision equations collapse except `A_i=Y_m`;
4. `A_i=Y_m` is a smaller equal-interval descent;
5. forbidden-hit recurrence is isolated as the only remaining Q2 issue.

Not proved here:

1. global recurrence descent;
2. endpoint avoidance theorem.
