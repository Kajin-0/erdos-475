# Analytic bypass rotation A6: local reinsertion formulas

This note continues from `docs/analytic_obstruction_graph_a5.md`.

The goal is to analyze the bypass zero-sum relations produced by a blocked right-adjacent swap at the earliest forbidden hit.  The main outcome of this note is a rigorous local rotation formula and an exact finite obstruction criterion.  This is progress toward A6, but it is not yet a complete proof of endpoint avoidance.

## Standing setup

Let

```text
R = (r_1, ..., r_t)
```

be a Graham-valid ordering of `A subset F_p^*`.  Let

```text
S_0 = 0,
S_i = r_1 + ... + r_i.
```

Assume endpoint avoidance for `(A,f)` fails, where

```text
f != sigma(A),
```

and choose `R` so that its unique forbidden hit

```text
S_h = f
```

occurs at the smallest possible index `h` among all Graham-valid orderings.

Since `S_t = sigma(A) != f`, we have `h<t`.

Write

```text
a = r_h,
b = r_{h+1},
P = S_{h-1}.
```

Then

```text
P+a = f.
```

By the first-hit right-swap obstruction lemma, the adjacent swap of `a,b` is blocked by some index `j != h` satisfying

```text
P+b = S_j.
```

This gives two branches:

```text
j < h  backward trap,
j > h  forward trap.
```

---

# 1. Forward trap rotation

Assume

```text
j > h.
```

Let

```text
C = (c_1, ..., c_m) = (r_{h+2}, ..., r_j),
```

where `m = j-h-1 >= 0`.

The forward bypass identity from A5 is

```text
a + c_1 + ... + c_m = 0.
```

Equivalently,

```text
sigma(C) = -a.
```

The local segment of `R` from positions `h` through `j` is

```text
a, b, C.
```

The proposed bypass rotation is

```text
a, b, C   ->   C, b, a.
```

This keeps the same total block sum because

```text
a + b + sigma(C) = b = sigma(C) + b + a.
```

Therefore all partial sums before position `h` and after position `j` are unchanged.

## Lemma A6.1: forward rotation partial sums

Let

```text
Q_0 = 0,
Q_k = c_1 + ... + c_k,   1 <= k <= m.
```

Then `Q_m = -a`.

After the rotation

```text
a,b,C -> C,b,a,
```

the new partial sums inside the block are exactly

```text
P + Q_1, ..., P + Q_m, P - a + b, P + b.
```

The last value `P+b` is the old endpoint `S_j`.

### Proof

Starting from prefix value `P`, the rotated block is

```text
c_1, ..., c_m, b, a.
```

After the first `k` entries of `C`, the partial sum is `P+Q_k`.  After all of `C` and then `b`, the partial sum is

```text
P + Q_m + b = P - a + b.
```

After the final `a`, the partial sum is

```text
P - a + b + a = P+b.
```

This proves the formula.  ∎

## Lemma A6.2: forward rotation escape criterion

In the forward trap, the rotation

```text
a,b,C -> C,b,a
```

produces a Graham-valid ordering avoiding `f` if and only if the set

```text
N_+ = {P+Q_1, ..., P+Q_m, P-a+b, P+b}
```

has the following two properties:

1. its elements are pairwise distinct;
2. no element of `N_+` except the endpoint `P+b=S_j` belongs to the old partial-sum set outside the block positions `h,...,j`;
3. `f` is not in `N_+`.

Equivalently, every failure of the forward rotation is witnessed by one of the finite equations:

```text
P+Q_u = P+Q_v                      with u != v,
P+Q_u = P-a+b,
P+Q_u = P+b,
P-a+b = P+b,
P+Q_u = S_k                        with k outside {h,...,j},
P-a+b = S_k                        with k outside {h,...,j},
f in {P+Q_u, P-a+b, P+b}.
```

The equation `P-a+b = P+b` is impossible because `a != 0`.  The endpoint `P+b` is allowed because it replaces the old partial sum at position `j`.

### Proof

Only the partial sums at positions `h,...,j` are replaced.  The old partial sums outside this block remain unchanged and were pairwise distinct because `R` was Graham-valid.  Thus the rotated ordering is Graham-valid exactly when the new block-values are pairwise distinct and do not collide with unchanged outside values.  It avoids `f` exactly when none of the new block-values is `f`.

The displayed equations are precisely the negations of those conditions.  ∎

## Internal simplifications in the forward case

Because `R` is Graham-valid, the original partial sums inside `C` are pairwise distinct.  Hence the prefix sums

```text
Q_0,Q_1,...,Q_m
```

are pairwise distinct.  In particular,

```text
Q_u = Q_v  iff  u=v.
```

So the first obstruction equation `P+Q_u=P+Q_v` with `u != v` cannot occur.

Also,

```text
P+b = f
```

would imply `b=a`, because `P+a=f`; this is impossible.  Therefore the endpoint of the rotated block is not the forbidden value.

Thus a forward rotation can fail only through the reduced list:

```text
Q_u = b-a,
Q_u = b,
P+Q_u = S_k outside the old block,
P-a+b = S_k outside the old block,
Q_u = a,
-a+b = a.
```

The final equation is

```text
b = 2a.
```

This is the first concrete `large atom / pair trap` structure: a failed forward bypass rotation forces either a prefix of the bypass block to hit one of a small set of special residues

```text
b-a, b, a
```

or a translated bypass-prefix value hits the outside partial-sum set.

---

# 2. Backward trap rotation

Assume

```text
j < h.
```

Let

```text
C = (c_1, ..., c_m) = (r_{j+1}, ..., r_{h-1}),
```

where `m = h-j-1 >= 0`.

The backward bypass identity from A5 is

```text
c_1 + ... + c_m + b = 0.
```

Equivalently,

```text
sigma(C) = -b.
```

The local segment of `R` from positions `j+1` through `h+1` is

```text
C, a, b.
```

The proposed bypass rotation is

```text
C, a, b   ->   b, a, C.
```

This keeps the same total block sum because

```text
sigma(C)+a+b = a = b+a+sigma(C).
```

Therefore all partial sums before position `j+1` and after position `h+1` are unchanged.

Let

```text
P0 = S_j.
```

## Lemma A6.3: backward rotation partial sums

Let

```text
Q_0 = 0,
Q_k = c_1 + ... + c_k,   1 <= k <= m.
```

Then `Q_m = -b`.

After the rotation

```text
C,a,b -> b,a,C,
```

the new partial sums inside the block are exactly

```text
P0+b, P0+b+a, P0+b+a+Q_1, ..., P0+b+a+Q_m.
```

The last value is

```text
P0+b+a+Q_m = P0+a,
```

which is the old endpoint `S_{h+1}`.

### Proof

Starting from prefix value `P0`, the rotated block is

```text
b,a,c_1,...,c_m.
```

After `b`, the partial sum is `P0+b`.  After `b,a`, it is `P0+b+a`.  After the first `k` entries of `C`, it is `P0+b+a+Q_k`.  Since `Q_m=-b`, the final value is `P0+a`, equal to the old total endpoint of the block.  ∎

## Lemma A6.4: backward rotation escape criterion

In the backward trap, the rotation

```text
C,a,b -> b,a,C
```

produces a Graham-valid ordering avoiding `f` if and only if the set

```text
N_- = {P0+b, P0+b+a, P0+b+a+Q_1, ..., P0+b+a+Q_m}
```

has the following two properties:

1. its elements are pairwise distinct;
2. no element of `N_-` except the endpoint `P0+a=S_{h+1}` belongs to the old partial-sum set outside the block positions `j+1,...,h+1`;
3. `f` is not in `N_-`.

Every failure is witnessed by an equality among new block-values, an equality between a new block-value and an unchanged outside partial sum, or a forbidden hit equation.

### Proof

Identical to Lemma A6.2.  Only the block partial sums are replaced.  The outside partial sums were already pairwise distinct.  ∎

## Internal simplifications in the backward case

Because the old ordering `R` is Graham-valid, the internal prefix sums

```text
Q_0,Q_1,...,Q_m
```

are pairwise distinct.

The forbidden value satisfies

```text
f = S_h = P0 + sigma(C) + a = P0 - b + a.
```

The first new value is `P0+b`.  This equals `f` exactly when

```text
P0+b = P0-b+a,
```

or

```text
a = 2b.
```

The second new value is `P0+b+a`; this equals `f` exactly when

```text
b+a = -b+a,
```

or

```text
2b = 0,
```

which is impossible for odd prime `p` and nonzero `b`, but must be checked separately for `p=2`.  The problem is trivial for `p=2`.

For a later new value `P0+b+a+Q_u`, the forbidden equation is

```text
P0+b+a+Q_u = P0-b+a,
```

or

```text
Q_u = -2b.
```

Thus a backward rotation can fail by forbidden hit only through the special residues

```text
a=2b
```

or

```text
Q_u=-2b.
```

As in the forward case, all remaining failures are outside-hit equations of translated prefix sums against old partial sums.

---

# 3. Refined A6 target

The bypass reinsertion lemma can now be stated in a sharper form.

## Target A6 refined

In the endpoint-avoidance failure setup, let the first-hit right-swap obstruction produce either a forward or backward bypass relation.

Then at least one of the following must hold:

1. the corresponding bypass rotation from this note is a Graham-valid ordering avoiding `f`;
2. the failure equations force a `large atom`, meaning many bypass-prefix sums land in a small fixed set of special residues or outside partial-sum fibers;
3. the failure equations force a `pair trap`, meaning a short algebraic relation such as

```text
b = 2a,
a = 2b,
Q_u in {a,b,b-a,-2b}
```

that supports a second local move.

The next proof layer should define `large atom` and `pair trap` in terms of the explicit equations above, not as informal labels.

---

# 4. Current status

Proved in this note:

1. exact forward rotation formula;
2. exact forward escape criterion;
3. exact backward rotation formula;
4. exact backward escape criterion;
5. reduced lists of obstruction equations.

Not proved yet:

1. that one of these rotations must succeed;
2. that all failures force a contradiction;
3. the final large-atom / pair-trap dichotomy.

The main mathematical value of this note is that A6 is now a finite list of explicit field equations rather than an informal reinsertion idea.
