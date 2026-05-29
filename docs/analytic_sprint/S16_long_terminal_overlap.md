# S16. Long terminal overlap/counting attack

This file attacks the dominant hard no-clean-descent residue identified in S15:

```text
LONG_TERMINAL_BRIDGE
```

## Setup

Let

```text
R = A Z B,
Z = z_1 ... z_m,
m >= 3,
sum(Z)=0,
```

where `Z` is an active shortest zero interval in a `D_short`-minimal ordering.

For a right-adjacent atom `q` after `Z`, write

```text
R = X Z q Y.
```

A right terminal bridge has

```text
z_m + Y_s = 0
```

where `Y_s` is a prefix of `Y`.

It is long if

```text
1 + |Y_s| >= m.
```

Similarly, a left terminal bridge has

```text
L_s + z_1 = 0
```

where `L_s` is a suffix of the left external side. It is long if

```text
1 + |L_s| >= m.
```

## Why long terminal bridges are expensive

A long terminal bridge consumes at least

```text
m-1
```

external atoms on one side of `Z`.

Thus if a shortest zero interval has terminal bridges on both sides, the total consumed support is at least

```text
2m - 2.
```

Since the active block itself has length `m`, this is a large local footprint.

The hope is:

```text
large footprint + no clean descent
=> overlap, endpoint sharing, or equal-difference structure.
```

## Same-side overlap principle

Suppose two right terminal bridges share the same active `Z` but arise from two different relevant moves or nearby active intervals:

```text
z_m + Y_s = 0,
z'_m + Y'_{s'} = 0.
```

If the right supports overlap, subtracting the two equations cancels the overlap and gives an equal-difference relation between endpoint atoms and remaining external tails.

This is structurally a distributed bridge:

```text
internal endpoint difference = external interval difference.
```

## Two-sided terminal principle

If both sides of the same active `Z` have long terminal bridges:

```text
L_s + z_1 = 0,
z_m + Y_t = 0,
```

then

```text
L_s = -z_1,
Y_t = -z_m.
```

Subtracting or adding these gives:

```text
L_s - Y_t = z_m - z_1,
L_s + Y_t = -(z_1+z_m).
```

If the endpoint pair itself has a simple relation, then a shorter endpoint zero interval or pair trap appears.

If not, then the two long external supports encode the two endpoint atoms externally.  This should enable an exchange of endpoint-support blocks with part of `Z`.

## Lemma S16.1: long two-sided terminal supports force large footprint

Assume both terminal bridges exist for an active shortest zero interval `Z`:

```text
L_s + z_1 = 0,
z_m + Y_t = 0,
```

and both are long:

```text
1+s >= m,
1+t >= m.
```

Then the combined external support length satisfies

```text
s+t >= 2m-2.
```

If the total number of atoms outside `Z` is less than `2m-2`, then the two supports must overlap in the linear ordering or one side cannot exist.

### Proof

Immediate from the two length inequalities. ∎

## Why this matters

If `S` is small relative to `m`, two-sided long terminal bridge is impossible without overlap.  If `S` is large, the external supports are large enough that other shortest zero intervals or external-equal-difference relations are likely forced.

This suggests a size split:

```text
small outside support -> overlap contradiction;
large outside support -> many available outside atoms, use another q or distributed bridge.
```

## One-sided long terminal case

Suppose only a right long terminal bridge appears repeatedly.

For a fixed active `Z`, there is at most one immediate right-adjacent atom `q`, but multiple insertion depths may all be blocked by the same terminal endpoint.

This is exactly the degeneracy identified in S11:

```text
max(B_q)=m-1
```

A single terminal bridge can block every insertion position.

Therefore one-sided terminal cannot be eliminated by counting insertion positions alone.

It must be attacked by using the other side of `Z`, a neighboring zero interval, or endpoint absorption.

## Lemma S16.2: pure one-sided terminal is unstable under reversal unless boundary-blocked

Let `Z` be an interior shortest zero interval with atoms on both sides.

If all right q-through-Z insertions are blocked only by a right long terminal bridge, then applying the same analysis to the left adjacent atom gives either:

```text
1. clean descent;
2. signed interval;
3. distributed bridge;
4. left terminal bridge.
```

If cases 1--3 do not occur, the hard case becomes two-sided terminal.

### Status

This is nearly definitional once both adjacent atoms are tested.  The formal proof must show the left-side reversal uses the same `D_short` ordering.

## Lemma S16.3: two-sided long terminal reduces to support-overlap or endpoint-external encoding

Assume `Z` is interior and both adjacent sides are terminal-blocked long.

Then either:

```text
1. the long supports overlap or touch, producing an external zero/equal-difference relation;
2. the supports are disjoint, consuming at least 2m-2 external atoms;
3. the ordering has enough exterior length to choose another active shortest zero interval or another adjacent atom whose bridge is distributed.
```

This is the first serious global-counting lemma needed in the project.

## What we need from computation next

The current aggregate data counts terminal flags but not record-level support geometry.

We need record-level splits:

```text
A. hard records with both left and right terminal flags;
B. hard records with only right terminal flags;
C. hard records with only left terminal flags;
D. hard records with terminal + distributed;
E. hard records with terminal + signed;
F. min/max/median terminal_total_length by hard record;
G. whether long supports on both sides overlap in the atom index line.
```

## Next script refinement

Add a summary mode or companion script:

```text
scripts/summarize_terminal_records.py
```

Input:

```text
logs/external_bridge_hard_terminal_lengths_p17.jsonl
logs/external_bridge_hard_terminal_lengths_p23.jsonl
```

Output:

```json
{
  "records": 2783,
  "both_left_right_terminal": ...,
  "right_only_terminal": ...,
  "left_only_terminal": ...,
  "terminal_and_distributed": ...,
  "terminal_and_signed": ...,
  "short_terminal_records": ...,
  "long_terminal_records": ...,
  "both_short_and_long_records": ...,
  "terminal_total_length_histogram": {...}
}
```

## Proof-priority update

The next proof target should be:

```text
Two-sided long terminal bridge reduction.
```

Reason:

```text
1. hard records are dominated by long terminal bridges;
2. one-sided terminal is probably not enough to contradict anything;
3. two-sided terminal gives two endpoint equations that can be combined;
4. if hard records are mostly two-sided, this is the main route;
5. if hard records are mostly one-sided, we need a boundary/one-sided lemma instead.
```

## Status

```text
Dominant hard case: long terminal bridge.
Most likely proof tool: support-overlap/counting plus two-sided endpoint equations.
Immediate next task: record-level terminal summary script.
```
