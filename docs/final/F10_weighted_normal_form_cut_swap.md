# F10 weighted normal form and fixed cut-swap theorem

This file continues the final-proof extraction phase begun with F11.

F10 supplies the weighted local input used by F11. It extracts the weighted normal-form reductions and the fixed proper cut-swap table from the A-notes, mainly:

```text
A56  weighted normal forms and transported-prefix tests
A58  nested zero-composite rewrite
A60  original cut-swap table
A95  external collision hardening
A97  weighted cut-swap displayed collision table hardening
```

Recent audit checkpoints:

```text
docs/analytic_a56_transported_prefix_tail_exhaustiveness_audit.md
docs/analytic_a97_signed_boundary_weighted_return_audit.md
docs/analytic_weighted_cut_swap_table_hardening_a97.md
docs/analytic_f9_f11_mutual_induction_convention.md
```

This file is an extracted draft, not yet the final manuscript version. The old broad risks “transported-prefix exhaustiveness” and “signed-boundary weighted return” are now narrowed:

```text
transported-prefix/tail requires a containing-block certificate;
isolated A97 signed-boundary equations are non-weighted equal-prefix/equal-tail exits;
only persistent signed-boundary rigidity across cuts remains a weighted-return issue.
```

---

## F10.0. Scope

F10 does not prove weighted cut-selection. That is F11.

F10 proves the following local statement:

```text
Given a genuine weighted core A+2B+C=0 and a chosen proper cut B=P R,
the fixed cut-swap A P R C -> A R P C has all displayed collisions routed into known classes.
```

Thus, once a cut is chosen, there is no new obstruction species outside the final state machine.

---

## F10.1. Weighted relation and easy reductions

Let the displayed segment be:

```text
X A B C Y
```

with block sums:

```text
a=sum(A),
b=sum(B),
c=sum(C).
```

A weighted relation is:

```text
a+2b+c=0.
```

The relation is nongenuine if any of the following holds:

```text
b=0,
a+b=0,
b+c=0,
a=c,
transported-prefix/tail rewrite applies with a containing-block certificate.
```

The relation is genuine if none of these reductions holds.

---

## Lemma F10.1: easy weighted reductions exit to non-weighted classes

If a weighted relation:

```text
A+2B+C=0
```

satisfies one of the easy reduction conditions, then it routes to one of:

```text
zero collapse,
two-piece zero-composite,
equal interval,
midpoint/adjacent-equal branch,
transported-prefix/tail non-weighted normal form.
```

### Extracted proof

If `B=0`, then the nonempty middle block is a zero interval, or the endpoint-empty case collapses immediately.

If `A+B=0`, then the adjacent block `A B` is a zero interval or zero-composite branch. Similarly, `B+C=0` gives a right adjacent zero branch.

If `A=C`, then the outer blocks have equal sum. If they are adjacent through zero gap after contraction, the branch is midpoint/adjacent-equal; if separated, it is an equal-interval or separated-equal branch.

If a transported-prefix/tail rewrite applies, then there is a containing-block certificate of one of the forms:

```text
D = B A,
D = B C,
D = A B,
D = C B,
```

where `D` is a known transported/containing block from the local move and the complementary piece occurs with coefficient `+1` in the displayed relation. Then one copy of `B` is absorbed into `D`, rewriting the apparent coefficient-2 relation as a non-weighted zero-composite/equal/signed relation.

Each output is non-weighted and exits to F4--F9 under the F9/F11 mutual-induction interface. ∎

### Audit status

```text
A56 transported-prefix/tail exhaustiveness is clarified in analytic_a56_transported_prefix_tail_exhaustiveness_audit.md.
Final manuscript must include the containing-block certificate criterion, not a bare transported-prefix Boolean.
```

---

## F10.2. Nested zero-composite representation

A genuine weighted relation satisfies:

```text
a+2b+c=0.
```

Since:

```text
sum(A B C)=a+b+c,
```

the weighted relation can be rewritten as:

```text
sum(A B C)+b=0.
```

Thus the whole displayed block plus the middle block forms a nested zero-composite relation.

---

## Lemma F10.2: weighted core is a nested zero-composite

Every weighted relation:

```text
A+2B+C=0
```

is equivalent to:

```text
ABC+B=0.
```

### Proof

The sum of `ABC` is `a+b+c`. Adding `b` gives `a+2b+c`, which is zero by hypothesis. ∎

### Use

This identity explains why weighted cores are connected to zero-composite machinery, but it does not by itself eliminate the weighted core. Static cuts of `B` are insufficient; the proof uses the dynamic cut-swap below.

---

## F10.3. Proper cut-swap setup

Assume the weighted core is genuine and:

```text
|B|>=2.
```

Choose a proper cut:

```text
B=P R,
P,R nonempty.
```

Write:

```text
p=sum(P),
r=sum(R),
b=p+r.
```

The fixed cut-swap is:

```text
X A P R C Y -> X A R P C Y.
```

The displayed segment sum is preserved.

---

## F10.4. Endpoint families before and after cut-swap

Before the cut-swap `A P R C`, displayed endpoint families are:

```text
A_i:  x+A_i,
P_j:  x+a+P_j,
R_k:  x+a+p+R_k,
C_l:  x+a+p+r+C_l.
```

After the cut-swap `A R P C`, displayed endpoint families are:

```text
A_i:   x+A_i,                  unchanged,
R_k':  x+a+R_k,
P_j':  x+a+r+P_j,
C_l':  x+a+r+p+C_l,            unchanged as C-family endpoint values.
```

Only the `R_k'` and `P_j'` families are moved. New displayed collisions must involve at least one moved family.

---

## F10.5. Displayed collision classification

## Lemma F10.3: displayed collisions of the fixed cut-swap are classified

For the fixed cut-swap:

```text
A P R C -> A R P C,
```

every displayed collision in the transformed window is one of:

```text
zero-composite,
two-piece zero,
equal-prefix/equal-tail interval,
separated-equal / bridge-gap,
signed interval / transported-prefix candidate,
forbidden recurrence,
endpoint zero-collapse,
persistent cut-rigid weighted-return branch.
```

External collisions are handled separately by F6.

### Extracted proof

The moved endpoint families are `R_k'` and `P_j'`.

The direct displayed collisions are:

```text
R_k' = A_i    -> A_i^+ + R_k = 0,
R_k' = C_l'   -> P + R_k^+ + C_l = 0,
R_k' = P_j'   -> P_j + R_k^+ = 0,
P_j' = A_i    -> A_i^+ + R + P_j = 0,
P_j' = C_l'   -> P_j^+ + C_l = 0,
P_j' = R_k'   -> P_j + R_k^+ = 0.
```

These are zero-composite or two-piece zero branches, with endpoint cases becoming zero-collapse or lower-piece zero-composite branches.

Comparisons of moved endpoint values with old moved-family positions give boundary relations:

```text
moved R against old P:  R_k = P_j,
moved P against old R:  r + P_j - p - R_k = 0.
```

Using:

```text
P = P_j P_j^+,
R = R_k R_k^+,
p = P_j + P_j^+,
r = R_k + R_k^+,
```

the second relation simplifies to:

```text
R_k^+ = P_j^+.
```

Thus isolated signed-boundary comparisons are equal-prefix/equal-tail non-weighted relations. They route to equal-interval, separated-equal, bridge-gap, zero-collapse, or F5/F8/F9 machinery.

A genuine same-middle weighted return can only come from persistent equal-prefix/equal-tail rigidity across cuts, i.e. the weak cut-rigid branch treated by F11/A90--A94/A89.

If the transformed ordering is Graham-valid but recurrent, the new forbidden hit must occur in a moved family:

```text
x+a+R_k=f,
x+a+r+P_j=f.
```

These are recurrence branches routed by F7.

Thus every displayed collision or recurrence is classified. ∎

### Audit status

```text
A97 signed-boundary algebra is audited in analytic_a97_signed_boundary_weighted_return_audit.md.
Endpoint/full-prefix cases are tabulated in analytic_weighted_cut_swap_table_hardening_a97.md.
Only persistent signed-boundary rigidity across cuts remains a weighted-return issue.
```

---

## F10.6. External collision theorem hook

## Lemma F10.4: cut-swap external collisions exit to F6

If the cut-swap creates a collision between a moved endpoint and an endpoint outside the displayed transformed window, then the collision is an external collision in the sense of F6/A95.

It routes to one of:

```text
bridge zero-composite,
signed bridge composite,
equal/separated interval,
transported-prefix relation,
pair-difference boundary,
cyclic-cut branch,
singleton/prefix recurrence,
weighted-core normal form,
collapse/minimality contradiction.
```

### Proof

The cut-swap is a local replacement of the window `W=A P R C` by `W'=A R P C` inside `X W Y`, preserving the window total. Therefore A95/F6 applies to any collision with an endpoint in `X`, `Y`, or a wrapped external family. ∎

---

## F10.7. Fixed cut-swap theorem

## Theorem F10.5: fixed weighted cut-swap theorem

Let:

```text
A+2B+C=0
```

be a genuine weighted core with `|B|>=2`, and choose a proper cut:

```text
B=P R.
```

The cut-swap:

```text
A P R C -> A R P C
```

has exactly the following outcomes:

```text
1. success;
2. displayed collision routed by Lemma F10.3;
3. external collision routed by Lemma F10.4;
4. forbidden recurrence routed by F7;
5. persistent cut-rigid weighted-return branch.
```

No new obstruction class appears.

### Proof

After the cut-swap, the transformed ordering is either Graham-valid and avoids `f`, non-Graham, or Graham-valid and recurrent.

If it is Graham-valid and avoids `f`, this is success.

If it is non-Graham, the collision is either displayed or external. Displayed collisions are Lemma F10.3; external collisions are Lemma F10.4.

If it is Graham-valid but recurrent, new forbidden hits occur only in moved endpoint families and route by F7.

Isolated boundary relations are equal-prefix/equal-tail non-weighted exits. The only remaining same-middle weighted continuation is persistent cut-rigidity across proper cuts, handled by F11. ∎

---

## F10.8. Interface with F11

F10 gives F11 the following exact input:

```text
For any chosen proper cut B=P R,
the cut-swap is controlled unless all relevant cuts persist in a weak cut-rigid weighted-return pattern.
```

F11 then handles the selection/termination problem:

```text
either some cut exits or descends under the mutual-induction interface,
or all cuts are weakly cut-rigid,
and weak cut-rigidity reduces to pattern-rigidity or routed descent.
```

---

## F10.9. Remaining risks

Before final manuscript status:

```text
R1. Include the A56 containing-block certificate criterion in final normal-form statement.
R2. Ensure every recurrence call points to the extracted F7 recurrence theorem.
R3. Ensure every external collision call points to extracted F6.
R4. W-to-NW exit decrease table is now created and should be cited in final manuscript.
R5. Delegate persistent cut-rigidity exactly to F11/A90--A94/A89.
```

Resolved or reduced:

```text
A56 transported-prefix/tail exhaustiveness -> analytic_a56_transported_prefix_tail_exhaustiveness_audit.md.
A97 signed-boundary algebra -> analytic_a97_signed_boundary_weighted_return_audit.md.
A97 endpoint/full-prefix table -> analytic_weighted_cut_swap_table_hardening_a97.md.
W-to-NW exit decrease table -> docs/analytic_weighted_to_nonweighted_exit_decrease_table.md.
All 19+2 W-to-NW exit types enumerated and decrease certified relative to NW_0.
```

---

## F10.10. Extraction status

```text
Status: extracted draft patched with A56/A97 audit citations and W-to-NW table reference.
Risk: YELLOW/ORANGE.
Main remaining dependency: F11 weak cut-rigidity closure (A90--A94/A89 formalization).
Resolved: W-to-NW exit decrease/no-reentry table exists at
  docs/analytic_weighted_to_nonweighted_exit_decrease_table.md.
Next recommended extraction: F11 weak cut-rigidity formalization or F9 edge-by-edge rank table.
```
