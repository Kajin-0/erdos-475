# Trust model

This repository should distinguish sharply between four different trust layers.

```text
Layer 1. Final witness certificate
Layer 2. Certificate verifier
Layer 3. Trace/provenance verifier
Layer 4. Analytic reduction ledger
```

Only Layers 1--2 are needed for the finite certificate theorem.

---

## 1. Layer 1: final witness certificate

A minimal certificate row is:

```json
{"p":29,"B":[1,2,5],"final_order":[...]}
```

The row claims:

```text
B is a complement subset of F_p^*;
final_order orders A = F_p^* \ B;
final_order has pairwise distinct nonempty partial sums mod p.
```

This layer is data, not proof logic.

---

## 2. Layer 2: certificate verifier

The verifier must recompute everything from the certificate row:

```text
prime check;
field universe F_p^*;
B subset check;
A = F_p^* \ B;
permutation check;
partial-sum computation;
pairwise distinctness;
canonical representative check;
coverage of declared finite domain.
```

The verifier must not trust fields such as:

```text
partial_sums;
trace_status;
repair_steps;
claimed_valid;
canonical_id;
coverage_count.
```

Those may be used as diagnostics only.

---

## 3. Layer 3: trace/provenance verifier

Repair traces explain how the witness was found.  They are useful for debugging and reproducibility, but they are not required for the finite existence theorem once the final witness is checked.

Trace verification can still check:

```text
move semantics;
intermediate partial sums;
certificate consistency;
descent classifications;
strictness claims.
```

But final witness verification is the smaller trust kernel.

---

## 4. Layer 4: analytic reduction ledger

The full Erdős 475 theorem requires external analytic reductions proving that all unresolved infinite cases reduce to the finite certified domain.

The required final ledger line is:

```text
remaining residue subset verified finite certificate domain.
```

Until that line is proved, the repository should not claim a complete proof of the full theorem.

---

## 5. Verification independence

The credibility target is two independent implementations:

```text
Python verifier: reference implementation, easy to audit.
Rust verifier: independent implementation, fast deterministic checker.
```

The Rust verifier should not share core code with the Python verifier.  It should independently implement:

```text
mod-p arithmetic;
partial sums;
subset/permutation checks;
canonical scaling;
coverage enumeration;
JSONL parsing.
```

---

## 6. Hash locking

Generated proof artifacts should be hash-locked through:

```text
MANIFEST.sha256
```

The manifest should include at least:

```text
certificates/*.jsonl
certificates/*.csv
traces/*.jsonl
scripts/*.py
docs/*.md
docs/*.tex
```

The manifest itself should be generated after certificates exist:

```bash
find certificates traces scripts docs -type f \
  | sort \
  | xargs sha256sum > MANIFEST.sha256
```

---

## 7. Current claim boundary

Safe claim:

```text
machine-checkable finite certificates for declared complement domains.
```

Unsafe claim until the reduction ledger is closed:

```text
complete proof of Erdős 475.
```

Unsafe claim until witness and coverage files are generated and verified:

```text
finite theorem is fully certified.
```
