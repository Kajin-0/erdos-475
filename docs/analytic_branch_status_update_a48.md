# Analytic branch status update A48

This note updates the branch-status map after A36--A47.

The major change is that the atom-balanced D2 boundary

```text
k=m=1
```

is no longer treated as a standalone hard local residual.  A46 identified it as a zero-composite branch, and A47 integrated it with the A28--A33 atom-insertion machinery.

The proof is still not complete.  The main remaining global bottleneck is still the A34 recurrence theorem.

---

## 1. Separated equal-interval branch after A36--A48

The separated equal interval branch starts with

```text
X A G C Y,
sum(A)=sum(C)=a.
```

The direct exchange

```text
X A G C Y -> X C G A Y
```

has five collision branches:

```text
D1: C_k = a + G_j
D2: C_k = 2a + g + Y_m
D3: A_i = G_j - g
D4: A_i = a + Y_m
D5: C_k = a + g + A_i
```

Current routing:

| Branch | Current status | Source |
|---|---|---|
| D1 | equal-interval descent / zero collapse | A37 |
| D2, `m<k` | strict support descent | A40 |
| D2, `m=k=1` | atom-balanced zero-composite, controlled modulo A34 | A46--A47 |
| D2, `m=k>=2` | balanced transfer / difference-walk residual | A41--A43 |
| D2, `m>k` | long-prefix recurrence | A40/A34 |
| D3 | two-piece zero / zero collapse | A36 |
| D4 | two-piece zero / zero collapse | A36 |
| D5 | strict-span three-piece zero or two-piece endpoint branch | A38 |

---

## 2. Atom-balanced D2 status

The atom-balanced D2 boundary is:

```text
k=m=1,
C=cL,
Y=yN,
c=2a+g+y.
```

A46 proves:

```text
sum(A G L y)=0.
```

A47 then exposes the zero block

```text
Z=A G L y
```

and inserts the outside atom `c` into a canonical cut

```text
P=A G,
Q=L y.
```

If `L` is nonempty, then

```text
|Q|>=2,
```

so the bad Q2 single-atom boundary from A31--A33 is avoided.  Therefore all non-forbidden-hit obstruction branches are controlled by the atom-insertion descent framework.

If `L` is empty, atom-balanced D2 is already a lower-piece composite-zero branch.

Thus:

```text
atom-balanced D2 -> composite-zero descent + A34 recurrence.
```

Status:

```text
CONTROLLED MODULO A34
```

---

## 3. Balanced D2 with k=m>=2

A41 rewrote balanced D2 as a paired difference walk

```text
D_r=sum(c_1,...,c_r)-sum(y_1,...,y_r)
```

with

```text
D_0=0,
D_k=2a+g.
```

Descending subcases:

```text
intermediate D_r=0       -> smaller separated equal interval
intermediate D_r=2a+g   -> shorter balanced transfer
repeated D_r=D_s         -> smaller separated equal interval
zero increment           -> impossible by atom distinctness
```

A42 and A43 showed that the remaining injective endpoint-avoiding difference-walk condition is locally realizable.  A44 and A45 showed that even stronger local separated-equal constraints can still have survivors, especially at `k=1`.

After A47, the `k=1` boundary is controlled modulo A34.  The proper balanced case

```text
k=m>=2
```

remains unresolved.

Status:

```text
HARD RESIDUAL / NEEDS GLOBAL STRUCTURE
```

---

## 4. Long-prefix D2 with m>k

A40 proved that D2 is support descent iff

```text
m<k.
```

The non-descending long-prefix range is

```text
m>k.
```

This is structurally similar to the long-prefix forbidden recurrence branches in A34.

Status:

```text
RECURRENCE WITH MEASURE OBLIGATION
```

Needed:

```text
show long-prefix transfer decreases a global measure after applying A5/A34 recurrence machinery.
```

---

## 5. Gap-after move branch

A36 also introduced the gap-after move

```text
X A G C Y -> X A C G Y.
```

Collision equations:

```text
C_k=A_i-a,
C_k=a+g+Y_m,
G_j=A_i-2a,
G_j=g+Y_m,
C_k=a+G_j.
```

These have not yet received the same full routing treatment as the direct-exchange D1--D5 branches.

Status:

```text
OPEN ROUTING TASK
```

Suggested target:

```text
A49: gap-after obstruction routing table.
```

---

## 6. Weighted signed overlap/nesting branch

A20 introduced weighted signed residuals such as

```text
sum(A)+2sum(B)+sum(C)=0.
```

Some branches previously suspected to be weighted, such as D5 proper-interior, have now been routed to composite-zero descent by A38.

However, the general weighted signed branch from signed interval overlap/nesting remains open.

Status:

```text
HARD RESIDUAL
```

Needed:

```text
separate genuine weighted branches from transported-prefix artifacts,
then test whether each routes to composite-zero or midpoint structure.
```

---

## 7. Midpoint branch

Midpoint branch:

```text
2S_y=S_x+S_v.
```

A36 identified it as the zero-gap boundary of separated equal intervals.

Status:

```text
HARD RESIDUAL / BOUNDARY OF SEPARATED EQUAL
```

Needed:

```text
atom-level adjacent equal-block analysis,
or embed midpoint into separated-equal surgery via a small artificial gap.
```

---

## 8. Current global proof obligations

The current proof program is reduced to the following major obligations.

### G1. A34 global recurrence theorem

Prove that every recurrence branch produces a new active obstruction with strictly smaller global measure.

This is currently the largest bottleneck.

### G2. Proper balanced D2 for k=m>=2

Use global separated-equal structure beyond local difference-walk constraints.

### G3. Long-prefix D2 for m>k

Control by A34 recurrence or prove a direct long-prefix descent.

### G4. Gap-after move routing

Route all A36.5 gap-after obstruction equations into known classes.

### G5. General weighted signed overlap/nesting

Separate transported-prefix artifacts from genuinely hard coefficient-2 branches.

### G6. Midpoint boundary

Eliminate or route adjacent equal-interval midpoint branches.

---

## 9. Recommended A49

The next most mechanical step is:

```text
A49: gap-after obstruction routing table
```

Given the equations

```text
C_k=A_i-a,
C_k=a+g+Y_m,
G_j=A_i-2a,
G_j=g+Y_m,
C_k=a+G_j,
```

rewrite each as one of:

```text
equal-interval descent,
two-piece zero,
three-piece zero,
weighted signed,
zero collapse,
forbidden recurrence.
```

This may eliminate another apparently hard branch by routing it into composite-zero machinery, as happened with D5.

---

## Bottom line

After A47, atom-balanced D2 is controlled modulo global recurrence.  The proof is still incomplete, but the local obstruction tree is increasingly concentrated around a small set of global obligations rather than many unrelated local cases.
