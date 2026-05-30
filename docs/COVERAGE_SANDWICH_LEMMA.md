# Coverage sandwich lemma for the prime-field theorem

This document records the main analytic-combinatorial bridge suggested by the current literature.  It does not prove the source theorems.  It formalizes how the known-style ranges would combine to reduce Erdős 475 to an explicit finite residue once effective constants are extracted.

## 1. Problem notation

Let `p` be prime and let

```text
A subset F_p^*,
t = |A|,
B = F_p^* \ A,
|B| = p - 1 - t.
```

Erdős 475 / Graham's rearrangement conjecture asks for an ordering of `A` whose nonempty partial sums are pairwise distinct modulo `p`.

## 2. Three analytic coverage inputs

The coverage-sandwich architecture uses three kinds of inputs.

### Input S: small-set coverage

There is a function `S(p)` such that the theorem is known for

```text
1 <= t <= S(p).
```

Examples of possible source-backed choices include:

```text
S(p) = 12
```

for legacy finite/computational small-set coverage, or a stronger published bound such as

```text
S(p) = exp((log p)^(1/4))
```

when the exact hypotheses and constants are extracted from Bedert--Kravitz.

### Input M: medium-set coverage

For every `alpha in (0,1)`, there are constants

```text
N_alpha,
P_alpha
```

such that for all primes `p >= P_alpha`, the theorem is known for

```text
N_alpha <= t <= p^(1 - alpha).
```

This is the range suggested by the Pham--Sauermann sufficiently-large-prime theorem.  The repository must still extract exact effective constants before this becomes a usable audit rule.

### Input L: large-set coverage

There are constants

```text
c > 0,
P_L
```

such that for all primes `p >= P_L`, the theorem is known for

```text
t >= p^(1 - c).
```

This is the form suggested by the very-large-set finite-group result.  The repository must still extract the exact constant status and dependencies before this becomes a usable audit rule.

## 3. Coverage sandwich lemma

### Lemma

Assume Inputs S, M, and L.  Suppose there exists a choice of

```text
alpha in (0,c)
```

such that for all primes `p >= P_S`,

```text
S(p) >= N_alpha.
```

Then Erdős 475 holds for every prime

```text
p >= P_* = max(P_S, P_alpha, P_L).
```

### Proof

Fix a prime `p >= P_*` and a subset `A subset F_p^*` with `t = |A|`.

There are three cases.

#### Case 1: small set

If

```text
t <= S(p),
```

then Input S applies.

#### Case 2: not small and not large

Assume

```text
t > S(p)
```

and

```text
t < p^(1 - c).
```

Since `S(p) >= N_alpha`, we have

```text
t > S(p) >= N_alpha,
```

so

```text
t >= N_alpha
```

because `t` is an integer.

Also, because `alpha < c`,

```text
1 - alpha > 1 - c,
```

and therefore

```text
p^(1 - c) <= p^(1 - alpha).
```

Since `t < p^(1 - c)`, it follows that

```text
t <= p^(1 - alpha).
```

Thus

```text
N_alpha <= t <= p^(1 - alpha),
```

so Input M applies.

#### Case 3: large set

If

```text
t >= p^(1 - c),
```

then Input L applies.

These three cases cover every possible `t`.  Hence the theorem holds for all primes `p >= P_*`. ∎

## 4. Consequence for finite completion

Once effective constants are extracted, the only remaining cases are primes

```text
p < P_*.
```

The finite residue audit should then enumerate all `(p,t)` with `p < P_*`, remove all source-backed covered ranges, translate surviving cases into complement sizes

```text
|B| = p - 1 - t,
```

and compare them against

```text
certificates/verified_domains.json.
```

The full prime-field theorem follows if the audit reports:

```text
residue_not_verified = 0
VERDICT: residue is contained in verified finite domain
```

and the finite artifacts meet the required trust tier.

## 5. Current blocker

The current blocker is not the abstract interval logic above.  The blocker is extracting source-backed effective data:

```text
1. exact S(p) and finite exceptions for small-set coverage;
2. exact N_alpha and P_alpha status for Pham--Sauermann;
3. exact c and P_L status for large-set coverage;
4. whether any of these constants are effective enough to produce a finite P_*;
5. if not effective, whether the literature still gives only a non-computable sufficiently-large threshold.
```

Until those values are extracted, the coverage sandwich is a conditional theorem architecture, not a full proof.
