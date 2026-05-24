# AI-assisted strategy for Erdős 475

This note records how the recent AI/Erdős developments should change the project workflow.

## Practical lesson

The useful lesson is not that an LLM can be trusted to write a long informal proof.

The useful lesson is:

```text
AI should generate candidates, but the repository should accept only:
  1. source-certified theorem statements,
  2. executable finite certificates,
  3. machine-verifiable proof objects, or
  4. narrowly scoped lemmas with explicit hypotheses and local checks.
```

## Recommended architecture

```text
literature theorem extraction
  -> interval/range coverage model over (p,t,b)
  -> finite residual witness generation
  -> independent witness verification
  -> optional Lean formalization of trusted semantics
```

where

```text
p = prime modulus
t = |A|
b = |B| = p - 1 - t
B = F_p^* \ A
```

## Separate base theorem from stronger variants

The base Erdős 475 statement only requires pairwise distinct nonempty partial sums.

Do not force the stronger endpoint-avoidance condition unless a later theorem explicitly needs it.

Recommended split:

```text
Base track:
  Graham-valid ordering only.

Strengthening track:
  endpoint avoidance, strong nonzero-sum, and related variants.
```

## AI task queue

### Task 1: Source extraction

Prompt an AI model with one paper at a time and require the following output only:

```text
Theorem number:
Exact quoted hypothesis:
Exact quoted conclusion:
Variables used by the paper:
Translation to p,t,b:
Are constants effective?
Any explicit thresholds?
Can this theorem be encoded in data/literature_coverage.json?
```

Reject outputs that paraphrase asymptotic notation without preserving quantifiers.

### Task 2: Coverage falsification

Ask AI to find gaps in a proposed coverage JSON:

```bash
python scripts/check_literature_coverage.py \
  --coverage-json data/literature_coverage.json \
  --finite-domain 29:3-7 \
  --finite-domain 31:3-6 \
  --max-p 10000 \
  --require-full-coverage
```

The AI should report uncovered `(p,t,b)` pairs rather than inventing missing theorems.

### Task 3: Witness minimization

Use AI to simplify certificate artifacts, but preserve an independently checkable kernel:

```text
{p, B, final_order}
```

Everything else is provenance.

### Task 4: Formalization

Use AI to generate Lean definitions and small lemmas first:

```text
partial sums
Nodup partial sums
order lists exactly A
complement relation B = F_p^* \ A
scaling invariance
single witness validity
```

Do not ask the model to formalize the full theorem until these primitives compile.

## Rejection criteria for AI-generated proof text

Reject or quarantine any AI output that:

```text
1. changes the theorem statement;
2. replaces explicit constants with 'sufficiently large' without a bound;
3. assumes endpoint avoidance when only Graham-validity is known;
4. confuses A-size t with complement-size b;
5. treats canonical representatives as all subsets without proving scaling invariance;
6. claims a complete proof without a coverage audit.
```

## Current priority

```text
Highest priority: complete docs/literature_exact_thresholds.md.
Second priority: build data/literature_coverage.json from source-certified values.
Third priority: align the finite certificate domain with the exact residual domain.
```
