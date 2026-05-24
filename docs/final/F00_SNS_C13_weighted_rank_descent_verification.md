# F00.SNS.C13 weighted rank-descent verification

This file continues the strong nonzero-sum repair path.

C11 verified the non-weighted local rows.  C12 verified the external and bridge/gap rows.  The remaining major row from C10 is:

```text
WEIGHTED_REPAIR.
```

C13 verifies the weighted row under SNS collision-defect mode, where:

```text
there is no forbidden endpoint f;
zero intervals are collision defects in ARBITRARY phase;
weighted cut-swap failures are collision pullbacks, not forbidden recurrences.
```

Status: weighted-rank verification draft.

---

## C13.1. Weighted repair setup

Work in ARBITRARY phase.

A weighted repair state has displayed form

```text
X A B C Y
```

with block sums

```text
a=sum(A),
b=sum(B),
c=sum(C),
```

and weighted relation

```text
a+2b+c=0.
```

The weighted measure is subordinate to the global collision profile:

```text
M_w=(|B|,M_loc).
```

Inside the full phase-aware measure:

```text
M_phase=(D_SNS^*,phase_rank,M_loc,M_w,transition_budget),
```

any strict decrease of `D_SNS^*` dominates all weighted data.

---

## C13.2. Nongenuine weighted reductions

A weighted repair state is nongenuine if one of the following holds:

```text
b=0,
a+b=0,
b+c=0,
a=c,
transported-prefix/tail rewrite applies.
```

## Lemma C13.1: nongenuine weighted repair exits to lower-ranked repair

Every nongenuine weighted repair state exits to a lower-ranked non-weighted or transported-prefix repair row:

```text
ZERO_DEFECT,
LOCAL_ZERO_COMPOSITE,
EQUAL_INTERVAL,
SIGNED_INTERVAL,
PAIR_DIFFERENCE,
TRANSPORTED_PREFIX,
BRIDGE_GAP.
```

### Proof

If `b=0`, the middle block is a zero defect.  If `a+b=0` or `b+c=0`, the adjacent union is zero, giving ZERO_DEFECT or LOCAL_ZERO_COMPOSITE.  If `a=c`, the outer blocks give an equal-interval or separated-equal relation.  Transported-prefix/tail cases rewrite the coefficient-2 relation into ordinary zero/equal/signed repair data unless the coefficient-2 core is genuinely independent.  Each target row has type rank lower than WEIGHTED_REPAIR or exits to a verified bridge/local row. ∎

### Measure effect

```text
type_rank decreases from WEIGHTED_REPAIR
```

unless the branch enters BRIDGE_GAP, which C12 verifies.

---

## C13.3. Atom-middle weighted repair

The base case is:

```text
|B|=1,
B=q.
```

The relation is:

```text
a+2q+c=0.
```

There is no proper cut of `B`.

## Lemma C13.2: atom-middle weighted repair exits to local repair

Every genuine atom-middle weighted repair state exits to one of:

```text
ZERO_DEFECT,
SIGNED_INTERVAL,
PAIR_DIFFERENCE,
EQUAL_INTERVAL,
BRIDGE_GAP,
TRANSPORTED_PREFIX,
atom/subset contradiction.
```

### Proof sketch

Attempt adjacent swaps involving the atom `q` and its neighboring boundary atoms when they exist.  In SNS mode, each failed swap creates an endpoint collision, not a forbidden recurrence.  C4 classifies that collision as moved-moved, moved-displayed, or moved-external.  The resulting equations are signed atom-boundary relations such as:

```text
q-alpha+P=0,
alpha-q+P=0,
gamma-q+P=0,
q-gamma+P=0,
P=0.
```

These are signed interval, pair-difference, zero defect, or bridge repair rows verified by C11/C12.

If both adjacent swaps are rigidly blocked, the endpoint-trap equations reduce the apparent weighted relation to a boundary triple relation involving the neighboring atoms and `q`; this is signed/pair repair, not a persistent weighted core. ∎

### Remaining audit

The endpoint-trap sign table from the F11/A81 atom-middle case must be written explicitly.

---

## C13.4. Proper-middle fixed cut-swap

Assume:

```text
|B|>=2,
B=P R,
P,R nonempty.
```

Use the cut-swap:

```text
A P R C -> A R P C.
```

In SNS mode the output is:

```text
collision-free success
or
collision-producing.
```

There is no forbidden-recurrence branch.

## Lemma C13.3: fixed cut-swap outputs are ranked

For a proper cut, the fixed cut-swap either:

```text
1. reaches COLLISION_FREE success;
2. creates displayed collision routed to C11 local rows;
3. creates external collision routed to C12;
4. returns to weighted repair through a signed boundary relation;
5. returns to weighted repair with smaller middle.
```

### Proof

The displayed endpoint families after cut-swap are:

```text
A_i:   x+A_i,
R_k':  x+a+R_k,
P_j':  x+a+r+P_j,
C_l':  x+a+r+p+C_l.
```

All displayed collisions involving moved `R_k'` or `P_j'` are the F10/A97 equations:

```text
R_k'=A_i     -> A_i^+ + R_k=0,
R_k'=C_l'    -> P+R_k^+ + C_l=0,
R_k'=P_j'    -> P_j+R_k^+=0,
P_j'=A_i     -> A_i^+ + R+P_j=0,
P_j'=C_l'    -> P_j^+ + C_l=0,
P_j'=R_k'    -> P_j+R_k^+=0.
```

These route to C11 local rows.  Moved-external collisions route to C12.  The only weighted return channel is the signed boundary relation comparing old and new cut-boundary endpoint data. ∎

---

## C13.5. Smaller-middle descent

## Lemma C13.4: smaller weighted middle decreases M_w

If a weighted repair return has middle block `B_new` satisfying

```text
|B_new|<|B|,
```

and the global defect `D_SNS^*` is fixed, then `M_w` strictly decreases.

### Proof

The first coordinate of `M_w` is `|B|`.  A strict decrease of that positive integer gives lexicographic descent. ∎

---

## C13.6. Side-contained weighted return

If the weighted return after cutting `B=P R` has its new middle contained in `P` or in `R`, then it is smaller.

## Lemma C13.5: side-contained return gives smaller middle

If `B_new subset P` or `B_new subset R`, then:

```text
|B_new|<|B|.
```

### Proof

Both `P` and `R` are nonempty proper subblocks of `B`.  Hence each has length strictly less than `|B|`. ∎

---

## C13.7. Phase-aware weak cut-rigidity

A weighted repair state is phase-aware weak cut-rigid if every proper cut either:

```text
1. returns to weighted repair without decreasing D_SNS^*;
2. returns with middle length at least |B| when D_SNS^* is fixed;
3. does not reach collision-free success;
4. does not exit to a C11/C12 row with descent.
```

This is the only nontrivial case after the fixed cut-swap and smaller-middle alternatives.

## Lemma C13.6: non-weak-rigid weighted repair descends or exits

If a genuine weighted repair state is not phase-aware weak cut-rigid, then some proper cut gives one of:

```text
D_SNS^* descent;
COLLISION_FREE success;
C11 local descent;
C12 external/bridge descent;
smaller weighted middle.
```

### Proof

This is the negation of phase-aware weak cut-rigidity combined with the fixed cut-swap classification Lemma C13.3. ∎

---

## C13.8. Weak cut-rigid reduction

The remaining case is phase-aware weak cut-rigidity.

Use the C7 theorem:

```text
weak cut-rigid -> pattern-rigid or exit.
```

## Lemma C13.7: weak cut-rigid repair reduces to pattern-rigid or ranked exit

Assuming C7.2--C7.4 are hardened, a phase-aware weak cut-rigid weighted repair state either:

```text
1. is phase-aware pattern-rigid;
2. decreases D_SNS^*;
3. exits to C11/C12 phase-aware non-weighted repair;
4. returns to smaller weighted middle;
5. reaches COLLISION_FREE success;
6. contradicts minimal non-descending self-return.
```

### Proof

This is Theorem C7.5.  Pattern changes of support, endpoints, boundary labels, or collision-profile contribution route to the listed exits.  Only full phase-aware pattern-rigidity remains. ∎

### Remaining audit

This imports the three C7 open hardening items:

```text
C7.2 collision-profile change compensation;
C7.3 first changed endpoint in SNS mode;
C7.4 support/boundary/label diagnostics.
```

---

## C13.9. Pattern-rigid exit

## Lemma C13.8: pattern-rigid weighted repair exits genuine weighted state

For odd `p`, a phase-aware pattern-rigid weighted self-return exits genuine weighted repair by producing ZERO_DEFECT or nongenuine weighted reduction.

### Proof

Pattern-rigidity gives internal endpoint-set translation invariance:

```text
E_B-T_k=E_B.
```

If `T_k=0`, the cut prefix is a zero defect.  If `T_k!=0`, translation invariance over the prime additive group forces `E_B=F_p`; then the middle block fills the field endpoint set and the weighted relation reduces to `2b=0`.  Since `p` is odd, `b=0`, a nongenuine weighted reduction to ZERO_DEFECT. ∎

---

## C13.10. Weighted rank-descent theorem

## Theorem C13.9: WEIGHTED_REPAIR row verified conditional on C7 hardening

Assume the C7 weak-to-pattern rigidity hardening lemmas are valid.  Then every WEIGHTED_REPAIR state in ARBITRARY/SNS mode either:

```text
1. exits to a lower-ranked C11 local row by easy reduction;
2. exits to C12 external/bridge row;
3. reaches COLLISION_FREE success;
4. decreases D_SNS^*;
5. decreases |B| in M_w;
6. exits pattern-rigid persistence to ZERO_DEFECT;
7. consumes finite cut-swap transition budget and then falls into one of the above.
```

Thus WEIGHTED_REPAIR cannot support an infinite same-measure branch once C7.2--C7.4 are hardened.

### Proof

If the state is nongenuine, Lemma C13.1 applies.  If `|B|=1`, Lemma C13.2 applies.  If `|B|>=2`, choose a proper cut and apply Lemma C13.3.  Smaller-middle returns descend by Lemmas C13.4--C13.5.  If the state is not weak cut-rigid, Lemma C13.6 applies.  If it is weak cut-rigid, Lemma C13.7 reduces to pattern-rigidity or ranked exit.  Pattern-rigidity exits by Lemma C13.8.  The number of proper cuts and displayed collision comparisons is finite, so the transition budget cannot sustain an infinite loop. ∎

---

## C13.11. What C13 resolves

Resolved:

```text
1. WEIGHTED_REPAIR row has a complete conditional descent structure;
2. easy reductions lower rank;
3. fixed cut-swap table is reusable in SNS mode;
4. smaller middle gives |B| descent;
5. pattern-rigid return exits to ZERO_DEFECT;
6. forbidden recurrence is fully removed from weighted SNS verification.
```

Remaining:

```text
1. C7.2--C7.4 hardening;
2. atom-middle endpoint-trap sign table;
3. explicit finite cut-swap budget table;
4. final integration into C14 global conditional theorem.
```

---

## C13.12. Recommended next file

The next file should assemble C9--C13 into a global conditional termination theorem and isolate the final red items:

```text
docs/final/F00_SNS_C14_global_termination_status.md
```

Goal:

```text
State exactly which lemmas remain before the SNS proof becomes unconditional.
```

---

## C13.13. Status

```text
Status: weighted rank-descent verification draft.
Risk: ORANGE, conditional on C7.2--C7.4.
Remaining red items are now sharply localized.
```
