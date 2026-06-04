# A92 no-reentry certificate instances

## Purpose

This document constructs concrete no-reentry certificate instances for the three W-to-NW exit rows where support containment is confirmed: E15 (R_k'=P_j', two-piece zero inside B), E18 (R_k=P_j, equal-prefix inside B), and E19 (R_k^+=P_j^+, equal-tail inside B). Each instance follows the schema defined in `docs/analytic_a92_no_reentry_certificate_schema.md`.

## Claim boundary

This document does not prove that any certificate is fully verified, does not prove A92, does not close F11, does not close the F9/F11 mutual-induction interface, and does not prove Erdős 475. All certificate instances are PROPOSED. Each instance documents its proof_status per field. No instance is PROVED unless every required field is PROVED or DEFINED.

## Certificate structure

Each certificate uses the C_no_reentry object:

```text
C_no_reentry = (
  parent_id,
  child_id,
  entry_m,
  forbidden_j_range,
  parent_measure,
  child_measure,
  measure_comparison,
  exclusion_basis,
  checked_coordinates,
  blocked_reentry_types,
  theorem_sources,
  proof_status
)
```

---

## Instance 1: E15 — R_k'=P_j' (two-piece zero inside B)

### Source

A97.3/6. The fixed cut-swap `A P R C -> A R P C` produces a displayed collision R_k' = P_j', where R_k' is a moved R endpoint and P_j' is a moved P endpoint. Since P, R ⊆ B, both endpoints lie inside B. The equation P_j + R_k^+ = 0 is a two-piece zero relation strictly inside B.

### Certificate

```text
no_reentry_certificate_id: nrc_e15_inside_B_two_piece_zero
parent:
  NW0_id: nw_<p>_<instance>
  M_NW_star_NW0: [enc_span_NW0, gap_NW0, support_NW0, r_depth_NW0, p_depth_NW0, s_depth_NW0, b_depth_NW0, t_rank_NW0, b_rank_NW0, h_excess_NW0]
weighted_entry:
  W_id: w_<p>_<m>
  m: <m>
child:
  NW1_id: nw_two_piece_zero_inside_B
  NW1_class: TWO_PIECE_ZERO
  M_NW_star_NW1: [enc_span_NW1, gap_NW1, support_NW1, r_depth_NW1, p_depth_NW1, s_depth_NW1, b_depth_NW1, t_rank_NW1, b_rank_NW1, h_excess_NW1]
forbidden_reentry:
  j_min: <m>
  j_range: "j >= <m>"
  excluded_weighted_states:
    - W(<m>): "same-middle return blocked — support_size(NW1) < m (strict), cannot support middle of length m"
    - W(j > <m>): "support_size(NW1) < m < j, cannot support middle of length >= m+1"
exclusion_basis:
  type: support_containment
  subtype: strict_inside_B
  coordinate: support_size
  basis_detail: "R_k'=P_j': both R_k' and P_j' are endpoints of P and R, which partition B.
    The two-piece zero equation P_j + R_k^+ = 0 involves only atoms from P and R.
    Therefore support(NW1) ⊆ B and support_size(NW1) <= max(|P_j atoms|, |R_k^+ atoms|).
    Since P and R are nonempty proper subblocks of B, |P| < m and |R| < m.
    The atoms involved are a subset of P∪R = B, but the collision identifies specific
    endpoints rather than using all atoms of B. Result: support_size(NW1) < m (strict)."
  inequality: "support_size(NW1) < m < m+1 <= support_size(Wwin)"
  lemma_source: "Containment lemma, docs/analytic_weighted_to_nonweighted_exit_decrease_table.md §3"
  coverage:
    same_middle_j_eq_m: "BLOCKED by support_size(NW1) < m: any weighted core W(m) needs middle length m,
      which requires |support(W(m))| >= m. But support(NW1) < m, so NW1 cannot provide
      enough active atoms to form a middle block of length m. Even if NW1 later acquires
      atoms via recombination, the M_NW* measure would strictly decrease first
      (enclosing_span or support_size would need to increase to reach m, contradicting
      the non-weighted termination guarantee of F9)."
    larger_middle_j_gt_m: "BLOCKED by support_size(NW1) < m < j: even more insufficient support."
checked_coordinates:
  enclosing_span: "enc_span(NW1) <= enc_span(NW0) — PROPOSED, requires verification that
    the two-piece zero inside B does not extend the enclosing span beyond NW0's span.
    Since support(NW1) ⊆ B ⊆ Wwin ⊆ Enc_W, and Enc_W is typically within or equal to
    enc_span(NW0), this is expected but not yet proved."
  gap_length: "gap(NW1) <= gap(NW0) — PROPOSED. TWO_PIECE_ZERO has gap_length = 0
    (no separated gap), so gap(NW1) = 0 <= gap(NW0) always."
  support_size: "support_size(NW1) < m — PROPOSED strict (see basis_detail above).
    This is the primary decreasing coordinate."
blocked_reentry_types:
  - A56 easy reduction: "A56 weighted entry requires a genuine coefficient-2 normal form
    with middle length >= m. support_size(NW1) < m makes this impossible because the
    middle block would need at least m atoms, but NW1 has fewer."
  - A81 atom-middle: "Atom-middle case requires |B| >= 1. Any atom-middle weighted entry
    from NW1 would need at least one atom, but the weighted core condition A+2B+C=0
    with B nonempty requires the full window structure. support(NW1) ⊆ B with
    |support(NW1)| < m < |B| of the original core, and forming a new A+2B+C=0 equation
    with j>=m would require more atoms than NW1 has."
  - A97 cut-swap: "A cut-swap weighted return with j>=m requires the returned middle
    to have length >= m. support(NW1) < m atoms makes this structurally impossible
    for NW1 alone. Any weighted re-entry would first need NW1 to acquire atoms
    through non-weighted routing, which would strictly decrease M_NW*."
  - F6 external collision: "F6 external collision weighted entry requires active support
    extending outside the original weighted window. support(NW1) ⊆ B removes this
    possibility — all atoms are inside B, so no external collision is possible."
  - F7 recurrence: "F7 recurrence weighted entry requires a forbidden hit in moved
    endpoint families (x+a+R_k=f or x+a+r+P_j=f). The external endpoint x is outside
    the support of NW1, and recurrence routing would first decrease M_NW*."
theorem_sources:
  - "Containment lemma: docs/analytic_weighted_to_nonweighted_exit_decrease_table.md §3"
  - "A97.3/6: docs/final/F10_weighted_normal_form_cut_swap.md §Lemma F10.3"
  - "F11.3: docs/final/F11_weighted_cut_selection_extraction.md §Lemma F11.3"
  - "F9.2: M_NW* coordinate definitions: docs/final/F09_nonweighted_termination_theorem.md §F9.2"
proof_status: PROPOSED
verification:
  child_matches_edge: true
  forbidden_range_checked: true
  source_theorems_cited: true
  all_required_fields_known: false
  missing_fields:
    - M_NW_star_NW0 (depends on concrete instance)
    - M_NW_star_NW1 (depends on concrete instance)
    - checked_coordinates enclosing_span comparison (needs per-instance verification)
    - checked_coordinates support_size strictness (needs per-instance verification of strictness)
    - blocked_reentry_types formal proof (currently heuristic)
  notes: "The structural argument that support_size(NW1) < m is sound for the strict-inside-B
    case. Remaining gaps: (1) per-instance measure coordinates, (2) formal proof that each
    blocked_reentry_type is truly impossible given support ⊆ B with strict size < m,
    (3) earlier-coordinate non-increase (span, gap) verification."
verdict: PROPOSED — structurally argued, not yet formally certified
```

---

## Instance 2: E18 — R_k=P_j (equal-prefix / separated-equal, support inside B)

### Source

A97.7. The moved R endpoint value equals an old P endpoint value: R_k = P_j. Both R_k and P_j are subblocks of B. The output is an equal-prefix relation (or separated-equal if the corresponding intervals are non-adjacent). Support is contained inside B.

Unlike E15, the support_size bound is <= m (not strict), because the equal-prefix could involve atoms covering all of B's endpoints.

### Certificate

```text
no_reentry_certificate_id: nrc_e18_equal_prefix_inside_B
parent:
  NW0_id: nw_<p>_<instance>
  M_NW_star_NW0: [enc_span_NW0, gap_NW0, support_NW0, r_depth_NW0, p_depth_NW0, s_depth_NW0, b_depth_NW0, t_rank_NW0, b_rank_NW0, h_excess_NW0]
weighted_entry:
  W_id: w_<p>_<m>
  m: <m>
child:
  NW1_id: nw_equal_prefix_inside_B
  NW1_class: EQUAL_INTERVAL or SEPARATED_EQUAL
  M_NW_star_NW1: [enc_span_NW1, gap_NW1, support_NW1, r_depth_NW1, p_depth_NW1, s_depth_NW1, b_depth_NW1, t_rank_NW1, b_rank_NW1, h_excess_NW1]
forbidden_reentry:
  j_min: <m>
  j_range: "j >= <m>"
  excluded_weighted_states:
    - W(<m>): "same-middle return blocked by A89/F11.7 — equal-prefix support ⊆ B,
      so same-middle j=m would require pattern-rigidity, which is impossible"
    - W(j > <m>): "support_size(NW1) <= m < j, cannot support middle of length > m"
exclusion_basis:
  type: support_containment
  subtype: inside_B_with_same_middle_A89
  coordinate: support_size
  basis_detail: "R_k = P_j: the moved R family endpoint equals an old P family endpoint.
    Both R and P are subblocks of B (B = P R), so the equal-prefix relation is contained
    inside B. Therefore support(NW1) ⊆ B and support_size(NW1) <= m.
    For j > m: support_size(NW1) <= m < j, so any W(j) with j > m is impossible.
    For j = m: if support_size(NW1) = m and support(NW1) = B (covers all atoms of B),
    support_size alone does not exclude same-middle return. However, same-middle weighted
    return from a weakly cut-rigid core requires pattern-rigidity (Definition F11.5,
    Lemma F11.6). Pattern-rigid self-return is impossible by A89/F11.7.
    Therefore j = m is also blocked."
  inequality: "support_size(NW1) <= m < m+1 <= support_size(Wwin)"
  lemma_source: "Containment lemma, docs/analytic_weighted_to_nonweighted_exit_decrease_table.md §3"
  coverage:
    same_middle_j_eq_m: "BLOCKED by A89/F11.7 (pattern-rigid impossibility), not by support_size alone.
      Relies on the fact that any same-middle weighted return from a weakly cut-rigid core
      must be pattern-rigid, and A89 proves pattern-rigid self-return is impossible."
    larger_middle_j_gt_m: "BLOCKED by support_size(NW1) <= m < j."
checked_coordinates:
  enclosing_span: "enc_span(NW1) <= enc_span(NW0) — PROPOSED. The equal-prefix inside B
    has enclosing span <= span of B, which is <= enc_span(NW0) because B is part of
    the weighted window entered from NW0. Expected but not yet proved."
  gap_length: "gap(NW1) — PROPOSED. If the equal-prefix is separated (non-adjacent
    intervals), gap_length may be > 0. Must verify gap(NW1) <= gap(NW0)."
  support_size: "support_size(NW1) <= m — PROPOSED. Not strict, but A89 handles j=m."
blocked_reentry_types:
  - A56 easy reduction: "A56 weighted entry requires a coefficient-2 normal form.
    support(NW1) ⊆ B with |support| <= m. Even if |support| = m (covers all of B),
    the weighted entry condition A+2B+C=0 requires outer blocks A and C outside B.
    NW1 has no atoms outside B, so A56 entry from NW1 into a weighted core with j>=m
    is impossible — there are no atoms to form A and C blocks."
  - A81 atom-middle: "Atom-middle weighted entry requires |B| >= 1 with the boundary
    structure A B C. For j >= m, the middle must have length >= m. The atoms available
    are inside B (support(NW1) ⊆ B). Forming a new A B C with middle length >= m and
    outer blocks A, C requires atoms outside the current support, which NW1 does not have."
  - A97 cut-swap: "A cut-swap weighted return with j>=m requires the returned middle
    to have length >= m. For j = m, this is blocked by A89. For j > m, support_size
    insufficiency blocks it."
  - F6 external collision: "External collision requires endpoints outside the displayed
    window. support(NW1) ⊆ B, so all atoms are inside the original weighted window.
    No external collision possible."
  - F7 recurrence: "F7 recurrence requires a forbidden hit involving external endpoint x.
    NW1 has no external endpoints — support is inside B."
theorem_sources:
  - "Containment lemma: docs/analytic_weighted_to_nonweighted_exit_decrease_table.md §3"
  - "A97.7: docs/final/F10_weighted_normal_form_cut_swap.md §Lemma F10.3"
  - "A89/F11.7: pattern-rigid impossibility: docs/final/F11_weighted_cut_selection_extraction.md §F11.8"
  - "F11.3: fixed cut-swap exits: docs/final/F11_weighted_cut_selection_extraction.md §Lemma F11.3"
proof_status: PROPOSED
verification:
  child_matches_edge: true
  forbidden_range_checked: true
  source_theorems_cited: true
  all_required_fields_known: false
  missing_fields:
    - M_NW_star_NW0 (depends on concrete instance)
    - M_NW_star_NW1 (depends on concrete instance)
    - gap_length comparison (depends on whether equal-prefix is separated or adjacent)
    - blocked_reentry_types formal proof (currently heuristic)
  notes: "Same-middle (j=m) relies on A89 pattern-rigid impossibility, NOT on support
    containment alone. If A89 is later weakened or revised, the j=m case would need
    a different argument. The support argument for j>m is unconditional."
verdict: PROPOSED — structurally argued, A89 dependency identified for j=m case
```

---

## Instance 3: E19 — R_k^+=P_j^+ (equal-tail / separated-equal, support inside B)

### Source

A97.8. The moved P endpoint equals an old R endpoint: R_k^+ = P_j^+. This is the symmetric counterpart of E18. Both R_k^+ and P_j^+ are endpoints of subblocks of B. The output is an equal-tail relation (or separated-equal). Support is contained inside B.

### Certificate

```text
no_reentry_certificate_id: nrc_e19_equal_tail_inside_B
parent:
  NW0_id: nw_<p>_<instance>
  M_NW_star_NW0: [enc_span_NW0, gap_NW0, support_NW0, r_depth_NW0, p_depth_NW0, s_depth_NW0, b_depth_NW0, t_rank_NW0, b_rank_NW0, h_excess_NW0]
weighted_entry:
  W_id: w_<p>_<m>
  m: <m>
child:
  NW1_id: nw_equal_tail_inside_B
  NW1_class: EQUAL_INTERVAL or SEPARATED_EQUAL
  M_NW_star_NW1: [enc_span_NW1, gap_NW1, support_NW1, r_depth_NW1, p_depth_NW1, s_depth_NW1, b_depth_NW1, t_rank_NW1, b_rank_NW1, h_excess_NW1]
forbidden_reentry:
  j_min: <m>
  j_range: "j >= <m>"
  excluded_weighted_states:
    - W(<m>): "same-middle return blocked by A89/F11.7 — equal-tail support ⊆ B,
      same-middle j=m would require pattern-rigidity, impossible by A89"
    - W(j > <m>): "support_size(NW1) <= m < j, cannot support middle of length > m"
exclusion_basis:
  type: support_containment
  subtype: inside_B_with_same_middle_A89
  coordinate: support_size
  basis_detail: "R_k^+ = P_j^+: the moved P family endpoint equals an old R family endpoint.
    This is the symmetric counterpart of E18. R_k^+ is the suffix of R, P_j^+ is the suffix of P.
    Both are subblocks of B, so the equal-tail relation is contained inside B.
    Therefore support(NW1) ⊆ B and support_size(NW1) <= m.
    For j > m: support_size(NW1) <= m < j blocks larger middle lengths.
    For j = m: same analysis as E18 — requires A89 pattern-rigid impossibility."
  inequality: "support_size(NW1) <= m < m+1 <= support_size(Wwin)"
  lemma_source: "Containment lemma, docs/analytic_weighted_to_nonweighted_exit_decrease_table.md §3"
  coverage:
    same_middle_j_eq_m: "BLOCKED by A89/F11.7, same reasoning as E18."
    larger_middle_j_gt_m: "BLOCKED by support_size(NW1) <= m < j."
checked_coordinates:
  enclosing_span: "enc_span(NW1) <= enc_span(NW0) — PROPOSED. Same reasoning as E18:
    equal-tail inside B has enclosing span <= span(B) <= enc_span(NW0)."
  gap_length: "gap(NW1) — PROPOSED. Same as E18: depends on whether separated or adjacent."
  support_size: "support_size(NW1) <= m — PROPOSED. Not strict; A89 handles j=m."
blocked_reentry_types:
  - A56 easy reduction: "Symmetric to E18: NW1 has no atoms outside B to form A and C blocks."
  - A81 atom-middle: "Symmetric to E18: insufficient atoms outside current support for middle >= m."
  - A97 cut-swap: "Symmetric to E18: j=m blocked by A89; j>m blocked by support_size."
  - F6 external collision: "Symmetric to E18: no external endpoints in support(NW1) ⊆ B."
  - F7 recurrence: "Symmetric to E18: no external endpoint x in support(NW1)."
theorem_sources:
  - "Containment lemma: docs/analytic_weighted_to_nonweighted_exit_decrease_table.md §3"
  - "A97.8: docs/final/F10_weighted_normal_form_cut_swap.md §Lemma F10.3"
  - "A89/F11.7: pattern-rigid impossibility: docs/final/F11_weighted_cut_selection_extraction.md §F11.8"
  - "F11.3: docs/final/F11_weighted_cut_selection_extraction.md §Lemma F11.3"
proof_status: PROPOSED
verification:
  child_matches_edge: true
  forbidden_range_checked: true
  source_theorems_cited: true
  all_required_fields_known: false
  missing_fields:
    - M_NW_star_NW0 (depends on concrete instance)
    - M_NW_star_NW1 (depends on concrete instance)
    - gap_length comparison (depends on separated vs adjacent)
    - blocked_reentry_types formal proof (currently heuristic)
  notes: "Structurally identical to E18. The equal-tail case is the mirror of the
    equal-prefix case. Both rely on A89 for same-middle exclusion."
verdict: PROPOSED — structurally argued, symmetric to E18
```

---

## Comparison summary

| Aspect                        | E15 (two-piece zero)                   | E18 (equal-prefix)                       | E19 (equal-tail)                 |
| ----------------------------- | -------------------------------------- | ---------------------------------------- | -------------------------------- |
| Source                        | A97.3/6                                | A97.7                                    | A97.8                            |
| Equation                      | R_k' = P_j' → P_j + R_k^+ = 0          | R_k = P_j                                | R_k^+ = P_j^+                    |
| NW class                      | TWO_PIECE_ZERO                         | EQUAL_INTERVAL / SEPARATED_EQUAL         | EQUAL_INTERVAL / SEPARATED_EQUAL |
| Support bound                 | support_size(NW1) < m (strict)         | support_size(NW1) <= m                   | support_size(NW1) <= m           |
| Same-middle (j=m) exclusion   | By strict support_size < m             | By A89/F11.7 pattern-rigid impossibility | By A89/F11.7                     |
| Larger-middle (j>m) exclusion | By support_size < m < j                | By support_size <= m < j                 | By support_size <= m < j         |
| A89 dependency                | No (strict size suffices)              | Yes (for j=m case)                       | Yes (for j=m case)               |
| Strength                      | Strongest (no external theorem needed) | Medium (needs A89)                       | Medium (needs A89)               |

## Attachment mapping

Each certificate attaches to the A92 return-path graph as specified in the schema:

```text
E15 graph edge:
  source: v_cut_<i>   (cut at position i where B = P R)
  target: v_NW_two_piece_zero
  result_type: NW_EXIT
  no_reentry_status: true
  no_reentry_certificate_id: nrc_e15_inside_B_two_piece_zero

E18 graph edge:
  source: v_cut_<i>
  target: v_NW_equal_prefix
  result_type: NW_EXIT
  no_reentry_status: true
  no_reentry_certificate_id: nrc_e18_equal_prefix_inside_B

E19 graph edge:
  source: v_cut_<i>
  target: v_NW_equal_tail
  result_type: NW_EXIT
  no_reentry_status: true
  no_reentry_certificate_id: nrc_e19_equal_tail_inside_B
```

## Remaining verification gaps

All three instances share the following gaps:

1. **Per-instance measure coordinates**: M_NW\*(NW0) and M_NW\*(NW1) depend on the concrete weighted core and exit. The certificates use placeholders (`<m>`, `<p>`, coordinate tuples) that must be filled per instance.
2. **Earlier-coordinate non-increase**: enclosing_span and gap_length comparisons between NW1 and NW0 are PROPOSED but not proved for these specific exit types. The support containment gives support_size decrease, but enclosing_span and gap_length must not increase.
3. **Blocked re-entry types formal proof**: The listed blocked_reentry_types entries are heuristic arguments that each weighted-core entry condition is incompatible with support(NW1) ⊆ B and support_size(NW1) <= m. A formal proof would need to show that no A56, A81, A97, F6, or F7 weighted entry can produce a genuine weighted core W(j) with j >= m from a non-weighted state whose support is contained within B.
4. **A89 dependency for E18 and E19**: If A89 is ever revised, the same-middle exclusion for these rows must be re-verified.
