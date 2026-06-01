# Analytic Audit: F6 Edge Compatibility for Endpoint Branch

This note audits the compatibility between endpoint-avoidance local-template outputs and the existing F6 external-collision theorem.

Claim boundary:

```text
This is an edge-compatibility audit, not a complete proof of Erdős 475.
It verifies class coverage and records remaining measure/manuscript obligations.
```

---

## Inputs

Endpoint-branch local coverage:

```text
docs/analytic_local_reduction_coverage_summary.md
```

Template-to-F6 embedding:

```text
docs/analytic_template_external_collision_embedding_f6.md
```

Fixed-ordering formalism bridge:

```text
docs/analytic_fixed_ordering_formalism_lemma.md
```

F6 source theorem:

```text
docs/final/F06_external_collision_theorem.md
```

F6 relevant exits:

```text
F6.1 left external collision:
  L+u=0.

F6.2 right external collision:
  R+(w-u)=0.

F6.3 signed external collision:
  signed bridge composite -> pair-difference / transported-prefix / signed interval / equal interval / zero-composite / weighted-core.

F6.4 unchanged displayed endpoint collision:
  u-d=0 -> proper-overlap equal interval / separated equal interval / two-piece zero-composite / pair-difference / transported-prefix.
```

---

## Endpoint-branch external output forms

The packaged endpoint-branch modules produce external outputs of three forms.

### E-type 1: true template external cancellation

Template form:

```text
K + A = 0
```

or

```text
B + K = 0.
```

Here:

```text
pi(H)=A,B,
K = adjacent real interval outside H.
```

F6 mapping:

```text
K+A=0 -> F6.1 left external collision L+u=0.
B+K=0 -> F6.2 right external collision R+(w-u)=0.
```

Status:

```text
Fully embedded by analytic_template_external_collision_embedding_f6.md.
```

---

### E-type 2: collision with unchanged displayed endpoint family

Template form:

```text
new moved value = old unchanged value.
```

After subtracting the local basepoint:

```text
u=d.
```

or

```text
u-d=0.
```

These occur in local notes when a genuinely new prefix value collides with an unchanged tail value, e.g.

```text
new fixed value = a+b+Y_s,
new J-family value = old J-family value,
new value = old endpoint/tail value.
```

F6 mapping:

```text
F6.4 unchanged displayed endpoint collision.
```

F6 exits:

```text
proper-overlap equal interval,
separated equal interval,
two-piece zero-composite,
pair-difference boundary,
transported-prefix relation.
```

Status:

```text
Compatible with F6/F9 local descent classes.
```

Measure obligation:

```text
For proper-overlap cases, uncrossing must produce proper subinterval descent.
For separated cases, F5/F8 bridge-gap or separated-equal routing must decrease gap/span/support or route to recurrence.
```

---

### E-type 3: signed or bounded correction composite

Template form:

```text
interval sum + bounded atom/pair correction = 0.
```

Examples can arise after affine singleton substitution, scalar absorption, pair-corrected moves, or recurrence pullback:

```text
L+U+E=0,
R+V+E=0,
L-U+E=0,
R-V+E=0.
```

F6 mapping:

```text
F6.3 signed external collision.
```

F6 exits:

```text
pair-difference,
transported-prefix,
signed interval,
equal interval,
zero-composite,
weighted-core normal form.
```

Status:

```text
Compatible with F6 class universe.
```

Measure obligation:

```text
Weighted-core exits must be routed through F10/F11 and then consumed by F9.
This is outside the first-blocker local algebra and remains part of the global proof audit.
```

---

## Module-by-module F6 compatibility

### T1 and T2

T1 explicit external branches:

```text
T1-Lz,
T1-Rz,
T1-Lza,
T1-Rza.
```

F6 compatibility:

```text
left branches -> F6.1;
right branches -> F6.2;
collisions with unchanged J/tail families -> F6.4;
long right bridge relations -> F6.1/F6.2 followed by F8 bridge/gap.
```

T2 follows by mirror symmetry.

Status:

```text
Compatible.
```

Open check:

```text
The two T1 bridge notes show smaller enclosing span locally. Final proof must cross-reference F8/A98 exactly.
```

---

### T3 and T4

T3 external outputs route to:

```text
Left(a),
Left(a-b),
Right(-a-b),
Right(-a).
```

T4 mirror outputs route to:

```text
Left(-b),
Left(-a-b),
Right(b-a),
Right(b).
```

F6 compatibility:

```text
Each is an adjacent external interval cancellation K+A=0 or B+K=0.
```

Then:

```text
duplicate targets -> duplicate interval target theorem -> GEN-L>=2 / GEN-R>=2;
generic targets -> GEN-L1/GEN-R1 or GEN-L>=2/GEN-R>=2;
scalar branch -> scalar absorption -> F6 if external failure remains.
```

Status:

```text
Compatible.
```

Open check:

```text
T3/T4 do not create new F6 exits; they create primitive interval states that re-enter generic/duplicate modules.
```

---

### GEN-L1 / GEN-R1

External outputs in GEN-L1:

```text
K+(b)=0,
(a,T,-a)+K=0,
K+(b,a)=0,
(T,-a)+K=0.
```

External outputs in GEN-R1:

```text
K+(b,-a)=0,
(T,a)+K=0,
K+(b,-a,T)=0,
(a)+K=0.
```

F6 compatibility:

```text
All are directly F6.1 or F6.2 with explicitly recorded A/B split.
```

Status:

```text
Compatible.
```

Open check:

```text
Repeated singleton routing from GEN-L1/GEN-R1 must be controlled by analytic_singleton_routing_theorem.md and F7 singleton-prefix recurrence.
```

---

### GEN-L>=2 / GEN-R>=2

External outputs in GEN-L>=2 occur at:

```text
W=z+a,
W=z+a+b,
W=z+a+b+Y_s.
```

External outputs in GEN-R>=2 occur at:

```text
W=z,
W=z+a,
W=z+a+b.
```

F6 compatibility:

```text
All left outputs are F6.1.
All right outputs are F6.2.
Collisions with unchanged prefix/tail families are F6.4.
```

Status:

```text
Compatible.
```

Open check:

```text
Some GEN-L cross-prefix cases produce proper internal subintervals inside J. Final proof must cite F6.4/F4 uncrossing or local proper-subinterval descent.
```

---

### DUP-L / DUP-R

Duplicate interval targets do not produce independent F6 forms.

They route as:

```text
length one -> contradiction by duplicate atom;
length >= 2 -> GEN-L>=2 or GEN-R>=2.
```

F6 compatibility:

```text
Inherited from GEN-L>=2 / GEN-R>=2.
```

Status:

```text
Compatible.
```

---

### Scalar absorption

Scalar absorption external outputs arise after explicit finite repair moves such as:

```text
a,2a,-a,c -> c,-a,2a,a.
```

External failures at new values are ordinary endpoint collisions of the hypothetical repaired ordering.

F6 compatibility:

```text
left external outputs -> F6.1;
right external outputs -> F6.2;
relative-zero/boundary outputs -> analytic_boundary_zero_lemma.md.
```

Status:

```text
Compatible.
```

Open check:

```text
Small-characteristic cases p=3,p=5 require separate scalar boundary audit.
```

---

## F6 Edge Compatibility Theorem

### Statement

Every external or displayed-family collision produced by the endpoint-avoidance local modules is an instance of one of:

```text
1. F6.1 left external collision L+u=0;
2. F6.2 right external collision R+(w-u)=0;
3. F6.3 signed external collision with bounded correction;
4. F6.4 unchanged displayed endpoint collision u-d=0.
```

Consequently, no endpoint-branch local module produces an external-collision class outside the existing F6/F9 state universe.

### Proof sketch

For each local module, the proposed move has the form:

```text
R_hyp=X pi(H) Y,
pi(H)=A,B.
```

A collision with a left external context endpoint yields:

```text
K+A=0,
```

which is F6.1.

A collision with a right external context endpoint yields:

```text
B+K=0,
```

which is F6.2.

A collision with an unchanged displayed family yields:

```text
u-d=0,
```

which is F6.4.

If affine substitution or recurrence introduces bounded atom/pair correction, the equation has F6.3 signed-correction form.

The module-by-module list above exhausts the packaged endpoint-branch external outputs. ∎

---

## Remaining measure obligations

This audit proves class compatibility, not full termination.

Remaining obligations:

```text
1. F6.1/F6.2 bridge zero-composites must enter F8/F9 with strict span/gap/support descent or controlled recurrence.
2. F6.3 signed-correction exits to weighted-core normal form must be handled by F10/F11 and consumed by F9.
3. F6.4 unchanged displayed endpoint collisions must be uncrossed into proper-overlap/separated-equal/two-piece-zero states with F4/F5/F8 descent.
4. Repeated F6 exits must be bounded by recurrence_depth / bridge_depth in M_NW^*.
```

---

## Consequence for endpoint-branch audit

This note addresses the F6 edge compatibility gap from:

```text
docs/analytic_endpoint_branch_f9_edge_audit.md
```

Remaining high-risk gaps after this note:

```text
1. F7 singleton-prefix endpoint audit inherited from A70.
2. Small-characteristic scalar boundary audit.
3. Full F9 edge-by-edge measure descent proof.
```

---

## Significant status

All endpoint-branch external outputs now have explicit F6 destinations.

The proof risk has moved from class coverage to measure descent and the remaining F7/scalar audits.
