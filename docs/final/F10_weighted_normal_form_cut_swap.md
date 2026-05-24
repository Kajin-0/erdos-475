# F10 weighted normal form and fixed cut-swap theorem

This file continues the final-proof extraction phase begun with F11.

F10 supplies the weighted local input used by F11.  It extracts the weighted normal-form reductions and the fixed proper cut-swap table from the A-notes, mainly:

```text
A56  weighted normal forms and transported-prefix tests
A58  nested zero-composite rewrite
A60  original cut-swap table
A95  external collision hardening
A97  weighted cut-swap displayed collision table hardening
```

This file is an extracted draft, not yet the final manuscript version.  The remaining risks are sign/endpoint audit and normal-form exhaustiveness.

---

## F10.0. Scope

F10 does not prove weighted cut-selection.  That is F11.

F10 proves the following local statement:

```text
Given a genuine weighted core A+2B+C=0 and a chosen proper cut B=P R,
the fixed cut-swap A P R C -> A R P C has all displayed collisions routed into known classes.
```

Thus, once a cut is chosen, there is no new obstruction species outside the final state machine.

---

## F10.1. Weighted relation and easy reductions

Let the displayed segment be

```text
X A B C Y
```

with block sums

```text
a=sum(A),
b=sum(B),
c=sum(C).
```

A weighted relation is

```text
a+2b+c=0.
```

The relation is nongenuine if any of the following holds:

```text
b=0,
a+b=0,
b+c=0,
a=c,
transported-prefix/tail rewrite applies.
```

The relation is genuine if none of these reductions holds.

---

## Lemma F10.1: easy weighted reductions exit to non-weighted classes

If a weighted relation

```text
A+2B+C=0
```

satisfies one of the easy reduction conditions, then it routes to one of:

```text
zero collapse,
two-piece zero-composite,
equal interval,
midpoint/adjacent-equal branch,
transported-prefix normal form.
```

### Extracted proof

If `B=0`, then the nonempty middle block is a zero interval, or the endpoint-empty case collapses immediately.

If `A+B=0`, then the adjacent block `A B` is a zero interval or zero-composite branch.  Similarly, `B+C=0` gives a right adjacent zero branch.

If `A=C`, then the outer blocks have equal sum.  If they are adjacent through zero gap after contraction, the branch is midpoint/adjacent-equal; if separated, it is an equal-interval or separated-equal branch.

If a transported-prefix/tail rewrite applies, the apparent coefficient-2 structure is rewritten as a zero-composite or ordinary signed-interval relation using the containing block.  This is the A56 transported-prefix normalization.

Each output is non-weighted and exits to F4--F9. ∎

### Audit flags

```text
A56 transported-prefix exhaustiveness remains a key audit item.
The final manuscript should state the transported-prefix/tail hypotheses explicitly.
```

---

## F10.2. Nested zero-composite representation

A genuine weighted relation satisfies

```text
a+2b+c=0.
```

Since

```text
sum(A B C)=a+b+c,
```

the weighted relation can be rewritten as

```text
sum(A B C)+b=0.
```

Thus the whole displayed block plus the middle block forms a nested zero-composite relation.

---

## Lemma F10.2: weighted core is a nested zero-composite

Every weighted relation

```text
A+2B+C=0
```

is equivalent to

```text
ABC+B=0.
```

### Proof

The sum of `ABC` is `a+b+c`.  Adding `b` gives `a+2b+c`, which is zero by hypothesis. ∎

### Use

This identity explains why weighted cores are connected to zero-composite machinery, but it does not by itself eliminate the weighted core.  Static cuts of `B` are insufficient; the proof uses the dynamic cut-swap below.

---

## F10.3. Proper cut-swap setup

Assume the weighted core is genuine and

```text
|B|>=2.
```

Choose a proper cut

```text
B=P R,
P,R nonempty.
```

Write

```text
p=sum(P),
r=sum(R),
b=p+r.
```

The fixed cut-swap is

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

Only the `R_k'` and `P_j'` families are moved.  New displayed collisions must involve at least one moved family.

---

## F10.5. Displayed collision classification

## Lemma F10.3: displayed collisions of the fixed cut-swap are classified

For the fixed cut-swap

```text
A P R C -> A R P C,
```

every displayed collision in the transformed window is one of:

```text
zero-composite,
two-piece zero,
equal/separated interval,
signed interval / transported-prefix candidate,
weighted-core return through signed boundary relation,
forbidden recurrence,
endpoint zero-collapse.
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

Comparisons of moved endpoint values with old moved-family positions give signed boundary relations:

```text
R_k = P_j,
r+P_j-p-R_k=0.
```

These are equal/signed interval relations.  If all easy reductions fail and a coefficient-2 pattern survives, the branch may return to weighted-core form.  This is the only displayed weighted-return channel.

If the transformed ordering is Graham-valid but recurrent, the new forbidden hit must occur in a moved family:

```text
x+a+R_k=f,
x+a+r+P_j=f.
```

These are recurrence branches routed by F7.

Thus every displayed collision or recurrence is classified. ∎

### Audit flags

```text
Endpoint/full-prefix cases should be included in an appendix table.
Signs in the moved-P versus old-R relation must be checked line by line.
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

The cut-swap is a local replacement of the window `W=A P R C` by `W'=A R P C` inside `X W Y`, preserving the window total.  Therefore A95/F6 applies to any collision with an endpoint in `X`, `Y`, or a wrapped external family. ∎

---

## F10.7. Fixed cut-swap theorem

## Theorem F10.5: fixed weighted cut-swap theorem

Let

```text
A+2B+C=0
```

be a genuine weighted core with `|B|>=2`, and choose a proper cut

```text
B=P R.
```

The cut-swap

```text
A P R C -> A R P C
```

has exactly the following outcomes:

```text
1. success;
2. displayed collision routed by Lemma F10.3;
3. external collision routed by Lemma F10.4;
4. forbidden recurrence routed by F7;
5. weighted-core return through a signed boundary relation.
```

No new obstruction class appears.

### Proof

After the cut-swap, the transformed ordering is either Graham-valid and avoids `f`, non-Graham, or Graham-valid and recurrent.

If it is Graham-valid and avoids `f`, this is success.

If it is non-Graham, the collision is either displayed or external.  Displayed collisions are Lemma F10.3; external collisions are Lemma F10.4.

If it is Graham-valid but recurrent, new forbidden hits occur only in moved endpoint families and route by F7.

The only weighted-core return channel is the signed boundary channel isolated in Lemma F10.3. ∎

---

## F10.8. Interface with F11

F10 gives F11 the following exact input:

```text
For any chosen proper cut B=P R,
the cut-swap is controlled unless it returns to weighted core through the signed boundary channel.
```

F11 then handles the selection/termination problem:

```text
either some cut exits or descends,
or all cuts are weakly cut-rigid,
and weak cut-rigidity reduces to pattern-rigidity or routed descent.
```

---

## F10.9. Remaining risks

Before final manuscript status:

```text
R1. Expand transported-prefix/tail normal-form hypotheses from A56.
R2. Verify endpoint cases in the collision table.
R3. Verify sign conventions in signed boundary relations.
R4. Ensure every recurrence call points to the extracted F7 recurrence theorem.
R5. Ensure every external collision call points to extracted F6.
```

---

## F10.10. Extraction status

```text
Status: extracted draft.
Risk: ORANGE.
Next recommended extraction: F6 external collision theorem or F7 recurrence routing theorem.
```
