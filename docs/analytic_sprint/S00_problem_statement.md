# S00. Problem statement and analytic target

This sprint is the AI-first analytic route for Erdős Problem 475 / Graham's rearrangement problem.

The objective is to prove or disprove the problem with minimal computation.  Scripts are used only for falsification, obstruction mining, and finite sanity checks.

## Base problem

Let `p` be prime and let

```text
A subset F_p^*
```

with `|A| = t`.  An ordering

```text
R = (r_1, ..., r_t)
```

of `A` has nonempty partial sums

```text
P_i(R) = r_1 + ... + r_i mod p,     1 <= i <= t.
```

The Graham-valid condition is:

```text
P_1(R), ..., P_t(R) are pairwise distinct.
```

Erdős 475 asks whether every finite `A subset F_p^*` admits a Graham-valid ordering.

## Strong nonzero-sum target

For the analytic attack, use the stronger but cleaner target:

```text
If S subset F_p^* and sigma(S) != 0,
then S has an ordering R such that
P_0(R)=0, P_1(R), ..., P_t(R)
are pairwise distinct.
```

Call this an `SNS ordering`.

The repository already records the append-one-atom implication:

```text
SNS theorem for all nonzero-sum subsets
=> Erdős 475 for all subsets.
```

## Zero-interval reformulation

For an ordering `R`, define extended partial sums:

```text
P_0 = 0,
P_i = r_1 + ... + r_i.
```

Then

```text
P_i = P_j with i < j
```

if and only if the contiguous block

```text
r_{i+1} + ... + r_j = 0.
```

Therefore, `R` is SNS if and only if it has no nonempty contiguous zero-sum interval.

This converts the problem into:

```text
Given S subset F_p^* with sigma(S) != 0,
find a permutation of S with no contiguous zero-sum block.
```

## Minimal-counterexample architecture

Assume a counterexample exists.  Choose a set `S` and an ordering `R` that minimizes a simple defect measure based on zero-sum intervals.

Then:

```text
1. R has at least one zero-sum interval.
2. Choose a shortest zero-sum interval Z.
3. Because sigma(S) != 0, Z is not the whole ordering.
4. There is at least one atom q outside Z adjacent to it or movable into it.
5. A local move should destroy Z.
6. If every local move fails to reduce defect, the failures should force a rigid obstruction equation.
7. The obstruction should either be repairable or impossible for a set of distinct nonzero atoms.
```

## Main sprint decision

Use `zero-sum intervals` as the primary language, not endpoint avoidance.

Endpoint avoidance remains a possible strengthening, but it is not the first analytic target.

## Deliverable for this sprint

A compact proof skeleton:

```text
Theorem. Let S subset F_p^* with sigma(S) != 0. There is an ordering of S with no nonempty contiguous zero-sum interval.

Proof.
Choose R minimizing D(R). If D(R)=0, done. Otherwise choose a shortest zero interval Z. Apply the local insertion/swap lemma. Either D decreases, contradiction, or a classified obstruction occurs. Each obstruction class is eliminated. Hence D=0.
```

The work is to make `D`, the local lemma, and the obstruction elimination rigorous.
