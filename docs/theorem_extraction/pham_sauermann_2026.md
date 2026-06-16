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
Effectivity level: 2+ provisional.
The theorem/proof dependency skeleton is identified.
The Section 5 top-level C_alpha inequalities are extracted from the PDF.
The Corollary 4.2 constants C_1 and C_D are still black-box constants, so the theorem is not yet executable.
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

Theorem 1.2 states that for every `0 < alpha < 1`, there is a constant `C_alpha > 0` such that if `p` is prime and

```text
S subset Z_p \ {0},
C_alpha <= |S| <= p^(1-alpha),
```

then `S` has a valid ordering.

This is the repo's desired medium-range source theorem.

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

## 3. Top-level constants extracted from the PDF

The proof of Theorem 1.2 starts Section 5 by reducing to:

```text
0 < alpha < 1/2.
```

This is valid because proving the result for a smaller exponent parameter implies it for larger `alpha` values.

It then defines:

```text
D = ceil(3 / alpha).
```

Let `C_1` and `C_D` denote the constants from Corollary 4.2 for:

```text
k = 1,
k = D.
```

The proof chooses `C_alpha` large enough so that all of the following hold.

### C_alpha lower-bound condition A

```text
C_alpha >= (10^4 * 2^(40D))^(1/alpha).
```

### C_alpha lower-bound condition B

The PDF line wrapping is awkward, but the displayed chain is:

```text
C_alpha >= (D + 1) * 2^D * D^(14D^2)
          >= 100 * (5D)^(2D)
          >= (40D)^D.
```

For executable extraction, use the direct sufficient condition:

```text
C_alpha >= max(
  (D + 1) * 2^D * D^(14D^2),
  100 * (5D)^(2D),
  (40D)^D
).
```

The first term appears intended to dominate the latter two, but an implementation should not assume domination without checking.

### C_alpha analytic inequality condition C

For all integers/reals `n >= C_alpha`, require:

```text
4 * max(C_D, C_1) * sqrt(log(n) / n^(1/2)) <= n^(-alpha).
```

Equivalently, because `sqrt(log(n) / n^(1/2)) = sqrt(log n) / n^(1/4)`, require:

```text
4 * max(C_D, C_1) * sqrt(log n) <= n^(1/4 - alpha).
```

This is only eventually possible when:

```text
alpha < 1/4
```

if transcribed exactly. The PDF line may instead intend:

```text
4 * max(C_D, C_1) * sqrt(log n / n) <= n^(-alpha),
```

which is eventually possible for all `alpha < 1/2`.

**Extraction warning:** the PDF text parser may have ambiguously parsed the radical/denominator. This exact inequality must be checked against the TeX source before executable coding.

### Consequences used immediately

For `S` satisfying Theorem 1.2, the proof records:

```text
|S| / p <= p^(-alpha) <= |S|^(-alpha),
4*C_1*sqrt(log |S| / |S|^(?)) <= |S|^(-alpha),
4*C_D*sqrt(log |S| / |S|^(?)) <= |S|^(-alpha).
```

The same radical ambiguity applies. The consequence is used repeatedly in Lemma 5.1--5.6 estimates.

---

## 4. Corollary 4.2 extracted statement

Corollary 4.2 states that for every positive integer `k`, there is a constant `C_k > 0` such that for prime `p`, subset `S subset Z_p`, and a uniformly random chain

```text
R_1 subset ... subset R_k subset S,
|R_i| = m_i,
1 <= m_1 < ... < m_k < |S|,
```

for any `z_1,...,z_k in Z_p`,

```text
P[ Sigma(R_i) = z_i for i=1,...,k ]
  <= sum_{j=0}^k product_{i in {0,...,k}\{j}}
       ( 1/p + C_k * sqrt(log |S| / ( |S| * (m_{i+1}-m_i) )) )
```

where the PDF displays the factor in a line-wrapped form. The intended denominator must be checked from TeX, but subsequent uses have the schematic factor:

```text
1/p + C_k * sqrt(log |S| / |S|) / sqrt(gap)
```

or equivalently:

```text
1/p + C_k * sqrt(log |S| / (|S| * gap)).
```

This corollary is the main black-box dependency for Section 5. Section 5 needs:

```text
C_1 = C_k for k=1,
C_D = C_k for k=D=ceil(3/alpha).
```

---

## 5. Proof structure map

The paper organization is:

```text
Section 2: preliminaries;
Section 3: Theorem 1.3, anticoncentration on boolean slices;
Section 4: Corollary 1.4 and Corollary 4.2, chain anticoncentration;
Section 5: proof of Theorem 1.2 using Corollary 4.2 and Lemmas 5.1--5.3.
```

### Theorem 1.3

Theorem 1.3 gives an anticoncentration bound for a random fixed-size subset `R`:

```text
max_z P[Sigma(R)=z] <= 1/p + C/( |S| * sqrt(m) ).
```

The proof of Section 3 says it proves the theorem with:

```text
C = 2^24.
```

### Corollary 1.4

Corollary 1.4 extends the bound to all `m <= (1-epsilon)|S|`:

```text
max_z P[Sigma(R)=z] <= 1/p + C'_epsilon * sqrt( log |S| / (|S| * m) ).
```

The constant `C'_epsilon` is not yet explicitly unwound.

### Corollary 4.2

Corollary 4.2 gives the chain version with constants `C_k`. Its constants depend on Corollary 1.4 and `k`.

### Lemma 4.3

Lemma 4.3 sums the Corollary 4.2 right-hand side over all choices of chain sizes. It is used in Lemmas 5.2, 5.5, and 5.6.

### Lemmas 5.1--5.3

These bound the bad events used in the random-bijection repair argument.

The proof of Theorem 1.2 first chooses a bijection avoiding three bad events, then greedily picks admissible transpositions. Lemmas 5.1--5.3 make the union of the bad-event probabilities small enough to guarantee such a bijection exists.

---

## 6. Constant dependency graph

| Constant | Source location | Depends on | Needed for | Current status |
|---|---|---|---|---|
| `C_alpha` | Theorem 1.2 / Section 5 setup | `alpha`, `D`, `C_1`, `C_D`, Lemma 5 thresholds | lower endpoint `t >= C_alpha` | top-level inequalities extracted; radical ambiguity pending TeX check |
| `D` | Section 5 | `alpha` | bad-event thresholds | extracted: `D=ceil(3/alpha)` |
| `C_1` | Corollary 4.2 | Corollary 1.4 with `k=1` | Section 5 estimates | black-box constant; not numeric |
| `C_D` | Corollary 4.2 | Corollary 1.4 with `k=D` | Section 5 estimates | black-box constant; not numeric |
| `C` for Theorem 1.3 | Section 3 | absolute Fourier/Chernoff estimates | base anticoncentration | extracted from prose as `2^24`; verify exact theorem-vs-proof constant from TeX |
| `C'_epsilon` | Corollary 1.4 | Theorem 1.3 constant and epsilon | larger subset anticoncentration | pending |
| `C_k` | Corollary 4.2 | `C'_epsilon`, `k` | chain anticoncentration | pending |
| `P_alpha` or `P_0` | not explicit in Theorem 1.2 | possibly absorbed by `C_alpha` | prime lower threshold if required | likely none separately; pending TeX check |

---

## 7. Effectivity assessment after PDF constant pass

Current assessment:

```text
Theorem 1.2 appears effective in principle.
It is not executable yet.
The top-level C_alpha recipe is now visible, but it depends on non-extracted C_1 and C_D from Corollary 4.2.
```

Reason:

```text
The proof uses finite probabilistic estimates, union bounds, hypergeometric Chernoff bounds, Cauchy-Davenport, and chain-anticoncentration estimates.
No non-effective compactness or infinitary regularity argument has been identified.
```

Remaining caveat:

```text
The PDF parser gives enough structure for the C_alpha threshold, but TeX source is still needed to remove radical/denominator ambiguity and to unwind C_k constants.
```

Therefore:

```text
Do not use --cover-medium-alpha in --prove mode.
Do not mark pham_sauermann_2026_large_prime effective.
```

---

## 8. Proposed executable extraction target

A symbolic executable recipe should eventually be:

```text
input alpha in (0,1):
  alpha0 = min(alpha, 1/3 or other value sufficient for the Section 5 reduction)
  D = ceil(3 / alpha0)
  C1 = corollary_4_2_constant(k=1)
  CD = corollary_4_2_constant(k=D)
  C_alpha = least integer N such that for all n>=N:
      N >= (10^4 * 2^(40D))^(1/alpha0)
      N >= (D+1)*2^D*D^(14D^2)
      N >= 100*(5D)^(2D)
      N >= (40D)^D
      4*max(CD,C1)*sqrt(log n / n) <= n^(-alpha0)   # pending TeX check
```

The final line must be corrected after TeX extraction if the denominator is `n^(1/2)` rather than `n` under the radical.

---

## 9. Source-access status

The arXiv PDF is accessible and was sufficient for the first constant pass. The arXiv abstract page also exposes a TeX Source link for `2602.15797`.

A local helper has been added:

```text
scripts/fetch_arxiv_source_bundle.py
```

Run on a machine with ordinary network access:

```bash
python scripts/fetch_arxiv_source_bundle.py 2602.15797 \
  --out-dir data/theorem_extraction/pham_sauermann_2026_source
```

Then search the extracted `.tex` files for:

```bash
grep -R "D =" data/theorem_extraction/pham_sauermann_2026_source
grep -R "C_\\alpha" data/theorem_extraction/pham_sauermann_2026_source
grep -R "Corollary 4.2" data/theorem_extraction/pham_sauermann_2026_source
grep -R "2^{24}\|2\\^" data/theorem_extraction/pham_sauermann_2026_source
```

---

## 10. Proposed YAML rule if extraction succeeds

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
  exact_statement: "For chosen alpha=<...>, every S subset Z_p\\{0} with C_alpha <= |S| <= p^(1-alpha) has a valid ordering."
  prime_hypotheses: "p prime"
  set_size_hypotheses: "C_alpha=<explicit> <= t <= floor(p^(1-alpha))"
  constants_or_thresholds: "alpha=<...>; C_alpha=<...>; P_alpha=<none or explicit>"
  effective_status: "effective"
  translation_to_p_t: "C_alpha <= t <= floor(p^(1-alpha))"
  translation_to_p_b: "p-1-floor(p^(1-alpha)) <= |B| <= p-1-C_alpha"
  audit_rule_status: "proof_mode_usable"
```

Do not add this until the Corollary 4.2 constants are made recursively explicit.

---

## 11. Current blockers

```text
1. Need TeX check of the radical/denominator in the Section 5 inequality.
2. Need exact Corollary 4.2 constant dependency for k=1 and k=D.
3. Need verification of Theorem 1.3 constant C=2^24 and how it feeds into Corollary 1.4.
4. Need explicit formulas/inequalities from Lemmas 5.1--5.6 if they impose further thresholds beyond the Section 5 setup.
5. Need decision whether all thresholds can be absorbed into C_alpha with no separate P_alpha.
```

---

## 12. Current action item

Next agent task:

```text
Use TeX source or careful PDF screenshots to resolve the Section 5 radical ambiguity and unwind Corollary 4.2 constants.
```
