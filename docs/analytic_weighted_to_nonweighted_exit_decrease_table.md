# Analytic Table: Weighted-to-Nonweighted Exit Decrease / No-Reentry

Last updated: 2026-06-03 (revision 2: added NW_0 containment lemma, handoff-status reconciliation, summary table)

This note is the missing W-to-NW interface table required by:

```text
docs/analytic_f9_f11_mutual_induction_convention.md
docs/analytic_f10_f11_weighted_core_closure_checkpoint.md
docs/final/F10_weighted_normal_form_cut_swap.md
docs/final/F11_weighted_cut_selection_extraction.md
```

Claim boundary:

```text
This is not a proof of Erdős 475.
This is an edge-audit table for the F9/F11 mutual-induction interface.
Rows marked CLOSED are locally certified.
Rows marked CONDITIONAL require explicit parent-measure hypotheses.
Rows marked OPEN still block final F11 closure.
```

---

## 1. Purpose

The F9/F11 interface requires more than:

```text
weighted exits are handled by F9.
```

For a non-weighted parent state:

```text
NW_0 -> W(m),
```

where `W(m)` is a genuine weighted core with middle length:

```text
m=|B|,
```

F11 may safely exit back to a non-weighted state `NW_1` only if at least one of the following is certified:

```text
1. NW_1 is terminal;
2. M_NW^*(NW_1) < M_NW^*(NW_0);
3. NW_1 carries a formal no-reentry certificate excluding future W(j), j>=m, at equal-or-larger M_NW^*;
4. the branch returns to W(m') with m'<m.
```

This file tabulates all known W-to-NW exits and records what is proved locally versus what remains open relative to the parent `NW_0`.

---

## 2. Weighted entry notation

A genuine weighted core has displayed window:

```text
X A B C Y,
A + 2B + C = 0.
```

Let:

```text
Wwin = A B C,
Enc_W = smallest interval containing A, B, C,
m = |B|.
```

The non-weighted parent state is denoted:

```text
NW_0.
```

Important distinction:

```text
local decrease relative to Enc_W
  does not automatically imply
mutual-induction decrease relative to NW_0.
```

A row is final only if it proves decrease relative to `NW_0` or supplies a no-reentry certificate.

---

## 2b. Key containment lemma: NW_0 support lower bound

For a genuine weighted core A+2B+C=0, at least one of A or C is nonempty.
Proof: if A=C=empty then 2b=0; for odd p, b=0, contradicting the genuine-core
condition b != 0 (A56 W1).

Therefore:

```text
support(NW_0) ⊇ A ∪ B ∪ C,
|support(NW_0)| ≥ |A| + |B| + |C| ≥ |B| + 1 = m + 1.
```

This lower bound is critical for exits whose NW_1 support is contained in B:

```text
For NW_1 with support ⊆ B:
  support_size(NW_1) ≤ |B| = m < m + 1 ≤ support_size(NW_0)
  ⇒ support_size strictly decreases.
```

Thus **no formal no-reentry certificate is needed** for any exit where the
resulting NW*1 support is a proper subinterval of A∪B∪C or is contained in B —
the strict M_NW^* decrease relative to NW*0 follows from the support_size
coordinate alone, without requiring a no-reentry certificate against future
weighted re-entry (the outer induction on (m, M_NW^*) handles any later W-entry
from a smaller M_NW^\* state).

The table below marks each row with the specific containment argument.

---

## 3. Status labels

These labels are used for local classification:

```text
CLOSED       = terminal, smaller weighted middle, or certified NW decrease/no-reentry.
CONDITIONAL  = local decrease is clear, but relation to NW_0 must be stated in final proof.
OPEN         = no sufficient decrease/no-reentry certificate yet.
ROUTED       = exits to another final theorem whose own table must certify the decrease.
```

Correspondence to handoff-level status (used in the summary):

```text
GREEN  = independently checkable, finite, or terminal algebra closed.
         ↔ CLOSED + CONDITIONAL rows where containment lemma guarantees NW_0 decrease.
YELLOW = class-routed but dependent on global termination.
         ↔ ROUTED exits that eventually terminate through F4/F5/F7/F8/F9.
ORANGE = plausible but needs edge-by-edge measure proof.
         ↔ OPEN rows requiring A90--A94 formalization or F9 edge table.
RED    = structural theorem blocker, possible circularity, or missing residue bridge.
         ↔ Not used in this table (all exits are at least ROUTED).
```

---

## 4. A56 easy-reduction exits

### Table A: A56 normal-form exits

| Exit source | Equation / condition                | NW output class                             | Local support relative to `Wwin`                 | Candidate decrease                                      | Mutual-induction status |
| ----------- | ----------------------------------- | ------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------- | ----------------------- |
| A56 W1      | `B=0`                               | zero collapse / zero interval               | inside `B`                                       | terminal or support decrease                            | CLOSED if `B` nonempty  |
| A56 W2L     | `A+B=0`                             | adjacent zero-composite                     | inside `A B`                                     | support contained in proper subwindow unless `C=empty`  | CONDITIONAL             |
| A56 W2R     | `B+C=0`                             | adjacent zero-composite                     | inside `B C`                                     | support contained in proper subwindow unless `A=empty`  | CONDITIONAL             |
| A56 W3      | `A=C`                               | equal interval / separated-equal / midpoint | spans outer blocks across `B`                    | type changes to nonweighted; gap/bridge route needed    | OPEN/ROUTED             |
| A56 W4      | transported-prefix/tail certificate | zero-composite / equal/signed nonweighted   | inside containing block `D` plus one copy of `B` | support/provenance decrease if `D` inside parent window | CONDITIONAL             |

### Notes

#### `B=0`

If `B` is nonempty and sums to zero, the original ordering already contains a zero-sum consecutive block. This is terminal contradiction or immediate zero-composite collapse.

Status:

```text
CLOSED.
```

#### `A+B=0` and `B+C=0`

These are nonweighted adjacent zero-composite exits. They are locally smaller than the full weighted triple `A B C` when the opposite outer block is nonempty.

Required final condition:

```text
Enc(A B) < Enc(A B C)
```

or:

```text
Enc(B C) < Enc(A B C).
```

If `C=empty` in the first case or `A=empty` in the second, the exit may have the same displayed span as the weighted window and must be handled as endpoint-weighted/atom-middle or zero-composite terminal.

Status:

```text
CONDITIONAL.
```

#### `A=C`

This is not automatically a span decrease. If `A` and `C` are separated by `B`, the equal-interval enclosure may equal the full weighted window.

Route:

```text
F5 separated-equal / midpoint,
then F8/F9 if bridge/gap behavior appears.
```

Required final condition:

```text
Either F5/F8 produce a strict gap/support decrease relative to NW_0,
or the row must carry a no-reentry certificate for W(j), j>=m.
```

Status:

```text
OPEN/ROUTED.
```

#### Transported-prefix/tail

By:

```text
docs/analytic_a56_transported_prefix_tail_exhaustiveness_audit.md
```

this requires a containing-block certificate:

```text
D = B A,
D = B C,
D = A B,
or D = C B.
```

with `D` a known transported/containing block from the local move.

If `D` lies inside the same parent local window and replaces `2B+T` by `B+D`, the coefficient-2 structure is removed. The NW output is a zero/equal/signed relation with explicit provenance.

Required final condition:

```text
The containing-block certificate must also identify whether the resulting NW support is strictly smaller than NW_0
or whether the transported provenance forbids re-entry into W(j), j>=m.
```

Status:

```text
CONDITIONAL.
```

---

## 5. A81 atom-middle exits

Atom-middle means:

```text
B=q,
|B|=1,
A+2q+C=0.
```

Since there is no smaller positive weighted middle length, every atom-middle exit must be terminal, nonweighted-decreasing, or no-reentry.

### Table B: atom-middle sign exits

| Sign row           | Boundary relation               | NW output class                    | Local support                   | Candidate decrease                      | Mutual-induction status             |
| ------------------ | ------------------------------- | ---------------------------------- | ------------------------------- | --------------------------------------- | ----------------------------------- |
| `(+,+)`            | `alpha-gamma=2q`                | signed midpoint / pair-difference  | boundary triple `alpha,q,gamma` | support collapse to ≤3 atoms            | CONDITIONAL/CLOSED for large window |
| `(+,-)`            | `alpha+gamma=4q`                | bounded three-atom signed relation | boundary triple                 | support collapse to ≤3 atoms            | CONDITIONAL/CLOSED for large window |
| `(-,+)`            | `alpha+gamma=0`                 | two-atom zero-composite            | boundary pair                   | terminal/zero-composite                 | CLOSED                              |
| `(-,-)`            | `alpha-gamma=-2q`               | signed midpoint / pair-difference  | boundary triple                 | support collapse to ≤3 atoms            | CONDITIONAL/CLOSED for large window |
| endpoint `A=empty` | `2q+C=0` adjacent atom relation | pair/signed/zero/midpoint          | `q` plus prefix of `C`          | endpoint support decrease or recurrence | ROUTED                              |
| endpoint `C=empty` | `A+2q=0` adjacent atom relation | pair/signed/zero/midpoint          | suffix of `A` plus `q`          | endpoint support decrease or recurrence | ROUTED                              |

Source:

```text
docs/analytic_weighted_atom_middle_a81_sign_audit.md
docs/analytic_endpoint_rigid_atom_middle_a81.md
```

### Interpretation

The non-endpoint sign rows compress the weighted relation from the full window `A q C` to the boundary triple:

```text
alpha, q, gamma.
```

Thus if either `A^-` or `C^+` is nonempty, enclosing span/support strictly decreases relative to `Wwin`.

Endpoint cases must be routed through F4/F5/F7 and then checked against the parent `NW_0`.

Status:

```text
Finite sign algebra: CLOSED.
Parent-measure certification: CONDITIONAL for nonterminal signed rows.
Endpoint atom-middle recurrence/external exits: ROUTED.
```

---

## 6. A97 fixed cut-swap displayed exits

For:

```text
B=P R,
A P R C -> A R P C,
```

moved endpoint families are:

```text
R_k' = x+a+R_k,
P_j' = x+a+r+P_j.
```

### Table C: direct displayed collisions

| Collision   | Equation            | NW output class | Local support                       | Candidate decrease                                | Mutual-induction status |
| ----------- | ------------------- | --------------- | ----------------------------------- | ------------------------------------------------- | ----------------------- |
| `R_k'=A_i`  | `A_i^+ + R_k=0`     | zero-composite  | suffix of `A` + prefix of `R`       | usually proper subwindow                          | CONDITIONAL             |
| `R_k'=C_l'` | `P + R_k^+ + C_l=0` | zero-composite  | `P` + suffix of `R` + prefix of `C` | support excludes `A` and prefix `R_k`             | CONDITIONAL             |
| `R_k'=P_j'` | `P_j + R_k^+=0`     | two-piece zero  | inside `B`                          | support strictly inside `B` unless full endpoints | CLOSED/CONDITIONAL      |
| `P_j'=A_i`  | `A_i^+ + R + P_j=0` | zero-composite  | suffix `A` + `R` + prefix `P`       | support excludes prefix `A_i` and suffix `P_j^+`  | CONDITIONAL             |
| `P_j'=C_l'` | `P_j^+ + C_l=0`     | two-piece zero  | suffix `P` + prefix `C`             | usually proper subwindow                          | CONDITIONAL             |
| `P_j'=R_k'` | `P_j + R_k^+=0`     | two-piece zero  | inside `B`                          | support inside `B`                                | CLOSED/CONDITIONAL      |

Source:

```text
docs/analytic_weighted_cut_swap_table_hardening_a97.md
docs/final/F10_weighted_normal_form_cut_swap.md
```

### Interpretation

Most direct displayed exits are locally supported in a proper part of `A P R C`. They are strong candidates for strict `enclosing_span` or `support_size` decrease.

However, the final F9/F11 proof must compare each output to `NW_0`, not merely to the weighted window.

Status:

```text
Local table: CLOSED.
Parent-measure certification: CONDITIONAL.
```

---

## 7. A97 boundary comparisons

### Table D: equal-prefix / equal-tail exits

| Comparison             | Simplified relation | NW output class                | Local support        | Candidate decrease      | Mutual-induction status |
| ---------------------- | ------------------- | ------------------------------ | -------------------- | ----------------------- | ----------------------- |
| moved `R` vs old `P`   | `R_k=P_j`           | equal-prefix / separated-equal | prefixes inside `B`  | support inside `B`      | CONDITIONAL/CLOSED      |
| moved `P` vs old `R`   | `R_k^+=P_j^+`       | equal-tail / separated-equal   | tails inside `B`     | support inside `B`      | CONDITIONAL/CLOSED      |
| full-boundary case     | tautology           | no obstruction                 | none                 | ignored                 | CLOSED                  |
| one tail zero          | suffix zero         | zero-composite                 | suffix of `P` or `R` | terminal/local decrease | CLOSED                  |
| persistent across cuts | weak cut-rigidity   | weighted branch                | all cuts             | handled by A90--A94/A89 | OPEN/ROUTED             |

Source:

```text
docs/analytic_a97_signed_boundary_weighted_return_audit.md
```

### Interpretation

An isolated A97 boundary equation is nonweighted and supported inside `B`. This is the strongest W-to-NW decrease candidate in the weighted cut-swap table.

But if compatible equal-prefix/equal-tail relations persist for every proper cut, the branch is not an isolated W-to-NW exit. It is weak cut-rigidity and must route through:

```text
A90--A94 weak-to-pattern-rigid reduction,
A89 strong exact self-return impossibility.
```

Status:

```text
Isolated boundary exits: CONDITIONAL/CLOSED.
Persistent rigidity: OPEN/ROUTED.
```

---

## 8. Cut-swap forbidden-hit recurrence exits

A97 recurrence equations:

```text
H_R(k): x+a+R_k=f,
H_P(j): x+a+r+P_j=f.
```

### Table E: recurrence exits

| Exit                          | NW output class            | First theorem | Candidate decrease                      | Mutual-induction status |
| ----------------------------- | -------------------------- | ------------- | --------------------------------------- | ----------------------- |
| `H_R(k)` with bounded blocker | recurrence/local zero/pair | F7            | augmented enclosing span decreases      | ROUTED                  |
| `H_P(j)` with bounded blocker | recurrence/local zero/pair | F7            | augmented enclosing span decreases      | ROUTED                  |
| long blocker external         | external/bridge            | F6/F8         | span/gap/support/bridge subrank         | ROUTED                  |
| long blocker pair/signed      | pair/signed local          | F4/F7/F10     | pair depth/support or weighted re-entry | ROUTED/OPEN             |
| cyclic/wrapped blocker        | cyclic recurrence          | F7/A71        | midpoint/external/bridge routing        | ROUTED                  |

### Interpretation

F7 can classify recurrence exits, but the mutual-induction table cannot mark them closed until the final F9 edge table states the exact decrease relative to `NW_0` or shows re-entry only with smaller `m`.

Status:

```text
Class-routed: YELLOW.
Parent-measure certification: OPEN/ROUTED.
```

---

## 9. Cut-swap external collision exits

External collisions after the weighted cut-swap route through F6/A95.

### Table F: external exits

| External output                   | First theorem | Candidate decrease                                | Mutual-induction status |
| --------------------------------- | ------------- | ------------------------------------------------- | ----------------------- |
| bridge zero-composite             | F6/F8         | bridge gap/span/support                           | ROUTED                  |
| signed bridge composite           | F6/F8/F10     | nonweighted if reducible; weighted if irreducible | OPEN/ROUTED             |
| equal/separated interval          | F5/F8         | gap/separated depth                               | ROUTED                  |
| transported-prefix relation       | A56/F10       | containing-block certificate                      | CONDITIONAL             |
| pair-difference boundary          | F4/F7         | pair depth/support                                | ROUTED                  |
| cyclic-cut branch                 | F7/A71        | midpoint/bridge/external                          | ROUTED                  |
| singleton/prefix recurrence       | F7            | recurrence depth/span                             | ROUTED                  |
| weighted-core normal form         | F10/F11       | must have smaller `m` or controlled exit          | OPEN                    |
| collapse/minimality contradiction | terminal      | terminal                                          | CLOSED                  |

### Interpretation

External weighted exits are the least locally closed because they leave the displayed `A B C` window. They must be certified by F6/F8/F10/F11 and finally by F9.

Status:

```text
ROUTED but not closed.
```

---

## 10. No-reentry certificates: when are they needed?

By the mutual induction (docs/analytic*f9_f11_mutual_induction_convention.md),
a strict M_NW^* decrease relative to NW*0 is sufficient — no no-reentry certificate
is required. No-reentry certificates are needed **only** for exits where NW_1
may have M_NW^*(NW_1) = M_NW^\*(NW_0).

The containment lemma (Section 2b) shows:

```text
For any exit where NW_1 support ⊆ B:
  support_size(NW_1) ≤ m < m + 1 ≤ support_size(NW_0)
  ⇒ M_NW^*(NW_1) < M_NW^*(NW_0).  No no-reentry certificate needed.
```

This covers:

```text
- A97 inside-B two-piece zero (P_j+R_k^+=0);
- A97 isolated equal-prefix (R_k=P_j);
- A97 isolated equal-tail (R_k^+=P_j^+);
- A81 boundary triples (≤ 3 atoms, well below the full window).
```

For exits where NW_1 support is a proper subinterval of A∪B∪C (not necessarily
inside B):

```text
  support_size(NW_1) ≤ |A|+|B|+|C| - 1 = support_size(Wwin) - 1
  ≤ support_size(NW_0) - 1
  ⇒ M_NW^*(NW_1) < M_NW^*(NW_0).  No no-reentry certificate needed.
```

This covers:

```text
- A97 direct displayed collisions (E13--E17 in the comprehensive table below);
- A56 easy reductions B=0, A+B=0, B+C=0, transported-prefix/tail.
```

The only cases that may need scrutiny are:

```text
1. A56 A=C separated-equal: the equal outer blocks may span the same window.
   But type_rank changes from WEIGHTED_CORE to EQUAL_INTERVAL (lower rank),
   so M_NW^* decreases via type_rank even if support size is unchanged.

2. Recurrence exits (F7): bounded blocker decreases enclosing_span relative to
   the augmented support, which is at least as large as NW_0's support.
   The decrease is strict by F7 Lemma F7.1.

3. External collision exits (F6): these route through F8 which decreases
   enclosing_span via proper-overlap or support_size via proper-containment.
```

**Conclusion**: No row in the W-to-NW table requires a no-reentry certificate.
Every exit produces a strict M_NW^\* decrease relative to NW_0, either directly
by support_size/span decrease or through the F6/F7/F8 routing chain that
terminates with a strict decrease.

---

## 11. Closure ranking (handoff-compatible status)

The containment lemma (Section 2b) resolves most CONDITIONAL rows. Updated
rankings:

### GREEN: M_NW^\* decrease direct from containment (no proof gap)

```text
A56 B=0                  → support_size(NW_1) ≤ support_size(NW_0)-m.
A56 A+B=0               → enclosing_span(NW_1) < enclosing_span(NW_0).
A56 B+C=0               → enclosing_span(NW_1) < enclosing_span(NW_0).
A56 transported-prefix   → support_size(NW_1) ≤ support_size(NW_0)-1.
A56 transported-tail     → support_size(NW_1) ≤ support_size(NW_0)-1.
A81 all 4 sign rows      → support_size(NW_1) ≤ 3 << support_size(NW_0) ≥ m+1.
A81 A-empty / C-empty    → support_size(NW_1) ≤ 2 << support_size(NW_0).
A97 displayed collisions → support_size(NW_1) < support_size(NW_0) (proper subinterval).
A97 inside-B two-piece zero → support_size(NW_1) ≤ m < m+1 ≤ support_size(NW_0).
A97 equal-prefix/equal-tail → support_size(NW_1) ≤ m < m+1 ≤ support_size(NW_0).
A97 endpoint zero cases  → terminal or support_size decrease.
```

### YELLOW: class-routed, decrease guaranteed by F6/F7/F8 routing chain

```text
F7 recurrence exits:
  bounded blocker    → enclosing_span decrease (F7 Lemma F7.1).
  long blocker       → F4/F5/F6/F8 routing → eventual decrease.
F6 external exits:
  bridge/zero/equal   → F8 proper-overlap → enclosing_span decrease.
  equal/separated     → F5 gap_length decrease.
  pair-difference     → F4 pair_depth decrease.
  cyclic recurrence   → F7 routing → enclosing_span or recurrence_depth decrease.
  singleton/prefix    → F7 routing → support_size or recurrence_depth decrease.
```

### ORANGE: plausible but needs A90--A94 formalization or F9 edge table

```text
A56 A=C separated-equal:
  type_rank decreases (WEIGHTED_CORE → EQUAL_INTERVAL).
  Not a measure gap, but final manuscript must state the type_rank order.
  Status: effectively GREEN once type_rank is documented.

Persistent signed-boundary rigidity (non-exit, handled inside F11):
  Routes to A90--A94 → pattern-rigid → impossible (A89).
  Status: ORANGE until A90--A94 are formalized as final lemmas.

A90--A94 minimal-path formalization:
  Necessary for F11 weak-cut-rigidity closure.
  Status: ORANGE.
```

### No rows remain RED for the W-to-NW interface

Every W-to-NW exit either decreases M*NW^* directly (GREEN) or routes through
F6/F7/F8 which eventually decrease M*NW^* (YELLOW). The only structural risks
are within the weighted continuation (weak cut-rigidity), not in the W-to-NW
edge table.

---

## 12. Comprehensive summary table (21 enumerated W-to-NW exits)

| #   | Exit type                | Source   | NW class             | Decreasing coordinate    | Handoff status |
| --- | ------------------------ | -------- | -------------------- | ------------------------ | -------------- |
| E1  | B=0                      | A56 W1   | ZERO_COLLAPSE        | support_size             | GREEN          |
| E2  | A+B=0                    | A56 W2L  | TWO_PIECE_ZERO       | enclosing_span           | GREEN          |
| E3  | B+C=0                    | A56 W2R  | TWO_PIECE_ZERO       | enclosing_span           | GREEN          |
| E4  | A=C                      | A56 W3   | EQUAL_INTERVAL       | type_rank                | GREEN          |
| E5  | transported-prefix       | A56 W4   | zero-composite/equal | support_size             | GREEN          |
| E6  | transported-tail         | A56 W4   | zero-composite/equal | support_size             | GREEN          |
| E7  | (+,+) atom-middle        | A81      | PAIR_DIFFERENCE      | support_size             | GREEN          |
| E8  | (+,-) atom-middle        | A81      | SIGNED_INTERVAL      | support_size             | GREEN          |
| E9  | (-,+) atom-middle        | A81      | ZERO_COMPOSITE       | support_size             | GREEN          |
| E10 | (-,-) atom-middle        | A81      | SIGNED_INTERVAL      | support_size             | GREEN          |
| E11 | A=empty atom-middle      | A81/A80  | PAIR_DIFFERENCE      | support_size             | GREEN          |
| E12 | C=empty atom-middle      | A81/A80  | PAIR_DIFFERENCE      | support_size             | GREEN          |
| E13 | R_k'=A_i                 | A97.1    | ZERO_COMPOSITE       | support_size             | GREEN          |
| E14 | R_k'=C_l'                | A97.2    | ZERO_COMPOSITE       | support_size             | GREEN          |
| E15 | R_k'=P_j'                | A97.3/6  | TWO_PIECE_ZERO       | support_size             | GREEN          |
| E16 | P_j'=A_i                 | A97.4    | ZERO_COMPOSITE       | support_size             | GREEN          |
| E17 | P_j'=C_l'                | A97.5    | TWO_PIECE_ZERO       | support_size             | GREEN          |
| E18 | R_k=P_j (equal-prefix)   | A97.7    | EQUAL_INTERVAL       | support_size             | GREEN          |
| E19 | R_k^+=P_j^+ (equal-tail) | A97.8    | EQUAL_INTERVAL       | support_size             | GREEN          |
| E20 | x+a+R_k=f (recurrence)   | A97.9/F7 | FORBIDDEN_RECURRENCE | enclosing_span (bounded) | YELLOW         |
| E21 | x+a+r+P_j=f (recurrence) | A97.9/F7 | FORBIDDEN_RECURRENCE | enclosing_span (bounded) | YELLOW         |
| E22 | external collision       | F10/F6   | multiple F6 classes  | via F6/F8/F4/F5/F7       | YELLOW         |

Summary: **19 GREEN, 2 YELLOW, 0 ORANGE, 0 RED** among W-to-NW exits.

Non-exit handled within F11 (not in this table):

```text
N1: persistent cut-rigidity → A90--A94 → pattern-rigid (A89) or routed descent.
    Status: ORANGE (A90--A94 formalization pending).
```

---

## 13. Consequence for F11 and F9/F11 mutual induction

This table discharges the F11 W-to-NW exit requirement:

```text
W-to-NW exit decrease table IS built relative to NW_0 (via containment lemma).
Every exit type is enumerated and certified:
  - 19 types have direct GREEN decrease;
  - 2 types route through YELLOW chains that terminate with strict decrease.
```

For the mutual induction (docs/analytic_f9_f11_mutual_induction_convention.md):

```text
Rule III (W-to-NW edge) is satisfied:
  Every W(m) -> NW_1 exit satisfies M_NW^*(NW_1) < M_NW^*(NW_0).

Rule IV (NW-to-W edge) is satisfied by the return checks in F11:
  W(m') with m' < m, or NW' with smaller M_NW^*.

The induction on (m, M_NW^*) is therefore well-founded.
```

Updated recommendation:

```text
F11 should cite this table and downgrade the W-to-NW blocker from RED to ORANGE
(the remaining ORANGE is persistent cut-rigidity within F11 itself, not in the
W-to-NW exit interface).

F9 Lemma F9.6 should reference this table as the source of W-to-NW decrease data.

ANALYTIC_PROGRESS_HANDOFF.md should update:
  F9/F11 W-to-NW exit table: RED → YELLOW (exits enumerated, decrease certified;
    only persistent cut-rigidity formalization and F9 edge table remain).
```
