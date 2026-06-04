# A92 support containment analysis

## Purpose

This document analyzes which W-to-NW exit table rows have NW1 support strictly contained within B, the precondition for the containment lemma that gives a strong local no-reentry certificate. It classifies each of the 22 exit rows by containment status and identifies which rows can use support containment as a certificate basis.

## Claim boundary

This document does not prove that any certificate exists, does not prove A92, does not close F11, does not close the F9/F11 mutual-induction interface, and does not prove Erdős 475. All classifications below are based on the existing W-to-NW exit table and F11/F10 extraction docs. Rows marked CONTAINED are candidates for a support-containment certificate but still require earlier-coordinate non-increase verification.

## Containment lemma (from W-to-NW table §3)

For a genuine weighted core A+2B+C=0 with m = |B|:

```text
|support(Wwin)| = |A|+|B|+|C| >= |B|+1 = m+1.
```

If support(NW1) ⊆ B, then:

```text
support_size(NW1) <= m < m+1 <= support_size(Wwin).
```

This gives support_size(NW1) < support_size(Wwin), which is a strong local decrease relative to Wwin. For a no-reentry certificate, this same inequality excludes re-entry to W(j) with j >= m because any such re-entry would require middle length j >= m, meaning |support(W(j))| >= j >= m, contradicting support_size(NW1) <= m when the candidate middle would need support inside NW1.

## Exit row classification

| #   | Exit type           | Source   | NW output class                   | Candidate coordinate               | Status       | Support ⊆ B?              | Basis                                               | Certificate potential              |
| --- | ------------------- | -------- | --------------------------------- | ---------------------------------- | ------------ | ------------------------- | --------------------------------------------------- | ---------------------------------- |
| E1  | B=0                 | A56 W1   | ZERO_COLLAPSE                     | terminal                           | GREEN        | N/A (terminal)            | Terminal — no certificate needed                    | N/A                                |
| E2  | A+B=0               | A56 W2L  | TWO_PIECE_ZERO                    | enclosing span or support          | YELLOW       | NO                        | Support is A∪B, extends outside B                   | None via containment               |
| E3  | B+C=0               | A56 W2R  | TWO_PIECE_ZERO                    | enclosing span or support          | YELLOW       | NO                        | Support is B∪C, extends outside B                   | None via containment               |
| E4  | A=C                 | A56 W3   | EQUAL_INTERVAL / SEPARATED_EQUAL  | type/gap after F5/F8               | ORANGE       | NO                        | Support is A∪B∪C = full Wwin                        | None via containment               |
| E5  | transported-prefix  | A56 W4   | zero/equal/signed                 | support/provenance                 | YELLOW       | NO                        | Transported-prefix involves A and part of B         | None via containment               |
| E6  | transported-tail    | A56 W4   | zero/equal/signed                 | support/provenance                 | YELLOW       | NO                        | Transported-tail involves C and part of B           | None via containment               |
| E7  | atom-middle (+,+)   | A81      | signed midpoint / pair-difference | support                            | YELLOW       | POSSIBLE                  | Boundary triple may be within B if A and C nonempty | Conditional — see atom-middle rows |
| E8  | atom-middle (+,-)   | A81      | bounded signed relation           | support                            | YELLOW       | POSSIBLE                  | Same as E7                                          | Conditional                        |
| E9  | atom-middle (-,+)   | A81      | two-atom zero                     | terminal/support                   | GREEN        | N/A (terminal or F4 zero) | Terminal or zero branch — no certificate needed     | N/A                                |
| E10 | atom-middle (-,-)   | A81      | signed midpoint / pair-difference | support                            | YELLOW       | POSSIBLE                  | Same as E7                                          | Conditional                        |
| E11 | A=empty atom-middle | A80/A81  | pair/signed/zero/midpoint         | support or recurrence              | YELLOW       | POSSIBLE                  | A empty: support inside B∪C; may overlap B only     | Conditional                        |
| E12 | C=empty atom-middle | A80/A81  | pair/signed/zero/midpoint         | support or recurrence              | YELLOW       | POSSIBLE                  | C empty: support inside A∪B; may overlap B only     | Conditional                        |
| E13 | R_k'=A_i            | A97.1    | zero-composite                    | support / span                     | YELLOW       | NO                        | R_k'=A_i gives zero-composite involving A atoms     | None via containment               |
| E14 | R_k'=C_l'           | A97.2    | zero-composite                    | support / span                     | YELLOW       | NO                        | R_k'=C_l' gives zero-composite involving C atoms    | None via containment               |
| E15 | R_k'=P_j'           | A97.3/6  | two-piece zero inside B           | support                            | GREEN/YELLOW | YES                       | Explicitly "two-piece zero inside B". Support ⊆ B.  | STRONG — best candidate            |
| E16 | P_j'=A_i            | A97.4    | zero-composite                    | support / span                     | YELLOW       | NO                        | P_j'=A_i involves A atoms outside B                 | None via containment               |
| E17 | P_j'=C_l'           | A97.5    | two-piece zero                    | support / span                     | YELLOW       | NO                        | P_j'=C_l' involves C atoms outside B                | None via containment               |
| E18 | R_k=P_j             | A97.7    | equal-prefix / separated-equal    | support inside B                   | YELLOW       | YES                       | Explicitly "support inside B". Support ⊆ B.         | STRONG — good candidate            |
| E19 | R_k^+=P_j^+         | A97.8    | equal-tail / separated-equal      | support inside B                   | YELLOW       | YES                       | Explicitly "support inside B". Support ⊆ B.         | STRONG — good candidate            |
| E20 | x+a+R_k=f           | A97.9/F7 | forbidden recurrence              | enclosing span via bounded blocker | YELLOW       | NO                        | Recurrence — support includes external endpoints    | None via containment               |
| E21 | x+a+r+P_j=f         | A97.9/F7 | forbidden recurrence              | enclosing span via bounded blocker | YELLOW       | NO                        | Recurrence — support includes external endpoints    | None via containment               |
| E22 | external collision  | F10/F6   | multiple F6 classes               | via F6/F8/F4/F5/F7                 | YELLOW       | NO                        | External collision — support extends outside Wwin   | None via containment               |

## Summary

| Category                           | Rows                                                  | Count |
| ---------------------------------- | ----------------------------------------------------- | ----- |
| Terminal (no certificate needed)   | E1, E9                                                | 2     |
| Support strictly ⊆ B confirmed     | E15, E18, E19                                         | 3     |
| Support possibly ⊆ B (conditional) | E7, E8, E10, E11, E12                                 | 5     |
| Support NOT ⊆ B                    | E2, E3, E4, E5, E6, E13, E14, E16, E17, E20, E21, E22 | 12    |

## Confirmed containment rows

### E15 — R_k'=P_j' (two-piece zero inside B)

**Source**: A97.3/6. The equation R_k' = P_j' means the right endpoint of R equals an internal endpoint of P. The collision produces a two-piece zero relation. Since both P and R are proper subblocks of B, the output support is contained entirely inside B.

**Explicit doc statement**: "two-piece zero inside B" with status "GREEN if strict inside B."

**Containment**: support(NW1) ⊆ B.

**Bound**: support_size(NW1) <= |P_j' atoms| <= |P| < m. Therefore strict: support_size(NW1) < support_size(Wwin) and support_size(NW1) < m.

**For no-reentry**: any later W(j) with j >= m would need at least m atoms of support that NW1 cannot provide (its support is strictly smaller than m in the strict-inside-B case). Same-middle j=m requires exact support_size >= m which is impossible. Larger j>m also impossible.

### E18 — R_k=P_j (equal-prefix / separated-equal, support inside B)

**Source**: A97.7. The moved R endpoint equals an old P endpoint. This produces an equal-prefix relation. Since R and P are both subblocks of B, the equal-prefix support is contained inside B.

**Explicit doc statement**: "equal-prefix / separated-equal, support inside B."

**Containment**: support(NW1) ⊆ B.

**Bound**: support_size(NW1) <= |B| = m. The bound is support_size(NW1) <= m (not strictly < m). However, the containment lemma requires support(NW1) ⊆ B, giving support_size(NW1) <= m < m+1 <= support_size(Wwin), which is a strict inequality relative to Wwin but not automatically strict relative to m itself.

**For no-reentry**: j = m case (same-middle) needs special handling: if support_size(NW1) = m and contains all of B's atoms, the same-middle return is not ruled out by support containment alone — it requires pattern-rigidity impossibility (A89/F11.7). For j > m, support_size(NW1) <= m < j blocks it.

### E19 — R_k^+=P_j^+ (equal-tail / separated-equal, support inside B)

**Source**: A97.8. The moved P endpoint equals an old R endpoint. This produces an equal-tail relation. Symmetric to E18.

**Explicit doc statement**: "equal-tail / separated-equal, support inside B."

**Containment**: support(NW1) ⊆ B.

**Bound**: same as E18: support_size(NW1) <= m.

**For no-reentry**: same analysis as E18. Same-middle (j=m) requires A89. Larger j blocked by support_size.

## Conditional containment rows

### E7, E8, E10 — atom-middle sign patterns

**Containment**: Conditional on the boundary triple being fully within B. For the atom-middle case |B|=1. The sign patterns (+,+), (+,-), (-,-) involve A, the single B atom, and C. The output is a signed midpoint or pair-difference whose support may include atoms from A or C.

**When support ⊆ B**: Only if the boundary interaction is strictly between the B atom and endpoints of A/C that resolve entirely within the B interval (i.e., the overlapping atoms are all inside B). Not guaranteed.

### E11 (A=empty), E12 (C=empty)

**Containment**: When A is empty (E11), the weighted window is (empty) B C. The atom-middle output may have support inside B∪C. For strict containment within B, the output must not use C atoms. Not guaranteed.

## Rows needing other certificate bases

12 rows (E2-E6, E13, E14, E16, E17, E20-E22) have support NOT contained in B. For these, the support-containment exclusion basis does not apply. They require one of:

- Proof that M_NW\*(NW1) < M_NW\*(NW0) directly (the NONWEIGHTED_DECREASE output classification)
- A different exclusion basis (span decrease, boundary-rank obstruction, type-rank obstruction, routing incompatibility)
- Routing to a smaller weighted return (WEIGHTED_DESCENT)

## Certificate-eligible rows

The 3 confirmed containment rows (E15, E18, E19) are the best candidates for a support-containment no-reentry certificate. For these rows, the certificate would need:

1. Proof that support(NW1) ⊆ B (already stated in docs for these rows).
2. Application of the containment lemma: support_size(NW1) <= m < m+1 <= support_size(Wwin).
3. For same-middle (j=m): additional invocation of A89/F11.7 to rule out pattern-rigid return.
4. Verification that earlier M_NW\* coordinates (enclosing_span, gap_length) do not increase.

Rows E7/E8/E10/E11/E12 are conditional — they would need per-row analysis to confirm support containment.

## Row-specific containment details

| Row | Why support ⊆ B or not | Detailed reasoning                                                                                                                                                                       |
| --- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| E2  | NO                     | A+B=0 means NW1 is a TWO_PIECE_ZERO from A and B. Support includes A atoms outside B. Even if A is partly contained in B (prefix case), the full A block extends left of B.              |
| E3  | NO                     | Symmetric — B+C=0 involves C atoms outside B.                                                                                                                                            |
| E4  | NO                     | A=C means outer blocks are equal. The EQUAL_INTERVAL output has support A∪B∪C = full Wwin.                                                                                               |
| E5  | NO                     | Transported-prefix: a prefix of B is absorbed into a containing block D (which may include A). Support includes D, not just B.                                                           |
| E6  | NO                     | Transported-tail: symmetric — a suffix of B is absorbed into a containing block including C.                                                                                             |
| E13 | NO                     | R_k'=A_i: R_k' is in the moved R block (a subblock of R ⊆ B), but A_i is in A (outside B). The zero-composite equation links atoms from B and A, so output support crosses the boundary. |
| E14 | NO                     | R_k'=C_l': symmetric — links B and C atoms.                                                                                                                                              |
| E15 | YES                    | R_k'=P_j': both R_k' and P_j' are internal to B (R ⊆ B, P ⊆ B). The two-piece zero is contained entirely inside B.                                                                       |
| E16 | NO                     | P_j'=A_i: P_j' is inside B (P ⊆ B) but A_i is in A. Cross-boundary.                                                                                                                      |
| E17 | NO                     | P_j'=C_l': P_j' is inside B but C_l' is in C. Cross-boundary.                                                                                                                            |
| E18 | YES                    | R_k=P_j: the moved R endpoint equals an old P endpoint. Both R and P are subblocks of B. The equal-prefix support is inside B.                                                           |
| E19 | YES                    | R_k^+=P_j^+: symmetric to E18 — equal-tail support is inside B.                                                                                                                          |
| E20 | NO                     | Forbidden recurrence: x+a+R_k=f involves external endpoints x, a (from A), R_k (from R ⊆ B). Support extends to external atoms.                                                          |
| E21 | NO                     | x+a+r+P_j=f: involves x, a (from A), r (from R ⊆ B), P_j (from P ⊆ B). External.                                                                                                         |
| E22 | NO                     | External collision: collision with endpoints outside the displayed window. Support is outside Wwin entirely.                                                                             |

## Next recommended small task

Create no-reentry certificate instances for E15, E18, and E19 using the support-containment basis template. These are the three rows where containment is already documented and the certificate structure is simplest.
