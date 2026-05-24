# Finite certificate theorem

This document separates the finite, machine-checkable statement from the full Erdős 475 theorem.

The immediate target is not a new analytic proof.  The immediate target is a small trusted certificate kernel:

```text
canonical complement representative B
+ final witness ordering of A = F_p^* \ B
+ direct verifier
+ canonical coverage audit
```

---

## 1. Finite theorem statement

Let `p` be a verified prime.  Let

```text
F_p^* = {1,2,...,p-1}.
```

Let `B subset F_p^*` be a complement set, and define

```text
A = F_p^* \ B.
```

A witness for `B` is an ordering

```text
W=(w_1,...,w_|A|)
```

of `A` such that the nonempty partial sums

```text
s_k = w_1 + ... + w_k mod p
```

are pairwise distinct.

The finite certificate theorem is:

```text
For every canonical multiplicative-scaling representative B in the declared finite domain,
the certificate table contains a valid witness ordering W for A = F_p^* \ B.
```

This is a finite theorem.  It does not, by itself, prove Erdős 475 for all primes.

---

## 2. Certificate kernel

The minimal witness record is one JSON object per line:

```json
{
  "p": 29,
  "B": [1, 2, 5, 11],
  "final_order": [3, 4, 6, 7]
}
```

The verifier checks:

```text
1. p is prime;
2. B is a subset of F_p^*;
3. final_order is a permutation of F_p^* \ B;
4. nonempty partial sums of final_order are pairwise distinct mod p;
5. B is canonical under multiplicative scaling, if canonical coverage is requested;
6. every canonical B in the declared domain appears exactly once.
```

The final witness proves existence.  Descent traces are useful provenance, but they are not required for the finite existence certificate once the witness ordering is independently verified.

---

## 3. Declared finite domains

The expected initial domains, pending generated witness data, are:

```text
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

The actual verified domain is whatever `scripts/verify_minimal_witnesses.py` reports from the certificate file and coverage flags.

Do not claim coverage outside the verified domain.

---

## 4. Relation to full Erdős 475

The full theorem requires an analytic reduction ledger.

The intended implication is:

```text
published/independent analytic reductions
+ finite certificate theorem
= full Erdős 475 theorem
```

The required reduction statement is:

```text
Remaining analytic residue subset verified finite certificate domain.
```

Until that line is proved in `docs/REDUCTION_LEDGER.md`, this repository should claim only the finite certificate theorem, not the full theorem.

---

## 5. Verification commands

Generate a minimal witness table from trace JSONL files:

```bash
python scripts/extract_minimal_witnesses.py \
  --trace traces/p29_r3_to_r7_repair_traces_strict.jsonl \
  --trace traces/p31_r3_to_r6_repair_traces_strict.jsonl \
  --out certificates/minimal_witnesses.jsonl
```

Verify the witness table:

```bash
python scripts/verify_minimal_witnesses.py \
  certificates/minimal_witnesses.jsonl \
  --domain 29:3-7 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
```

Run the top-level verification script:

```bash
bash scripts/run_all_verification.sh
```

---

## 6. Trust boundary

Trusted kernel:

```text
mod-p arithmetic;
subset/permutation checks;
partial-sum distinctness;
canonical scaling orbit enumeration;
coverage of declared finite domain.
```

Not trusted by the finite certificate theorem:

```text
repair-trace generation logic;
heuristic search strategy;
minimal-obstruction analytic notes;
SNS repair notes;
external analytic reduction ledger until completed.
```

---

## 7. Status

```text
Finite certificate infrastructure: in progress.
Minimal witness table: must be generated.
Independent verifier: pending.
Reduction ledger: pending.
Full Erdős 475 theorem: not claimed here.
```
