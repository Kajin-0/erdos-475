# Literature collection protocol for Erdos 475

This file is the next action plan for completing the analytic reduction audit.

The finite verification phase is complete for the currently verified domain. The remaining work is source extraction from the published literature.

## Verified finite domain

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

The analytic proof must show that all remaining cases outside standard small-set and large-set ranges reduce to this verified domain, or else explicitly list the extra residue.

## Search targets

Use these exact search queries in Google Scholar, arXiv, MathSciNet, zbMATH, Semantic Scholar, or publisher search.

```text
"Erdos Problem 475" Graham
"Erdos 475" "partial sums"
"Erdos 475" "finite field"
"Graham" "partial sums" "finite field"
"Graham's conjecture" "partial sums"
"rotational sequencing" cyclic group subset finite field
"sequenceable groups" "cyclic group" "partial sums"
"Alspach conjecture" "cyclic group" "partial sums"
"terraces" "cyclic group" "sequenceable"
"simple ordering" subset finite field partial sums
"distinct partial sums" subset finite field prime
"zero-sum-free" ordering finite field partial sums
```

## Source triage

A source is relevant only if it gives one of the following:

```text
1. exact small-set theorem, likely t <= 12;
2. exact very-large-set theorem, likely |B| <= 2;
3. exact sufficiently-large-prime theorem;
4. exact finite exceptional/residue list;
5. prior computational residue table;
6. equivalent theorem under rotational sequencing / terraces / sequenceable groups.
```

Discard sources that only discuss unrelated zero-sum subsequence problems, additive bases, or Olson constants unless they explicitly imply the ordering-with-distinct-partial-sums statement.

## Extraction template

For each source, copy the exact theorem statement into `docs/source_theorem_ledger.md` using this format:

```text
source_id:
authors:
title:
year:
publication_or_arxiv:
theorem_number:
exact_statement:
source_variables:
translation_to_this_project:
covered_p_range:
covered_t_range:
covered_B_range:
exceptions:
dependencies:
status:
confidence:
notes:
```

## Translation rules

This project uses:

```text
p = prime modulus
A subset F_p^*
t = |A|
B = F_p^* \ A
|B| = p - 1 - t
```

Common translations:

```text
large original set: t near p - 1
small complement: |B| near 0
very-large-set theorem p - 3 <= t <= p - 1: |B| <= 2
small-set theorem t <= 12: all complements with |B| >= p - 13
```

## Final audit requirement

After theorem extraction, encode the ranges in:

```text
scripts/reduction_residue_audit.py
```

The target command should produce:

```text
residue_not_verified = 0
VERDICT: residue is contained in verified finite domain
```

## Blocking facts still needed

```text
T1: exact citation and theorem for t <= 12.
T2: exact citation and theorem for |B| <= 2.
T3: exact citation and theorem eliminating all primes beyond the finite verified range, or giving a finite exceptional list.
T4: exact citation and theorem/list defining the remaining finite residue.
```

## Current recommendation

Do not generate more finite witness files until the analytic audit exposes a concrete uncovered case.

The next input needed is a PDF, arXiv link, theorem statement, or bibliographic reference for the published reduction theorem(s).
