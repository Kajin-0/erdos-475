# AI-first analytic roadmap for Erdős 475

This roadmap is optimized for a single researcher with limited compute.

The goal is not to brute-force the problem.  The goal is to use AI as a fast analytic coauthor and use scripts only when they produce high-value falsification, examples, counterexamples, or finite sanity checks.

## North-star objective

Prove or disprove Erdős Problem 475 / Graham's rearrangement problem by developing a human-readable analytic proof chain, with computation used only as a guardrail.

The desired artifact is:

```text
A concise analytic manuscript:
  definitions
  one main invariant
  a small number of repair lemmas
  global termination or explicit obstruction
  finite sanity checks as appendix only
```

The repository should avoid becoming a compute-heavy enumeration project.

## Resource assumptions

```text
Researcher: one person
Compute: laptop / low-resource VPS / occasional short scripts
Primary accelerator: AI reasoning over lemmas, examples, proof compression, and counterexample search
Unacceptable strategy: massive exhaustive search over all subsets for large p
Acceptable scripts: small-prime falsification, local move testing, obstruction mining, witness checking
```

## Correct role of computation

Use computation for four narrow tasks.

### 1. Lemma falsification

Before spending days on a lemma, test it for small primes.

A lemma should be marked:

```text
UNTESTED
TESTED_SMALL
FALSE_COUNTEREXAMPLE_FOUND
SURVIVED_SMALL_TESTS
PROVED
```

Small tests do not prove the lemma, but they prevent wasted analytic effort.

### 2. Obstruction mining

When a local repair fails, collect the exact algebraic shape of the obstruction.

The script output should be mathematical, not just PASS/FAIL:

```text
failed move type
active interval
collision equation
which old partial sums collide
which atom caused the obstruction
minimal obstruction profile
```

### 3. Proof-shape discovery

Use scripts to generate examples that AI can inspect and generalize:

```text
minimal bad configuration under a proposed invariant
minimal forced descent example
smallest obstruction graph
symmetry-normalized pattern
```

### 4. Final witness/certificate checking

Use finite scripts only after an analytic residue is sharply bounded.

Do not let finite checking define the proof strategy.

## Main analytic attack

The strongest current internal route is the strong nonzero-sum repair program.

Target theorem:

```text
If S subset F_p^* and sigma(S) != 0,
then S has an ordering whose extended partial sums
0, S_1, ..., S_t
are pairwise distinct.
```

This implies Erdős 475 by the append-one-atom argument already recorded in the repo.

## Preferred proof strategy

### Step 1. Defect minimization

Pick an ordering minimizing a defect vector.

Candidate defect:

```text
D(R) = (
  number_of_zero_hits_or_collisions,
  shortest_bad_interval_length,
  boundary_rank,
  local_support_size,
  tie_breaker
)
```

The exact vector must be simple enough to state in a paper.

### Step 2. Local repair lemma

Show that if a bad interval exists, moving an adjacent outside atom through the interval either:

```text
1. strictly decreases D(R), or
2. creates a rigid algebraic obstruction.
```

The local move should be one of:

```text
adjacent swap
cut-and-insert
block rotation
two-block exchange
```

Keep the move library small.  Too many move types make the proof unmanageable.

### Step 3. Obstruction classification

If all useful local repairs fail, prove the obstruction equations force one of a few rigid structures:

```text
PAIR_TRAP
SIGNED_INTERVAL
SEPARATED_EQUAL_SUM
MIDPOINT_ADJACENT
LARGE_ATOM / repeated blocker
```

Every obstruction class must have:

```text
precise algebraic definition
minimal example
repair lemma or contradiction lemma
small-prime tests
status tag
```

### Step 4. Global termination

Define one well-founded measure and prove every nonterminal repair decreases it.

Avoid a large state machine unless absolutely necessary.

Preferred final form:

```text
Minimal-counterexample contradiction:
  choose R minimizing D
  find active bad interval
  either repair decreases D, contradiction,
  or obstruction classification applies,
  each obstruction class gives a smaller D or impossible equation.
```

## Do not over-prioritize literature constants

The literature route remains valuable as a safety rail, but it is not the main creative route.

Use it for:

```text
checking whether the problem is already effectively resolved;
benchmarking proof techniques;
preventing rediscovery of known partial results;
identifying likely useful lemmas.
```

Do not let it consume the project.  Exact asymptotic constants can become a sinkhole.

## AI work loop

Use a repeated 6-stage loop.

```text
1. State one lemma precisely.
2. Ask AI for a proof.
3. Ask AI to attack the proof and find the weakest step.
4. Run a small falsification script if the lemma is local/combinatorial.
5. If false, save the counterexample and weaken the lemma.
6. If true-looking, compress into manuscript form.
```

No large proof should be accepted unless every intermediate lemma has gone through this loop.

## AI prompt template: lemma generation

```text
We are working on Erdős 475 over F_p.
Definitions:
- R is an ordering of S subset F_p^*.
- Partial sums are P_i = r_1 + ... + r_i.
- A strong nonzero-sum ordering has 0,P_1,...,P_t pairwise distinct.

Task:
Prove or disprove the following lemma.

Lemma:
[insert exact lemma]

Rules:
1. Do not change the statement.
2. If false, give the smallest counterexample you can find by reasoning.
3. If true, give a proof using only explicit algebraic equalities in F_p.
4. Identify every place where distinctness of atoms is used.
5. Identify whether the proof requires p to be odd, p > 3, or any size bound.
```

## AI prompt template: proof attack

```text
Act as a hostile referee.
The following lemma is proposed for Erdős 475.

[lemma + proof]

Find the first invalid step.
If the proof is valid, say exactly what hidden hypotheses are required.
If the statement is false, construct a counterexample over the smallest prime p possible.
```

## AI prompt template: obstruction compression

```text
Given these failed local repairs and collision equations:

[data]

Find the smallest algebraic obstruction class that explains them.
Return:
1. a named obstruction class;
2. its defining equations;
3. whether it is invariant under translation/scaling/reversal;
4. a repair move that should break it;
5. one lemma statement that would eliminate the class.
```

## Repository organization for analytic sprint

Recommended files:

```text
docs/analytic_sprint/S00_problem_statement.md
docs/analytic_sprint/S01_defect_vector.md
docs/analytic_sprint/S02_local_moves.md
docs/analytic_sprint/S03_obstruction_classes.md
docs/analytic_sprint/S04_global_termination.md
docs/analytic_sprint/S05_counterexample_ledger.md
scripts/mine_local_obstructions.py
scripts/test_local_lemma.py
```

## Immediate analytic priorities

### Priority 1: simplify the defect vector

Current internal notes contain many phase/rank concepts.  This may be too complex for a publishable proof.

Find the smallest defect vector that can drive the proof.

### Priority 2: prove one universal local repair lemma

Target:

```text
Given a minimal defective ordering and a shortest bad interval,
at least one adjacent outside atom can be inserted or swapped to reduce defect,
unless a named obstruction equation holds.
```

### Priority 3: classify minimal obstruction equations

Generate obstruction examples for primes up to a small bound, then ask AI to compress the patterns.

### Priority 4: decide whether endpoint avoidance is a distraction

Endpoint avoidance is stronger than base Erdős 475.  Use it only if it makes the strong nonzero-sum proof cleaner.  Otherwise keep it separate.

## Success criterion

A meaningful win is not necessarily the full theorem immediately.

Acceptable publishable progress could be:

```text
1. a new proof of a known size regime;
2. a simpler proof of the sufficiently-large-prime theorem;
3. a finite-residue reduction with explicit small constants;
4. a clean analytic proof of the strong nonzero-sum theorem under one natural extra condition;
5. a counterexample to a stronger endpoint-avoidance variant.
```

The fastest route to priority is a clean analytic insight, not a large computation.
