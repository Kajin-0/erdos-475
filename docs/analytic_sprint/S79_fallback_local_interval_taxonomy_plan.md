# S79. Fallback local interval taxonomy plan

S78 reduced the equality fallback proof to two local claims:

```text
A. Primary worsening implies only q + T_prefix new shortest blocks.
B. Fallback q T P M creates no new shortest blocks.
```

S75 verified B at the shortest-block level for the two primary-failure rows:

```text
primary_failure_rows = 2
fallback_neutral = 2
fallback_new_short_blocks = none
```

The next diagnostic expands this from shortest-block accounting to full local interval taxonomy in the fallback order.

## Goal

For primary-failure rows only, classify all fallback zero intervals in the local order

```text
q | T | P | M
```

and mark each as:

```text
old      = same symbolic block exists in the old order;
new      = does not exist in old order;
local    = supported inside q/T/P/M zones;
external = involves X/Y zones.
```

## New diagnostic

Add:

```text
scripts/taxonomize_fallback_local_intervals.py
```

Inputs:

```text
--analysis logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl \
           logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl
--equations logs/bzqa_hidden_support_equations_p17_v3.jsonl \
            logs/bzqa_hidden_support_equations_p23_v3.jsonl
```

The script should:

```text
1. reconstruct old order A z q P T M;
2. reconstruct primary order A z P q T M;
3. reconstruct fallback order A z q T P M;
4. identify primary-failure rows where primary is worse;
5. enumerate all fallback zero intervals;
6. classify each interval by q/T/P/M endpoint zones;
7. mark whether its symbolic block exists in old;
8. summarize old/new interval classes and shortest intervals.
```

## Expected outcome

For the two primary-failure rows:

```text
fallback shortest new intervals = 0.
```

There may be longer fallback-new intervals.  Those should be classified and checked against already-routed branches or length noncriticality.

## Proof use

If the fallback has no new shortest intervals and any longer new intervals are routable/noncritical, then condition B becomes:

```text
q T P M preserves D_short.
```

This directly supports the fallback implication:

```text
P q T M worse -> q T P M neutral.
```

## Status

```text
Next: add fallback local interval taxonomy script and inspect the two primary-failure rows.
```
