# Analytic global architecture A63

This note consolidates the proof program after A1--A62.

The local obstruction analysis has reached a transition point.  Most local algebraic branches now route into a small set of known classes.  The remaining work is no longer mainly case enumeration; it is global descent.

No complete proof is claimed here.

---

## 1. Main theorem target

The strengthened target remains endpoint avoidance.

For a nonempty subset `A` of `F_p^*` and a forbidden value

```text
f != sigma(A),
```

show that there exists a Graham-valid ordering whose partial sums avoid `f`.

This implies the strong nonzero-sum ordering theorem, and hence Erdős 475 by the reductions established earlier.

---

## 2. Current proof skeleton

The proof program uses contradiction/minimality.

Assume endpoint avoidance fails.  Choose a Graham-valid ordering `R` with first forbidden hit

```text
S_h=f
```

where `h` is minimal among all Graham-valid orderings.

Local moves are then attempted:

```text
adjacent swaps,
cyclic cuts,
block exchanges,
gap moves,
atom insertions,
cut-swaps.
```

Each move has three possible outcomes:

```text
1. success: transformed ordering is Graham-valid and avoids f;
2. collision: transformed ordering is not Graham-valid;
3. recurrence: transformed ordering is Graham-valid but hits f.
```

Collision branches are routed into interval/composite obstruction classes.  Recurrence branches require A34.

---

## 3. Local branches now routed

The following local branches have been routed at the displayed-collision level.

### 3.1 First-hit local blocker

A5 gives the first-hit adjacent-swap obstruction.  This produces bypass zero-sum relations and starts the local obstruction tree.

Status:

```text
proved local obstruction;
feeds zero-composite and interval geometry.
```

### 3.2 Cyclic-cut obstruction package

A7--A12 provide cyclic-cut formulas, cross-collision conditions, and equal-sum trap reductions.

Status:

```text
formulas and reductions proved;
remaining branches routed into later interval/composite machinery.
```

### 3.3 Equal and signed interval geometry

A20--A27 classify interval overlaps, proper-overlap descent, nested two-piece zero relations, signed branches, and symbolic normalization.

Status:

```text
partially normalized;
terminal branches routed into zero-composite, midpoint, weighted, or separated-equal classes.
```

### 3.4 Two-piece zero and atom insertion

A28--A33 develop zero-composite standard forms, zero-block breaking, atom-insertion equations, boundary pair traps, and pair-difference routing.

Status:

```text
local atom-insertion branches controlled except forbidden recurrence;
Q2/Q3 non-descending boundaries routed or eliminated under stated hypotheses.
```

### 3.5 Global recurrence framework

A34 defines active obstruction states and proposes a global measure.  It is not yet proved.

Status:

```text
framework only;
central open theorem.
```

### 3.6 Separated equal intervals

A36--A54 route separated equal-interval surgery.

Direct exchange branches:

```text
D1 -> equal-interval descent / zero collapse;
D2 -> strict descent or zero-composite controlled modulo A34;
D3 -> two-piece zero / zero collapse;
D4 -> two-piece zero / zero collapse;
D5 -> strict-span three-piece zero or endpoint two-piece zero.
```

Gap-after branches:

```text
E1--E5 -> two-piece zero, three-piece zero, equal-interval descent, or zero collapse.
```

Status:

```text
collision side locally routed;
forbidden-hit side depends on A34.
```

### 3.7 Midpoint boundary

A55 routes midpoint displayed collisions:

```text
C_k=0,
a+A_i=0,
C_k=a+A_i,
C_k=2a+Y_m,
A_i=a+Y_m.
```

Status:

```text
displayed collisions route to zero collapse, two-piece zero, three-piece zero;
forbidden hits depend on A34;
external collisions routed by A62.
```

### 3.8 Weighted signed branch

A56--A61 separate transported-prefix artifacts from genuine weighted cores.

A genuine weighted core

```text
A+2B+C=0
```

is equivalent to a nested zero-composite

```text
ABC+B=0.
```

For a cut `B=P R`, the dynamic cut-swap

```text
A P R C -> A R P C
```

has displayed collisions routed to zero-composite classes.

Status:

```text
cut-swap displayed collisions locally routed;
cut-selection theorem open;
forbidden hits depend on A34.
```

### 3.9 External collisions

A62 proves that external collisions pull back to interval/composite geometry.

Status:

```text
routing lemma proved;
not a termination theorem.
```

---

## 4. Remaining proof obligations

After A62, the remaining proof obligations are concentrated into four global statements.

---

# O1. A34 global recurrence theorem

This is the main bottleneck.

## Required statement

Every transformed-order forbidden recurrence either:

```text
1. gives an earlier forbidden hit, contradicting minimality;
2. collapses to a zero-prefix/interior-zero branch;
3. produces a new active obstruction with strictly smaller global measure.
```

The measure must be well-founded and compatible with all routed branches.

A candidate measure has appeared in A34:

```text
M*(O) = (h, span, pieces, type_rank, boundary_rank)
```

or a variant with first-hit index fixed and secondary data ordered lexicographically.

## Required coverage

A34 must cover recurrence branches from:

```text
atom insertion;
pair-difference swaps;
separated equal direct exchange;
gap-after moves;
midpoint exchange;
weighted cut-swap;
external transformed-order landings.
```

---

# O2. Weighted core cut-selection theorem

A60 proves that for a fixed cut `B=P R`, the cut-swap displayed collisions are controlled.

What remains is to prove that a useful cut exists.

## Required statement

For every genuine weighted core

```text
A+2B+C=0
```

there exists a proper cut

```text
B=P R
```

such that the cut-swap

```text
A P R C -> A R P C
```

is either successful, descending, collapsing, or A34-recurrent.

## Present gap

A60 routes failures after a cut is chosen.  It does not prove existence of a globally useful cut.

---

# O3. Final descent/termination theorem for routed collision classes

Many local branches now route to:

```text
two-piece zero,
three-piece zero,
equal interval,
signed interval,
transported-prefix artifact,
midpoint boundary,
weighted cut-swap branch.
```

Each class has local reductions, but the final proof needs one global statement that the routing process terminates.

## Required statement

Starting from any collision obstruction produced by the proof, repeated application of the routing rules either:

```text
1. gives a contradiction to Graham-validity;
2. produces a successful endpoint-avoiding ordering;
3. reaches a forbidden recurrence handled by A34;
4. strictly decreases a well-founded obstruction measure.
```

---

# O4. Finite verification / exceptional cases bridge

The program has finite-verification tooling and logs for small primes and residual local models.  The final proof should specify exactly what is handled analytically and what, if anything, is delegated to finite verification.

At minimum, the final architecture should include:

```text
1. p=2 handling;
2. small p already verified by scripts;
3. assumptions requiring odd characteristic, especially division by 2;
4. validation that all scripted searches are advisory unless explicitly certified.
```

---

## 5. What is not yet proved

The following statements are not yet proved and should not be claimed.

```text
1. Endpoint avoidance theorem.
2. Strong nonzero-sum ordering theorem.
3. Erdős 475.
4. A34 global recurrence theorem.
5. Weighted core cut-selection theorem.
6. Full global termination theorem.
```

---

## 6. What has effectively been achieved

The local case tree has been heavily compressed.

Originally hard-looking branches such as:

```text
separated equal intervals,
D2 balanced/long-prefix branches,
midpoint displayed collisions,
many coefficient-2 branches,
gap-after moves,
external collisions
```

now route into a common framework:

```text
zero-composite surgery,
equal/signed interval geometry,
transported-prefix normalization,
A34 recurrence.
```

This is useful progress because a complete proof no longer appears to require solving dozens of unrelated local problems.  It appears to require solving a small number of global structural problems.

---

## 7. Recommended next step A64

The next note should attack A34 directly.

Suggested A64 title:

```text
Analytic recurrence theorem attempt A64
```

Starting point:

```text
A transformed Graham-valid ordering R' has first forbidden hit h' >= h.
Apply A5 to R'.
Compare the new A5 blocker with the old active obstruction that generated R'.
```

Required output:

```text
1. define the active obstruction measure precisely;
2. prove descent for at least one large family of recurrence branches;
3. isolate exact recurrence ties instead of leaving A34 abstract.
```

---

## Bottom line

After A63, the proof program is no longer primarily local algebra.  It is now a global descent problem.

The next serious proof step is A34/A64: prove that recurrence cannot cycle.
