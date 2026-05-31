# Analytic Theorem Note: T1 External Cancellation Theorem

This note consolidates the template-aware external-cancellation analysis for the first clean blocker template.

Claim boundary:

```text
This is a local proof-module theorem, not a complete proof of Erdős 475.
The global obstruction-tree termination theorem remains open.
```

---

## Source notes consolidated here

This theorem note packages the following subcase files:

```text
docs/analytic_template_external_cancellation_t1.md
docs/analytic_template_external_cancellation_t1_lz_long.md
docs/analytic_template_external_cancellation_t1_rz_singleton.md
docs/analytic_template_external_cancellation_t1_rz_long_attempt.md
docs/analytic_template_bridge_routing_t1_rz.md
docs/analytic_template_external_cancellation_t1_lza_singleton.md
docs/analytic_template_external_cancellation_t1_lza_long.md
docs/analytic_template_external_cancellation_t1_rza_singleton.md
docs/analytic_template_external_cancellation_t1_rza_long.md
```

The purpose of this file is to give future agents a single reusable statement for T1.

---

## Parent template T1

T1 is the general right-blocker template with blocker length at least two.

Original local block:

```text
a,b,z,J
```

with

```text
sum(z,J) = -a,
sum(J) = -a-z.
```

The parent repair is

```text
a,b,z,J  ->  z,a,b,J.
```

The active block total is

```text
E=b.
```

Original relative partial sums:

```text
a,
a+b,
a+b+z,
a+b+z+Y_s,
...,
b.
```

New relative partial sums:

```text
z,
z+a,
z+a+b,
z+a+b+Y_s,
...,
b.
```

The only genuinely new relative partial sums are

```text
z,
z+a.
```

The parent move removes the original forbidden relative value `a` unless internal obstruction occurs.

Known parent internal failures:

```text
Affine/singleton:
  z = a+b,
  z = b-a.

Proper prefix in J:
  Y_s = -a-b,
  Y_s = a-b.

Impossible:
  z=a,
  z=b,
  z=0,
  z=-a with nonempty J.
```

External failures occur only at the new values

```text
W=z,
W=z+a.
```

---

## External-collision normal form used

Let the proposed permutation be split as

```text
pi(H)=A,B
```

with

```text
sum(A)=W,
sum(B)=E-W.
```

A left external collision gives a real interval `K` immediately left of the active block such that

```text
sum(K)+sum(A)=0.
```

A right external collision gives a real interval `K` immediately right of the active block such that

```text
sum(B)+sum(K)=0.
```

This template-aware form is essential. Bare `Left(T)` / `Right(T)` notation is not sufficient for proof.

---

## T1 external branches

There are four top-level external branches:

```text
T1-Lz:
  left external collision at W=z.

T1-Rz:
  right external collision at W=z.

T1-Lza:
  left external collision at W=z+a.

T1-Rza:
  right external collision at W=z+a.
```

Each splits into singleton and long canceling-interval cases.

---

## Branch T1-Lz

At `W=z`, the proposed split is

```text
A=z,
B=a,b,J.
```

Left external collision gives

```text
sum(K)=-z.
```

### Singleton case

If

```text
K=(-z),
```

use

```text
-z,a,b,z,J  ->  z,a,b,-z,J.
```

Failures reduce to:

```text
affine/singleton conditions,
proper prefixes inside J,
further external cancellation,
impossible conditions.
```

### Long case

If

```text
K=K',y,
sum(K')=-z-y,
```

use

```text
K',y,a,b,z,J  ->  K',z,a,b,y,J.
```

Failures reduce to:

```text
affine/singleton in y,
proper prefixes inside J,
proper suffixes inside K',
further external cancellation,
impossible or boundary-sensitive conditions.
```

Conclusion:

```text
T1-Lz is fully reduced to the standard local menu.
```

---

## Branch T1-Rz

At `W=z`, the proposed split is

```text
A=z,
B=a,b,J.
```

Since

```text
sum(B)=b-z,
```

right external collision gives

```text
sum(K)=z-b.
```

### Singleton case

If

```text
K=(z-b),
```

use

```text
a,b,z,J,z-b  ->  z-b,a,b,z,J.
```

Failures reduce to:

```text
affine/singleton,
proper prefix inside J,
proper internal subinterval inside J,
further external cancellation,
impossible or boundary-sensitive conditions.
```

### Long case

If

```text
K=y,K',
sum(K')=z-b-y,
```

try

```text
a,b,z,J,y,K'  ->  y,a,b,z,J,K'.
```

Most failures reduce as expected, but a cross-prefix bridge can occur:

```text
U_t - Y_s = a+z,
```

where `Y_s` is a prefix of `J` and `U_t` is a prefix of `K'`.

This bridge is equivalent to

```text
sum(J_s^+) + sum(K_t^-)=0,
```

where:

```text
J_s^+ = suffix of J after prefix Y_s,
K_t^- = prefix of K' with sum U_t.
```

The bridge appears in the original ordering as

```text
J_s^+, y, K_t^-.
```

Its enclosing span is strictly smaller than the full parent block

```text
a,b,z,J,y,K'.
```

Therefore T1-Rz-long routes to the bridge/gap framework rather than creating a terminal obstruction.

Conclusion:

```text
T1-Rz is reduced to the standard local menu plus smaller-enclosure bridge/gap state.
```

---

## Branch T1-Lza

At `W=z+a`, the proposed split is

```text
A=z,a,
B=b,J.
```

Left external collision gives

```text
sum(K)=-z-a.
```

### Singleton case

If

```text
K=(-z-a),
```

use

```text
-z-a,a,b,z,J  ->  z,a,b,-z-a,J.
```

Failures reduce to:

```text
affine/singleton,
proper prefix inside J,
further external cancellation,
impossible or boundary-sensitive conditions.
```

### Long case

If

```text
K=K',y,
sum(K')=-z-a-y,
```

use

```text
K',y,a,b,z,J  ->  K',z,a,b,y,J.
```

Failures reduce to:

```text
affine/singleton in y,
proper prefix inside J,
proper suffix inside K',
further external cancellation,
impossible or boundary-sensitive conditions.
```

Conclusion:

```text
T1-Lza is fully reduced to the standard local menu.
```

---

## Branch T1-Rza

At `W=z+a`, the proposed split is

```text
A=z,a,
B=b,J.
```

Since

```text
sum(B)=b-a-z,
```

right external collision gives

```text
sum(K)=z+a-b.
```

### Singleton case

If

```text
K=(z+a-b),
```

use

```text
a,b,z,J,z+a-b  ->  z+a-b,a,b,z,J.
```

Failures reduce to:

```text
affine/singleton,
proper prefix inside J,
proper internal subinterval inside J,
further external cancellation,
impossible or boundary-sensitive conditions.
```

### Long case

If

```text
K=y,K',
sum(K')=z+a-b-y,
```

use

```text
a,b,z,J,y,K'  ->  y,a,b,z,J,K'.
```

Again, the bridge relation appears:

```text
U_t - Y_s = a+z.
```

As above, this is equivalent to the separated zero-bridge

```text
sum(J_s^+) + sum(K_t^-)=0.
```

The bridge support lies inside

```text
J_s^+, y, K_t^-,
```

with strictly smaller enclosing span than the full parent block

```text
a,b,z,J,y,K'.
```

Conclusion:

```text
T1-Rza is reduced to the standard local menu plus smaller-enclosure bridge/gap state.
```

---

## T1 External Cancellation Theorem

### Statement

For the T1 parent move

```text
a,b,z,J  ->  z,a,b,J,
```

with

```text
sum(J)=-a-z,
```

every internal or external failure of the move is routed to one of the following:

```text
1. affine/singleton obstruction;
2. proper prefix, suffix, or internal subinterval obstruction;
3. further template-aware external cancellation;
4. separated zero-bridge with strictly smaller enclosing span;
5. impossible nonzero, duplicate-atom, Graham-validity, or boundary-sensitive zero condition.
```

In particular, no T1 external child creates an unclassified obstruction type.

### Proof

Internal failures are classified directly from the two genuinely new parent values `z` and `z+a`.

External failures split into the four top-level branches:

```text
T1-Lz,
T1-Rz,
T1-Lza,
T1-Rza.
```

Each branch is handled by its singleton and long canceling-interval analyses listed above.

The two long right-collision branches produce the same bridge relation

```text
U_t - Y_s = a+z,
```

which is routed to the bridge/gap framework as a separated zero-bridge of strictly smaller enclosing span.

Therefore the theorem follows from the subcase notes. ∎

---

## Significant status

This is the first complete template module under the corrected template-aware framework.

It handles the general right-blocker length-at-least-two template from the first forbidden-hit adjacent swap.

This is meaningful progress, but it is not the whole proof.

---

## Remaining proof obligations after T1

### Local template obligations

Need analogous packaging for at least:

```text
T2: general left blocker, length >= 2
    J,z,a,b -> J,a,b,z.

T3: right singleton blocker
    a,b,-a -> -a,b,a.

T4: left singleton blocker
    -b,a,b -> b,a,-b.

Scalar absorption templates.
```

T2 should be mostly symmetric to T1, but it must still be written carefully because the prefix/suffix orientation reverses.

### Global obligations

Need to integrate:

```text
standard local descent,
further external cancellation,
smaller-enclosure bridge/gap states,
boundary-sensitive zero cases,
affine/singleton routing
```

into a single well-founded obstruction-tree termination theorem.

Until that theorem is proved, the analytic proof remains incomplete.
