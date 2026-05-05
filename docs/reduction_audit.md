# Reduction audit for Erdos 475

This note tracks the remaining bridge between the verified finite complement package and a possible complete solution of Erdos Problem 475.

## Notation

```text
A subset F_p^*
B = F_p^* \ A
|B| = p - 1 - |A|
t = |A|
```

## Verified finite domain

The currently verified finite complement domain is:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

This domain is covered by two computational proof styles:

```text
1. Main three-branch descent certificate:
   p = 29, |B| = 3..7
   p = 31, |B| = 3..6

2. Direct witness / summary-only witness verification:
   p = 17, |B| = 3
   p = 19, |B| = 3..5
   p = 23, |B| = 3..9
   p = 29, |B| = 8..15
   p = 31, |B| = 7..17
```

## Direct witness supplement: small-prime residue

A direct witness supplement has been generated and independently checked for:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
```

Verification status:

```text
small_prime_residue_witness_traces_full.jsonl
records = 50508
failures = 0
VERDICT: PASS
```

Per-case record counts:

```text
p=17 |B|=3: 35
p=19 |B|=3: 46
p=19 |B|=4: 172
p=19 |B|=5: 476
p=23 |B|=3: 70
p=23 |B|=4: 201
p=23 |B|=5: 1197
p=23 |B|=6: 3399
p=23 |B|=7: 7752
p=23 |B|=8: 14550
p=23 |B|=9: 22610
```

This supplement is a direct witness trace, not the same three-branch descent certificate used for the original p=29 and p=31 certified cases.

## Direct witness supplement: p = 29 medium residue

The following p=29 medium-residue classes have been generated as direct witness JSONL files and verified by `verify_erdos475_trace_semantics.py`.

```text
p=29 |B|=8:  111041 records, failures=0, VERDICT: PASS
p=29 |B|=9:  246675 records, failures=0, VERDICT: PASS
p=29 |B|=10: 468754 records, failures=0, VERDICT: PASS
p=29 |B|=11: 766935 records, failures=0, VERDICT: PASS
p=29 |B|=12: 1086601 records, failures=0, VERDICT: PASS
p=29 |B|=13: 1337220 records, failures=0, VERDICT: PASS
p=29 |B|=14: 1432860 records, failures=0, VERDICT: PASS
p=29 |B|=15: 1337220 records, failures=0, VERDICT: PASS
```

Thus p=29 is verified for:

```text
|B| = 3..15
```

where |B|=3..7 is covered by the main descent certificate and |B|=8..15 is covered by direct witnesses.

## Direct witness supplement: p = 31 medium residue

The following p=31 medium-residue classes have been generated as direct witness JSONL files and verified by `verify_erdos475_trace_semantics.py`.

```text
p=31 |B|=7:  67860 records, failures=0, VERDICT: PASS
p=31 |B|=8:  195143 records, failures=0, VERDICT: PASS
p=31 |B|=9:  476913 records, failures=0, VERDICT: PASS
p=31 |B|=10: 1001603 records, failures=0, VERDICT: PASS
p=31 |B|=11: 1820910 records, failures=0, VERDICT: PASS
p=31 |B|=12: 2883289 records, failures=0, VERDICT: PASS
p=31 |B|=13: 3991995 records, failures=0, VERDICT: PASS
p=31 |B|=14: 4847637 records, failures=0, VERDICT: PASS
p=31 |B|=15: 5170604 records, failures=0, VERDICT: PASS
p=31 |B|=16: 4847637 records, failures=0, VERDICT: PASS
```

The final class was run in summary-only mode to avoid writing another multi-GB JSONL file.

```text
p=31 |B|=17
processed = 3991995
solved = 3991995
failed = 0
VERDICT: PASS
class_sha256 = e1aa6a80e90560084d5538867d396d03057d1b777cde2e20dd7bcdebf4b4e2cb
aggregate_sha256 = e1aa6a80e90560084d5538867d396d03057d1b777cde2e20dd7bcdebf4b4e2cb
elapsed_seconds = 42409.89
```

Thus p=31 is verified for:

```text
|B| = 3..17
```

where |B|=3..6 is covered by the main descent certificate and |B|=7..17 is covered by direct or summary-only witnesses.

## Internal finite proof status for main descent certificate

The main finite certificate is organized into three descent mechanisms.

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
Do the known analytic reductions leave only cases contained in the verified finite domain?
```

That verified finite domain is:

```text
p = 17, |B| = 3
p = 19, |B| = 3..5
p = 23, |B| = 3..9
p = 29, |B| = 3..15
p = 31, |B| = 3..17
```

If yes, then the finite package plus the witness supplements likely complete the remaining finite check.

If no, any additional residue cases must be listed explicitly and then certified or eliminated analytically.

## Known range ledger

Fill this table from the published sources.

| Source | Covered range | Translation | Status |
|---|---|---|---|
| Small-set theorem | t <= 12 | direct small original set size | known covered |
| Very-large-set theorem | p - 3 <= t <= p - 1 | |B| <= 2 | known covered |
| Verified finite domain | p=17,19,23,29,31 ranges listed above | complement finite residue | verified PASS |
| Sufficiently-large-prime theorem | TBD | TBD | needs audit |
| Public finite-check residue | TBD | TBD | needs audit |

## Exact audit procedure

For each prime `p` not covered automatically by sufficiently-large-prime results:

1. list all possible `t = |A|`, with `1 <= t <= p - 1`;
2. remove ranges covered by published theorems;
3. translate remaining `t` into complement size `|B| = p - 1 - t`;
4. quotient by multiplicative scaling if needed;
5. compare the residue with the verified finite domain.

## Target outcome

The strongest possible outcome is:

```text
finite residue is contained in verified domain
```

If the audit finds additional residue cases, they should be listed explicitly as:

```text
p = ?, |B| = ?
```

and then certified or eliminated analytically.

## Current status

Main p=29/p=31 descent certificate: stable.

Small-prime witness supplement: verified for 50508 records.

p=29 medium-residue direct witnesses: verified for |B|=8..15.

p=31 medium-residue direct witnesses: verified for |B|=7..16.

p=31, |B|=17 summary-only witness verification: PASS with SHA256 digest.

External reduction audit: not complete.
