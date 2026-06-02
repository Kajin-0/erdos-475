# Analytic Checkpoint: Global Class Graph and Measure Status

This checkpoint is intended to stop the analytic proof work from becoming an indefinite sequence of local-routing notes.

Claim boundary:

```text
This file is not a proof of Erdős 475.
It is a proof-status checkpoint.
It separates:
  1. finite-computational evidence;
  2. endpoint/local analytic routing progress;
  3. global termination obligations that remain unresolved.
```

---

## Why this checkpoint exists

External review correctly emphasizes that the most independently checkable progress in the repository is the finite-certificate layer.

The recent analytic notes are meaningful only if they contribute to a global termination proof. Local statements of the form:

```text
this branch routes to F6/F7/F8/F9
```

are not enough unless every resulting class transition is shown to decrease a well-founded measure or terminate.

This file records the global class graph that must now be closed.

---

## Current evidence classes

### Computational finite-certificate evidence

Status:

```text
Strongest externally credible layer.
```

Current Tier 1 verified finite frontier in `certificates/verified_domains.json`:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

Artifact distinction:

```text
Tier 1A: committed / repository-checkable.
Tier 1B: verified local/external JSONL or summary digest, not fully committed due to size.
```

The computational layer proves only finite instances in declared domains. It does not prove that the analytic residue lies in those domains.

### Analytic local-routing evidence

Status:

```text
Useful but not theorem-complete.
```

Local endpoint branch work has packaged:

```text
T1/T2/T3/T4 first-blocker templates;
generic interval modules;
duplicate interval modules;
scalar absorption;
boundary-zero handling;
singleton routing;
F6 external-collision embedding;
F7 recurrence endpoint audits;
F9 endpoint measure audit.
```

This establishes class coverage for endpoint-local branches, not global termination.

### Analytic global termination evidence

Status:

```text
Main unresolved proof layer.
```

The required theorem is:

```text
Every nonterminal branch in the global obstruction graph strictly decreases M_NW^*,
or enters a bounded recurrence class that later decreases M_NW^*,
or exits to a separately terminating weighted-core theorem.
```

This is not yet proved.

---

## Global measure

Use the F9 measure:

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

Every edge in the obstruction graph must be labeled by at least one of:

```text
TERMINAL,
STRICT_DECREASE(enclosing_span),
STRICT_DECREASE(gap_length),
STRICT_DECREASE(support_size),
STRICT_DECREASE(recurrence_depth),
STRICT_DECREASE(pair_depth),
STRICT_DECREASE(separated_depth),
STRICT_DECREASE(bridge_depth),
STRICT_DECREASE(type_rank),
STRICT_DECREASE(boundary_rank),
WEIGHTED_EXIT_TO_F10_F11,
UNRESOLVED.
```

Edges labeled `UNRESOLVED` block theorem-level claims.

---

## Global obstruction class graph

### Terminal classes

| Class | Destination | Measure status | Current status |
|---|---|---|---|
| SUCCESS | terminal | TERMINAL | closed |
| CONTRADICTION | terminal | TERMINAL | closed |
| ZERO_ATOM | terminal | TERMINAL | closed |
| DUPLICATE_ATOM | terminal | TERMINAL | closed |
| MINIMALITY_VIOLATION | terminal | TERMINAL | closed |
| INTERIOR_RELATIVE_ZERO | terminal | TERMINAL | closed by boundary-zero lemma |

---

### Local descent classes

| Class | Typical destination | Required decrease | Current status |
|---|---|---|---|
| PROPER_SUBINTERVAL | F4 local descent | enclosing_span or support_size | conditionally routed |
| PREFIX_ZERO | F4 / terminal | enclosing_span or terminal | conditionally routed |
| TWO_PIECE_ZERO | F4 / A28--A33 | enclosing_span/support_size or recurrence | partially unresolved globally |
| THREE_PIECE_ZERO | F4 / A28--A33 | enclosing_span/support_size or recurrence | partially unresolved globally |
| EQUAL_INTERVAL | F4/F5 | enclosing_span/gap_length/support_size | partially unresolved globally |
| SIGNED_INTERVAL | F4/F6/F10 | enclosing_span/support_size or weighted exit | partially unresolved globally |
| PAIR_DIFFERENCE | F7/F4/F10 | pair_depth/support_size or weighted exit | partially unresolved globally |

Status interpretation:

```text
Endpoint-local notes usually route into these classes correctly.
The full descent proof for the classes themselves belongs to F4/F5/F7/F10/F11/F9.
```

---

### External and bridge classes

| Class | Typical destination | Required decrease | Current status |
|---|---|---|---|
| TEMPLATE_EXTERNAL_CANCELLATION | F6 | class embedding closed | endpoint-specific closed |
| EXTERNAL_COLLISION | F6 exits | span/gap/support/recurrence or weighted exit | globally conditional |
| BRIDGE_GAP | F8 | enclosing_span/gap_length/bridge_depth | globally conditional |
| SEPARATED_EQUAL | F5/F8 | gap_length/separated_depth | globally conditional |
| MIDPOINT | A55/F5/F7 | zero-composite/recurrence | class-routed, global descent pending |
| WRAPPING_BRIDGE | F6/F8 | bridge_depth/gap_length/span | globally conditional |

Endpoint-specific status:

```text
Template-aware external outputs have explicit F6 destinations.
T1/T2 long collision bridge outputs locally show smaller enclosure in several cases.
But full bridge/gap termination remains an F8/F9 obligation.
```

---

### Recurrence classes

| Class | Typical destination | Required decrease | Current status |
|---|---|---|---|
| SINGLETON_RECURRENCE | F7 | recurrence_depth then enclosing_span | endpoint atom table closed, global F7/F9 conditional |
| PAIR_DIFFERENCE_RECURRENCE | F7 | pair_depth/support/span | endpoint table patched, global F7/F9 conditional |
| CYCLIC_RECURRENCE | F7/A71 | minimality/span/bridge/midpoint routing | midpoint characteristic audit closed, global conditional |
| A34_RECURRENCE | F7/F9 | recurrence_depth or bounded-blocker span decrease | global conditional |
| BOUNDED_BLOCKER | F7 | enclosing_span | conditionally closed if augmented span convention holds |
| LONG_BLOCKER | F7/F6/F8 | routes to bridge/pair/signed/cyclic classes | class-routed, termination conditional |

Recent hardening:

```text
H1/H2 sign audit completed.
H2 source correction applied to A67 and F07.
Pair-difference endpoint table completed.
A69 source correction applied.
Singleton atom endpoint audit completed.
Cyclic midpoint characteristic audit completed.
```

Remaining recurrence risk:

```text
Prove that all F7 exits are consumed by F9 without cycles at equal measure.
Verify augmented span convention edge-by-edge.
```

---

### Weighted-core classes

| Class | Typical destination | Required decrease | Current status |
|---|---|---|---|
| WEIGHTED_CORE | F10/F11 | weighted measure or cut-selection descent | unresolved as theorem dependency |
| WEIGHTED_SIGNED_INTERVAL | F10/F11 | weighted exit or conversion to nonweighted class | unresolved globally |
| CUT_RIGID_RETURN | F10/F11/A82 | finite return-path or weighted descent | unresolved globally |

Status:

```text
This is one of the highest-risk remaining areas.
Any nonweighted route that exits into WEIGHTED_CORE is not closed until F10/F11 are closed.
```

---

## Endpoint-branch contribution to the graph

Endpoint branch now contributes the following local-to-global edges:

| Endpoint output | Global destination | Endpoint-specific status |
|---|---|---|
| SUCCESS | terminal | closed |
| CONTRADICTION | terminal | closed |
| PROPER_SUBINTERVAL | F4/F9 local descent | class-routed |
| TEMPLATE_EXTERNAL_CANCELLATION | F6 external collision | class-routed and embedded |
| BRIDGE_GAP_SMALLER_ENCLOSURE | F8 bridge/gap | class-routed, F8 conditional |
| AFFINE_SINGLETON | duplicate/generic/scalar/F7 | class-routed |
| SCALAR_ABSORPTION | finite local branch then F6/terminal | class-routed and p=3/p=5 audited |
| BOUNDARY_SENSITIVE_ZERO | terminal or boundary_rank | class-routed |

Endpoint-specific conclusion:

```text
No known endpoint-local branch is currently unclassified.
```

But:

```text
Endpoint avoidance is not proved until the destination classes terminate globally.
```

---

## Current unresolved theorem blockers

### Blocker 1: F9 edge-by-edge descent proof

Need a table proving every nonterminal edge in the global class graph decreases `M_NW^*` or exits to a separately terminating weighted theorem.

Current status:

```text
Not complete.
```

### Blocker 2: F8 bridge/gap descent hardening

Need to prove every bridge/gap route decreases:

```text
enclosing_span,
gap_length,
support_size,
or bridge_depth.
```

Current status:

```text
Partially developed, still global-risk.
```

### Blocker 3: F10/F11 weighted-core termination

Need a non-circular weighted cut-selection theorem.

Current status:

```text
Unresolved/high-risk.
```

### Blocker 4: analytic residue bridge

Need exact source-theorem extraction proving:

```text
remaining analytic residue subset verified finite frontier.
```

Current status:

```text
Unresolved.
```

### Blocker 5: artifact hardening for Tier 1B

Need public artifact retrieval/regeneration and independent review commands for:

```text
p=29, |B|=9..15,
p=31, |B|=7..16,
p=31, |B|=17 summary digest.
```

Current status:

```text
Evidence exists, but not all routine Git/CI-checkable.
```

---

## Progress accounting

### Real progress from recent analytic work

The recent analytic work should be counted as real progress only in these categories:

```text
1. unsafe notation corrected;
2. local branch taxonomy completed for endpoint branch;
3. template-aware external-collision data added;
4. H2 and A69 endpoint-convention errors found and corrected;
5. singleton/pair/cyclic recurrence endpoint audits completed;
6. endpoint-local outputs mapped into global classes.
```

### Not yet proof-grade progress

The recent analytic work should not be counted as proof-grade closure of Erdős 475 because:

```text
1. global class graph termination is not proved;
2. weighted-core termination is not proved;
3. analytic residue inclusion is not proved;
4. Tier 1B artifact release/reproduction is not fully hardened.
```

---

## Recommended next actions

Do not continue adding new local endpoint-branch notes unless a concrete algebraic error is found.

Next proof actions should be:

```text
1. F8 bridge/gap descent hardening.
2. F10/F11 weighted-core termination audit.
3. F9 global edge-by-edge measure table.
4. Exact analytic residue extraction from published theorems.
```

Next engineering actions should be:

```text
1. Make strict CI check Tier 1A artifacts by default.
2. Add artifact retrieval/regeneration instructions for Tier 1B.
3. Fix stale docs such as docs/FINITE_THEOREM.md if still inconsistent.
4. Harden Python witness parsing to reject non-integer JSON values.
```

---

## One-line status

```text
Finite evidence is strong.
Endpoint-local analytic routing is substantially improved.
Global analytic termination and residue inclusion remain the real theorem gaps.
```
