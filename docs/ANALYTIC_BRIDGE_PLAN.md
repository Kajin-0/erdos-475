# Analytic Bridge Plan

Last updated: 2026-06-04

Purpose:

```text
Define the source-theorem extraction pipeline needed to decide whether published analytic theorems reduce all remaining Erdős 475 / Graham rearrangement cases to the verified finite certificate domain.
```

Claim boundary:

```text
This document is not a proof of Erdős 475.
It is a plan for extracting an effective residue-inclusion theorem.
No external theorem is treated as proof-level coverage unless its constants are explicit or recursively computable and recorded in docs/source_theorems.yaml with effective_status: effective.
```

---

## 1. Target theorem

The missing theorem-level bridge is:

```text
Residue Inclusion Theorem:
  After applying source-certified analytic coverage rules,
  every remaining prime-field case lies inside the verified finite certificate domain.
```

The executable form is:

```text
source-certified analytic rules
+ certificates/verified_domains.json
+ reduction_residue_audit.py --prove
=> residue_not_verified = 0.
```

Until this is achieved, the repository is a finite-certificate verification package plus analytic infrastructure, not a complete proof.

---

## 2. Three possible bridge verdicts

The theorem-extraction pipeline must produce exactly one of the following.

### Verdict A: Closed bridge

```text
Published analytic theorems are effective enough.
The resulting residue is contained in the verified finite domain.
```

Required output:

```text
residue_not_verified = 0
VERDICT: residue is contained in verified finite domain
```

### Verdict B: Finite but too large

```text
Published analytic theorems are effective.
The residue is finite and explicit.
The residue extends beyond current certificates.
```

Required output:

```text
residue_not_verified > 0
analytic_residue.json emitted
certificate expansion target defined exactly
```

### Verdict C: Not currently effective

```text
Published theorems use qualitative sufficiently-large or existential constants
that are not extractable from the written proofs at current audit depth.
```

Required output:

```text
No proof-level bridge claim.
Repo remains conditional finite-completion package.
Need either deeper source extraction or new internal analytic theorem.
```

---

## 3. Three-range decomposition

Use:

```text
A subset F_p^*,
t = |A|,
B = F_p^* \ A,
|B| = p - 1 - t.
```

The analytic coverage sandwich is:

| Regime | Desired coverage | Source direction | Current ledger status |
|---|---|---|---|
| Small A | `t <= S(p)` | Bedert--Kravitz 2024 | non_effective |
| Medium A | `C_alpha <= t <= p^(1-alpha)` | Pham--Sauermann 2026 | non_effective |
| Large A | `t >= p^(1-c)` | BBKMM 2025 | non_effective |
| Very small A | `t <= 20` | Costa--Della Fiore--Fontana--Vena 2026 | effective, abstract-level |
| Verified complement | declared `|B|` finite domains | repo certificates | finite verification |

The ideal sandwich:

```text
small-set theorem covers t <= S(p)
medium theorem covers C_alpha <= t <= p^(1-alpha)
large-set theorem covers t >= p^(1-c)
```

If an explicit `c>0` exists, choose:

```text
0 < alpha < c.
```

Then:

```text
p^(1-c) <= p^(1-alpha),
```

so the medium and large regimes overlap at the top. The small/medium gap closes once:

```text
S(p) >= C_alpha.
```

The blocker is effectivity of:

```text
S(p) threshold P_small,
C_alpha,
P_alpha,
c,
P_large.
```

---

## 4. Effectivity levels

Every external theorem must receive one level.

| Level | Status | Meaning | Usable in `--prove`? |
|---:|---|---|---|
| 0 | abstract only | only abstract-level statement extracted | no |
| 1 | exact theorem statement | theorem identified but constants not tracked | no |
| 2 | dependency graph extracted | named constants and dependencies listed | no |
| 3 | effective symbolic | constants recursively defined but not evaluated | not yet |
| 4 | executable bound | script can compute required thresholds | yes |
| 5 | residue closed | audit shows residue inside finite domain | yes, final bridge |

Current target:

```text
Reach Level 2 for Pham--Sauermann first.
Then determine whether Level 3/4 is possible.
```

---

## 5. Source ledger rule

The machine-readable source of truth is:

```text
docs/source_theorems.yaml
```

Proof-level rule:

```text
Only entries with effective_status: effective may be used in --prove mode.
```

Current hard gate:

```text
scripts/reduction_residue_audit.py --prove
```

rejects:

```text
1. p-dependent rules whose source theorem is not effective;
2. manual --range rules without source_id=<effective source>;
3. manual --range rules not marked kind=finite_local with finite p-bounds.
```

This protects the repo from turning placeholder ranges into proof claims.

---

## 6. Practical extraction order

### First: Pham--Sauermann 2026

Reason:

```text
It is the central medium-range theorem.
If C_alpha and P_alpha are not extractable,
the full published-literature bridge probably cannot close effectively.
```

Deliverable:

```text
docs/theorem_extraction/pham_sauermann_2026.md
```

### Second: Bedert--Kravitz 2024

Reason:

```text
Small-set lower endpoint must overlap the Pham--Sauermann lower threshold.
```

Deliverable:

```text
docs/theorem_extraction/bedert_kravitz_2024.md
```

### Third: BBKMM 2025

Reason:

```text
Need concrete c>0 or at least recursively computable c for large-set overlap.
```

Deliverable:

```text
docs/theorem_extraction/bbkmm_2025.md
```

---

## 7. Extraction template

Each theorem extraction file must contain:

```text
1. Exact theorem statement.
2. Translation to repo notation.
3. Required constants.
4. Lemmas used in proof.
5. Constant dependency graph.
6. Effectivity status.
7. Can this produce an executable audit rule?
8. Proposed source_theorems.yaml patch if yes.
9. Precise blocker if no.
```

---

## 8. Relation to local-repair work

If published constants are not extractable or are unusably huge, the fallback is internal analytic compression:

```text
prove a new finite-residue compression theorem or local-repair theorem.
```

Candidate local-repair direction:

```text
Start from a known full sequencing of F_p^* or a nearly complete valid ordering.
Delete a small complement B.
Repair Q_p \ B using bounded local block moves.
```

Potential theorem shape:

```text
For all sufficiently large primes p and all complements B with |B| <= K,
F_p^* \ B admits a valid ordering after bounded local repairs.
```

Do not prioritize this over theorem extraction until the source-effectivity audit shows the literature bridge cannot close cleanly.

---

## 9. Immediate next actions

```text
1. Create docs/theorem_extraction/pham_sauermann_2026.md.
2. Build dependency graph for C_alpha and P_alpha.
3. Decide whether Pham--Sauermann can reach effectivity Level 3 or 4.
4. If yes, encode symbolic/executable rule in docs/source_theorems.yaml.
5. If no, record precise blocker and keep rule non_effective.
```

---

## 10. Current status

```text
Bridge plan: created.
Source ledger: exists.
--prove hard gate: implemented and hardened against ungated manual ranges.
Effectivity extraction: not complete.
Residue inclusion theorem: not proved.
```
