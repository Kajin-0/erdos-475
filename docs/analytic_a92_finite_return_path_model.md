# A92 finite return-path model

## Purpose

This document isolates the finite return-path model needed for A92 in the A90-A94 persistent cut-rigidity branch. It defines the objects, interface, graph model, and obligations that A92 must supply. It does not prove A92.

## Claim boundary

This document does not prove A92, does not close F11, does not close the F9/F11 mutual-induction interface, and does not prove Erdős 475. It records what definitions exist, what definitions are missing, and what gap types remain. No claim in this document is PROVED unless an explicit proof exists in the docs read this session.

## Parent state and weighted state

The following objects are extracted from existing docs. If an object is missing or informal, it is marked MISSING or AMBIGUOUS.

### Defined objects

| Object                        | Definition                                                                                                                                                       | Location                                                                                                                          | Status  |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------- |
| Non-weighted parent state NW0 | A non-weighted obstruction state that enters a genuine weighted core W(m).                                                                                       | `docs/analytic_f9_f11_mutual_induction_convention.md` §Problem, `docs/analytic_weighted_to_nonweighted_exit_decrease_table.md` §1 | DEFINED |
| Weighted window Wwin          | The displayed segment A B C of a genuine weighted core, where A+2B+C=0 and active support is contained in the smallest interval containing A, B, C.              | `docs/analytic_weighted_to_nonweighted_exit_decrease_table.md` §2                                                                 | DEFINED |
| Weighted core middle length m | m = \|B\|, the length of the middle block of the genuine weighted core.                                                                                          | `docs/final/F11_weighted_cut_selection_extraction.md` §F11.2                                                                      | DEFINED |
| Weighted measure M_W          | M_W = (m, M_NW^\*, w_subrank).                                                                                                                                   | `docs/analytic_f9_f11_mutual_induction_convention.md` §State classes                                                              | DEFINED |
| Non-weighted measure M_NW\*   | Lexicographic tuple (enclosing_span, gap_length, support_size, recurrence_depth, pair_depth, separated_depth, bridge_depth, type_rank, boundary_rank, h_excess). | `docs/final/F09_nonweighted_termination_theorem.md` §F9.2                                                                         | DEFINED |

### Objects needed by A92

| Object                          | Location                                                                                                                                                                                                                          | Status  | Notes                                                                                                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Returned non-weighted state NW1 | The non-weighted state produced when a weighted branch exits. Referenced in mutual-induction interface.                                                                                                                           | PARTIAL | Defined implicitly (any NW state output by W(m) → NW). No formal construction from weighted return path exists.                                                  |
| Allowed weighted return W(m')   | A return to weighted core with m' < m. Referenced in F11.1 outcome 5 and Lemma F11.4.                                                                                                                                             | DEFINED | Lemma F11.4: "Side-contained weighted returns descend in \|B\|."                                                                                                 |
| No-reentry certificate          | A formal certificate that NW1 cannot re-enter W(j) with j >= m at equal-or-larger M_NW\*.                                                                                                                                         | MISSING | Referenced in F9/F11 interface but no definition, schema, or construction exists anywhere in the docs read.                                                      |
| Weak cut-rigid weighted core    | A genuine weighted core with \|B\| >= 2 where every proper cut B=P R produces a cut-swap return with doubled middle length at least \|B\| and no routed exit has terminated or satisfied the mutual-induction decrease condition. | PARTIAL | Definition F11.5 exists but uses informal terms: "doubled middle" and "routed exit" are not formally defined.                                                    |
| Finite return path              | A finite sequence of intermediate states modeling a weakly cut-rigid weighted self-return, each corresponding to a cut of B, with bounded length.                                                                                 | MISSING | Referenced as an assumption in Lemma F11.6 and as a dependency in F11.11 R3. No explicit definition, construction, or bound exists.                              |
| First changed endpoint          | The first position along a finite return path where an internal endpoint of B changes.                                                                                                                                            | MISSING | Used in the Lemma F11.6 proof sketch but not defined. Unclear whether "first" refers to position along B ordering, index in return path, or some other ordering. |
| Self-return path minimality     | A minimal non-descending self-return for A94.                                                                                                                                                                                     | MISSING | No definition of what "minimal" means (minimum \|B\|? minimum M_NW\*? minimum path length?) is extracted.                                                        |

## Required A92 interface

A92 must eventually provide the following interface.

Given a persistent cut-rigidity branch entering F11 from parent NW0, every finite return path must output one of:

1. SUCCESS;
2. CONTRADICTION or COLLAPSE;
3. W(m') with m' < m;
4. NW1 with M_NW\*(NW1) < M_NW\*(NW0);
5. NW1 with a formal no-reentry certificate excluding W(j), j >= m, at equal-or-larger M_NW\*.

This list is taken from `docs/analytic_f9_f11_mutual_induction_convention.md` §Mutual Induction Interface Lemma and `docs/analytic_a90_a94_formalization_obligation_ledger.md` §Parent obstruction context. It is unchanged.

## Finite return-path graph model

The finite return-path model that A92 must define is a finite directed graph.

### Vertices (PROPOSED)

Each vertex corresponds to a proper cut B = P R of the weakly cut-rigid middle block B, where B is expressed as a concatenation of the sequence elements (b_1, ..., b_m). A vertex may also represent the initial entry state (before any cut is applied) and terminal states.

| Vertex type                    | Representation                                                                       | Current status                 |
| ------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------ |
| Entry vertex v_entry           | The state of the weighted core before the first cut-swap is applied.                 | PROPOSED                       |
| Cut vertex v\_{P,R}            | The state after applying the fixed cut-swap to cut B=P R. One vertex per proper cut. | PROPOSED                       |
| Weighted return vertex v_W(m') | A state where the cut-swap returns to a weighted core with middle length m'.         | PROPOSED                       |
| Non-weighted exit vertex v_NW  | A state where the cut-swap exits to a non-weighted obstruction class.                | PROPOSED                       |
| Terminal vertex v_term         | SUCCESS, CONTRADICTION, or COLLAPSE.                                                 | DEFINED (F9.3 terminal states) |

### Edges (PROPOSED)

Each edge represents a transition from one vertex to another via a single cut-swap operation, routing step, or return transition.

| Edge type              | Source             | Target                | Current status |
| ---------------------- | ------------------ | --------------------- | -------------- |
| Cut-swap edge          | v*entry or v*{P,R} | v\_{P',R'} (next cut) | PROPOSED       |
| Weighted return edge   | v\_{P,R}           | v_W(m')               | PROPOSED       |
| Non-weighted exit edge | v\_{P,R}           | v_NW                  | PROPOSED       |
| Terminal edge          | v\_{P,R}           | v_term                | PROPOSED       |

### Edge labels (PROPOSED)

Each edge must carry:

| Label           | Description                                                                             | Current status               |
| --------------- | --------------------------------------------------------------------------------------- | ---------------------------- |
| cut_position    | The split point i where B = b*1...b_i \| b*{i+1}...b_m.                                 | PROPOSED                     |
| middle_length   | \|B\| before the cut-swap.                                                              | DEFINED                      |
| result_type     | One of: WEIGHTED_RETURN, NW_EXIT, TERMINAL, PERSISTENT_CUT_RIGID.                       | PROPOSED                     |
| measure_delta   | M_NW\*(child) - M_NW\*(entry) if applicable, or UNKNOWN for persistent cut-rigid edges. | PROPOSED                     |
| no_reentry_flag | Boolean: whether the child carries a no-reentry certificate.                            | PROPOSED (schema is MISSING) |

### Admissible transitions (PROPOSED)

A transition is admissible only if:

- Cut-swap edges preserve the weak cut-rigidity invariant (every proper cut returns with doubled middle length >= |B|).
- Weighted return edges satisfy m' < m (strict middle-length decrease).
- Non-weighted exit edges carry a measure-decrease annotation or no-reentry certificate relative to NW0.
- Terminal edges terminate.

### Forbidden transitions (PROPOSED)

The following are forbidden:

- Same-middle weighted return (m' = m) that is not pattern-rigid.
- Pattern-rigid same-middle return (forbidden by A89/F11.7).
- NW → W(m) where m' >= m and M_NW\* is not strictly smaller.

### Rank or measure annotations required on each edge

Each edge in the finite return-path graph must carry one of the following annotations:

1. strict_M_NW_decrease: M_NW\*(child) < M_NW\*(entry_state)
2. strict_m_decrease: child is W(m') with m' < m
3. terminal: child is SUCCESS, CONTRADICTION, or COLLAPSE
4. no_reentry: child carries a formal no-reentry certificate
5. unresolved: edge is PERSISTENT_CUT_RIGID and requires the A90-A94 chain

## A92 obligation table

| Object or claim                      | Location in existing docs                                                                                                                                  | Needed definition                                                                                                                                       | Current status | Gap type         | Notes                                                                         |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ---------------- | ----------------------------------------------------------------------------- |
| Finite return-path model             | `docs/final/F11_weighted_cut_selection_extraction.md` §F11.7 (Lemma F11.6 assumption), §F11.0 (dependency), §F11.11 R3                                     | A finite directed graph whose vertices are proper cuts of B and whose edges are cut-swap transitions, with bounded length as a function of \|B\| and p. | MISSING        | definition_gap   | Most foundational missing piece. A91 and A94 cannot be formalized without it. |
| Weak cut-rigid weighted core         | `docs/final/F11_weighted_cut_selection_extraction.md` §Definition F11.5                                                                                    | A genuine weighted core with \|B\|>=2 where every proper cut produces a doubled-middle return or no routed exit satisfying mutual-induction decrease.   | PARTIAL        | definition_gap   | "Doubled middle" and "routed exit" are not formally defined.                  |
| Vertex set V                         | Not extracted                                                                                                                                              | The set of proper cuts B=P R, plus entry vertex and terminal vertices.                                                                                  | MISSING        | finite_graph_gap |                                                                               |
| Edge set E                           | Not extracted                                                                                                                                              | Transitions between vertices via cut-swap, routing, return, or termination.                                                                             | MISSING        | finite_graph_gap |                                                                               |
| Edge labels                          | Not extracted                                                                                                                                              | cut_position, result_type, measure_delta, no_reentry_flag per edge.                                                                                     | MISSING        | edge_label_gap   |                                                                               |
| Bounded path length                  | Not extracted                                                                                                                                              | The return path has length bounded by a function of \|B\| and p.                                                                                        | MISSING        | finite_graph_gap | Referenced in A92 description but no bound is extracted.                      |
| First changed endpoint               | `docs/final/F11_weighted_cut_selection_extraction.md` §F11.7 proof sketch                                                                                  | The first vertex along the return path where the internal endpoint set of B differs from the previous vertex.                                           | MISSING        | definition_gap   | Used by A91 and A94.                                                          |
| No-reentry certificate schema        | Referenced in `docs/analytic_f9_f11_mutual_induction_convention.md` §Mutual Induction Interface Lemma                                                      | A formal certificate that NW1 cannot re-enter W(j) with j >= m at equal-or-larger M_NW\*.                                                               | MISSING        | no_reentry_gap   | No definition, schema, or construction exists anywhere in the docs.           |
| Parent-support annotation            | `docs/final/F11_weighted_cut_selection_extraction.md` §F11.11 R2                                                                                           | An annotation recording the measure of NW0 and the interval of B that entered the weighted branch.                                                      | MISSING        | measure_gap      | Needed to compare NW1 against NW0 rather than against Wwin.                   |
| M_NW\*(NW1) < M_NW\*(NW0) comparison | `docs/analytic_weighted_to_nonweighted_exit_decrease_table.md` §1, `docs/analytic_f9_f11_mutual_induction_convention.md` §Mutual Induction Interface Lemma | Proof that each NW exit edge carries strict M_NW\* decrease relative to the entering parent NW0.                                                        | MISSING        | measure_gap      | Current W-to-NW table compares against Wwin, not NW0.                         |
| A92 dependency graph position        | `docs/analytic_a90_a94_formalization_obligation_ledger.md` §Dependency graph                                                                               | A92 is foundational: A91 and A94 depend on it.                                                                                                          | DEFINED        | none             | Dependency structure is well-understood.                                      |

## Minimal example schema

Below is a pseudo-schema for one return-path certificate in the persistent cut-rigidity branch. This is a PROPOSED template, not a proved certificate format.

```text
return_path_id: a92_example_1
parent_state:
  NW0_id: nw_17_31_5
  M_NW*(NW0): (span=7, gap=0, support=5, recur_depth=2, pair_depth=0, sep_depth=1, bridge_depth=0, type_rank=3, boundary_rank=2, h_excess=0)
entry_weighted_state:
  W_id: w_m5_p31
  m: 5
  B: [b1, b2, b3, b4, b5]
  weak_cut_rigid: true
vertices:
  - v_entry
  - v_cut_1_4    (B = b1 | b2 b3 b4 b5)
  - v_cut_2_3    (B = b1 b2 | b3 b4 b5)
  - v_cut_3_2    (B = b1 b2 b3 | b4 b5)
  - v_cut_4_1    (B = b1 b2 b3 b4 | b5)
edges:
  - source: v_entry
    target: v_cut_1_4
    cut_position: 1
    result_type: PERSISTENT_CUT_RIGID
    measure_delta: UNKNOWN
    no_reentry_flag: false
  - source: v_cut_1_4
    target: v_cut_2_3
    cut_position: 2
    result_type: PERSISTENT_CUT_RIGID
    measure_delta: UNKNOWN
    no_reentry_flag: false
  - source: v_cut_2_3
    target: v_cut_3_2
    cut_position: 3
    result_type: PERSISTENT_CUT_RIGID
    measure_delta: UNKNOWN
    no_reentry_flag: false
  - source: v_cut_3_2
    target: v_cut_4_1
    cut_position: 4
    result_type: NW_EXIT
    measure_delta: -1  (support_size decreases by 1)
    no_reentry_flag: true
    no_reentry_certificate:
      excludes_W_j: "j >= 5"
      basis: "containment lemma: support(NW1) <= m < m+1 <= support(Wwin)"
      earlier_coordinates_nonincrease: PROPOSED (not yet proved)
  - source: v_cut_4_1
    target: v_NW_exit
    result_type: NW_EXIT
    measure_delta: -1
terminal_type: non_terminal (NW1 output)
measure_comparison: M_NW*(NW1) < M_NW*(NW0) ? PROPOSED (support_size decreases, earlier coordinates need verification)
no_reentry_certificate: PROPOSED (support-based containment)
verdict: PERSISTENT_CUT_RIGID → requires A90-A94 chain for full certification
```

## Summary of gaps

| Gap                                                              | Severity | Needed to close                                                          |
| ---------------------------------------------------------------- | -------- | ------------------------------------------------------------------------ |
| Finite return-path graph not defined                             | BLOCKER  | A92 must define vertices, edges, labels, and bounded-length proof.       |
| No-reentry certificate schema missing                            | BLOCKER  | Required for interface option 5. Needs formal schema and construction.   |
| Parent-support annotation format missing                         | HIGH     | Required to compare NW1 against NW0 instead of Wwin.                     |
| M_NW\*(NW1) < M_NW\*(NW0) not proved for persistent cut-rigidity | HIGH     | Core obligation of the A90-A94 chain.                                    |
| Weak cut-rigidity definition partially informal                  | MEDIUM   | F11.5 uses "doubled middle" and "routed exit" without formal definition. |
| First changed endpoint undefined                                 | MEDIUM   | Used by A91/A94 proof sketch but not formally defined.                   |
| Self-return path minimality undefined                            | MEDIUM   | Used by A94 but not defined.                                             |

## Next recommended small task

Formalize the vertex set and edge set of the finite return-path graph model for a weakly cut-rigid weighted core with |B| >= 2. This is the minimal first step: without a vertex/edge definition, A92 cannot be stated as a lemma.
