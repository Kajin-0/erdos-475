# F11 weighted cut-selection and termination extraction

This file begins the final-proof extraction phase recommended in A100.

F11 is the highest-risk extracted lemma because it closes the weighted obstruction branch.  The purpose of this file is to convert the A-note proof program into a compact final-proof lemma, while preserving every dependency and every remaining audit flag.

This is not yet the final publishable proof.  It is the first extracted draft of the weighted-core theorem.

---

## F11.0. Dependency summary

F11 depends on the following hardened A-notes.

```text
A56  weighted normal forms and transported-prefix reductions
A58  nested zero-composite rewrite
A60  original fixed cut-swap table
A79  weighted cut-selection refinement
A80  atom-middle weighted core
A81  endpoint-rigid atom-middle trap
A89  strong exact internal cyclic self-return hardening
A90  weak cut-rigid to pattern-rigid diagnostic
A91  first-changed-endpoint lemma
A92  finite return-path formalization
A93  state-machine coverage
A94  strict progress lemma
A95  external collision hardening
A96  bounded-blocker recurrence hardening
A97  weighted cut-swap displayed collision table hardening
A98  bridge/gap measure hardening
A99  recurrence span-convention audit
```

F11 exits into the following later final lemmas:

```text
F6  external collision theorem
F7  recurrence routing theorem
F8  bridge/gap descent theorem
F9  non-weighted termination theorem
F10 weighted normal form and fixed cut-swap theorem
```

---

## F11.1. Weighted core setup

Let the active displayed segment of a Graham-valid ordering be

```text
X A B C Y
```

with block sums

```text
a=sum(A),
b=sum(B),
c=sum(C).
```

A weighted core is a relation

```text
a+2b+c=0.
```

A weighted core is genuine if all easy weighted reductions fail:

```text
b != 0,
a+b != 0,
b+c != 0,
a != c,
no transported-prefix/tail rewrite applies.
```

These hypotheses are inherited from A56.

The weighted measure is

```text
M_W=(|B|, M_NW^*)
```

with lexicographic order, where `M_NW^*` is the non-weighted global measure used in F9/A78.

---

## F11.2. Statement of weighted cut-selection theorem

## Theorem F11.1: weighted core termination theorem

Assume the weighted normal-form lemmas A56, the fixed cut-swap table A97, the recurrence and external-collision routing lemmas A95--A99, and the non-weighted termination theorem F9.

Then no genuine weighted core can generate an infinite non-descending obstruction path.

Equivalently, every genuine weighted core either:

```text
1. exits by an A56 easy reduction;
2. exits to a non-weighted obstruction handled by F9;
3. collapses;
4. succeeds;
5. or returns to a genuine weighted core with strictly smaller middle length |B|.
```

Therefore weighted obstruction paths terminate by induction on `|B|`.

---

## F11.3. Atom-middle base case

The base case is

```text
|B|=1.
```

Write

```text
B=q
```

where `q` is a single atom.  The weighted relation is

```text
a+2q+c=0.
```

Since there is no nonempty proper cut of `B`, the cut-swap method cannot apply.  A80--A81 handle this case.

## Lemma F11.2: atom-middle weighted cores exit to non-weighted machinery

Every genuine atom-middle weighted core

```text
A+2q+C=0
```

routes to one of:

```text
1. A56 easy reduction;
2. zero collapse;
3. pair-difference boundary;
4. equal/signed interval;
5. midpoint or singleton recurrence;
6. non-weighted obstruction handled by F9.
```

### Extracted proof

Attempt adjacent swaps of `q` with the nearest atom on the right and on the left, when those atoms exist.

The right swap has local form

```text
A q gamma C^+ -> A gamma q C^+.
```

The left swap has local form

```text
A^- alpha q C -> A^- q alpha C.
```

Displayed collisions from either adjacent swap produce atom-difference equations of the form

```text
q-alpha+P=0,
alpha-q+P=0,
gamma-q+P=0,
q-gamma+P=0,
P=0,
```

where `P` is a local prefix or tail.  These are pair-difference, zero-composite, equal/signed interval, or zero-collapse branches.  If the transformed ordering is Graham-valid but recurrent, A5 produces singleton-prefix or pair-difference recurrence, routed by F7.

The only remaining rigid atom-middle case is the endpoint-rigid trap.  Writing

```text
A=A^- alpha,
C=gamma C^+,
```

the canonical endpoint-trap equations are

```text
q-alpha=a,
gamma-q=c.
```

Substitution into

```text
a+2q+c=0
```

gives

```text
alpha-gamma=2q.
```

Thus the apparent weighted obstruction compresses to a boundary triple relation on

```text
alpha,q,gamma.
```

The sign-reversed and mixed sign endpoint conventions similarly compress to bounded boundary-atom relations.  These are non-weighted branches, handled by F9 after routing through F4--F8.

Thus the atom-middle case cannot remain as a genuine weighted obstruction. ∎

### Audit flags

```text
A81 sign-pattern algebra must be checked line by line.
Endpoint-empty cases A=empty or C=empty must be explicitly included in the final manuscript.
```

---

## F11.4. Proper-middle cut-swap

Assume now

```text
|B|>=2.
```

Choose a proper cut

```text
B=P R,
P,R nonempty.
```

The weighted cut-swap is

```text
A P R C -> A R P C.
```

A97 hardens the displayed collision table for this move.

## Lemma F11.3: fixed cut-swap exits unless it returns to weighted core

For any proper cut `B=P R`, the cut-swap produces one of:

```text
1. success;
2. displayed collision routed to zero-composite/equal/signed interval/pair-difference;
3. external collision routed by F6/A95;
4. recurrence routed by F7/A96/A99;
5. weighted-core return through a signed boundary relation.
```

No other obstruction species is produced.

### Extracted proof

The transformed endpoint families in

```text
A R P C
```

are

```text
A_i:   x+A_i,
R_k':  x+a+R_k,
P_j':  x+a+r+P_j,
C_l':  x+a+r+p+C_l.
```

A97 compares all moved families against displayed families.  Direct moved-family collisions yield zero-composite or equal/signed interval equations, for example:

```text
R_k'=A_i     -> A_i^+ + R_k=0,
R_k'=C_l'    -> P+R_k^+ + C_l=0,
R_k'=P_j'    -> P_j+R_k^+=0,
P_j'=A_i     -> A_i^+ + R+P_j=0,
P_j'=C_l'    -> P_j^+ + C_l=0.
```

Forbidden hits can occur only in moved families:

```text
x+a+R_k=f,
x+a+r+P_j=f.
```

These are recurrence branches routed by F7.  External collisions are routed by F6.  The only possible weighted-core return comes from signed boundary relations comparing old and new cut-boundary data. ∎

### Audit flags

```text
A97 endpoint/full-prefix cases must be included in appendix collision table.
The signed boundary channel must be explicitly tied to A56 normal forms.
```

---

## F11.5. Smaller weighted return

Suppose the cut-swap returns to a genuine weighted core.  If the new doubled middle block is contained in either `P` or `R`, then its length is strictly smaller than `|B|`.

## Lemma F11.4: side-contained weighted returns descend

If a weighted return after the cut `B=P R` has doubled middle contained in `P` or contained in `R`, then

```text
|B_new|<|B|.
```

### Proof

Both `P` and `R` are nonempty proper subblocks of `B`, so

```text
|P|<|B|,
|R|<|B|.
```

Any middle contained in one side has length strictly less than `|B|`. ∎

---

## F11.6. Weak cut-rigidity

If no cut produces success, collapse, non-weighted exit, or smaller middle, the core is weakly cut-rigid.

## Definition F11.5: weak cut-rigid weighted core

A genuine weighted core with `|B|>=2` is weakly cut-rigid if for every proper cut `B=P R`, the cut-swap return, when it returns to weighted core, has doubled middle length at least `|B|` and no routed exit has terminated the branch.

A79--A82 show that weak cut-rigidity forces returned middles to cross every internal cut of `B`, hence to contain all of `B`, unless the branch routes out.

---

## F11.7. Pattern-rigidity reduction

A90--A94 refine weak cut-rigidity.  Weak cut-rigidity alone does not imply that the internal endpoint set of `B` is preserved.  The proof therefore uses the state-machine and first-changed-endpoint machinery.

## Lemma F11.6: weak cut-rigid return is pattern-rigid or routed

Assume the A92 finite return-path model and the A94 strict progress lemma.  A weak cut-rigid weighted self-return either:

```text
1. is pattern-rigid;
2. produces a non-weighted obstruction handled by F9;
3. produces an A56 easy reduction;
4. returns to a smaller weighted middle;
5. collapses;
6. contradicts minimality of the chosen self-return path.
```

### Extracted proof

If the return is not pattern-rigid, then one of the following changes:

```text
middle support,
outer blocks,
internal endpoint set,
boundary endpoints,
endpoint labels.
```

Changes of middle support are containment/overlap/disjointness cases and route to smaller middle, bridge/equal interval, or external-collision machinery.  Changes of outer blocks subtract two weighted equations and expose a non-weighted zero/equal relation.  Changes of boundary endpoints expose A56 transported-prefix or adjacent zero/equal relations.

If the internal endpoint set changes, take the first changed endpoint along the finite return path.  A91 shows it creates a routed obstruction, smaller weighted middle, recurrence, external collision, or unobstructed progress.  A94 rules out unobstructed first changes in a minimal non-descending self-return.  Therefore endpoint-set changes are routed or descending.

If endpoint values are preserved but labels change, subtracting the two interval representations gives a zero/equal/pair-difference or recurrence branch.

Thus any non-pattern return is routed or descending. ∎

### Audit flags

```text
This is the highest-risk extraction step.
The final manuscript must define pattern-rigid precisely and avoid informal “invisible self-return” language.
A94's remove-change/undo minimality argument must be written as a formal minimal-path lemma.
```

---

## F11.8. Pattern-rigid impossibility

Pattern-rigid return preserves the same middle support, boundary endpoints, and internal endpoint set of `B`.  It is therefore strong enough for the A89 internal cyclic self-return argument.

## Lemma F11.7: pattern-rigid self-return is impossible

A genuine weighted core cannot have a pattern-rigid self-return at a proper cut of `B`.

### Proof

Pattern-rigidity implies strong exact internal cyclic self-return in the sense of A89.  For a cut after internal partial sum `T_k`, strong exactness gives

```text
E_B - T_k = E_B.
```

If `T_k=0`, then `B` has an internal zero-prefix, a contradiction to Graham-validity.  If `T_k != 0`, the nonzero translation by `-T_k` preserves `E_B`.  Since the additive group of `F_p` has prime order, this forces

```text
E_B=F_p.
```

Then `|E_B|=p`, so `|B|=p-1`.  Since the full ordering is a subset of `F_p^*`, no atoms remain outside `B`, so `A=C=empty`.  The weighted relation becomes

```text
2b=0.
```

For odd `p`, this gives `b=0`, hence `B` is a zero-sum block.  That contradicts the genuine weighted-core assumption.

Thus pattern-rigid self-return is impossible. ∎

### Audit flags

```text
The final proof must state p odd here.
The p=2 case is handled separately in F13/A86.
```

---

## F11.9. Weighted induction

## Lemma F11.8: weighted descent terminates

Any sequence of weighted-core returns with strictly decreasing middle length terminates.

### Proof

The middle length `|B|` is a positive integer.  A strictly decreasing sequence of positive integers is finite. ∎

---

## F11.10. Proof of Theorem F11.1

Let a genuine weighted core be given.

If `|B|=1`, Lemma F11.2 routes it out of the genuine weighted class.

If `|B|>=2`, choose a proper cut `B=P R`.  By Lemma F11.3, the cut-swap either succeeds, collapses, exits to non-weighted machinery, enters recurrence/external collision machinery, or returns to a weighted core.

If it returns to a weighted core with smaller middle, Lemma F11.8 applies by induction.

If no cut gives smaller middle or routed exit, the core is weakly cut-rigid.  By Lemma F11.6, the weakly cut-rigid return is either pattern-rigid or routed/descending.  Pattern-rigid return is impossible by Lemma F11.7.  Routed/descending alternatives terminate by F9, F6--F8, A56, or weighted induction.

Therefore every weighted core path exits, collapses, succeeds, or descends in `|B|`.  No infinite non-descending weighted path exists. ∎

---

## F11.11. Remaining extraction risks

Before this lemma can be treated as final, the following must be audited.

```text
R1. A81 sign-pattern algebra for atom-middle endpoint traps.
R2. A97 endpoint/full-prefix cases in the cut-swap table.
R3. A90--A94 pattern-rigidity reduction, especially the minimal self-return path argument.
R4. Explicit exits from weighted branches to final lemmas F6--F9.
R5. Odd-characteristic assumptions wherever division by 2 is used.
```

---

## F11.12. Current extraction status

```text
Status: extracted draft, not final.
Risk: RED -> ORANGE if R1--R5 are resolved.
Next recommended extraction: F10 weighted normal form and cut-swap theorem, or harden R3 directly.
```
