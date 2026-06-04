# Effectivity audit roadmap

This document records the practical plan for converting recent analytic progress on Graham's rearrangement conjecture / Erdos 475 into executable residue-audit rules.

It is a research roadmap, not a proof claim. Nothing in this file should be interpreted as closing the analytic bridge or solving Erdos 475.

## Goal

The target bridge is:

```text
published analytic theorem statements
        -> explicit or mechanically extractable constants
        -> executable coverage rules in scripts/reduction_residue_audit.py
        -> finite residue set
        -> comparison against certificates/verified_domains.json
```

The bridge is complete only if the audit produces:

```text
residue_not_verified = 0
VERDICT: residue is contained in verified finite domain
```

and every analytic rule used in the audit is marked proof-level usable.

## Current status

The source theorem ledger is:

```text
docs/source_theorems.yaml
```

The machine-readable extraction task queue is:

```text
docs/source_effectivity_targets.yaml
```

Only sources with:

```text
effective_status: "effective"
```

may be used in proof-level residue audits. Sources marked `non_effective` or `pending_extraction` are exploratory until their constants and finite exceptions are extracted.

## Priority order

### 1. Pham--Sauermann 2026: medium range

Source id:

```text
pham_sauermann_2026_large_prime
```

Target id:

```text
pham_sauermann_C_alpha_bridge
```

Needed extraction:

```text
C_alpha
P_alpha or any sufficiently-large-prime threshold
all dependencies between alpha and the proof constants
whether the explicit anticoncentration constant C = 2^24 feeds into Theorem 1.2 in a traceable way
```

Desired executable rule:

```text
C_alpha <= t <= floor(p^(1-alpha)) for p >= P_alpha
```

This is the highest-leverage target. If it remains non-effective, the full analytic-to-finite bridge cannot be closed from current literature alone.

### 2. BBKMM 2025: large original sets

Source id:

```text
bbkmm_2025_large_sets_general_groups
```

Target id:

```text
bbkmm_large_set_exponent_c
```

Needed extraction:

```text
explicit c_large > 0 in |G|^(1-c_large)
any finite threshold P_large
all absorber / regularity dependencies that affect c_large
```

Desired executable rule:

```text
t >= ceil(p^(1-c_large)) for p >= P_large
```

A very weak explicit value of `c_large` is acceptable. It only needs to be positive and compatible with choosing `alpha < c_large` in the coverage sandwich.

### 3. Kravitz 2024: effective small-set baseline

Source id:

```text
kravitz_2024_log_over_loglog_small_sets
```

Target id:

```text
kravitz_log_over_loglog_effective_baseline
```

Needed extraction:

```text
exact theorem number
endpoint convention for floor(log p / log log p)
minimum prime threshold
small-prime exceptions
rectification and integer-ordering dependencies
```

Desired executable rule:

```text
t <= floor(log(p)/log(log(p))) for p >= P_small_log
```

This is weaker than the Bedert--Kravitz exponential-quarter theorem, but it may be much easier to make explicit. Treat it as the baseline small-set effectivity target.

### 4. Bedert--Kravitz 2024: stronger small-set range

Source id:

```text
bedert_kravitz_2024_small_prime_field_sets
```

Target id:

```text
bedert_kravitz_exp_quarter_effectivity
```

Needed extraction:

```text
specific c_small > 0
large-prime threshold P_small_exp
union-bound bottlenecks
probabilistic and dissociated-set constants
```

Desired executable rule:

```text
t <= floor(exp(c_small * (log p)^0.25)) for p >= P_small_exp
```

This is asymptotically stronger than Kravitz 2024, but likely harder to make explicit.

### 5. Costa--Della Fiore 2026: one-shot LLL method

Source id:

```text
costa_dellafiore_2026_cyclic_weak_sequenceability
```

Target id:

```text
costa_dellafiore_one_shot_lll_method
```

Needed extraction:

```text
exact theorem number
constant c in exp(c(log p)^(1/3))
Lovasz Local Lemma bad-event probability estimates
dependency degree estimates
large-k or least-prime-divisor threshold
```

This source is secondary for prime fields but important for method mining and future cyclic-group generalization.

## Coverage sandwich test

Once a candidate small, medium, and large rule are extracted, run the sandwich logic.

Input shapes:

```text
Small:  t <= S(p)
Medium: C_alpha <= t <= p^(1-alpha)
Large:  t >= p^(1-c_large)
```

The bridge can work if:

```text
alpha < c_large
S(p) >= C_alpha
p >= max(P_small, P_alpha, P_large)
```

Then all sufficiently large primes are covered. The remaining residue is finite:

```text
p < P_star
```

where:

```text
P_star = max(P_small, P_alpha, P_large, threshold where S(p) >= C_alpha)
```

## Failure modes

The project should distinguish three outcomes.

### Outcome A: executable bridge closes

```text
all constants extracted
residue finite and contained in verified domain
```

This is the desired finite-completion route.

### Outcome B: executable bridge exists but residue is too large

```text
all constants extracted
residue finite but not currently verified
```

This guides future finite-certificate expansion.

### Outcome C: published proofs are non-effective for this purpose

```text
one or more critical constants remain qualitative
```

Then the repository should remain a finite-certificate and conditional-completion workspace. The next path would be internal analytic work, not more source extraction.

## Do not overclaim

Do not state that Erdos 475 is solved from this roadmap.

Do not encode any source into proof-level residue audits unless:

```text
source_effectivity_targets.yaml marks the target complete
docs/source_theorems.yaml marks the source effective
reduction_residue_audit.py has a non-placeholder rule
```

## Immediate next task

Start with:

```text
pham_sauermann_C_alpha_bridge
```

Deliverable:

```text
docs/PHAM_SAUERMANN_EFFECTIVITY_AUDIT.md
```

Required sections:

```text
1. Exact theorem statement
2. Translation to A, t, B notation
3. Constant dependency graph
4. Lemmas feeding C_alpha
5. Lemmas feeding any prime threshold
6. Whether Theorem 1.3 with C = 2^24 is sufficient to make the proof executable
7. Proposed YAML update if successful
8. Precise blocker if unsuccessful
```
