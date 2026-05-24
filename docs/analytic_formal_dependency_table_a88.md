# Analytic formal dependency table A88

This note continues from A87.

A87 established the local lemma audit checklist.  A88 converts the proof program into a formal dependency table for proof extraction.

The purpose is to separate:

```text
1. theorem-level dependencies;
2. local obstruction dependencies;
3. high-risk proof-sketch dependencies;
4. computational/advisory dependencies;
5. final-proof replacement lemma IDs.
```

This is not a proof.  It is a proof-extraction roadmap.

---

## 1. Status labels

Use the following audit labels.

```text
GREEN      statement appears self-contained or nearly self-contained;
YELLOW     statement likely correct but needs endpoint/sign/empty-block hardening;
ORANGE     statement relies on routing language or proof sketches;
RED        statement is a structural bottleneck requiring full proof reconstruction;
ADVISORY   computational or exploratory evidence only;
OBSOLETE   replaced by later sharper statement.
```

Use the following extraction labels.

```text
KEEP       include in final proof after polishing;
MERGE      combine with nearby lemmas into one final proof lemma;
HARDEN     expand proof sketch into complete proof;
REPLACE    replace with a cleaner final-proof lemma;
DROP       omit from final proof narrative;
CERTIFY    requires computational certificate or independent verifier.
```

---

## 2. Final theorem dependency table

| Final claim | Required notes | Risk | Audit status | Final-proof action |
|---|---|---:|---|---|
| Erdős 475 for `p=2` | A86 | GREEN | Direct enumeration complete | KEEP |
| Endpoint avoidance for odd primes | A5, A64--A84 | RED | Conditional on local routing audit | REPLACE with final proof theorem |
| Endpoint avoidance -> strong nonzero-sum | A2/A3, A85 | GREEN | Clean theorem-level implication | KEEP |
| Strong nonzero-sum -> Erdős 475 | A1, A85 | GREEN | Clean theorem-level implication | KEEP |
| Erdős 475 for odd primes | A84, A85 | RED | Conditional on endpoint-avoidance audit | REPLACE after hardening |
| Erdős 475 for all primes | A84--A86 | RED | Depends on odd-prime proof audit | REPLACE after hardening |

---

## 3. Endpoint-avoidance proof dependencies

| Component | Required notes | Risk | Missing details | Final-proof lemma ID |
|---|---|---:|---|---|
| Minimal counterexample setup | A4, A5, A34, A84 | YELLOW | uniqueness/existence of Graham-valid starting order must be stated cleanly | F1-MinimalSetup |
| First forbidden-hit obstruction | A4, A5 | YELLOW | exact blocker equation and endpoint cases | F2-AdjacentBlocker |
| Obstruction class universe | A35, A63, A72 | ORANGE | compress class taxonomy; remove obsolete labels | F3-ObstructionClasses |
| Non-weighted termination | A72--A78 | RED | all cycles need complete measure-decrease proofs | F4-NonWeightedTermination |
| Weighted-core termination | A56--A62, A79--A83 | RED | A83.2 and weighted induction must be fully formal | F5-WeightedTermination |
| Final contradiction/success assembly | A84 | YELLOW | replace conditional language with dependency-resolved proof | F6-EndpointAvoidance |

---

## 4. Non-weighted termination dependency table

| Subclaim | Required notes | Risk | Audit status | Final-proof action |
|---|---|---:|---|---|
| Obstruction graph nodes/edges | A72 | ORANGE | Needs edge-by-edge formal table | HARDEN |
| Global non-weighted measure `M_NW^*` | A73, A78 | ORANGE | Need prove every coordinate is nonnegative integer and updated correctly | HARDEN |
| Zero-composite / pair-difference cycle descends | A33, A69, A73, A78 | ORANGE | Pair endpoint cases require explicit signs | HARDEN |
| Singleton / pair recurrence cycle descends | A69, A70, A73, A78 | ORANGE | Need exhaustive blocker-location proof | HARDEN |
| Cyclic / singleton recurrence cycle descends | A70, A71, A73, A78 | ORANGE | Wrapping cases must be formalized | HARDEN |
| Separated-equal recurrence cycle descends | A36--A55, A74--A78 | RED | Bridge/gap monotonicity chain must be converted from sketches | HARDEN |
| External collisions are routing edges | A62, A74, A78 | RED | A62 must be fully formal and exhaustive | HARDEN |
| Transported-prefix normalization | A56, A78 | YELLOW | Need exact support/span nonincrease proof | MERGE |

---

## 5. Bridge/gap chain dependency table

| Subclaim | Required notes | Risk | Missing details | Final-proof action |
|---|---|---:|---|---|
| Proper-overlap bridge descent | A74 | YELLOW | Write exact interval decompositions for both orientations | HARDEN |
| Proper-containment bridge descent | A74 | YELLOW | Endpoint containment cases | HARDEN |
| Signed bridge normalization | A74, A56, A69--A70 | ORANGE | Atom-correction absorption must be exhaustive | HARDEN |
| Equal-span separated bridge return | A75 | ORANGE | Need exact gap-after collision table in final notation | HARDEN |
| Gap-preserving separated recurrence | A76 | RED | U-hit/G-hit blocker pullbacks need full sign audit | HARDEN |
| Rigid separated self-return | A77 | RED | Same/exchange orientation proof must be formalized | HARDEN |
| Direct exchange recurrence routing | A36--A54, A70, A77 | ORANGE | Need direct exchange recurrence table, not just reference | MERGE |

---

## 6. Recurrence-routing dependency table

| Recurrence source | Required notes | Risk | Missing details | Final-proof action |
|---|---|---:|---|---|
| Bounded blocker recurrence | A64 | ORANGE | Prove nearest blocker and measure descent rigorously | HARDEN |
| H1 atom-insertion recurrence | A65, A66 | ORANGE | Pullback formulas and crossing cases need sign audit | HARDEN |
| H2 atom-insertion recurrence | A67 | ORANGE | Endpoint `V=empty` and right-blocker signs | HARDEN |
| Pair-swap recurrence | A69 | ORANGE | Proper-prefix/end-point cases | HARDEN |
| Singleton-prefix recurrence | A70 | YELLOW | Atom case and endpoint next-atom cases | HARDEN |
| Cyclic-cut recurrence | A71 | ORANGE | Wrapped/non-wrapped partial sums and special `2f` equations | HARDEN |
| Recurrence status map | A68, A72 | YELLOW | Use only after individual recurrence proofs are hardened | MERGE |

---

## 7. Separated-equal and midpoint dependency table

| Branch | Required notes | Risk | Missing details | Final-proof action |
|---|---|---:|---|---|
| Direct exchange collision table D1--D5 | A36--A54 | ORANGE | Verify all displayed collision equations | HARDEN |
| Gap-after collision table E1--E5 | A49--A54, A75 | ORANGE | Endpoint and empty-gap cases | HARDEN |
| D2 equal/separated subbranch | A40, A52, A53 | RED | Historically high-risk branch; needs full reconstruction | HARDEN |
| Midpoint boundary | A55, A71 | ORANGE | Division by 2 and endpoint cases | HARDEN |
| Adjacent equal blocks | A55, A75, A77 | YELLOW | Ensure zero-gap separated-equal handled uniformly | MERGE |

---

## 8. Weighted-core dependency table

| Subclaim | Required notes | Risk | Missing details | Final-proof action |
|---|---|---:|---|---|
| Weighted normal forms | A56 | RED | Exhaustiveness of easy reductions | HARDEN |
| Nested zero-composite rewrite | A58 | YELLOW | Exact algebra and support relation | KEEP/MERGE |
| Static cut insufficiency | A59 | YELLOW | May be omitted from final proof | DROP unless needed |
| Fixed cut-swap collision routing | A60--A62 | RED | Displayed + external collisions must be exhaustive | HARDEN |
| Weighted cut-selection split | A79 | ORANGE | Induction framing and returned-core classification | HARDEN |
| Atom-middle core | A80, A81 | RED | Adjacent-swap routing and endpoint sign cases | HARDEN |
| Cut-rigid weighted self-return | A82 | RED | Common-return and larger-middle alternatives | HARDEN |
| Internal cyclic rigidity | A83 | RED | Critical A83.2 endpoint-set invariance implication | HARDEN |
| Weighted induction on `|B|` | A79--A83 | RED | Need no branch can increase `|B|` indefinitely before descent | REPLACE |

---

## 9. Computational/certification dependency table

| Item | Required notes/scripts | Risk | Current status | Final-proof action |
|---|---|---:|---|---|
| `p=2` | A86 | GREEN | Done analytically | KEEP |
| `p=3` | A86 + audit | YELLOW | Included in odd proof; audit accidental `/3` | HARDEN |
| Small-prime verification | missing/unknown ledger | ADVISORY | Exact `docs/finite_verification_ledger.md` not found | CERTIFY if cited |
| Exhaustive endpoint avoidance script | future script | ADVISORY | Not required if analytic proof complete | Optional |
| Independent certificate checker | future script | ADVISORY | Not present | Optional unless computation cited |

---

## 10. Critical bottleneck list

Before extraction, resolve these in order.

### B1. A83.2 endpoint-set invariance

Claim:

```text
exact cyclic self-return implies E_B - T_k = E_B.
```

Risk:

```text
This is the linchpin of weighted-core closure.
```

Required hardening:

```text
Define exact self-return formally enough that endpoint-set invariance follows by equality of endpoint sets, not intuition.
```

---

### B2. A62 external collision theorem

Risk:

```text
Used as a universal delegator in many later notes.
```

Required hardening:

```text
Give a complete classification of before/after/cyclic/external collisions and measure effects.
```

---

### B3. A74--A77 bridge/gap chain

Risk:

```text
Turns the hardest non-weighted recurrence tie into known mechanisms.
```

Required hardening:

```text
Convert all proof sketches into exact interval equations and strict measure decreases.
```

---

### B4. A60 cut-swap table

Risk:

```text
Fixed-cut weighted routing rests on the displayed collision table.
```

Required hardening:

```text
Check every collision equation for empty blocks, endpoint collisions, and external collisions.
```

---

### B5. A64 recurrence measure

Risk:

```text
All recurrence routing depends on bounded-blocker descent and long-blocker classification.
```

Required hardening:

```text
Prove nearest-blocker selection and descent under the final global measure.
```

---

## 11. Proposed final-proof lemma numbering

The final extracted proof should not use A1--A88 numbering.  Use a compact final sequence.

```text
F1. Minimal counterexample and adjacent blocker lemma.
F2. Obstruction class definitions and measure.
F3. Zero-composite and pair-difference descent.
F4. Separated-equal and midpoint descent.
F5. Recurrence routing theorem.
F6. External collision theorem.
F7. Non-weighted termination theorem.
F8. Weighted normal-form theorem.
F9. Weighted fixed-cut theorem.
F10. Weighted cut-selection theorem.
F11. Endpoint avoidance theorem.
F12. Endpoint avoidance -> Erdős 475.
F13. Exceptional cases.
```

---

## 12. Extraction order

Recommended order for hardening:

```text
1. F1 adjacent blocker / minimal setup.
2. F6 external collision theorem.
3. F4 separated-equal / midpoint tables.
4. F5 recurrence routing theorem.
5. F3 zero-composite / pair-difference descent.
6. F7 non-weighted termination.
7. F8--F10 weighted proof.
8. F11 endpoint avoidance.
9. F12 theorem dependency.
10. F13 exceptional cases.
```

This order attacks the universal delegators first before assembling global termination.

---

## 13. Current status after A88

The proof program now has:

```text
1. conditional architecture;
2. theorem dependency chain;
3. finite/exceptional case note;
4. audit checklist;
5. formal dependency table.
```

The next phase is not to add more branches.  The next phase is to harden the bottleneck lemmas.

---

## 14. Target A89

A89 should begin hardening the first bottleneck:

```text
A83.2 endpoint-set invariance in internal cyclic rigidity.
```

Recommended title:

```text
Formal hardening of internal cyclic self-return A89
```

Goal:

```text
replace the proof sketch of A83.2 with a definition-driven lemma.
```

Minimum required output:

```text
Definition: exact internal cyclic self-return.
Lemma: exact internal cyclic self-return implies equality of internal endpoint sets.
Lemma: equality under nonzero translation forces full field.
Conclusion: internal cyclic rigidity impossible.
```
