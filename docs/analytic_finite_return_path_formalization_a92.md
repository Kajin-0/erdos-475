# Analytic finite return-path formalization A92

This note continues from A91.

A91 hardened the first-changed-endpoint argument, but it remained conditional on two proof-architecture items:

```text
T1. every routed weighted self-return admits a finite return-path model;
T2. an unobstructed first endpoint-pattern change gives progress/success/descent, not invisible self-return.
```

A92 formalizes the finite return-path model as an obstruction state machine.

This note is still not a final proof.  It defines the state machine needed to make A91 fully formal and identifies the remaining verification task: every routing step in A1--A91 must be shown to be one transition or a finite sequence of transitions in this state machine.

---

## 1. Obstruction state

An obstruction state is a tuple

```text
Omega=(R, I, C, E, M, tag)
```

where:

```text
R    = current ordering of the same subset S subset F_p^*;
I    = active interval or active displayed window in R;
C    = obstruction class;
E    = endpoint data attached to I;
M    = measure tuple;
tag  = provenance label describing the local move that produced the state.
```

The obstruction class `C` belongs to the class universe from A72/A78:

```text
ZERO_COLLAPSE,
PREFIX_ZERO,
TWO_PIECE_ZERO,
THREE_PIECE_ZERO,
HIGHER_ZERO_COMPOSITE,
ZERO_COMPOSITE_SURGERY,
EQUAL_INTERVAL,
SIGNED_INTERVAL,
SEPARATED_EQUAL,
MIDPOINT,
PAIR_DIFFERENCE,
TRANSPORTED_PREFIX,
WEIGHTED_CORE,
SINGLETON_RECURRENCE,
CYCLIC_RECURRENCE,
FORBIDDEN_RECURRENCE,
EXTERNAL_COLLISION,
SUCCESS,
CONTRADICTION.
```

The endpoint data `E` contains, as applicable:

```text
basepoint;
left and right boundary endpoints;
internal partial-sum list;
internal endpoint set;
forbidden-hit index;
block decomposition labels;
block sums;
A5 blocker index;
next atom after a forbidden hit.
```

The measure `M` is either the non-weighted measure `M_NW^*` or the weighted measure `(|B|, M_NW^*)` when `C=WEIGHTED_CORE`.

---

## 2. Terminal states

Terminal states are:

```text
SUCCESS,
CONTRADICTION.
```

A state is `SUCCESS` if the current ordering is Graham-valid and avoids the forbidden value `f`.

A state is `CONTRADICTION` if one of the following is forced:

```text
nonempty zero interval;
zero atom;
repeated partial sums in a claimed Graham-valid ordering;
forbidden hit earlier than the globally minimal hit;
violation of subset/distinct-atom assumptions;
invalid endpoint condition f=sigma when f was assumed external.
```

---

## 3. Allowed transition types

Every nonterminal transition must be one of the following.

### T-adjacent-swap

Swap two adjacent atoms or adjacent blocks:

```text
L M -> M L.
```

Endpoint data is updated by replacing the local middle endpoint

```text
u+sum(L)
```

with

```text
u+sum(M).
```

Collision, forbidden-hit, and success outcomes are then tested.

---

### T-block-exchange

Exchange two displayed equal-sum or signed-related blocks, such as:

```text
A G C -> C G A
```

or a gap-after move:

```text
A G C -> A C G.
```

This includes the separated-equal moves from A36--A55 and A75--A77.

---

### T-cut-swap

For weighted cores, choose a proper cut

```text
B=P R
```

and apply

```text
A P R C -> A R P C.
```

This is the A60 fixed cut-swap.

---

### T-cyclic-cut

Rotate an active block or the whole ordering around a cut endpoint:

```text
P R -> R P.
```

Endpoint data is updated by the cyclic partial-sum formula:

```text
S_i-S_c
```

for suffix endpoints and

```text
sigma-S_c+S_i
```

for wrapped endpoints.

---

### T-atom-insertion-normalization

Move an atom into or out of a displayed zero-composite window as in the A28--A34 atom-insertion framework:

```text
X P Q q Y -> X P q Q Y.
```

This transition records H1/H2 recurrence data if the transformed ordering hits `f`.

---

### T-A5-blocker-pullback

At a recurrent forbidden hit, apply the A5 blocker relation

```text
S'_{H-1}+r'_{H+1}=S'_{j'}
```

and pull the relation back to the pre-move ordering.

The output class is one of:

```text
zero-composite;
equal/signed interval;
pair-difference;
singleton recurrence;
cyclic recurrence;
external bridge collision;
weighted core;
collapse.
```

---

### T-external-collision-pullback

If a transformed move collides with an endpoint outside the displayed local window, pull the collision back into one of:

```text
zero-composite;
equal/signed interval;
transported-prefix;
pair-difference;
forbidden recurrence;
bridge/separated-equal branch.
```

This is the state-machine form of A62.

---

### T-normal-form-rewrite

Rewrite a displayed obstruction without changing the ordering, e.g.:

```text
transported-prefix -> zero-composite;
weighted easy reduction -> zero-composite/equal interval;
midpoint relation -> adjacent equal/midpoint branch;
endpoint pair relation -> pair-difference branch.
```

This transition must not increase the active measure.  If it does not strictly decrease the measure, it must move to a lower type-rank class or enter a separately terminating subroutine.

---

## 4. Transition outcome trichotomy

Every move transition has exactly one of the following outcomes:

```text
1. SUCCESS: transformed ordering is Graham-valid and avoids f;
2. COLLISION: transformed ordering is not Graham-valid;
3. RECURRENCE: transformed ordering is Graham-valid but hits f;
4. NORMALIZED: no ordering change, but obstruction class is rewritten;
5. DESCENT: an active measure coordinate strictly decreases;
6. WEIGHTED_RETURN: state returns to WEIGHTED_CORE.
```

The first three are mutually exclusive for genuine ordering-changing moves.

The last three occur inside the routing/normalization layer.

---

## 5. Finite return path

## Definition A92.1: finite return path

A finite return path from obstruction state `Omega_0` to obstruction state `Omega_N` is a finite sequence

```text
Omega_0 -> Omega_1 -> ... -> Omega_N
```

where every arrow is one allowed transition from Section 3.

A weighted self-return is a finite return path with:

```text
Omega_0.C = WEIGHTED_CORE,
Omega_N.C = WEIGHTED_CORE.
```

It is non-descending if the returned weighted middle length is not smaller than the original weighted middle length.

---

## 6. First-change principle

Let a finite return path preserve the same outer blocks and same middle support `B`, but change the internal endpoint pattern of `B`.

Define

```text
s_* = min{s : E_s != E_0}
```

where `E_s` is the internal endpoint set of `B` in state `Omega_s`.

A91 analyzed the transition at `s_*`.

---

## Lemma A92.2: first endpoint-pattern change occurs at one allowed transition

If a finite return path changes the internal endpoint pattern, then the first change occurs during exactly one allowed transition of type:

```text
T-adjacent-swap,
T-block-exchange,
T-cut-swap,
T-cyclic-cut,
T-A5-blocker-pullback,
T-external-collision-pullback,
T-normal-form-rewrite.
```

### Proof

By Definition A92.1, each step of the path is one allowed transition.  Since the path is finite and the endpoint set changes, the least index `s_*` exists.  The transition `Omega_{s_*-1}->Omega_{s_*}` is therefore one allowed transition. ∎

---

## Lemma A92.3: unobstructed first endpoint-pattern change is progress

Suppose the first endpoint-pattern change creates a new internal endpoint value which:

```text
1. does not collide with any current endpoint;
2. does not hit f;
3. does not change the weighted middle length upward;
4. does not create a new weighted core with the same measure.
```

Then the transition is progress: the transformed ordering or transformed obstruction is strictly closer to success or has strictly smaller active measure.

### Proof sketch

If the new endpoint is collision-free and not forbidden, the local move that created it is not blocked at that endpoint.  If no weighted measure is preserved, the active obstruction cannot be the same self-return state.  Therefore the state either advances to a collision-free transformed ordering, exits to a lower obstruction class, or decreases the measure.  In a minimal self-return, such an unobstructed first change cannot be part of an invisible cycle. ∎

### Status

This is the main remaining proof-engineering lemma.  A final proof must define “strictly closer to success” purely in terms of the global measure, not informally.

---

## 7. State-machine version of A91

## Theorem A92.4: first-changed-endpoint theorem in the state machine

Assume a weighted self-return has a finite return path and preserves the same outer blocks and same middle support `B`, but changes the internal endpoint set of `B`.

Then the first endpoint-pattern change produces one of:

```text
1. internal zero collapse;
2. internal equal/separated interval;
3. pair-difference boundary;
4. singleton/prefix recurrence;
5. cyclic recurrence;
6. A56 transported-prefix/easy reduction;
7. smaller weighted middle;
8. progress/descent by Lemma A92.3.
```

### Proof

By Lemma A92.2, the first change occurs at a single allowed transition.  The transition types are exactly those analyzed in A91.  Their outputs are the listed alternatives. ∎

---

## 8. Coverage obligation for A1--A91

A92 does not yet prove that every routing step in the previous notes is covered by the state machine.

The required audit is:

```text
For each A-note routing step, assign one transition type from Section 3.
```

Examples:

```text
A5 adjacent blocker                -> T-adjacent-swap + T-A5-blocker-pullback
A36 direct exchange                -> T-block-exchange
A49 gap-after move                 -> T-block-exchange
A60 weighted cut-swap              -> T-cut-swap
A62 external collision             -> T-external-collision-pullback
A65--A67 atom insertion recurrence -> T-atom-insertion-normalization + T-A5-blocker-pullback
A69 pair-swap recurrence           -> T-adjacent-swap + T-A5-blocker-pullback
A70 singleton recurrence           -> T-A5-blocker-pullback
A71 cyclic recurrence              -> T-cyclic-cut + T-A5-blocker-pullback
A74--A77 bridge/gap routing        -> T-block-exchange + T-external-collision-pullback
A79--A83 weighted routing          -> T-cut-swap + T-normal-form-rewrite
```

---

## 9. Conditional weighted closure from the state machine

## Theorem A92.5: weighted closure under state-machine coverage

Assume:

```text
1. every routed weighted self-return admits a finite return path in the A92 state machine;
2. Lemma A92.3 is hardened into a strict measure descent statement;
3. A78 non-weighted acyclicity holds;
4. A89 eliminates pattern-rigid strong exact self-return.
```

Then weak cut-rigid weighted self-return cannot persist indefinitely.

### Proof

If a weak return is pattern-rigid, A89 eliminates it.  If it is not pattern-rigid, then some part of the endpoint/boundary/label/middle data changes.  By A90 and A92.4, the first change produces a routed non-weighted obstruction, an A56 reduction, smaller weighted middle, collapse, or progress.  These alternatives terminate by A78, weighted induction, contradiction, or success. ∎

---

## 10. Remaining proof-engineering tasks

A92 reduces the remaining weighted formalization to two precise tasks.

### Task S1: State-machine coverage table

Create a table mapping every routing lemma A1--A91 to one or more allowed transition types.

### Task S2: Strict progress lemma

Replace Lemma A92.3's proof sketch with a formal measure statement.

A possible measure extension is:

```text
M_total=(
  weighted_middle_length,
  M_NW^*,
  unresolved_endpoint_changes,
  transition_depth
).
```

A final proof must show unobstructed first endpoint changes strictly decrease this measure or produce success.

---

## 11. Target A93

A93 should be the state-machine coverage table.

Suggested title:

```text
State-machine coverage table A93
```

Minimum deliverables:

```text
1. table from A-note lemmas to transition types;
2. identify any routing step not covered by T1--T8;
3. add missing transition types if needed;
4. identify which steps still rely on informal progress language.
```

---

## Current status after A92

Proved/defined here:

```text
1. obstruction state tuple;
2. allowed transition types;
3. finite return path definition;
4. first endpoint-pattern change occurs at one transition;
5. state-machine version of A91;
6. weighted closure conditional on state-machine coverage and strict progress lemma.
```

Still open:

```text
1. state-machine coverage table for A1--A91;
2. strict progress lemma for unobstructed first endpoint changes;
3. final unconditional weighted closure.
```
