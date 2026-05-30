# AI provenance and verification standard

Some documentation and code development in this repository used AI assistance.

This note records the intended trust model.

## Scope of AI assistance

AI assistance may have been used for:

```text
1. drafting documentation;
2. refactoring code;
3. generating test scaffolding;
4. proposing proof-engineering workflows;
5. organizing theorem and reduction ledgers.
```

AI assistance must not be treated as mathematical authority.

## Certificate standard

The intended finite-certificate claims are direct, machine-checkable witness-verification claims.

For each trusted finite certificate row, verifiers must check from the raw data:

```text
p is prime;
B subset F_p^*;
B is canonical under nonzero multiplicative scaling, when required;
final_order is a permutation of A = F_p^* \ B;
all nonempty partial sums of final_order are pairwise distinct modulo p;
declared canonical coverage is complete, when required.
```

A claim is not trusted because it was written by a human or by an AI system.  It is trusted only to the extent that independent verification code checks the stated finite object.

## Theorem-level standard

The repository does not currently claim a complete proof of Erdős 475.

Any future theorem-level claim requires:

```text
1. independently checkable finite witness artifacts;
2. Python and Rust verifier agreement;
3. hash-locked release artifacts;
4. a completed analytic residue inclusion;
5. synchronized claim-boundary documentation.
```

## External communication standard

Any issue or pull request submitted to an external repository should disclose AI assistance and should not describe this repository as a completed proof or solution.

Suggested wording:

```text
Some documentation and code development used AI assistance. The intended certificate claims are direct, machine-checkable witness-verification claims.
```
