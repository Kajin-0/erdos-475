# Analytic Audit: F7 Cyclic-Cut Midpoint Characteristic Cases

This note audits the cyclic-cut recurrence midpoint equations and the characteristic-sensitive warnings in F7.

Claim boundary:

```text
This is a recurrence-routing audit note.
It is not a complete proof of Erdős 475.
It does not prove full F9 termination.
```

---

## Source files

Primary source:

```text
docs/analytic_cyclic_cut_recurrence_a71.md
```

Earlier cyclic-cut source:

```text
docs/analytic_cyclic_cut_a7.md
```

Midpoint routing source:

```text
docs/analytic_midpoint_boundary_a55.md
```

F7 theorem:

```text
docs/final/F07_recurrence_routing_theorem.md
```

F7 currently flags:

```text
A71 special midpoint equations and p=3 behavior require audit.
No division by 3 should occur.
```

This note addresses that flag.

---

## Standing cyclic-cut setup

Let:

```text
R=(r_1,...,r_t),
S_i=r_1+...+r_i,
S_0=0,
S_t=sigma.
```

Assume:

```text
S_h=f,
f != sigma.
```

A cyclic cut after index `c` produces the rotated ordering:

```text
R_c=(r_{c+1},...,r_t,r_1,...,r_c).
```

The rotated partial sums are:

```text
i>c:   S_i-S_c,
i<=c:  sigma-S_c+S_i.
```

These formulas are purely additive and use no division.

---

## Cyclic forbidden-hit equations

A rotated forbidden hit has one of two forms.

### Suffix hit

For `i>c`:

```text
S_i-S_c=f,
```

or:

```text
S_i=S_c+f.
```

### Wrapped hit

For `i<=c`:

```text
sigma-S_c+S_i=f,
```

or:

```text
S_i=S_c+f-sigma.
```

Again, these are additive endpoint-pair equations and use no division.

---

## Special equations from the cut at the forbidden hit

For the cyclic cut after the original forbidden hit `h`, the formula becomes:

```text
S_h=f.
```

A first-side forbidden hit after rotating at `h` requires:

```text
S_a-f=f,
```

so:

```text
S_a=2f.
```

A second-side forbidden hit requires:

```text
sigma-f+S_b=f,
```

so:

```text
S_b=2f-sigma.
```

These are the special cyclic equations:

```text
S_alpha=2f,
S_beta=2f-sigma.
```

They are obtained by addition/subtraction only.

---

## Midpoint interpretation without division

The special equations are midpoint-boundary equations in the following additive sense:

```text
S_alpha=2f
  <=>
S_alpha+S_0=2f.
```

and:

```text
S_beta=2f-sigma
  <=>
S_beta+S_t=2f.
```

since:

```text
S_0=0,
S_t=sigma.
```

Thus:

```text
2f=S_alpha+S_0,
2f=S_beta+S_t.
```

This is the same midpoint relation used in A55:

```text
2S_y=S_x+S_v.
```

No step requires dividing by 2. The proof only uses the displayed doubled equation.

Because `p` is odd in the Erdős 475 setting, division by 2 would be legal if needed. But the routing does not require it.

---

## Characteristic p=3 audit

In characteristic 3:

```text
2=-1.
```

Therefore the special equations become:

```text
S_alpha=-f,
S_beta=-f-sigma.
```

This does not create a new obstruction species.

The equations remain endpoint-pair / midpoint-boundary equations:

```text
S_alpha+S_0=2f,
S_beta+S_t=2f.
```

They route to A55 midpoint machinery exactly as in all odd characteristics.

No step requires:

```text
3^{-1},
f=(S_alpha+S_0)/2,
```

or any equation of the form:

```text
3x=y.
```

Thus `p=3` is harmless for the cyclic midpoint routing itself.

Any p=3 collapse would have to arise from an independent atom-duplication or zero-sum condition in a downstream local module, not from the cyclic midpoint equations.

---

## Interaction with A55 midpoint boundary

A55 analyzes adjacent equal-block exchange with:

```text
sum(A)=sum(C)=a.
```

The midpoint displayed equation is:

```text
2S_y=S_x+S_v.
```

A55 routes displayed collisions to:

```text
zero-prefix/interior-zero,
two-piece zero,
three-piece zero,
forbidden recurrence,
external/equal-interval routing.
```

The only endpoint characteristic-sensitive equation in A55 is:

```text
2a=0.
```

For odd prime `p`, including `p=3`, this implies:

```text
a=0.
```

which is a zero-sum interval collapse.

There is no use of division by 3 in A55.

---

## Wrapping blocker audit

A71 also routes A5 blockers after cyclic recurrence.

A non-wrapping blocker remains a contiguous interval in the original ordering and gives:

```text
ordinary zero-composite / signed interval.
```

A wrapping blocker crosses the cyclic cut and pulls back to:

```text
right bridge + left bridge + correction = 0.
```

This is a bridge zero/signed composite routed through:

```text
F6/F8/F9
```

or to singleton-prefix recurrence depending on orientation.

These blocker equations are additive interval equations and do not introduce characteristic-specific division.

---

## Cyclic-Cut Midpoint Characteristic Lemma

### Statement

The cyclic-cut special equations:

```text
S_alpha=2f,
S_beta=2f-sigma
```

are additive midpoint-boundary equations:

```text
2f=S_alpha+S_0,
2f=S_beta+S_t.
```

They route to A55 midpoint machinery without requiring division by 2 or division by 3.

In characteristic 3, the equations become:

```text
S_alpha=-f,
S_beta=-f-sigma,
```

but remain the same midpoint-boundary class and create no new recurrence species.

### Proof

The identities follow by substituting `S_0=0` and `S_t=sigma`. A71's cyclic-cut formulas are translations of old endpoints by `-S_c` or `sigma-S_c`. The special equations arise by setting the translated endpoint equal to `f`. All transformations are additions and subtractions in `F_p`. ∎

---

## Impact on F7

This note resolves the F7 audit flag:

```text
A71 special midpoint equations and p=3 behavior require audit.
No division by 3 should occur.
```

The result is:

```text
No division by 3 occurs.
p=3 gives no new cyclic-midpoint branch.
Special cyclic hits route to MIDPOINT / A55.
Wrapping blockers route to F6/F8 bridge machinery.
```

---

## Remaining recurrence risks after this audit

After the H1/H2 correction, pair-difference endpoint audit, singleton endpoint audit, and this cyclic midpoint audit, the F7 recurrence-specific risks are reduced to final manuscript hardening:

```text
1. inline or cite the H1/H2 corrected sign tables;
2. inline or cite the pair-difference endpoint table;
3. inline or cite the singleton-prefix endpoint table;
4. inline or cite this cyclic-cut midpoint characteristic audit;
5. cross-reference every F7 exit to F4/F5/F6/F8/F10/F11;
6. verify augmented span conventions at the final F9 level.
```

No currently identified F7 recurrence source remains an unclassified local algebraic species.

---

## Significant status

The cyclic-cut midpoint characteristic branch is now audited.

The remaining proof bottleneck is global measure descent and weighted-core termination, not cyclic-cut characteristic behavior.
