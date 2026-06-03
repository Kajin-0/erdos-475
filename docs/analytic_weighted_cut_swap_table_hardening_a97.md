# Analytic weighted cut-swap table hardening A97

This note continues from A96.

A93 isolated five hardening obligations:

```text
U1. Strict progress lemma.
U2. Universal external-collision classification.
U3. Recurrence bounded-blocker measure.
U4. Cut-swap displayed collision table.
U5. Bridge/gap measure inequalities.
```

A94 addressed U1. A95 addressed U2. A96 addressed U3. A97 addresses U4 by hardening the A60 weighted cut-swap displayed collision table.

This patched version incorporates:

```text
docs/analytic_a97_signed_boundary_weighted_return_audit.md
```

The main correction is that the A97.8 signed boundary equation simplifies exactly to an equal-tail relation:

```text
R_k^+ = P_j^+.
```

Thus an isolated signed-boundary collision is non-weighted. A genuine same-length weighted return can only arise from persistent signed-boundary rigidity across cuts, which is the A90--A94 weak-to-pattern-rigid branch.

---

## 1. Standing weighted core

Let the original displayed segment be:

```text
X A P R C Y
```

where:

```text
B=P R,
P,R nonempty.
```

Write block sums:

```text
a=sum(A),
p=sum(P),
r=sum(R),
c=sum(C),
b=p+r.
```

The genuine weighted core is:

```text
a+2b+c=0,
```

or equivalently:

```text
a+2p+2r+c=0.
```

The cut-swap is:

```text
X A P R C Y -> X A R P C Y.
```

Let:

```text
x=sum(X).
```

The total displayed segment sum is preserved:

```text
sum(A P R C)=sum(A R P C)=a+p+r+c.
```

---

## 2. Endpoint families

In the original order `A P R C`, displayed internal endpoint families are:

```text
A_i:         x + A_i,
P_j:         x + a + P_j,
R_k:         x + a + p + R_k,
C_l:         x + a + p + r + C_l.
```

In the transformed order `A R P C`, displayed endpoint families are:

```text
A_i:         x + A_i,                       unchanged
R_k':        x + a + R_k,
P_j':        x + a + r + P_j,
C_l':        x + a + r + p + C_l,           same as x+a+p+r+C_l.
```

Only collisions involving a moved `R_k'` or moved `P_j'` need to be displayed. Collisions entirely within `A`, `P`, `R`, or `C` are inherited from the original Graham-valid ordering.

---

## 3. Direct displayed collision table

| Collision | Equation | Tail form | Class |
|---|---|---|---|
| `R_k' = A_i` | `a+R_k-A_i=0` | `A_i^+ + R_k=0` | zero-composite |
| `R_k' = C_l'` | `R_k=p+r+C_l` | `P+R_k^+ + C_l=0` | zero-composite |
| `R_k' = P_j'` | `R_k-r-P_j=0` | `P_j+R_k^+=0` | two-piece zero |
| `P_j' = A_i` | `a+r+P_j-A_i=0` | `A_i^+ + R + P_j=0` | zero-composite |
| `P_j' = C_l'` | `P_j=p+C_l` | `P_j^+ + C_l=0` | two-piece zero |
| `P_j' = R_k'` | same as `R_k'=P_j'` | `P_j+R_k^+=0` | two-piece zero |

Endpoint cases route to zero-collapse, lower-piece zero-composite, or boundary branches. No direct displayed collision with `A` or `C` produces a genuine weighted core.

---

## 4. Pullback comparisons with old moved-family positions

The transformed moved families may also be compared with old endpoint values that occur in proof pullbacks.

The two important comparisons are:

```text
x+a+R_k       vs old x+a+P_j,
x+a+r+P_j    vs old x+a+p+R_k.
```

These are not necessarily collisions inside the final transformed ordering unless the old endpoint value is also present as an unchanged endpoint. They appear in signed-boundary and self-return calculations.

---

## Lemma A97.7: moved `R` against old `P` gives equal-prefix relation

If:

```text
x+a+R_k = x+a+P_j,
```

then:

```text
R_k=P_j.
```

This is an equal-prefix relation between prefixes of `R` and `P`.

Classification:

```text
equal interval,
separated-equal inside B,
midpoint/equal interval after uncrossing,
zero-composite if adjacent/overlapping degenerates.
```

It is non-weighted.

---

## Lemma A97.8: moved `P` against old `R` gives equal-tail relation

If:

```text
x+a+r+P_j = x+a+p+R_k,
```

then:

```text
r+P_j-p-R_k=0.
```

Write:

```text
P=P_j P_j^+,
R=R_k R_k^+.
```

Thus:

```text
p=P_j+P_j^+,
r=R_k+R_k^+.
```

Substitute into the signed boundary equation:

```text
(R_k+R_k^+) + P_j - (P_j+P_j^+) - R_k = 0.
```

Cancelling equal terms gives:

```text
R_k^+ - P_j^+ = 0,
```

hence:

```text
R_k^+ = P_j^+.
```

### Classification

This is an equal-tail relation between a suffix of `R` and a suffix of `P`.

It routes to:

```text
EQUAL_INTERVAL,
SEPARATED_EQUAL,
ZERO_COLLAPSE,
PROPER_SUBINTERVAL,
BRIDGE_GAP if separated by a nonempty gap,
F5/F8/F9 machinery.
```

A single A97.8 equation is therefore non-weighted. It does not by itself produce a genuine weighted-core return.

A genuine same-length weighted return can only arise if compatible equal-prefix/equal-tail relations persist across cuts, producing weak cut-rigidity. That persistent branch is handled by:

```text
A90--A94 weak-to-pattern-rigid reduction,
A89 strong exact self-return impossibility.
```

### Endpoint cases

If `P_j=P`, then `P_j^+=empty` and the equation gives:

```text
R_k^+=0.
```

If `R_k^+` is nonempty, this is a zero-sum suffix of `R`; if it is empty, the comparison is the full-boundary tautology.

If `R_k=R`, then `R_k^+=empty` and the equation gives:

```text
P_j^+=0.
```

If `P_j^+` is nonempty, this is a zero-sum suffix of `P`; if empty, the comparison is again full-boundary tautology.

If both tails are nonempty, `R_k^+=P_j^+` is a proper equal-tail relation supported strictly inside `B`.

---

## 5. Forbidden-hit equations for the cut-swap

If the transformed ordering is Graham-valid but recurrent, the new forbidden hit must occur in a moved family:

```text
H_R(k): x+a+R_k=f,
H_P(j): x+a+r+P_j=f.
```

The unchanged `A` and `C` families cannot create new forbidden hits unless they already hit `f` before the move.

## Lemma A97.9: cut-swap recurrence is moved-prefix recurrence

Every new forbidden hit from the cut-swap is a moved-prefix hit of type `H_R` or `H_P`.

Classification:

```text
A64 bounded-blocker theorem;
A69 pair-swap / moved-prefix recurrence if atom-level;
A70 singleton-prefix recurrence;
A71 cyclic recurrence if the cut is interpreted cyclically;
A95 external collision if the blocker is external.
```

Proof: only `R_k'` and `P_j'` moved. Therefore only those endpoint families can newly hit `f`. ∎

---

## 6. Weighted-core return equations

A displayed collision table can return to a weighted relation only if the collision equation contains a surviving coefficient-2 structure after zero-composite, equal-tail, and transported-prefix tests fail.

The direct displayed collisions A97.1--A97.6 produce zero-composite branches. A97.7 produces equal-prefix branches. A97.8 produces equal-tail branches.

Therefore an isolated displayed collision does not create a new weighted core. Weighted return means a persistent rigidity pattern across cuts, not a single displayed equation.

---

## Lemma A97.10: weighted return requires persistent signed-boundary rigidity

A genuine same-length weighted-core return after cut-swap can only occur if signed-boundary equal-prefix/equal-tail relations persist across proper cuts in a way that prevents all cut-swaps from producing success, collapse, smaller middle, or non-weighted descent.

That is precisely the weak cut-rigid branch treated by A90--A94, with final contradiction supplied by A89 if the return becomes pattern-rigid/strong exact.

### Proof

Direct transformed-family collisions are zero-composite by Section 3. Pullback comparison A97.7 is equal-prefix. Pullback comparison A97.8 is equal-tail. Each isolated relation is non-weighted. A weighted same-middle return must therefore preserve a coherent doubled-middle pattern across the cut rather than arise from one displayed collision. This is the definition of the weak cut-rigid return branch. ∎

---

## 7. Displayed collision table summary

| Collision | Equation | Class |
|---|---|---|
| `R_k' = A_i` | `A_i^+ + R_k = 0` | zero-composite |
| `R_k' = C_l'` | `P + R_k^+ + C_l = 0` | zero-composite |
| `R_k' = P_j'` | `P_j + R_k^+ = 0` | two-piece zero |
| `P_j' = A_i` | `A_i^+ + R + P_j = 0` | zero-composite |
| `P_j' = C_l'` | `P_j^+ + C_l = 0` | two-piece zero |
| `P_j' = R_k'` | `P_j + R_k^+ = 0` | two-piece zero |
| moved `R` vs old `P` | `R_k=P_j` | equal prefix / separated-equal |
| moved `P` vs old `R` | `R_k^+=P_j^+` | equal tail / separated-equal |
| moved family hits `f` | `x+a+R_k=f` or `x+a+r+P_j=f` | recurrence |
| persistent cut rigidity | all cuts fail to descend | A90--A94 / A89 |

---

## 8. Endpoint and empty-block cases

The cut requires:

```text
P,R nonempty.
```

Prefixes such as `P_j`, `R_k`, `A_i`, `C_l` may be proper nonempty prefixes, full prefixes, or empty only if boundary endpoint comparisons are explicitly added.

Endpoint cases route as follows:

```text
empty prefix causing equation 0=atom/block sum -> zero collapse or boundary branch;
full prefix causing tail empty -> lower-piece zero-composite;
full-boundary tautology -> no nontrivial obstruction;
A or C empty -> endpoint weighted case, handled by A80/A81 or A56.
```

No endpoint case creates a new transition type.

---

## 9. Hardened A60 theorem

## Theorem A97.11: weighted cut-swap displayed collisions are classified

For the weighted cut-swap:

```text
A P R C -> A R P C,
```

with `P,R` nonempty, every displayed collision or pullback comparison in the transformed window is one of:

```text
1. zero-composite;
2. two-piece zero;
3. equal-prefix/equal-tail interval;
4. separated-equal / bridge-gap;
5. signed interval / transported-prefix candidate;
6. forbidden recurrence;
7. endpoint zero-collapse;
8. persistent cut-rigid weighted-return branch A90--A94/A89.
```

External collisions are not part of the displayed table and are handled by A95.

### Proof

The transformed moved endpoint families are `R_k'` and `P_j'`. Collisions involving these families with displayed `A`, `C`, and each other are Section 3. Pullback comparisons with old moved-family positions are A97.7--A97.8. New forbidden hits are A97.9. Persistent same-middle weighted returns are restricted by A97.10. Endpoint cases are Section 8. ∎

---

## 10. Consequence for weighted proof

A97 hardens U4 at the displayed-table level:

```text
A60 cut-swap displayed collisions introduce no new obstruction species.
```

The previous phrase:

```text
weighted-core return through signed boundary relation
```

should now be read as:

```text
persistent signed-boundary rigidity across cuts,
not an isolated A97.8 equation.
```

An isolated A97.8 equation is the non-weighted equal-tail relation:

```text
R_k^+ = P_j^+.
```

---

## 11. Current status after A97 patch

Proved/recorded here:

```text
1. displayed endpoint families for A P R C -> A R P C;
2. all moved-family collision equations;
3. zero-composite classification for direct displayed collisions;
4. A97.7 equal-prefix relation;
5. A97.8 equal-tail relation R_k^+=P_j^+;
6. cut-swap recurrence equations;
7. endpoint/empty-block handling;
8. persistent signed-boundary weighted return reduced to A90--A94/A89.
```

Still open:

```text
1. A56 transported-prefix/tail exhaustiveness;
2. persistent cut-rigidity formalization in final F11;
3. W-to-NW exit decrease/no-reentry table;
4. final mutual-induction implementation in F9/F11.
```
