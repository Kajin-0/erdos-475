# S61. Assembled hidden-support extraction proof

This note assembles S55-S60 into a single proof-ready draft of Lemma A.

## Lemma A. Hidden-support extraction

### Statement

Work in `Z/pZ`.  Let `R` be an `m=3` right-terminal pure worse-only residual with normal form

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0,
D_short(R) = (1,3,1,[2]).
```

Consider the local permutation

```text
A z q B -> B z q A,
```

so that the moved order is

```text
R' = X B z q A Y.
```

Then `R'` contains at least one hidden-support zero interval whose reduced equation is one of:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

Equivalently, before algebraic reduction, the relevant zero interval has one of the forms:

```text
B_tail + z + q = 0,
B_tail + z + q + A_i + Y_prefix = 0,
B_tail + z + q + A1 + A2 + Y_prefix = 0.
```

## Proof

### Step 1. Endpoint-zone decomposition

In the moved order

```text
R' = X B z q A Y,
```

any zero interval has endpoints in the ordered zones

```text
X | B | z | q | A | Y.
```

We classify zero intervals by which zones their endpoints cross.

The old terminal relations are:

```text
A1 + A2 + z = 0,                    (A-z relation)
sum(B) + z = 0.                     (B-z relation)
```

The moved order contains the contiguous block

```text
B z,
```

so the full block `B+z=0` is always present.  This is tautological and not a new obstruction.

### Step 2. Intervals contained in `B z`

If a zero interval is contained in `B z`, then by E1 it is either the full terminal tautology

```text
B + z = 0,
```

or it implies a proper support zero relation inside `B`.

Indeed, writing

```text
B = b1 b2 ... bs,
b1 + ... + bs + z = 0,
```

a proper interval inside `B z` is either

```text
b_i + ... + b_j = 0
```

or

```text
b_i + ... + b_s + z = 0,    i > 1.
```

In the second case, subtracting from the full terminal equation gives

```text
b1 + ... + b_{i-1} = 0.
```

Thus every proper contained interval gives a support sub-block zero relation.  Such a relation is a prior support/terminal branch, excluded from the unresolved pure worse-only residual.

Therefore the only `B z`-contained interval remaining in the pure branch is the tautology

```text
B + z = 0.
```

### Step 3. Exterior-crossing intervals

Suppose a zero interval has one endpoint in an exterior zone, e.g. in `X` or in an exterior part of `Y`, and is not one of the target hidden-support forms.

A zero interval is equivalent to a repeated partial sum:

```text
P_i = P_j.
```

If one endpoint is exterior and the other lies in or across the active window, then this equality has the form

```text
P_ext = P_active.
```

By E2, this is exactly an external bridge relation.  Depending on the side and multiplicity, it routes to one of:

```text
EXTERNAL_BRIDGE,
LEFT_TERMINAL_BRIDGE,
RIGHT_TERMINAL_BRIDGE,
MIXED_TERMINAL_BRIDGE,
DISTRIBUTED_BRIDGE.
```

By E4, pure worse-only residuals exclude already-routed external bridge cases.  Therefore exterior non-target intervals do not form unresolved endpoint cases.

If an exterior interval coexists with a target hidden-support interval, the extraction lemma simply uses the target interval.  This is precisely what occurred in the two documented p=23 left-external cases.

### Step 4. Local active-window non-target intervals

Now suppose the zero interval lies locally inside the active zones

```text
B | z | q | A,
```

but is neither the terminal tautology `B+z=0` nor a target hidden-support crossing interval.

By E3, such a local interval creates a repeated local partial-sum pair that routes to one of:

```text
SIGNED_INTERVAL,
DISTRIBUTED_BRIDGE,
PAIR_TRAP,
support-tail trap,
Bq/BqY routed branch.
```

These are already-routed local mechanisms.  By E4, they are excluded from the unresolved pure worse-only residual.

Thus, after removing:

```text
1. the terminal tautology B+z=0;
2. exterior bridge intervals;
3. local signed/support/distributed intervals;
```

the only remaining useful active-window zero intervals must cross the separator

```text
z q
```

from a suffix of `B` into `A` and possibly a prefix of `Y`.

### Step 5. Remaining crossing forms

The remaining interval must begin in a suffix of `B`, pass through `z q`, and then terminate either:

```text
before A,
after one A element,
after both A elements,
after both A elements plus a prefix of Y.
```

Therefore it has one of the following forms:

```text
B_tail + z + q = 0,                                      (1)
B_tail + z + q + A_i + Y_prefix = 0,                     (2)
B_tail + z + q + A1 + A2 + Y_prefix = 0.                 (3)
```

These are exactly the hidden-support endpoint classes:

```text
hidden_prefix_core,
hidden_partial_A_tail_core,
hidden_full_A_tail_core.
```

### Step 6. Algebraic reduction

#### Case (1): prefix-core

If

```text
B_tail + z + q = 0,
```

and

```text
B_prefix + B_tail + z = 0,
```

then subtracting gives

```text
B_prefix = q.
```

This is the prefix equality family.

#### Case (2): partial-A tail-core

If

```text
B_tail + z + q + A_i + Y_prefix = 0,
```

and `{i,j}={1,2}`, then from

```text
A_i + A_j + z = 0
```

we get

```text
z + A_i = -A_j.
```

Substitution yields

```text
B_tail + q + Y_prefix = A_j.
```

When `Y_prefix` is empty this becomes

```text
B_tail + q = A_complement.
```

This is the equality family.

#### Case (3): full-A tail-core

If

```text
B_tail + z + q + A1 + A2 + Y_prefix = 0,
```

and

```text
A1 + A2 + z = 0,
```

then

```text
B_tail + q + Y_prefix = 0.
```

When `Y_prefix` is empty this becomes

```text
B_tail + q = 0.
```

This is the zero-sum family.

## Conclusion

Every unresolved non-tautological endpoint case in the pure worse-only branch exposes one of the four reduced hidden-support families:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

This proves the hidden-support extraction lemma, modulo the branch-exclusion lemmas E1-E4.

## Certificate support

The endpoint taxonomy confirms the shape of the proof in the certified data:

```text
p=17: target hidden-support interval present in 35/35 records.
p=23: target hidden-support interval present in 59/59 records.
```

The only non-target interval classes observed were:

```text
tautology_terminal_zB,
left_external_X.
```

The first is handled by E1.  The second is handled by E2 and, in the two observed cases, coexists with a valid hidden-support target interval.

## Consequence for the pure worse-only branch

Combining Lemma A with the v4 certificate table gives:

```text
zero-sum extraction families:
  B_tail+q              -> Bq_zero  -> routed
  B_tail+q+Y_prefix     -> BqY_zero -> routed

equality extraction families:
  B_tail+q=A_complement -> q_tail_span_gap decreases
  B_prefix=q            -> q_tail_span_gap decreases
```

Thus, at the proof-skeleton level, the pure worse-only `m=3` branch is reduced to previously routed mechanisms plus the refined equality tie-break.

## Remaining work

For a final publication-grade proof, the following definitions must be fixed:

```text
1. precise definition of pure worse-only residual;
2. precise definition of support-minimality for B;
3. precise definition of the already-routed branch vocabulary;
4. formal proof that E2 and E3 route to those branches in the chosen proof system;
5. formal proof of the q_tail_span_gap tie-break for equality families.
```

## Status

```text
Lemma A assembled as a standalone proof draft.
Next target: formalize the equality tie-break lemma using S_tail = span_gap({q} union B_tail).
```
