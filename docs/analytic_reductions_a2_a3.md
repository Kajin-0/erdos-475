# Analytic reductions A2/A3: endpoint avoidance and strong nonzero-sum

This note records the next clean analytic reductions in the proof program for Erdős Problem 475 / Graham's rearrangement problem.

It is intentionally conservative: it proves the reductions stated below, but does **not** claim that the remaining endpoint-avoidance theorem is proved.

## Notation

Let `p` be prime and let

```text
A subset F_p^*
```

be finite.  For an ordering

```text
R = (r_1, ..., r_t)
```

write

```text
S_i(R) = r_1 + ... + r_i mod p,    1 <= i <= t,
S_0(R) = 0,
sigma(A) = sum_{a in A} a mod p.
```

A Graham-valid ordering is an ordering for which

```text
S_1(R), ..., S_t(R)
```

are pairwise distinct.  The endpoint is forced:

```text
S_t(R) = sigma(A).
```

---

## A2. External endpoint avoidance implies strong nonzero-sum

### Definition A2.1: single-forbidden endpoint-avoidance theorem

The single-forbidden endpoint-avoidance theorem is the following statement.

> For every prime `p`, every finite `A subset F_p^*`, and every `f in F_p` satisfying
>
> ```text
> f != sigma(A),
> ```
>
> there is a Graham-valid ordering `R` of `A` such that
>
> ```text
> f notin {S_1(R), ..., S_t(R)}.
> ```

The condition `f != sigma(A)` is necessary because the final partial sum is always `sigma(A)`.

### Definition A2.2: strong nonzero-sum theorem

The strong nonzero-sum theorem says:

> If `sigma(A) != 0`, then there is an ordering `R` of `A` such that
>
> ```text
> S_0(R)=0, S_1(R), ..., S_t(R)
> ```
>
> are pairwise distinct.

Equivalently, the ordering is Graham-valid and no nonempty partial sum equals `0`.

### Proposition A2

The single-forbidden endpoint-avoidance theorem implies the strong nonzero-sum theorem.

### Proof

Assume the single-forbidden endpoint-avoidance theorem.

Let `A subset F_p^*` satisfy

```text
sigma(A) != 0.
```

Apply endpoint avoidance with forbidden value

```text
f = 0.
```

This is admissible because `0 != sigma(A)`.  Therefore there is a Graham-valid ordering `R` of `A` such that

```text
0 notin {S_1(R), ..., S_t(R)}.
```

Since `R` is Graham-valid, the values

```text
S_1(R), ..., S_t(R)
```

are pairwise distinct.  Since none of them is `0`, the extended list

```text
S_0(R)=0, S_1(R), ..., S_t(R)
```

is pairwise distinct.  This is exactly the strong nonzero-sum conclusion.  ∎

### Corollary A2.3

The single-forbidden endpoint-avoidance theorem implies Erdős Problem 475.

### Proof

By Proposition A2, endpoint avoidance implies the strong nonzero-sum theorem.  By Proposition A1 in `docs/analytic_proof_notes.md`, the strong nonzero-sum theorem implies Erdős Problem 475.  ∎

---

## A3. Path-external avoidance is equivalent to single-forbidden endpoint avoidance

The old proof-program label was:

```text
sign-free avoidance is equivalent to external endpoint avoidance
```

The precise formulation recorded here is the translation-normalized version.  If the earlier phrase `sign-free avoidance` meant a stricter statement, this section should be renamed rather than overused.

### Definition A3.1: path-external avoidance

Given a start point `x in F_p`, an ordering `R` of `A` defines path vertices

```text
V_i = x + S_i(R),    0 <= i <= t.
```

The path-external avoidance theorem says:

> For every `x,z in F_p`, every finite `A subset F_p^*`, if
>
> ```text
> z != x + sigma(A),
> ```
>
> then there is an ordering `R` of `A` such that
>
> ```text
> V_1, ..., V_t
> ```
>
> are pairwise distinct and
>
> ```text
> z notin {V_1, ..., V_t}.
> ```

The condition `z != x + sigma(A)` is necessary because `V_t = x + sigma(A)` for every ordering.

This formulation does **not** require avoiding the start vertex `x` unless `z=x` is chosen.  It is a one-forbidden-vertex version of endpoint avoidance for translated partial-sum paths.

### Proposition A3

Path-external avoidance is equivalent to single-forbidden endpoint avoidance.

### Proof

#### Path-external avoidance implies single-forbidden endpoint avoidance

Take

```text
x = 0,
z = f.
```

Then

```text
V_i = S_i(R),
```

and the hypothesis `z != x + sigma(A)` becomes

```text
f != sigma(A).
```

Thus path-external avoidance gives a Graham-valid ordering avoiding `f` among the nonempty partial sums.

#### Single-forbidden endpoint avoidance implies path-external avoidance

Assume single-forbidden endpoint avoidance.

Let `x,z in F_p` and suppose

```text
z != x + sigma(A).
```

Define the normalized forbidden value

```text
f = z - x.
```

Then

```text
f != sigma(A).
```

By single-forbidden endpoint avoidance, there is a Graham-valid ordering `R` of `A` such that

```text
f notin {S_1(R), ..., S_t(R)}.
```

Adding `x` to every partial sum is a bijection of `F_p`, so

```text
x+S_1(R), ..., x+S_t(R)
```

are pairwise distinct.  Also,

```text
z notin {x+S_1(R), ..., x+S_t(R)}
```

because `z=x+S_i(R)` would imply `f=S_i(R)`.  Hence path-external avoidance holds.  ∎

---

## Combined reduction chain

The current rigorous reduction chain is:

```text
single-forbidden endpoint avoidance
    <=> path-external avoidance
    => strong nonzero-sum theorem
    => Erdős Problem 475.
```

Therefore the main analytic target can be sharpened to one theorem:

> For every finite `A subset F_p^*` and every `f != sigma(A)`, construct a Graham-valid ordering of `A` whose nonempty partial sums avoid `f`.

This theorem is stronger than Graham's original conjecture by one forbidden value.

---

## Immediate obstruction setup for the remaining theorem

Assume the endpoint-avoidance theorem fails.  Then there exist `A` and `f != sigma(A)` such that every Graham-valid ordering of `A` hits `f` exactly once.

The phrase `exactly once` follows from Graham-validity: if the nonempty partial sums are pairwise distinct, then any value is hit at most once.

Choose a Graham-valid ordering minimizing the position `i` for which

```text
S_i = f.
```

The adjacent forbidden-hit obstruction lemma from `docs/analytic_proof_notes.md` says that if `i<t`, the adjacent swap of `r_i` and `r_{i+1}` repairs the forbidden hit unless

```text
S_{i-1} + r_{i+1} = S_j
```

for some `j != i`.

Thus the next proof target is to show that a minimal forbidden-hit ordering cannot have all such adjacent repairs blocked.  This is the obstruction-dichotomy problem recorded as A5/A6.
