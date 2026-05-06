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

Audit status:

```text
not source-certified yet
```

### T3. Sufficiently-large-prime or general-prime reduction

```text
source_id: T3_large_prime_reduction
status: source needed
claimed_role: eliminates all p >= P0, or all p outside a finite exceptional list
```

Required exact statement:

```text
What is the exact threshold P0?
Does the theorem cover all t, or only a range of t?
Does it have exceptional primes or exceptional set sizes?
```

Potential encodings after source verification:

```text
--range "p>=37,t=all,name=T3_large_prime_reduction"
```

or, if only a size range is covered:

```text
--range "p>=37,t=13..?,name=T3_large_prime_medium_range"
```

Audit status:

```text
missing critical theorem
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

Final proof audit command will depend on the exact published large-prime theorem. Example placeholder:

```powershell
python scripts\reduction_residue_audit.py --max-prime 31 --cover-verified-domain --range "p>=37,t=all,name=T3_large_prime_reduction"
```

Do not treat that placeholder command as a proof until the source theorem is verified.

## Blocking items

The proof is not complete until these are resolved:

```text
1. exact source for t <= 12 coverage;
2. exact source for |B| <= 2 coverage;
3. exact source for all primes beyond the finite domain, likely p >= 37 or a similar threshold;
4. exact source for any published finite exceptional list;
5. final audit log showing no residue outside the verified finite domain.
```

## Current conclusion

Finite verification is strong and organized.

Analytic reduction is still the blocking step.

No complete-solution claim should be made until the source theorem ledger is filled and the final reduction audit passes.
