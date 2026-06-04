# A92 no-reentry certificate schema

## Purpose

This document defines the proposed schema for the no-reentry certificate required by A92 and the F9/F11 mutual-induction interface. It specifies what a certificate must contain, which inputs it requires, what exclusion bases it may use, and how it attaches to an A92 return-path graph edge. It does not prove that any such certificate exists.

## Claim boundary

This document does not prove the no-reentry certificate exists, does not prove A92, does not close F11, does not close the F9/F11 mutual-induction interface, and does not prove Erdős 475. All definitions in this document are PROPOSED unless explicitly marked DEFINED. No claim is PROVED unless an explicit proof exists in the docs read this session.

## Interface role

The F9/F11 mutual-induction interface (defined in `docs/analytic_f9_f11_mutual_induction_convention.md` §Mutual Induction Interface Lemma) requires that every weighted-core invocation from a non-weighted parent state NW0 returns one of:

1. SUCCESS;
2. CONTRADICTION or COLLAPSE;
3. W(m') with m' < m;
4. NW1 with M_NW\*(NW1) < M_NW\*(NW0);
5. NW1 with a formal no-reentry certificate excluding W(j), j >= m, at equal-or-larger M_NW\*.

The no-reentry certificate is the mechanism for option 5. It is required when the returned non-weighted state NW1 does NOT satisfy strict M_NW\* decrease relative to NW0. In that case, the certificate must prove that NW1 cannot later re-enter a weighted core W(j) with middle length j >= m at equal-or-larger M_NW\*.

The A92 return-path graph schema (`docs/analytic_a92_return_path_graph_schema.md`) attaches no-reentry certificates to NONWEIGHTED_NO_REENTRY output classifications at the graph-edge level. Each such edge must carry a `no_reentry_status: true` label with a referenced certificate.

## Required inputs

The following inputs are required to construct or verify a no-reentry certificate.

| Input                                  | Definition                                                                                              | Location                                                                                | Status  |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------- |
| Parent non-weighted state NW0          | The non-weighted obstruction state that entered the weighted branch W(m).                               | `docs/analytic_f9_f11_mutual_induction_convention.md` §Problem                          | DEFINED |
| Parent measure M_NW\*(NW0)             | The 10-coordinate non-weighted lexicographic measure of NW0.                                            | `docs/final/F09_nonweighted_termination_theorem.md` §F9.2                               | DEFINED |
| Weighted entry state W(m)              | A genuine weighted-core state with middle length m = \|B\|.                                             | `docs/final/F11_weighted_cut_selection_extraction.md` §F11.2                            | DEFINED |
| Entry middle length m                  | m = \|B\| at the weighted entry.                                                                        | `docs/final/F11_weighted_cut_selection_extraction.md` §F11.2                            | DEFINED |
| Returned non-weighted state NW1        | The non-weighted obstruction class produced by a weighted-core exit.                                    | Implicit in W(m) → NW1 transitions                                                      | PARTIAL |
| Returned measure M_NW\*(NW1)           | The 10-coordinate non-weighted lexicographic measure of NW1.                                            | `docs/final/F09_nonweighted_termination_theorem.md` §F9.2                               | DEFINED |
| Candidate re-entry weighted state W(j) | A hypothetical weighted core with middle length j that NW1 might later enter.                           | Not explicitly defined as a formal object                                               | MISSING |
| Forbidden re-entry range               | j >= m, i.e., any weighted core with middle length >= the original entry middle.                        | `docs/analytic_f9_f11_mutual_induction_convention.md` §Mutual Induction Interface Lemma | DEFINED |
| Comparison M_NW\*(NW1) vs M_NW\*(NW0)  | Whether the returned measure is strictly less, equal, or greater.                                       | Must be computed from coordinates                                                       | DEFINED |
| Weighted window Wwin                   | The displayed segment A B C where A+2B+C=0, active support inside smallest interval containing A, B, C. | `docs/analytic_weighted_to_nonweighted_exit_decrease_table.md` §2                       | DEFINED |

## Certificate object

Define a proposed certificate object:

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

## Certificate fields

| Field                 | Meaning                                                                         | Required? | Status   | Gap type       | Notes                                                               |
| --------------------- | ------------------------------------------------------------------------------- | --------- | -------- | -------------- | ------------------------------------------------------------------- |
| parent_id             | Identifier of the non-weighted parent state NW0.                                | REQUIRED  | PROPOSED | none           | Links certificate to the A92 graph entry.                           |
| child_id              | Identifier of the returned non-weighted state NW1.                              | REQUIRED  | PROPOSED | none           | Links certificate to the A92 graph edge.                            |
| entry_m               | The middle length m of the original weighted entry W(m).                        | REQUIRED  | DEFINED  | none           | m = \|B\| from the weighted entry.                                  |
| forbidden_j_range     | The range of forbidden middle lengths, always j >= m.                           | REQUIRED  | DEFINED  | none           | Taken from mutual-induction interface.                              |
| parent_measure        | M_NW\*(NW0) as a 10-tuple.                                                      | REQUIRED  | DEFINED  | none           | Defined in F9.2.                                                    |
| child_measure         | M_NW\*(NW1) as a 10-tuple.                                                      | REQUIRED  | DEFINED  | none           | Defined in F9.2.                                                    |
| measure_comparison    | Whether M_NW\*(NW1) < M_NW\*(NW0), equal, or greater at each coordinate.        | REQUIRED  | DEFINED  | none           | Must be computed per coordinate.                                    |
| exclusion_basis       | The specific structural reason NW1 cannot re-enter W(j) for j >= m.             | REQUIRED  | MISSING  | definition_gap | Core of the certificate. See exclusion bases below.                 |
| checked_coordinates   | Which M_NW\* coordinates were verified to forbid re-entry.                      | REQUIRED  | PROPOSED | measure_gap    | At minimum, enclosing_span, support_size, type_rank, boundary_rank. |
| blocked_reentry_types | Which weighted-core entry conditions are blocked (e.g., A56, A81, A97, F6, F7). | REQUIRED  | PROPOSED | routing_gap    | Must cover all entry conditions for weighted cores with j >= m.     |
| theorem_sources       | List of citations to theorems used in the exclusion basis.                      | REQUIRED  | PROPOSED | proof_gap      | Each exclusion claim must cite a proved or asserted theorem.        |
| proof_status          | One of: PROVED, ASSERTED, PROPOSED, MISSING.                                    | REQUIRED  | PROPOSED | none           | Records the verification status of this certificate.                |

## Exclusion bases

The following are possible exclusion bases. Each is a structural reason why NW1 cannot re-enter a weighted core W(j) with j >= m. All are PROPOSED unless proved in existing docs.

### 1. Support containment exclusion (PROPOSED)

**What it must prove**: The active support of NW1 is strictly contained within the middle block B of the original weighted window Wwin. Therefore any weighted core W(j) that NW1 could later enter would need a middle block whose atoms are a subset of support(NW1), so j <= |support(NW1)| <= m. Since j must be >= m for a forbidden re-entry, the only possibility is j = m with exact support equality, but same-middle weighted return requires the return to be pattern-rigid, and pattern-rigid returns are impossible (A89/F11.7).

**M_NW\* coordinate**: support_size. Containment lemma gives support_size(NW1) <= m < m+1 <= support_size(Wwin).

**Current docs**: The containment lemma exists in `docs/analytic_weighted_to_nonweighted_exit_decrease_table.md` §3. It proves support(Wwin) >= m+1. It does not prove support(NW1) subset B — that requires per-row analysis of each W-to-NW exit type.

**Status**: PARTIAL — containment lemma exists, but per-row verification that NW1 support is contained in B is not complete.

### 2. Span decrease exclusion (PROPOSED)

**What it must prove**: The enclosing_span of NW1 is strictly smaller than the enclosing_span of NW0. Any weighted core W(j) has an enclosing span at least the size of its middle block j. For j >= m, the enclosing span would be at least m, and the smaller enclosing_span of NW1 prevents forming a window large enough to contain a genuine weighted core with j >= m.

**M_NW\* coordinate**: enclosing_span.

**Current docs**: The W-to-NW exit table rows claim enclosing_span decrease for specific exit types (E2, E3, E13, E14, E16, E17) but mark them YELLOW pending earlier-coordinate non-increase verification.

**Status**: YELLOW — class-claimed but not edge-certified.

### 3. Middle-length incompatibility (PROPOSED)

**What it must prove**: The returned NW1 has structural properties that are incompatible with forming a weighted core of middle length j >= m. For example, if NW1 is a zero-composite or equal-interval state, its configuration cannot support the A+2B+C=0 equation with middle length >= m because the required coefficient-2 relation would exceed available atom multiplicity.

**M_NW\* coordinate**: type_rank or boundary_rank.

**Current docs**: No explicit argument exists linking specific non-weighted class configurations to weighted-core middle-length bounds.

**Status**: MISSING.

### 4. Boundary-rank obstruction (PROPOSED)

**What it must prove**: The boundary_rank of NW1 is low enough that any hypothetical weighted core W(j) reachable from NW1 would violate the boundary-rank ordering of non-weighted classes (F9.2, C10.5 table). A re-entry to W(j) would require boundary_rank to increase, contradicting the guaranteed decrease or stability of boundary_rank under non-weighted routing.

**M_NW\* coordinate**: boundary_rank.

**Current docs**: Boundary rank is defined in F9.2 and C10.5. No argument connecting boundary rank to weighted-core re-entry exists.

**Status**: MISSING.

### 5. Type-rank obstruction (PROPOSED)

**What it must prove**: The type_rank of NW1 is strictly lower than the minimum type_rank needed to enter a weighted core W(j) with j >= m. Re-entry would require NW1 to first increase its type_rank (impossible in non-weighted routing) or to directly transition to a weighted class (which would require an intermediate increase).

**M_NW\* coordinate**: type_rank.

**Current docs**: Type rank is defined in F9.2 and C10.3. No argument connecting type rank to weighted-core entry conditions exists.

**Status**: MISSING.

### 6. Recurrence-depth obstruction (PROPOSED)

**What it must prove**: If NW1 has positive recurrence_depth, then the recurrence routing theorem (F7) ensures that any subsequent path either decreases M_NW\* or terminates, preventing sustained re-entry to a weighted core at the same or larger M_NW\* level.

**M_NW\* coordinate**: recurrence_depth.

**Current docs**: F7 claims class routing for recurrence states. No explicit no-reentry argument is made.

**Status**: MISSING.

### 7. Routing incompatibility (PROPOSED)

**What it must prove**: The specific non-weighted class of NW1 (e.g., TWO_PIECE_ZERO, EQUAL_INTERVAL, SEPARATED_EQUAL, BRIDGE_GAP) has no admissible transition to any weighted core entry condition (A56, A81, A97, F6, F7 weighted exits). Every routing path from NW1 terminates, decreases M_NW\*, or enters a weighted core W(j) with j < m.

**M_NW\* coordinate**: N/A (uses class routing graph).

**Current docs**: The F4-F9 theorem suite and weighted-exit audit interface enumerate WEIGHTED_EXIT conditions per source theorem. A comprehensive mapping from every non-weighted class to its weighted-entry eligibility does not exist.

**Status**: MISSING.

## Verification conditions

A valid no-reentry certificate must satisfy all of the following conditions.

| #   | Condition                                                                                                                      | Required evidence                                                                     | Current status |
| --- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- | -------------- |
| 1   | NW1 is the actual child produced by an A92 graph edge.                                                                         | Graph edge label referenced by child_id must match the A92 return-path graph.         | PROPOSED       |
| 2   | entry_m = m from the parent weighted state W(m).                                                                               | Weighted entry identifier referenced by parent_id must be consistent.                 | DEFINED        |
| 3   | The forbidden range is j >= m.                                                                                                 | Must match mutual-induction interface specification.                                  | DEFINED        |
| 4   | Either M_NW\*(NW1) < M_NW\*(NW0), or if not, the certificate excludes all re-entry W(j) with j >= m at equal-or-larger M_NW\*. | Measure comparison must be computed; exclusion basis must cover all entry conditions. | PROPOSED       |
| 5   | The exclusion basis is tied to explicit M_NW\* coordinates or structural invariants.                                           | Each exclusion base must cite specific coordinates or class-routing properties.       | MISSING        |
| 6   | Every theorem source used is cited and its proof_status is PROVED or ASSERTED.                                                 | Theorem_sources field must contain valid citations.                                   | PROPOSED       |
| 7   | No required field is UNKNOWN or MISSING.                                                                                       | All fields must be populated.                                                         | MISSING        |

Condition 4 is the critical disjunction: if M_NW\*(NW1) < M_NW\*(NW0) already holds, the certificate is not needed (the edge classifies as NONWEIGHTED_DECREASE instead). If it does not hold, the certificate must provide positive proof that no re-entry to W(j) with j >= m is possible.

## Pseudo-schema

```text
no_reentry_certificate_id: nrc_a92_example_1
parent:
  NW0_id: nw_17_31_5
  M_NW_star_NW0: [7, 0, 5, 2, 0, 1, 0, 3, 2, 0]
weighted_entry:
  W_id: w_m5_p31
  m: 5
child:
  NW1_id: nw_exit_two_piece_zero
  M_NW_star_NW1: [7, 0, 4, 0, 0, 0, 0, 2, 1, 0]
forbidden_reentry:
  j_min: 5
  j_range: "j >= 5"
  excluded_weighted_states:
    - W(5): "same-middle return requires pattern-rigidity, impossible by A89/F11.7"
    - W(j>5): "support_size(NW1)=4 < 5 <= j, cannot support middle of length >=5"
exclusion_basis: support_containment
  type: support_containment
  coordinate: support_size
  inequality: "support_size(NW1)=4 <= m=5 < m+1=6 <= support_size(Wwin)"
  theorem_source: "Containment lemma, docs/analytic_weighted_to_nonweighted_exit_decrease_table.md §3"
  coverage:
    - "same-middle (j=m): blocked by A89 pattern-rigid impossibility"
    - "larger-middle (j>m): blocked by support_size insufficiency"
checked_coordinates:
  enclosing_span: "7 <= 7 (equal, not increasing)"
  gap_length: "0 <= 0 (equal, not increasing)"
  support_size: "4 < 5 (strict decrease)"
  recurrence_depth: "0 <= 2 (decrease)"
  pair_depth: "0 <= 0 (equal)"
  separated_depth: "0 <= 1 (decrease)"
  bridge_depth: "0 <= 0 (equal)"
  type_rank: "2 < 3 (decrease)"
  boundary_rank: "1 < 2 (decrease)"
  h_excess: "0 <= 0 (equal)"
blocked_reentry_types:
  - A56 easy reduction: "support_size 4 insufficient for coefficient-2 with j>=5"
  - A81 atom-middle: "j>=5 requires |B|>=5, support_size 4 cannot provide"
  - A97 cut-swap: "middle length j>=5 incompatible with support span"
  - F6 external collision: "requires active support larger than NW1"
  - F7 recurrence: "recurrence_depth=0, no recurrence chain available"
theorem_sources:
  - "Containment lemma: analytic_weighted_to_nonweighted_exit_decrease_table.md §3"
  - "A89/F11.7: pattern-rigid self-return is impossible"
  - "F9.2: M_NW* coordinate definitions"
proof_status: PROPOSED
verification:
  child_matches_edge: true
  forbidden_range_checked: true
  source_theorems_cited: true
  all_required_fields_known: false
  notes: "blocked_reentry_types entries are heuristic — no formal proof that each entry condition is blocked by support_size alone"
verdict: PROPOSED — not yet certified
```

## Attachment to A92 graph edge

A no-reentry certificate attaches to a single A92 graph edge as follows:

1. The edge's `no_reentry_status` label field must be `true`.
2. The edge's `no_reentry_certificate_id` label field must reference the certificate's identifier.
3. The certificate's `parent_id` must match the graph's `parent.NW0_id`.
4. The certificate's `child_id` must match the edge's target vertex.
5. The certificate's `entry_m` must match the edge's `m_before`.

If any of these consistency checks fail, the certificate is not valid for that edge.
