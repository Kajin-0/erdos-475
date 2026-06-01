# Analytic Audit: Endpoint-Branch F9 Measure Descent

This note specializes the F9 non-weighted termination theorem to the endpoint-avoidance local modules packaged in this reconstruction phase.

Claim boundary:

```text
This is an endpoint-branch measure audit, not a complete proof of Erdős 475.
It is conditional on the final validity of F3--F8 and F10--F11.
```

---

## Source files

Endpoint local coverage:

```text
docs/analytic_local_reduction_coverage_summary.md
```

Endpoint/global interface notes:

```text
docs/analytic_template_external_collision_embedding_f6.md
docs/analytic_endpoint_branch_f9_edge_audit.md
docs/analytic_singleton_routing_theorem.md
docs/analytic_boundary_zero_lemma.md
docs/analytic_fixed_ordering_formalism_lemma.md
docs/analytic_f6_edge_compatibility_audit.md
docs/analytic_scalar_small_characteristic_audit.md
docs/analytic_f7_singleton_endpoint_audit.md
```

Global termination framework:

```text
docs/final/F09_nonweighted_termination_theorem.md
```

---

## Measure

Use the F9 non-weighted measure:

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

The order is lexicographic over nonnegative integers.

For endpoint-branch states, evaluate `enclosing_span` and `support_size` using the provenance-rich fixed-ordering state from:

```text
docs/analytic_fixed_ordering_formalism_lemma.md
```

That is, every node stores:

```text
R_fixed,
active window,
local block H,
proposed permutation pi(H),
external interval K if present,
recurrent hit/blocker data if present,
local theorem tag.
```

---

## Endpoint-branch output classes

The packaged endpoint modules output only:

```text
SUCCESS,
CONTRADICTION,
AFFINE_SINGLETON,
PROPER_SUBINTERVAL,
TEMPLATE_EXTERNAL_CANCELLATION,
BRIDGE_GAP_SMALLER_ENCLOSURE,
BOUNDARY_SENSITIVE_ZERO,
SCALAR_ABSORPTION.
```

The edge audit maps these into F9 classes:

```text
AFFINE_SINGLETON              -> SINGLETON_RECURRENCE / generic singleton modules.
PROPER_SUBINTERVAL            -> F4 local zero/equal/pair classes.
TEMPLATE_EXTERNAL_CANCELLATION -> EXTERNAL_COLLISION.
BRIDGE_GAP_SMALLER_ENCLOSURE  -> BRIDGE_GAP.
BOUNDARY_SENSITIVE_ZERO       -> ZERO_COLLAPSE/PREFIX_ZERO or boundary_rank finite branch.
SCALAR_ABSORPTION             -> finite local scalar class, then SUCCESS/CONTRADICTION/EXTERNAL_COLLISION.
```

---

## Coordinate descent audit

### 1. SUCCESS

Terminal.

Measure:

```text
not evaluated after termination.
```

---

### 2. CONTRADICTION

Includes:

```text
zero atom,
duplicate atom,
nonempty zero interval,
repeated partial sum,
small-characteristic scalar collapse,
minimality violation.
```

Terminal.

Measure:

```text
not evaluated after termination.
```

---

### 3. PROPER_SUBINTERVAL

Local forms:

```text
proper prefix inside J,
proper suffix inside K',
proper internal subinterval inside J or K',
proper overlap uncrossing,
proper two-piece zero composite inside a smaller local tail.
```

F9 route:

```text
F4 local descent -> F9.1.
```

Primary decreasing coordinate:

```text
enclosing_span
```

if the child subinterval is strictly contained in the parent active window.

Fallback decreasing coordinate:

```text
support_size
```

if the enclosing span is unchanged but the participating obstruction support is strictly smaller.

Endpoint-module status:

```text
T1/T2 proper prefix/suffix/internal-subinterval outputs are strict subwindows of the parent template.
GEN-L/GEN-R prefix/subinterval outputs are strict subwindows of J or of the split interval tail.
T3/T4 proper outputs enter GEN modules or F4 local descent.
```

Audit risk:

```text
The final manuscript must check every local note's "proper prefix/suffix/subinterval" label against the stored parent active window.
```

No new endpoint-specific risk remains.

---

### 4. BRIDGE_GAP_SMALLER_ENCLOSURE

Endpoint bridge forms include:

```text
sum(J_s^+) + sum(K_t^-)=0
```

arising from:

```text
T1-Rz-long,
T1-Rza-long,
T2 mirror branches.
```

F9 route:

```text
F8 bridge/gap descent -> F9.5.
```

Primary decreasing coordinate for the endpoint-created bridge:

```text
enclosing_span.
```

Local proof:

```text
bridge support lies inside J_s^+, y, K_t^-;
parent repair support is a,b,z,J,y,K';
therefore the bridge enclosure omits at least a,b,z and is strictly smaller.
```

If F8 later transforms the bridge rather than immediately terminating, its possible decreases are:

```text
enclosing_span,
gap_length,
support_size,
bridge_depth.
```

Audit risk:

```text
Need exact F8/A98 cross-reference in final manuscript.
```

Endpoint-specific bridge creation is now locally routed.

---

### 5. TEMPLATE_EXTERNAL_CANCELLATION

Template forms:

```text
K+A=0,
B+K=0.
```

F9 route:

```text
EXTERNAL_COLLISION -> F6 -> F9.3.
```

F6 exits to:

```text
bridge zero-composite,
signed bridge composite,
equal/separated interval,
transported-prefix,
pair-difference,
cyclic recurrence,
singleton/prefix recurrence,
weighted-core normal form,
collapse or minimality contradiction.
```

Primary decreasing coordinates after F6 exit:

```text
bridge zero-composite      -> enclosing_span / gap_length / support_size / bridge_depth via F8;
signed/equal/pair/local    -> enclosing_span / support_size / pair_depth via F4;
separated equal/midpoint    -> gap_length / separated_depth via F5;
recurrence                 -> recurrence_depth, then enclosing_span by bounded-blocker descent via F7;
weighted-core              -> exits to F10/F11, not a non-weighted cycle;
collapse                   -> terminal.
```

Endpoint-specific audit:

```text
docs/analytic_f6_edge_compatibility_audit.md
```

shows all endpoint external outputs are F6.1/F6.2/F6.3/F6.4.

Audit risk:

```text
Full F6/F8/F10/F11 measure proof remains inherited from final framework.
No new endpoint-specific F6 edge remains unclassified.
```

---

### 6. AFFINE_SINGLETON

Endpoint forms:

```text
z=T_*,
y=T_*,
T=T_*,
b=2a,
a=2b,
```

F9 route:

```text
SINGLETON_RECURRENCE / singleton local module / scalar absorption.
```

Endpoint routing theorem:

```text
docs/analytic_singleton_routing_theorem.md
```

Routing cases:

```text
zero/duplicate atom          -> terminal contradiction;
duplicate interval target    -> duplicate interval theorem;
nonduplicate length-one      -> GEN-L1 / GEN-R1;
scalar coefficient-two       -> scalar absorption;
recurrent singleton-prefix   -> F7 singleton-prefix recurrence;
external output              -> F6.
```

Primary decreasing coordinate depends on route:

```text
duplicate interval length-one -> terminal contradiction;
duplicate interval length>=2  -> type_rank decreases into GEN-L/GEN-R;
GEN-L1/GEN-R1                 -> finite type_rank descent or F6 external route;
scalar absorption             -> finite type_rank / boundary_rank branch;
F7 singleton recurrence        -> recurrence_depth then enclosing_span by bounded-blocker descent;
proper subinterval             -> enclosing_span / support_size.
```

Endpoint-specific audit:

```text
docs/analytic_f7_singleton_endpoint_audit.md
```

shows the atom-singleton endpoint cases route to zero-atom contradiction, pair-difference, or bridge classes.

Audit risk:

```text
General F7 recurrence routing still inherits global H1/H2, cyclic, and pair-difference audit risks, but the endpoint-specific atom-singleton gap is closed.
```

---

### 7. SCALAR_ABSORPTION

Scalar branches:

```text
b=2a,
a=2b.
```

Local theorem:

```text
docs/analytic_scalar_absorption_theorem.md
```

Small-characteristic audit:

```text
docs/analytic_scalar_small_characteristic_audit.md
```

Routes:

```text
right-neighbor absorption,
left-neighbor absorption,
explicit d=-2a boundary repair,
explicit d=-3a repair,
whole-set repair,
mirror repairs.
```

Primary decreasing/finite coordinates:

```text
type_rank
boundary_rank
```

or terminal success/contradiction.

Any external failure produced by scalar absorption is:

```text
TEMPLATE_EXTERNAL_CANCELLATION -> F6.
```

Small characteristics:

```text
p=3 -> scalar triple duplicate collapse;
p=5 in d=-3a branch -> neighbor duplicates 2a.
```

Therefore scalar absorption is finite and cannot support an infinite same-measure branch.

Audit risk:

```text
None endpoint-specific after small-characteristic audit, except inherited F6/F9 termination for external outputs.
```

---

### 8. BOUNDARY_SENSITIVE_ZERO

Boundary lemma:

```text
docs/analytic_boundary_zero_lemma.md
```

Routes:

```text
interior relative zero -> terminal contradiction;
beginning-boundary relative zero -> explicit finite boundary repair or boundary_rank branch;
ending-boundary total zero -> contradiction unless whole-set boundary case;
whole-set scalar zero case -> explicit scalar repair.
```

Primary decreasing/finite coordinate:

```text
boundary_rank.
```

Terminal cases:

```text
ZERO_COLLAPSE,
PREFIX_ZERO,
CONTRADICTION.
```

Endpoint-specific audit:

```text
Boundary zero branches are finite local exceptions, not recurrence species.
```

Audit risk:

```text
Final manuscript should cross-reference every "boundary-sensitive" local note to this lemma.
```

---

## Endpoint-Branch F9 Measure Audit Theorem

### Statement

Assume the global F9 framework and its dependencies F3--F8 and F10--F11 are valid.

Then every nonterminal endpoint-branch state produced by the packaged local modules either:

```text
1. strictly decreases enclosing_span;
2. strictly decreases gap_length;
3. strictly decreases support_size;
4. decreases one of recurrence_depth, pair_depth, separated_depth, or bridge_depth after routing through F6/F7/F8;
5. decreases finite type_rank or boundary_rank;
6. exits to weighted-core machinery F10/F11;
7. or terminates by success/contradiction.
```

Therefore the endpoint-branch local modules introduce no additional non-weighted cycle beyond those already covered by F9.

### Proof sketch

The endpoint local output universe is exhausted by the eight classes listed above.

Each class maps to the F9 non-weighted universe or a terminal/finite local branch. The coordinate-descent mapping is given in the audit table above.

For classes that route to F6/F7/F8/F10/F11, the result is conditional on those global theorems, exactly as F9 itself is conditional.

Thus endpoint-specific local algebra does not create a new termination obligation outside F9. ∎

---

## What remains after this audit

This note does not prove F9 itself.

The remaining proof work is to harden the global final-framework dependencies:

```text
1. F4 local descent proof details.
2. F5 separated-equal/midpoint routing.
3. F6 external collision theorem final manuscript form.
4. F7 recurrence routing theorem, especially H1/H2 signs, pair-difference endpoint table, cyclic-cut midpoint equations.
5. F8 bridge/gap descent theorem.
6. F10/F11 weighted-core termination.
7. final assembly from endpoint avoidance to Erdős 475.
```

Endpoint-branch-specific gaps have been reduced to those inherited global obligations.

---

## Significant status

The endpoint-avoidance branch now has:

```text
local coverage,
external-collision embedding,
singleton routing,
boundary-zero handling,
fixed-ordering formalism,
F6 edge compatibility,
scalar small-characteristic audit,
F7 singleton endpoint audit,
F9 endpoint measure audit.
```

The remaining work is global final-proof hardening, not another endpoint-specific local branch expansion.
