# S15. Terminal bridge length empirical status

This file records the terminal bridge support-length split after instrumenting `scripts/test_external_bridge_overlap.py`.

The purpose is to determine whether terminal bridges should be attacked by:

```text
1. short endpoint absorption; or
2. long support-overlap / counting.
```

The data strongly favors the second path for hard no-clean-descent records.

## p=17, size=9, m>=3

Command:

```bash
python3 scripts/test_external_bridge_overlap.py \
  --p 17 \
  --size 9 \
  --max-sets 1000 \
  --order-samples 5000 \
  --orders-per-set 20 \
  --max-intervals 5 \
  --min-active-length 3 \
  --random-sets \
  --seed 9 \
  --out logs/external_bridge_p17_size9_terminal_lengths_seed9.jsonl
```

Observed global flags:

```text
records = 18880
CLEAN_DESCENT           = 36804
SIGNED_INTERVAL         =  8997
RIGHT_TERMINAL_BRIDGE   = 11216
LEFT_TERMINAL_BRIDGE    = 10042
SHORT_TERMINAL_BRIDGE   =  7374
LONG_TERMINAL_BRIDGE    = 13884
EXTERNAL_BRIDGE         =  7398
DISTRIBUTED_BRIDGE      =  3172
```

Hard no-clean-descent records:

```bash
jq -c 'select((.attempt_flag_counts.CLEAN_DESCENT // 0) == 0)' \
  logs/external_bridge_p17_size9_terminal_lengths_seed9.jsonl \
  > logs/external_bridge_hard_terminal_lengths_p17.jsonl
```

Observed hard flags:

```text
records = 2783
SIGNED_INTERVAL         =  458
RIGHT_TERMINAL_BRIDGE   = 4268
LEFT_TERMINAL_BRIDGE    = 2846
SHORT_TERMINAL_BRIDGE   =  766
LONG_TERMINAL_BRIDGE    = 6348
DISTRIBUTED_BRIDGE      =  848
```

Terminal-length ratio inside hard flags:

```text
LONG / SHORT = 6348 / 766 ≈ 8.29
```

## p=23, size=12, m>=3

Command:

```bash
python3 scripts/test_external_bridge_overlap.py \
  --p 23 \
  --size 12 \
  --max-sets 1000 \
  --order-samples 5000 \
  --orders-per-set 20 \
  --max-intervals 5 \
  --min-active-length 3 \
  --random-sets \
  --seed 10 \
  --out logs/external_bridge_p23_size12_terminal_lengths_seed10.jsonl
```

Observed global flags:

```text
records = 19160
CLEAN_DESCENT           = 34683
SIGNED_INTERVAL         =  6188
RIGHT_TERMINAL_BRIDGE   = 12261
LEFT_TERMINAL_BRIDGE    = 11943
SHORT_TERMINAL_BRIDGE   =  5574
LONG_TERMINAL_BRIDGE    = 18630
EXTERNAL_BRIDGE         =  8381
DISTRIBUTED_BRIDGE      =  4964
```

Hard no-clean-descent records:

```bash
jq -c 'select((.attempt_flag_counts.CLEAN_DESCENT // 0) == 0)' \
  logs/external_bridge_p23_size12_terminal_lengths_seed10.jsonl \
  > logs/external_bridge_hard_terminal_lengths_p23.jsonl
```

Observed hard flags:

```text
records = 3391
SIGNED_INTERVAL         =  368
RIGHT_TERMINAL_BRIDGE   = 4931
LEFT_TERMINAL_BRIDGE    = 4272
SHORT_TERMINAL_BRIDGE   =  799
LONG_TERMINAL_BRIDGE    = 8404
DISTRIBUTED_BRIDGE      = 1687
```

Terminal-length ratio inside hard flags:

```text
LONG / SHORT = 8404 / 799 ≈ 10.52
```

## Interpretation

Short terminal bridges exist, but they are not the dominant hard case.

The hard no-clean-descent residue is overwhelmingly:

```text
LONG_TERMINAL_BRIDGE
```

Therefore, the highest-leverage next proof target is:

```text
Long terminal bridge overlap/counting.
```

Endpoint absorption for short terminal bridges remains useful, but it should not be the main attack.

## Mathematical meaning

A right terminal bridge has:

```text
z_m + Y_s = 0
```

where `Y_s` is a right external prefix after `q`.

A long terminal bridge has:

```text
1 + |Y_s| >= m.
```

Since `m` is the length of the active shortest zero interval, every long terminal bridge consumes at least `m-1` external atoms on one side.

Similarly, a left terminal bridge consumes at least `m-1` atoms on the left side.

This suggests the following principle:

```text
Many long terminal bridges cannot be independent.
They must overlap, share endpoints, or force a two-sided relation.
```

Overlap or sharing should produce one of:

```text
1. distributed bridge;
2. signed interval;
3. pair trap;
4. shorter cross-boundary zero interval;
5. contradiction to D_short minimality.
```

## Next proof target

Proceed to:

```text
docs/analytic_sprint/S16_long_terminal_overlap.md
```

Target theorem:

```text
Let R be D_short-minimal and let Z be an active shortest zero interval with m>=3.
If all adjacent q-through-Z insertions are blocked by long terminal bridges and no clean descent exists, then either the left and right terminal supports overlap or their total length forces a distributed/equal-difference obstruction.
```

## Next script target

Instrument hard records further by counting:

```text
1. records with both left and right terminal bridges;
2. records with only right terminal bridges;
3. records with only left terminal bridges;
4. records with terminal + distributed;
5. records with terminal + signed;
6. minimum/maximum terminal support lengths per record.
```

This will tell us whether to prove a two-sided terminal lemma first or a same-side overlap lemma first.

## Status

```text
Terminal length split complete.
Dominant hard case: long terminal bridge.
Next proof attack: long terminal overlap/counting.
```
