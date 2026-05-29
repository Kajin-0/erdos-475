# S54. Hidden-support extraction lemma draft

This note drafts the formal hidden-support extraction lemma using the endpoint taxonomy results from S52 and the left-external resolution from S53.

## Lemma A. Hidden-support extraction

### Statement

Let `R` be an `m=3` right-terminal pure worse-only residual in `Z/pZ` with normal form

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0,
D_short(R) = (1,3,1,[2]).
```

Consider the local permutation

```text
A z q B -> B z q A.
```

Then the moved order contains at least one non-tautological hidden-support zero interval whose symbolic form is one of:

```text
B_tail + z + q + A1 + A2 + Y_prefix = 0,
B_tail + z + q + A_i + Y_prefix = 0,
B_tail + z + q = 0.
```

Consequently, the moved order exposes one of the reduced equations:

```text
B_tail + q + Y_prefix = 0,
B_tail + q + Y_prefix = A_complement,
B_prefix = q.
```

The special case `Y_prefix` empty gives

```text
B_tail + q = 0,
B_tail + q = A_complement.
```

Thus the extraction families are exactly:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

## Algebraic reductions

### Full-A tail-core case

Suppose the zero interval has symbolic block

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

If `Y_prefix` is empty, this is

```text
B_tail + q = 0.
```

### Partial-A tail-core case

Suppose the zero interval has symbolic block

```text
B_tail + z + q + A_i + Y_prefix = 0.
```

Let `{i,j}={1,2}`.  Since

```text
A_i + A_j + z = 0,
```

we have

```text
z + A_i = -A_j.
```

Therefore

```text
B_tail + q + Y_prefix = A_j.
```

In the current certificate, the observed reduced family is

```text
B_tail + q = A_complement.
```

### Prefix-core case

Suppose the zero interval has symbolic block

```text
B_tail + z + q = 0.
```

Because

```text
B_prefix + B_tail + z = 0,
```

subtracting the two equations gives

```text
B_prefix = q.
```

## Endpoint taxonomy support

The endpoint-taxonomy script verifies target hidden-support presence in all certified records:

```text
p=17: target present in 35/35 records
p=23: target present in 59/59 records
```

The block-class histograms were:

```text
p=17:
  hidden_full_A_tail_core     33
  hidden_partial_A_tail_core   8
  hidden_prefix_core           5
  tautology_terminal_zB       35

p=23:
  hidden_full_A_tail_core     65
  hidden_partial_A_tail_core  16
  hidden_prefix_core          10
  left_external_X              2
  tautology_terminal_zB       59
```

Thus every record has a target interval.  The only non-target intervals are:

```text
tautology_terminal_zB,
left_external_X.
```

The `left_external_X` cases occur only twice in p=23, records 183 and 449, and both contain a valid `hidden_full_A_tail_core` target interval.

## Endpoint-exclusion proof structure

The formal proof should be organized as follows.

### Step 1. Enumerate endpoint zones

In the moved order

```text
X B z q A Y,
```

zero intervals have endpoints in the ordered zones:

```text
X | B | z | q | A | Y.
```

Any interval wholly corresponding to `B+z` is the terminal tautology:

```text
sum(B) + z = 0.
```

Any interval corresponding to `A+z` is the triple tautology:

```text
A1 + A2 + z = 0.
```

### Step 2. Identify the only useful crossing forms

A non-tautological interval crossing the central separator `z q` and involving the support block `B` must be one of:

```text
B_tail + z + q,
B_tail + z + q + A_i + Y_prefix,
B_tail + z + q + A1 + A2 + Y_prefix.
```

These produce exactly the hidden-support equations.

### Step 3. Dispose of non-target forms

Other interval shapes fall into prior branches or are irrelevant to extraction:

```text
terminal_zB       -> tautological terminal equation;
left_external_X   -> external/cross-window collision, and target interval still exists;
right exterior    -> external bridge branch;
A/B without zq    -> signed/distributed branch;
B/q support only  -> Bq/BqY routed branch.
```

For Lemma A as an existence lemma, it is enough to prove that at least one target interval exists.  Non-target intervals do not invalidate the extraction.

## Empirical certificate connection

After Lemma A, S50 gives the complete branch reduction:

```text
1. B_tail+q = 0
   -> Bq_zero target
   -> routed through existing classifier machinery.

2. B_tail+q+Y_prefix = 0
   -> BqY_zero target
   -> routed through existing classifier machinery.

3. B_tail+q = A_complement
   -> D_short-neutral
   -> q_tail_span_gap decreases.

4. B_prefix = q
   -> D_short-neutral
   -> q_tail_span_gap decreases.
```

## Remaining formal burden

The proof is not yet complete.  The missing formal arguments are:

```text
1. a non-computational endpoint-exclusion proof for Step 2;
2. a proof that pure worse-only forces the existence of at least one non-tautological interval under B z q A;
3. a proof that target intervals reduce exactly as stated;
4. formalization of the Bq/BqY routing and q_tail_span_gap tie-break.
```

The third item is algebraic and essentially done.  The main mathematical work is item 1 and item 2.

## Status

```text
Lemma A has a concrete proof skeleton and complete endpoint taxonomy support.
Next formal step: prove the endpoint-zone enumeration without relying on logs.
```
