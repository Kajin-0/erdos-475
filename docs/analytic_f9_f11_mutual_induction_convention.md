# Analytic Convention: Non-Circular F9/F11 Mutual Induction

This note addresses the circularity risk identified in:

```text
docs/analytic_f10_f11_weighted_core_closure_checkpoint.md
```

Claim boundary:

```text
This is a proof-interface convention note.
It is not a proof of Erdős 475.
It specifies the induction order needed to make the F9/F11 interface non-circular.
```

---

## Problem

The extracted final drafts currently have the following interface:

```text
F9 non-weighted termination:
  non-weighted paths terminate if weighted exits terminate by F11.

F11 weighted termination:
  weighted paths terminate if routed non-weighted exits terminate by F9.
```

This is potentially circular unless the final proof uses a well-founded mutual induction.

The purpose of this note is to state the admissible induction structure.

---

## State classes

Use two top-level phases:

```text
NW = non-weighted obstruction state;
W(m) = genuine weighted-core state with middle length m=|B|.
```

A non-weighted state uses:

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

A weighted state uses:

```text
M_W = (m, M_NW^*, w_subrank).
```

where:

```text
m = |B|,
w_subrank = finite weighted local subrank.
```

The exact `w_subrank` may include:

```text
atom_middle_rank,
cut_rigidity_rank,
signed_boundary_rank,
return_path_depth,
transported_prefix_rank,
endpoint_pattern_rank.
```

---

## Recommended combined measure

Define the global measure:

```text
M_total = (
  phase_weight,
  weighted_middle_length,
  M_NW^*,
  weighted_subrank,
  transition_depth
).
```

with:

```text
phase_weight = 0 for NW states,
phase_weight = 1 for W states.
```

This ordering alone is not enough, because an NW state may enter W. Therefore the proof should be written as nested induction, not as a naive lexicographic descent on `phase_weight`.

---

## Safer formulation: induction on weighted middle length

For each integer `m >= 1`, define the proposition:

```text
P(m):
  All obstruction paths starting from either
    (i) a non-weighted state whose future weighted exits have middle length <= m,
    or
    (ii) a weighted state W(k) with k <= m,
  terminate, provided every weighted return from W(k) has middle length < k
  or exits to a non-weighted state that cannot re-enter W(j) with j >= k at the same or larger M_NW^*.
```

This is too verbose for the final manuscript, but it captures the dependency.

A cleaner final proof can use the following admissible edge rules.

---

## Admissible edge rules

### Rule I: NW-to-NW edge

A non-weighted transition:

```text
NW -> NW
```

is admissible only if:

```text
M_NW^*(child) < M_NW^*(parent),
```

or if it is part of a finite routing chain whose final non-weighted output strictly decreases `M_NW^*`.

### Rule II: W-to-W edge

A weighted transition:

```text
W(m) -> W(m')
```

is admissible only if:

```text
m' < m,
```

or, for intermediate same-`m` local routing states, if `w_subrank` strictly decreases and the chain cannot persist indefinitely.

Final weighted self-return at the same middle length is forbidden unless it is pattern-rigid, and pattern-rigid returns are impossible by A89.

### Rule III: W-to-NW edge

A weighted transition:

```text
W(m) -> NW
```

is admissible if the resulting non-weighted state is handled by F9 under the restriction:

```text
Any later NW -> W transition must enter W(m') with m' < m,
```

or the non-weighted state has strictly smaller `M_NW^*` than the entry state that led to `W(m)`.

This is the key anti-circularity condition.

### Rule IV: NW-to-W edge

A non-weighted transition:

```text
NW -> W(m)
```

is admissible if the weighted theorem applied to `W(m)` proves one of:

```text
1. success;
2. contradiction/collapse;
3. W(m') with m' < m;
4. NW' with M_NW^*(NW') < M_NW^*(NW);
5. NW' with a no-reentry certificate forbidding later W(j) with j >= m at equal or larger M_NW^*.
```

The weakest acceptable form is item 4.

Item 5 is possible but requires a formal no-reentry certificate and should be avoided if possible.

---

## Preferred theorem pair

The final proof should replace independent F9/F11 statements with a coupled pair.

### Theorem F9'

For non-weighted states:

```text
Every non-weighted obstruction path terminates or strictly decreases M_NW^*,
except that it may enter a weighted core W(m).
```

If it enters `W(m)`, invoke F11' with entry measure recorded.

### Theorem F11'

For weighted states:

```text
Starting from W(m) entered from a non-weighted parent NW_0,
every weighted path either:
  1. succeeds;
  2. collapses;
  3. returns to W(m') with m'<m;
  4. exits to NW_1 with M_NW^*(NW_1) < M_NW^*(NW_0);
  5. or exits to a non-weighted terminal contradiction/success branch.
```

Then F9' and F11' compose without circularity.

---

## Stronger single-measure alternative

A single-measure proof may define:

```text
M_joint = (
  active_weighted_middle_bound,
  M_NW^*,
  phase_rank,
  weighted_subrank,
  bridge_subrank,
  return_path_depth
).
```

where:

```text
active_weighted_middle_bound = m when inside a weighted branch entered from W(m),
active_weighted_middle_bound = p for pure non-weighted states with no active weighted branch.
```

But this is harder to state cleanly because pure non-weighted states do not naturally carry a weighted middle length.

Recommendation:

```text
Use mutual induction, not a single global measure, in the final manuscript.
```

---

## Current F11 gap relative to this convention

Current F11 says weighted exits to non-weighted machinery are handled by F9.

That is insufficient unless F11 proves the stronger W-to-NW condition:

```text
W(m) -> NW_1
```

must satisfy one of:

```text
M_NW^*(NW_1) < M_NW^*(NW_entry),
```

or:

```text
NW_1 cannot re-enter W(j) with j >= m at equal-or-larger M_NW^*.
```

Current status:

```text
Not fully audited.
```

This is the main structural theorem blocker.

---

## Where existing notes help

### A89

Eliminates pattern-rigid same-middle self-return.

### A90--A94

Show weak cut-rigid same-middle return becomes pattern-rigid or produces routed descent, assuming the finite return-path/minimal self-return model.

### A97

Shows fixed cut-swap displayed collisions produce weighted return only through signed boundary relations.

### A98/F8

Controls bridge/gap exits, except irreducible signed weighted exits.

Together these suggest that F11' may be provable, but the current drafts do not yet state it in the anti-circular form.

---

## Required audit edges

To make F11' true, audit the following edge types.

### E1. Easy reductions

```text
W(m) -> NW_1
```

via:

```text
B=0,
A+B=0,
B+C=0,
A=C,
transported-prefix/tail rewrite.
```

Need to label the exact `M_NW^*` coordinate that decreases or prove no-reentry to same/larger `m`.

### E2. Atom-middle exits

```text
W(1) -> NW_1.
```

Since there is no smaller positive weighted middle length, every atom-middle weighted core must exit terminally or to non-weighted state that cannot re-enter `W(1)` at equal/larger measure.

This requires the A81 sign-pattern audit.

### E3. Cut-swap displayed zero-composite exits

```text
W(m) -> NW_1
```

via A97 zero-composite/equal/signed branches.

Need to show `NW_1` has active support strictly inside the original weighted window or otherwise decreases `M_NW^*`.

### E4. Cut-swap recurrence exits

```text
W(m) -> recurrence NW_1.
```

Need to show F7's bounded-blocker/long-blocker routing either decreases `M_NW^*` relative to the weighted entry or returns to weighted with smaller `m`.

### E5. Cut-swap external collision exits

```text
W(m) -> external NW_1.
```

Need F6/F8 to show span/gap/support decrease relative to weighted entry or smaller weighted return.

### E6. Signed boundary weighted return

```text
W(m) -> W(m').
```

Need to prove:

```text
m'<m
```

unless the branch is weak cut-rigid, in which case A90--A94 reduce it to pattern-rigid contradiction or routed descent.

---

## Mutual Induction Interface Lemma

### Statement

The F9/F11 interface is non-circular if every weighted-core invocation from a non-weighted parent state `NW_0` satisfies the following:

For weighted entry `W(m)`, F11 returns only:

```text
1. SUCCESS;
2. CONTRADICTION/COLLAPSE;
3. W(m') with m'<m;
4. NW_1 with M_NW^*(NW_1)<M_NW^*(NW_0);
5. NW_1 with a formal no-reentry certificate excluding W(j), j>=m, at equal-or-larger M_NW^*.
```

Then non-weighted F9 termination and weighted F11 termination may be proved by mutual induction on:

```text
(m, M_NW^*)
```

where weighted calls decrease `m` or return to strictly smaller non-weighted measure, and non-weighted calls decrease `M_NW^*` except when entering such a controlled weighted invocation.

### Proof sketch

Assume a minimal infinite obstruction path under lexicographic order on `(m, M_NW^*)`. If it stays non-weighted, F9 gives a strict `M_NW^*` decrease or terminal state. If it enters `W(m)`, the controlled F11 output is terminal, `W(m')` with `m'<m`, or `NW_1` with smaller `M_NW^*`. Each contradicts minimality. The no-reentry certificate option prevents hidden same-measure cycles through `NW -> W -> NW`. ∎

---

## Consequence for final extraction

Patch F9 and F11 to avoid phrases like:

```text
handled by F9
handled by F11
```

unless accompanied by the decrease condition.

Recommended replacement:

```text
handled by the mutual induction interface of docs/analytic_f9_f11_mutual_induction_convention.md.
```

---

## Status

This note resolves the wording-level circularity by specifying the necessary induction interface.

It does not prove that all F10/F11 exits satisfy the interface.

Remaining concrete audits:

```text
1. A81 atom-middle sign-pattern audit.
2. A56 transported-prefix/tail exhaustiveness audit.
3. A97 signed boundary weighted-return audit.
4. W-to-NW exit decrease table relative to the weighted entry state.
```
