# S47. Bq/BqY routing closure status

This note records the route-classifier output for the zero-sum hidden-support branches.

## Inputs

The routing diagnostic was run on:

```text
logs/hidden_support_bridge_moves_p17_v5.jsonl
logs/hidden_support_bridge_moves_p23_v5.jsonl
```

using:

```text
scripts/route_bq_bqy_obstructions.py
```

## Result

Every zero-sum hidden-support branch record routes through the existing external-bridge classifier vocabulary.

### p=17

```text
records = 31
B_tail+q              = 23
B_tail+q+Y_prefix     =  8
```

Route success:

```text
B_tail+q              -> yes: 23 / 23
B_tail+q+Y_prefix     -> yes:  8 /  8
```

Route flags observed:

```text
B_tail+q:
  CLEAN_DESCENT          238
  LEFT_TERMINAL_BRIDGE    51
  RIGHT_TERMINAL_BRIDGE   47
  LONG_TERMINAL_BRIDGE    75
  SHORT_TERMINAL_BRIDGE   23
  SIGNED_INTERVAL         20
  EXTERNAL_BRIDGE         18
  DISTRIBUTED_BRIDGE       1

B_tail+q+Y_prefix:
  CLEAN_DESCENT          137
  RIGHT_TERMINAL_BRIDGE   36
  LONG_TERMINAL_BRIDGE    23
  SHORT_TERMINAL_BRIDGE   18
  SIGNED_INTERVAL         12
  EXTERNAL_BRIDGE          8
  DISTRIBUTED_BRIDGE       4
```

### p=23

```text
records = 52
B_tail+q              = 20
B_tail+q+Y_prefix     = 32
```

Route success:

```text
B_tail+q              -> yes: 20 / 20
B_tail+q+Y_prefix     -> yes: 32 / 32
```

Route flags observed:

```text
B_tail+q:
  CLEAN_DESCENT          138
  RIGHT_TERMINAL_BRIDGE   52
  LEFT_TERMINAL_BRIDGE    28
  MIXED_TERMINAL_BRIDGE    4
  LONG_TERMINAL_BRIDGE    76
  SHORT_TERMINAL_BRIDGE    8
  EXTERNAL_BRIDGE         19
  DISTRIBUTED_BRIDGE       3
  SIGNED_INTERVAL          3

B_tail+q+Y_prefix:
  CLEAN_DESCENT          691
  RIGHT_TERMINAL_BRIDGE  151
  LEFT_TERMINAL_BRIDGE    65
  MIXED_TERMINAL_BRIDGE    6
  LONG_TERMINAL_BRIDGE   189
  SHORT_TERMINAL_BRIDGE   38
  EXTERNAL_BRIDGE         83
  DISTRIBUTED_BRIDGE      20
  SIGNED_INTERVAL         51
```

## Interpretation

The zero-sum hidden-support families are no longer open empirical branches.

The chain is now:

```text
pure worse-only m=3 residual
  -> B z q A hidden-support extraction
  -> zero-sum branch: B_tail+q or B_tail+q+Y_prefix
  -> secondary Bq/BqY obstruction
  -> existing classifier route succeeds for every record
```

Observed route success:

```text
p=17: 31 / 31
p=23: 52 / 52
```

## Proof consequence

The Bq/BqY routing lemma can now be stated as:

```text
Lemma: Bq/BqY obstruction routing.
In the zero-sum hidden-support branch, the secondary Bq/BqY obstruction is not primitive. It routes to an existing descent/bridge mechanism: clean descent, signed interval, external bridge, distributed bridge, or terminal bridge.
```

The route-classifier output strongly supports using the existing branch vocabulary rather than defining a new obstruction class.

## Remaining branch

The only remaining pure worse-only subcase is the equality branch:

```text
B_tail+q=A_complement
B_prefix=q
```

Observed certificate:

```text
p=17: 4 equality records, all neutral
p=23: 7 equality records, all neutral
```

This branch needs a refined tie-break, likely based on one of:

```text
terminal position rank,
cyclic rank of A1,A2,z,
support-prefix rank involving q.
```

## Status

```text
Zero-sum hidden-support branch routed through existing classifier machinery.
Remaining target: equality-branch tie-break lemma.
```
