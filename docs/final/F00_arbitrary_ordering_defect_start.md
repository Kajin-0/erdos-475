# F00 arbitrary-ordering defect start

This file begins the repair of the starting-ordering gap exposed in F1, F12, and F13.

The current extracted endpoint-avoidance proof assumes:

```text
Input G: at least one Graham-valid ordering of S exists.
```

That is too strong for an unconditional proof of Erdős 475, because Graham-valid existence is essentially the target theorem.

F00 proposes a replacement: start from an arbitrary ordering and minimize a combined defect vector.  If the minimal defect is zero, endpoint avoidance succeeds.  If the defect is nonzero, the first defect should generate an obstruction state in the F3 state machine.

This is a repair draft, not yet a completed proof.

---

## F00.1. Objective

Replace the conditional input

```text
there exists a Graham-valid ordering
```

with a minimization over all orderings of `S`.

The intended theorem is:

```text
For every finite S subset F_p^* and every f != sigma(S),
there exists an ordering whose nonempty partial sums are distinct and avoid f.
```

No Graham-valid starting ordering should be assumed.

---

## F00.2. Ordering defects

Let

```text
R=(r_1,...,r_t)
```

be any ordering of `S`, and define partial sums

```text
S_i=r_1+...+r_i,
0<=i<=t.
```

There are two kinds of defects.

### Collision defect

A collision defect is a pair

```text
0 <= i < j <= t
```

such that

```text
S_i=S_j.
```

Equivalently, the interval

```text
r_{i+1}+...+r_j
```

has sum zero.

For Graham-validity of nonempty partial sums, collisions among

```text
S_1,...,S_t
```

are forbidden.  Collisions involving `S_0=0` are also important because they correspond to nonempty zero-prefix intervals.

### Forbidden endpoint defect

A forbidden endpoint defect is an index

```text
1 <= h <= t
```

such that

```text
S_h=f.
```

Since `f != sigma(S)`, the final endpoint is not forbidden:

```text
S_t=sigma(S) != f.
```

Thus any forbidden endpoint has

```text
h<t.
```

---

## F00.3. Defect vector

Define a defect vector for an ordering `R`:

```text
D(R)=(
  collision_count,
  first_collision_span,
  first_forbidden_index,
  active_defect_span,
  active_defect_type_rank,
  boundary_rank
).
```

The order is lexicographic.

Definitions:

```text
collision_count       = number of repeated endpoint pairs among S_0,...,S_t;
first_collision_span  = minimum j-i over collision pairs S_i=S_j;
first_forbidden_index = minimum h with S_h=f, or infinity if none;
active_defect_span    = span of the selected first active defect;
active_defect_type_rank = rank of selected defect type;
boundary_rank         = endpoint degeneracy rank.
```

Use finite replacements for infinity:

```text
first_forbidden_index = t+1 if no forbidden endpoint exists;
first_collision_span  = t+1 if no collision exists.
```

Thus `D(R)` is a tuple of nonnegative integers bounded by functions of `t`, so a minimizer exists.

---

## Lemma F00.1: defect minimizer exists

Among all orderings of finite `S`, there exists an ordering minimizing `D(R)` lexicographically.

### Proof

There are finitely many orderings of `S`.  The defect vector takes values in a finite set of integer tuples.  Therefore a lexicographic minimizer exists. ∎

---

## F00.4. Zero-defect implication

If

```text
collision_count=0
```

and

```text
first_forbidden_index=t+1,
```

then:

```text
1. all partial sums S_0,...,S_t are pairwise distinct;
2. no nonempty partial sum equals f.
```

This is stronger than endpoint avoidance.

## Lemma F00.2: zero defect gives endpoint avoidance

If an ordering has no endpoint collision among `S_0,...,S_t` and no forbidden endpoint, then it is Graham-valid and avoids `f`.

### Proof

No endpoint collision among `S_0,...,S_t` implies in particular that the nonempty partial sums `S_1,...,S_t` are pairwise distinct.  No forbidden endpoint means none of them equals `f`. ∎

---

## F00.5. First active defect

Let `R` be a defect-minimal ordering.  If `R` is not endpoint-avoiding, then at least one defect exists.

Choose the active defect by priority:

```text
1. shortest collision interval S_i=S_j;
2. if no collision exists, first forbidden endpoint S_h=f.
```

This priority is designed so that Graham-validity defects are repaired before forbidden-endpoint defects.

There are two cases.

---

# 6. Case C: first active defect is a collision

Suppose the active defect is a shortest collision

```text
S_i=S_j,
0<=i<j<=t.
```

Then the interval

```text
Z=r_{i+1}...r_j
```

has sum zero:

```text
sum(Z)=0.
```

If `Z` is nonempty, this is a zero interval.

In the current F3 state machine, zero intervals are terminal contradictions only when the ordering is already claimed Graham-valid.  Here the ordering is arbitrary, so a zero interval is not contradiction.  It is a defect to be repaired.

Thus the arbitrary-ordering start requires a new local repair theorem:

```text
zero-interval defect repair.
```

---

## Lemma F00.3: shortest collision has no internal collision

Let `S_i=S_j` be a collision pair with minimal span `j-i`.  Then the interval `Z=r_{i+1}...r_j` has no proper nonempty zero subinterval.

### Proof

If a proper subinterval of `Z` had sum zero, then there would be a collision pair with smaller endpoint distance than `j-i`, contradicting minimality of the collision span. ∎

---

## F00.6. Collision repair target

For a shortest zero interval

```text
Z=z_1...z_m,
sum(Z)=0,
```

with no internal zero subinterval, the repair goal is to perform a local rearrangement of `Z` or move an adjacent atom across the boundary so that:

```text
1. collision_count decreases; or
2. first_collision_span increases while collision_count is unchanged; or
3. the branch enters the F3 obstruction state machine with smaller measure; or
4. endpoint avoidance succeeds.
```

This is not yet proved in the existing F1--F13 extraction.

---

## Repair theorem needed: zero-interval defect repair

## Needed Lemma F00.C1

Let `R` be a defect-minimal ordering and let `Z` be a shortest zero interval.  Then there exists a local move involving `Z` and at least one adjacent atom, unless `Z` is the whole ordering, such that the move either:

```text
1. decreases D(R);
2. creates an F3 obstruction state already handled by F4--F11;
3. reaches endpoint avoidance;
4. or forces a structural contradiction.
```

### Status

Open.  This is the main new obligation introduced by removing Input G.

---

# 7. Case F: first active defect is forbidden endpoint only

Suppose the defect-minimal ordering has no endpoint collisions but has a forbidden endpoint:

```text
S_h=f.
```

Then the ordering is already Graham-valid, and this is exactly the F1/F2 setup.

Since

```text
f != sigma(S),
```

we have

```text
h<t.
```

The adjacent swap at the first forbidden hit gives the F2 trichotomy:

```text
success;
collision blocker;
recurrence.
```

In this case, the previous endpoint-avoidance proof applies directly.

## Lemma F00.4: no-collision forbidden defect reduces to F1/F2

If a defect-minimal ordering has no endpoint collisions but has a forbidden endpoint, then the F1/F2 adjacent-blocker setup applies without Input G.

### Proof

No endpoint collisions imply the ordering is Graham-valid.  The first forbidden endpoint exists and is nonfinal because `f != sigma(S)`.  Thus F1/F2 applies. ∎

---

# 8. Revised endpoint-avoidance start

Combining the cases:

```text
D(R)=0                      -> endpoint avoidance succeeds;
collision defect exists      -> needs zero-interval repair F00.C1;
no collision, forbidden hit  -> F1/F2 applies.
```

Thus the starting-ordering gap is reduced to one precise missing theorem:

```text
F00.C1 shortest zero-interval defect repair.
```

---

## F00.7. Why this is nontrivial

A zero interval in an arbitrary ordering is not a contradiction.  It is exactly what Graham-validity must eliminate.

The existing obstruction engine treats zero intervals as contradictions only after assuming the current ordering is Graham-valid.  Therefore the proof engine must be extended at the start to show that shortest zero intervals can be repaired or converted into handled obstruction states.

This is the correct place where the original Erdős 475 difficulty reappears.

---

## F00.8. Potential attack on F00.C1

Possible route:

1. Let `Z` be a shortest zero interval, so `Z` has no internal zero subinterval.
2. If `Z` is not the full ordering, choose an adjacent atom `q` immediately outside `Z`.
3. Try moving `q` through `Z` by adjacent swaps.
4. If every adjacent swap preserves or worsens the collision defect, collect the blocker equations.
5. These blocker equations should form the same obstruction species as F4--F11:

```text
pair-difference,
separated-equal,
zero-composite,
weighted core,
cyclic recurrence.
```

6. If `Z` is the full ordering, then `sigma(S)=0`.  For Erdős 475, this case may be handled by the append-one-atom reduction from strong nonzero-sum, but for endpoint avoidance it still needs direct treatment.

---

## F00.9. Alternative: prove strong nonzero-sum first

Instead of proving full endpoint avoidance from arbitrary orderings, one may aim to prove strong nonzero-sum directly:

```text
sigma(S) != 0 -> ordering with S_0,S_1,...,S_t distinct.
```

This naturally starts from arbitrary ordering and minimizes zero-collision defects only, avoiding the additional forbidden endpoint `f` until after Graham-validity is established.

Then F12 can be used as a strengthening theorem.

This may be cleaner:

```text
arbitrary ordering defect minimization -> strong nonzero-sum -> Erdős 475;
then conditional F12 strengthens Graham-valid orderings to endpoint avoidance.
```

However, this changes the proof architecture and must be planned separately.

---

## F00.10. Current repair status

F00 partially resolves the Input G issue by replacing it with a sharper missing lemma.

Current status:

```text
Input G is not resolved.
It is reduced to F00.C1: shortest zero-interval defect repair.
```

The proof is not yet unconditional.

---

## F00.11. Next recommended file

The next file should attack F00.C1 directly:

```text
docs/final/F00_C1_shortest_zero_interval_repair.md
```

Minimum contents:

```text
1. shortest zero interval setup;
2. adjacent outside atom q;
3. q-through-Z swap sequence;
4. blocker equations if swaps fail;
5. classification into F3 obstruction states;
6. special full-ordering zero-total case.
```

---

## F00.12. Extraction status

```text
Status: repair draft.
Risk: RED.
Main result: Input G reduced to shortest zero-interval repair, not eliminated.
```
