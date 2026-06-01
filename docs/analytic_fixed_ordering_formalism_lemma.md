# Analytic Lemma Note: Fixed-Ordering vs Current-Ordering Formalism

This note addresses the fixed-ordering/current-ordering gap identified in:

```text
docs/analytic_endpoint_branch_f9_edge_audit.md
docs/analytic_template_external_collision_embedding_f6.md
```

Claim boundary:

```text
This is a formalism bridge lemma for the endpoint-avoidance proof architecture.
It is not a complete proof of Erdős 475.
```

---

## Purpose

The endpoint-avoidance reconstruction often fixes one original Graham-valid ordering:

```text
R=(r_1,...,r_t)
```

chosen with minimal first forbidden hit, and then analyzes hypothetical local replacements inside that fixed ordering.

Several extracted global theorems, especially:

```text
docs/final/F06_external_collision_theorem.md
docs/final/F07_recurrence_routing_theorem.md
docs/final/F09_nonweighted_termination_theorem.md
```

are phrased in current-ordering form:

```text
R = X W Y,
R' = X W' Y.
```

This note records why the algebraic obstruction equations are the same, provided the obstruction state stores provenance data.

---

## Fixed-ordering state

A fixed-ordering endpoint-avoidance obstruction state should store:

```text
Omega=(R_fixed, I, H, pi(H), side_data, tag)
```

where:

```text
R_fixed = original Graham-valid ordering;
I       = active interval/window in R_fixed;
H       = active local block inside I;
pi(H)   = proposed permutation of H;
side_data = optional external interval K and split data;
tag     = local module provenance.
```

If the proposed local replacement is inserted, the hypothetical ordering is:

```text
R_hyp = X pi(H) Y
```

where:

```text
R_fixed = X H Y.
```

The proof does not need to mutate `R_fixed` globally. It only needs endpoint equations derived from the hypothetical insertion.

---

## Current-ordering state

The current-ordering formalism in F6/F7/F9 begins from:

```text
R = X W Y
```

and replaces `W` by `W'`:

```text
R' = X W' Y.
```

This is exactly the same local algebra after setting:

```text
R = R_fixed,
W = H,
W' = pi(H),
R' = R_hyp.
```

The only difference is interpretive:

```text
current-ordering style: R' may become the next active ordering;
fixed-ordering style: R' is a hypothetical witness or failed candidate generated from R_fixed.
```

The endpoint equations are identical.

---

## Internal endpoint equation equivalence

Let

```text
x=sum(X),
w=sum(H)=sum(pi(H)).
```

Let a prefix of the proposed block `pi(H)` have sum:

```text
u.
```

The corresponding hypothetical global endpoint is:

```text
x+u.
```

An internal failure in current-ordering notation occurs when:

```text
x+u = x+v
```

for another endpoint `v` inside the active window, or when:

```text
x+u=f.
```

In fixed-ordering notation, the same equation is read relative to the same basepoint `x`.

Subtracting `x`, all internal equations are identical.

Therefore any internal obstruction derived in the local notes is a valid F4/F7/F9 obstruction equation for the hypothetical candidate.

---

## External endpoint equation equivalence

Let:

```text
pi(H)=A,B,
u=sum(A),
w-u=sum(B).
```

### Left external endpoint

A left external endpoint in `X` has form:

```text
x-L
```

where `L` is the sum of a suffix interval `K` of `X` adjacent to the window.

Collision with the moved endpoint gives:

```text
x+u=x-L.
```

Equivalently:

```text
L+u=0.
```

In template-aware fixed-ordering notation:

```text
sum(K)+sum(A)=0.
```

Thus F6 left external collision and fixed-ordering template left cancellation are identical.

### Right external endpoint

A right external endpoint in `Y` has form:

```text
x+w+R
```

where `R` is the sum of a prefix interval `K` of `Y` adjacent to the window.

Collision gives:

```text
x+u=x+w+R.
```

Equivalently:

```text
R+(w-u)=0.
```

In template-aware fixed-ordering notation:

```text
sum(K)+sum(B)=0.
```

Thus F6 right external collision and fixed-ordering template right cancellation are identical.

---

## Recurrence equation equivalence

F7 recurrence starts from a hypothetical ordering `R'` that remains Graham-valid but still hits the forbidden value at a recurrent endpoint.

In fixed-ordering endpoint avoidance, this is exactly the case:

```text
R_hyp = X pi(H) Y
```

is Graham-valid but hits `f`.

The A5 adjacent-blocker equation is computed inside `R_hyp`:

```text
S'_{H-1}+z=S'_j.
```

This equation only depends on the endpoint values of `R_hyp`, which are explicitly computable from `R_fixed`, `H`, and `pi(H)`.

Therefore F7's blocker pullbacks can be recorded as obstruction equations on the fixed-ordering state, as long as `Omega` stores:

```text
pi(H),
first recurrent hit index in R_hyp,
next atom z,
blocker endpoint j,
pullback support in R_fixed.
```

No actual mutation of the master ordering is needed.

---

## Measure compatibility

The global measure:

```text
M_NW^*
```

should be evaluated on the obstruction support stored in `Omega`, not on an implicit mutable runtime ordering.

For a fixed-ordering state, define:

```text
enclosing_span(Omega)
```

as the smallest interval in `R_fixed` containing all atoms participating in the obstruction equation, plus any moved atoms and correction atoms required by the augmented support convention.

This agrees with F7's augmented support convention:

```text
Supp_src^+(O),
Supp_blk^+(j,H).
```

Thus F7 bounded-blocker descent remains valid in fixed-ordering form:

```text
Supp_blk^+ subsetneq Supp_src^+
  -> enclosing_span(child) < enclosing_span(parent).
```

---

## Fixed-Ordering Formalism Lemma

### Statement

Every obstruction equation generated by a hypothetical local replacement inside a fixed Graham-valid ordering is algebraically identical to the corresponding current-ordering equation in F6/F7/F9 after identifying:

```text
R = R_fixed,
W = H,
W' = pi(H),
R' = R_hyp.
```

Therefore the endpoint-avoidance proof may use F6/F7/F9 routing theorems without treating `R_fixed` as physically mutated at every obstruction-tree node, provided every node stores the required provenance data.

### Proof

Internal endpoints, external endpoints, and recurrent endpoints have the same formulas in both formalisms:

```text
internal: x+u,
left external: x-L,
right external: x+w+R,
recurrence: endpoint equations inside R_hyp.
```

Subtracting the common basepoint gives the same obstruction equations:

```text
internal equal/zero/forbidden equations,
L+u=0,
R+(w-u)=0,
A5 blocker pullbacks.
```

The support and measure are then evaluated using the stored atoms in `R_fixed`, with the same augmented support convention as F7/A99.

Thus the formalisms are equivalent for routing and measure purposes. ∎

---

## Required provenance fields

To avoid ambiguity, final obstruction-tree nodes should store at least:

```text
R_fixed identifier;
active window indices [L+1,R];
local block H;
proposed permutation pi(H);
proposed split A,B for external collision;
external interval K and side, if present;
recurrent hit index in R_hyp, if recurrence occurs;
A5 blocker endpoint, if recurrence occurs;
augmented source support;
augmented blocker support;
local theorem tag.
```

This eliminates the ambiguity that caused bare `Left(T)` / `Right(T)` labels to be unsafe.

---

## Consequence for endpoint-branch edge audit

This note addresses Gap 4 from:

```text
docs/analytic_endpoint_branch_f9_edge_audit.md
```

Remaining high-risk gaps after this note:

```text
1. F6 edge compatibility audit.
2. F7 singleton-prefix endpoint audit inherited from A70.
3. Small-characteristic scalar boundary audit.
```

---

## Significant status

The endpoint-avoidance proof can now cite F6/F7/F9 in a fixed-ordering obstruction-tree setting, provided the final manuscript uses the provenance-rich state object described here.
