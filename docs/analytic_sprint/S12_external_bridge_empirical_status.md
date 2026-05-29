# S12. External bridge empirical status for m >= 3

This file records the first meaningful external-bridge mining runs after filtering out length-2 inverse-pair shortest zero intervals.

## Why the earlier m=2 runs were not decisive

When `L_min=2`, the active zero interval is an inverse pair:

```text
Z = [a, -a]
```

This produces terminal-bridge behavior that is special to two-atom zero intervals.  It is not the main external-overlap hard case.

The script was therefore updated so `--min-active-length 3` filters during sampling, not only after candidate selection.

## p=17, size=9, m>=3 run

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
  --seed 7 \
  --out logs/external_bridge_p17_size9_minge3_seed7.jsonl
```

Observed output:

```text
sets_seen=1000
orders_tested=18780
skipped_short_active=2026568
external_bridge_records=18780
aggregate_labels={
  "CLEAN_DESCENT": 25999,
  "DISTRIBUTED_BRIDGE": 3217,
  "EXTERNAL_BRIDGE": 6202,
  "LEFT_TERMINAL_BRIDGE": 9466,
  "MIXED": 12817,
  "RIGHT_TERMINAL_BRIDGE": 6567
}
aggregate_flags={
  "CLEAN_DESCENT": 36346,
  "DISTRIBUTED_BRIDGE": 3217,
  "EXTERNAL_BRIDGE": 7235,
  "LEFT_TERMINAL_BRIDGE": 10135,
  "RIGHT_TERMINAL_BRIDGE": 11384,
  "SIGNED_INTERVAL": 8768
}
```

## p=23, size=12, m>=3 run

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
  --seed 8 \
  --out logs/external_bridge_p23_size12_minge3_seed8.jsonl
```

Observed output:

```text
sets_seen=1000
orders_tested=19200
skipped_short_active=2051797
external_bridge_records=19200
aggregate_labels={
  "CLEAN_DESCENT": 27624,
  "DISTRIBUTED_BRIDGE": 4920,
  "EXTERNAL_BRIDGE": 7619,
  "LEFT_TERMINAL_BRIDGE": 11353,
  "MIXED": 9199,
  "RIGHT_TERMINAL_BRIDGE": 8817
}
aggregate_flags={
  "CLEAN_DESCENT": 34969,
  "DISTRIBUTED_BRIDGE": 4920,
  "EXTERNAL_BRIDGE": 8478,
  "LEFT_TERMINAL_BRIDGE": 11848,
  "RIGHT_TERMINAL_BRIDGE": 12308,
  "SIGNED_INTERVAL": 6208
}
```

## Interpretation

The real m>=3 external-bridge regime is not dominated by one class.

It contains:

```text
1. many clean descents;
2. many terminal bridges;
3. a substantial ordinary external-bridge class;
4. a nontrivial distributed-bridge class;
5. many mixed attempts containing multiple simultaneous flags;
6. signed-interval flags, which should route back through S07/S10.
```

This supports the current proof architecture:

```text
external bridge
  -> terminal bridge branch
  -> distributed bridge branch
  -> signed interval branch already reduced
  -> mixed branch split by included flags
```

## Key next question

For a minimal counterexample, any available clean descent kills the ordering.

Therefore aggregate attempt counts are not enough.  The next useful statistic is record-level:

```text
How many records have no CLEAN_DESCENT attempt at all?
```

Those are the real hard records.

## Next command

For p=17:

```bash
jq -c 'select((.attempt_flag_counts.CLEAN_DESCENT // 0) == 0)' \
  logs/external_bridge_p17_size9_minge3_seed7.jsonl \
  > logs/external_bridge_hard_p17_minge3_seed7.jsonl

wc -l logs/external_bridge_hard_p17_minge3_seed7.jsonl
```

For p=23:

```bash
jq -c 'select((.attempt_flag_counts.CLEAN_DESCENT // 0) == 0)' \
  logs/external_bridge_p23_size12_minge3_seed8.jsonl \
  > logs/external_bridge_hard_p23_minge3_seed8.jsonl

wc -l logs/external_bridge_hard_p23_minge3_seed8.jsonl
```

Then summarize hard-record flags:

```bash
jq -s '{
  records: length,
  flags: reduce .[] as $r ({};
    reduce ($r.attempt_flag_counts | to_entries[]) as $e (.;
      .[$e.key] = ((.[$e.key] // 0) + $e.value)
    )
  ),
  labels: reduce .[] as $r ({};
    reduce ($r.attempt_label_counts | to_entries[]) as $e (.;
      .[$e.key] = ((.[$e.key] // 0) + $e.value)
    )
  )
}' logs/external_bridge_hard_p17_minge3_seed7.jsonl
```

## Proof priority update

The next analytic priority is no longer generic external bridge.  It is:

```text
hard records with no clean descent
```

Within those records, prioritize by frequency:

```text
1. terminal-only hard records;
2. distributed hard records;
3. mixed hard records containing signed intervals;
4. mixed hard records containing both terminal and distributed bridge.
```

## Candidate next lemma

A good next lemma is the terminal-bridge reduction:

```text
Let R be D_short-minimal and let Z be a shortest zero interval with m>=3.
If every q-through-Z insertion is blocked only by terminal bridges, then one of the two adjacent atoms to Z gives a clean descent, signed-interval reduction, or distributed bridge after reversing orientation.
```

This is motivated by the observed high terminal-bridge counts but still frequent clean descents.

## Status

```text
External bridge m>=3: active hard case identified.
Length-2 inverse-pair artifacts: filtered.
Next empirical target: hard records with no CLEAN_DESCENT.
Next proof target: terminal bridge reduction or distributed bridge reduction, depending on hard-record distribution.
```
