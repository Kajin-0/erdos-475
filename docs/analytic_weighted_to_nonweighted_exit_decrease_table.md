# Analytic Table: Weighted-to-Nonweighted Exit Decrease / No-Reentry

Last updated: 2026-06-03

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

## 3. Status labels

```text
CLOSED       = terminal, smaller weighted middle, or certified NW decrease/no-reentry.
CONDITIONAL  = local decrease is clear, but relation to NW_0 must be stated in final proof.
OPEN         = no sufficient decrease/no-reentry certificate yet.
ROUTED       = exits to another final theorem whose own table must certify the decrease.
```

---

## 4. A56 easy-reduction exits

### Table A: A56 normal-form exits

| Exit source | Equation / condition | NW output class | Local support relative to `Wwin` | Candidate decrease | Mutual-induction status |
|---|---|---|---|---|---|
| A56 W1 | `B=0` | zero collapse / zero interval | inside `B` | terminal or support decrease | CLOSED if `B` nonempty |
| A56 W2L | `A+B=0` | adjacent zero-composite | inside `A B` | support contained in proper subwindow unless `C=empty` | CONDITIONAL |
| A56 W2R | `B+C=0` | adjacent zero-composite | inside `B C` | support contained in proper subwindow unless `A=empty` | CONDITIONAL |
| A56 W3 | `A=C` | equal interval / separated-equal / midpoint | spans outer blocks across `B` | type changes to nonweighted; gap/bridge route needed | OPEN/ROUTED |
| A56 W4 | transported-prefix/tail certificate | zero-composite / equal/signed nonweighted | inside containing block `D` plus one copy of `B` | support/provenance decrease if `D` inside parent window | CONDITIONAL |

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

| Sign row | Boundary relation | NW output class | Local support | Candidate decrease | Mutual-induction status |
|---|---|---|---|---|---|
| `(+,+)` | `alpha-gamma=2q` | signed midpoint / pair-difference | boundary triple `alpha,q,gamma` | support collapse to ≤3 atoms | CONDITIONAL/CLOSED for large window |
| `(+,-)` | `alpha+gamma=4q` | bounded three-atom signed relation | boundary triple | support collapse to ≤3 atoms | CONDITIONAL/CLOSED for large window |
| `(-,+)` | `alpha+gamma=0` | two-atom zero-composite | boundary pair | terminal/zero-composite | CLOSED |
| `(-,-)` | `alpha-gamma=-2q` | signed midpoint / pair-difference | boundary triple | support collapse to ≤3 atoms | CONDITIONAL/CLOSED for large window |
| endpoint `A=empty` | `2q+C=0` adjacent atom relation | pair/signed/zero/midpoint | `q` plus prefix of `C` | endpoint support decrease or recurrence | ROUTED |
| endpoint `C=empty` | `A+2q=0` adjacent atom relation | pair/signed/zero/midpoint | suffix of `A` plus `q` | endpoint support decrease or recurrence | ROUTED |

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

| Collision | Equation | NW output class | Local support | Candidate decrease | Mutual-induction status |
|---|---|---|---|---|---|
| `R_k'=A_i` | `A_i^+ + R_k=0` | zero-composite | suffix of `A` + prefix of `R` | usually proper subwindow | CONDITIONAL |
| `R_k'=C_l'` | `P + R_k^+ + C_l=0` | zero-composite | `P` + suffix of `R` + prefix of `C` | support excludes `A` and prefix `R_k` | CONDITIONAL |
| `R_k'=P_j'` | `P_j + R_k^+=0` | two-piece zero | inside `B` | support strictly inside `B` unless full endpoints | CLOSED/CONDITIONAL |
| `P_j'=A_i` | `A_i^+ + R + P_j=0` | zero-composite | suffix `A` + `R` + prefix `P` | support excludes prefix `A_i` and suffix `P_j^+` | CONDITIONAL |
| `P_j'=C_l'` | `P_j^+ + C_l=0` | two-piece zero | suffix `P` + prefix `C` | usually proper subwindow | CONDITIONAL |
| `P_j'=R_k'` | `P_j + R_k^+=0` | two-piece zero | inside `B` | support inside `B` | CLOSED/CONDITIONAL |

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

| Comparison | Simplified relation | NW output class | Local support | Candidate decrease | Mutual-induction status |
|---|---|---|---|---|---|
| moved `R` vs old `P` | `R_k=P_j` | equal-prefix / separated-equal | prefixes inside `B` | support inside `B` | CONDITIONAL/CLOSED |
| moved `P` vs old `R` | `R_k^+=P_j^+` | equal-tail / separated-equal | tails inside `B` | support inside `B` | CONDITIONAL/CLOSED |
| full-boundary case | tautology | no obstruction | none | ignored | CLOSED |
| one tail zero | suffix zero | zero-composite | suffix of `P` or `R` | terminal/local decrease | CLOSED |
| persistent across cuts | weak cut-rigidity | weighted branch | all cuts | handled by A90--A94/A89 | OPEN/ROUTED |

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

| Exit | NW output class | First theorem | Candidate decrease | Mutual-induction status |
|---|---|---|---|---|
| `H_R(k)` with bounded blocker | recurrence/local zero/pair | F7 | augmented enclosing span decreases | ROUTED |
| `H_P(j)` with bounded blocker | recurrence/local zero/pair | F7 | augmented enclosing span decreases | ROUTED |
| long blocker external | external/bridge | F6/F8 | span/gap/support/bridge subrank | ROUTED |
| long blocker pair/signed | pair/signed local | F4/F7/F10 | pair depth/support or weighted re-entry | ROUTED/OPEN |
| cyclic/wrapped blocker | cyclic recurrence | F7/A71 | midpoint/external/bridge routing | ROUTED |

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

| External output | First theorem | Candidate decrease | Mutual-induction status |
|---|---|---|---|
| bridge zero-composite | F6/F8 | bridge gap/span/support | ROUTED |
| signed bridge composite | F6/F8/F10 | nonweighted if reducible; weighted if irreducible | OPEN/ROUTED |
| equal/separated interval | F5/F8 | gap/separated depth | ROUTED |
| transported-prefix relation | A56/F10 | containing-block certificate | CONDITIONAL |
| pair-difference boundary | F4/F7 | pair depth/support | ROUTED |
| cyclic-cut branch | F7/A71 | midpoint/bridge/external | ROUTED |
| singleton/prefix recurrence | F7 | recurrence depth/span | ROUTED |
| weighted-core normal form | F10/F11 | must have smaller `m` or controlled exit | OPEN |
| collapse/minimality contradiction | terminal | terminal | CLOSED |

### Interpretation

External weighted exits are the least locally closed because they leave the displayed `A B C` window. They must be certified by F6/F8/F10/F11 and finally by F9.

Status:

```text
ROUTED but not closed.
```

---

## 10. No-reentry certificates: what is currently missing

A no-reentry certificate must show:

```text
Starting from NW_1, no future route can enter W(j), j>=m, at equal-or-larger M_NW^*.
```

No full no-reentry certificate currently exists.

The strongest candidates are:

```text
1. isolated A97 equal-prefix/equal-tail exits supported strictly inside B;
2. A81 atom-middle boundary triples when the full weighted window has length > 3;
3. direct A97 two-piece zero exits supported strictly inside B.
```

For these, a likely certificate is:

```text
support contained in the old weighted middle B
=> any later weighted core using middle length >=m would need support at least B again
=> re-entry at same/larger m requires persistent cut-rigidity
=> route to A90--A94/A89 rather than ordinary NW cycle.
```

This is not yet formalized.

---

## 11. Preliminary closure ranking

### Locally closed

```text
B=0 terminal collapse.
A81 (-,+) alpha+gamma=0 two-atom zero.
A97 full-boundary tautology ignored.
A97 one-tail-zero suffix zero.
A97 direct inside-B two-piece zero, modulo parent-measure comparison.
```

### Strong candidates for closure after parent-span hypothesis

```text
A56 A+B=0 / B+C=0 when the opposite outer block is nonempty.
A81 boundary triple rows when A^- or C^+ is nonempty.
A97 direct displayed zero-composite rows with proper support.
A97 isolated equal-prefix/equal-tail rows inside B.
```

### Still genuinely open

```text
A56 A=C separated-equal exit.
A56 transported-prefix/tail no-reentry unless certificate records parent support.
F7 recurrence exits from weighted cut-swap.
F6 external exits from weighted cut-swap.
Persistent signed-boundary rigidity across all cuts.
A90--A94 minimal-path formalization.
```

---

## 12. Required next refinement

This table should be converted into a final proof table with exact columns:

```text
source edge;
local equation;
child obstruction class;
child support interval;
parent support interval;
M_NW^* coordinate decreased;
if no decrease, no-reentry certificate;
dependency theorem;
status.
```

The most urgent missing data is:

```text
parent support interval of NW_0 for each weighted invocation.
```

Without that, many rows can prove only local decrease relative to `Wwin`, not the stronger mutual-induction decrease relative to `NW_0`.

---

## 13. Consequence for F11

This table partially discharges the F11 risk:

```text
W-to-NW exit decrease/no-reentry table must be built relative to weighted entry state.
```

New status:

```text
Table drafted.
Many rows are locally classified.
Final closure still needs parent-support annotations and no-reentry certificates.
```

Patch recommendation:

```text
Update F11 to cite this table and keep risk as ORANGE, not GREEN.
Update ANALYTIC_PROGRESS_HANDOFF.md to record that the first W-to-NW table exists but is not final.
```
