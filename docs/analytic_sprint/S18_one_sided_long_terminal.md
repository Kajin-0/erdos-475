# S18. One-sided long terminal bridge attack

This file attacks the largest remaining branch from S17:

```text
one-sided long terminal bridge
```

The goal is to understand when a terminal bridge on only one side of an active shortest zero interval can persist without producing clean descent, signed interval, pair trap, or distributed bridge.

## Setup

Work in an orientation where the terminal side is on the right.

Let

```text
R = X Z q Y,
Z = z_1 ... z_m,
m >= 3,
sum(Z)=0,
```

and let `Z` be an active shortest zero interval for `D_short`.

A right long terminal bridge is:

```text
z_m + Y_s = 0,
Y_s = y_1 + ... + y_s,
1+s >= m.
```

The support block is:

```text
W = y_1 ... y_s.
```

So:

```text
sum(W) = -z_m = T_{m-1}.
```

## What one-sided means

One-sided terminal means the same active interval `Z` has terminal obstruction only from the right adjacent side, or after orientation normalization only one adjacent side contributes terminal blocking.

The opposite side may be absent because `Z` touches a boundary, or it may exist but not produce a terminal bridge.

Thus split into:

```text
A. boundary one-sided terminal;
B. interior one-sided terminal.
```

The interior case should be easier because the opposite adjacent atom gives another q-through-Z test.

## Boundary one-sided terminal

If

```text
R = Z q Y
```

with `Z` at the left boundary, then there is no left adjacent atom.

But the total sum of `S` is nonzero, so the full ordering is not a zero interval.  The right side must carry the imbalance.

A boundary terminal bridge gives:

```text
z_m + Y_s = 0.
```

Since `Z` itself is zero:

```text
z_1+...+z_{m-1} = -z_m = Y_s.
```

Therefore:

```text
sum(z_1...z_{m-1}) = sum(Y_s).
```

This is an equal-sum relation between the prefix of `Z` and a right external block.

That is an internal-external pair trap.

## Lemma S18.1: boundary right terminal gives internal-external equal-sum

Assume

```text
R = Z q Y,
sum(Z)=0,
z_m + Y_s = 0.
```

Then

```text
sum(z_1...z_{m-1}) = Y_s.
```

### Proof

From `sum(Z)=0`,

```text
sum(z_1...z_{m-1}) = -z_m.
```

From the terminal bridge,

```text
Y_s = -z_m.
```

Therefore the two sums are equal. ∎

## Consequence

Boundary one-sided terminal is not purely terminal. It is an internal-external equal-sum relation.

This should route to the distributed bridge branch after a block exchange between:

```text
A = z_1...z_{m-1},
B = Y_s.
```

If the exchange is blocked, the blocker is external/distributed by construction.

## Interior one-sided terminal

Now assume

```text
R = U r Z q Y,
```

with both adjacent outside atoms:

```text
r on the left,
q on the right.
```

The right terminal bridge is:

```text
z_m + Y_s = 0.
```

If the left q-through-Z analysis has no terminal bridge and no clean descent, then by the existing classification it must produce one of:

```text
SIGNED_INTERVAL,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
MIXED.
```

If it produces signed interval, S07/S10 reduce it to pair/distributed/external.
If it produces distributed bridge, we are done with this branch.
If it produces ordinary external bridge, persistence should refine it into terminal or distributed.

Thus true interior one-sided terminal can persist only if the opposite side is ordinary external in a way not yet classified.

## Lemma S18.2: interior one-sided terminal reduces to opposite-side obstruction

Let `Z` be interior. Suppose the right side is long-terminal blocked and no clean descent exists.

If the left side is not terminal-blocked, then the left-side q-through-Z attempts must produce a nonterminal obstruction:

```text
SIGNED_INTERVAL,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
MIXED.
```

The signed branch routes to S07/S10. The distributed branch routes to the distributed-bridge proof. The remaining branch is ordinary external bridge.

### Status

This is a structural reduction.  It says one-sided terminal is not independently hard unless ordinary external bridge remains hard.

## Long-support internal structure

Because the terminal support is long:

```text
s >= m-1.
```

The external block `W=y_1...y_s` has at least as many atoms as `Z` without one endpoint.

Its total sum equals:

```text
sum(W)=sum(z_1...z_{m-1}).
```

Therefore the two sequences

```text
z_1...z_{m-1}
```

and

```text
y_1...y_s
```

have the same sum, with `|W| >= |Z|-1`.

This is a large equal-sum block relation.

## Lemma S18.3: long terminal support gives large equal-sum block

A right long terminal bridge always gives:

```text
sum(z_1...z_{m-1}) = sum(Y_s),
|Y_s| >= m-1.
```

### Proof

Same as S18.1, plus the long condition. ∎

## Attack move: equal-sum exchange with endpoint-deleted Z

Let

```text
A = z_1...z_{m-1},
B = Y_s.
```

Then

```text
sum(A)=sum(B).
```

Consider exchanging `A` and `B` while keeping the endpoint atom `z_m` controlled.

Original local structure:

```text
A z_m q B Y_r
```

Possible exchange:

```text
B z_m q A Y_r
```

or a more local endpoint absorption:

```text
z_m B
```

which is zero.

Because `sum(A)=sum(B)`, swapping `A` and `B` preserves the endpoint after the combined window.  This is exactly the same mechanism as pair-trap disjoint equal-sum exchange, but one block is external.

## Candidate theorem S18.4: one-sided long terminal exchange theorem

Let `R` be `D_short`-minimal and suppose a right one-sided long terminal bridge exists:

```text
sum(A)=sum(B),
A=z_1...z_{m-1},
B=Y_s,
|B|>=|A|.
```

Then exchanging `A` and `B` gives one of:

```text
1. D_short descent;
2. signed interval obstruction;
3. pair trap obstruction;
4. distributed bridge obstruction;
5. terminal bridge with strictly larger consumed support;
6. boundary exhaustion.
```

If case 5 repeats, support length strictly increases until boundary exhaustion or overlap.  Therefore the process cannot continue indefinitely.

## Why this is promising

One-sided long terminal looked hard because one terminal blocker can block every insertion depth.

But the long terminal equality is stronger than a blocker:

```text
sum(z_1...z_{m-1}) = sum(Y_s).
```

So it exposes a large equal-sum exchange opportunity.

This may bypass the terminal degeneracy entirely.

## Required computation next

Test the exchange move:

```text
A z_m q B -> B z_m q A
```

for one-sided long terminal hard records.

We need to know whether it usually:

```text
1. decreases D_short;
2. creates distributed bridge;
3. creates signed/pair trap;
4. remains neutral but increases support;
5. fails due to boundary issues.
```

## Next script target

Add:

```text
scripts/test_one_sided_terminal_exchange.py
```

Input:

```text
logs/external_bridge_hard_terminal_lengths_p17.jsonl
logs/external_bridge_hard_terminal_lengths_p23.jsonl
```

For each right-only or left-only long terminal record:

```text
1. find terminal support metadata;
2. construct A=z_1...z_{m-1} and B=external support;
3. swap A and B if disjoint and valid;
4. compare D_short;
5. classify new collisions.
```

## Status

```text
Dominant hard branch: one-sided long terminal.
Core insight: long terminal gives large equal-sum exchange A=z_1...z_{m-1} with B=external support.
Next validation: test one-sided terminal exchange.
```
