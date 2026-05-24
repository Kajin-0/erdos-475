# Analytic finite and exceptional cases A86

This note continues from A85.

A84 assembled the conditional endpoint-avoidance theorem.  A85 audited the theorem dependency chain:

```text
endpoint avoidance -> strong nonzero-sum -> Erdős 475.
```

A86 records finite and exceptional cases.  It separates analytically trivial cases from computational evidence and from cases still needing certification.

Important: this note does not certify any computation.  It states what must be certified before a final proof claim.

---

## 1. Field characteristic assumptions in the analytic proof

Several analytic notes use division by `2`, especially:

```text
A55 midpoint boundary;
A56 equal-outer weighted reduction;
A58 weighted midpoint form;
A81 endpoint-rigid atom-middle trap;
A83 full-field cyclic rigidity collapse.
```

Therefore the analytic endpoint-avoidance assembly A84 is currently stated for:

```text
p odd prime.
```

The theorem-dependency audit A85 then gives Erdős 475 for odd primes, conditional on A1--A83.

---

## 2. The case p=2

For `p=2`,

```text
F_2^* = {1}.
```

The subsets are:

```text
empty set,
{1}.
```

For Erdős 475:

```text
empty set -> empty ordering;
{1} -> ordering (1), partial sum 1.
```

Thus Erdős 475 is trivial for `p=2`.

## Lemma A86.1: Erdős 475 holds for p=2

Every subset of `F_2^*` admits a Graham-valid ordering.

### Proof

There are only the two subsets listed above.  The empty ordering has no repeated nonempty partial sums.  The ordering `(1)` has one nonempty partial sum, so it is pairwise distinct. ∎

---

## 3. Endpoint avoidance at p=2

Endpoint avoidance is stronger than Erdős 475 and should not be automatically conflated with it at `p=2`.

For `S={1}`,

```text
sigma(S)=1.
```

The admissible forbidden value is

```text
f=0.
```

The only nonempty partial sum is `1`, so it avoids `0`.  Thus endpoint avoidance also holds for `S={1}`.

For `S=empty`,

```text
sigma(S)=0.
```

The admissible forbidden value is `f=1`.  There are no nonempty partial sums, so the empty ordering avoids `1`.

## Lemma A86.2: endpoint avoidance holds for p=2

The single-forbidden endpoint-avoidance theorem holds for all subsets of `F_2^*`.

### Proof

Check the two subsets explicitly as above. ∎

---

## 4. The case p=3

For `p=3`, the analytic proof is within odd characteristic, so division by `2` is valid because

```text
2^{-1}=2 mod 3.
```

However, any lemma using coefficients such as `3q`, triple sums, or triple-reversal heuristics must avoid dividing by `3`.

In the current A-notes, division by `3` is not intended as a proof step.  A81 mentions triple relations but routes them as bounded atom relations, not by dividing by `3`.

## Audit item A86.p3

Search A1--A83 for any implicit division by `3` or argument requiring `3 != 0` beyond ordinary odd-characteristic assumptions.

Current status:

```text
No known p=3-specific analytic obstruction, but this requires audit.
```

---

## 5. Small-prime finite verification

Earlier repository notes mention finite verification through small primes, including references to verification through `p <= 31` in recorded residual domains.

However, in the current repository search performed for A86, the exact file path

```text
docs/finite_verification_ledger.md
```

was not found by name.

Therefore small-prime finite verification should currently be treated as:

```text
advisory until the ledger/certificate files are located, regenerated, or replaced by a certified script output.
```

---

## 6. Required finite-verification ledger contents

A final finite-verification ledger should contain at least:

```text
1. prime range checked;
2. exact theorem checked;
3. whether all subsets of F_p^* were checked or only residual domains;
4. script name and commit hash;
5. command used;
6. output hash or saved certificate artifact;
7. independent verifier script, if possible;
8. statement of whether the computation is required for the final proof or only advisory.
```

Recommended ledger path:

```text
docs/finite_verification_ledger.md
```

Recommended certificate directory:

```text
certificates/
```

Recommended scripts:

```text
scripts/verify_endpoint_avoidance_exhaustive.py
scripts/verify_erdos475_exhaustive.py
scripts/check_certificate.py
```

---

## 7. What computation is actually needed?

If A84's endpoint-avoidance assembly is fully audited for all odd primes, and A86.2 handles `p=2`, then no finite computation is logically needed for the final theorem.

Finite computation would still be valuable for:

```text
1. regression testing local lemmas;
2. searching for missing endpoint cases;
3. validating small-prime behavior;
4. producing confidence before public release;
5. detecting hidden assumptions in A1--A83.
```

Thus the final proof should distinguish:

```text
necessary computation
vs.
advisory computation.
```

Current status:

```text
No necessary computation identified if A1--A83 audit succeeds.
```

---

## 8. Characteristic-dependent lemma audit table

| Note | Characteristic sensitivity | Required audit |
|---|---|---|
| A55 midpoint | divides by 2 / midpoint equations | odd prime or p=2 separate |
| A56 equal outer weighted reduction | divides by 2 | odd prime or p=2 separate |
| A58 weighted midpoint form | divides by 2 | odd prime or p=2 separate |
| A81 atom-middle endpoint trap | divides by 2 in atom relations | odd prime or p=2 separate |
| A83 cyclic rigidity | uses additive group of F_p generated by nonzero element | prime field essential |
| A85 theorem dependency | all primes, except relies on endpoint avoidance input | ok |
| A86 p=2 | direct enumeration | complete |

---

## 9. Prime-field versus cyclic-group assumptions

A83 uses the fact that in `F_p`, any nonzero translation generates the full additive group.  This is true because the additive group of `F_p` has prime order.

If one generalized to non-prime cyclic groups or arbitrary finite abelian groups, A83 would need modification: a nonzero translation may generate only a proper subgroup.

For Erdős 475 as currently formulated over `F_p`, this is acceptable.

## Lemma A86.3: A83's translation-invariance step is valid over prime fields

If `d != 0` in `F_p`, then the additive subgroup generated by `d` is all of `F_p`.

### Proof

The additive group of `F_p` has prime order `p`; every nonzero element has additive order `p`. ∎

---

## 10. Empty-set conventions

The main problem usually concerns finite subsets of `F_p^*`, possibly nonempty.  Some reductions choose an element `x in S`, which requires nonempty `S`.

For the empty set:

```text
sigma(empty)=0;
there are no nonempty partial sums;
Graham-validity is vacuous.
```

Endpoint avoidance also holds for every forbidden value `f != 0`, because there are no nonempty partial sums.

## Lemma A86.4: empty set is harmless

The empty subset satisfies Erdős 475 and endpoint avoidance under the single-forbidden endpoint condition.

### Proof

The empty ordering has no nonempty partial sums. ∎

---

## 11. Final exceptional-case theorem

## Theorem A86.5: exceptional prime cases are reduced to audit only

For Erdős 475:

```text
p=2 is trivial;
p odd is covered conditionally by A84+A85, assuming A1--A83 audit succeeds.
```

For endpoint avoidance:

```text
p=2 is directly checked;
p odd is covered conditionally by A84, assuming A1--A83 audit succeeds.
```

Thus there is no currently known exceptional prime requiring a separate analytic theorem beyond the A1--A83 audit.

### Proof

Combine Lemmas A86.1, A86.2, A86.4 with A84 and A85. ∎

---

## 12. Remaining certification tasks

Before claiming a complete public proof, do the following.

### C1. Locate or regenerate finite ledger

Find or create:

```text
docs/finite_verification_ledger.md
```

If the file does not exist, do not cite it as proof.

### C2. Add exact exhaustive scripts

Add scripts that can exhaustively verify for small primes:

```text
endpoint avoidance;
strong nonzero-sum;
Erdős 475.
```

### C3. Add deterministic output artifacts

Store command outputs and hashes:

```text
certificates/p_le_31_endpoint_avoidance.json
certificates/p_le_31_erdos475.json
```

or equivalent.

### C4. Audit characteristic assumptions

Search for:

```text
/2, divide by 2, midpoint, 2^{-1}, odd, characteristic, triple, /3
```

inside A1--A83.

### C5. Independent verifier

Write a small independent checker that validates a certificate without using the same search logic as the generator.

---

## 13. Target A87

A87 should be the local lemma audit checklist.

It should identify every A-note that must be hardened, especially those containing phrases like:

```text
proof sketch;
routes to;
expected;
should;
modulo;
not proved here;
status;
partial;
```

The goal is to separate:

```text
fully proved lemmas
from
programmatic routing claims requiring hard proof.
```

This is essential before any public proof claim.

---

## Current status after A86

Exceptional cases:

```text
p=2 handled directly;
p=3 included in odd-prime proof but needs audit for accidental division by 3;
small-prime computation advisory unless certified ledger is restored/generated.
```

Remaining before complete proof claim:

```text
1. local lemma audit A1--A83;
2. finite/certification ledger cleanup;
3. final polished proof extraction.
```
