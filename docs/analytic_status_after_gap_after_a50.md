# Analytic status after gap-after routing A50

This note updates the proof-status map after A49.

A49 routed the gap-after collision equations from the separated equal-interval branch.  The routing result is important because the gap-after move had been one of the remaining local routing tasks after A48.

The status after A49 is:

```text
Gap-after collision routing: closed locally.
Gap-after forbidden-hit recurrences: still depend on A34.
```

No complete proof is claimed here.

---

## 1. What A49 closed

For the separated equal-interval setup

```text
X A G C Y,
sum(A)=sum(C)=a,
sum(G)=g,
```

the gap-after move is

```text
X A G C Y -> X A C G Y.
```

A36 gave five collision equations:

```text
E1: C_k = A_i - a
E2: C_k = a + g + Y_m
E3: G_j = A_i - 2a
E4: G_j = g + Y_m
E5: C_k = a + G_j
```

A49 routed them as:

| Equation | Routed form | Status |
|---|---|---|
| `C_k=A_i-a` | `prefix(C)+tail(A)=0` | two-piece zero |
| `C_k=a+g+Y_m` | `G+tail(C)+prefix(Y)=0` | three-piece zero |
| `G_j=A_i-2a` | `C+tail(A)+prefix(G)=0` | three-piece zero |
| `G_j=g+Y_m` | `tail(G)+prefix(Y)=0` | two-piece zero |
| `C_k=a+G_j` | `A+prefix(G)=prefix(C)` | equal-interval descent |

Thus the gap-after collision side adds no new obstruction type.

---

## 2. Remaining gap-after issue

The gap-after move also has forbidden-hit equations:

```text
x+a+C_k=f,
x+2a+G_j=f.
```

These are not collision equations.  They are transformed-order forbidden landings.

Status:

```text
A34 recurrence obligation
```

If the resulting forbidden hit is earlier than the original minimal forbidden hit, it is eliminated by minimality.  If not, it re-enters the A5 local-blocker framework and requires the global recurrence measure.

---

## 3. Updated separated-equal branch status

The separated-equal branch now has the following status.

### Direct exchange side

The direct exchange

```text
X A G C Y -> X C G A Y
```

has collision branches D1--D5.

Current status:

| Branch | Status |
|---|---|
| D1 | equal-interval descent / zero collapse |
| D2, `m<k` | strict support descent |
| D2, `m=k=1` | atom-balanced zero-composite, controlled modulo A34 |
| D2, `m=k>=2` | proper balanced transfer residual |
| D2, `m>k` | long-prefix recurrence / A34 obligation |
| D3 | two-piece zero / zero collapse |
| D4 | two-piece zero / zero collapse |
| D5 | strict-span three-piece zero or two-piece endpoint branch |

### Gap-after side

All collision branches E1--E5 route to:

```text
two-piece zero,
three-piece zero,
equal-interval descent,
zero collapse.
```

Only forbidden-hit recurrences remain.

---

## 4. Current open proof obligations

After A49, the open obligations are more concentrated.

### O1. A34 global recurrence theorem

This is the largest global bottleneck.

Required statement:

```text
Every transformed-order forbidden recurrence either gives an earlier forbidden hit
or produces a new active obstruction with strictly smaller global measure.
```

This is needed for:

```text
A31 H1/H2,
A33 pair-difference recurrence,
A36/A49 separated-equal forbidden recurrences,
long-prefix D2 branches,
other transformed-order forbidden landings.
```

### O2. Proper balanced D2 with `k=m>=2`

A41 reduced this branch to a paired difference walk.  A42/A43 showed the local difference-walk conditions alone are insufficient.  A44/A45 strengthened the local model and found survivors, especially at `k=1`.  A47 controlled the `k=1` atom-balanced boundary modulo A34.

The remaining balanced case is therefore:

```text
k=m>=2.
```

It likely requires global structure beyond local A,G,C,Y algebra.

### O3. Long-prefix D2 with `m>k`

A40 showed D2 is strict support descent iff `m<k`.  The long-prefix range

```text
m>k
```

is a recurrence branch.  It likely belongs to A34 but may admit a direct long-prefix compression lemma.

### O4. General weighted signed overlap/nesting

A20 produced weighted signed relations such as

```text
sum(A)+2sum(B)+sum(C)=0.
```

Several apparent weighted branches, including D5, have since been routed to composite-zero classes.  The remaining task is to identify which weighted signed branches are genuine and which are transported-prefix artifacts.

### O5. Midpoint branch

The midpoint branch is

```text
2S_y=S_x+S_v.
```

A36 identified it as the zero-gap boundary of separated equal intervals.  It still needs an atom-level boundary analysis or a reduction into the separated-equal surgery framework.

---

## 5. Suggested A51 target

The next highest-value local target is:

```text
proper balanced D2 with k=m>=2.
```

Reason:

1. `m<k` is strict descent by A40.
2. `m=k=1` is controlled modulo A34 by A46--A47.
3. `m>k` is clearly a long-prefix recurrence.
4. Therefore the only balanced D2 case not yet routed is `k=m>=2`.

A51 should focus on the first nontrivial proper case:

```text
k=m=2.
```

Suggested structure:

```text
K=(c_1,c_2),
M=(y_1,y_2),
D_1=c_1-y_1,
D_2=c_1+c_2-y_1-y_2=2a+g.
```

The A41 residual conditions require:

```text
D_1 notin {0, 2a+g}.
```

Analyze how the absence of D1/D3/D4/D5 and the separated equal identity constrain `D_1`.

Expected outcomes:

```text
smaller equal interval,
atom-balanced D2 subcase,
two-piece zero,
A34 recurrence,
or a rigid pair-difference trap.
```

---

## Current status

Closed locally by A49:

```text
gap-after collision routing.
```

Still open:

```text
A34 recurrence theorem,
proper balanced D2 k=m>=2,
long-prefix D2,
general weighted signed branches,
midpoint boundary.
```
