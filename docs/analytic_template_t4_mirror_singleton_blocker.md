# Analytic Note: T4 Mirror Singleton Blocker

This note packages the left singleton blocker template by mirror symmetry from T3.

Claim boundary:

```text
This is a local template routing note, not a complete proof of Erdős 475.
The global obstruction-tree termination theorem remains open.
```

---

## Source template T3

T3 is the right singleton blocker:

```text
a,b,-a -> -a,b,a.
```

It was packaged in:

```text
docs/analytic_template_t3_right_singleton_blocker.md
docs/analytic_template_t3_external_routing.md
```

T3 has scalar branch:

```text
b=2a,
```

and external branches routing to:

```text
Left(a),
Left(a-b),
Right(-a-b),
Right(-a).
```

---

## T4 parent template

T4 is the left singleton blocker:

```text
-b,a,b -> b,a,-b.
```

Original relative partial sums:

```text
-b,
a-b,
a.
```

Forbidden relative value:

```text
a-b.
```

Active block total:

```text
a.
```

Candidate move:

```text
-b,a,b -> b,a,-b.
```

New relative partial sums:

```text
b,
a+b,
a.
```

The endpoint `a` is unchanged. The genuinely new values are:

```text
W_1=b,
W_2=a+b.
```

---

## Internal classification

### Forbidden hits

The new values hit the forbidden value `a-b` only if:

```text
b = a-b        -> a=2b,
a+b = a-b      -> 2b=0.
```

Since `p` is odd and `b != 0`, the second is impossible.

Thus the genuine scalar branch is:

```text
a=2b.
```

This is the mirror of the T3 scalar branch `b=2a`.

### Zero hits

```text
b=0           impossible,
a+b=0         -> a=-b.
```

If `a=-b`, then `a` duplicates the local atom `-b`, impossible because `S` is a set.

### Internal collisions

```text
b=a+b         -> a=0, impossible,
b=a           -> duplicate atom,
a+b=a         -> b=0, impossible.
```

Therefore, outside the scalar branch `a=2b`, the T4 repair is internally Graham-valid and removes the forbidden relative value.

---

## External collision normal forms

External failures can occur at the genuinely new values:

```text
W_1=b,
W_2=a+b.
```

---

## External branch at W_1=b

At `W_1=b`, the proposed split is:

```text
A=(b),
B=(a,-b).
```

### Left external collision

A left interval `K` immediately before the active block satisfies:

```text
K+(b)=0,
sum(K)=-b.
```

Old shorthand:

```text
Left(-b).
```

This is a duplicate-left interval target because `-b` is already a local atom in the T4 active block.

### Right external collision

A right interval `K` immediately after the active block satisfies:

```text
(a,-b)+K=0,
sum(K)=b-a.
```

Old shorthand:

```text
Right(b-a).
```

This is a generic right interval target unless it duplicates a local atom.

---

## External branch at W_2=a+b

At `W_2=a+b`, the proposed split is:

```text
A=(b,a),
B=(-b).
```

### Left external collision

A left interval `K` immediately before the active block satisfies:

```text
K+(b,a)=0,
sum(K)=-a-b.
```

Old shorthand:

```text
Left(-a-b).
```

This is a generic left interval target unless it duplicates a local atom.

### Right external collision

A right interval `K` immediately after the active block satisfies:

```text
(-b)+K=0,
sum(K)=b.
```

Old shorthand:

```text
Right(b).
```

This is a duplicate-right interval target because `b` is already a local atom in the T4 active block.

---

## T4 routing theorem

### Statement

For the left singleton blocker template

```text
-b,a,b -> b,a,-b,
```

every failure is one of:

```text
1. scalar branch a=2b;
2. duplicate-left interval target Left(-b);
3. duplicate-right interval target Right(b);
4. generic-left interval target Left(-a-b);
5. generic-right interval target Right(b-a);
6. impossible nonzero or duplicate-atom condition.
```

The scalar branch routes to mirror scalar absorption.

The duplicate branches route through `docs/analytic_duplicate_interval_target_theorem.md`.

The generic interval branches route through:

```text
docs/analytic_generic_interval_length_one_theorem.md
docs/analytic_generic_interval_splitting_theorem.md
```

depending on the length of the canceling interval.

---

## Mirror relation with T3

Under reversal and relabeling:

```text
a_T3 = b,
b_T3 = a,
```

T4 is the mirror of T3:

```text
-b,a,b -> b,a,-b.
```

External branches transform as:

```text
Left(a)       <-> Right(b),
Right(-a)     <-> Left(-b),
Left(a-b)     <-> Right(b-a),
Right(-a-b)   <-> Left(-a-b).
```

The scalar branch transforms as:

```text
b_T3=2a_T3  <->  a=2b.
```

Thus T4 introduces no new local obstruction type beyond those already exposed by T3.

---

## Significance

Together, T3 and T4 now cover both singleton first-blocker cases:

```text
T3: right singleton blocker
    a,b,-a -> -a,b,a.

T4: left singleton blocker
    -b,a,b -> b,a,-b.
```

Both route to:

```text
scalar absorption,
duplicate interval templates,
generic interval templates,
impossible conditions.
```

---

## Remaining local package

The remaining un-packaged local module is scalar absorption:

```text
b=2a,
a=2b mirror.
```

After scalar absorption is packaged, the first-blocker local reduction modules will be substantially organized.
