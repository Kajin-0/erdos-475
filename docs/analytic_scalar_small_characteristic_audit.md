# Analytic Audit: Small-Characteristic Scalar Boundary Cases

This note audits the small-characteristic edge cases in:

```text
docs/analytic_scalar_absorption_theorem.md
docs/analytic_boundary_zero_lemma.md
```

Claim boundary:

```text
This is a finite scalar-boundary audit note.
It is not a complete proof of Erdős 475.
```

---

## Purpose

The scalar absorption theorem treats the singleton-blocker scalar branches:

```text
b=2a,
a=2b.
```

The main branch is:

```text
a,2a,-a.
```

The local proof repeatedly says that small characteristics either degenerate the atom set or force a duplicate atom.

This note makes those claims explicit.

---

## Standing hypotheses

Work over:

```text
F_p
```

with:

```text
p odd,
S subset F_p^*,
S is a set.
```

For the scalar branch:

```text
a != 0,
```

and the local triple is required to consist of distinct atoms:

```text
a,
2a,
-a.
```

---

## Audit 1: p=3 collapses the scalar triple

In characteristic 3,

```text
2a = -a.
```

Therefore the local triple

```text
a,2a,-a
```

contains the same atom twice.

This contradicts the assumption that `S` is a set.

Thus:

```text
p=3 never produces a genuine scalar absorption branch.
```

All conditions in the scalar absorption note involving:

```text
3a=0
```

are therefore terminal duplicate-atom collapses, not live proof branches.

---

## Audit 2: right-neighbor absorption has no p=5 exception

Right-neighbor absorption uses:

```text
a,2a,-a,c -> c,-a,2a,a.
```

New relative partial sums:

```text
c,
c-a,
c+a,
c+2a.
```

Pairwise collisions force:

```text
a=0,
2a=0,
3a=0.
```

Since `p` is odd and `a != 0`, only `3a=0` is a possible small-characteristic issue.

But `3a=0` means `p=3`, already excluded by Audit 1.

Therefore:

```text
right-neighbor scalar absorption is internally valid for all genuine scalar branches, including p=5.
```

Forbidden-value hits force only:

```text
c in {0,a,2a,-a},
```

which are impossible by nonzero/distinctness if `c` is a genuine right neighbor.

---

## Audit 3: left-neighbor generic absorption has only listed exceptions

Left-neighbor absorption applies to:

```text
d,a,2a,-a -> -a,d,a,2a.
```

when no right neighbor exists.

New relative partial sums:

```text
-a,
d-a,
d,
d+2a.
```

Forbidden-value hit occurs only when:

```text
d=-2a.
```

Internal collision occurs only when:

```text
d=-a,
d=-3a,
3a=0,
```

besides impossible zero conditions.

Here:

```text
d=-a
```

is duplicate-atom collapse because `-a` is already in the scalar triple.

And:

```text
3a=0
```

is the p=3 scalar-triple collapse from Audit 1.

Thus the only genuine left-neighbor exceptional values are:

```text
d=-2a,
d=-3a,
```

as stated in the scalar absorption theorem.

---

## Audit 4: exceptional case d=-2a

The exceptional block is:

```text
-2a,a,2a,-a.
```

Its total is:

```text
-2a+a+2a-a=0.
```

If this block is interior, total zero repeats the local basepoint and contradicts Graham-validity by the Boundary Zero Lemma.

If the block starts at the global beginning, the scalar absorption theorem uses:

```text
-2a,a,2a,-a -> a,2a,-a,-2a.
```

New partial sums:

```text
a,
3a,
2a,
0.
```

The forbidden value in this boundary block is:

```text
-a.
```

### Collision audit

The values:

```text
a,3a,2a,0
```

are pairwise distinct unless one of:

```text
a=0,
2a=0,
3a=0.
```

Since `p` is odd and `a != 0`, only `3a=0` is possible, which is p=3 and already excluded.

### Forbidden audit

A hit of `-a` would require:

```text
a=-a      -> 2a=0,
3a=-a     -> 4a=0,
2a=-a     -> 3a=0,
0=-a      -> a=0.
```

For odd primes and nonzero `a`, the only possible issue is `3a=0`, again p=3 collapse.

Therefore:

```text
d=-2a is resolved for every genuine scalar branch.
```

In particular, p=5 is harmless here.

---

## Audit 5: exceptional case d=-3a

The exceptional block is:

```text
-3a,a,2a,-a.
```

The scalar absorption theorem uses:

```text
-3a,a,2a,-a -> a,2a,-a,-3a.
```

New relative partial sums:

```text
a,
3a,
2a,
-a.
```

The forbidden value is:

```text
-2a.
```

### Collision audit

The values:

```text
a,3a,2a,-a
```

are pairwise distinct unless one of:

```text
a=0,
2a=0,
3a=0,
4a=0.
```

For odd prime and nonzero `a`:

```text
3a=0 -> p=3,
```

which is scalar-triple collapse.

No odd prime `p>=5` makes `2a=0` or `4a=0` for nonzero `a`.

### Forbidden audit

A hit of `-2a` would require:

```text
a=-2a     -> 3a=0,
3a=-2a    -> 5a=0,
2a=-2a    -> 4a=0,
-a=-2a    -> a=0.
```

The possible odd-prime issues are:

```text
p=3,
p=5.
```

The p=3 case is scalar-triple collapse.

The p=5 case gives:

```text
-3a = 2a.
```

Thus the left neighbor

```text
d=-3a
```

duplicates the already-present local atom:

```text
2a.
```

This contradicts `S` being a set.

Therefore:

```text
d=-3a is resolved for every genuine scalar branch.
```

The only apparent p=5 forbidden hit is impossible because the hypothesized neighbor is not distinct.

---

## Audit 6: whole-set scalar triple

If the scalar triple has no neighbors, then:

```text
S={a,2a,-a}.
```

The scalar absorption theorem uses:

```text
-a,a,2a.
```

Partial sums:

```text
-a,
0,
2a.
```

### Distinctness audit

These partial sums collide only if:

```text
-a=0      -> a=0,
2a=0,
-a=2a    -> 3a=0.
```

The only possible odd-prime issue is p=3, already excluded by scalar-triple collapse.

### Forbidden audit

The forbidden value is:

```text
a.
```

A hit would require:

```text
-a=a      -> 2a=0,
0=a       -> a=0,
2a=a      -> a=0.
```

All are impossible for odd prime and nonzero `a`.

Therefore the whole-set scalar triple repair is valid in every genuine scalar branch.

---

## Mirror branch a=2b

The mirror scalar branch:

```text
a=2b
```

is obtained by relabeling:

```text
a_{S1}=b
```

and reversing left/right.

All small-characteristic audits above transfer exactly:

```text
p=3 collapses b,2b,-b;
p=5 in the mirror d=-3b case duplicates 2b;
all other odd-prime cases are nondegenerate.
```

---

## Small-Characteristic Scalar Boundary Lemma

### Statement

In the scalar branches:

```text
b=2a,
a=2b,
```

every small-characteristic exception appearing in scalar absorption is terminal:

```text
p=3 -> duplicate atom in the scalar triple;
p=5 in the d=-3a or mirror branch -> duplicate neighbor already present in the local triple.
```

For all genuine odd-prime distinct scalar branches, the scalar absorption repairs listed in `analytic_scalar_absorption_theorem.md` are internally valid and avoid the relevant forbidden value, modulo the already-routed template-aware external collisions.

### Proof

The audits above enumerate all equalities that can cause internal collision or forbidden-value hit in the scalar absorption branches. The only odd-prime small-characteristic equations are `3a=0` and `5a=0`. The first forces p=3 and collapses `2a=-a`; the second appears only in the `d=-3a` branch and forces `d=2a`, a duplicate atom. ∎

---

## Consequence for global edge audit

This note resolves the small-characteristic scalar boundary audit listed in:

```text
docs/analytic_f6_edge_compatibility_audit.md
docs/analytic_boundary_zero_lemma.md
```

Remaining high-risk gaps after this note:

```text
1. F7 singleton-prefix endpoint audit inherited from A70.
2. Full F9 edge-by-edge measure descent proof.
```

---

## Significant status

The scalar absorption branch no longer has an un-audited p=3/p=5 exception.

All apparent small-characteristic scalar failures are duplicate-atom collapses under the standing hypotheses.
