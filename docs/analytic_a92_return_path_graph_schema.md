# A92 return-path graph schema

## Purpose

This document defines the proposed finite directed graph schema needed by A92. It defines vertices, edges, labels, terminal types, admissibility rules, forbidden transitions, required annotations, and the output classification for maximal paths. It does not prove A92.

## Claim boundary

This document does not prove A92, does not close F11, does not close the F9/F11 mutual-induction interface, and does not prove Erdős 475. All definitions in this document are PROPOSED unless explicitly marked DEFINED. No claim is PROVED unless an explicit proof exists in the docs read this session.

## Inputs

The graph schema operates on the following input data.

| Input                         | Definition                                                                                                                                                                                  | Location                                                                | Status                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------- |
| Non-weighted parent state NW0 | A non-weighted obstruction state that enters a genuine weighted core W(m).                                                                                                                  | `docs/analytic_f9_f11_mutual_induction_convention.md` §Problem          | DEFINED                                  |
| Parent measure M_NW\*(NW0)    | The 10-coordinate non-weighted lexicographic measure of NW0.                                                                                                                                | `docs/final/F09_nonweighted_termination_theorem.md` §F9.2               | DEFINED                                  |
| Weighted entry state W(m)     | A genuine weighted-core state with middle length m = \|B\|.                                                                                                                                 | `docs/final/F11_weighted_cut_selection_extraction.md` §F11.2            | DEFINED                                  |
| Weighted window Wwin          | The displayed segment A B C where A+2B+C=0, active support inside smallest interval containing A, B, C.                                                                                     | `docs/analytic_weighted_to_nonweighted_exit_decrease_table.md` §2       | DEFINED                                  |
| Middle block B                | The ordered sequence (b_1, ..., b_m) of atoms in the weighted middle.                                                                                                                       | `docs/final/F11_weighted_cut_selection_extraction.md` §F11.1            | DEFINED                                  |
| Weak cut-rigid flag           | Boolean: true if for every proper cut B=P R, the cut-swap return has doubled middle length >= \|B\| and no routed exit has terminated or satisfied the mutual-induction decrease condition. | `docs/final/F11_weighted_cut_selection_extraction.md` §Definition F11.5 | PARTIAL (definition uses informal terms) |
| Allowed cut positions         | Integers 1 <= i <= m-1, each corresponding to a proper cut B = b*1...b_i \| b*{i+1}...b_m.                                                                                                  | Implicit in cut notation                                                | DEFINED                                  |
| Routing theorem outputs       | The set of admissible non-weighted exit types from F10/F11 (A56 easy reductions, A97 displayed collisions, F7 recurrence, F6 external collision, isolated signed-boundary exits).           | `docs/analytic_weighted_exit_audit_interface.md` §Detail                | DEFINED                                  |

## Graph definition

Define a finite directed graph:

```text
G_A92 = (V, E, Lambda)
```

where:

- V is the finite vertex set.
- E is the finite edge set (ordered pairs from V x V).
- Lambda: E → L is a labeling function assigning each edge a label from the label set L.

### Vertex types (PROPOSED)

| Vertex type        | Tag         | Description                                                                                                                                                                                                                                            | Current status |
| ------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| ENTRY              | v_entry     | The weighted core state before any cut-swap is applied. Equivalent to the weakly cut-rigid core entered from NW0 with middle length m.                                                                                                                 | PROPOSED       |
| CUT_STATE          | v_cut_i     | The state after applying the fixed cut-swap to cut B = b*1...b_i \| b*{i+1}...b_m, for 1 <= i <= m-1. Each CUT_STATE records the resulting returned window.                                                                                            | PROPOSED       |
| WEIGHTED_RETURN    | v_W_m'      | A state where a cut-swap returns to a genuine weighted core with middle length m' < m.                                                                                                                                                                 | PROPOSED       |
| NONWEIGHTED_RETURN | v_NW        | A state where a cut-swap produces a non-weighted obstruction class NW1 (zero-composite, equal-interval, signed-interval, separated-equal, midpoint, pair-difference, transported-prefix, recurrence, external collision, bridge-gap, or any F3 class). | PROPOSED       |
| TERMINAL           | v_term      | SUCCESS, CONTRADICTION, or COLLAPSE. These are absorbing.                                                                                                                                                                                              | DEFINED (F9.3) |
| FORBIDDEN          | v_forbidden | A state that would violate the mutual-induction interface (re-entry to W(j) with j >= m without M_NW\* decrease or no-reentry certificate). Used to mark inadmissible transitions, not as reachable vertices.                                          | PROPOSED       |

### Edge types (PROPOSED)

| Edge type           | Tag        | Source type(s)                | Target type(s)     | Description                                                                                                                        | Current status  |
| ------------------- | ---------- | ----------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| CUT_SWAP            | cut_swap   | ENTRY, CUT_STATE              | CUT_STATE          | Transition via the fixed cut-swap operation (Lemma F11.3) applied to a proper cut B = P R.                                         | PROPOSED        |
| ROUTING             | routing    | CUT_STATE                     | NONWEIGHTED_RETURN | Transition when a cut-swap produces a non-weighted exit that routes to an F3 obstruction class without returning to weighted core. | PROPOSED        |
| WEIGHTED_DESCENT    | w_descent  | CUT_STATE                     | WEIGHTED_RETURN    | Transition when a cut-swap returns to a genuine weighted core with middle length m' < m.                                           | PROPOSED        |
| NONWEIGHTED_EXIT    | nw_exit    | NONWEIGHTED_RETURN            | TERMINAL           | Terminal exit from a non-weighted obstruction (SUCCESS, CONTRADICTION, COLLAPSE).                                                  | DEFINED (F9.3)  |
| NONWEIGHTED_DESCENT | nw_descent | NONWEIGHTED_RETURN            | TERMINAL           | Non-weighted state that satisfies M_NW\*(NW1) < M_NW\*(NW0) and terminates the return path.                                        | PROPOSED        |
| TERMINAL_EXIT       | term_exit  | CUT_STATE                     | TERMINAL           | Direct terminal exit from a cut-swap (immediate success, collapse, or contradiction).                                              | DEFINED (F11.3) |
| FORBIDDEN_REENTRY   | forbidden  | CUT_STATE, NONWEIGHTED_RETURN | FORBIDDEN          | A transition that would re-enter W(j) with j >= m without M_NW\* decrease or no-reentry certificate.                               | PROPOSED        |

### Edge labels (PROPOSED)

Each edge e in E carries a label Lambda(e) containing the following fields.

| Label field       | Type                        | Description                                                                                                                                        | Current status            |
| ----------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| cut_position      | integer (1..m-1) or NULL    | The split point i for the proper cut applied. NULL for edges not originating from a cut-swap.                                                      | PROPOSED                  |
| source_cut        | string or NULL              | Identifier of the source cut vertex (e.g., "P,R" or "b1...bi \| bi+1...bm"). NULL for entry vertex.                                                | PROPOSED                  |
| target_cut        | string or NULL              | Identifier of the target cut vertex (e.g., "P',R'") if target is CUT_STATE. NULL otherwise.                                                        | PROPOSED                  |
| result_type       | enum                        | One of: WEIGHTED_RETURN, NW_EXIT, TERMINAL, PERSISTENT_CUT_RIGID, FORBIDDEN.                                                                       | PROPOSED                  |
| m_before          | positive integer            | Value of m = \|B\| at the source state.                                                                                                            | DEFINED                   |
| m_after           | nonnegative integer or NULL | Value of m' = \|B\| at the target state. NULL if target is not a weighted core.                                                                    | PROPOSED                  |
| M_NW_parent       | tuple (10 integers)         | M_NW\*(NW0) — the measure of the entering non-weighted parent.                                                                                     | DEFINED                   |
| M_NW_child        | tuple (10 integers) or NULL | M_NW\*(NW1) — the measure of the non-weighted child state, if the edge exits to non-weighted machinery. NULL otherwise.                            | PROPOSED                  |
| measure_relation  | enum or NULL                | One of: LESS (M_NW\*(NW1) < M_NW\*(NW0)), EQUAL_UNKNOWN, GREATER, NOT_APPLICABLE, UNKNOWN. NULL for edges that do not exit to non-weighted states. | PROPOSED                  |
| no_reentry_status | boolean or UNKNOWN          | True if the child carries a formal no-reentry certificate. UNKNOWN if not yet certified.                                                           | PROPOSED (schema MISSING) |
| theorem_source    | string                      | Citation to the theorem lemma that justifies this transition (e.g., "F11.3", "F11.4", "F11.6", "A56", "A97").                                      | PROPOSED                  |
| proof_status      | enum                        | One of: PROVED, ASSERTED, PROPOSED, MISSING.                                                                                                       | PROPOSED                  |

## Vertex count

The vertex set size is bounded by:

```text
|V| <= 1 + (m-1) + t + n + 2
```

where:

- 1 = the ENTRY vertex
- (m-1) = CUT_STATE vertices (one per proper cut of B)
- t = number of distinct terminal types reached (at most 3: SUCCESS, CONTRADICTION, COLLAPSE)
- n = number of distinct non-weighted return states reachable from the graph (bounded by the F3 class universe, which is finite for a fixed p)
- 2 = one FORBIDDEN marker vertex, one WEIGHTED_RETURN class vertex

This bound is PROPOSED. No explicit proof of finiteness exists in the docs — it relies on the finite F3 obstruction class universe (bounded by p) and the finite number of proper cuts of B (m-1).

## Edge count

The edge set size is bounded by:

```text
|E| <= |V| * (max_out_degree)
```

where max_out_degree is at most (m-1) + (routing exits) + (terminal exits) + (forbidden exits). A conservative bound is O(m + p). This bound is PROPOSED.

## Admissibility rules

An edge e in E is admissible only if it satisfies the rule for its type.

### CUT_SWAP admissibility

```
source type: ENTRY or CUT_STATE
target type: CUT_STATE
cut_position: 1 <= i <= m_before - 1
weak_cut_rigid: true (the returned middle has length >= m_before)
```

The weak cut-rigid invariant must be preserved: the cut-swap return, if it returns to weighted core, must have doubled middle length at least m_before. If this fails, the core is not weakly cut-rigid and the graph does not apply.

### WEIGHTED_DESCENT admissibility

```
source type: CUT_STATE
target type: WEIGHTED_RETURN
m_after < m_before   (strict middle-length decrease)
```

Justified by Lemma F11.4 (side-contained weighted returns descend in |B|) and F11.8 (weighted descent terminates).

### NONWEIGHTED_EXIT admissibility

```
source type: CUT_STATE or NONWEIGHTED_RETURN
target type: NONWEIGHTED_RETURN or TERMINAL
```

Must satisfy ONE of:

1. M_NW\*(NW1) < M_NW\*(NW0) (strict measure decrease relative to entering parent), OR
2. NW1 carries a formal no-reentry certificate excluding W(j) with j >= m at equal-or-larger M_NW\*.

If neither condition holds, the edge is not admissible under the mutual-induction interface.

### TERMINAL_EXIT admissibility

```
source type: CUT_STATE
target type: TERMINAL
target state: SUCCESS, CONTRADICTION, or COLLAPSE
```

Terminal exits are always admissible. They close the obstruction path.

### ROUTING admissibility

```
source type: CUT_STATE
target type: NONWEIGHTED_RETURN
result_type: NW_EXIT
theorem_source: cited theorem justifying the routing
proof_status: PROVED or ASSERTED
```

Routing edges are admissible if the cited theorem exists and claims the routing. They are not automatically proved — the proof_status label records verification status.

### FORBIDDEN_REENTRY marking

```
source type: CUT_STATE or NONWEIGHTED_RETURN
target type: FORBIDDEN
condition: the transition would re-enter W(j) with j >= m
  without M_NW\* decrease and without no-reentry certificate
```

FORBIDDEN_REENTRY edges are not reachable in a valid proof — they mark transitions that would break the mutual-induction interface.

## Forbidden transitions

The following are explicitly forbidden in any admissible return-path graph:

1. **Same-middle weighted return (m' = m) without pattern-rigidity**: A weighted return from W(m) to W(m) is only admissible if the return is pattern-rigid, and pattern-rigid returns are impossible by A89/F11.7. Therefore any same-middle weighted return is forbidden.
2. **NW → W(j) with j >= m at equal-or-larger M_NW\***: A non-weighted exit that later re-enters a weighted core with middle length >= the original entry middle, without a strict M_NW\* decrease relative to NW0, is forbidden.
3. **Cyclic non-weighted same-measure path**: A sequence of NONWEIGHTED_RETURN vertices with non-decreasing M_NW\* is forbidden (would violate F9 termination).
4. **Unlabeled edges**: Every edge must carry a full label. Unlabeled edges are forbidden.

## Output classification

Every maximal path in G_A92 (a path that cannot be extended) must be classified as exactly one of the following.

| Output class              | Tag                       | Condition                                                                                                                                   | Current status                 |
| ------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| SUCCESS                   | SUCCESS                   | The path reaches TERMINAL with SUCCESS.                                                                                                     | DEFINED                        |
| CONTRADICTION_OR_COLLAPSE | CONTRADICTION_OR_COLLAPSE | The path reaches TERMINAL with CONTRADICTION or COLLAPSE.                                                                                   | DEFINED                        |
| WEIGHTED_DESCENT          | WEIGHTED_DESCENT          | The path reaches WEIGHTED_RETURN with m_after < m_before.                                                                                   | PROPOSED                       |
| NONWEIGHTED_DECREASE      | NONWEIGHTED_DECREASE      | The path reaches NONWEIGHTED_RETURN and satisfies M_NW\*(NW1) < M_NW\*(NW0).                                                                | PROPOSED                       |
| NONWEIGHTED_NO_REENTRY    | NONWEIGHTED_NO_REENTRY    | The path reaches NONWEIGHTED_RETURN with no-reentry certificate excluding W(j), j >= m.                                                     | PROPOSED (certificate MISSING) |
| OPEN_PERSISTENT_BRANCH    | OPEN_PERSISTENT_BRANCH    | The path terminates at a CUT_STATE or NONWEIGHTED_RETURN vertex whose outgoing edges are all PERSISTENT_CUT_RIGID (requires A90-A94 chain). | PROPOSED                       |

OPEN_PERSISTENT_BRANCH must not be removed — it prevents overclaiming closure of the A90-A94 chain before it is proved.

## Certificate schema

Below is the proposed pseudo-schema for a complete return-path graph certificate.

```text
graph_id: a92_graph_<unique_id>
parent:
  NW0_id: <string>
  M_NW*(NW0): [span, gap, support, r_depth, p_depth, s_depth, b_depth, t_rank, b_rank, h_excess]
weighted_entry:
  W_id: <string>
  m: <positive integer>
  B: [list of atoms]
  Wwin: { A: [atoms], B: [atoms], C: [atoms] }
  weak_cut_rigid: <boolean>
vertices:
  - id: v_entry
    type: ENTRY
    m_before: <integer>
    M_NW_parent: [10 integers]
  - id: v_cut_<i>
    type: CUT_STATE
    cut_position: <integer i>
    m_before: <integer>
    result_type: <WEIGHTED_RETURN | NW_EXIT | TERMINAL | PERSISTENT_CUT_RIGID>
  - id: v_W_<m'>
    type: WEIGHTED_RETURN
    m_after: <integer m' < m>
  - id: v_NW_<id>
    type: NONWEIGHTED_RETURN
    M_NW_child: [10 integers] or NULL
    measure_relation: <LESS | EQUAL_UNKNOWN | GREATER | NOT_APPLICABLE | UNKNOWN>
    no_reentry_status: <boolean | UNKNOWN>
  - id: v_term
    type: TERMINAL
    terminal_type: <SUCCESS | CONTRADICTION | COLLAPSE>
edges:
  - source: v_entry
    target: v_cut_<i>
    type: CUT_SWAP
    cut_position: <i>
    result_type: PERSISTENT_CUT_RIGID
    m_before: <m>
    m_after: NULL
    M_NW_parent: [10 integers]
    M_NW_child: NULL
    measure_relation: NOT_APPLICABLE
    no_reentry_status: UNKNOWN
    theorem_source: F11.3
    proof_status: PROVED
  - source: v_cut_<i>
    target: v_NW_<id>
    type: ROUTING
    result_type: NW_EXIT
    m_before: <m>
    m_after: NULL
    M_NW_parent: [10 integers]
    M_NW_child: [10 integers]
    measure_relation: <LESS | UNKNOWN>
    no_reentry_status: <boolean | UNKNOWN>
    theorem_source: <e.g., A56, A97, F7, F6>
    proof_status: <PROVED | ASSERTED | PROPOSED>
  - source: v_cut_<i>
    target: v_W_<m'>
    type: WEIGHTED_DESCENT
    result_type: WEIGHTED_RETURN
    m_before: <m>
    m_after: <m' < m>
    measure_relation: NOT_APPLICABLE
    no_reentry_status: false
    theorem_source: F11.4
    proof_status: PROVED
  - source: v_cut_<i>
    target: v_term
    type: TERMINAL_EXIT
    result_type: TERMINAL
    terminal_type: <SUCCESS | CONTRADICTION | COLLAPSE>
    proof_status: PROVED
maximal_paths:
  - path_id: path_1
    vertex_sequence: [v_entry, v_cut_1, v_NW_1]
    output_classification: NONWEIGHTED_DECREASE
    measure_relation: LESS
    no_reentry_flag: false
    unresolved_edges: []
  - path_id: path_2
    vertex_sequence: [v_entry, v_cut_2, v_cut_3, v_NW_2]
    output_classification: NONWEIGHTED_NO_REENTRY
    no_reentry_certificate:
      excludes_W_j: "j >= <m>"
      basis: <string>
    unresolved_edges: []
  - path_id: path_3
    vertex_sequence: [v_entry, v_cut_4]
    output_classification: OPEN_PERSISTENT_BRANCH
    unresolved_edges:
      - source: v_cut_4
        target: NULL
        reason: "PERSISTENT_CUT_RIGID — requires A90-A94 chain"
verdict: <PERSISTENT_CUT_RIGID | ROUTED_DESCENT | TERMINAL>
```
