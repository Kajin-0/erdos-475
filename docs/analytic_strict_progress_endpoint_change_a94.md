# Analytic strict progress lemma for unobstructed endpoint changes A94

This note continues from A93.

A91 introduced the first-changed-endpoint argument.  A92 formalized obstruction states and finite return paths.  A93 showed that the local moves used in A1--A92 fit the A92 state machine.

The remaining state-machine bottleneck is:

```text
U1. Strict progress lemma.
```

A94 formulates this lemma precisely.

The key idea is simple:

```text
If a first internal endpoint-pattern change creates no collision, no forbidden hit, no weighted self-return of equal measure, and no larger active obstruction, then it cannot be part of an invisible self-return.  It is progress.
```

The hard part is defining progress in a well-founded way.

---

## 1. State-machine setup

Use the A92 obstruction state:

```text
Omega=(R,I,C,E,M,tag).
```

Here:

```text
R = current ordering;
I = active interval/window;
C = obstruction class;
E = endpoint data;
M = active measure;
tag = provenance label.
```

A finite obstruction path is:

```text
Omega_0 -> Omega_1 -> ... -> Omega_N.
```

Each transition is one of the A92 transition types:

```text
TAS, TBX, TCS, TCC, TAIN, TA5, TEX, TNF.
```

---

## 2. Endpoint-pattern data

For an active middle block or active internal block `B`, define:

```text
E_B(Omega)=internal endpoint set of B in state Omega.
```

If the active object is not a weighted middle block, use the analogous active endpoint set:

```text
E_I(Omega)=endpoint set of the active interval/window I.
```

For weighted self-return analysis, `E_B` is the important one.

---

## 3. First endpoint-pattern change

Suppose a finite return path has:

```text
same outer blocks A,C;
same middle support B;
E_B(Omega_0) != E_B(Omega_N).
```

Define the first changed endpoint-pattern index:

```text
s_* = min{s : E_B(Omega_s) != E_B(Omega_0)}.
```

Then:

```text
E_B(Omega_{s_*-1}) = E_B(Omega_0),
E_B(Omega_{s_*}) != E_B(Omega_0).
```

A91 classified the transition at `s_*`.

---

## 4. Obstructed versus unobstructed first change

## Definition A94.1: obstructed first endpoint change

The first endpoint-pattern change is obstructed if the transition at `s_*` produces at least one of:

```text
1. a Graham collision;
2. a forbidden hit f;
3. an internal zero interval;
4. an internal equal/separated interval;
5. a pair-difference boundary;
6. a singleton/prefix recurrence;
7. a cyclic recurrence;
8. an A56 transported-prefix/easy reduction;
9. a smaller weighted middle;
10. an external collision;
11. a weighted return with strictly smaller leading weighted measure.
```

These are all already routed by A78, A56, A89, or weighted induction.

---

## Definition A94.2: unobstructed first endpoint change

The first endpoint-pattern change is unobstructed if none of the conditions in Definition A94.1 occur.

Equivalently, the changed endpoint:

```text
does not collide;
does not hit f;
does not create a routed internal relation;
does not change the weighted middle to a smaller core;
does not enter any named obstruction class.
```

---

# 5. Progress measure

The usual obstruction measure tracks active obstruction complexity.  For first-change arguments, add a local progress coordinate.

Define:

```text
M_prog(Omega)=(
  wlen,
  M_NW^*,
  unresolved_change_count,
  return_depth,
  transition_rank
).
```

where:

```text
wlen = |B| if C=WEIGHTED_CORE, otherwise 0;
M_NW^* = non-weighted global measure from A78;
unresolved_change_count = number of endpoint-pattern changes not yet routed to an obstruction;
return_depth = number of transitions since the current return path began;
transition_rank = rank of the transition type.
```

Lexicographic order is used.

For a minimal self-return path, choose one with minimal:

```text
(length of return path, number of endpoint-pattern changes, active measure).
```

This minimality is the formal substitute for the informal phrase “invisible self-return.”

---

## Lemma A94.3: a minimal self-return has no removable unobstructed first change

Let

```text
Omega_0 -> ... -> Omega_N
```

be a minimal non-descending weighted self-return path among all such paths with the same initial weighted core.

If the first endpoint-pattern change at `s_*` is unobstructed, then the prefix ending at `Omega_{s_*}` can be accepted as progress and cannot be required to reconstruct `Omega_0` invisibly.

### Proof

Because the change is unobstructed:

```text
1. the transformed ordering remains Graham-valid at the changed endpoint;
2. the changed endpoint does not hit f;
3. no new named obstruction is created;
4. no smaller weighted core or routed branch is created.
```

Thus the transition is locally admissible.  If the path later returns to the original weighted obstruction, then the endpoint-pattern change must later be undone.  The undoing transition is a second endpoint-pattern change.  Since the first change was unobstructed, deleting the change/undo pair gives a shorter self-return path with the same endpoints and no worse active measure, contradicting minimality of the chosen self-return path.

If the change is not undone, then the final state cannot be the same self-return state.  It either has different pattern data, which is non-pattern and handled by A91/A92, or it is progress away from the original obstruction.

Therefore a minimal non-descending self-return cannot contain an unobstructed first endpoint-pattern change. ∎

---

## 6. Strict progress statement

## Proposition A94.4: unobstructed first endpoint change gives strict progress or contradicts minimal self-return

In the A92 state machine, let a finite weighted return path be chosen minimal among non-descending self-returns.  If the first internal endpoint-pattern change is unobstructed, then the path cannot be a valid non-descending self-return.

Equivalently, every valid minimal non-descending self-return must have its first endpoint-pattern change obstructed.

### Proof

This is Lemma A94.3 restated in state-machine language. ∎

---

## 7. Consequence for A91

A91 gave the alternatives:

```text
internal zero collapse;
internal equal/separated interval;
pair-difference boundary;
singleton/prefix recurrence;
cyclic recurrence;
A56 transported-prefix/easy reduction;
smaller weighted middle;
unobstructed progress.
```

A94 eliminates the last alternative for minimal non-descending self-return paths.

---

## Corollary A94.5: first endpoint-pattern change is always routed in a minimal self-return

For a minimal non-descending weighted self-return path, the first endpoint-pattern change produces one of:

```text
1. collapse;
2. non-weighted obstruction handled by A78;
3. A56 easy reduction;
4. smaller weighted middle;
5. recurrence already routed by A64--A71;
6. external collision handled by A62;
7. contradiction to minimal self-return.
```

Thus changed endpoint pattern cannot persist in a minimal weighted self-return.

### Proof

Combine A91.6 with Proposition A94.4. ∎

---

# 8. Weak cut-rigidity now implies pattern-rigidity modulo routed exits

## Theorem A94.6: weak cut-rigid self-return reduces to pattern-rigid self-return or routed descent

Assume:

```text
1. the A92 finite return-path model;
2. the minimal self-return choice above;
3. A78 non-weighted termination;
4. A89 strong exact self-return impossibility.
```

Then every weak cut-rigid weighted self-return either:

```text
1. is pattern-rigid;
2. produces a routed non-weighted obstruction;
3. produces an A56 reduction;
4. returns to a smaller weighted middle;
5. collapses;
6. contradicts minimal self-return.
```

### Proof

If the return is pattern-rigid, done.  If not, some component of the pattern changes: middle support, outer blocks, endpoint set, boundary endpoints, or endpoint labels.  A90 handles support, outer-block, boundary, and label changes.  A91 handles endpoint-set changes.  A94 removes the unobstructed-progress escape case from A91 for minimal self-returns.  Therefore every non-pattern return is routed or descending. ∎

---

# 9. Weighted closure after A94

## Theorem A94.7: weighted core is controlled modulo A60/A62/A64/A74 hardening

Assume the following hardened inputs:

```text
H1. A60 fixed cut-swap table is exhaustive;
H2. A62 external collision theorem is exhaustive;
H3. A64 recurrence bounded-blocker measure is valid;
H4. A74--A77 bridge/gap measure inequalities are valid;
H5. A78 non-weighted acyclicity is valid;
H6. A89 strong exact self-return impossibility is valid.
```

Then no genuine weighted core can produce an infinite non-descending obstruction path.

### Proof

Atom-middle cores are handled by A80--A81.  Proper-middle cores use A79.  If a proper cut returns a smaller weighted middle, induction on `|B|` applies.  If every cut is weakly cut-rigid, Theorem A94.6 reduces it to pattern-rigid self-return or routed descent.  Pattern-rigid self-return is impossible by A89.  Routed descent terminates by A78, A56, or weighted induction. ∎

---

# 10. Remaining bottlenecks after A94

A94 closes the specific strict-progress gap U1, subject to the minimal self-return model.

The remaining bottlenecks are now the four hardening items from A93:

```text
U2. Universal external-collision classification A62.
U3. Recurrence bounded-blocker measure A64.
U4. Cut-swap displayed collision table A60.
U5. Bridge/gap measure inequalities A74--A77.
```

The weighted proof no longer has a separate endpoint-pattern invisibility gap, provided the minimal self-return model is accepted.

---

## 11. Target A95

A95 should harden A62:

```text
Universal external-collision classification.
```

Required output:

```text
1. define external collision formally;
2. classify before-left, after-right, and cyclic/wrapped collisions;
3. show each pullback is zero-composite, equal/signed interval, transported-prefix, pair-difference, recurrence, or bridge branch;
4. prove measure nonincrease or route to A74--A77 bridge/gap chain.
```

---

## Current status after A94

Proved/recorded here:

```text
1. obstructed vs unobstructed first endpoint change;
2. minimal self-return progress principle;
3. unobstructed first endpoint changes cannot occur in minimal non-descending self-returns;
4. weak cut-rigidity reduces to pattern-rigidity or routed descent;
5. weighted closure now depends on the remaining hardening items U2--U5.
```

Still open:

```text
1. A62 exhaustive external-collision theorem;
2. A64 recurrence bounded-blocker measure;
3. A60 cut-swap displayed collision table;
4. A74--A77 bridge/gap inequality hardening;
5. final extraction.
```
