# Analytic proof notes for Erdős 475 / Graham rearrangement

This file records analytic proof progress separately from the finite certificate package.

The goal is to avoid overclaiming.  A statement is marked `PROVED` only when the proof is included here in a self-contained form.  Candidate lemmas and recalled labels from prior work are recorded as `PROGRAM` or `GAP` until they are fully written.

## Problem statement

Let `p` be prime and let

```text
A subset F_p^*
```

An ordering

```text
R = (r_1, ..., r_t)
```

has partial sums

```text
S_i = r_1 + ... + r_i mod p,  1 <= i <= t.
```

Erdős Problem 475 / Graham's rearrangement problem asks whether every finite `A subset F_p^*` admits an ordering for which

```text
S_1, ..., S_t
```

are pairwise distinct.

The finite certificate package in this repository verifies the residual complement-domain cases currently recorded in `docs/finite_verification_ledger.md`.  The analytic task is to prove the remaining infinite/general reduction without relying on finite enumeration.

## Status ledger

| ID | Statement | Status |
|---|---|---|
| F1 | finite verification through `p <= 31` in the recorded residual domain | PROVED COMPUTATIONALLY in repo |
| A1 | strong nonzero-sum ordering theorem implies Erdős 475 | PROVED below |
| A2 | external endpoint avoidance implies strong nonzero-sum | PROGRAM, needs exact final statement |
| A3 | sign-free avoidance equivalent to external endpoint avoidance | PROGRAM, needs exact final statement |
| A4 | adjacent forbidden-hit obstruction lemma | PROVED below |
| A5 | adjacent obstruction dichotomy: large atom or pair trap | PROGRAM |
| A6 | pair-trap branch controlled by first-cut pair reinsertion | PROGRAM |
| A7 | single-forbidden atom ordering | PROGRAM / partial, exact hypothesis needed |
| A8 | large-atom pure `f`-hit obstruction eliminated | PROGRAM / partial, exact hypothesis needed |

The current best route is to convert A2--A8 into a closed proof chain.  The definite analytic progress in this file is A1 and A4.

---

## A1. Strong nonzero-sum ordering implies Erdős 475

### Definition: strong nonzero-sum ordering

For `S subset F_p^*`, write

```text
sigma(S) = sum_{s in S} s mod p.
```

A strong nonzero-sum ordering theorem says:

> If `sigma(S) != 0`, then there is an ordering `s_1,...,s_m` of `S` such that the extended partial sums
>
> ```text
> T_0 = 0,
> T_i = s_1 + ... + s_i,  1 <= i <= m
> ```
>
> are pairwise distinct.

Equivalently, all nonempty partial sums are pairwise distinct and none of them is `0`.

### Proposition A1

If the strong nonzero-sum ordering theorem holds for all subsets of `F_p^*`, then Erdős Problem 475 holds for all subsets of `F_p^*`.

### Proof

Let `A subset F_p^*`.

#### Case 1: `sigma(A) != 0`

Apply the strong nonzero-sum theorem directly to `A`.  It gives an ordering whose extended partial sums

```text
0, S_1, ..., S_t
```

are pairwise distinct.  Therefore `S_1,...,S_t` are pairwise distinct, so this is a valid Graham ordering.

#### Case 2: `sigma(A) = 0`

Choose any `x in A`, and put

```text
B = A \ {x}.
```

Then

```text
sigma(B) = -x != 0.
```

By the strong nonzero-sum theorem, there is an ordering

```text
b_1, ..., b_m
```

of `B` such that the extended partial sums

```text
0, T_1, ..., T_m
```

are pairwise distinct, where

```text
T_i = b_1 + ... + b_i.
```

Now append `x` at the end:

```text
b_1, ..., b_m, x.
```

The partial sums of this ordering are

```text
T_1, ..., T_m, T_m + x.
```

But

```text
T_m + x = sigma(B) + x = -x + x = 0.
```

Since the strong nonzero-sum ordering of `B` has `T_i != 0` for every `1 <= i <= m`, the final partial sum `0` is distinct from all previous partial sums.  The `T_i` are pairwise distinct by construction.  Hence

```text
T_1, ..., T_m, 0
```

are pairwise distinct, giving a valid Graham ordering of `A`.

This proves Erdős 475 conditional on the strong nonzero-sum theorem.  ∎

---

## A4. Adjacent forbidden-hit obstruction lemma

This lemma is a local repair fact.  It is useful for an avoidance proof in which one already has a Graham-valid ordering but one partial sum hits a forbidden value `f`.

### Setup

Let

```text
R = (r_1, ..., r_t)
```

be an ordering of a set `A subset F_p^*` whose partial sums

```text
S_1, ..., S_t
```

are pairwise distinct.

Fix a forbidden value `f in F_p`, and suppose exactly one partial sum hits `f`:

```text
S_i = f.
```

Assume `i < t`.  Let

```text
a = r_i,
 b = r_{i+1},
 P = S_{i-1},
```

with the convention that `S_0 = 0`.  Thus

```text
S_i = P + a = f,
S_{i+1} = P + a + b.
```

Consider the adjacent transposition swapping `a,b`:

```text
..., a, b, ...  ->  ..., b, a, ... .
```

### Lemma A4

After swapping the adjacent pair `a,b`, all partial sums except the `i`th partial sum are unchanged, and the new `i`th partial sum is

```text
S'_i = P + b.
```

The swapped ordering is Graham-valid and avoids `f` if and only if

```text
P + b notin {S_1, ..., S_t} \ {S_i}.
```

Equivalently, the adjacent swap is obstructed exactly when

```text
P + b = S_j
```

for some `j != i`.

### Proof

Only the internal order of the adjacent entries `a,b` changes.  The partial sums before position `i` are unchanged.  The partial sum at position `i` changes from

```text
P + a
```

to

```text
P + b.
```

The partial sum at position `i+1` remains

```text
P + a + b,
```

and every later partial sum is unchanged because the total contribution of the adjacent pair is still `a+b`.

Therefore the only possible new collision or forbidden hit involves the single new value `P+b`.

Because `S_i=f=P+a`, the equality `P+b=f` would imply

```text
P+b = P+a,
```

so `a=b`, impossible since `R` is an ordering of a set with distinct elements.  Thus the new value cannot equal the forbidden value `f`.

Hence the swapped ordering is Graham-valid and avoids `f` precisely when `P+b` is not equal to any old partial sum other than the old value `S_i`, which has been removed from position `i`.  This is exactly

```text
P + b notin {S_1, ..., S_t} \ {S_i}.
```

∎

### Left-adjacent version

If `i > 1`, the analogous swap of `r_{i-1}` and `r_i` modifies only the partial sum at position `i-1`.  Writing

```text
c = r_{i-1},
 a = r_i,
 Q = S_{i-2},
```

with

```text
S_{i-1} = Q+c,
S_i = Q+c+a = f,
```

the swap

```text
..., c, a, ... -> ..., a, c, ...
```

changes only

```text
S_{i-1}
```

to

```text
Q+a.
```

The same obstruction criterion holds:

```text
Q+a notin {S_1, ..., S_t} \ {S_{i-1}}
```

is exactly the condition for preserving Graham-validity and not creating a forbidden hit.

---

## Consequence of A4: first obstruction graph

Given a Graham-valid ordering with a unique forbidden hit `S_i=f`, the immediate right repair is blocked exactly when

```text
S_{i-1} + r_{i+1} = S_j
```

for some `j != i`.

Equivalently,

```text
r_{i+1} = S_j - S_{i-1}.
```

Thus a failed adjacent repair converts into a precise difference relation between an adjacent unused replacement value and the existing partial-sum set.

This is the first rigorous form of the `adjacent forbidden-hit obstruction` idea.  The remaining proof program is to show that simultaneous obstructions on enough adjacent repairs force either:

```text
1. a large atom, or
2. a pair trap,
```

and that both branches can be escaped by reinsertion or atom-ordering arguments.

---

## Next proof targets

The next notes should make the old-chat labels precise as formal lemmas.

### Target A2: external endpoint avoidance implies strong nonzero-sum

Needed: exact statement of `external endpoint avoidance`.

A likely formal target is:

> Given `S subset F_p^*` with `sigma(S) != 0`, construct a Graham-valid ordering whose extended path from `0` to `sigma(S)` avoids a chosen external point.  With the external point chosen as the startpoint obstruction, this should produce the strong nonzero-sum ordering.

This must be sharpened.  Current status: not yet a proof.

### Target A3: sign-free avoidance equivalent to external endpoint avoidance

Needed: exact definitions of both formulations.  This likely uses translation of the partial-sum path and the fact that only differences of partial sums matter for Graham-validity.

Current status: not yet a proof.

### Target A5: adjacent obstruction dichotomy

Using Lemma A4, define the obstruction map

```text
r_{i+1} -> S_{i-1}+r_{i+1} in PartialSums.
```

The goal is to prove that if too many adjacent repairs are blocked, then the blockers concentrate into either:

```text
large atom: many blockers hit the same partial-sum value or same forbidden residue structure;
pair trap: blockers occur in paired relations that can be attacked by reinsertion.
```

Current status: program lemma.

### Target A6: pair reinsertion-or-large-atom lemma

The expected mechanism is to cut the ordering at the first trapped pair and reinsert one side.  If reinsertion fails for all cuts, the failures should force a large atom, reducing to A7/A8.

Current status: program lemma.

---

## Guardrails

Do not claim a complete analytic proof until all of A2--A8 are formalized and proved.

In particular, A1 and A4 are definite.  A2--A8 are the active analytic proof program.
