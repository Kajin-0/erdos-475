# S55. Endpoint-zone enumeration proof draft

This note begins the non-computational proof of Lemma A from S54.

## Objective

Replace the empirical statement

```text
B z q A exposes one of the hidden-support interval classes
```

with a deterministic endpoint-zone enumeration argument.

## Setup

Work in the cyclic group `Z/pZ`.  The hard residual has normal form

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0.
```

The branch is `m=3` right-terminal and pure worse-only, with

```text
D_short(R) = (1,3,1,[2]).
```

Consider the moved order

```text
R' = X B z q A Y.
```

Write

```text
B = B_prefix B_tail,
Y = Y_prefix Y_suffix.
```

A zero interval in `R'` is a contiguous block whose sum is zero.  Its endpoints lie in the ordered zones

```text
X | B | z | q | A | Y.
```

## Fundamental old relations

The original terminal relations are:

```text
A1 + A2 + z = 0,                         (A-z relation)
sum(B) + z = 0.                          (B-z relation)
```

The moved order `X B z q A Y` contains the contiguous block

```text
B z,
```

so the whole block `B+z` is always a zero interval.  This is the class

```text
tautology_terminal_zB.
```

It is not a new obstruction and should be ignored for hidden-support extraction.

## Interval-zone taxonomy

Let `I` be a zero interval in `R' = X B z q A Y`.

### Case 1. `I` is contained in `B z`

Then `I` is either the full terminal block

```text
B + z = 0,
```

or a proper sub-block of `B z`.

In the pure minimal residual setting, a proper sub-block of `B z` would create a shorter support-terminal zero interval or an internal support collision.  Such a case routes to an earlier terminal/support branch and is excluded from the pure worse-only residual.

Thus the only allowed contained-in-`B z` interval is the tautological full `B+z` relation.

### Case 2. `I` is contained in `z q A`

A zero interval inside `z q A` can be one of:

```text
z,
z q,
z q A1,
z q A1 A2,
q,
q A1,
q A1 A2,
A1,
A1 A2,
A2.
```

The only old tautological `A`-relation is

```text
A1 + A2 + z = 0.
```

In the moved order `z q A1 A2`, the block `z A1 A2` is not contiguous because `q` separates `z` from `A`.  Therefore a zero interval wholly inside `z q A` would either involve `q` or be a proper `A`-subblock.

Such a zero interval would be a shorter local relation involving `q` or part of `A`, giving an immediate signed/support collision.  In a pure worse-only residual, these are routed to earlier local branches, not to the hidden-support branch.

Therefore the hidden-support extraction focuses on intervals that begin in a suffix of `B`, cross `z q`, and terminate in `A` and possibly a prefix of `Y`.

### Case 3. `I` crosses from `B` through `z q`

This is the essential case.  Since the zones are ordered as

```text
B | z | q | A | Y,
```

any such interval has the form

```text
B_tail + z + q + A_prefix + Y_prefix = 0,
```

where

```text
A_prefix in {empty, A1, A1 A2}.
```

Thus there are three subcases.

#### Case 3a. `A_prefix` is empty

Then

```text
B_tail + z + q = 0.
```

Using

```text
B_prefix + B_tail + z = 0,
```

we obtain

```text
B_prefix = q.
```

This is the hidden prefix equality family.

#### Case 3b. `A_prefix = A_i`

In the moved order the prefix of `A` is normally `A1`, but the symbolic classification allows the partial-A case abstractly as `A_i` because the local normal form may be viewed after canonical or mirrored labeling.

Then

```text
B_tail + z + q + A_i + Y_prefix = 0.
```

Since

```text
z + A_i = -A_j,
```

where `{i,j}={1,2}`, this reduces to

```text
B_tail + q + Y_prefix = A_j.
```

If `Y_prefix` is empty:

```text
B_tail + q = A_complement.
```

This is the hidden equality family.

#### Case 3c. `A_prefix = A1 A2`

Then

```text
B_tail + z + q + A1 + A2 + Y_prefix = 0.
```

Using

```text
A1 + A2 + z = 0,
```

we get

```text
B_tail + q + Y_prefix = 0.
```

If `Y_prefix` is empty:

```text
B_tail + q = 0.
```

This is the hidden zero-sum family.

### Case 4. `I` begins in `X`

Then `I` has form

```text
X_suffix + B_prefix_or_more + ... = 0.
```

This is an exterior/cross-window interval.  It is not a hidden-support extraction interval.  It routes to an external bridge branch or is irrelevant if a target interval also exists.

The endpoint taxonomy found exactly two such cases in the certified p=23 data, records 183 and 449.  Both also contain a valid `hidden_full_A_tail_core` interval, so they do not obstruct the existence lemma.

Formal treatment:

```text
If an X-crossing zero interval appears, then either:
  1. it gives an external branch directly; or
  2. it coexists with a B-tail crossing interval and can be ignored for extraction existence.
```

### Case 5. `I` terminates in `Y`

If `I` begins in `B` and crosses `z q A`, then it is already covered by Case 3 with a possibly nonempty `Y_prefix`.

If `I` begins outside `B`, or begins in `A` or `q`, then it is a right-exterior interval.  Such intervals route to external bridge or signed/exterior branches unless they are the target full-A tail-core with `Y_prefix`.

Thus `Y` is allowed in the hidden-support form only as a prefix appended after the `A` block:

```text
B_tail + z + q + A_prefix + Y_prefix = 0.
```

## Extraction conclusion

After excluding tautological and already-routed exterior/local cases, any useful zero interval crossing the active support separator must be one of:

```text
B_tail + z + q = 0,
B_tail + z + q + A_i + Y_prefix = 0,
B_tail + z + q + A1 + A2 + Y_prefix = 0.
```

These reduce respectively to:

```text
B_prefix = q,
B_tail + q + Y_prefix = A_complement,
B_tail + q + Y_prefix = 0.
```

With `Y_prefix` empty, the last two become:

```text
B_tail + q = A_complement,
B_tail + q = 0.
```

Therefore the hidden-support extraction families are:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

## What remains non-formal

This draft still uses two branch-exclusion statements that must be made precise:

```text
1. Proper sub-blocks of B z route to prior terminal/support branches.
2. Intervals wholly inside z q A or crossing only X/exterior zones route to signed/external/support branches.
```

These are compatible with the existing classifier vocabulary, but need formal lemma references.

## Minimal formal lemma dependencies

The endpoint enumeration can be closed if the proof already has:

```text
Lemma E1. Proper sub-terminal support interval exclusion.
Lemma E2. Exterior crossing interval routes to external bridge.
Lemma E3. Local q/A or A/B zero interval routes to signed/distributed branch.
Lemma E4. Pure worse-only excludes already-routed branches.
```

Then Lemma A follows by finite endpoint-zone enumeration.

## Status

```text
Endpoint-zone enumeration proof draft complete.
Remaining work: link excluded endpoint cases to named prior branch lemmas.
```
