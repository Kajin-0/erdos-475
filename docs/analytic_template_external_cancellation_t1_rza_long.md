# Analytic Note: T1 Right External Cancellation at W=z+a, Long K

This note continues the template-aware external cancellation program.

Claim boundary:

```text
This is a partial analytic reduction note. It is not a complete proof of Erdős 475.
```

---

## Parent template T1

Parent template:

```text
a,b,z,J  ->  z,a,b,J
```

with

```text
sum(z,J) = -a,
sum(J) = -a-z.
```

The parent move has genuinely new values

```text
z,
z+a.
```

This note treats the right external collision at

```text
W = z+a
```

when the right canceling interval has length at least two.

---

## External collision normal form at W=z+a

At `W=z+a`, the proposed permutation splits as

```text
pi(H) = A,B = (z,a), (b,J).
```

The suffix has sum

```text
sum(B) = b+sum(J) = b-a-z.
```

A right external collision gives an interval `K` immediately right of the active block with

```text
sum(B)+sum(K)=0.
```

Thus

```text
sum(K)=z+a-b.
```

The singleton case `K=(z+a-b)` is handled in:

```text
docs/analytic_template_external_cancellation_t1_rza_singleton.md
```

Now assume

```text
|K| >= 2.
```

Write

```text
K = y,K'
```

where `y` is adjacent to the original active block. Then

```text
sum(K') = z+a-b-y.
```

The original combined block is

```text
a,b,z,J,y,K'.
```

The original forbidden relative value is still

```text
a.
```

The total of the combined block is

```text
a+b+z+sum(J)+y+sum(K')
= a+b+z-a-z+y+z+a-b-y
= z+a.
```

---

## Candidate repair

Use the right-long analogue of the singleton move:

```text
a,b,z,J,y,K'
   ->
y,a,b,z,J,K'.
```

The total is preserved:

```text
y+a+b+z+sum(J)+sum(K')
= y+a+b+z-a-z+z+a-b-y
= z+a.
```

The new relative partial sums are

```text
y,
y+a,
y+a+b,
y+a+b+z,
y+a+b+z+Y_s,
...,
y+b,
y+b+U_t,
...,
z+a,
```

where:

```text
Y_s = proper prefix sums of J,
U_t = proper prefix sums of K'.
```

The values

```text
y+b,
y+b+U_t,
...,
z+a
```

already occurred in the original block after the old prefix through `J,y,K'`.

Therefore the new fixed values are

```text
y,
y+a,
y+a+b,
y+a+b+z,
```

and the new J-prefix family is

```text
y+a+b+z+Y_s.
```

---

## Forbidden-value hits

Forbidden relative value:

```text
F = a.
```

The new fixed values hit `F` only if

```text
y = a              -> duplicate atom a,
y+a = a            -> y=0,
y+a+b = a          -> y=-b,
y+a+b+z = a        -> y=-b-z.
```

The first two are impossible by distinctness/nonzero. The latter two are affine/singleton conditions.

The J-prefix family hits `F` if

```text
y+a+b+z+Y_s = a
```

so

```text
Y_s = -y-b-z.
```

This is a proper-prefix obstruction inside `J`.

---

## Zero-hit checks

The new fixed values hit zero only if

```text
y = 0,
y = -a,
y = -a-b,
y = -a-b-z.
```

The first is impossible. The other three are affine/singleton or boundary-sensitive zero conditions.

The J-prefix family hits zero if

```text
y+a+b+z+Y_s = 0
```

so

```text
Y_s = -a-b-z-y.
```

This is a proper-prefix obstruction inside `J`.

---

## Fixed internal collisions

Among the fixed new values

```text
y,
y+a,
y+a+b,
y+a+b+z
```

collisions force one of

```text
a=0,
b=0,
z=0,
a+b=0,
b+z=0,
a+b+z=0.
```

The first three are impossible. The remaining cases are affine/degenerate or boundary-sensitive conditions:

```text
a+b=0,
z=-b,
z=-a-b.
```

As in earlier notes, `a+b=0` is not silently discarded because relative zero is boundary-sensitive.

---

## Proper-prefix reductions inside J

Collisions between the J-prefix family

```text
y+a+b+z+Y_s
```

and the fixed new values give:

```text
y+a+b+z+Y_s = y              -> Y_s=-a-b-z,
y+a+b+z+Y_s = y+a            -> Y_s=-b-z,
y+a+b+z+Y_s = y+a+b          -> Y_s=-z,
y+a+b+z+Y_s = y+a+b+z        -> Y_s=0.
```

The case `Y_s=0` contradicts Graham-validity for a nonempty proper prefix of `J`.

Thus proper-prefix obstructions inside `J` include

```text
Y_s in {
  -y-b-z,
  -a-b-z-y,
  -a-b-z,
  -b-z,
  -z
}.
```

The first two come from forbidden/zero hits, and the last three from collisions with fixed new values.

---

## New bridge obstruction: cross-prefix relation between J and K'

The main nontrivial issue is the collision between the new J-prefix family and the old K'-tail values.

Old K'-tail values have form

```text
y+b+U_t,
```

where `U_t` is a proper prefix sum of `K'`.

A collision

```text
y+a+b+z+Y_s = y+b+U_t
```

gives

```text
U_t - Y_s = a+z.
```

This is exactly the same bridge relation discovered in `T1-Rz-long`.

It is not a simple one-interval prefix/suffix obstruction. It relates a prefix of `J` to a prefix of `K'`.

---

## Bridge routing

As in `docs/analytic_template_bridge_routing_t1_rz.md`, define:

```text
J_s^+ = suffix of J after prefix Y_s,
K_t^- = prefix of K' with sum U_t.
```

Then

```text
sum(J_s^+) = sum(J) - Y_s = -a-z-Y_s.
```

Using the bridge equation

```text
U_t - Y_s = a+z,
```

we get

```text
sum(J_s^+) + sum(K_t^-)
= (-a-z-Y_s)+U_t
= 0.
```

Thus the cross-prefix collision is equivalent to the separated zero-bridge

```text
sum(J_s^+) + sum(K_t^-) = 0.
```

In the original ordering these two pieces occur as

```text
J_s^+, y, K_t^-.
```

So this is a separated zero-bridge with single-atom gap `y` and strictly smaller enclosure than the full parent block

```text
a,b,z,J,y,K'.
```

It should be routed into the bridge/gap framework rather than treated as a terminal obstruction.

---

## Full reduction statement

### Lemma T1-Rza-long

In template T1, suppose the right external collision at `W=z+a` has a canceling interval

```text
K = y,K'
```

with length at least two and

```text
sum(K)=z+a-b.
```

Then the move

```text
a,b,z,J,y,K'
   ->
y,a,b,z,J,K'
```

is total-preserving and removes the forbidden relative value `a` unless one of the listed affine or boundary-sensitive conditions occurs.

If it does not produce a valid endpoint-avoiding local repair, every failure is one of:

```text
1. affine/singleton obstruction involving y,z,a,b;
2. proper-prefix obstruction inside J;
3. separated zero-bridge between a suffix of J and a prefix of K';
4. further external cancellation involving one of the new values;
5. impossible nonzero, duplicate-atom, Graham-validity, or boundary-sensitive zero condition.
```

The bridge case has smaller enclosing span than the full parent repair block and is routed to the bridge/gap framework.

---

## Consequence for T1

All top-level external-child branches for template T1 have now been analyzed:

```text
T1-Lz-1,
T1-Lz-long,
T1-Rz-1,
T1-Rz-long,
T1-Lza-1,
T1-Lza-long,
T1-Rza-1,
T1-Rza-long.
```

The unresolved part is no longer a missing T1 branch. It is global integration:

```text
How to combine the standard finite menu plus bridge/gap routing into a well-founded obstruction-tree termination theorem.
```

---

## Significant-result status

This completes the template-aware external-cancellation map for T1, modulo global bridge/gap termination integration.

Template T1 now supports the desired local conclusion:

```text
Every external child of a,b,z,J -> z,a,b,J reduces to:
  success,
  affine/singleton,
  proper subinterval/prefix/suffix obstruction,
  bridge/gap state of smaller enclosure,
  further external cancellation,
  impossible/boundary condition.
```

This is a meaningful proof-module milestone, but still not a complete proof.
