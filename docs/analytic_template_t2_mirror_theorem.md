# Analytic Theorem Note: T2 Mirror Reduction from T1

This note continues from:

```text
docs/analytic_template_t1_external_cancellation_theorem.md
```

Claim boundary:

```text
This is a local template-reduction theorem note, not a complete proof of Erdős 475.
The global obstruction-tree termination theorem remains open.
```

---

## Purpose

T2 is the general left-blocker template with blocker length at least two.

Rather than redo all eight external-cancellation subcases, this note records the mirror symmetry reducing T2 to the completed T1 external-cancellation theorem.

---

## T2 parent template

The T2 local block is

```text
J,z,a,b
```

with

```text
sum(J,z) = -b,
sum(J) = -b-z.
```

The parent move is

```text
J,z,a,b  ->  J,a,b,z.
```

This was derived from the general left-blocker length-at-least-two case.

The original forbidden relative value is

```text
a-b.
```

The genuinely new values after the unchanged prefix `J` are

```text
A = a-b-z,
B = a-z.
```

Known parent failures:

```text
Affine/singleton:
  z = a-b.

Proper suffix inside J:
  suffix(J) = -a,
  suffix(J) = -a-b.

External collisions involving:
  a-b-z,
  a-z.
```

---

## Mirror transformation

Define the reversal of an interval sequence by writing it in opposite order.

Apply reversal to the T2 parent move:

```text
J,z,a,b  ->  J,a,b,z
```

Reversed original block:

```text
b,a,z,J^R
```

Reversed proposed block:

```text
z,b,a,J^R
```

where `J^R` is `J` in reverse order.

Now relabel T1 variables by

```text
a_T1 = b,
b_T1 = a,
z_T1 = z,
J_T1 = J^R.
```

Then

```text
sum(J_T1) = sum(J) = -b-z = -a_T1-z_T1.
```

So the reversed T2 template is exactly the T1 parent template:

```text
a_T1,b_T1,z_T1,J_T1  ->  z_T1,a_T1,b_T1,J_T1.
```

Thus T2 is the mirror-dual of T1.

---

## Effect on obstruction classes

Under reversal:

```text
left external collision  <->  right external collision,
right external collision <->  left external collision,
prefix obstruction       <->  suffix obstruction,
proper internal subinterval obstruction stays internal,
bridge/gap state         stays bridge/gap state,
affine/singleton         stays affine/singleton,
impossible condition     stays impossible,
boundary-sensitive zero  stays boundary-sensitive zero.
```

The enclosing span of a bridge/gap state is invariant under reversal, and strict decrease of enclosing span is preserved.

Therefore every T1 conclusion transfers to T2.

---

## T2 External Cancellation Theorem

### Statement

For the T2 parent move

```text
J,z,a,b  ->  J,a,b,z,
```

with

```text
sum(J)=-b-z,
```

every internal or external failure of the move is routed to one of the following:

```text
1. affine/singleton obstruction;
2. proper prefix, suffix, or internal subinterval obstruction;
3. further template-aware external cancellation;
4. separated zero-bridge with strictly smaller enclosing span;
5. impossible nonzero, duplicate-atom, Graham-validity, or boundary-sensitive zero condition.
```

In particular, no T2 external child creates an unclassified obstruction type, provided the T1 theorem is accepted.

### Proof

Reverse the T2 active block and relabel

```text
a_T1=b,
b_T1=a,
z_T1=z,
J_T1=J^R.
```

The reversed T2 move becomes the T1 move

```text
a_T1,b_T1,z_T1,J_T1  ->  z_T1,a_T1,b_T1,J_T1.
```

By `docs/analytic_template_t1_external_cancellation_theorem.md`, all T1 failures route to the finite controlled menu:

```text
affine/singleton,
proper subinterval obstruction,
further external cancellation,
smaller-enclosure bridge/gap state,
impossible/boundary condition.
```

Reversing back preserves this classification, exchanging left/right and prefix/suffix as described above.

Therefore the T2 theorem follows. ∎

---

## Significance

This avoids duplicating the eight-subcase T1 analysis for the mirror template.

Together, T1 and T2 now cover the length-at-least-two first-blocker reductions:

```text
T1: right blocker, |D|>=2
    a,b,z,J -> z,a,b,J.

T2: left blocker, |L|>=2
    J,z,a,b -> J,a,b,z.
```

Both templates reduce to the controlled local menu plus bridge/gap routing.

---

## Remaining local templates

Still to package or verify:

```text
T3: right singleton blocker
    a,b,-a -> -a,b,a.

T4: left singleton blocker
    -b,a,b -> b,a,-b.

Scalar absorption templates:
    b=2a and mirror a=2b.
```

The singleton templates produce more scalar/finite affine branches and need careful boundary handling.

---

## Global obligations still open

Even with T1 and T2 locally controlled, the full proof still requires:

```text
1. a precise global obstruction-tree state definition;
2. a well-founded measure incorporating:
   - local support/enclosing span,
   - bridge/gap span,
   - proper subinterval descent,
   - external-cancellation recurrence depth,
   - boundary-sensitive zero cases;
3. affine/singleton routing into length-one templates;
4. scalar absorption routing;
5. final conditional endpoint-avoidance theorem.
```

This note is a local module, not the global termination theorem.
