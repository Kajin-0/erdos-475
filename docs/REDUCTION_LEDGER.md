# Reduction ledger

This ledger is the bridge between the finite certificate theorem and the full Erdős 475 theorem.

The finite certificate theorem verifies only declared finite complement domains.  The full theorem requires external analytic reductions showing that every remaining case lies inside those finite domains.

---

## 1. Required final statement

The ledger is complete only when it proves:

```text
remaining analytic residue subset verified finite certificate domain.
```

Until then, the repository must not claim a complete proof of Erdős 475.

---

## 2. Ledger schema

Each reduction entry should specify:

| Field | Meaning |
|---|---|
| Theorem name | Published or internally proved reduction theorem |
| Source | Citation or repo proof file |
| Original statement | Exact mathematical statement |
| Hypotheses | Prime range, set-size range, exclusions |
| Covered p range | Which primes are covered |
| Covered A range | Which subset sizes `|A|` are covered |
| Complement translation | Corresponding `|B|=p-1-|A|` range |
| Remaining residue | Cases not covered after applying this theorem |
| Verification status | `proved`, `cited`, `TBD`, or `blocked` |

---

## 3. Current finite certificate domains

Initial intended finite domains:

```text
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

These are not considered verified until `certificates/minimal_witnesses.jsonl` exists and passes:

```bash
python scripts/verify_minimal_witnesses.py \
  certificates/minimal_witnesses.jsonl \
  --domain 29:3-7 \
  --domain 31:3-6 \
  --require-canonical \
  --require-coverage
```

---

## 4. Reduction table

| Theorem | Source | Original statement | Hypotheses | Covered p | Covered `|A|` | Complement `|B|` | Remaining residue | Status |
|---|---|---|---|---|---|---|---|---|
| Small-set theorem | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Very-large-set theorem | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Prime-range reduction | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Finite residue theorem | this repo | finite canonical complements | declared finite domain | 29,31 initially | translated from `B` | `3..7`, `3..6` initially | TBD | pending certificates |

---

## 5. Completion checklist

```text
[ ] Identify every external theorem needed.
[ ] Record exact statements and hypotheses.
[ ] Translate every set-size condition into complement-size language.
[ ] Compute the remaining residue exactly.
[ ] Compare residue against verified certificate coverage.
[ ] Add citations or self-contained proofs.
[ ] State final inclusion: residue subset verified finite domain.
```

---

## 6. Current status

```text
Reduction ledger: incomplete.
Finite certificate domain: pending generated witnesses and verification.
Full Erdős 475 theorem: not claimed.
```
