# Analytic Theorem Note: Singleton Routing for Endpoint Branches

This note addresses the main remaining local-to-global gap identified in:

```text
docs/analytic_endpoint_branch_f9_edge_audit.md
```

Claim boundary:

```text
This is an integration theorem note for affine/singleton outputs.
It is not a complete proof of Erdős 475.
It depends on the existing F7 recurrence-routing theorem, which still has ORANGE audit status.
```

---

## Purpose

The packaged local modules produce many affine/singleton equations of the form:

```text
z = T_*,
y = T_*,
T = T_*,
linear scalar relation involving one active atom.
```

These equations must not remain as orphan obstruction classes.

This note packages their routing into the existing local modules and the F7 recurrence framework.

---

## Inputs

Relevant local modules:

```text
docs/analytic_template_t1_external_cancellation_theorem.md
docs/analytic_template_t2_mirror_theorem.md
docs/analytic_template_t3_right_singleton_blocker.md
docs/analytic_template_t3_external_routing.md
docs/analytic_template_t4_mirror_singleton_blocker.md
docs/analytic_generic_interval_length_one_theorem.md
docs/analytic_generic_interval_splitting_theorem.md
docs/analytic_duplicate_interval_target_theorem.md
docs/analytic_scalar_absorption_theorem.md
```

Relevant global recurrence theorem:

```text
docs/final/F07_recurrence_routing_theorem.md
```

F7 routes singleton-prefix recurrence to:

```text
suffix-zero descent,
pair-difference prefix descent,
zero-composite branch,
external bridge branch,
cyclic recurrence,
collapse.
```

---

## Singleton equation types

The local modules produce four useful singleton forms.

### Type S0: impossible singleton

Equation forces:

```text
z=0,
y=0,
T=0,
```

or duplicates an already-present atom in the same set `S`.

Route:

```text
CONTRADICTION.
```

Reason:

```text
S subset F_p^*, and S is a set.
```

---

### Type S1: duplicate-target interval

Equation forces an interval target equal to an atom already in the adjacent active block.

Example:

```text
Left(a),
Right(-a),
Left(-b),
Right(b).
```

Route:

```text
docs/analytic_duplicate_interval_target_theorem.md
```

The duplicate-target theorem says:

```text
1. length-one duplicate interval is impossible by distinctness of S;
2. length >= 2 routes to GEN-L>=2 or GEN-R>=2.
```

Global class mapping:

```text
CONTRADICTION
or
PROPER_SUBINTERVAL / TEMPLATE_EXTERNAL_CANCELLATION
via GEN-L>=2 or GEN-R>=2.
```

---

### Type S2: nonduplicate singleton interval

Equation creates a singleton interval target not equal to a local atom.

Typical local form:

```text
T,a,b,-a
```

or

```text
a,b,-a,T.
```

Route:

```text
docs/analytic_generic_interval_length_one_theorem.md
```

Specifically:

```text
GEN-L1: T,a,b,-a -> b,a,T,-a.
GEN-R1: a,b,-a,T -> b,-a,T,a.
```

Global class mapping:

```text
SINGLETON_RECURRENCE
or local template state with finite type_rank.
```

Failures inside GEN-L1 / GEN-R1 are already routed to:

```text
affine/singleton,
duplicate/impossible,
template-aware external cancellation,
scalar/affine condition.
```

To avoid a loop, repeated S2 routing must be interpreted through F7's singleton-prefix recurrence class.

---

### Type S3: scalar singleton relation

Equation forces:

```text
b=2a
```

or mirror:

```text
a=2b.
```

Route:

```text
docs/analytic_scalar_absorption_theorem.md
```

Global class mapping:

```text
SCALAR_ABSORPTION
```

then:

```text
SUCCESS,
CONTRADICTION,
BOUNDARY_SENSITIVE_ZERO,
or TEMPLATE_EXTERNAL_CANCELLATION -> F6.
```

---

### Type S4: singleton-prefix recurrence

Equation creates a new forbidden hit or recurrent singleton-prefix branch of the form:

```text
x+q=f
```

or

```text
x+B_i=f.
```

Route:

```text
F7 singleton-prefix recurrence.
```

F7 states that singleton-prefix recurrence routes to:

```text
suffix-zero descent,
pair-difference prefix descent,
zero-composite branch,
external bridge branch,
cyclic recurrence,
collapse.
```

Global class mapping:

```text
SINGLETON_RECURRENCE -> F7 -> F9.
```

---

## Singleton Routing Theorem

### Statement

Every affine/singleton equation produced by the packaged endpoint-avoidance local modules routes to one of:

```text
1. contradiction by zero atom, duplicate atom, or Graham-validity violation;
2. duplicate-target interval theorem;
3. generic length-one interval theorem;
4. scalar absorption theorem;
5. F7 singleton-prefix recurrence;
6. template-aware external collision through F6;
7. proper subinterval descent through F4/F9.
```

Therefore affine/singleton outputs introduce no new global obstruction class beyond the F3/F9 state universe.

### Proof sketch

Take a local affine/singleton equation.

If it forces zero or a duplicate atom, route to contradiction.

If the singleton equals a target already present as a neighboring atom, it is a duplicate-target interval state and routes through the duplicate interval target theorem.

If the singleton is a genuine new one-atom interval target, it has one of the GEN-L1 or GEN-R1 local forms and routes through the generic length-one theorem.

If the equation is a coefficient-two scalar relation, route to scalar absorption.

If the singleton equation appears as a recurrent forbidden hit rather than a static interval target, route to F7 singleton-prefix recurrence.

All external failures generated by these modules are template-aware external collisions and embed into F6 by `analytic_template_external_collision_embedding_f6.md`.

All proper subinterval failures route to F4/F9 local descent.

Thus no new class remains. ∎

---

## Measure interpretation

Assign affine/singleton outputs to either:

```text
SINGLETON_RECURRENCE
```

or a finite local `type_rank` below the parent first-blocker template.

Repeated singleton routing is controlled by F7:

```text
bounded blockers strictly decrease enclosing_span;
external/cyclic blockers route to F6/F8/cyclic recurrence;
long internal blockers route to known classes.
```

Thus the intended global measure behavior is:

```text
1. immediate contradiction/success terminates;
2. duplicate/generic/scalar local modules have finite type-rank descent;
3. recurrence is handled by F7 and then consumed by F9.
```

---

## Remaining audit risk

This theorem depends on F7's singleton-prefix recurrence branch, which is still marked with an audit flag:

```text
A70 atom-singleton endpoint cases need explicit final text.
```

Therefore this note reduces the singleton-routing gap to the existing F7 audit obligation, but does not independently close that final endpoint-case audit.

---

## Consequence for endpoint-branch edge audit

This note addresses Gap 1 from:

```text
docs/analytic_endpoint_branch_f9_edge_audit.md
```

The remaining high-risk gaps are now:

```text
1. Boundary Zero Lemma.
2. F6 edge compatibility audit.
3. Fixed-ordering vs current-ordering formalism lemma.
4. F7 singleton-prefix endpoint audit inherited from A70.
```

---

## Significant status

The endpoint-branch affine/singleton outputs are now routed into existing local modules or F7/F9 recurrence machinery.

This is a reduction of proof risk, not a complete global termination proof.
