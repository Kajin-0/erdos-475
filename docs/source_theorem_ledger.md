# Source theorem ledger for Erdos 475

This ledger is for the analytic reduction audit. It records the exact published theorem statements needed to connect the verified finite domain to a complete proof.

## Current finite endpoint

The verified finite complement-domain coverage is:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

Here:

```text
A subset F_p^*
B = F_p^* \ A
|B| = p - 1 - |A|
t = |A|
```

The analytic audit is complete only if the published reductions leave no cases outside this verified finite domain.

## Critical warning from preliminary literature search

A preliminary GitHub-indexed literature lead says the conjecture is still open in full generality as of January 2026, with the intermediate regime still open. This is not yet a primary-source theorem citation, but it is strong enough to change the working assumption:

```text
Do not assume a published theorem reduces all p >= 37 to the verified finite domain.
```

Known-range leads from that preliminary source:

```text
small sets: |A| <= 12
Kravitz 2024: |A| <= log(p)/loglog(p)
Bedert-Kravitz 2024/2025: |A| <= exp(c (log p)^(1/4))
very large sets: |A| >= p^(1-c) in finite groups, for some absolute c > 0
```

These ranges do not obviously cover the full intermediate regime for all large primes.

Therefore, unless a stronger source is found, the project must be treated as attempting new mathematics beyond the published literature.

## Required theorem-entry format

For each source theorem, record:

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

The critical fields are the exact statement and the translation to `p`, `t=|A|`, and `|B|`.

## Ledger entries

### T1. Small-set coverage

```text
source_id: T1_small_set
status: source needed
claimed_role: covers t <= 12
```

Required exact statement:

```text
For which modulus class and which set sizes t does the theorem guarantee a simple ordering?
```

Current bookkeeping assumption:

```text
t <= 12
```

Translation:

```text
t = |A|
|B| = p - 1 - t
```

Preliminary lead:

```text
A GitHub-indexed candidate literature summary states that small sets |A| <= 12 have been verified via polynomial method/computation, with references collected in later papers.
```

Audit status:

```text
not source-certified yet
```

### T2. Very-large-set coverage

```text
source_id: T2_very_large_set
status: source needed
claimed_role: covers |B| <= 2, equivalently p - 3 <= t <= p - 1
```

Required exact statement:

```text
For which large-set or complement-size range is the theorem valid?
```

Current bookkeeping assumption:

```text
|B| <= 2
p - 3 <= t <= p - 1
```

Preliminary lead:

```text
A GitHub-indexed candidate literature summary states that recent finite-group work covers |A| >= |G|^(1-c), hence |A| >= p^(1-c) over F_p, for some absolute c > 0.
This is much weaker than |B| <= 2 for concrete small p but may subsume very-large sets asymptotically depending on c.
```

Audit status:

```text
not source-certified yet
```

### T3. Sufficiently-large-prime or general-prime reduction

```text
source_id: T3_large_prime_reduction
status: likely not available in current literature
claimed_role: eliminates all p >= P0, or all p outside a finite exceptional list
```

Required exact statement:

```text
What is the exact threshold P0?
Does the theorem cover all t, or only a range of t?
Does it have exceptional primes or exceptional set sizes?
```

Potential encodings if such a theorem exists:

```text
--range "p>=37,t=all,name=T3_large_prime_reduction"
```

or, if only a size range is covered:

```text
--range "p>=37,t=13..?,name=T3_large_prime_medium_range"
```

Preliminary lead:

```text
A GitHub-indexed candidate literature summary says the full prime-field conjecture is not known in general and that the intermediate regime remains open.
This suggests that no published theorem currently gives p >= 37, t=all.
```

Audit status:

```text
critical gap; probably requires new proof, not just source lookup
```

### T4. Published finite residue list

```text
source_id: T4_published_residue
status: source needed
claimed_role: states the finite cases left after analytic reductions
```

Required exact statement:

```text
Which primes and set sizes remain after the published analytic reductions?
```

Target condition:

```text
published residue subset verified finite domain
```

Verified finite domain:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

Audit status:

```text
not source-certified yet
```

## Preliminary source leads to verify

### L1. GPT-Erdos candidate solution page

```text
repository: neelsomani/gpt-erdos
path: data/solutions/475/candidate_solution.md
status: secondary/unverified, useful only as a roadmap
key claims:
  - problem is Graham's rearrangement conjecture;
  - full prime-field statement is not proved in general;
  - intermediate regime remains open;
  - small sets |A| <= 12 verified;
  - Kravitz 2024 gives |A| <= log(p)/loglog(p);
  - Bedert-Kravitz gives |A| <= exp(c(log p)^(1/4));
  - very-large finite-group result gives |A| >= |G|^(1-c).
```

### L2. Atomicium proof-candidate repository

```text
repository: Atomicium-org/graham-rearrangement-certificates
status: research draft / proof candidate, not peer-reviewed
usefulness:
  - possible ideas for a new proof architecture;
  - not a published analytic reduction theorem;
  - README explicitly says it should be read as a research draft / proof candidate with executable local certification.
```

## Audit commands

After exact theorem ranges are entered, run the residue audit script.

Baseline finite-domain sanity check:

```powershell
python scripts\reduction_residue_audit.py --max-prime 31 --cover-verified-domain
```

Expected already observed result:

```text
residue_cases = 0
residue_not_verified = 0
VERDICT: residue is contained in verified finite domain
```

A placeholder final proof audit command would look like this:

```powershell
python scripts\reduction_residue_audit.py --max-prime 31 --cover-verified-domain --range "p>=37,t=all,name=T3_large_prime_reduction"
```

Do not treat that placeholder command as a proof unless an actual theorem proves the encoded range.

## Blocking items

The proof is not complete until these are resolved:

```text
1. exact source for t <= 12 coverage;
2. exact source for |B| <= 2 coverage;
3. proof of the intermediate regime outside known small/large ranges;
4. final audit log showing no residue outside the verified finite domain.
```

## Current conclusion

Finite verification is strong and organized.

Published literature, based on the preliminary leads, probably does not already reduce the problem to the finite domain.

A complete proof likely requires a new analytic argument for the intermediate regime, not merely a literature audit.

No complete-solution claim should be made until either:

```text
1. a source theorem is found that covers the intermediate regime, or
2. the project supplies a new rigorous analytic proof for that regime.
```
