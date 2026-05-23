# Analytic obstruction dependency graph A72

This note continues from A71.

A71 routed the last named recurrence source, cyclic-cut recurrence, into the existing obstruction framework.  The local algebraic taxonomy is now mostly closed.  The remaining task is global acyclicity: prove that the directed graph of reductions cannot cycle without strict measure descent.

This note builds the current dependency graph of obstruction classes and marks which edges are proved descending, which are routed modulo A34/global termination, and which remain open.

No complete proof is claimed here.

---

## 1. Obstruction classes

Use the following node set.

```text
SUCCESS
CONTRADICTION
ZERO_COLLAPSE
PREFIX_ZERO
TWO_PIECE_ZERO
THREE_PIECE_ZERO
HIGHER_ZERO_COMPOSITE
ZERO_COMPOSITE_SURGERY
EQUAL_INTERVAL
SIGNED_INTERVAL
SEPARATED_EQUAL
MIDPOINT
PAIR_DIFFERENCE
TRANSPORTED_PREFIX
WEIGHTED_CORE
WEIGHTED_CUT_SWAP
SINGLETON_RECURRENCE
CYCLIC_RECURRENCE
FORBIDDEN_RECURRENCE
EXTERNAL_COLLISION
GLOBAL_TERMINATION
FINITE_VERIFICATION
```

Interpretation:

- `SUCCESS`: an endpoint-avoiding Graham-valid ordering is produced.
- `CONTRADICTION`: Graham-validity/minimality/zero-atom contradiction.
- `ZERO_COLLAPSE`, `PREFIX_ZERO`: immediate zero interval or prefix-zero collapse.
- `TWO_PIECE_ZERO`, `THREE_PIECE_ZERO`, `HIGHER_ZERO_COMPOSITE`: composite zero relations.
- `ZERO_COMPOSITE_SURGERY`: A28--A33 atom-insertion/zero-block breaking mechanism.
- `EQUAL_INTERVAL`, `SIGNED_INTERVAL`, `SEPARATED_EQUAL`, `MIDPOINT`: interval geometry branches.
- `PAIR_DIFFERENCE`: A33-type pair-difference boundary.
- `TRANSPORTED_PREFIX`: coefficient-2 artifact removable by prefix/tail substitution.
- `WEIGHTED_CORE`: genuine weighted signed core `A+2B+C=0` after A56 tests.
- `WEIGHTED_CUT_SWAP`: dynamic cut-swap `A P R C -> A R P C` from A60.
- `SINGLETON_RECURRENCE`, `CYCLIC_RECURRENCE`, `FORBIDDEN_RECURRENCE`: recurrence branches.
- `EXTERNAL_COLLISION`: external collision pulled back by A62.
- `GLOBAL_TERMINATION`: desired final descent/acyclicity theorem.
- `FINITE_VERIFICATION`: small-prime/exceptional-case bridge.

---

## 2. Edge labels

Use these edge statuses.

```text
DESCENDS          strict support/span/measure descent already proved locally
COLLAPSES         zero-prefix/interior-zero/zero-atom contradiction
ROUTES            algebraically routes to another class, descent not necessarily immediate
MOD_A34           routed but may require forbidden-recurrence termination
OPEN              edge exists but still lacks a proof of existence/descent
ADVISORY          computational/finite evidence only unless certified
```

---

## 3. Core collapse edges

```text
ZERO_COLLAPSE        -> CONTRADICTION          COLLAPSES
PREFIX_ZERO          -> CONTRADICTION          COLLAPSES
TRANSPORTED_PREFIX   -> ZERO_COMPOSITE_SURGERY ROUTES
```

These are safe terminal or normalizing edges.

---

## 4. Zero-composite graph

From A28--A33, A47, A51--A53, A55, A60, and later recurrence pullbacks:

```text
TWO_PIECE_ZERO        -> ZERO_COMPOSITE_SURGERY  ROUTES
THREE_PIECE_ZERO      -> ZERO_COMPOSITE_SURGERY  ROUTES
HIGHER_ZERO_COMPOSITE -> ZERO_COMPOSITE_SURGERY  ROUTES
ZERO_COMPOSITE_SURGERY -> ZERO_COLLAPSE          COLLAPSES
ZERO_COMPOSITE_SURGERY -> TWO_PIECE_ZERO         DESCENDS
ZERO_COMPOSITE_SURGERY -> THREE_PIECE_ZERO       DESCENDS
ZERO_COMPOSITE_SURGERY -> EQUAL_INTERVAL         DESCENDS
ZERO_COMPOSITE_SURGERY -> PAIR_DIFFERENCE        ROUTES
ZERO_COMPOSITE_SURGERY -> FORBIDDEN_RECURRENCE   MOD_A34
ZERO_COMPOSITE_SURGERY -> SUCCESS                DESCENDS
```

Important residual cycle:

```text
ZERO_COMPOSITE_SURGERY -> PAIR_DIFFERENCE -> ZERO_COMPOSITE_SURGERY
```

This cycle is controlled locally only if the support/span decreases or the pair-difference endpoint case routes to recurrence with smaller measure.  A33, A65--A70 cover much of this but a final global acyclicity statement is still needed.

---

## 5. Equal/signed interval graph

From A20--A27, A36--A55, A62, A66, and A71:

```text
EQUAL_INTERVAL    -> ZERO_COLLAPSE          COLLAPSES
EQUAL_INTERVAL    -> TWO_PIECE_ZERO         DESCENDS
EQUAL_INTERVAL    -> SEPARATED_EQUAL        ROUTES
EQUAL_INTERVAL    -> MIDPOINT               ROUTES
EQUAL_INTERVAL    -> SIGNED_INTERVAL        ROUTES
SIGNED_INTERVAL   -> TRANSPORTED_PREFIX     ROUTES
SIGNED_INTERVAL   -> WEIGHTED_CORE          ROUTES
SIGNED_INTERVAL   -> ZERO_COMPOSITE_SURGERY ROUTES
SIGNED_INTERVAL   -> EQUAL_INTERVAL         DESCENDS
SEPARATED_EQUAL   -> ZERO_COMPOSITE_SURGERY MOD_A34
SEPARATED_EQUAL   -> EQUAL_INTERVAL         DESCENDS
SEPARATED_EQUAL   -> FORBIDDEN_RECURRENCE   MOD_A34
MIDPOINT          -> ZERO_COMPOSITE_SURGERY MOD_A34
MIDPOINT          -> ZERO_COLLAPSE          COLLAPSES
MIDPOINT          -> FORBIDDEN_RECURRENCE   MOD_A34
```

Current status:

```text
separated-equal collision routing is locally closed modulo A34;
midpoint displayed collision routing is locally closed modulo A34;
signed interval can still route into WEIGHTED_CORE.
```

---

## 6. D2 / separated-equal subgraph

D2 is no longer an independent node.  A40/A52/A53 show:

```text
D2 m<k -> DESCENDS
D2 m=k -> ZERO_COMPOSITE_SURGERY MOD_A34
D2 m>k -> ZERO_COMPOSITE_SURGERY MOD_A34
```

In graph form:

```text
SEPARATED_EQUAL -> ZERO_COMPOSITE_SURGERY MOD_A34
SEPARATED_EQUAL -> EQUAL_INTERVAL         DESCENDS
SEPARATED_EQUAL -> ZERO_COLLAPSE          COLLAPSES
```

Thus D2 contributes no new class.

---

## 7. Pair-difference graph

From A33, A65--A70:

```text
PAIR_DIFFERENCE -> EQUAL_INTERVAL         DESCENDS
PAIR_DIFFERENCE -> TWO_PIECE_ZERO         DESCENDS
PAIR_DIFFERENCE -> ZERO_COMPOSITE_SURGERY ROUTES
PAIR_DIFFERENCE -> SINGLETON_RECURRENCE   ROUTES
PAIR_DIFFERENCE -> FORBIDDEN_RECURRENCE   MOD_A34
PAIR_DIFFERENCE -> SUCCESS                DESCENDS
```

Open issue:

```text
PAIR_DIFFERENCE can cycle back into ZERO_COMPOSITE_SURGERY.
```

Expected controlling measure:

```text
span-first measure with pair boundary rank below the source zero-composite rank.
```

This must be part of the final global termination theorem.

---

## 8. Recurrence graph

A64--A71 route named recurrence sources.

```text
FORBIDDEN_RECURRENCE -> ZERO_COMPOSITE_SURGERY MOD_A34
FORBIDDEN_RECURRENCE -> EQUAL_INTERVAL         MOD_A34
FORBIDDEN_RECURRENCE -> SIGNED_INTERVAL        MOD_A34
FORBIDDEN_RECURRENCE -> PAIR_DIFFERENCE        MOD_A34
FORBIDDEN_RECURRENCE -> SINGLETON_RECURRENCE   MOD_A34
FORBIDDEN_RECURRENCE -> CYCLIC_RECURRENCE      MOD_A34
FORBIDDEN_RECURRENCE -> GLOBAL_TERMINATION     OPEN
SINGLETON_RECURRENCE -> PAIR_DIFFERENCE        ROUTES
SINGLETON_RECURRENCE -> ZERO_COMPOSITE_SURGERY ROUTES
SINGLETON_RECURRENCE -> CYCLIC_RECURRENCE      ROUTES
SINGLETON_RECURRENCE -> FORBIDDEN_RECURRENCE   MOD_A34
CYCLIC_RECURRENCE    -> MIDPOINT               ROUTES
CYCLIC_RECURRENCE    -> ZERO_COMPOSITE_SURGERY ROUTES
CYCLIC_RECURRENCE    -> SINGLETON_RECURRENCE   ROUTES
CYCLIC_RECURRENCE    -> FORBIDDEN_RECURRENCE   MOD_A34
```

A64 proved bounded-blocker descent.  A65--A71 show the named recurrence sources introduce no new local species.

Remaining issue:

```text
prove the recurrence graph is acyclic under a single global measure.
```

---

## 9. External collision graph

A62 gives:

```text
EXTERNAL_COLLISION -> ZERO_COMPOSITE_SURGERY ROUTES
EXTERNAL_COLLISION -> EQUAL_INTERVAL         ROUTES
EXTERNAL_COLLISION -> SIGNED_INTERVAL        ROUTES
EXTERNAL_COLLISION -> TRANSPORTED_PREFIX     ROUTES
EXTERNAL_COLLISION -> FORBIDDEN_RECURRENCE   MOD_A34
```

External collisions are not a hard node anymore.  They are a routing layer.

---

## 10. Weighted graph

From A56--A61:

```text
SIGNED_INTERVAL       -> TRANSPORTED_PREFIX     ROUTES
SIGNED_INTERVAL       -> WEIGHTED_CORE          ROUTES
WEIGHTED_CORE         -> TRANSPORTED_PREFIX     DESCENDS if W1 applies
WEIGHTED_CORE         -> ZERO_COLLAPSE          COLLAPSES if W2 applies
WEIGHTED_CORE         -> TWO_PIECE_ZERO         DESCENDS if W3/W4 applies
WEIGHTED_CORE         -> WEIGHTED_CUT_SWAP      OPEN
WEIGHTED_CUT_SWAP     -> ZERO_COMPOSITE_SURGERY ROUTES
WEIGHTED_CUT_SWAP     -> EQUAL_INTERVAL         ROUTES
WEIGHTED_CUT_SWAP     -> SIGNED_INTERVAL        ROUTES
WEIGHTED_CUT_SWAP     -> FORBIDDEN_RECURRENCE   MOD_A34
```

The key open edge is:

```text
WEIGHTED_CORE -> WEIGHTED_CUT_SWAP OPEN
```

This is exactly the weighted core cut-selection theorem.

A60 proves that once a cut is selected, displayed collisions from the cut-swap route locally.  It does not prove a useful cut exists.

---

## 11. Condensed dependency graph

A high-level graph is:

```text
SIGNED_INTERVAL
   -> TRANSPORTED_PREFIX -> ZERO_COMPOSITE_SURGERY
   -> WEIGHTED_CORE --OPEN--> WEIGHTED_CUT_SWAP -> ZERO_COMPOSITE_SURGERY

EQUAL_INTERVAL
   -> SEPARATED_EQUAL -> ZERO_COMPOSITE_SURGERY
   -> MIDPOINT -> ZERO_COMPOSITE_SURGERY

ZERO_COMPOSITE_SURGERY
   -> PAIR_DIFFERENCE
   -> FORBIDDEN_RECURRENCE
   -> SUCCESS / COLLAPSE / smaller zero-composite

PAIR_DIFFERENCE
   -> ZERO_COMPOSITE_SURGERY
   -> SINGLETON_RECURRENCE

SINGLETON_RECURRENCE
   -> PAIR_DIFFERENCE / ZERO_COMPOSITE_SURGERY / CYCLIC_RECURRENCE

CYCLIC_RECURRENCE
   -> MIDPOINT / ZERO_COMPOSITE_SURGERY / SINGLETON_RECURRENCE

FORBIDDEN_RECURRENCE
   -> bounded-blocker descent OR routed class
```

The visible cycles are:

```text
CYCLE 1: ZERO_COMPOSITE_SURGERY <-> PAIR_DIFFERENCE
CYCLE 2: SINGLETON_RECURRENCE -> PAIR_DIFFERENCE -> SINGLETON_RECURRENCE
CYCLE 3: CYCLIC_RECURRENCE -> SINGLETON_RECURRENCE -> CYCLIC_RECURRENCE
CYCLE 4: SIGNED_INTERVAL -> WEIGHTED_CORE -> WEIGHTED_CUT_SWAP -> SIGNED_INTERVAL
CYCLE 5: SEPARATED_EQUAL -> ZERO_COMPOSITE_SURGERY -> FORBIDDEN_RECURRENCE -> SEPARATED_EQUAL
```

A complete proof needs a measure decreasing around each cycle.

---

## 12. Candidate global measure

A64 suggested recurrence measure:

```text
M_rec=(span,pieces,type_rank,boundary_rank,h_excess).
```

For the full graph, a more robust measure may need two layers:

```text
M_global=(
  total_active_span,
  active_support_size,
  recurrence_depth,
  weighted_depth,
  type_rank,
  boundary_rank,
  h_excess
)
```

Definitions:

- `total_active_span`: enclosing interval length of current active obstruction.
- `active_support_size`: number of atoms in the participating pieces.
- `recurrence_depth`: number of consecutive recurrence routings since last strict collision descent.
- `weighted_depth`: 1 for genuine weighted core, 0 otherwise, or a finer cut-depth metric.
- `type_rank`: obstruction class rank.
- `boundary_rank`: endpoint/boundary degeneracy rank.
- `h_excess`: first forbidden index minus global minimal first-hit index.

This is only a candidate.  It must be validated edge-by-edge.

---

## 13. Remaining unproved edges

The graph shows the current real gaps.

### Gap G1: global acyclicity

Need:

```text
Every directed cycle in the routed obstruction graph strictly decreases M_global.
```

This is the final termination theorem.

### Gap G2: weighted cut-selection

Need:

```text
WEIGHTED_CORE -> WEIGHTED_CUT_SWAP
```

with a cut that is useful globally.

### Gap G3: recurrence depth control

Need:

```text
FORBIDDEN_RECURRENCE cannot re-enter itself indefinitely through routed classes.
```

A64 bounded-blocker descent and A65--A71 routing are partial progress.

### Gap G4: finite verification bridge

Need to specify:

```text
small p cases,
characteristic-2 or division-by-2 exceptions,
script certification status.
```

---

## 14. Recommended A73

The next useful note should attack G1 directly.

Suggested title:

```text
Analytic global acyclicity attempt A73
```

Start by proving acyclicity for the subgraph excluding `WEIGHTED_CORE`:

```text
ZERO_COMPOSITE_SURGERY,
PAIR_DIFFERENCE,
SINGLETON_RECURRENCE,
CYCLIC_RECURRENCE,
SEPARATED_EQUAL,
MIDPOINT,
FORBIDDEN_RECURRENCE.
```

If that subgraph can be assigned a strict measure, then the only remaining non-termination risk is the weighted-core cut-selection edge.

---

## Current status

Proved/recorded here:

1. obstruction-class node set;
2. directed dependency graph of routed reductions;
3. visible cycles;
4. candidate global measure;
5. precise remaining gaps.

Not proved here:

1. global acyclicity;
2. weighted cut-selection;
3. final endpoint avoidance theorem.
