# Analytic theorem dependency audit A85

This note continues from A84.

A84 assembled the conditional endpoint-avoidance theorem from the obstruction-routing program A1--A83.  A85 audits the theorem-level dependency chain:

```text
endpoint avoidance -> strong nonzero-sum -> Erdős 475.
```

This note is independent of the local obstruction notation.  It restates the three theorem statements and proves the implications cleanly.

No new local proof is claimed here.

---

## 1. Notation

Let `p` be prime and let

```text
S subset F_p^*
```

be finite.  For an ordering

```text
R=(r_1,...,r_t)
```

write

```text
S_i(R)=r_1+...+r_i,       1<=i<=t,
S_0(R)=0,
sigma(S)=sum_{s in S} s.
```

All sums are in `F_p`.

---

## 2. Graham-valid ordering

An ordering `R` of `S` is Graham-valid if the nonempty partial sums

```text
S_1(R),...,S_t(R)
```

are pairwise distinct.

This is the conclusion required by Erdős Problem 475 / Graham's rearrangement problem.

---

## 3. Endpoint avoidance theorem

The single-forbidden endpoint-avoidance theorem says:

> For every finite `S subset F_p^*` and every forbidden value `f in F_p` satisfying
>
> ```text
> f != sigma(S),
> ```
>
> there exists a Graham-valid ordering `R` of `S` such that
>
> ```text
> f notin {S_1(R),...,S_t(R)}.
> ```

The condition `f != sigma(S)` is necessary because

```text
S_t(R)=sigma(S)
```

for every ordering.

A84 conditionally proves this theorem for odd primes, assuming A1--A83 are valid.

---

## 4. Strong nonzero-sum theorem

The strong nonzero-sum theorem says:

> If `sigma(S) != 0`, then there exists an ordering `R` of `S` such that
>
> ```text
> S_0(R),S_1(R),...,S_t(R)
> ```
>
> are pairwise distinct.

Equivalently:

```text
1. R is Graham-valid;
2. no nonempty partial sum equals 0.
```

---

## 5. Erdős 475 / Graham rearrangement theorem

Erdős Problem 475 asks whether every finite subset

```text
S subset F_p^*
```

has an ordering whose nonempty partial sums are pairwise distinct.

Equivalently:

> Every finite `S subset F_p^*` admits a Graham-valid ordering.

---

# 6. Endpoint avoidance implies strong nonzero-sum

## Proposition A85.1

Assume the endpoint-avoidance theorem for `F_p`.  Then the strong nonzero-sum theorem holds for `F_p`.

### Proof

Let `S subset F_p^*` satisfy

```text
sigma(S) != 0.
```

Apply endpoint avoidance with forbidden value

```text
f=0.
```

This is admissible because `0 != sigma(S)`.  Therefore there exists a Graham-valid ordering `R` of `S` such that

```text
0 notin {S_1(R),...,S_t(R)}.
```

Since `R` is Graham-valid, the nonempty partial sums are pairwise distinct.  Since none of them equals `0`, the extended list

```text
S_0(R)=0,S_1(R),...,S_t(R)
```

is pairwise distinct.

That is exactly the strong nonzero-sum theorem. ∎

---

# 7. Strong nonzero-sum implies Erdős 475

## Proposition A85.2

Assume the strong nonzero-sum theorem for all finite subsets of `F_p^*`.  Then Erdős 475 holds over `F_p`.

### Proof

Let

```text
S subset F_p^*
```

be finite.

There are two cases.

---

### Case 1: `sigma(S) != 0`

Apply the strong nonzero-sum theorem directly to `S`.

It gives an ordering `R` such that

```text
S_0(R),S_1(R),...,S_t(R)
```

are pairwise distinct.  In particular,

```text
S_1(R),...,S_t(R)
```

are pairwise distinct.  Thus `R` is Graham-valid.

---

### Case 2: `sigma(S)=0`

If `S` is empty, the result is trivial.  In the usual nonempty formulation, choose any

```text
x in S.
```

Let

```text
T=S\{x}.
```

Then

```text
sigma(T)=sigma(S)-x=-x.
```

Since `x in F_p^*`, we have

```text
-x != 0.
```

So

```text
sigma(T) != 0.
```

Apply the strong nonzero-sum theorem to `T`.  There exists an ordering

```text
t_1,...,t_m
```

of `T` such that the extended partial sums

```text
0,T_1,...,T_m
```

are pairwise distinct.

Now append `x` at the end:

```text
t_1,...,t_m,x.
```

The nonempty partial sums of this ordering of `S` are

```text
T_1,...,T_m,T_m+x.
```

But

```text
T_m+x=sigma(T)+x=-x+x=0.
```

Since the extended partial sums of `T` are pairwise distinct, none of

```text
T_1,...,T_m
```

is `0`, and they are pairwise distinct.  Therefore

```text
T_1,...,T_m,0
```

are pairwise distinct.

Thus the appended ordering is Graham-valid for `S`.

This proves Erdős 475. ∎

---

# 8. Endpoint avoidance implies Erdős 475

## Corollary A85.3

Endpoint avoidance implies Erdős 475.

### Proof

Endpoint avoidance implies the strong nonzero-sum theorem by Proposition A85.1.  The strong nonzero-sum theorem implies Erdős 475 by Proposition A85.2. ∎

---

# 9. Odd-prime version from A84

A84 conditionally proves endpoint avoidance over odd prime fields, assuming A1--A83.

Therefore:

## Corollary A85.4

Assume A1--A83 are valid.  Then Erdős 475 holds over every odd prime field `F_p`.

### Proof

By A84, endpoint avoidance holds over odd prime fields.  By Corollary A85.3, endpoint avoidance implies Erdős 475. ∎

---

# 10. What remains for `p=2`

For `p=2`,

```text
F_2^*={1}.
```

The only subsets are:

```text
empty set,
{1}.
```

Both are trivially Graham-valid:

```text
empty ordering for empty set;
(1) for {1}, with partial sum 1.
```

Thus Erdős 475 itself is trivial for `p=2`.

However, the stronger endpoint-avoidance theorem needs care in `p=2` because the condition

```text
f != sigma(S)
```

may still leave only one field value to avoid.  This is harmless for Erdős 475 but should be stated separately if endpoint avoidance is advertised for all primes.

---

# 11. Final theorem-level chain

Combining A84 and A85 gives the following conditional chain:

```text
A1--A83 local routing validity
    -> endpoint avoidance for odd primes
    -> strong nonzero-sum for odd primes
    -> Erdős 475 for odd primes.
```

Together with the trivial `p=2` case:

```text
A1--A83 local routing validity
    -> Erdős 475 for all primes.
```

This is still conditional on the local lemma audit.

---

# 12. Remaining audit items after A85

A85 closes the theorem-dependency chain at the statement level.

The remaining tasks are:

```text
1. finite / exceptional case bridge;
2. audit all local lemmas A1--A83 for hidden assumptions;
3. identify which computational scripts are advisory vs certifying;
4. prepare a clean final proof document with only the necessary lemmas.
```

---

# 13. Target A86

A86 should handle finite and exceptional cases explicitly.

Recommended contents:

```text
1. p=2 proof;
2. small p finite verification ledger summary;
3. check every use of division by 2 and odd characteristic;
4. identify whether p=3 needs any separate treatment;
5. state which computations are needed for the final theorem and which are only exploratory.
```

---

## Current status

Proved here:

1. endpoint avoidance implies strong nonzero-sum;
2. strong nonzero-sum implies Erdős 475;
3. endpoint avoidance implies Erdős 475;
4. A84 plus A85 gives conditional Erdős 475 over odd prime fields;
5. p=2 is trivial for Erdős 475.

Not proved here:

1. local lemma audit A1--A83;
2. finite/exceptional case certification;
3. final polished proof.
