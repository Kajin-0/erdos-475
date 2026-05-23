# Analytic endpoint-avoidance assembly A84

This note continues from A83.

A78 established the non-weighted obstruction graph is acyclic, conditional on the local routing lemmas A1--A77.  A83 eliminated the final weighted obstruction by reducing weighted cut-selection to internal cyclic rigidity of the middle block `B`, then ruling out that rigidity over an odd prime field.

This note assembles those results into the endpoint-avoidance theorem, explicitly conditional on the previous lemmas.

Important: this is an assembly theorem, not an independent verification of every prior local lemma.  The remaining work after A84 is audit/certification:

```text
1. verify all local lemmas A1--A83 have no hidden assumptions;
2. handle p=2 and small/exceptional cases;
3. connect endpoint avoidance back to the strong nonzero-sum theorem and Erdős 475.
```

---

## 1. Endpoint-avoidance target

Let `p` be an odd prime.  Let

```text
S subset F_p^*
```

be a nonempty subset, and let

```text
sigma=sum(S).
```

Let

```text
f in F_p,
f != sigma.
```

The endpoint-avoidance theorem asserts:

> There exists an ordering of `S` whose partial sums are pairwise distinct and avoid `f`.

Such an ordering will be called `f`-avoiding Graham-valid.

---

## 2. Minimal counterexample setup

Assume endpoint avoidance fails.

Then every Graham-valid ordering of `S` hits `f` at some non-final partial sum.  Choose a Graham-valid ordering

```text
R=(r_1,...,r_t)
```

whose first forbidden hit

```text
S_h=f
```

has minimal possible index `h` among all Graham-valid orderings.

The final endpoint is excluded because

```text
S_t=sigma != f.
```

Therefore

```text
h<t.
```

---

## 3. First local obstruction

Apply the A5 adjacent-swap obstruction at the first forbidden hit `h`.

If the adjacent swap at `h` were Graham-valid and avoided `f`, endpoint avoidance would hold.  Therefore the swap is either blocked by a collision or produces a forbidden recurrence.

A5 gives a local blocker relation of the form

```text
S_{h-1}+r_{h+1}=S_j
```

for some blocker index `j`.

This produces the initial active obstruction state.

---

## 4. Obstruction routing universe

The local analyses A1--A83 route every active obstruction into one of the following classes:

```text
SUCCESS,
CONTRADICTION,
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
EXTERNAL_COLLISION.
```

A72 recorded the dependency graph among these classes.

---

## 5. Non-weighted termination

A78 proved the following conditional theorem.

## Theorem A84.1: non-weighted obstruction paths terminate

Assume the local routing lemmas A1--A77.  In the obstruction dependency graph with `WEIGHTED_CORE` removed, every directed path either:

```text
1. reaches SUCCESS;
2. reaches CONTRADICTION;
3. strictly decreases the non-weighted global measure M_NW^* after finitely many routing steps.
```

Thus there is no infinite non-weighted obstruction path avoiding success and contradiction.

### Input from A78

The measure is

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

This measure is lexicographic over nonnegative integers, hence well-founded.

---

## 6. Weighted termination

The only obstruction class excluded from A78 is the genuine weighted core

```text
A + 2B + C = 0.
```

A56 removed transported-prefix artifacts and easy collapses.  A58 rewrote the genuine weighted core as the nested zero-composite

```text
ABC + B = 0.
```

A79 split the weighted problem into:

```text
W-base: atom-middle weighted core |B|=1;
W-rigid: cut-rigid weighted self-return |B|>=2.
```

A80--A81 eliminated the atom-middle base case modulo the non-weighted acyclic graph A78.

A82 reduced cut-rigid weighted self-return to internal cyclic rigidity of `B`.

A83 proved internal cyclic rigidity is impossible over an odd prime field in a genuine weighted core.

---

## Theorem A84.2: weighted obstruction paths terminate modulo A78

Assume A56--A83.  Every genuine weighted core either:

```text
1. routes by an A56 easy reduction;
2. is atom-middle and routes to A78 by A80--A81;
3. has |B|>=2 and admits a proper cut whose A60 cut-swap succeeds, collapses, enters A78, or returns to a smaller weighted core;
4. terminates by induction on |B|.
```

Therefore no infinite obstruction path can remain inside `WEIGHTED_CORE`.

### Proof

If `|B|=1`, use A80--A81.  If `|B|>=2`, A79 shows that a fixed proper cut is useful unless it returns to a weighted core.  If the returned weighted middle is smaller, induction on `|B|` applies.  If all cuts fail to descend, A82 gives internal cyclic rigidity.  A83 rules this out. ∎

---

## 7. Combined termination theorem

## Theorem A84.3: full obstruction graph terminates modulo local lemma audit

Assume all routing lemmas A1--A83 are valid.  Then every obstruction path generated from the minimal counterexample either:

```text
1. reaches SUCCESS;
2. reaches CONTRADICTION;
3. strictly decreases a well-founded measure after finitely many routing steps.
```

Therefore no infinite obstruction path exists.

### Proof

If the path avoids `WEIGHTED_CORE`, A84.1 applies.  If it enters `WEIGHTED_CORE`, A84.2 either sends it into A78's non-weighted graph, collapses it, succeeds, or returns to a weighted core with smaller middle length.  Since `|B|` is a positive integer, weighted descent terminates.  Once the path leaves the weighted core, A84.1 applies. ∎

---

## 8. Endpoint-avoidance theorem, conditional form

## Theorem A84.4: endpoint avoidance over odd prime fields, conditional on A1--A83

Assume the local routing and termination lemmas A1--A83 are valid.  Let `p` be an odd prime, let `S subset F_p^*` be nonempty, and let

```text
f != sigma(S).
```

Then there exists a Graham-valid ordering of `S` whose partial sums avoid `f`.

### Proof

Assume not.  Choose a minimal first-hit Graham-valid ordering as in Section 2.  A5 produces an initial active obstruction.  By A84.3, the obstruction path cannot continue indefinitely.  It must reach either `SUCCESS` or `CONTRADICTION`.

If it reaches `SUCCESS`, an `f`-avoiding Graham-valid ordering exists, contradicting the assumption that endpoint avoidance fails.

If it reaches `CONTRADICTION`, the assumed minimal counterexample violates Graham-validity, nonzero atom status, or minimality.

Both alternatives contradict the existence of a minimal counterexample.  Therefore endpoint avoidance holds. ∎

---

## 9. Consequence for strong nonzero-sum theorem

Earlier reductions established:

```text
external endpoint avoidance -> strong nonzero-sum theorem.
```

Thus, assuming those reductions and A84.4, the strong nonzero-sum theorem follows for odd prime fields.

The exact connection should be restated and audited in the next note because it is a theorem-level dependency, not merely a local obstruction lemma.

---

## 10. Consequence for Erdős 475

Earlier reductions also established:

```text
strong nonzero-sum theorem -> Erdős 475.
```

Therefore, conditional on:

```text
1. A1--A83 local routing validity;
2. endpoint avoidance -> strong nonzero-sum reduction;
3. strong nonzero-sum -> Erdős 475 reduction;
4. finite/exceptional case bridge;
```

Erdős 475 follows.

This should not yet be advertised as a complete proof until the audit items are completed.

---

## 11. Remaining audit obligations

The proof program is now assembled, but several verification tasks remain.

### Audit O1. Local lemma audit

Check every A-note for:

```text
hidden nonempty assumptions;
endpoint cases accidentally omitted;
orientation/sign errors;
use of odd characteristic or division by 2;
transformed ordering preserving the same subset/multiset;
external collision cases not listed in displayed tables;
claims of support/span descent that may be only heuristic.
```

### Audit O2. Characteristic and small-prime bridge

Explicitly handle:

```text
p=2;
p=3 if any division-by-3 or triple relation appears;
small p verified by scripts;
odd prime assumptions in A55, A56, A81, A83.
```

### Audit O3. Reduction chain audit

Restate and prove cleanly:

```text
endpoint avoidance -> strong nonzero-sum;
strong nonzero-sum -> Erdős 475.
```

### Audit O4. Mechanization/certification

The repository contains scripts and finite checks.  Decide which are:

```text
advisory;
certifying;
needed only for small primes;
not needed in the analytic proof.
```

---

## 12. Recommended A85

A85 should perform the theorem-dependency audit:

```text
Endpoint Avoidance -> Strong Nonzero-Sum -> Erdős 475
```

It should quote the exact statements and prove the implications without relying on local obstruction notation.

A86 should then handle finite/exceptional cases.

A87 should be a proof-audit checklist identifying every lemma that must be hardened before public release.

---

## Current status after A84

Conditional proof architecture:

```text
complete modulo A1--A83 audit.
```

Remaining before claiming a complete proof:

```text
1. theorem-dependency audit;
2. finite/exceptional case handling;
3. local lemma hardening;
4. independent consistency check, ideally with scripts or proof assistant fragments.
```
