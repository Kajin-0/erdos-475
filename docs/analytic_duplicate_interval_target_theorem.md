# Analytic Theorem Note: Duplicate Interval Target Templates

This note packages duplicate-target interval routing for left and right interval states.

Claim boundary:

```text
This is a local routing theorem note, not a complete proof of Erdős 475.
The global obstruction-tree termination theorem remains open.
```

---

## Purpose

The T3 right singleton blocker routes two external branches to duplicate interval targets:

```text
E1 -> Left(a)
E4 -> Right(-a)
```

where the target is already an atom in the neighboring active local block.

This note records the general duplicate-target principle:

```text
1. length-one duplicate interval is impossible because S is a set;
2. length-at-least-two duplicate interval routes to the generic splitting templates.
```

This prevents duplicate-target states from being treated as a separate obstruction class.

---

## Duplicate target principle

Let an interval state have target `T` and suppose `T` is already one of the atoms in the adjacent active local block.

If the external interval had length one, then it would consist of the singleton atom `T`.

But the active local block already contains the atom `T`.

Since `S` is a set, the same nonzero field element cannot occur twice as two different atoms.

Therefore:

```text
Duplicate-target interval states have interval length at least two.
```

This is the main simplification.

---

# DUP-L: duplicate left interval target

## Setup

Local form:

```text
I, a, b, -a
```

with

```text
sum(I)=T,
T in {a,b,-a}
```

or, more generally, `T` is already an atom in the active local block adjacent to `I`.

The duplicate-target principle implies

```text
|I| >= 2.
```

Write

```text
I=z,J,
sum(J)=T-z.
```

Use the generic left splitting move:

```text
z,J,a,b,-a
   ->
z,a,b,J,-a.
```

This is exactly the GEN-L>=2 template from:

```text
docs/analytic_generic_interval_splitting_theorem.md
```

No separate duplicate-left algebra is needed, except for tracking which affine conditions are impossible because they duplicate local atoms.

---

## DUP-L failure routing

By GEN-L>=2, every failure routes to one of:

```text
1. affine/singleton obstruction;
2. proper prefix or proper internal subinterval obstruction inside J;
3. template-aware external cancellation;
4. impossible nonzero, duplicate-atom, Graham-validity, or boundary-sensitive condition.
```

In the duplicate-target case, some affine/singleton outputs collapse immediately to duplicate-atom contradictions. For example, if an affine branch forces

```text
z = a
```

and `a` already appears in the active local block, then this is impossible by distinctness of `S`.

Other affine branches route through singleton routing as usual.

Thus DUP-L creates no new obstruction type.

---

# DUP-R: duplicate right interval target

## Setup

Local form:

```text
a, b, -a, D
```

with

```text
sum(D)=T,
T in {a,b,-a}
```

or, more generally, `T` is already an atom in the active local block adjacent to `D`.

The duplicate-target principle implies

```text
|D| >= 2.
```

Write

```text
D=z,J,
sum(J)=T-z.
```

Use the generic right splitting move:

```text
a,b,-a,z,J
   ->
z,a,b,-a,J.
```

This is exactly the GEN-R>=2 template from:

```text
docs/analytic_generic_interval_splitting_theorem.md
```

---

## DUP-R failure routing

By GEN-R>=2, every failure routes to one of:

```text
1. affine/singleton obstruction;
2. proper prefix obstruction inside J;
3. template-aware external cancellation;
4. impossible nonzero, duplicate-atom, Graham-validity, or boundary-sensitive condition.
```

As in DUP-L, any affine branch forcing `z` to equal an already-used local atom is immediately impossible by distinctness of `S`.

Other affine/singleton branches route through the singleton-routing framework.

Thus DUP-R creates no new obstruction type.

---

## Application to T3

The T3 external routing note produced:

```text
E1 -> Left(a)
E4 -> Right(-a)
```

These are duplicate-target branches because `a` and `-a` already appear in the T3 active local block

```text
a,b,-a.
```

Therefore:

```text
E1 = DUP-L with target a.
E4 = DUP-R with target -a.
```

Length one is impossible in both branches.

Length at least two routes to GEN-L>=2 or GEN-R>=2 respectively.

---

## Duplicate Interval Target Theorem

### Statement

Any duplicate-target interval obstruction produced by the local templates satisfies:

```text
1. If the external interval has length one, contradiction by distinctness of S.
2. If the external interval has length at least two, the obstruction routes to the corresponding generic splitting template GEN-L>=2 or GEN-R>=2.
```

Consequently, duplicate-target interval states introduce no new obstruction class beyond:

```text
affine/singleton routing,
proper subinterval descent,
template-aware external cancellation,
impossible/boundary conditions.
```

### Proof

The length-one case would require a second copy of an atom already present in the local block. This contradicts the assumption that `S` is a set.

The length-at-least-two case is exactly the corresponding generic splitting template after writing the interval as first atom plus remainder:

```text
I=z,J
```

or

```text
D=z,J.
```

Then apply GEN-L>=2 or GEN-R>=2. ∎

---

## Significance

This note closes the duplicate interval dependency exposed by T3 routing.

T3 now depends only on:

```text
1. scalar absorption for b=2a;
2. GEN-L1 / GEN-R1 for nonduplicate length-one interval branches;
3. GEN-L>=2 / GEN-R>=2 for nonduplicate length-at-least-two branches;
4. DUP-L / DUP-R for duplicate branches.
```

All four dependencies now have durable notes except scalar absorption packaging.

---

## Remaining local packaging

Still needed:

```text
T4 mirror of T3:
  -b,a,b -> b,a,-b.

Scalar absorption theorem package:
  b=2a and mirror a=2b.
```

After those, the first-blocker local reductions are largely packaged, modulo global obstruction-tree termination.
