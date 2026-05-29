# S50. Pure worse-only branch closure certificate

This note records the closure checkpoint for the pure worse-only `m=3` right-terminal branch.

## Final certificate table

Generated file:

```text
logs/pure_worse_certificate_table_v4.md
```

Table:

```text
| p | family | records | mode | verified_total | best_bridge_class | target | target_coverage | route_coverage | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 17 | B_tail+q | 23 | zero_sum | 35/35 | worse:23 | Bq_zero | 23/23 | 23/23 | zero_sum_routed |
| 17 | B_tail+q+Y_prefix | 8 | zero_sum | 35/35 | worse:8 | BqY_zero | 8/8 | 8/8 | zero_sum_routed |
| 17 | B_tail+q=A_complement | 4 | equality | 35/35 | neutral:4 | q_tail_span_gap | 4/4 | not_applicable | equality_tiebroken |
| 23 | B_tail+q | 20 | zero_sum | 59/59 | worse:20 | Bq_zero | 20/20 | 20/20 | zero_sum_routed |
| 23 | B_tail+q+Y_prefix | 32 | zero_sum | 59/59 | worse:32 | BqY_zero | 32/32 | 32/32 | zero_sum_routed |
| 23 | B_tail+q=A_complement | 5 | equality | 59/59 | neutral:5 | q_tail_span_gap | 5/5 | not_applicable | equality_tiebroken |
| 23 | B_prefix=q | 2 | equality | 59/59 | neutral:2 | q_tail_span_gap | 2/2 | not_applicable | equality_tiebroken |
```

## Closure statement

For every certified pure worse-only `m=3` right-terminal residual in the current samples:

```text
p=17: 35 / 35 records
p=23: 59 / 59 records
```

the branch reduces by one of two mechanisms:

```text
1. zero-sum hidden-support branch:
   target obstruction exists and routes through existing branch machinery;

2. equality hidden-support branch:
   D_short is preserved but q_tail_span_gap decreases.
```

Therefore the pure worse-only branch is empirically closed under the refined defect:

```text
D_ref = (D_short, q_tail_span_gap)
```

for equality branches, plus the existing routed branch machinery for zero-sum branches.

## Normal form

The branch normal form is:

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0,
D_short(R) = (1,3,1,[2]).
```

The hidden-support extraction under

```text
A z q B -> B z q A
```

produces exactly one of:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

## Branch reduction map

### Zero-sum branches

```text
B_tail + q = 0
```

routes as:

```text
B_tail+q -> Bq_zero -> existing classifier route.
```

Certified coverage:

```text
p=17: 23 / 23 target, 23 / 23 routed
p=23: 20 / 20 target, 20 / 20 routed
```

```text
B_tail + q + Y_prefix = 0
```

routes as:

```text
B_tail+q+Y_prefix -> BqY_zero -> existing classifier route.
```

Certified coverage:

```text
p=17: 8 / 8 target, 8 / 8 routed
p=23: 32 / 32 target, 32 / 32 routed
```

### Equality branches

```text
B_tail + q = A_complement
```

is neutral for `D_short` but decreases:

```text
q_tail_span_gap.
```

Certified coverage:

```text
p=17: 4 / 4
p=23: 5 / 5
```

```text
B_prefix = q
```

is neutral for `D_short` but decreases:

```text
q_tail_span_gap.
```

Certified coverage:

```text
p=23: 2 / 2
```

## Refined rank

Define, for the extracted relation,

```text
S_tail(R) = span_gap({q} union B_tail),
```

where

```text
span_gap(U) = max_position(U) - min_position(U) + 1 - |U|.
```

Then the equality branches satisfy:

```text
D_short(R') = D_short(R),
S_tail(R') < S_tail(R).
```

## Formal proof obligations remaining

The branch is empirically closed.  To make it a proof, the following lemmas must be formalized.

### Lemma A. Hidden-support extraction

Show that pure worse-only `m=3` right-terminal residuals force one of the four extracted relations:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

Key missing ingredient:

```text
endpoint-exclusion argument for all other non-tautological zero intervals under B z q A.
```

### Lemma B. Zero-sum routing

Show that the zero-sum hidden-support branches force secondary `Bq_zero` / `BqY_zero` obstructions and that these are covered by existing clean descent / signed / external / distributed / terminal bridge machinery.

### Lemma C. Equality tie-break

Show that equality branches admit a `D_short`-neutral move decreasing `S_tail`.

## Current mathematical status

```text
Pure worse-only branch:
  empirically closed.

Remaining proof work:
  formalize extraction, routing, and tie-break lemmas.
```

## Recommended next target

The next highest-leverage proof target is Lemma A:

```text
formal endpoint-exclusion for the B z q A hidden-support extraction.
```

Once Lemma A is formalized, Lemmas B and C are much more mechanical because they correspond directly to finite local branch reductions already isolated by the certificate.
