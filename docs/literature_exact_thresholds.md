# Literature exact-threshold extraction ledger

This file is the main audit ledger for converting the published `sufficiently large p` resolution of Erdős 475 into an effective finite certificate statement.

The purpose is not to summarize the papers loosely.  The purpose is to extract constants, thresholds, hypotheses, and variable translations with enough precision that a script can verify coverage over `(p,t)`.

## Variable dictionary

Repository variables:

```text
p  = prime modulus
A  = subset of F_p^*
t  = |A|
B  = F_p^* \ A
b  = |B| = p - 1 - t
```

A theorem covers a pair `(p,t)` if every `A subset F_p^*` with `|A| = t` is guaranteed to have a Graham-valid ordering.

## Required extraction format

Each source theorem should be recorded with this exact structure.

```text
source_id:
authors:
title:
year:
publication_or_arxiv:
theorem_number:
claim_type: base_graham | endpoint_avoidance | stronger_sequenceability | other
exact_statement:
source_variables:
translation_to_project_variables:
prime_hypothesis:
size_hypothesis_t:
size_hypothesis_b:
constants:
effective_thresholds:
exceptional_cases:
dependencies:
proof_effective: yes | no | unclear
machine_coverage_encoding:
status: TODO | extracted | source_checked | encoded | blocked
confidence: low | medium | high
notes:
```

## T1. Small-set theorem

```text
source_id: T1_small
status: TODO
claim_type: base_graham
expected_role: covers t up to exp(c (log p)^(1/3)) for sufficiently large p
```

Fields to extract:

```text
authors: Costa--Della Fiore
year: 2026
exact theorem number: TODO
explicit c: TODO
explicit P0: TODO
whether constants are effective: TODO
```

Machine-coverage target:

```text
T1_small(p,t) := p >= P0_small and t <= exp(c_small * (log p)^(1/3))
```

If the paper proves only existence of `c > 0` and `P0` without numerical values, mark `proof_effective: unclear` and do not use this theorem in finite-residue certification.

## T2. Medium-set theorem

```text
source_id: T2_medium
status: TODO
claim_type: base_graham
expected_role: covers 1 <<_alpha t <= p^(1-alpha)
```

Fields to extract:

```text
authors: Pham--Sauermann
year: 2026
exact theorem number: TODO
valid alpha range: TODO
threshold function C(alpha): TODO
explicit or ineffective threshold: TODO
```

Machine-coverage target:

```text
T2_medium(p,t; alpha, C_alpha) := p >= P0_medium(alpha)
                              and C_alpha <= t
                              and t <= floor(p^(1-alpha))
```

Because `1 <<_alpha t` is asymptotic notation, the extraction must determine whether a concrete threshold is available.

## T3. Large-set theorem

```text
source_id: T3_large
status: TODO
claim_type: base_graham
expected_role: covers p^(1-c) <= t <= (1-o(1))p
```

Fields to extract:

```text
authors: Bedert--Bucić--Kravitz--Montgomery--Müyesser
year: 2025
exact theorem number: TODO
constant c: TODO
upper boundary in t or b: TODO
explicit P0: TODO
```

Machine-coverage target candidates:

```text
T3_large(p,t) := p >= P0_large and ceil(p^(1-c_large)) <= t <= U_large(p)
```

or complement form:

```text
T3_large(p,b) := p >= P0_large and L_large(p) <= b <= floor(p - 1 - p^(1-c_large))
```

Use whichever matches the source theorem exactly.

## T4. Very-large-set theorem

```text
source_id: T4_very_large
status: TODO
claim_type: base_graham
expected_role: covers t >= (1-o(1))p
```

Fields to extract:

```text
authors: Müyesser--Pokrovskiy
year: 2025
exact theorem number: TODO
threshold in t or complement b: TODO
explicit P0: TODO
```

Machine-coverage target candidates:

```text
T4_very_large(p,t) := p >= P0_vlarge and t >= L_vlarge(p)
```

or

```text
T4_very_large(p,b) := p >= P0_vlarge and b <= B_vlarge(p)
```

## T5. Previously verified finite or small exceptional cases

```text
source_id: T5_finite_published
status: TODO
claim_type: base_graham
expected_role: identifies exact finite residue after T1--T4
```

Fields to extract:

```text
source of finite residue: TODO
exact primes left: TODO
exact t or b ranges left: TODO
whether residue is modulo scaling: TODO
whether residue matches repository certificate domain: TODO
```

Target comparison against current repository finite certificate domain:

```text
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

Previous local notes also mention broader provisional finite endpoint domains:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

Do not merge these domains until the exact certificate files and coverage requirements are aligned.

## Blocking criteria

A theorem entry is blocked from machine certification if any of the following are unresolved:

```text
1. The theorem is asymptotic and no effective constants are available.
2. The theorem applies to a different group model without a verified translation to F_p^* subsets.
3. The theorem proves a stronger/different ordering condition whose implication to Graham-validity is not written.
4. The theorem excludes residues, signs, endpoints, or exceptional cases not modeled here.
5. The theorem assumes p sufficiently large but gives no computable P0.
```

## Certification target

The completed ledger should support a machine-readable file such as:

```text
data/literature_coverage.json
```

with entries like:

```json
{
  "source_id": "T2_medium",
  "kind": "base_graham",
  "p_min": 1000003,
  "t_min_expr": "C_alpha",
  "t_max_expr": "floor(p**(1-alpha))",
  "parameters": {"alpha": 0.10, "C_alpha": 1000}
}
```

Until this ledger is completed, the project status remains:

```text
finite certificate package + literature extraction in progress
```
