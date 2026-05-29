# S13. Hard external-bridge status and next proof target

This file records the first hard-record distribution for the `m >= 3` external-bridge regime.

A hard record means:

```text
attempt_flag_counts.CLEAN_DESCENT = 0
```

That is the proof-relevant external-bridge residue: no tested adjacent q-through-Z insertion immediately decreases `D_short`.

## p=17 hard records

Input file:

```text
logs/external_bridge_p17_size9_minge3_seed7.jsonl
```

Filter:

```bash
jq -c 'select((.attempt_flag_counts.CLEAN_DESCENT // 0) == 0)' \
  logs/external_bridge_p17_size9_minge3_seed7.jsonl \
  > logs/external_bridge_hard_p17_minge3_seed7.jsonl
```

Observed:

```text
hard_records = 2793
```

Aggregate labels:

```text
RIGHT_TERMINAL_BRIDGE = 4024
LEFT_TERMINAL_BRIDGE  = 2618
DISTRIBUTED_BRIDGE    =  853
MIXED                 =  473
```

Aggregate flags:

```text
RIGHT_TERMINAL_BRIDGE = 4325
LEFT_TERMINAL_BRIDGE  = 2790
DISTRIBUTED_BRIDGE    =  853
SIGNED_INTERVAL       =  473
```

## p=23 hard records

Input file:

```text
logs/external_bridge_p23_size12_minge3_seed8.jsonl
```

Filter:

```bash
jq -c 'select((.attempt_flag_counts.CLEAN_DESCENT // 0) == 0)' \
  logs/external_bridge_p23_size12_minge3_seed8.jsonl \
  > logs/external_bridge_hard_p23_minge3_seed8.jsonl
```

Observed:

```text
hard_records = 3381
```

Aggregate labels:

```text
RIGHT_TERMINAL_BRIDGE = 4746
LEFT_TERMINAL_BRIDGE  = 4110
DISTRIBUTED_BRIDGE    = 1674
MIXED                 =  370
```

Aggregate flags:

```text
RIGHT_TERMINAL_BRIDGE = 4958
LEFT_TERMINAL_BRIDGE  = 4268
DISTRIBUTED_BRIDGE    = 1674
SIGNED_INTERVAL       =  370
```

## Interpretation

In the no-clean-descent residue, terminal bridges dominate.

For `p=17`:

```text
terminal flags = 4325 + 2790 = 7115
distributed flags = 853
signed flags = 473
```

For `p=23`:

```text
terminal flags = 4958 + 4268 = 9226
distributed flags = 1674
signed flags = 370
```

Thus the next proof target should not be generic external-overlap.

It should be:

```text
TERMINAL BRIDGE REDUCTION
```

The distributed bridge branch remains important, but the dominant hard obstruction is terminal.

## Proof-priority ranking

```text
1. Terminal bridge reduction.
2. Distributed bridge equal-difference reduction.
3. Mixed terminal + signed branch, routed through S07/S10.
4. Ordinary external bridge, which should either refine to terminal/distributed under persistence or expose missing classification.
```

## Terminal bridge shape

For a right-adjacent atom:

```text
R = X Z q Y,
Z = z_1 ... z_m,
sum(Z)=0,
T_{m-1} = -z_m.
```

A right-terminal bridge has:

```text
x + q + T_{m-1} = x + q + Y_s
```

so

```text
T_{m-1} = Y_s
```

and therefore

```text
z_m + Y_s = 0.
```

Thus terminal bridge is not mysterious.  It says the last atom of the zero interval cancels a right-side external prefix.

For a left-terminal bridge, by reversal the analogous statement says the first atom of the zero interval cancels a left-side external suffix.

## Main conceptual reduction

Terminal bridges are endpoint-cancellation relations.

They should be handled by endpoint absorption, not additive-energy overlap.

The target is to prove:

```text
If every useful insertion at both sides of a shortest zero interval is blocked only by terminal bridges,
then one endpoint atom of Z participates in a shorter cross-boundary zero interval,
which either decreases D_short or creates a signed/pair/distributed obstruction already routed elsewhere.
```

## Next file

Proceed to:

```text
docs/analytic_sprint/S14_terminal_bridge_reduction.md
```

Target theorem:

```text
Terminal Bridge Reduction.
Let R be D_short-minimal and let Z be an active shortest zero interval with m>=3.
If adjacent q-through-Z moves have no clean descent and are terminal-bridge blocked,
then either:
  1. a shorter cross-boundary zero interval exists;
  2. a signed interval appears and routes to S07;
  3. a pair trap appears and routes to S10;
  4. two terminal bridges combine into a distributed bridge;
  5. contradiction to D_short-minimality.
```

## Status

```text
Hard external bridge identified.
Dominant hard branch: terminal bridge.
Next proof attack: endpoint-cancellation / terminal-bridge reduction.
```
