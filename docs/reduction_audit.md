# Reduction audit for Erdos 475

This note tracks the remaining bridge between the certified finite complement package and a possible complete solution of Erdos Problem 475.

## Certified finite domain

The current repository certifies the following complement cases, where

```text
B = F_p^* \ A
```

Certified cases:

```text
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

Equivalently, in the original set-size variable `t = |A|`:

```text
p = 29, t = 21..25
p = 31, t = 24..27
```

## Internal finite proof status

The finite certificate is organized into three descent mechanisms.

### 1. Non-atomic branch

Condition:

```text
E >= 2 and not (P = 2 and max multiplicity = 2)
```

Verified status:

```text
101385 total rows
101384 multmax_halo4_len1 rows
1 multmax_halo4_len2 row
0 unresolved rows
```

The unique length-2 exception is:

```text
p = 31
|B| = 6
B = {1, 3, 5, 17, 19, 25}
state = after_1
branch = matching_Pge3
Phi: (3,3,10) -> (1,1,2)
move = (13,2,10)
delta Phi = (-2,-2,-8)
```

### 2. Atomic branch

Condition:

```text
P = 2 and max multiplicity = 2
```

Verified status:

```text
28717 atomic instances
15160 local signatures
14890 single-template signatures
270 high-cover signatures
0 uncovered signatures
all certificate moves have block length 1 or 2
```

Relation classes:

```text
proper_overlap
nested
separated_disjoint
endpoint_adjacent_disjoint
```

Worst high-cover case:

```text
relation = separated_disjoint
spans = 3 5
cover size = 5
moves = (4,2,1);(-1,1,0);(5,1,2);(9,2,6);(9,2,8)
```

### 3. One-collision branch

Condition:

```text
E = P = 1
```

Verified status:

```text
39812 total states
39424 depth-1 states
383 depth-2 states
5 depth-3 states
0 unresolved states
```

Every one-collision state either resolves completely or strictly shortens the collision span `L`:

```text
(1,1,L) -> (0,0,0)
```

or

```text
(1,1,L) -> (1,1,L') with L' < L
```

## Remaining external reduction question

The unresolved global question is:

```text
Do the known analytic reductions leave exactly the certified complement cases
p = 29, |B| = 3..7 and p = 31, |B| = 3..6?
```

If yes, then the finite certificate likely completes the remaining finite check.

If no, the missing residue cases must be added to the trace/certificate pipeline.

## Known range ledger

Fill this table from the published sources.

| Source | Covered range | Translation | Status |
|---|---|---|---|
| Small-set theorem | t <= 12 | direct small original set size | known covered |
| Very-large-set theorem | p - 3 <= t <= p - 1 | |B| <= 2 | known covered |
| Sufficiently-large-prime theorem | TBD | TBD | needs audit |
| Public finite-check residue | TBD | TBD | needs audit |

## Exact audit procedure

For each prime `p` not covered automatically by sufficiently-large-prime results:

1. list all possible `t = |A|`, with `1 <= t <= p - 1`;
2. remove ranges covered by published theorems;
3. translate remaining `t` into complement size `|B| = p - 1 - t`;
4. quotient by multiplicative scaling if needed;
5. compare the residue with the certified domain.

## Target outcome

The strongest possible outcome is:

```text
finite residue = certified domain
```

meaning:

```text
p = 29, |B| = 3..7
p = 31, |B| = 3..6
```

If the audit finds additional residue cases, they should be listed explicitly as:

```text
p = ?, |B| = ?
```

and then certified or eliminated analytically.

## Current status

Internal finite proof: stable.

External reduction audit: not complete.
