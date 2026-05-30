# Effective finite-completion theorem for Erdős 475

This document states the theorem-level architecture that separates the verified finite certificate package from the still-open analytic residue audit.

## 1. Prime-field statement

Erdős Problem 475 / Graham's rearrangement conjecture over prime fields asks:

```text
For every prime p and every subset A ⊆ F_p^*, there is an ordering
A = {a_1,...,a_t} such that the nonempty partial sums

a_1,
a_1 + a_2,
...,
a_1 + ... + a_t

are pairwise distinct modulo p.
```

Throughout this repository,

```text
B = F_p^* \ A,
t = |A|,
|B| = p - 1 - t.
```

## 2. Verified finite complement domain

The currently recorded finite complement domain is defined in:

```text
certificates/verified_domains.json
```

and summarized in:

```text
docs/THEOREM_DOMAIN_LEDGER.md
```

At the time of this file, the domain is:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

This finite domain combines descent certificates, direct witnesses, and summary/digest-backed witness checks. The trust tier of each domain is recorded in the machine-readable domain file.

## 3. Finite certificate theorem

The finite certificate theorem is:

```text
For every canonical multiplicative-scaling representative B in the verified
finite complement domain, the project records evidence for an ordering of
A = F_p^* \ B whose nonempty partial sums are pairwise distinct modulo p.
```

The strongest public form of this statement depends on artifact availability:

```text
Tier 1: committed or repository-generated artifacts checked by verifiers.
Tier 2: reproducible external artifacts with hashes and commands.
Tier 3: log-only or digest-only evidence requiring artifact hardening.
```

## 4. Known analytic coverage inputs

The analytic literature has recently advanced the prime-field case. Pham and Sauermann prove the conjecture for subsets `S ⊆ Z_p \ {0}` with `|S| ≤ p^(1-α)` and `|S|` sufficiently large with respect to `α`, for every `α ∈ (0,1)`. Their abstract states that, combined with earlier results, this gives a complete resolution for all sufficiently large primes `p`.

Reference:

```text
Huy Tuan Pham and Lisa Sauermann,
"On Graham's rearrangement conjecture",
arXiv:2602.15797,
https://arxiv.org/abs/2602.15797
```

A separate 2026 paper by Costa, Della Fiore, Fontana, and Vena states that the prime-field conjecture was recently proved for sufficiently large primes by Pham and Sauermann combined with earlier results, while the broader problem remains open for general abelian groups, even cyclic groups `Z_k`.

Reference:

```text
Simone Costa, Stefano Della Fiore, Mattia Fontana, Lluís Vena,
"Graham conjecture on small sets in abelian groups",
arXiv:2603.20961,
https://arxiv.org/abs/2603.20961
```

## 5. Residue inclusion theorem

The missing bridge is the following statement.

```text
Residue Inclusion Theorem.
After applying the published analytic results, every remaining prime-field case
not already covered by small-set or very-large-set theorems is contained in the
verified finite complement domain recorded in certificates/verified_domains.json.
```

This repository does not currently prove the residue inclusion theorem.

## 6. Conditional finite-completion theorem

The current theorem-level result should therefore be stated conditionally.

```text
Conditional finite-completion theorem.
Assume:

1. the small-set and very-large-set analytic coverage rules are valid in the
   ranges encoded in scripts/reduction_residue_audit.py;
2. any sufficiently-large-prime or medium-range analytic theorem used in the
   audit is stated with exact hypotheses and translated correctly into (p,t)
   or (p,|B|) notation;
3. the resulting analytic residue is contained in certificates/verified_domains.json;
4. the finite-domain artifacts for every residue case satisfy the required
   trust tier for the intended claim.

Then Erdős 475 over prime fields follows from the analytic coverage rules plus
the verified finite complement-domain certificate package.
```

## 7. Exact audit command pattern

The residue audit should be run with explicit theorem rules. For example, a placeholder sufficiently-large-prime rule would look like:

```bash
python scripts/reduction_residue_audit.py \
  --max-prime 31 \
  --cover-verified-domain \
  --range "p>=37,t=all,name=sufficiently_large_prime_theorem"
```

This command is only a proof audit if the encoded range is backed by an actual theorem with matching hypotheses.

The desired audit output is:

```text
residue_not_verified = 0
VERDICT: residue is contained in verified finite domain
```

## 8. What remains unsolved in this repository

The repository still needs one of the following:

```text
1. an effective literature extraction proving that the published analytic
   residue is contained in the verified finite domain; or
2. additional finite verification covering every residue case found by the
   audit; or
3. a new internal analytic proof eliminating any residue outside the verified
   finite domain.
```

Until one of these is completed, the correct claim is finite-domain verification plus a conditional finite-completion theorem, not an unconditional proof of Erdős 475.
