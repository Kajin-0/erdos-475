# Pham--Sauermann 2026 Effectivity Audit

Last updated: 2026-06-04

Source:

```text
Huy Tuan Pham; Lisa Sauermann.
On Graham's rearrangement conjecture.
arXiv:2602.15797.
```

Claim boundary:

```text
This file does not prove Erdős 475.
This file does not certify Pham--Sauermann as proof-mode effective.
It is an extraction worksheet for determining whether Theorem 1.2 can become an executable residue-audit rule.
```

Current verdict:

```text
Effectivity level: 1/2.
Exact theorem role identified; dependency graph not yet extracted from the proof body.
Not proof-mode usable.
```

Ledger entry:

```text
docs/source_theorems.yaml
source_id: pham_sauermann_2026_large_prime
effective_status: non_effective
```

---

## 1. Exact theorem role

The relevant statement is recorded in the source ledger as:

```text
For any 0 < alpha < 1, there exists a constant C_alpha > 0 such that:
Let p be a prime and let S subset Z_p \ {0} with

  C_alpha <= |S| <= p^(1-alpha).

Then S has a valid ordering.
```

The public abstract states the same qualitative coverage:

```text
|S| <= p^(1-alpha)
and |S| sufficiently large with respect to alpha,
for any alpha in (0,1).
```

It also states that combined with earlier results this resolves the conjecture for all sufficiently large primes.

---

## 2. Translation to repo notation

Repo notation:

```text
A subset F_p^*,
t = |A|,
B = F_p^* \ A,
|B| = p - 1 - t.
```

Source notation:

```text
S subset Z_p \ {0}.
```

Translation:

```text
S = A,
|S| = t.
```

Coverage rule shape:

```text
C_alpha <= t <= floor(p^(1-alpha)).
```

Complement form:

```text
p - 1 - floor(p^(1-alpha)) <= |B| <= p - 1 - C_alpha.
```

---

## 3. Constants required for executable use

To use this theorem in:

```text
scripts/reduction_residue_audit.py --prove
```

we need at minimum:

```text
alpha: chosen rational/decimal in (0,1)
C_alpha: explicit integer lower threshold for t
P_alpha or P_0: explicit prime lower threshold, if any
```

An executable medium-range rule has form:

```text
covers if:
  p >= P_alpha
  C_alpha <= t <= floor(p^(1-alpha))
```

Current status:

```text
C_alpha: not extracted
P_alpha/P_0: not extracted
```

---

## 4. Constant dependency graph placeholder

The proof-body extraction must fill this table.

| Constant | Source location | Depends on | Needed for | Current status |
|---|---|---|---|---|
| `C_alpha` | Theorem 1.2 / proof | `alpha`, proof lemmas | lower endpoint `t >= C_alpha` | pending |
| `P_alpha` or `P_0` | theorem/proof if present | `alpha`, thresholds | prime lower threshold | pending |
| anticoncentration constant | Theorem 1.3 per ledger note | possibly explicit `2^24` | proof ingredient | partially identified, not linked to `C_alpha` |
| absorption/extension thresholds | proof body | unknown | construction completion | pending |
| probabilistic thresholds | proof body | unknown | valid-ordering existence | pending |
| earlier-result interface | combined sufficiently-large claim | Bedert--Kravitz / other sources | full large-prime closure | pending |

---

## 5. Extraction pass plan

### Pass 1: theorem map

Extract:

```text
1. Theorem 1.2 exact wording.
2. Theorem 1.3 exact wording and constant role.
3. Every lemma/proposition used in proving Theorem 1.2.
4. Every occurrence of:
   - sufficiently large;
   - choose epsilon small enough;
   - for C large enough;
   - with high probability;
   - by previous theorem/result.
```

### Pass 2: constant dependency graph

For each constant, record:

```text
constant_name
introduced_in
depends_on
explicit_formula_or_inequality
recursive_definition_possible?
numeric evaluation possible?
```

### Pass 3: executable rule decision

Decide one of:

```text
A. effective executable: update source_theorems.yaml to effective;
B. effective symbolic but not executable: keep non_effective, add symbolic graph;
C. not extractable from written proof: keep non_effective and record blocker.
```

---

## 6. Preliminary effectivity assessment

Based on current repo ledger and abstract-level record:

```text
The theorem is qualitative in the repo's current extraction state.
C_alpha exists but is not currently numeric or recursively encoded.
The complete sufficiently-large-prime closure also depends on earlier results and thresholds not yet combined effectively.
```

Therefore:

```text
Do not use --cover-medium-alpha in --prove mode.
Do not mark pham_sauermann_2026_large_prime effective.
```

---

## 7. Proposed YAML rule if extraction succeeds

Only after constants are extracted, update:

```text
docs/source_theorems.yaml
```

with a new effective entry or revise the existing one:

```yaml
- source_id: pham_sauermann_2026_alpha_<tag>
  authors: "Huy Tuan Pham; Lisa Sauermann"
  title: "On Graham's rearrangement conjecture"
  arxiv_or_publication: "arXiv:2602.15797"
  theorem_number: "Theorem 1.2"
  exact_statement: "For chosen alpha=<...>, every S subset Z_p\\{0} with C_alpha <= |S| <= p^(1-alpha) has a valid ordering, for p >= P_alpha."
  prime_hypotheses: "p prime, p >= P_alpha=<explicit>"
  set_size_hypotheses: "C_alpha=<explicit> <= t <= floor(p^(1-alpha))"
  constants_or_thresholds: "alpha=<...>; C_alpha=<...>; P_alpha=<...>"
  effective_status: "effective"
  translation_to_p_t: "C_alpha <= t <= floor(p^(1-alpha)) for p >= P_alpha"
  translation_to_p_b: "p-1-floor(p^(1-alpha)) <= |B| <= p-1-C_alpha for p >= P_alpha"
  audit_rule_status: "proof_mode_usable"
```

Do not add this until the proof-body extraction supports it.

---

## 8. Current blocker

```text
Need proof-body extraction of C_alpha and any p-threshold.
```

More precise blockers to identify during reading:

```text
1. Is C_alpha explicitly bounded or only existential?
2. Does the proof depend on non-effective compactness/regularity/removal machinery?
3. Are all probabilistic thresholds quantitative?
4. Does Theorem 1.3's explicit constant feed quantitatively into Theorem 1.2?
5. What previous results are needed for the “combined with earlier results” full large-prime claim?
```

---

## 9. Current action item

Next agent task:

```text
Open arXiv:2602.15797 PDF.
Read proof of Theorem 1.2 as a compiler.
Fill Sections 4--8 with theorem-numbered dependencies and exact constant status.
```
