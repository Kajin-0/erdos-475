# F00.SNS.C9 phase-aware global measure

This file continues the strong nonzero-sum repair path.

C8 assembled the conditional strong nonzero-sum theorem and identified the remaining global task:

```text
Define one global well-founded measure for ARBITRARY-phase SNS repair
and map every C1--C7 branch to strict descent, terminal success, or an explicitly unresolved edge.
```

C9 defines that measure and gives the first edge table.

Status: global-measure draft.  It is not yet a complete termination proof.

---

## C9.1. Phase-aware state

Use the phase-aware state

```text
Omega=(R,I,C,E,M,tag,phase)
```

where

```text
phase in {ARBITRARY,COLLISION_FREE}.
```

For the strong nonzero-sum proof:

```text
ARBITRARY      = endpoint collisions may exist;
COLLISION_FREE = no endpoint collisions exist, hence SNS success.
```

---

## C9.2. Primary global defect

For an ordering `R`, define the collision profile

```text
P_col(R)=(N_1(R),N_2(R),...,N_t(R)),
```

where

```text
N_s(R)=number of endpoint collision pairs (i,j) with j-i=s.
```

Let

```text
L_col^*(R)=(t+1-i,t+1-j)
```

where `(i,j)` is the lexicographically first shortest collision.  If no collision exists, use sentinel value `(0,0)`.

The primary global defect is

```text
D_SNS^*(R)=(P_col(R),L_col^*(R),boundary_rank(R)).
```

The profile `P_col` is ordered lexicographically from small spans to large spans.

---

## C9.3. Local repair measure

For a local repair state, define

```text
M_loc=(
  enclosing_span,
  gap_length,
  support_size,
  bridge_depth,
  pair_depth,
  separated_depth,
  type_rank,
  boundary_rank_loc
).
```

Definitions:

```text
enclosing_span    = smallest atom interval containing active local support;
gap_length        = separated/bridge gap length, otherwise 0;
support_size      = number of active atoms in the local obstruction;
bridge_depth      = consecutive bridge returns at fixed D_SNS^*;
pair_depth        = consecutive pair/signed returns at fixed D_SNS^*;
separated_depth   = consecutive separated-equal returns at fixed D_SNS^*;
type_rank         = finite obstruction-class rank;
boundary_rank_loc = finite endpoint-degeneracy rank.
```

All coordinates are nonnegative integers.

---

## C9.4. Weighted repair measure

For a weighted repair state

```text
A+2B+C=0,
```

define

```text
M_w=(|B|, M_loc).
```

The weighted middle length `|B|` is subordinate to `D_SNS^*`.  It is used only after the global collision profile is fixed.

---

## C9.5. Full phase-aware measure

## Definition C9.1: global phase-aware measure

In ARBITRARY phase, define

```text
M_phase(Omega)=(
  D_SNS^*(R),
  phase_rank,
  M_loc,
  M_w,
  transition_budget
).
```

Use lexicographic order.

Set

```text
phase_rank(ARBITRARY)=1,
phase_rank(COLLISION_FREE)=0.
```

`COLLISION_FREE` is terminal SNS success, so no further descent is needed.

The coordinate `transition_budget` is a finite local tie-breaker used only inside a fixed finite q-through-Z insertion sequence or fixed cut-swap table.

---

## Lemma C9.2: M_phase is well-founded

The measure `M_phase` is well-founded.

### Proof

Each coordinate is a finite tuple of nonnegative integers.  Lexicographic order on finite products of well-ordered finite integer ranges is well-founded. ∎

---

## C9.6. Terminal states

Terminal states are:

```text
COLLISION_FREE success;
atom-zero contradiction;
duplicate atom-label contradiction;
violation of S subset F_p^*;
sigma(S)=0 contradiction inside the nonzero-total SNS theorem.
```

A zero interval is not terminal in ARBITRARY phase.

---

## C9.7. Edge table: q-through-Z start

| Branch | Source | Output | Measure effect | Status |
|---|---|---|---|---|
| Strongly clean insertion | C1 | repaired active collision | strict `D_SNS^*` descent | hardened at C1 level |
| Local moved collision | C2/C4 | local zero/equal/signed repair | enters C5 with controlled `M_loc` | needs full edge inequalities |
| External moved collision | C2/C4 | bridge/external repair | enters C5/F6/F8 | needs phase-aware bridge audit |
| Weighted normal form | C2/C4 | weighted repair | enters C6/C7 | conditional |
| Collision-free insertion | C4 | SNS success | terminal | clean |
| Boundary degeneracy | C2 | endpoint/boundary repair | lower `boundary_rank` or contradiction | needs final convention |

---

## C9.8. Edge table: phase-aware local repair

| Branch | Output | Measure effect | Status |
|---|---|---|---|
| Zero interval of smaller span | contradiction to `D_SNS^*` minimality | impossible | clean |
| Zero interval same span earlier | contradiction to active choice | impossible | clean |
| Zero interval same span later | active repair state | `L_col^*` lower after repair required | needs bookkeeping |
| Proper-overlap equal interval | smaller local enclosure | `M_loc` descent | mostly clean |
| Proper-containment equal interval | smaller support | `M_loc` descent | mostly clean |
| Pair/signed relation | pair repair | `pair_depth/type_rank` descent or route | needs rank table |
| Transported prefix | local or weighted repair | route to C6 if genuine | conditional |

---

## C9.9. Edge table: separated and bridge/gap repair

| Branch | Output | Measure effect | Status |
|---|---|---|---|
| Gap-after success | smaller gap | `gap_length` descent | clean |
| Gap-after displayed collision | local repair | C5/C4 routing | needs table |
| Direct exchange success | local success or profile descent | `D_SNS^*`/`M_loc` descent | needs SNS interpretation |
| Proper bridge overlap | smaller enclosure | `M_loc` descent | clean |
| Proper bridge containment | smaller support | `M_loc` descent | clean |
| Gap-preserving recurrence analogue | rigid separated return | route to direct exchange or local repair | needs SNS collision-only rewrite |
| External bridge | bridge repair | F6/F8 phase-aware route | conditional |

---

## C9.10. Edge table: weighted repair

| Branch | Output | Measure effect | Status |
|---|---|---|---|
| Easy weighted reduction | non-weighted repair | exits C6 to C5 | clean algebra, phase audit needed |
| Fixed cut-swap success | collision-free success | terminal | clean |
| Fixed cut-swap displayed collision | local repair | C5 route | table from F10 reusable |
| Fixed cut-swap external collision | external/bridge repair | C5/F6/F8 route | conditional |
| Smaller middle | weighted repair | `|B|` descent at fixed `D_SNS^*` | clean |
| Weak cut-rigid non-pattern return | local/external/defect descent | C7 route | needs C7.2--C7.4 |
| Pattern-rigid return | zero defect or exits genuine weighted state | exits to C5 | algebra clean, phase audit needed |

---

## C9.11. Conditional global termination theorem

## Theorem C9.3: phase-aware global termination, conditional

Assume:

```text
1. every C5 local repair edge either decreases M_phase or exits to a listed branch;
2. every C6 weighted repair edge either decreases M_phase or exits to C5/C8 success;
3. C7 weak cut-rigidity hardening is valid;
4. all finite rank tables are explicitly defined;
5. boundary-rank convention is fixed so useful interior insertions do not worsen rank.
```

Then no ARBITRARY-phase SNS repair path can be infinite at fixed `D_SNS^*`.  Therefore every defect-minimal start either reaches COLLISION_FREE success or contradicts the fixed assumptions.

### Proof

Every transition appears in one of the edge tables C9.7--C9.10.  By assumptions 1--5, each nonterminal transition strictly decreases `M_phase` or enters a branch whose next transition decreases `M_phase`.  Since `M_phase` is well-founded, no infinite nonterminal repair path exists. ∎

---

## C9.12. What C9 resolves

Resolved:

```text
1. one global phase-aware measure is proposed;
2. zero intervals are handled as defects in ARBITRARY phase;
3. q-through-Z, local, bridge, and weighted branches are placed in one descent table;
4. remaining hardening items are now edge-table obligations, not vague architecture gaps.
```

Not resolved:

```text
1. explicit finite type_rank table;
2. explicit finite boundary_rank table;
3. full C5 local edge inequalities;
4. full C7 weak cut-rigidity hardening;
5. proof that every edge table row strictly descends M_phase or exits terminally.
```

---

## C9.13. Recommended next file

The next useful file should define the finite rank tables:

```text
docs/final/F00_SNS_C10_rank_tables.md
```

Goal:

```text
Make type_rank, boundary_rank, and local-depth ranks explicit so C9 can become a real termination theorem instead of a measure proposal.
```

---

## C9.14. Status

```text
Status: global-measure draft.
Risk: ORANGE/RED.
Current remaining gap: turn edge-table obligations into explicit rank/descent lemmas.
```
