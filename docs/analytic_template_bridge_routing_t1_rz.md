# Analytic Note: Routing the T1-Rz-long Bridge Obstruction

This note follows:

```text
docs/analytic_template_external_cancellation_t1_rz_long_attempt.md
```

and connects the newly exposed bridge obstruction to the existing bridge/gap framework in:

```text
docs/final/F08_bridge_gap_descent_theorem.md
docs/analytic_bridge_gap_measure_hardening_a98.md
```

Claim boundary:

```text
This note does not prove Erdős 475.
It routes one newly exposed obstruction into an existing bridge/gap framework.
The final bridge/gap termination theorem still needs line-by-line integration.
```

---

## Parent situation: T1-Rz-long

Parent template:

```text
a,b,z,J  ->  z,a,b,J
```

with

```text
sum(J) = -a-z.
```

Right external collision at `W=z` gives a right interval

```text
K = y,K'
```

with

```text
sum(K) = z-b,
sum(K') = z-b-y.
```

The attempted long-cancellation repair was

```text
a,b,z,J,y,K'
   ->
y,a,b,z,J,K'.
```

The cross-prefix collision found in the attempt is:

```text
U_t - Y_s = a+z,
```

where:

```text
Y_s = prefix sum of J,
U_t = prefix sum of K'.
```

This was identified as a bridge obstruction rather than a simple prefix obstruction.

---

## Convert the bridge equation to a two-piece zero relation

Let

```text
J_s^+ = suffix of J after prefix Y_s.
```

Then

```text
sum(J_s^+) = sum(J) - Y_s = -a-z-Y_s.
```

Let

```text
K_t^- = prefix of K' with sum U_t.
```

The bridge equation

```text
U_t - Y_s = a+z
```

implies

```text
sum(J_s^+) + sum(K_t^-)
= (-a-z-Y_s) + U_t
= -a-z + (U_t-Y_s)
= -a-z + (a+z)
= 0.
```

Therefore the bridge obstruction is exactly a two-piece zero-composite:

```text
sum(J_s^+) + sum(K_t^-) = 0.
```

In the original ordering, these two pieces are separated by the atom `y`:

```text
J_s^+ , y , K_t^-.
```

Equivalently, the contiguous interval

```text
J_s^+ , y , K_t^-
```

has sum

```text
y.
```

So this is a separated zero-bridge around the single-atom gap `y`.

---

## Relation to existing F8/A98 bridge framework

The existing bridge/gap framework allows bridge relations of the form

```text
B_ext + U = 0
```

and signed variants. The T1-Rz-long bridge is exactly this with

```text
B_ext = K_t^-,
U = J_s^+.
```

The gap is

```text
G = y.
```

So the branch has the separated form

```text
U, G, B_ext
```

with

```text
sum(U)+sum(B_ext)=0.
```

This is a signed separated bridge relation.

---

## Measure comparison

The full T1-Rz-long active block was

```text
a,b,z,J,y,K'.
```

The bridge support is contained in

```text
J_s^+, y, K_t^-.
```

This excludes the leading atoms

```text
a,b,z
```

and may also exclude an initial prefix of `J` and a terminal suffix of `K'`.

Therefore the bridge enclosure is strictly smaller than the full active block enclosure:

```text
Enc(J_s^+, y, K_t^-)
  proper subset of
Enc(a,b,z,J,y,K')
```

provided the parent active block is the full support used for the T1-Rz-long repair.

Thus the bridge obstruction is not an equal-complexity recurrence of the whole T1-Rz-long state. It descends to a bridge/gap state with smaller enclosing span relative to the parent repair attempt.

---

## Result: T1-Rz-long bridge routing lemma

### Lemma

In the T1-Rz-long attempted repair

```text
a,b,z,J,y,K'
   ->
y,a,b,z,J,K',
```

the cross-prefix collision

```text
U_t - Y_s = a+z
```

is equivalent to the separated zero-bridge

```text
sum(J_s^+) + sum(K_t^-) = 0,
```

where `J_s^+` is a suffix of `J` and `K_t^-` is a prefix of `K'`.

The participating bridge support lies inside

```text
J_s^+, y, K_t^-,
```

which has strictly smaller enclosing span than the full parent block

```text
a,b,z,J,y,K'.
```

Therefore this bridge collision should be routed into the existing bridge/gap descent framework rather than treated as a terminal obstruction.

---

## Significance

This upgrades the previous negative result:

```text
T1-Rz-long is not closed by simple prefix/suffix descent.
```

to a routed statement:

```text
The new bridge obstruction is a separated zero-bridge of strictly smaller enclosure.
```

This strongly suggests that the corrected template-aware proof can still be viable if the existing bridge/gap descent theorem is integrated carefully.

---

## Remaining obligations

This note does not close all of T1-Rz-long by itself.

Remaining obligations:

```text
1. Verify all non-bridge failures in T1-Rz-long are covered by:
   affine/singleton,
   proper prefix,
   proper subinterval,
   external cancellation,
   impossible condition.

2. Integrate this bridge routing into the global obstruction-tree measure.

3. Ensure the bridge/gap framework handles signed zero-bridges with single-atom gaps exactly as used here.

4. Update the final termination theorem so that bridge/gap descent is an allowed child type.
```

---

## Updated T1-Rz-long status

Before this note:

```text
T1-Rz-long exposed a bridge obstruction and was not closed.
```

After this note:

```text
The bridge obstruction is identified as a smaller-enclosure separated zero-bridge.
```

This is a significant partial closure, but still requires integration with the bridge/gap descent machinery.
