# S05. Attack priority matrix

This file ranks the strongest low-compute analytic attack vectors after reading the existing C2, C7, C15, and C18 notes.

The objective is to spend effort where a single analytic insight could bypass large computation and beat brute-force/formal-search approaches.

## Existing-work assessment

### C2 q-through-zero interval

Status:

```text
Strongest near-term brick.
```

Why:

```text
1. It has explicit endpoint formulas.
2. It reduces failed insertion to concrete equations.
3. It does not require the full weighted state machine immediately.
4. It naturally fits the shortest-zero-interval proof strategy.
```

Main formula:

```text
E_k = {T_0,...,T_k} union {q+T_k,...,q+T_m}.
```

This should be promoted into the analytic sprint as the first real lemma.

### C7 / C15 / C18 weighted state-machine path

Status:

```text
Powerful but dangerous.
```

Why:

```text
1. It may already contain most of a proof architecture.
2. But it requires heavy bookkeeping: phase ranks, weighted states, neutral excursions, endpoint/sign tables, finite budgets.
3. This is exactly where a solo researcher can lose weeks without a clean conceptual payoff.
```

Use as backup or inspiration, not as the first manuscript route.

### Endpoint avoidance path

Status:

```text
Defer.
```

Why:

```text
Endpoint avoidance is stronger than needed.
It can be revived after Graham-valid existence is proved.
```

## Highest-leverage attack vectors

## Rank 1: external-overlap replacement lemma

### Target

Prove that the external bridge obstruction cannot persist for all useful insertions.

Setup:

```text
Z = z_1...z_m shortest zero interval,
T_0=0, T_m=0,
T_0,...,T_{m-1} distinct,
q adjacent outside Z.
```

External bridge obstruction for insertion position `k` means:

```text
q + T_b = e
```

for some `b >= k` and external endpoint `e`.

If this happens for every `1 <= k < m`, then many suffix endpoints of `Z` satisfy:

```text
q + T_b in E_ext.
```

Thus:

```text
(q + suffix-prefix-set of Z) intersects E_ext heavily.
```

### Desired lemma

```text
If q + {T_1,...,T_{m-1}} has large ordered overlap with external endpoints,
then either:
  1. there is a shorter zero interval crossing the Z boundary;
  2. a pair-trap/equal-difference relation allows a two-block exchange;
  3. a different outside atom gives a clean insertion;
  4. the collision profile decreases.
```

### Why this is strongest

This could replace much of the C7 weighted-state machinery with one overlap-rigidity argument.

### Risk

```text
High, but high reward.
```

This is the clever route.

## Rank 2: signed-interval elimination

### Target

Handle local cross-side collisions:

```text
T_a = q + T_b,
q = T_a - T_b.
```

This means `q` equals the signed sum of a proper interval inside `Z`.

### Desired lemma

```text
If q equals the signed sum of a proper subinterval of a shortest zero interval Z,
then inserting q at one endpoint of that subinterval creates a smaller repair move,
unless an external bridge occurs.
```

### Why this matters

This is likely easier than external bridge and may isolate the real hard case.

### Risk

```text
Medium.
```

## Rank 3: two-outside-atom argument

### Target

Use both adjacent outside atoms when `Z` has atoms on both sides:

```text
R = X q_L Z q_R Y.
```

If both `q_L` and `q_R` are blocked for all useful insertions, then two translated copies of internal prefix sets overlap with external endpoints:

```text
q_L + T-set,
q_R + T-set.
```

Subtracting gives structure involving:

```text
q_R - q_L.
```

### Desired lemma

```text
If both adjacent atoms are fully blocked, then their difference is represented by many differences of internal/external endpoint pairs, forcing either a pair trap or a clean insertion.
```

### Why this matters

Labs may brute-force local moves.  A two-outside-atom analytic compression is more human/AI-clever.

### Risk

```text
Medium/high.
```

## Rank 4: minimal neutral-excursion lemma

### Target

Harden the C18 red item:

```text
If a self-return path has a change/undo segment preserving all ranked data,
then the segment is removable or exposes a routed obstruction.
```

### Why this matters

This may complete the existing C7/C15 architecture.

### Risk

```text
Medium, but bookkeeping-heavy.
```

This is not the first choice for a solo low-compute sprint, but it is the best fallback if the cleaner external-overlap route stalls.

## Rank 5: finite-state audit tables

### Target

Endpoint/sign tables, bridge budgets, weighted cut-swap budgets, boundary-rank consistency.

### Risk

```text
Low conceptual reward, high time cost.
```

Defer until a compact proof route is identified.

## Recommended next three files

```text
S06_signed_interval_elimination.md
S07_external_overlap_replacement.md
S08_two_adjacent_atoms.md
```

These target the clever route first.

## What to avoid now

```text
1. Do not expand the full state machine unless forced.
2. Do not chase literature constants for days.
3. Do not run large exhaustive searches.
4. Do not formalize Lean until the analytic proof shape stabilizes.
5. Do not strengthen to endpoint avoidance unless it simplifies the proof.
```

## Near-term win condition

The next meaningful analytic milestone is:

```text
All q-through-Z insertion failures reduce to external bridge.
```

That is, prove signed-interval failures are repairable or lead to smaller defects.

Then the whole problem reduces to the single hard obstruction:

```text
persistent external overlap.
```

This is the cleanest possible battlefield.
