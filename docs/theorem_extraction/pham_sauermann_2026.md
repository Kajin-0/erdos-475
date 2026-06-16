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
Effectivity level: 2 provisional.
The theorem/proof dependency skeleton is now identified from the arXiv HTML.
The constants are not yet executable.
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

The arXiv abstract states that the paper proves Graham's conjecture for all subsets

```text
S subset Z_p \ {0}
```

with:

```text
|S| <= p^(1-alpha)
```

and `|S|` sufficiently large with respect to `alpha`, for every `alpha in (0,1)`.

Theorem 1.2 is the precise source theorem. It states, in repo-paraphrase:

```text
For any 0 < alpha < 1, there exists a constant C_alpha such that:
if p is prime and S subset Z_p \ {0} satisfies

  C_alpha <= |S| <= p^(1-alpha),

then S has a valid ordering.
```

The paper also states that combining this with earlier results resolves Graham's rearrangement conjecture for all sufficiently large primes.

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
P_alpha or P_0: explicit prime lower threshold, if the proof requires one
```

An executable medium-range rule has form:

```text
covers if:
  p >= P_alpha
  C_alpha <= t <= floor(p^(1-alpha))
```

Current status:

```text
C_alpha: structurally located in Section 5 proof setup, but not extracted numerically.
P_alpha/P_0: not separately identified; may be absorbed into C_alpha if all arguments only require |S| large.
```

Important observation:

```text
Theorem 1.2 itself is phrased using only C_alpha and p prime.
The Section 5 proof starts by choosing constants depending on alpha and then takes |S| large enough.
This suggests the theorem may be effective in principle if the constants in Corollary 4.2 and Lemmas 5.1--5.3 are unwound.
```

---

## 4. Proof structure map

The paper organization is:

```text
Section 2: preliminaries;
Section 3: Theorem 1.3, anticoncentration on boolean slices;
Section 4: Corollary 1.4 and Corollary 4.2, chain anticoncentration;
Section 5: proof of Theorem 1.2 using Corollary 4.2 and Lemmas 5.1--5.3.
```

### Theorem 1.3

Role:

```text
Anticoncentration for sums of random subsets of fixed size.
```

Ledger note:

```text
The source_theorems.yaml entry records an explicit-looking absolute constant C=2^24 for Theorem 1.3,
but this still needs verification from the paper body because arXiv HTML strips some displayed math.
```

Dependency status:

```text
Likely quantitative/effective.
Depends on Section 3 lemmas using Chernoff/hypergeometric concentration, Fourier bounds, Cauchy-Davenport, and union bounds.
```

### Corollary 1.4

Role:

```text
Extends Theorem 1.3 to a larger size range needed later.
```

Effectivity issue:

```text
The proof says small |S| can be handled by choosing a large constant.
This introduces a constant depending on alpha/gamma-like parameters.
Need to extract exact dependency.
```

### Corollary 4.2

Role:

```text
Anticoncentration for a uniformly random chain of subsets of prescribed sizes.
```

Effectivity issue:

```text
For every positive integer d, there exists a constant used to bound chain-sum probabilities.
Section 5 uses these constants for d=3 and d=5.
```

### Lemma 4.3

Role:

```text
Sums the Corollary 4.2 bounds over many tuple choices.
```

Effectivity issue:

```text
Appears quantitative once the Corollary 4.2 constant is explicit.
```

### Lemmas 5.1--5.3

Role:

```text
Bad-event bounds for the random starting bijection and admissible transposition repair process.
```

In the proof of Theorem 1.2, the authors choose a random bijection avoiding the bad events in Lemmas 5.1--5.3, then greedily construct transpositions to eliminate zero-sum intervals.

Effectivity issue:

```text
The proof uses constants chosen at the start of Section 5 so that the union of bad-event probabilities is < 1.
The required inequalities must be extracted to define C_alpha.
```

### Lemmas 5.4--5.6

Role:

```text
Auxiliary probability bounds used to prove Lemmas 5.2 and 5.3.
```

Effectivity issue:

```text
These contain union bounds over admissible permutations and chains.
Need to track powers/exponents to build explicit size threshold.
```

---

## 5. Section 5 constant choice: current extraction

The proof of Theorem 1.2 begins by fixing a parameter from `alpha` and then choosing constants large enough.

The arXiv HTML math is partially stripped, but the prose gives the dependency shape:

```text
Let [parameter depending on alpha].
Let [constant] be large enough such that [several inequalities hold]
where constants from Corollary 4.2 for d=3 and d=5 appear.
```

More concretely, Section 5 states that the proof uses constants from Corollary 4.2 for:

```text
d = 3,
d = 5.
```

and chooses the main lower threshold large enough so that several inequalities hold for all relevant sizes.

Current interpretation:

```text
C_alpha is probably a maximum of finitely many explicit threshold inequalities involving:
  - alpha or a derived beta/gamma parameter;
  - constants from Corollary 4.2 for d=3 and d=5;
  - polynomial/exponential union-bound exponents in Lemmas 5.1--5.6.
```

This is encouraging because it suggests the proof is likely effective in principle.

However:

```text
The repo does not yet have the displayed inequalities because arXiv HTML strips much of the math.
The PDF or TeX source must be inspected to extract them exactly.
```

---

## 6. Constant dependency graph

| Constant | Source location | Depends on | Needed for | Current status |
|---|---|---|---|---|
| `C_alpha` | Theorem 1.2 / Section 5 setup | `alpha`, Corollary 4.2 constants, Lemmas 5.1--5.3 thresholds | lower endpoint `t >= C_alpha` | structural dependencies identified; numeric formula pending |
| `P_alpha` or `P_0` | not explicit in theorem statement | possibly none separately if absorbed by `C_alpha` | prime lower threshold if required | pending |
| `C_AC` for Theorem 1.3 | Theorem 1.3 / Section 3 | absolute constants from Fourier/Chernoff estimates | random subset anticoncentration | likely explicit; ledger says `2^24`, verify from PDF/TeX |
| `C_gamma` for Corollary 1.4 | Corollary 1.4 | Theorem 1.3 constant plus gamma/alpha parameters | larger subset anticoncentration | pending |
| `C_d` for Corollary 4.2 | Corollary 4.2 | Corollary 1.4 constants and `d` | chain anticoncentration | pending; Section 5 uses d=3,5 |
| Lemma 5.1 threshold | Section 5 | `C_3` or `C_5`, alpha-derived parameters | bad event probability | pending |
| Lemma 5.2 threshold | Section 5 | Lemma 5.4, Corollary 4.2, Lemma 4.3 | bad event probability | pending |
| Lemma 5.3 threshold | Section 5 | Lemmas 5.5, 5.6, Corollary 4.2, Lemma 4.3 | blocked-elements event probability | pending |
| earlier-result interface | introduction / combined claim | Bedert--Kravitz, BBKMM, others | full sufficiently-large-prime closure | not part of Theorem 1.2 executable medium rule |

---

## 7. Effectivity assessment after first proof-structure pass

Current assessment:

```text
Theorem 1.2 appears likely effective in principle.
It is not executable yet.
The current blocker is extraction of displayed inequalities and constants from the PDF/TeX source, especially Section 5 setup and Corollary 4.2.
```

Reason:

```text
The proof uses finite probabilistic estimates, union bounds, hypergeometric Chernoff bounds, Cauchy-Davenport, and explicit chain-anticoncentration deductions.
No non-effective compactness or infinitary regularity argument has been identified in the first pass.
```

Caveat:

```text
This is only a first pass based on arXiv HTML and visible prose.
Displayed equations are heavily stripped in the HTML and must be recovered from PDF or TeX before the status can be upgraded to Level 3.
```

Therefore:

```text
Do not use --cover-medium-alpha in --prove mode.
Do not mark pham_sauermann_2026_large_prime effective.
```

---

## 8. Proposed executable extraction target

The target is a symbolic recipe:

```text
Given alpha in (0,1):
  beta = beta(alpha) from Section 5.
  C3 = constant from Corollary 4.2 with d=3 and beta/gamma parameter.
  C5 = constant from Corollary 4.2 with d=5 and beta/gamma parameter.
  C_alpha = max(thresholds from Section 5 setup, Lemmas 5.1, 5.2, 5.3).
```

A later executable rule may not need a clean closed form. It can be recursive/pseudocode if every dependency is explicit and finite.

---

## 9. Source-access status

The arXiv abstract page exposes a TeX Source link for `2602.15797`. Browser access through the current assistant toolchain could not safely fetch the source bundle, but this is an environment limitation rather than evidence that the source is unavailable.

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
grep -R "Theorem" data/theorem_extraction/pham_sauermann_2026_source
grep -R "Corollary" data/theorem_extraction/pham_sauermann_2026_source
grep -R "Lemma 5" data/theorem_extraction/pham_sauermann_2026_source
grep -R "large enough" data/theorem_extraction/pham_sauermann_2026_source
grep -R "2^{24}\|2\\^" data/theorem_extraction/pham_sauermann_2026_source
```

Expected files to inspect:

```text
main .tex source;
any macro/style file defining theorem environments;
any bibliography file only for dependency references.
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

Do not add this until the proof-body extraction supports it.

---

## 11. Current blockers

```text
1. Need PDF/TeX extraction of the displayed inequalities in Section 5 setup.
2. Need exact Corollary 4.2 constant dependency for d=3 and d=5.
3. Need verification of Theorem 1.3's constant and whether it feeds quantitatively into Corollary 1.4.
4. Need explicit formulas/inequalities from Lemmas 5.1--5.6.
5. Need decision whether all thresholds can be absorbed into C_alpha with no separate P_alpha.
```

---

## 12. Current action item

Next agent task:

```text
Run scripts/fetch_arxiv_source_bundle.py for 2602.15797.
Inspect the extracted TeX.
Patch this file with exact displayed inequalities.
```

Expected next file update:

```text
Upgrade this audit from Level 2 provisional to Level 2 complete,
with a concrete constant-dependency graph and unresolved formula entries.
```
