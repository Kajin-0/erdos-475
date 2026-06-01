# Analytic Lemma Note: Boundary Zero Handling

This note addresses the boundary-sensitive zero gap identified in:

```text
docs/analytic_endpoint_branch_f9_edge_audit.md
docs/analytic_singleton_routing_theorem.md
```

Claim boundary:

```text
This is a local/global interface lemma for endpoint-branch proof routing.
It is not a complete proof of Erdős 475.
```

---

## Purpose

Many local template notes record conditions as:

```text
boundary-sensitive zero,
relative zero,
zero endpoint,
```

rather than silently discarding them.

This is necessary because a relative zero inside an active local block can mean two different things depending on whether the active block begins at the global start of the ordering.

This note packages the rule.

---

## Global setup

Let

```text
R=(r_1,...,r_t)
```

be a Graham-valid ordering.

Define partial sums:

```text
P_i = r_1+...+r_i,
```

with the empty sum denoted by

```text
P_0=0.
```

Graham-valid means the nonempty partial sums

```text
P_1,...,P_t
```

are pairwise distinct.

The empty sum `P_0` is not itself one of the nonempty partial sums, but a repeated endpoint inside a local block may still imply equality between two nonempty partial sums if the local block does not start at index 1.

---

## Local relative-coordinate setup

Let an active local window be

```text
H=(r_{L+1},...,r_R)
```

with basepoint

```text
v=P_L.
```

A relative partial sum inside the window has form

```text
S_j = r_{L+1}+...+r_j,
```

for

```text
L < j <= R.
```

The corresponding global partial sum is

```text
P_j = v + S_j.
```

A relative zero occurs when

```text
S_j=0.
```

Then

```text
P_j = v = P_L.
```

---

## Lemma 1: interior relative zero is contradiction

### Statement

If

```text
L >= 1
```

and a nonempty relative prefix of the active window has sum zero, then Graham-validity is contradicted.

### Proof

If `L>=1`, then `P_L` is a nonempty partial sum of the original ordering.

A nonempty relative prefix with sum zero gives

```text
P_j=P_L
```

for some `j>L`.

Both `P_L` and `P_j` are nonempty partial sums, and they occur at distinct indices. This contradicts pairwise distinctness. ∎

---

## Lemma 2: beginning-boundary relative zero is not automatically contradiction

### Statement

If

```text
L=0,
```

a nonempty relative prefix of the active window may have sum zero without immediately contradicting Graham-validity, because it only gives

```text
P_j=P_0=0,
```

and `P_0` is not a nonempty partial sum.

### Consequence

Beginning-boundary relative zero must be handled separately.

It can still be impossible if another nonempty partial sum is also zero, or if the zero occurs in a way that creates a duplicate later endpoint. But it is not automatically forbidden solely because it equals the empty sum.

---

## Lemma 3: ending-boundary total zero is contradiction unless global total is zero-allowed by context

Suppose the active local window ends at the global end:

```text
R=t.
```

If the active window total is zero and `L>=1`, then:

```text
P_t=P_L.
```

Both are nonempty partial sums, so this contradicts Graham-validity.

If `L=0`, then:

```text
P_t=0.
```

This is a nonempty partial sum equal to the empty sum. Graham-validity alone does not compare `P_t` with `P_0`, but in the endpoint-avoidance application this case must be checked against the forbidden endpoint and the set total:

```text
P_t = sigma(S).
```

Thus whole-set zero-total cases require explicit boundary treatment, not automatic contradiction.

---

## Boundary Zero Routing Rule

Every relative-zero output from a local template must be routed as follows.

### Case A: active basepoint is interior

If

```text
L>=1,
```

then:

```text
relative zero -> CONTRADICTION.
```

Global class:

```text
ZERO_COLLAPSE / PREFIX_ZERO / CONTRADICTION.
```

### Case B: active basepoint is global beginning

If

```text
L=0,
```

then:

```text
relative zero -> BOUNDARY_ZERO_BEGIN.
```

This must be handled by one of:

```text
1. explicit boundary repair;
2. contradiction from a later repeated nonempty zero partial sum;
3. contradiction from duplicate/nonzero atom assumptions;
4. finite boundary-rank descent.
```

### Case C: active endpoint is global end

If a total-zero condition occurs at the end, then route to:

```text
BOUNDARY_ZERO_END.
```

This must be handled by:

```text
1. interior contradiction if L>=1;
2. whole-set explicit repair if L=0;
3. endpoint-avoidance check using sigma(S) and f != sigma(S).
```

---

## Application to scalar absorption

Scalar absorption produced the clearest boundary-sensitive cases.

### Case d=-2a

Block:

```text
-2a,a,2a,-a
```

has total zero.

If this four-block is interior, the total-zero condition repeats the local basepoint and is a contradiction.

If it starts at the global beginning, the explicit repair used in the scalar absorption note is:

```text
-2a,a,2a,-a -> a,2a,-a,-2a.
```

This boundary repair is finite and does not generate an infinite boundary-zero branch.

### Case no neighbors

If the scalar triple is the whole set:

```text
S={a,2a,-a},
```

then the ordering

```text
-a,a,2a
```

has partial sums:

```text
-a,
0,
2a.
```

The zero occurs as a nonempty partial sum equal to the empty sum, which is not automatically forbidden by Graham-validity. This is why the whole-set boundary case must be treated explicitly.

---

## Boundary Zero Lemma

### Statement

Every boundary-sensitive zero condition produced by the packaged endpoint-avoidance local modules routes to one of:

```text
1. contradiction, if the zero repeats a nonempty partial sum;
2. explicit finite boundary repair, if the active block starts at the global beginning;
3. endpoint-total check, if the active block is the whole set or ends at the global end;
4. scalar absorption boundary case;
5. boundary_rank decrease in M_NW^*.
```

In particular, boundary-sensitive zero conditions introduce no new infinite obstruction class, provided each explicit boundary case is listed in the local module where it occurs.

### Proof sketch

A relative zero always means equality between the current global endpoint and the active basepoint:

```text
P_j=P_L.
```

If `L>=1`, this repeats two nonempty partial sums and is terminal contradiction.

If `L=0`, the equality is with the empty sum, which is not part of the Graham-valid partial-sum set. Therefore the case must be explicitly repaired or assigned to a finite boundary class.

The packaged scalar absorption theorem lists the only scalar whole-block boundary cases currently exposed by the first-blocker modules. Generic local modules route their boundary-zero outputs either to duplicate/nonzero contradictions or to explicit scalar/generic interval cases.

Thus boundary-zero branches are finite local exceptions, not a new recurrence species. ∎

---

## Measure interpretation

Boundary-sensitive states should use the coordinate:

```text
boundary_rank
```

in

```text
M_NW^*.
```

Suggested finite rank order:

```text
0. no boundary issue;
1. beginning-boundary relative zero;
2. ending-boundary total zero;
3. whole-set zero-total case;
4. scalar exceptional boundary block.
```

A final proof should choose the order so that every explicit repair decreases boundary_rank or terminates.

---

## Remaining audit obligations

This note reduces the boundary-zero gap but leaves two manuscript obligations:

```text
1. Verify every local note that says "boundary-sensitive" points to one of the cases above.
2. Audit small characteristics, especially p=3 and p=5, in scalar absorption and whole-set repairs.
```

---

## Consequence for endpoint-branch edge audit

This note addresses Gap 2 from:

```text
docs/analytic_endpoint_branch_f9_edge_audit.md
```

Remaining high-risk gaps after this note:

```text
1. F6 edge compatibility audit.
2. Fixed-ordering vs current-ordering formalism lemma.
3. F7 singleton-prefix endpoint audit inherited from A70.
4. Small-characteristic scalar boundary audit.
```

---

## Significant status

Boundary-sensitive zero conditions are now routed into terminal contradiction or finite boundary handling.

They are no longer an unclassified global obstruction type.
