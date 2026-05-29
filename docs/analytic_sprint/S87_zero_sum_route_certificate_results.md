# S87. Zero-sum route certificate results

This note records the output of:

```text
scripts/make_zero_sum_route_certificate.py
```

using:

```text
logs/zero_sum_route_certificate.md
logs/zero_sum_route_certificate.json
```

## Main result

The zero-sum hidden-support branch is fully routed in the current certificate.

Aggregate summary:

```text
zero_sum_rows = 4
zero_sum_records = 83
target_classified_records = 83
routed_records = 83
all_rows_routed = true
```

Thus every zero-sum record is both:

```text
1. classified as the intended target obstruction Bq_zero or BqY_zero;
2. routed to already-closed branch machinery.
```

## Certificate table

```text
| p | family | target | records | verified_total | best_bridge_class | target_coverage | route_coverage | dominant_route_labels | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 17 | B_tail+q | Bq_zero | 23 | 35/35 | worse:23 | 23/23 | 23/23 | CLEAN_DESCENT:182, DISTRIBUTED_BRIDGE:1, EXTERNAL_BRIDGE:6, MIXED:125 | zero_sum_routed |
| 17 | B_tail+q+Y_prefix | BqY_zero | 8 | 35/35 | worse:8 | 8/8 | 8/8 | CLEAN_DESCENT:92, DISTRIBUTED_BRIDGE:2, MIXED:54 | zero_sum_routed |
| 23 | B_tail+q | Bq_zero | 20 | 59/59 | worse:20 | 20/20 | 20/20 | CLEAN_DESCENT:103, DISTRIBUTED_BRIDGE:3, EXTERNAL_BRIDGE:12, MIXED:92 | zero_sum_routed |
| 23 | B_tail+q+Y_prefix | BqY_zero | 32 | 59/59 | worse:32 | 32/32 | 32/32 | CLEAN_DESCENT:487, DISTRIBUTED_BRIDGE:12, EXTERNAL_BRIDGE:32, MIXED:305 | zero_sum_routed |
```

## Coverage by family

### `B_tail+q -> Bq_zero`

```text
p=17: 23/23 classified, 23/23 routed
p=23: 20/20 classified, 20/20 routed
combined: 43/43 routed
```

### `B_tail+q+Y_prefix -> BqY_zero`

```text
p=17: 8/8 classified, 8/8 routed
p=23: 32/32 classified, 32/32 routed
combined: 40/40 routed
```

Combined zero-sum branch:

```text
83/83 routed
```

## Dominant route labels

The route-label histograms show that zero-sum cases route primarily through:

```text
CLEAN_DESCENT,
MIXED,
EXTERNAL_BRIDGE,
DISTRIBUTED_BRIDGE.
```

The total route-label counts are move/attempt-level counts, not record counts.  Record-level route coverage is given by `route_coverage`.

## Interpretation

The zero-sum hidden-support branch is not primitive.  Whenever Lemma A extracts one of:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
```

the record triggers already-routed machinery:

```text
Bq_zero  -> routed branch,
BqY_zero -> routed branch.
```

Therefore the zero-sum branch can be treated as closed in the empirical proof skeleton.

## Relation to equality branch

Together with S85:

```text
zero-sum families -> routed;
equality families -> refined tie-break descent.
```

Thus all four hidden-support families extracted by Lemma A are covered:

```text
B_tail + q = 0                  -> zero_sum_routed
B_tail + q + Y_prefix = 0       -> zero_sum_routed
B_tail + q = A_complement       -> equality_tiebroken
B_prefix = q                    -> equality_tiebroken
```

## Remaining publication-grade proof obligation

The remaining symbolic zero-sum task is to prove generally that:

```text
Bq_zero  implies one of the already-routed labels;
BqY_zero implies one of the already-routed labels.
```

The route certificate verifies this in all certified zero-sum records:

```text
p=17,p=23 combined: 83/83.
```

## Status

```text
Zero-sum route certificate consolidated.
Next: draft the symbolic Bq/BqY routing lemma.
```
