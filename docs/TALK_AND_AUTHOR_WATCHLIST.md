# Talk and author watchlist

This file tracks places to monitor for non-paper information relevant to Erdos 475 / Graham's rearrangement conjecture.

This is not a proof dependency. It is a source-discovery aid.

## Purpose

Recent progress on Graham's rearrangement conjecture is moving quickly. Some useful information may appear first in:

```text
seminar abstracts
conference talks
author webpages
slide decks
video lectures
MathOverflow comments
GitHub repositories
problem-database updates
```

The purpose of this file is to monitor those channels without polluting the proof ledger.

## Promotion rule

A talk or informal note may influence the proof codebase only after it is converted into one of:

```text
1. a published/preprint source entry in docs/source_theorems.yaml;
2. a target entry in docs/source_effectivity_targets.yaml;
3. a clearly labeled informal lead in docs/INFORMAL_LEADS_AND_SANITY_CHECKS.md;
4. a dedicated source-audit document.
```

## Authors to monitor

### Huy Tuan Pham

Reason:

```text
Coauthor of the 2026 prime-field sufficiently-large-prime breakthrough.
```

Watch for:

```text
slides explaining Theorem 1.2
explicit notes on C_alpha
updates to arXiv:2602.15797
seminar recordings or abstracts
```

### Lisa Sauermann

Reason:

```text
Coauthor of the 2026 prime-field sufficiently-large-prime breakthrough.
```

Watch for:

```text
conference slides
research talks on anticoncentration / additive combinatorics
updated versions of arXiv:2602.15797
```

### Benjamin Bedert

Reason:

```text
Coauthor of the small-set exponential-quarter theorem and large-set / group-theoretic work.
```

Watch for:

```text
slides on the rectification barrier
clarifications of the large-prime threshold in Bedert--Kravitz
updates on BBKMM constants
```

### Noah Kravitz

Reason:

```text
Author/coauthor of both the log/loglog small-set baseline and the stronger Bedert--Kravitz small-set theorem.
```

Watch for:

```text
notes on explicit constants
MathOverflow comments
integer-ordering lemmas
seminar slides on Graham's conjecture
```

### Matija Bucic, Richard Montgomery, Alp Muyesser

Reason:

```text
Coauthors on the large-set / F_2^n / general-group paper.
```

Watch for:

```text
absorber-method explanations
explicit c in |G|^(1-c)
regularity or local lemma constants
```

### Simone Costa, Stefano Della Fiore, Mattia Fontana, Lluis Vena

Reason:

```text
Recent abelian/cyclic-group sequenceability papers, including the |A| <= 20 abelian result and the Z_k weak-sequenceability improvement.
```

Watch for:

```text
explicit constants in the Z_k exp(c(log p)^(1/3)) theorem
Lovasz Local Lemma dependency calculations
cyclic-group refinements that specialize to prime fields
```

## Venues / sites to monitor

### arXiv search terms

```text
"Graham's rearrangement conjecture"
"Graham rearrangement conjecture"
"sequenceability"
"weak sequenceability"
"distinct partial sums"
"rainbow paths" "Graham"
"zero-sum" "sequenceable"
```

Suggested cadence:

```text
monthly until the bridge is closed
weekly during active extraction work
```

### Erdős problem database

Reason:

```text
Problem 475 status or comments may update as new community information appears.
```

Watch for:

```text
status changes
comments pointing to new sources
AI-contribution entries
OEIS or finite-computation notes
```

### MathOverflow

Reason:

```text
Informal explicit bounds, proof sketches, or author clarifications may appear there before they appear in papers.
```

Search terms:

```text
Graham rearrangement
sequenceable group
distinct partial sums
Erdos 475
```

Promotion condition:

```text
A MathOverflow lead must be independently reconstructed or tied to a formal source before use.
```

### Seminar pages and conference abstracts

Priority topics:

```text
additive combinatorics
probabilistic combinatorics
rainbow paths
zero-sum theory
sequenceable groups
Latin transversals / sequencing
```

Potentially useful clues:

```text
slides with constants
proof outlines not visible in abstracts
references to upcoming stronger versions
collaborator comments about effectivity
```

## What to record when a useful talk/source is found

Use this template in a future audit note:

```text
source_type: talk | slides | video | webpage | MathOverflow | GitHub | preprint
source_url:
authors_or_speakers:
date_observed:
mathematical_claim:
exact_quote_or_timestamp:
relation_to_prime_field_bridge:
constants_mentioned:
can_be_promoted_to_source_theorem: yes/no
next_action:
```

## Current monitoring conclusion

As of 2026-06-04, the highest-value task is not broad monitoring. It is direct PDF/body extraction for:

```text
1. Pham--Sauermann 2026
2. BBKMM 2025
3. Kravitz 2024
4. Bedert--Kravitz 2024
5. Costa--Della Fiore 2026
```

Monitoring is useful only if it supplies missing constants, corrected theorem statements, or newer versions of these sources.
