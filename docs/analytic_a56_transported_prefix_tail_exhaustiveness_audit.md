# Analytic Audit: A56 Transported-Prefix/Tail Exhaustiveness

This note audits the A56 weighted normal-form test:

```text
transported-prefix/tail artifact vs genuine weighted core.
```

Claim boundary:

```text
This is a normal-form exhaustiveness audit.
It is not a proof of Erdős 475.
It clarifies exactly when the coefficient-2 term is removable by transported-prefix/tail substitution.
```

---

## Source files

Primary source:

```text
docs/analytic_weighted_signed_normal_forms_a56.md
```

Related classifier:

```text
scripts/classify_weighted_signed_normal_form.py
```

Weighted final draft:

```text
docs/final/F10_weighted_normal_form_cut_swap.md
docs/final/F11_weighted_cut_selection_extraction.md
```

---

## Problem

A56 classifies a relation:

```text
A + 2B + C = 0
```

as either:

```text
1. transported-prefix/tail artifact;
2. zero doubled-block collapse;
3. adjacent-pair zero reduction;
4. equal-outer reduction;
5. genuine weighted core.
```

The ambiguity is in item 1:

```text
When exactly is B a transported prefix/tail rather than a genuine doubled block?
```

This note gives a precise interval-containment criterion.

---

## Algebraic identity

Let a known containing block `D` decompose as:

```text
D = B T.
```

Then:

```text
2B + T = B + D.
```

Similarly, if:

```text
D = T B,
```

then:

```text
T + 2B = D + B.
```

These are exactly A56.1 and A56.2.

The doubled block `B` is removable only when the complementary block `T` occurs with coefficient `+1` in the same relation and `B T` or `T B` is a known transported/containing block whose total is already part of the local obstruction structure.

---

## Precise transported-prefix criterion

A relation:

```text
A + 2B + C = 0
```

is a transported-prefix artifact if there exists a known containing block:

```text
D = B T
```

such that one of the outer pieces is exactly the complementary tail:

```text
A = T
```

or

```text
C = T.
```

Then the weighted relation is rewritten as:

```text
2B + T + U = 0
```

where `U` is the other outer piece. Using:

```text
2B+T = B+D,
```

we obtain:

```text
B + D + U = 0.
```

This is a non-weighted zero-composite/equal-interval branch involving the transported block `D` and one copy of `B`.

### Required metadata

To assert transported-prefix, the proof must specify:

```text
1. the containing block D;
2. its decomposition D=B T;
3. which outer piece equals T;
4. why D is a known transported block in the local move.
```

Without all four items, the coefficient-2 term must remain classified as genuine weighted unless another A56 test applies.

---

## Precise transported-tail criterion

A relation:

```text
A + 2B + C = 0
```

is a transported-tail artifact if there exists a known containing block:

```text
D = T B
```

such that one of the outer pieces is exactly the complementary prefix:

```text
A = T
```

or

```text
C = T.
```

Then:

```text
T+2B+U=0
```

is rewritten by:

```text
T+2B = D+B,
```

so:

```text
D+B+U=0.
```

Again, this is non-weighted.

### Required metadata

To assert transported-tail, the proof must specify:

```text
1. the containing block D;
2. its decomposition D=T B;
3. which outer piece equals T;
4. why D is a known transported block in the local move.
```

---

## Exhaustiveness statement

For a displayed relation:

```text
A+2B+C=0,
```

with `A,B,C` consecutive active pieces, exactly one of the following applies.

### Case 1: containing-block certificate exists

There is a known transported/containing block `D` such that:

```text
D=B A,
D=B C,
D=A B,
or D=C B.
```

Then the relation is a transported-prefix/tail artifact and is non-weighted after rewriting.

### Case 2: no containing-block certificate exists

No local block in the move has total:

```text
B+A,
B+C,
A+B,
or C+B
```

available as a known transported block.

Then the coefficient `2B` cannot be removed by transported-prefix/tail substitution.

If W2--W4 also fail:

```text
B != 0,
A+B != 0,
B+C != 0,
A != C,
```

then the relation is a genuine weighted core.

---

## Non-examples

The following do **not** certify transported-prefix/tail status.

### Same numerical sum without interval provenance

If:

```text
sum(T)=sum(A)
```

but `T` is not the actual complementary interval completing `B` to a known transported block, then the proof cannot use A56.1/A56.2 as a structural rewrite.

It may be an equal-interval obstruction, but it is not a transported-prefix certificate.

### Complement exists geometrically but not in the relation

If `D=B T` exists geometrically but neither outer piece in:

```text
A+2B+C=0
```

is `T`, then the identity:

```text
2B+T=B+D
```

cannot be applied to the displayed relation.

### Complement is external without bridge control

If the complementary piece `T` lies outside the active local window, the branch is not an internal transported-prefix artifact. It is an external bridge/collision branch and must route through:

```text
F6/F8
```

with provenance retained.

---

## Relation to A56 examples

### A38 D5 proper-interior

A56 records that an apparent doubled prefix in A38 becomes:

```text
P+G+L=0.
```

This is transported-prefix because the apparent doubled piece is a prefix of a known block, and the complementary tail appears in the same relation.

### A49 E3

A56 records:

```text
G_j=A_i-2a
```

where the equal known block `C` plus `tail(A)` removes the coefficient-2 term:

```text
C+tail(A)+prefix(G)=0.
```

Here the containing-block certificate is the known equal/transported block from the local move.

### A55 midpoint

A56 records that:

```text
C_k=2a+Y_m
```

becomes:

```text
A+tail(C)+prefix(Y)=0.
```

Again, the coefficient-2 term is removable because one copy is replaced by a known equal block and the complementary tail appears.

---

## Classifier implication

The script:

```text
scripts/classify_weighted_signed_normal_form.py
```

currently uses Boolean flags:

```text
--transported-prefix,
--transported-tail.
```

This is acceptable as a symbolic classifier, but a proof audit must attach a certificate object:

```json
{
  "kind": "transported_prefix",
  "doubled_piece": "B",
  "containing_block": "D",
  "decomposition": "D = B T",
  "complement_piece": "T",
  "outer_piece_equal_to_complement": "A or C",
  "local_move_source": "A38/A49/A55/etc."
}
```

A future stronger classifier should accept this certificate rather than a bare Boolean.

---

## A56 Exhaustiveness Lemma

### Statement

For a relation:

```text
A+2B+C=0,
```

the coefficient-2 term is removable by transported-prefix/tail substitution if and only if there exists a containing-block certificate of one of the forms:

```text
D=B A,
D=B C,
D=A B,
D=C B,
```

where `D` is a known transported/containing block in the local move and the complementary piece occurs with coefficient `+1` in the displayed relation.

If no such certificate exists, then A56.1/A56.2 do not apply. The branch may still reduce by:

```text
B=0,
A+B=0,
B+C=0,
A=C,
```

but if these also fail, it is a genuine weighted core.

### Proof

The identities A56.1/A56.2 require exactly a decomposition of a known block into the doubled piece plus its complementary piece. If such a decomposition exists and the complement is present, substitution rewrites `2B+T` as `B+D` or `T+2B` as `D+B`. Conversely, without a known containing block and the complementary piece in the relation, there is no interval-provenance-preserving substitution that removes one copy of `B`; the coefficient `2B` remains genuinely weighted unless one of the endpoint collapse tests W2--W4 applies. ∎

---

## Impact on F10/F11

This audit reduces weighted blocker:

```text
W3. A56 transported-prefix/tail exhaustiveness.
```

New status:

```text
A56 transported-prefix/tail is exhaustive once a containing-block certificate model is adopted.
```

Remaining action:

```text
1. Patch A56 to require explicit containing-block certificates.
2. Patch F10/F11 to cite this audit.
3. Optionally upgrade classify_weighted_signed_normal_form.py to accept certificate metadata instead of bare Boolean flags.
```

---

## Remaining weighted blockers after this audit

```text
1. W-to-NW exit decrease/no-reentry table relative to weighted entry.
2. Final F9/F11 mutual-induction implementation.
3. A90--A94 minimal-path formalization.
4. Optional classifier upgrade for transported-prefix certificates.
```

---

## Current status

Closed here:

```text
1. exact transported-prefix criterion;
2. exact transported-tail criterion;
3. non-examples that do not count as transported artifacts;
4. proof that failure of containing-block certificate plus W2--W4 gives genuine weighted core.
```

Still not closed:

```text
1. global weighted termination;
2. W-to-NW decrease table;
3. finite certificate/residue bridge.
```
