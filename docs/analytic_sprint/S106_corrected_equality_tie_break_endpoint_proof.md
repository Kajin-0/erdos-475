# S106. Corrected equality tie-break endpoint proof

This note drafts the symbolic endpoint proof for Lemma C from S100.

The goal is to convert the corrected equality tie-break mechanism from S85 into a proof-facing local argument.

## Lemma C target

Suppose hidden-support extraction returns an equality family:

```text
B_tail + q = A_complement
```

or

```text
B_prefix = q.
```

Then the equality branch admits a local rearrangement that preserves `D_short` and strictly decreases the refined support-tail span gap:

```text
S_tail = span_gap({q} union T).
```

Therefore the equality branch descends in:

```text
D_ref = (D_short, S_tail).
```

## Local decomposition

For the support-tail equality case, write:

```text
B = P T M,
T = B_tail.
```

The old local order is:

```text
old: q | P | T | M.
```

Here:

```text
P = support prefix separating q from T,
T = extracted support tail,
M = remaining support material after T if present.
```

The two candidate localizations are:

```text
primary:  P | q | T | M,
fallback: q | T | P | M.
```

Both make:

```text
{q} union T
```

contiguous, hence both make:

```text
S_tail = 0.
```

Thus either move is sufficient if it preserves `D_short`.

## Span-gap calculation

In the old order:

```text
q | P | T | M,
```

the set:

```text
U = {q} union T
```

has span width:

```text
span_width_old(U) = 1 + |P| + |T|.
```

Since:

```text
|U| = 1 + |T|,
```

we get:

```text
S_tail(old) = |P|.
```

In either candidate order:

```text
P | q | T | M
q | T | P | M,
```

the elements of `U` are contiguous, so:

```text
S_tail(new) = 0.
```

Therefore, if `D_short` is preserved:

```text
D_ref(new) = (D_short(old),0) < (D_short(old),|P|) = D_ref(old).
```

## Primary-neutral case

If the primary localization:

```text
q | P | T | M -> P | q | T | M
```

is `D_short`-neutral, then the span-gap calculation immediately gives:

```text
D_ref(primary) < D_ref(old).
```

This closes the primary-neutral equality case.

## Primary-worse case

The only difficult case is when the primary localization is `D_short`-worse.

The corrected empirical mechanism from S84-S85 is:

```text
primary failure = P_suffix + q = 0.
```

not:

```text
T_prefix + q = 0.
```

The symbolic target is therefore:

```text
If P | q | T | M is D_short-worse, then every primary-new shortest zero block crosses the new adjacency P|q and has form P_suffix + q.
```

## Endpoint proof for primary failure shape

The primary move changes local adjacencies from:

```text
old:     q | P,  P | T,  T | M
primary: P | q,  q | T,  T | M.
```

The only newly created adjacencies are:

```text
P | q,
q | T.
```

The old adjacency:

```text
T | M
```

is unchanged.

Therefore any new contiguous zero block in the primary order must cross at least one of:

```text
P | q,
q | T.
```

### Excluding q|T as the worsening source

The equality hypothesis is:

```text
T + q = A_complement
```

or the corresponding `B_prefix=q` equality.  In the support-tail equality case, `q|T` is the intended localization: it makes the extracted equality support contiguous and reduces `S_tail` to zero.

A new zero block crossing only `q|T` would have the form:

```text
q + T_prefix = 0
```

or:

```text
q + T_subblock = 0.
```

But under the equality branch, the extracted relation is not zero-sum:

```text
q + T = A_complement,
```

and the zero-sum cases were already routed by Lemma Z.  Thus a `q|T` zero obstruction would force the record into the zero-sum route branch rather than the equality-only branch.

In the certified equality primary-failure rows, no `q|T` new shortest block occurs.

Therefore the primary-worse equality case is forced to use the other new adjacency:

```text
P | q.
```

### Form of a P|q block

Any contiguous block crossing `P|q` but not using material to the right of `q` has form:

```text
P_suffix + q.
```

If it also crossed `q|T`, the block would have form:

```text
P_suffix + q + T_prefix.
```

Such a block contains the `q|T` localization material and would either be longer than the observed shortest obstruction or route into the zero-sum/signed branch by the same endpoint logic as Lemma Z.

The primary-shortest worsening observed in the equality branch is therefore:

```text
P_suffix + q = 0.
```

This is the corrected primary-failure shape.

## Fallback move

When primary fails, use:

```text
fallback: q | T | P | M.
```

This fallback has two critical properties.

### Property 1. It localizes q with T

The set:

```text
{q} union T
```

is contiguous, so:

```text
S_tail(fallback) = 0.
```

### Property 2. It removes the P|q adjacency

The primary obstruction was:

```text
P_suffix + q = 0.
```

This requires the adjacency:

```text
P | q.
```

Fallback changes the order to:

```text
q | T | P | M.
```

so `P` is no longer adjacent to `q`.  Therefore the primary-new shortest block:

```text
P_suffix + q
```

is not contiguous in the fallback order.

## Fallback cleanliness

The fallback introduces new adjacencies:

```text
q | T,
T | P.
```

The `q|T` adjacency is the intended equality localization, already discussed above.  If it produced a zero-sum obstruction, the record would route to Lemma Z rather than remain in the equality branch.

The `T|P` adjacency reconnects two support pieces from the same support block.  Any zero block crossing `T|P` is a support-internal zero relation.  Such a relation either already existed in the old support block or triggers the support/signed branch machinery.

Thus, within the certified equality branch, fallback creates no new shortest zero block.

Empirically, S80 verifies:

```text
fallback_new_short_total = 0
fallback_new_short_symbols = {}
fallback_new_zone_histogram = {}
fallback_zone_histogram = {A+z: 2}
```

So the only fallback zero interval class is the old terminal triple:

```text
A1 + A2 + z = 0.
```

Therefore:

```text
D_short(fallback) = D_short(old).
```

Combined with span-gap descent:

```text
D_ref(fallback) < D_ref(old).
```

## B_prefix = q family

The family:

```text
B_prefix = q
```

is an equality tie-break case in which the support-prefix relation already identifies `q` with the relevant support prefix.

The certified records occur for:

```text
p=23: 2/2 records.
```

The same refined-defect principle applies:

```text
localize q with the extracted support segment,
preserve D_short,
set S_tail = 0.
```

In the certificate, both records are handled by the primary-neutral/tie-break route without requiring a separate fallback obstruction.

For a publication-grade proof, this family should either be reduced to the same `q|P|T|M` template by relabeling, or stated as a short separate equality-prefix lemma.

## Lemma C proof summary

The equality branch proof is:

```text
1. Decompose B = P T M.
2. Compute S_tail(old)=|P|.
3. Try primary P|q|T|M.
4. If primary is D_short-neutral, then D_ref descends.
5. If primary is D_short-worse, the only primary-new shortest block is P_suffix+q.
6. Use fallback q|T|P|M.
7. Fallback removes P|q, creates no new shortest block, preserves D_short.
8. Fallback has S_tail=0, so D_ref descends.
```

Therefore every equality branch record descends in `D_ref`.

## Certified alignment

From S85:

```text
p=17:
  B_tail+q=A_complement: 4/4 equality_tiebroken

p=23:
  B_tail+q=A_complement: 5/5 equality_tiebroken
  B_prefix=q:            2/2 equality_tiebroken

Total:
  11/11 equality records tiebroken.
```

From S84:

```text
primary_failure_rows = 2
rows_with_only_Pq_new_short = 2
rows_with_non_Pq_new_short = 0
zone_class_histogram = {P+q: 2}
```

From S80:

```text
fallback_new_short_total = 0
fallback_new_short_symbols = {}
fallback_new_zone_histogram = {}
```

## Remaining rigor gaps

This proof is now structurally clear, but the following symbolic details remain to be tightened:

```text
1. Formal exclusion of q|T as a primary-worse source without referencing certificates.
2. Formal proof that any P|q primary-new shortest block must reduce to P_suffix+q rather than P_suffix+q+T_prefix.
3. Formal proof that T|P fallback adjacency cannot create a new shortest zero block outside already-routed support/signed machinery.
4. Uniform treatment of the B_prefix=q family, either by relabeling or a separate equality-prefix lemma.
```

## Status

```text
Corrected equality tie-break endpoint proof drafted.
Primary failure mechanism: P_suffix+q.
Fallback: q|T|P|M removes P|q and preserves D_short in certified records.
Next: either tighten the four remaining symbolic gaps or move to VERIFIED_DOMAIN.md.
```
