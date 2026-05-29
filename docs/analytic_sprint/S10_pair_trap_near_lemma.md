# S10. Pair-trap near-lemma and reduction to external bridge

This file records the proof-relevant pair-trap test and promotes the pair-trap route from exploratory attack to near-lemma status.

## Proof-relevant test

The VM run used the shortest-active mode:

```bash
python3 scripts/test_pair_trap_moves.py \
  --p 17 \
  --size 9 \
  --max-sets 500 \
  --order-samples 2000 \
  --orders-per-set 20 \
  --random-sets \
  --seed 3 \
  --order-mode defective \
  --active-mode shortest \
  --out logs/pair_trap_defective_p17_size9_v4_shortest.jsonl
```

Observed output:

```text
sets_seen=500
orders_tested=9460
pair_trap_records=681
aggregate={
  "danger": 0,
  "external_only": 216,
  "improved": 713,
  "non_shortest_active_artifact": 0,
  "supported_results": 929,
  "unsupported": 451
}
```

Summary over supported disjoint/crossing/nested traps:

```text
supported_results = 929
improved          = 713
external_only     = 216
danger            = 0
```

Thus every supported shortest-active pair-trap move routed to:

```text
D_short descent
or
EXTERNAL_BRIDGE.
```

## Non-proof-relevant long-active control

The long-active run was:

```bash
python3 scripts/test_pair_trap_moves.py \
  --p 17 \
  --size 9 \
  --max-sets 200 \
  --order-samples 1000 \
  --orders-per-set 10 \
  --random-sets \
  --seed 1 \
  --order-mode defective \
  --active-mode longest \
  --out logs/pair_trap_defective_p17_size9_v4_longest.jsonl
```

Observed output:

```text
sets_seen=200
orders_tested=1820
pair_trap_records=1803
aggregate={
  "danger": 0,
  "external_only": 2584,
  "improved": 11457,
  "non_shortest_active_artifact": 2,
  "supported_results": 14043,
  "unsupported": 14549
}
```

The previous apparent danger cases are now correctly classified as:

```text
non_shortest_active_artifact.
```

They occurred because the tested active interval was not the `D_short`-controlling shortest zero interval.

## Near-lemma statement

## Pair-trap block move near-lemma

Let `R` be a `D_short`-minimal defective ordering, and let `Z` be an active shortest zero interval. Suppose `Z` contains a supported pair trap of one of the following types:

```text
disjoint
crossing
nested
```

Then the corresponding canonical block move gives either:

```text
1. strict D_short descent; or
2. an external bridge obstruction.
```

## Supported trap types

### Disjoint

If

```text
i < j < k < l
```

and

```text
U(i,j)=U(k,l),
```

then swap the equal-sum blocks:

```text
A M B -> B M A.
```

### Crossing

If

```text
i < k < j < l
```

and

```text
U(i,j)=U(k,l),
```

then

```text
U(i,k)=U(j,l).
```

Swap the equal-sum flank blocks:

```text
A B C -> C B A.
```

### Nested

If

```text
i < k < l < j
```

and

```text
U(i,j)=U(k,l),
```

then

```text
U(i,k)+U(l,j)=0.
```

Bring the zero flanks together:

```text
A B C -> A C B.
```

## Remaining unsupported classes

The tester still records unsupported traps:

```text
shared_endpoint
other
```

These are not part of the supported near-lemma. They should be handled separately.

Likely classification:

```text
shared_endpoint -> degeneracy or whole-Z endpoint effect
other           -> orientation/cyclic wrap artifact or needs normalized interval labels
```

Before the final proof, write a short normalization lemma showing every nondegenerate internal pair trap either falls into supported disjoint/crossing/nested form or is an endpoint degeneracy that produces no new obstruction.

## Strategic consequence

The internal obstruction chain now compresses to:

```text
q-through-Z failure
  -> signed interval or external bridge
  -> q-zero compression
  -> pair trap or external bridge
  -> pair-trap block move
  -> D_short descent or external bridge.
```

Therefore the only primitive hard obstruction left is:

```text
persistent external bridge overlap.
```

## Next file

Proceed to:

```text
docs/analytic_sprint/S11_external_bridge_overlap.md
```

Target:

```text
If every useful q-through-Z insertion is externally blocked,
then translated internal endpoints q + T_b overlap heavily with the external endpoint path.
This overlap must either produce a shorter zero interval, a pair trap, or a clean insertion.
```

## Status

```text
Pair-trap route: near-lemma.
Empirical status: zero shortest-active danger cases in 929 supported moves.
Remaining formal work: endpoint/other normalization and exact external bridge definition.
Next hard case: persistent external bridge overlap.
```
