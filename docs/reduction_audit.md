# Reduction Audit

This note tracks the remaining mathematical step needed to turn the certified finite complement package into a complete proof of Erdos Problem 475.

## Certified finite complement domain

The repository verifies all canonical multiplicative-scaling representatives for:

```text
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

where:

```text
B = F_p^* \ A
```

Equivalently, the original set sizes are:

```text
p = 29, |A| = 21..25
p = 31, |A| = 24..27
```

## Verified package status

The repository contains three independent checks:

```text
trace semantics: PASS
certificate verifier: TOTAL ok=198631 fail=0
canonical-scaling coverage: 100%, missing=0, extra=0
```

The trace-semantics verifier confirms that `B` is the complement/defect set and that the ordered set is `A = F_p^* \ B`.

## Remaining proof obligation

The remaining proof obligation is external to the certificate verifier:

```text
Do the known analytic reductions for Erdos Problem 475 leave exactly the certified complement cases?
```

More explicitly, we need to verify whether the finite residue after known analytic arguments is exactly:

```text
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

If yes, then this repository completes the finite check.

If no, then the missing complement cases should be listed explicitly and either certified by the same machinery or eliminated analytically.

## Known boundaries to compare against

Known results cited on the public problem page include:

```text
small set range: t <= 12
very-large set range: p - 3 <= t <= p - 1
sufficiently large primes: covered by combined analytic results
```

The certified cases lie immediately below the very-large range:

```text
p = 29: very-large range starts at |A| = 26; certified |A| = 21..25
p = 31: very-large range starts at |A| = 28; certified |A| = 24..27
```

## Next action

The next mathematical task is to audit the literature reduction and produce a short table of all remaining finite cases after the known ranges are applied.

Target outcome:

```text
remaining cases = certified cases
```

or an explicit list of additional cases to certify.
