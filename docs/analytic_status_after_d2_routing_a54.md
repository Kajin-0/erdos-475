# Analytic status after D2 routing A54

This note updates the proof-status map after A52 and A53.

A52 handled the balanced D2 range

```text
m=k
```

and A53 handled the long-prefix D2 range

```text
m>k.
```

Together with A40, this means every D2 range is now routed either to strict support descent or to zero-composite surgery plus the global A34 recurrence obligation.

No complete proof is claimed here.  The main remaining obstruction is still global recurrence.

---

## 1. D2 status after A40, A52, A53

Recall D2 from separated equal-interval direct exchange:

```text
D2: C_k = 2a + g + Y_m
```

where

```text
sum(A)=sum(C)=a,
sum(G)=g.
```

Write

```text
C=K L,
Y=M N,
```

where

```text
K=prefix_k(C),
L=tail_k(C),
M=prefix_m(Y).
```

D2 is equivalent to

```text
sum(A G L M)=0.
```

That is:

```text
A G tail_k(C) prefix_m(Y)
```

is a zero composite.

---

## 2. Complete D2 range table

| Range | Result | Status |
|---|---|---|
| `m<k` | support drops by `k-m` | strict support descent by A40 |
| `m=k` | support-neutral zero composite | controlled modulo A34 by A52 |
| `m>k` | support increases by `m-k`, but canonical cut avoids Q2 boundary | controlled modulo A34 by A53 |

Thus D2 is no longer a standalone hard residual.

Status:

```text
D2: CONTROLLED MODULO A34
```

---

## 3. Separated equal-interval direct exchange after D2 routing

The direct exchange branch

```text
X A G C Y -> X C G A Y
```

has collision families:

```text
D1: C_k = a + G_j
D2: C_k = 2a + g + Y_m
D3: A_i = G_j - g
D4: A_i = a + Y_m
D5: C_k = a + g + A_i
```

Current status:

| Branch | Status |
|---|---|
| D1 | equal-interval descent / zero collapse |
| D2 | strict descent or zero-composite controlled modulo A34 |
| D3 | two-piece zero / zero collapse |
| D4 | two-piece zero / zero collapse |
| D5 | strict-span three-piece zero or two-piece endpoint branch |

Therefore the direct-exchange collision side is locally routed.

---

## 4. Separated equal-interval gap-after side

The gap-after move

```text
X A G C Y -> X A C G Y
```

has collision equations:

```text
E1: C_k = A_i - a
E2: C_k = a + g + Y_m
E3: G_j = A_i - 2a
E4: G_j = g + Y_m
E5: C_k = a + G_j
```

A49 routed them as:

| Equation | Status |
|---|---|
| E1 | two-piece zero |
| E2 | three-piece zero |
| E3 | three-piece zero |
| E4 | two-piece zero |
| E5 | equal-interval descent |

Therefore the gap-after collision side is locally routed.

---

## 5. Separated equal branch conclusion

After A36--A54, the separated equal-interval branch has the following status:

```text
collision obstructions: locally routed;
forbidden-hit obstructions: A34 recurrence;
midpoint boundary: separate zero-gap boundary.
```

More explicitly:

```text
Separated equal intervals are controlled modulo A34 recurrence and midpoint-boundary analysis.
```

The branch no longer contains unclassified local D1--D5 or E1--E5 collision obstructions.

---

## 6. Updated global obligations

The current remaining obligations are:

### O1. A34 global recurrence theorem

This is the largest remaining proof obligation.

Needed for:

```text
forbidden-hit recurrences from atom insertion;
forbidden-hit recurrences from separated equal surgery;
long-prefix transformed-order landings;
any transformed Graham-valid ordering whose first f-hit is not earlier.
```

### O2. Midpoint boundary

The midpoint branch is

```text
2S_y=S_x+S_v.
```

A36 identified it as the zero-gap boundary of separated equal intervals.  It remains to route this boundary into either:

```text
zero-composite surgery,
pair trap,
equal-interval descent,
A34 recurrence.
```

### O3. General weighted signed overlap/nesting

A20 produced weighted signed relations of the form

```text
sum(A)+2sum(B)+sum(C)=0.
```

Several apparent weighted branches have since been routed to composite-zero classes.  The remaining task is to determine whether any genuine weighted signed residual remains after applying transported-prefix rewrites similar to A38 and A49.

---

## 7. Recommended A55 target

The next best local target is the midpoint boundary.

Reason:

1. D2 is now routed modulo A34.
2. Gap-after collision routing is closed locally.
3. Midpoint is a clean zero-gap boundary of separated equal intervals.
4. It may route to the same zero-composite or pair-insertion framework with fewer moving parts than the general weighted branch.

Suggested A55 setup:

```text
X A C Y,
sum(A)=sum(C)=a.
```

The midpoint identity is:

```text
2S_y=S_x+S_v.
```

Equivalently:

```text
sum(A)=sum(C).
```

with no gap between `A` and `C`.

Analyze the moves:

```text
X A C Y -> X C A Y,
X A C q Y -> X A q C Y,
X A C Y -> X A' C' Y after cutting A or C.
```

Expected routes:

```text
old collision,
prefix/interior zero,
pair trap,
smaller separated equal interval,
A34 recurrence.
```

---

## Bottom line

After A54, separated equal-interval collision surgery is locally organized.  The remaining proof is increasingly concentrated around two themes:

```text
1. global recurrence descent;
2. boundary cases: midpoint and genuine weighted signed relations.
```
