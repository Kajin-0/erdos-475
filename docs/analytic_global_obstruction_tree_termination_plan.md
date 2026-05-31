# Analytic Plan: Global Obstruction-Tree Termination

This note transitions from local template algebra to the global termination problem.

Claim boundary:

```text
This is a proof plan and integration map, not a complete proof of Erdős 475.
The local first-blocker templates are now packaged, but global termination remains the hard open layer.
```

---

## Source local coverage

The local first-blocker system is indexed in:

```text
docs/analytic_local_reduction_coverage_summary.md
```

Packaged local modules include:

```text
T1: right blocker, length >= 2.
T2: left blocker, length >= 2.
T3: right singleton blocker.
T4: left singleton blocker.
GEN-L1 / GEN-R1.
GEN-L>=2 / GEN-R>=2.
DUP-L / DUP-R.
Scalar absorption.
```

The local branches route to:

```text
SUCCESS,
CONTRADICTION / impossible condition,
AFFINE_SINGLETON,
PROPER_SUBINTERVAL,
TEMPLATE_EXTERNAL_CANCELLATION,
BRIDGE_GAP_SMALLER_ENCLOSURE,
BOUNDARY_SENSITIVE_ZERO,
SCALAR_ABSORPTION.
```

---

## Existing global framework to reuse

Existing final-draft files already define a broad obstruction-state and termination framework:

```text
docs/final/F03_obstruction_state_machine.md
docs/final/F08_bridge_gap_descent_theorem.md
docs/final/F09_nonweighted_termination_theorem.md
```

In particular, F03 defines obstruction states of the form:

```text
Omega=(R,I,C,E,M,tag).
```

F03/F09 use the non-weighted measure:

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

This new local-template work should be integrated into that framework rather than replacing it.

---

## Corrected state object for this proof branch

For the template-aware endpoint-avoidance proof, an obstruction-tree node should specialize F03 as follows:

```text
Omega = (R, I, C, E, M, tag)
```

where:

```text
R = fixed original Graham-valid ordering chosen with minimal first forbidden hit;
I = active enclosing interval/window in R;
C = obstruction class;
E = endpoint/block data;
M = active measure tuple, compatible with M_NW^*;
tag = provenance label, e.g. T1-Lz-long, GEN-R1, scalar-S1-A.
```

The endpoint/block data `E` must include template-aware cancellation data:

```text
active block H;
proposed permutation pi(H);
split pi(H)=A,B;
external interval K if present;
cancellation equation:
  K + A = 0
or
  B + K = 0;
for bridge states:
  bridge pieces B_ext,U,E_corr if applicable;
for singleton/affine states:
  affine equation z=T_*;
for boundary states:
  whether the active block begins at index 1 or ends at t.
```

This is stricter than bare `Left(T)` / `Right(T)` notation.

---

## Class mapping from local modules to global classes

The newly packaged local outcomes should map to the F03/F09 class universe as follows.

### SUCCESS

Maps to:

```text
SUCCESS.
```

A local proposed permutation is Graham-valid and avoids the forbidden value.

### CONTRADICTION / impossible condition

Maps to:

```text
CONTRADICTION,
ZERO_COLLAPSE,
PREFIX_ZERO,
```

or direct terminal contradiction:

```text
zero atom,
duplicate atom,
nonempty zero interval,
repeated partial sum,
minimality violation.
```

### AFFINE_SINGLETON

Maps to:

```text
SINGLETON_RECURRENCE
```

or a singleton interval routing state.

Required proof obligation:

```text
Show every affine equation z=T_* produced by the local modules creates a valid singleton routing state with smaller or finite-rank measure, or immediately contradicts distinctness/nonzero assumptions.
```

### PROPER_SUBINTERVAL

Maps to local descent classes:

```text
PREFIX_ZERO,
SIGNED_INTERVAL,
EQUAL_INTERVAL,
TRANSPORTED_PREFIX,
TWO_PIECE_ZERO,
```

or a generic local subinterval class depending on equation form.

Required proof obligation:

```text
Show that proper prefix/suffix/internal subinterval states strictly decrease enclosing_span or support_size relative to the parent active window.
```

### TEMPLATE_EXTERNAL_CANCELLATION

Maps to:

```text
EXTERNAL_COLLISION.
```

But with the corrected template data:

```text
K+A=0
or
B+K=0.
```

Required proof obligation:

```text
Show each packaged template external-cancellation child either:
  1. is one of the already packaged local templates;
  2. routes to bridge/gap with smaller enclosure;
  3. produces a recurrence class controlled by F7/F9;
  4. or strictly decreases M_NW^*.
```

### BRIDGE_GAP_SMALLER_ENCLOSURE

Maps to:

```text
BRIDGE_GAP.
```

The T1 long right-collision branches produced separated zero-bridges:

```text
sum(J_s^+) + sum(K_t^-)=0
```

with support inside:

```text
J_s^+, y, K_t^-.
```

Required proof obligation:

```text
Show these have strictly smaller enclosing_span than the parent template window and satisfy F8/A98 bridge/gap hypotheses.
```

### BOUNDARY_SENSITIVE_ZERO

Maps to:

```text
boundary_rank
```

within `M_NW^*` or a terminal contradiction depending on position.

Required proof obligation:

```text
If relative zero occurs in an interior block, it is terminal contradiction.
If it occurs at global beginning, route to a boundary case with smaller boundary_rank or explicit repair.
```

### SCALAR_ABSORPTION

Maps to local scalar routing plus external-collision outputs.

Required proof obligation:

```text
Show scalar absorption either succeeds/contradicts or produces template-aware external cancellation states whose active support is not larger than the absorbed four-block except through standard external routing.
```

---

## Candidate measure specialization

Use the existing non-weighted measure:

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

For the current template-aware local proof, define:

```text
enclosing_span:
  length of smallest interval in the fixed ordering containing all atoms used by the active obstruction state.

gap_length:
  for separated bridge/cancellation states, number of atoms strictly between the participating pieces;
  otherwise 0.

support_size:
  number of atoms participating in the displayed obstruction equation or local repair.

recurrence_depth:
  consecutive returns to an equal or larger active support without span/support descent.

pair_depth:
  consecutive affine/pair-difference routings.

separated_depth:
  consecutive separated-equal or separated-zero routings without gap descent.

bridge_depth:
  consecutive bridge/gap routings without span/gap/support descent.

type_rank:
  finite rank assigned to local outcome classes.

boundary_rank:
  finite rank assigned to boundary-sensitive zero cases.

h_excess:
  recurrent forbidden-hit index minus the globally minimal first-hit index.
```

Suggested type-rank order, from lower to higher priority:

```text
CONTRADICTION / SUCCESS,
PROPER_SUBINTERVAL,
BRIDGE_GAP,
AFFINE_SINGLETON,
TEMPLATE_EXTERNAL_CANCELLATION,
SCALAR_ABSORPTION,
FIRST_BLOCKER_TEMPLATE.
```

This ranking is provisional and must be audited edge-by-edge.

---

## Required strict-progress checks

The global theorem needs the following checks.

### Check 1: proper subinterval descent

Every proper prefix/suffix/internal subinterval child must satisfy:

```text
enclosing_span(child) < enclosing_span(parent)
```

or at minimum:

```text
support_size(child) < support_size(parent)
```

with no earlier coordinate increasing.

### Check 2: bridge/gap descent

Every separated zero-bridge produced by T1 long right-collision branches must satisfy:

```text
enclosing_span(child) < enclosing_span(parent).
```

This was shown locally for:

```text
T1-Rz-long,
T1-Rza-long.
```

Need to verify the same for any future T2 mirror branches and generic interval branches.

### Check 3: external-cancellation recurrence

A branch of repeated external cancellations must either:

```text
1. move monotonically outward until boundary contradiction/repair;
2. create a smaller bridge/gap state;
3. create a proper subinterval state;
4. create affine singleton/scalar routing with finite rank decrease;
5. enter a recurrence class controlled by existing F7/F9 machinery.
```

This is currently the main global gap.

### Check 4: affine/singleton routing

Every affine singleton equation must route to:

```text
1. duplicate contradiction;
2. nonzero contradiction;
3. GEN-L1 / GEN-R1 if length one and nonduplicate;
4. GEN-L>=2 / GEN-R>=2 if the corresponding interval has length at least two;
5. scalar absorption if it creates b=2a or a=2b.
```

Need to prove this does not increase earlier measure coordinates indefinitely.

### Check 5: boundary-sensitive zero

Interior relative zero:

```text
terminal contradiction.
```

Boundary relative zero:

```text
explicit boundary repair or boundary_rank decrease.
```

Need a small boundary lemma package.

---

## Proposed Global Obstruction-Tree Termination Theorem

### Draft statement

Fix a Graham-valid ordering `R` of `S` whose first forbidden hit `h` is minimal among all Graham-valid orderings hitting `f`.

Construct the obstruction tree using the packaged local modules and template-aware external collision normal form.

Then every branch terminates in one of:

```text
1. SUCCESS: a Graham-valid ordering avoiding f;
2. CONTRADICTION: zero atom, duplicate atom, nonempty zero interval, repeated partial sum, or minimality violation;
3. explicit boundary repair;
4. exit to a strictly smaller obstruction state under M_NW^*.
```

Equivalently, there is no infinite branch because `M_NW^*` decreases lexicographically along every nonterminal route after finite same-rank recurrence depth.

### Current status

This theorem is not yet proved.

The local modules provide the transition classification needed for the proof, but edge-by-edge measure verification remains incomplete.

---

## Immediate next proof target

The highest-value next lemma is:

```text
External-Cancellation Recurrence Lemma.
```

Draft target:

```text
Any chain of template-aware external cancellations generated by the packaged local modules either:
  1. produces a proper subinterval obstruction;
  2. produces a smaller-enclosure bridge/gap state;
  3. produces affine/singleton or scalar routing;
  4. reaches a boundary condition;
  5. or strictly increases recurrence_depth until an existing F7/F9 recurrence-routing lemma applies.
```

This lemma is the main bridge between local coverage and global termination.

---

## Significant status

The project has moved from local algebra discovery to global termination integration.

Completed:

```text
First-blocker local reductions are packaged.
```

Open:

```text
Global well-foundedness of the obstruction tree.
```
