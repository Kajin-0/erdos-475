# Analytic reduction audit plan for Erdos 475

This file defines the next phase after the finite verification work.

The computational phase should stop unless a published reduction theorem exposes additional finite residue cases.

## Verified finite domain

The verified complement-domain coverage is:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

Here

```text
B = F_p^* \ A
|B| = p - 1 - |A|
t = |A|
```

## Goal

Determine whether the published analytic reductions for Erdos Problem 475 reduce the infinite problem to a finite residue contained in the verified finite domain above.

The target conclusion is:

```text
analytic residue subset verified finite domain
```

If true, then the remaining finite cases have already been covered by the current repository plus local witness logs.

If false, every extra residue case must be listed explicitly as:

```text
p = ?, |A| = ?, |B| = ?
```

and then either certified computationally or eliminated by an additional analytic argument.

## Required source extraction format

For every relevant published theorem, extract the following fields.

```text
source_id:
authors:
title:
year:
publication / arXiv:
theorem number:
exact statement:
variables used by source:
translation to p, |A|, |B|:
covered range:
exceptions:
dependencies on previous theorems:
confidence:
notes:
```

Do not paraphrase theorem ranges loosely. Record the exact inequalities.

## Known coverage already encoded

The current bookkeeping assumes these broad ranges are already known or expected:

```text
t <= 12
|B| <= 2
```

These must still be tied to exact published theorem statements before making a complete-solution claim.

## Reduction checklist

### 1. Identify source theorem ranges

Find the exact published statements for:

```text
small-set coverage
very-large-set coverage
large-prime or sufficiently-large-prime coverage
any finite residue table claimed in the literature
any exceptional prime list
```

### 2. Translate variables

For every theorem, translate source variables into this repository's notation:

```text
p = prime modulus
A subset F_p^*
t = |A|
B = F_p^* \ A
|B| = p - 1 - t
```

### 3. Encode each theorem in the residue audit script

Use:

```text
scripts/reduction_residue_audit.py
```

A theorem should become one or more explicit rules such as:

```text
--range "p>=37,t=all,name=large_prime_theorem"
--range "p=29,t=13..20,name=medium_range_theorem"
--range "p=31,b=7..17,name=verified_witness_domain"
```

Only encode rules after the theorem statement is fully translated.

### 4. Run the audit

The desired audit output is:

```text
residue_not_certified = 0
```

or, more generally:

```text
residue is contained in verified finite domain
```

### 5. Record exact command and output

Every successful audit should be logged under:

```text
logs/
```

Recommended filename:

```text
logs/reduction_audit_final_pass.txt
```

The log should include:

```text
full command
coverage rules
residue count
comparison to verified finite domain
VERDICT
```

## Current risk points

### Risk 1: relying on placeholders

The current reduction audit uses placeholder assumptions until exact published theorem ranges are entered.

No complete-solution claim should be made from placeholder ranges.

### Risk 2: direct witnesses versus descent certificate

The p=29, |B|=3..7 and p=31, |B|=3..6 classes have a structured descent certificate.

Many additional classes are covered by direct witnesses, not by a branch-descent proof.

This is still valid for a finite check, but it should be described honestly:

```text
finite verification uses mixed certificate styles
```

### Risk 3: artifact storage

Large JSONL files are not committed. The repository currently stores concise logs, counts, and digests.

Before external review, decide whether to provide:

```text
compressed raw witness files
release artifacts
reproducible generation scripts
hash manifests
or regenerated-on-demand verification instructions
```

## Immediate next action

Find and enter the exact theorem statements in a source ledger.

Recommended next file:

```text
docs/source_theorem_ledger.md
```

Do not generate additional finite witnesses unless the analytic audit exposes new residue outside:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```
