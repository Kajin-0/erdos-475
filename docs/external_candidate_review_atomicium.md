# External candidate review: Atomicium graham-rearrangement-certificates

Repository reviewed:

```text
https://github.com/Atomicium-org/graham-rearrangement-certificates
```

## Bottom-line classification

This is not presently a complete accepted proof of Erdős Problem 475 / Graham's rearrangement conjecture.

It should be treated as:

```text
research draft / proof candidate with executable local certification
```

This is also the repository's own stated classification.

## Evidence from the repository itself

The README says the project is a `research draft / proof candidate with executable local certification`, not a formally accepted proof.  It explicitly says the remaining audit question is whether every mathematical branch in the manuscript necessarily produces a finite certificate accepted by the checkers.

The global executable certificate says the package certifies the finite local-certificate language used by the manuscript.  Its honest conditional statement is:

```text
If the manuscript produces, in every local branch, the prescribed finite certificates,
then this package checks that those certificates are routed according to the proof scheme.
```

The external review guide identifies the key bridge to audit:

```text
mathematical branch in the manuscript
    -> finite local certificate
    -> checker-accepted descent / classified exit / contraction
```

The roadmap lists strengthening the bridge from local mathematical cases to certificate objects as a next technical goal.

## Technical interpretation

The repository appears relevant and potentially useful.  Its proof architecture is close in spirit to this repository's finite-certificate approach: minimal counterexample, local bricks, potential descent, classified exits, and executable local checks.

However, the current package does not by itself establish that:

1. every branch in the handwritten manuscript is covered by a checker-accepted certificate;
2. the visible finite description loses no additive/cyclic information from the original mathematical object;
3. all classified exits are globally contradictory in the original problem;
4. no hidden infinitary assumption enters the finite-state graph;
5. the manuscript-to-certificate semantic bridge is complete.

Therefore it is not yet a replacement for a complete analytic proof.

## Useful audit targets

The strongest next use of this repository is not to re-run `scripts/run_all.sh` only.  The useful audit is to inspect the semantic bridge for the named local bricks:

```text
R
C0.3
H0-B+
U0simple
C0.1
C0.2
```

Priority questions:

1. Does `Vis` contain every datum used by the local predicates?
2. Is `Car(T)` computed only from explicit finite fields?
3. Can a branch depend on trace-shadow information not captured by the carrier?
4. Does perfect neutrality really imply a contractible segment?
5. Are the classified exits actually incompatible with a minimal counterexample?
6. Is the global reassembly from local exits to Graham's conjecture logically closed?

## Relation to this project

This external candidate should be treated as a source of proof ideas and possible local-brick templates.

It should not be cited as a complete solution unless and until the semantic bridge is independently audited or formalized.

## Status

```text
Relevant lead: yes
Complete proof: not established
Use for proof mining: yes
Use for final theorem claim: no
```
