# Informal leads and sanity checks

This file records non-authoritative or not-yet-audited leads that may help guide future work on Erdos 475 / Graham's rearrangement conjecture.

Nothing in this file is a proof dependency. Do not cite this file in proof-level residue audits. Any item here must be promoted through `docs/source_theorems.yaml` and `docs/source_effectivity_targets.yaml` before use in a formal or proof-level claim.

## Use policy

A lead may be promoted only if all of the following are satisfied:

```text
1. the source is identified precisely;
2. the mathematical statement is copied into a source-audit document;
3. the statement is checked against the original source;
4. constants and hypotheses are extracted;
5. the result is encoded as a source theorem or rejected explicitly.
```

## Lead 1: explicit rough small-set bounds from MathOverflow-style discussions

Status:

```text
informal_lead_unverified
```

Possible relevance:

```text
An explicit bound of the rough form k^(k/2) or similar may exist in informal discussion around small-set sequenceability.
```

Why it matters:

```text
Even a weak explicit bound could serve as a sanity-check baseline for the small-set side of the coverage bridge. If the bound implies something like t <= f(p) with f(p) invertible into p >= P(t), it may provide an executable but weak coverage rule.
```

Required audit steps:

```text
1. Locate the exact MathOverflow question/comment/answer.
2. Record the author and URL.
3. Determine whether the statement is complete or heuristic.
4. Translate the claim into A subset F_p^*, t = |A| notation.
5. Check whether the argument covers prime fields, cyclic groups, or general abelian groups.
6. Compare against Kravitz 2024 and Costa--Della Fiore 2026.
```

Do not encode this in `reduction_residue_audit.py` unless it becomes a citable theorem or a fully reconstructed proof.

## Lead 2: rainbow-path / edge-colouring analogy

Status:

```text
method_context_only
```

Possible relevance:

```text
Sequenceability can be recast in terms of paths with distinct vertices / rainbow-type constraints in coloured Cayley graphs or related edge-coloured graph models.
```

Why it matters:

```text
This may suggest absorber, nibble, or local lemma approaches for constructing orderings with distinct partial sums. It is most relevant if the current analytic bridge fails because constants are non-effective.
```

Required audit steps:

```text
1. Identify exact preprints or papers using rainbow paths for Graham-type rearrangement problems.
2. Extract the graph model precisely.
3. Determine whether the result gives exact sequenceability, almost-sequenceability, or only asymptotic partial distinctness.
4. Decide whether the method can support an explicit repair lemma for finite complements B.
```

Do not add as a source theorem unless it produces a coverage rule in (p,t) or (p,|B|) form.

## Lead 3: one-shot Lovasz Local Lemma constraints

Status:

```text
method_mining
```

Primary source candidate:

```text
costa_dellafiore_2026_cyclic_weak_sequenceability
```

Possible relevance:

```text
The one-shot LLL framework may replace a two-step random construction and give more traceable constants. This could be useful for either small-set sequenceability or local insertion-repair arguments.
```

Required audit steps:

```text
1. Extract the bad events.
2. Extract the probability bound for each bad event.
3. Extract the dependency degree.
4. Check whether the symmetric or asymmetric LLL is used.
5. Determine whether the inequalities are explicit enough to solve for c.
```

Potential implementation target:

```text
scripts/lll_constant_sanity_check.py
```

This script should not be written until the proof body has been audited.

## Lead 4: finite-complement insertion repair

Status:

```text
internal_method_candidate
```

Possible relevance:

```text
The repository's finite certificates are expressed in complement notation B = F_p^* \ A. If a general local insertion or repair theorem can be proved for small |B|, it could provide a direct small-complement / large-A theorem independent of BBKMM constants.
```

Potential theorem shape:

```text
For fixed K, for all sufficiently large primes p and all B subset F_p^* with |B| <= K, the set A = F_p^* \ B is sequenceable.
```

Required audit steps:

```text
1. Identify a canonical base ordering of F_p^* or F_p^* minus a small set.
2. Characterize collisions caused by deleting B.
3. Define local repairs by block swaps, rotations, or insertions.
4. Prove that the repair graph has no trapped components for sufficiently large p.
5. Validate the lemma against existing finite certificates.
```

This is likely hard but may become necessary if published large-set constants remain non-effective.

## Lead 5: cyclic-group generalization track

Status:

```text
future_scope
```

Possible relevance:

```text
Problem 475 in the repository is focused on prime fields, but recent cyclic-group papers suggest a natural second branch for Z_k and general abelian groups.
```

Do not mix the cyclic branch into the prime-field proof ledger unless the theorem explicitly specializes to prime fields and improves or clarifies an audit rule.

Recommended future file:

```text
docs/CYCLIC_GROUP_EXTENSION_PLAN.md
```

Only create this once the prime-field bridge is structurally stable.
