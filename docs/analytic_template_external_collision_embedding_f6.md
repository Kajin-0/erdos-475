# Analytic Theorem Note: Embedding Template-Aware External Cancellations into F6

This note connects the newly packaged template-aware external-cancellation states to the existing external-collision framework in:

```text
docs/final/F06_external_collision_theorem.md
docs/final/F09_nonweighted_termination_theorem.md
```

Claim boundary:

```text
This is an integration theorem note, not a complete proof of Erdős 475.
It shows that the new template-aware external states fit the existing F6 external-collision class.
Global termination still requires the F9 edge-by-edge measure audit.
```

---

## Background

The local template reconstruction introduced the corrected external-collision normal form.

If a local window `H` has total

```text
E=sum(H)
```

and a proposed total-preserving permutation splits as

```text
pi(H)=A,B,
```

then a moved endpoint after prefix `A` has relative value

```text
W=sum(A).
```

External collisions are:

```text
Left:
  K + A = 0,

Right:
  B + K = 0,
```

where `K` is the adjacent real interval outside the active window.

This note verifies that this is exactly the F6 external-collision framework.

---

## F6 setup

F6 decomposes the current ordering as

```text
R = X W Y
```

where:

```text
X = left external context,
W = active local window,
Y = right external context.
```

A local move replaces `W` by `W'` with the same total:

```text
sum(W')=sum(W)=w.
```

Let

```text
x=sum(X).
```

An internal moved endpoint of `W'` has form

```text
x+u,
```

where `u` is a nonempty proper prefix sum of `W'`.

In template notation:

```text
W'=pi(H)=A,B,
u=sum(A),
w-u=sum(B).
```

---

## Left external collision embedding

F6 left external endpoints have form

```text
x-L,
```

where `L` is the sum of a nonempty suffix of `X` ending at the window basepoint.

A collision

```text
x+u=x-L
```

gives

```text
L+u=0.
```

In template notation:

```text
u=sum(A),
L=sum(K),
```

where `K` is the adjacent real interval on the left.

Therefore:

```text
L+u=0
```

is exactly:

```text
sum(K)+sum(A)=0.
```

So the template-aware left cancellation

```text
K+A=0
```

is precisely F6.1's left external bridge zero-composite.

---

## Right external collision embedding

F6 right external endpoints have form

```text
x+w+R,
```

where `R` is the sum of a nonempty prefix of `Y` starting after the window.

A collision

```text
x+u=x+w+R
```

gives

```text
R+(w-u)=0.
```

In template notation:

```text
w-u=sum(B),
R=sum(K),
```

where `K` is the adjacent real interval on the right.

Therefore:

```text
R+(w-u)=0
```

is exactly:

```text
sum(K)+sum(B)=0.
```

So the template-aware right cancellation

```text
B+K=0
```

is precisely F6.2's right external bridge zero-composite.

---

## Embedding theorem

### Statement

Every template-aware external-cancellation child produced by the packaged local modules is an instance of the F6 external-collision class.

More precisely:

```text
Template left cancellation K+A=0
  embeds as F6 left external collision L+u=0.

Template right cancellation B+K=0
  embeds as F6 right external collision R+(w-u)=0.
```

Consequently, template-aware external-cancellation states should be assigned global obstruction class:

```text
EXTERNAL_COLLISION
```

with endpoint/block data retaining:

```text
pi(H)=A,B,
K,
side,
collision equation.
```

### Proof

The left and right calculations above are direct substitutions into the F6 setup:

```text
u=sum(A),
w-u=sum(B),
L=sum(K_left),
R=sum(K_right).
```

Thus the template-aware normal form is not a new class. It is the explicit endpoint/block data for F6's external-collision class. ∎

---

## Fixed-ordering caveat

The analytic endpoint-avoidance reconstruction uses a fixed original Graham-valid ordering and treats local moves hypothetically.

F6 is written in terms of a current ordering `R=XWY` and transformed ordering `R'=XW'Y`.

This difference is not algebraic; both frameworks derive the same obstruction equation from the failed local move.

For final proof integration, the state object should record:

```text
R_fixed = original Graham-valid ordering;
W      = active window in R_fixed;
W'     = proposed local permutation;
X,Y    = fixed external contexts relative to W;
collision endpoint in X or Y.
```

Then the F6 equations apply verbatim without committing to an actual iterative mutation of `R_fixed`.

---

## Consequence for local modules

All local module outputs labeled:

```text
TEMPLATE_EXTERNAL_CANCELLATION
```

can be globally routed as:

```text
EXTERNAL_COLLISION -> F6 -> F4/F5/F7/F8/F10/F11 or terminal contradiction.
```

This includes external outputs from:

```text
T1,
T2,
T3,
T4,
GEN-L1 / GEN-R1,
GEN-L>=2 / GEN-R>=2,
DUP-L / DUP-R,
Scalar absorption.
```

The template-aware data should not be discarded, but it is carried as `E` in the F03 state object.

---

## Remaining obligation

This embedding note does not itself prove global termination.

The remaining work is to audit that F6's outgoing routes are compatible with the newly packaged local modules and the fixed-ordering endpoint-avoidance proof.

Specifically, need to verify:

```text
1. F6 bridge zero-composites match the BRIDGE_GAP_SMALLER_ENCLOSURE cases documented in T1.
2. F6 unchanged displayed endpoint collisions match proper subinterval/equal-interval states in the local notes.
3. F6 recurrence exits match the recurrence-depth coordinates in M_NW^*.
4. No template-aware external child bypasses F6's class universe.
```

---

## Significant status

This note is a global integration step.

It shows that the corrected template-aware external-cancellation machinery is not parallel to the existing repo proof framework. It is a concrete specialization of F6.

The main unsolved layer is now the F9 edge-by-edge measure audit for the endpoint-avoidance branch.
