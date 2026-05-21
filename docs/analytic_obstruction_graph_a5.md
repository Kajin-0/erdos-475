# Analytic obstruction graph A5: first-hit right-swap obstruction

This note continues the endpoint-avoidance proof program.

It corrects one small ambiguity from `docs/analytic_proof_notes.md`: the right-adjacent swap at a forbidden hit removes that hit, while the left-adjacent swap generally does not.  The useful avoidance repair is therefore the right-adjacent swap, or more generally a move that changes the partial sum at the forbidden-hit index itself.

## Setup

Let `p` be prime, let

```text
A subset F_p^*
```

and let

```text
f in F_p,  f != sigma(A).
```

Assume that the single-forbidden endpoint-avoidance theorem fails for `(A,f)`.

Thus every Graham-valid ordering of `A` hits `f` among its nonempty partial sums.  Since a Graham-valid ordering has pairwise distinct nonempty partial sums, each such ordering hits `f` exactly once.

Let

```text
R = (r_1, ..., r_t)
```

be a Graham-valid ordering of `A`, and let

```text
S_i = r_1 + ... + r_i,    S_0 = 0.
```

Let `h(R)` be the unique index satisfying

```text
S_{h(R)} = f.
```

Choose `R` so that `h(R)` is minimal among all Graham-valid orderings of `A`.

Write

```text
h = h(R).
```

Because `S_t = sigma(A) != f`, one has

```text
h < t.
```

Therefore the right-adjacent pair

```text
r_h, r_{h+1}
```

exists.

---

## Lemma A5.1: first-hit right-swap obstruction

With the setup above, the adjacent transposition

```text
(r_1, ..., r_{h-1}, r_h, r_{h+1}, r_{h+2}, ..., r_t)

      ->

(r_1, ..., r_{h-1}, r_{h+1}, r_h, r_{h+2}, ..., r_t)
```

is obstructed by a collision.  Equivalently, there exists an index

```text
j != h
```

such that

```text
S_{h-1} + r_{h+1} = S_j.
```

### Proof

Let

```text
P = S_{h-1},
a = r_h,
b = r_{h+1}.
```

The original forbidden hit is

```text
S_h = P + a = f.
```

After swapping the adjacent pair `a,b`, the only changed nonempty partial sum is the partial sum at index `h`, which becomes

```text
S'_h = P + b.
```

All partial sums before index `h` are unchanged.  The partial sum at index `h+1` remains

```text
P+a+b,
```

and every later partial sum is unchanged because the total contribution of the adjacent pair is still `a+b`.

Moreover,

```text
P+b != f,
```

because `P+a=f` and `a != b` since `A` is a set.

If `P+b` were not equal to any old partial sum except possibly `S_h`, then the swapped ordering would remain Graham-valid and would avoid `f`: the old unique occurrence of `f` at `S_h` has been replaced by `P+b != f`, and all other partial sums were unchanged and did not equal `f`.

This would contradict the assumption that every Graham-valid ordering hits `f`.

Therefore the swapped ordering must fail Graham-validity.  Since only `S_h` changed, the failure is exactly that the new value `P+b` equals some old partial sum `S_j` with `j != h`:

```text
S_{h-1}+r_{h+1}=S_j.
```

∎

---

## Lemma A5.2: the blocker index cannot be before the first hit

In Lemma A5.1, any blocker index `j` satisfying

```text
S_{h-1}+r_{h+1}=S_j
```

must satisfy

```text
j > h.
```

### Proof

The case `j=h` is excluded by Lemma A5.1.

If `j<h`, then `S_j` is an old partial sum before the first forbidden hit.  Since the swapped ordering changes only the partial sum at index `h`, all partial sums up to index `h-1` remain unchanged and pairwise distinct.

Now consider the swapped ordering `R'` even though it has a collision at indices `j,h`.  Its partial sums satisfy

```text
S'_h = S_j,
```

and all other values are unchanged.

This collision gives the zero-sum interval in `R'`

```text
r'_{j+1} + ... + r'_h = 0.
```

But in `R'`, the block from `j+1` to `h` consists of the original entries

```text
r_{j+1}, ..., r_{h-1}, r_{h+1}
```

because `r_h` was moved one step to the right.

Using `S_j = S_{h-1}+r_{h+1}`, we get

```text
r_{j+1}+...+r_{h-1}+r_{h+1}=0.
```

Equivalently,

```text
r_{j+1}+...+r_{h-1} = -r_{h+1}.
```

This identity by itself is not a contradiction.  Therefore the statement `j<h` cannot be ruled out from Graham-validity alone.

So the advertised lemma is **not proved** under the current hypotheses.  It becomes true only under an additional minimality or admissibility condition that rules out early zero-sum replacement intervals.

### Status

`Lemma A5.2` is a failed lemma in this generality.  It is retained here because it identifies exactly where a tempting proof breaks.

The obstruction index can be either:

```text
j < h    early blocker / backward trap
j > h    late blocker / forward trap
```

Both cases must be handled in the next proof layer.

---

## Corrected obstruction dichotomy

Lemma A5.1 is the solid result.  It yields a precise obstruction edge attached to the first forbidden hit:

```text
(h -> j),    S_{h-1}+r_{h+1}=S_j,    j != h.
```

Equivalently,

```text
r_{h+1} = S_j - S_{h-1}.
```

The index `j` defines two branches.

### Branch B-: backward trap

```text
j < h.
```

Then replacing `r_h` by `r_{h+1}` at the first-hit cut creates a collision with an earlier partial sum.  Algebraically,

```text
r_{j+1}+...+r_{h-1}+r_{h+1}=0.
```

This is a zero-sum relation that bypasses the forbidden element `r_h` and pulls in the next element `r_{h+1}`.

Expected use: first-cut pair reinsertion.  The relation says that the segment

```text
(r_{j+1}, ..., r_{h-1})
```

can be paired with `r_{h+1}` to form a zero-sum block after the adjacent swap.  A repair should move `r_h` across this block or reinsert `r_{h+1}` earlier.

### Branch B+: forward trap

```text
j > h.
```

Then the collision created by the right swap lands on a later old partial sum.  Algebraically,

```text
r_h + r_{h+2}+...+r_j = 0
```

because

```text
S_j - S_h = S_j - f,
```

and using

```text
S_j = S_{h-1}+r_{h+1},
S_h = S_{h-1}+r_h,
```

gives

```text
S_j-S_h = r_{h+1}-r_h.
```

Expanding the interval from `h+1` to `j` in the original order gives

```text
r_{h+1}+r_{h+2}+...+r_j = S_j-S_h = r_{h+1}-r_h,
```

hence

```text
r_h+r_{h+2}+...+r_j = 0.
```

This is a zero-sum relation that bypasses `r_{h+1}` and pulls in the forbidden-hit element `r_h`.

Expected use: pair trap.  The pair `(r_h,r_{h+1})` is exchange-blocked because one of them can be substituted into a zero-sum interval containing the other side.

---

## Lemma A5.3: every first-hit obstruction yields a bypass zero-sum relation

Under the endpoint-avoidance failure setup, the first-hit right-swap obstruction produces one of the following zero-sum bypass relations.

### Backward case

If the blocker index satisfies `j<h`, then

```text
r_{j+1}+...+r_{h-1}+r_{h+1}=0.
```

### Forward case

If the blocker index satisfies `j>h`, then

```text
r_h+r_{h+2}+...+r_j=0.
```

### Proof

Both identities were derived above.

In the backward case,

```text
S_j = S_{h-1}+r_{h+1}
```

gives

```text
S_{h-1}-S_j+r_{h+1}=0.
```

Since

```text
S_{h-1}-S_j = r_{j+1}+...+r_{h-1},
```

we get

```text
r_{j+1}+...+r_{h-1}+r_{h+1}=0.
```

In the forward case,

```text
S_j = S_{h-1}+r_{h+1}
```

and

```text
S_j-S_h = r_{h+1}-r_h.
```

But also

```text
S_j-S_h = r_{h+1}+r_{h+2}+...+r_j.
```

Therefore

```text
r_{h+1}+r_{h+2}+...+r_j = r_{h+1}-r_h,
```

so

```text
r_h+r_{h+2}+...+r_j=0.
```

∎

---

## Consequence: the next proof problem is a zero-sum bypass problem

The endpoint-avoidance theorem will follow if we can prove the following statement.

### Target A6: bypass reinsertion lemma

Let `R` be a Graham-valid ordering with earliest unavoidable forbidden hit at `h`, and suppose the right-swap obstruction produces a bypass zero-sum relation as in Lemma A5.3.

Then there exists a block move or reinsertion producing a new Graham-valid ordering whose forbidden hit occurs earlier than `h`, or a Graham-valid ordering avoiding `f` entirely.

Either outcome contradicts the choice of `R`:

```text
avoiding f entirely     contradicts endpoint-avoidance failure;
earlier hit position    contradicts minimality of h.
```

This is a sharper replacement for the earlier informal phrase:

```text
pair trap branch is controlled by first-cut pair reinsertion.
```

---

## Current proved progress

The following are now rigorous in this file:

1. first-hit right-swap obstruction, Lemma A5.1;
2. classification into backward and forward blocker branches;
3. bypass zero-sum identities, Lemma A5.3.

The following is explicitly **not** proved:

```text
blocker index must be late
```

The proof attempt fails because an early blocker gives a real zero-sum bypass relation, not an immediate contradiction.

The next mathematical target is A6: prove that every bypass relation allows a reinsertion escape or forces a larger atom that can be handled separately.
