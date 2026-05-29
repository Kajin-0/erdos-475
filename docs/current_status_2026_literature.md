# Current 2026 literature status for Erdős 475

This note updates the project strategy after the 2026 literature changes around Graham's rearrangement conjecture.

## Problem

Let `p` be prime and let

```text
A subset F_p^*
```

with `|A| = t`.  Erdős Problem 475 / Graham's rearrangement problem asks whether there is an ordering

```text
A = {a_1, ..., a_t}
```

such that the nonempty partial sums

```text
a_1,
a_1 + a_2,
...,
a_1 + ... + a_t
```

are pairwise distinct in `F_p`.

## Current external status

As of the 2026 update on the Erdős Problems site, Problem 475 is marked:

```text
DECIDABLE: Resolved up to a finite check.
```

The page also records that the conjecture has been proved for all sufficiently large primes by combining several size-regime results.

## Size regimes recorded externally

The external page divides the sufficiently-large-prime proof into four regimes.

| Regime | Stated range | Source listed externally | Role in this repository |
|---|---|---|---|
| Small `A` | `t <= exp(c (log p)^(1/3))` for some `c > 0` | Costa--Della Fiore 2026, improving Bedert--Kravitz and Kravitz | Needs exact/effective constants before machine coverage can be certified. |
| Medium `A` | for each `0 < alpha < 1`, `1 <<_alpha t <= p^(1-alpha)` | Pham--Sauermann 2026 | Central bridge from small to power-sized sets; exact threshold dependence on `alpha` must be extracted. |
| Large `A` | `p^(1-c) <= t <= (1-o(1))p` for some small `c > 0` | Bedert--Bucić--Kravitz--Montgomery--Müyesser 2025 | Needs exact constants or an explicit threshold. |
| Very large `A` | `t >= (1-o(1))p` | Müyesser--Pokrovskiy 2025 | Needs explicit complement-size threshold. |

## Consequence for project direction

The repository should now prioritize a finite-check completion package rather than a fully independent informal proof program.

The clean proof architecture is:

```text
external literature reductions with exact effective thresholds
+ finite residual witness verification
+ coverage proof that every remaining pair (p,t) is included in the finite certificate domain
= complete certificate-style proof package
```

## Critical warning

The phrase `sufficiently large primes` is not automatically a computable finite bound unless the source papers provide effective constants and thresholds.

Therefore, this repository must not claim a full proof until the following fields are extracted from the papers:

```text
P0                      # explicit prime threshold, if available
small_c                 # constant in exp(c (log p)^(1/3))
medium_threshold(alpha) # explicit lower threshold in 1 <<_alpha t
large_c                 # exponent constant in p^(1-c)
large_upper(p)          # explicit version of (1-o(1))p
very_large_lower(p)     # explicit version of (1-o(1))p
```

If any of these are ineffective, the correct status remains:

```text
theorem known in the literature for sufficiently large p;
this repository verifies only the declared finite computational domain;
full effective finite completion still requires extracting or replacing thresholds.
```

## Relation to the previous analytic notes

The existing analytic notes remain useful as independent research scaffolding.  However, they should not be treated as the main path unless the literature route fails to produce an effective finite residue.

Recommended priority order:

```text
1. Exact literature theorem extraction.
2. Coverage interval modeling.
3. Base Graham finite witness verification.
4. Optional strengthening: endpoint avoidance.
5. Optional Lean formalization of finite certificate semantics.
6. Independent analytic proof program only after the certificate route is exhausted.
```

## Immediate action items

```text
A. Fill docs/literature_exact_thresholds.md from the source papers.
B. Run scripts/check_literature_coverage.py with provisional theorem parameters.
C. Separate base Erdős 475 verification from endpoint-avoidance strengthening.
D. Promote only the minimal witness verifier into the trusted kernel.
E. Add Lean definitions for the statement and finite certificate semantics without claiming a completed formal proof.
```
