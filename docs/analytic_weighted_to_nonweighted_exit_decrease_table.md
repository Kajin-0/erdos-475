# Analytic Table: Weighted-to-Nonweighted Exit Decrease / No-Reentry

Last reconciled: 2026-06-04

This note audits weighted-to-nonweighted exits used by the F9/F11 mutual-induction interface.

Claim boundary:

```text
This is not a proof of Erdős 475.
This is an edge-audit table.
It records local classifications and identifies what still needs a final lexicographic-rank proof.
Do not read this file as final closure of F11 or F9.
```

---

## 1. Purpose

For a non-weighted parent state:

```text
NW_0 -> W(m),
```

where `W(m)` is a genuine weighted core with middle length:

```text
m = |B|,
```

an exit:

```text
W(m) -> NW_1
```

is safe for mutual induction only if one of the following is proved:

```text
1. NW_1 is terminal;
2. M_NW^*(NW_1) < M_NW^*(NW_0);
3. NW_1 carries a formal no-reentry certificate excluding W(j), j >= m,
   at equal-or-larger M_NW^*;
4. the branch returns to W(m') with m' < m.
```

This table distinguishes:

```text
local classification
```

from:

```text
final lexicographic decrease relative to NW_0.
```

A local support-size decrease is not automatically a final lexicographic decrease unless earlier coordinates of `M_NW^*` are also shown not to increase.

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

The global non-weighted measure is:

```text
M_NW^* = (
  enclosing_span,
  gap_length,
  support_size,
  recurrence_depth,
  pair_depth,
  separated_depth,
  bridge_depth,
  type_rank,
  boundary_rank,
  h_excess
).
```

Thus a row using `support_size` as its decreasing coordinate must also verify:

```text
enclosing_span(NW_1) <= enclosing_span(NW_0),
gap_length(NW_1) <= gap_length(NW_0),
```

or must route to a theorem that proves these earlier-coordinate conditions.

---

## 3. Containment lemma, useful but not sufficient by itself

For a genuine weighted core:

```text
A+2B+C=0,
```

at least one of `A` or `C` is nonempty.

Reason:

```text
if A=C=empty, then 2B=0;
for odd p this gives B=0, contradicting genuine-core condition B != 0.
```

Therefore:

```text
|support(Wwin)| = |A|+|B|+|C| >= |B|+1 = m+1.
```

This is useful for rows whose output support is contained in `B`:

```text
support(NW_1) subset B
=> support_size(NW_1) <= m < m+1 <= support_size(Wwin).
```

However, final mutual induction needs comparison against `NW_0`, not only `Wwin`, and lexicographic earlier coordinates must not increase. The containment lemma is therefore a strong local decrease certificate, not a standalone final proof for every row.

---

## 4. Status labels

```text
GREEN  = terminal or direct local decrease with clear non-increase of earlier coordinates.
YELLOW = class-routed; expected decrease via F4/F5/F6/F7/F8/F9 but final edge table needed.
ORANGE = plausible but still requires explicit lexicographic or no-reentry proof.
RED    = unclassified or circular. No row below is RED after current audits.
```

---

## 5. Comprehensive W-to-NW exit table

There are **22 enumerated rows**, not 21.

| # | Exit type | Source | NW output class | Candidate decreasing coordinate | Status | Required final check |
|---|---|---|---|---|---|---|
| E1 | `B=0` | A56 W1 | `ZERO_COLLAPSE` | terminal / contradiction | GREEN | state odd-characteristic `2 != 0` where used |
| E2 | `A+B=0` | A56 W2L | `TWO_PIECE_ZERO` | enclosing span or support | YELLOW | handle `C=empty` endpoint case; prove earlier coordinates do not increase |
| E3 | `B+C=0` | A56 W2R | `TWO_PIECE_ZERO` | enclosing span or support | YELLOW | handle `A=empty` endpoint case; prove earlier coordinates do not increase |
| E4 | `A=C` | A56 W3 | `EQUAL_INTERVAL` / `SEPARATED_EQUAL` | type/gap after F5/F8 | ORANGE | final type-rank order and F5/F8 gap descent required |
| E5 | transported-prefix | A56 W4 | zero/equal/signed nonweighted | support/provenance | YELLOW | containing-block certificate must include parent support and earlier-coordinate nonincrease |
| E6 | transported-tail | A56 W4 | zero/equal/signed nonweighted | support/provenance | YELLOW | same as E5 |
| E7 | atom-middle `(+,+)` | A81 | signed midpoint / pair-difference | support | YELLOW | boundary triple inside parent window; earlier-coordinate nonincrease |
| E8 | atom-middle `(+,-)` | A81 | bounded signed relation | support | YELLOW | boundary triple inside parent window; earlier-coordinate nonincrease |
| E9 | atom-middle `(-,+)` | A81 | two-atom zero | terminal/support | GREEN | zero-composite terminal or F4 zero branch |
| E10 | atom-middle `(-,-)` | A81 | signed midpoint / pair-difference | support | YELLOW | boundary triple inside parent window; earlier-coordinate nonincrease |
| E11 | `A=empty` atom-middle | A80/A81 | pair/signed/zero/midpoint | support or recurrence | YELLOW | endpoint routing through F4/F5/F7 |
| E12 | `C=empty` atom-middle | A80/A81 | pair/signed/zero/midpoint | support or recurrence | YELLOW | endpoint routing through F4/F5/F7 |
| E13 | `R_k'=A_i` | A97.1 | zero-composite | support / span | YELLOW | prefix/suffix endpoint cases and earlier-coordinate nonincrease |
| E14 | `R_k'=C_l'` | A97.2 | zero-composite | support / span | YELLOW | prefix/suffix endpoint cases and earlier-coordinate nonincrease |
| E15 | `R_k'=P_j'` | A97.3/6 | two-piece zero inside `B` | support | GREEN/YELLOW | GREEN if strict inside `B`; endpoint cases require table row |
| E16 | `P_j'=A_i` | A97.4 | zero-composite | support / span | YELLOW | prefix/suffix endpoint cases and earlier-coordinate nonincrease |
| E17 | `P_j'=C_l'` | A97.5 | two-piece zero | support / span | YELLOW | prefix/suffix endpoint cases and earlier-coordinate nonincrease |
| E18 | `R_k=P_j` | A97.7 | equal-prefix / separated-equal | support inside `B` | YELLOW | F5/F8 routing if separated; earlier-coordinate nonincrease |
| E19 | `R_k^+=P_j^+` | A97.8 | equal-tail / separated-equal | support inside `B` | YELLOW | F5/F8 routing if separated; earlier-coordinate nonincrease |
| E20 | `x+a+R_k=f` | A97.9/F7 | forbidden recurrence | enclosing span via bounded blocker or routed | YELLOW | final F7/F9 edge table |
| E21 | `x+a+r+P_j=f` | A97.9/F7 | forbidden recurrence | enclosing span via bounded blocker or routed | YELLOW | final F7/F9 edge table |
| E22 | external collision | F10/F6 | multiple F6 classes | via F6/F8/F4/F5/F7 | YELLOW | final F6/F8/F9 finite-budget/edge table |

Summary:

```text
22 rows total.
2 rows currently GREEN without substantial routing caveat: E1, E9.
Most rows are YELLOW: locally classified but needing final lexicographic edge verification.
1 row is ORANGE: E4, because equal-outer blocks can preserve span and require explicit F5/F8/type-rank handling.
0 rows are RED.
```

---

## 6. Rows that are locally strong

The strongest local decrease candidates are:

```text
A97 inside-B two-piece zero rows;
A97 isolated equal-prefix/equal-tail rows inside B;
A81 boundary-triple rows when the full weighted window has extra outer atoms;
A56 adjacent zero rows when the opposite outer block is nonempty.
```

These should be easy to promote once the final edge table includes the earlier-coordinate checks.

---

## 7. Rows that still need explicit final treatment

### A56 `A=C`

This is the main local nonweighted exit that can preserve the full weighted window span. It should be routed through:

```text
F5 separated-equal / midpoint;
F8 bridge/gap if separated;
F9 edge table for final rank decrease.
```

Do not mark this GREEN until the `type_rank` order and earlier-coordinate nonincrease are explicit.

### Recurrence exits E20--E21

These depend on F7 and then F9.

Current status:

```text
class-routed but not final-edge certified.
```

### External collision exit E22

This depends on F6/F8/F9 finite-budget and edge-table closure.

Current status:

```text
class-routed but not final-edge certified.
```

### Persistent signed-boundary rigidity

This is not a W-to-NW exit row. It remains inside the weighted branch and belongs to:

```text
A90--A94 weak-to-pattern-rigid reduction;
A89 strong exact self-return impossibility;
SNS C15--C18 finite-state/minimality program, if using the phase-aware route.
```

Status:

```text
ORANGE outside this table.
```

---

## 8. Consequence for F11

This table **substantially reduces** the F11 W-to-NW interface risk but does not fully discharge F11.

Safe current statement:

```text
W-to-NW exits are enumerated and locally classified.
Most have clear local support/span decrease candidates.
Final closure still requires the F9/global edge table to verify lexicographic nonincrease of earlier coordinates and routed exits.
```

Unsafe statement:

```text
Every W-to-NW exit is already certified and Rule III is fully satisfied.
```

Do not use the unsafe statement in final proof or handoff documents until the F9 edge table and finite-budget audits are complete.

---

## 9. Next required artifact

Create or patch a final global edge table with columns:

```text
source edge;
child obstruction class;
enclosing_span comparison;
gap_length comparison;
support_size comparison;
later-coordinate decrease;
destination theorem;
status.
```

Recommended file:

```text
docs/analytic_global_edge_rank_table.md
```

For the SNS route, the analogous file should use:

```text
M_phase = (D_SNS^*, phase_rank, M_loc, M_w, transition_budget).
```

---

## 10. Current status

```text
Status: reconciled conservative W-to-NW audit.
Risk: YELLOW/ORANGE.
Main remaining issues:
  1. final F9/F6/F7/F8 edge-rank table;
  2. persistent weighted cut-rigidity / finite-state minimality;
  3. SNS final edge table if the phase-aware route remains primary.
```
