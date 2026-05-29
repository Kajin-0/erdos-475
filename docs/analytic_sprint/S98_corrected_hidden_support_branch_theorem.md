# S98. Corrected hidden-support branch theorem

This note assembles the corrected pure worse-only `m=3` hidden-support branch theorem from the two closed components:

```text
S85: corrected equality tie-break theorem
S97: zero-sum rich attempt witness closure
```

## Scope

This theorem applies to the certified pure worse-only right-terminal `m=3` residuals analyzed in the S17-S97 sprint.

The local residual has the structural form:

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0.
```

The branch is called `pure worse-only` because the obvious hidden-support localization attempts are not immediately improving under the base short-defect order.

## Defect order

The base short defect is:

```text
D_short = (E, L_min, N_min, M),
```

where:

```text
E      = partial-sum collision excess,
L_min  = shortest zero-block length,
N_min  = number of shortest zero blocks,
M      = repeated partial-sum multiplicity profile.
```

For equality branches we refine by the support-tail span gap:

```text
D_ref = (D_short, S_tail),
S_tail = span_gap({q} union T),
```

where `T` is the extracted support tail.

## Lemma A input

The hidden-support extraction reduces every certified pure worse-only residual to one of four families:

```text
1. B_tail + q = 0,
2. B_tail + q + Y_prefix = 0,
3. B_tail + q = A_complement,
4. B_prefix = q.
```

The first two are zero-sum families.  The last two are equality families.

## Theorem H. Corrected hidden-support branch theorem

### Statement

For every certified pure worse-only `m=3` right-terminal residual satisfying Lemma A, one of the following holds:

```text
1. the residual exits through an already-routed zero-sum branch;
2. the residual admits an equality tie-break move that preserves D_short and strictly decreases S_tail.
```

Consequently, no certified hidden-support residual remains primitive after applying the zero-sum routing lemma and equality tie-break theorem.

Equivalently, all four Lemma A families are covered:

```text
B_tail + q = 0                  -> zero_sum_routed,
B_tail + q + Y_prefix = 0       -> zero_sum_routed,
B_tail + q = A_complement       -> equality_tiebroken,
B_prefix = q                    -> equality_tiebroken.
```

## Proof

### Case 1. `B_tail + q = 0`

This is the `Bq_zero` family.

S97 gives record-level, example-level, and attempt-level coverage:

```text
record-level route coverage: 43/43
attempt-level witnesses: complete in sampled representatives
```

The zero-sum certificate routes this family through already-closed mechanisms including:

```text
CLEAN_DESCENT,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
SIGNED_INTERVAL,
terminal bridges.
```

Thus this family is not primitive.

### Case 2. `B_tail + q + Y_prefix = 0`

This is the `BqY_zero` family.

S97 gives record-level, example-level, and attempt-level coverage:

```text
record-level route coverage: 40/40
attempt-level witnesses: complete in sampled representatives
```

This family also routes through closed mechanisms:

```text
CLEAN_DESCENT,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
SIGNED_INTERVAL,
terminal bridges.
```

The presence of `Y_prefix` naturally exposes active-to-exterior bridge structure, but clean descent and distributed routes also occur.

Thus this family is not primitive.

### Case 3. `B_tail + q = A_complement`

This is an equality family.

Write the support block as:

```text
B = P T M,
T = B_tail.
```

The old local order is:

```text
old: q P T M.
```

The two candidate localizations are:

```text
primary:  P q T M,
fallback: q T P M.
```

Both make `{q} union T` contiguous, hence both give:

```text
S_tail = 0.
```

If the primary move is `D_short`-neutral, use it.

If the primary move is `D_short`-worse, S84-S85 show that the primary failure has the corrected form:

```text
P_suffix + q = 0.
```

The fallback removes the `P|q` adjacency and creates no new shortest block.  Therefore:

```text
D_short(fallback) = D_short(old),
S_tail(fallback) = 0 < S_tail(old).
```

So:

```text
D_ref(fallback) < D_ref(old).
```

Thus the equality branch descends under the refined defect.

### Case 4. `B_prefix = q`

This is the second equality family.

S85 includes this family in the equality tie-break coverage:

```text
p=23: B_prefix=q, 2/2 equality_tiebroken.
```

The same refined-defect mechanism applies:

```text
D_short preserved,
S_tail -> 0.
```

Thus this equality family also descends under `D_ref`.

## Certified coverage summary

The sprint has the following coverage layers.

### Zero-sum branch

From S97:

```text
Record-level route coverage:
  83/83 routed.

Representative route examples:
  24/24 extracted.

Attempt-level witnesses:
  24/24 matched.
```

Family split:

```text
B_tail+q:
  p=17: 23/23 routed
  p=23: 20/20 routed
  combined: 43/43 routed

B_tail+q+Y_prefix:
  p=17: 8/8 routed
  p=23: 32/32 routed
  combined: 40/40 routed
```

### Equality branch

From S85:

```text
p=17:
  B_tail+q=A_complement: 4/4 equality_tiebroken

p=23:
  B_tail+q=A_complement: 5/5 equality_tiebroken
  B_prefix=q:            2/2 equality_tiebroken
```

Combined equality coverage:

```text
11/11 equality records tiebroken.
```

### Hidden-support families combined

```text
zero_sum records: 83/83 covered
equality records: 11/11 covered
combined hidden-support records: 94/94 covered
```

## Corrected mechanism summary

The corrected equality mechanism is:

```text
old:      q | P | T | M
primary:  P | q | T | M
fallback: q | T | P | M
```

Primary can fail only by creating:

```text
P_suffix + q = 0.
```

Fallback removes the `P|q` adjacency and creates no new shortest block.

This supersedes the earlier incorrect `T_prefix+q` hypothesis.

## Relation to full theorem status

This note closes the certified hidden-support branch at the empirical-symbolic level.  It does not, by itself, prove the full Erdős 475 theorem.

A full proof still requires the global analytic bridge:

```text
analytic residue subset certified finite domain.
```

The safe claim boundary is therefore:

```text
Hidden-support pure worse-only branch: certified closed in the analyzed finite domain.
Full Erdős 475 theorem: still conditional on the global analytic reduction and verified-domain synchronization.
```

## Remaining publication-grade proof obligations

The certificate-backed theorem should be converted into symbolic lemmas:

```text
1. Lemma A: prove the four-family hidden-support extraction generally.
2. Lemma Z: prove Bq_zero and BqY_zero imply an already-routed branch symbolically.
3. Lemma C: prove the corrected equality tie-break symbolically:
   P q T M worse -> P_suffix+q only,
   q T P M creates no new shortest block.
4. Domain ledger: prove the analytic residue is contained in the verified finite domain.
```

## Status

```text
Corrected hidden-support branch theorem assembled.
Zero-sum branch: closed with rich attempt witnesses.
Equality branch: closed with corrected tie-break.
Safe theorem boundary preserved.
```
