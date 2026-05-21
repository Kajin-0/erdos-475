# Submission/publication target: teorth/erdosproblems

Repository:

```text
https://github.com/teorth/erdosproblems
```

## Why this matters

This repository is a community-maintained database for the problems on `erdosproblems.com`.  It is maintained by Thomas Bloom and Terence Tao, and its generated table is based on the YAML file:

```text
data/problems.yaml
```

The README says that `data/problems.yaml` is the ground truth for the table and that proposed changes should be made by opening a pull request editing that file.

## Current Problem 475 entry observed

As of the inspected `main` branch, Problem 475 is recorded as:

```yaml
- number: "475"
  prize: "no"
  status:
    state: "decidable"
    last_update: "2026-02-23"
  oeis: ["N/A"]
  formalized:
    state: "no"
    last_update: "2025-08-31"
  tags: ["number theory", "additive combinatorics"]
```

This status is consistent with the current research situation: the problem has substantial finite/computational structure, but the analytic proof must be fully closed before proposing `proved`.

## Contribution path

The contributing guide says to edit `data/problems.yaml`, open a pull request, and describe methodology / links to code in the PR comment.  It also says mathematical discussion should generally happen on the corresponding `erdosproblems.com` problem page, while GitHub issues are mainly for database-entry matters.

## How to use this target later

Do **not** open a PR claiming `proved` until we have one of the following:

1. a complete accepted analytic proof;
2. a complete formal proof;
3. a complete and independently auditable finite reduction + certificate package covering every residual case with no semantic gap.

If/when the proof is complete, the likely PR diff is:

```yaml
- number: "475"
  prize: "no"
  status:
    state: "proved"
    last_update: "YYYY-MM-DD"
  oeis: ["N/A"]
  formalized:
    state: "no"
    last_update: "2025-08-31"
  comments: "Graham's rearrangement conjecture; proof/certificate package: <link>"
  tags: ["number theory", "additive combinatorics"]
```

If the result is only a finite/computational completion under known reductions, avoid saying `proved`; instead propose a comment update describing the verified finite domain and cite the certificate repository.

## Immediate use for this project

This repository is useful as:

```text
1. a status benchmark;
2. an eventual public update target;
3. a place to identify formalization / Lean status;
4. a place to compare terminology and external references.
```

It is not a substitute for proving the remaining analytic obstruction lemmas in this repository.
