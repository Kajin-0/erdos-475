# S107. Equality tie-break symbolic gap closure draft

S106 drafted the corrected equality tie-break endpoint proof and isolated four remaining symbolic gaps:

```text
1. Formal exclusion of q|T as a primary-worse source.
2. Formal reduction of P|q new shortest blocks to P_suffix+q.
3. Formal proof that fallback T|P cannot create a new shortest zero block outside already-routed support/signed machinery.
4. Uniform treatment of the B_prefix=q family.
```

This note drafts local sublemmas addressing those gaps.

## Local setup

Work in the support-tail equality family:

```text
B_tail + q = A_complement.
```

Write:

```text
B = P T M,
T = B_tail.
```

The old, primary, and fallback local orders are:

```text
old:      q | P | T | M,
primary:  P | q | T | M,
fallback: q | T | P | M.
```

The refined defect is:

```text
D_ref = (D_short, S_tail),
S_tail = span_gap({q} union T).
```

Both primary and fallback make `{q} union T` contiguous:

```text
S_tail = 0.
```

Therefore the only obstruction is whether `D_short` is preserved.

## Gap 1. Excluding q|T as the primary-worse source

### Sublemma C1. qT-zero implies zero-sum route

If the primary order

```text
P | q | T | M
```

creates a new shortest zero block crossing the adjacency

```text
q | T,
```

then the record is not a primitive equality obstruction.  It routes to the zero-sum/signed machinery already handled by Lemma Z.

### Reason

Any new contiguous zero block crossing `q|T` has one of the forms:

```text
q + T_prefix = 0,
P_suffix + q + T_prefix = 0,
q + T_subblock = 0.
```

The first and third forms are direct zero-sum support-tail or support-subtail relations involving `q`.  They fall under the same endpoint classification used in Lemma Z:

```text
SIGNED_INTERVAL,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
TERMINAL_BRIDGE,
CLEAN_DESCENT.
```

The second form includes a `P_suffix` term.  If it is shortest and genuinely new, then either:

```text
1. the shorter suffix q+T_prefix is already zero, which routes by Lemma Z; or
2. the zero cancellation depends essentially on P_suffix, in which case the block also crosses P|q and is classified as a P|q obstruction rather than a pure q|T obstruction.
```

Thus a primary-worse equality case cannot have a primitive `q|T` obstruction.  It must either route by Lemma Z or be charged to the `P|q` adjacency.

### Certificate alignment

S84 verifies:

```text
primary_failure_rows = 2
rows_with_only_Pq_new_short = 2
rows_with_non_Pq_new_short = 0
```

So no certified primary-failure row has a non-`P+q` new shortest block.

## Gap 2. Reducing P|q new shortest blocks to P_suffix+q

### Sublemma C2. Minimal Pq obstruction has no T-prefix

Suppose the primary order

```text
P | q | T | M
```

creates a new shortest zero block crossing `P|q`, and suppose the block is not already routed by Lemma Z.

Then the block has form:

```text
P_suffix + q = 0.
```

### Proof sketch

A contiguous block crossing `P|q` has one of the forms:

```text
P_suffix + q,
P_suffix + q + T_prefix.
```

If the second form occurs, then it also crosses `q|T`.  There are two possibilities.

#### Case 1. q+T_prefix is zero

Then:

```text
q + T_prefix = 0,
```

which is a zero-sum route by Lemma Z.  This is not a primitive equality obstruction.

#### Case 2. q+T_prefix is nonzero

Then the zero relation depends on `P_suffix`:

```text
P_suffix = -(q+T_prefix).
```

But the equality branch already has the support-tail relation:

```text
q + T = A_complement.
```

A zero block using both `P_suffix` and `T_prefix` gives a support-internal split relation between pieces of `B` and `A_complement`.  Such a relation is either:

```text
1. longer than the minimal P_suffix+q obstruction when the terminal T_prefix is removed; or
2. a support/signed bridge obstruction already routed by the signed/support machinery.
```

Therefore the only primitive primary-new shortest block crossing `P|q` is:

```text
P_suffix + q = 0.
```

### Certificate alignment

The two certified primary-failure rows are exactly:

```text
p=17 record 739: B3 q
p=23 record 716: B3 B4 q
```

Both have zone class:

```text
P+q.
```

No `P+q+T` block occurs in the primary-failure certificate.

## Gap 3. Fallback T|P cleanliness

### Sublemma C3. T|P fallback obstruction routes or is old

In the fallback order

```text
q | T | P | M,
```

any new zero block crossing the adjacency

```text
T | P
```

is either:

```text
1. an old support-internal zero relation already present in B;
2. a signed/support obstruction handled by existing branch machinery;
3. longer than the active shortest zero block and therefore not a D_short worsening.
```

### Reason

The fallback only permutes pieces inside the support block after placing `q` next to `T`:

```text
old support order:      P | T | M,
fallback support order: T | P | M.
```

A zero block crossing `T|P` consists entirely of support atoms unless it also includes `q`.  If it does not include `q`, it is support-internal.  Such support-internal zero relations are not new primitive equality obstructions; they are already covered by support/signed route logic.

If it includes `q`, then it crosses `q|T`, so Sublemma C1 applies and the record routes by Lemma Z or signed/bridge machinery.

Therefore a fallback `T|P` block cannot be a new primitive shortest obstruction in the equality branch.

### Certificate alignment

S80 verifies in the primary-failure rows:

```text
fallback_new_short_total = 0
fallback_new_short_symbols = {}
fallback_new_zone_histogram = {}
fallback_zone_histogram = {A+z: 2}
```

Thus the only fallback zero interval class is the old terminal triple:

```text
A1 + A2 + z = 0.
```

## Gap 4. Uniform treatment of B_prefix=q

### Sublemma C4. B_prefix equality is prefix-normal form of the same tie-break

The family

```text
B_prefix = q
```

can be treated as a degenerate equality tie-break in which the extracted support segment lies on the prefix side rather than the tail side.

### Normalization

Write:

```text
B = T M,
T = B_prefix.
```

The equality is:

```text
T = q.
```

Equivalently:

```text
T - q = 0.
```

The relevant localization places `q` adjacent to `T`, giving:

```text
q | T | M
```

or its reflected form.  This makes the extracted equality support contiguous and sets the corresponding span gap to zero.

### Defect behavior

In the certified records:

```text
p=23: B_prefix=q, 2/2 records
```

both are handled by equality tie-break without fallback failure.

For a uniform proof, define a prefix span-gap:

```text
S_prefix = span_gap({q} union T),
```

where `T=B_prefix`.  Then the same refined-defect descent applies:

```text
D_ref_prefix = (D_short, S_prefix).
```

If desired, this can be folded into the same notation by allowing `T` to denote the extracted support segment, whether it is a prefix or tail.

## Consolidated Lemma C proof after gap closure

The equality tie-break proof can now be stated as follows.

### Statement

Let the equality branch extract a support segment `T` satisfying either:

```text
q + T = A_complement
```

or:

```text
T = q.
```

Then there is a local rearrangement `R -> R'` such that:

```text
D_short(R') = D_short(R),
span_gap({q} union T; R') = 0 < span_gap({q} union T; R).
```

Therefore:

```text
D_ref(R') < D_ref(R).
```

### Proof outline

1. Try the primary localization that places `q` adjacent to the extracted support segment `T`.
2. If this is `D_short`-neutral, the refined defect descends immediately.
3. If this is worse, Sublemma C1 excludes primitive `q|T` worsening.
4. Sublemma C2 shows the only primitive primary worsening is `P_suffix+q`.
5. Use the fallback order `q|T|P|M`.
6. The fallback removes the `P|q` adjacency responsible for `P_suffix+q`.
7. Sublemma C3 excludes new primitive `T|P` fallback worsening.
8. Hence fallback preserves `D_short` and sets span gap to zero.
9. Sublemma C4 covers the prefix-equality family by the same extracted-segment span-gap logic.

## What is still certificate-backed

The sublemmas above are proof-facing drafts.  They still rely on already-routed branch machinery being available for:

```text
zero-sum routes,
signed/support obstructions,
terminal/external/distributed bridges.
```

This is consistent with the theorem dependency graph in S99.

The key empirical checks remain:

```text
S84: primary failures are only P+q.
S80: fallback creates no new shortest block.
S85: 11/11 equality records tiebroken.
```

## Status

```text
Equality tie-break symbolic gaps drafted as sublemmas C1-C4.
Lemma C is now proof-facing, modulo citations to already-closed route machinery.
Next: either integrate Lemma Z and Lemma C into a final local theorem proof, or build docs/VERIFIED_DOMAIN.md.
```
