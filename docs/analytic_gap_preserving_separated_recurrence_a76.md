# Analytic gap-preserving separated recurrence A76

This note continues from A75.

A74 reduced bridge-span monotonicity to equal-span separated bridge returns.  A75 then reduced equal-span separated bridge returns to one specific tie:

```text
gap-preserving separated recurrence.
```

This tie occurs when a separated equal interval

```text
B G U,
sum(B)=sum(U)=a,
G nonempty,
```

uses the gap-after move

```text
B G U -> B U G,
```

and the move is Graham-valid but recurrent, and the A5 blocker pullback recreates a separated-equal bridge with the same enclosing span and same gap length.

This note analyzes the exact form of that tie.  The result is partial: it shows that a gap-preserving return must reuse the old gap endpoints in a rigid way.  Non-rigid returns decrease gap/span or route to midpoint/zero-composite/cyclic recurrence.  The final rigid self-return remains open.

---

## 1. Standing setup

Let the original displayed segment be

```text
X B G U Y
```

with

```text
sum(B)=sum(U)=a,
sum(G)=g,
|G|>0.
```

Let

```text
x=sum(X).
```

Original displayed partial-sum families are

```text
x+B_i,
x+a+G_j,
x+a+g+U_k,
x+2a+g+Y_m.
```

Apply the gap-after move:

```text
X B G U Y -> X B U G Y.
```

Moved displayed partial-sum families are

```text
x+B_i,
x+a+U_k,
x+2a+G_j,
x+2a+g+Y_m.
```

The `B` and post-segment `Y` families are unchanged; the `U` and `G` families move.

---

## 2. Gap-after recurrence equations

A forbidden recurrence after the gap-after move can occur only through a moved family:

```text
H_U: x+a+U_k=f,
H_G: x+2a+G_j=f.
```

The `B` and `Y` families are unchanged from the original ordering; if they hit `f`, this is an old forbidden hit and not a new gap-after recurrence.

---

## Lemma A76.1: gap-after recurrence is either U-hit or G-hit

In the gap-after move `B G U -> B U G`, every new forbidden hit is of type

```text
x+a+U_k=f
```

or

```text
x+2a+G_j=f.
```

### Proof

The only moved families are `U` and `G`.  The unchanged `B` and post-segment families preserve their old partial-sum values. ∎

---

# 3. A5 blocker for a U-hit

Assume the recurrent hit is

```text
x+a+U_k=f.
```

Let

```text
U=K L,
K=prefix_k(U),
L=tail_k(U).
```

Let `l_1` be the first atom of `L`, assuming `L` is nonempty.  If `L` is empty, this is an endpoint branch handled below.

In the moved order

```text
B U G,
```

the hit occurs after

```text
B K.
```

A5 gives a blocker

```text
S'_{H-1}+l_1=S'_{j'}.
```

---

## Lemma A76.2: U-hit left blocker inside K gives suffix-zero descent

If the A5 blocker lies inside `K`, then the pullback is

```text
suffix(K)+l_1=0.
```

This is a two-piece zero branch strictly smaller than the separated interval `B G U`.

### Proof

For a left blocker, the interval from the blocker to immediately before the hit is a proper suffix of `K`.  Add the A5 atom `l_1`. ∎

---

## Lemma A76.3: U-hit left blocker inside B gives zero-composite descent

If the A5 blocker lies inside `B`, then the pullback is

```text
tail(B)+K+l_1=0.
```

This routes to zero-composite surgery.  It has smaller active support unless `tail(B)=B` and `K` is all of `U`, which is an endpoint boundary handled separately.

### Proof

The interval from the blocker to the pre-hit endpoint in the moved order passes through a suffix of `B` and then `K`.  Add `l_1`. ∎

---

## Lemma A76.4: U-hit left blocker before B gives a left bridge relation

If the A5 blocker lies before `B`, then the pullback is

```text
Lft + B + K + l_1=0,
```

where `Lft` is the external left bridge ending at the start of `B`.

Using `B=U=K+L`, this implies

```text
Lft + K + L + K + l_1=0.
```

Equivalently, after comparing with the original equality `B=U`, this is a signed/equal bridge relation involving `Lft`, `L`, and the boundary atom `l_1`.

### Status

This is a crossing bridge branch.  By A74, it descends or normalizes unless it is an equal-span separated bridge return.

---

## Lemma A76.5: U-hit right blocker inside L gives pair-difference prefix descent

If the A5 blocker lies to the right inside a proper prefix `L_r` of `L`, then

```text
L_r = l_1-u_k,
```

where `u_k` is the last atom of `K`.

Equivalently,

```text
u_k-l_1+L_r=0.
```

This is a smaller pair-difference prefix obstruction.

### Proof

This is the standard A5 right-blocker calculation used in A67/A70.  Subtract the recurrent endpoint from the blocker endpoint. ∎

---

## Lemma A76.6: U-hit right blocker beyond U crosses the old gap position

If the right blocker lies beyond `U`, then in the moved order it enters either `G` or the post-segment region.  Its pullback to the original order crosses the old gap boundary because `G` originally separated `B` and `U`.

The resulting relation is a bridge signed composite involving:

```text
remaining tail of U,
part/all of G,
possible post bridge,
and the atom correction u_k-l_1.
```

### Status

This branch is routed by A74.  It can preserve the old gap only if the bridge component is exactly the old `G` and no proper prefix/tail of `G` is lost.

---

# 4. A5 blocker for a G-hit

Now assume the recurrent hit is

```text
x+2a+G_j=f.
```

Write

```text
G=H R,
H=prefix_j(G),
R=tail_j(G),
```

and let `r_1` be the first atom of `R` if `R` is nonempty.

In the moved order `B U G`, the hit occurs after

```text
B U H.
```

---

## Lemma A76.7: G-hit left blocker inside H gives suffix-zero descent

If the left blocker lies inside `H`, then the pullback is

```text
suffix(H)+r_1=0.
```

This is a two-piece zero branch inside the old gap block, hence strict descent.

### Proof

Same suffix calculation as Lemma A76.2. ∎

---

## Lemma A76.8: G-hit left blocker inside U gives zero-composite descent

If the left blocker lies inside `U`, then the pullback is

```text
tail(U)+H+r_1=0.
```

This is a zero-composite branch using a proper tail of the equal interval `U` and a prefix of the gap.

### Proof

The interval from the blocker to the pre-hit endpoint passes through a suffix of `U` and the prefix `H` of `G`.  Add `r_1`. ∎

---

## Lemma A76.9: G-hit left blocker inside B gives zero-composite crossing both equal blocks

If the left blocker lies inside `B`, then the pullback is

```text
tail(B)+U+H+r_1=0.
```

Since `sum(B)=sum(U)`, this can be compared with `tail(B)+prefix(B)` to produce a transported-prefix/equal-interval relation unless the tail is all of `B`.

### Status

Routes to zero-composite / transported-prefix / separated-equal machinery.

---

## Lemma A76.10: G-hit right blocker inside R gives pair-difference prefix descent

If the right blocker lies inside a proper prefix `R_s` of `R`, then

```text
R_s = r_1-g_j,
```

where `g_j` is the last atom of `H`.

Equivalently,

```text
g_j-r_1+R_s=0.
```

This is a smaller pair-difference prefix obstruction inside the old gap.

### Proof

Standard right-blocker calculation. ∎

---

## Lemma A76.11: G-hit right blocker beyond G gives a post-gap bridge relation

If the right blocker lies beyond `G`, then the pullback is

```text
R + Post + g_j-r_1=0,
```

where `Post` is the bridge after `G` up to the blocker.

This is a signed bridge relation.  It can preserve the old separated gap only if `R=G` and `Post` recreates the original external bridge without shortening.

### Status

Routed by A74; only equal-span separated bridge return can tie.

---

# 5. Endpoint branches

If the recurrent hit occurs at the endpoint of `U` or `G`, the next atom belongs to the following block.

## Lemma A76.12: endpoint U-hit reduces to adjacent equal-block / midpoint recurrence

If `K=U`, then the U-hit is after `B U`, i.e. after adjacent equal blocks in the moved order.  Since `sum(B)=sum(U)`, this is exactly the midpoint/adjacent-equal boundary from A55.

### Proof

The moved segment begins `B U`, with equal sums and no gap. ∎

---

## Lemma A76.13: endpoint G-hit is a post-segment recurrence, not a separated-gap return

If `H=G`, the G-hit is after the full moved segment `B U G`.  This endpoint has the same total value as the original segment endpoint `B G U`.  Therefore a new forbidden hit here is either an old post-segment hit or an external/cyclic recurrence branch.

### Proof

Both orders have total sum `2a+g`. ∎

---

# 6. Gap-preservation constraints

A gap-preserving separated recurrence requires the pullback to recreate a separated-equal bridge with the same gap length `|G|`.

From the cases above, this is highly restrictive.

## Lemma A76.14: any blocker using a proper prefix or proper tail of G reduces gap length

If the A5 pullback uses a proper prefix `H` of `G` or a proper tail `R` of `G`, then any separated-equal return has gap length strictly smaller than `|G|`.

### Proof

A separated return using only a proper subblock of `G` as the separating gap cannot preserve the full old gap.  The unused nonempty portion of `G` either becomes part of an equal interval or part of a zero-composite bridge, reducing the gap coordinate. ∎

---

## Lemma A76.15: gap preservation forces the blocker to cross the whole old gap G

If a gap-after recurrence returns to a separated-equal bridge with the same gap length `|G|`, then the A5 blocker pullback must include all of `G` as the separating bridge and cannot use a proper prefix or proper tail of `G` as the active gap.

### Proof

Immediate from Lemma A76.14 and the definition of gap preservation. ∎

---

## Lemma A76.16: full-gap reuse forces endpoint alignment

If the pullback includes all of `G` as the preserved gap, then the equal intervals on either side must begin and end at the old boundaries of `G`; otherwise the gap is shortened or lengthened.

Thus a gap-preserving return must reuse the old gap endpoints.

### Proof

Moving either boundary of the gap inward shortens it.  Moving either boundary outward changes the enclosing span or absorbs external bridge atoms into the gap, contradicting equal-span preservation unless the whole external extension is zero/collapsing. ∎

---

# 7. Rigid self-return

The preceding lemmas show that a true gap-preserving return is rigid.

## Definition A76.17: rigid separated self-return

A rigid separated self-return is a gap-preserving separated recurrence in which the returned separated-equal state is exactly

```text
B G U
```

or its direct exchange

```text
U G B
```

with the same gap endpoints and the same equal-interval endpoints.

---

## Proposition A76.18: gap-preserving separated recurrence reduces to rigid self-return

Every gap-preserving separated recurrence either:

```text
1. decreases gap length;
2. decreases enclosing span;
3. routes to midpoint/zero-composite/pair-difference/cyclic recurrence;
4. or is a rigid separated self-return.
```

### Proof

Non-endpoint U-hit and G-hit blocker cases are classified above.  Proper use of `G` decreases gap by Lemma A76.14.  Preserving the full gap forces endpoint alignment by Lemmas A76.15--A76.16.  Endpoint U-hit routes to midpoint by Lemma A76.12; endpoint G-hit routes to external/cyclic recurrence by Lemma A76.13.  The only remaining case is exact reuse of the old separated-equal state, possibly with the equal blocks exchanged. ∎

---

# 8. Remaining rigid case

The rigid self-return is now the only non-weighted tie left by A76.

It is very restrictive: the local operation

```text
B G U -> B U G
```

followed by recurrence and A5 pullback must reconstruct the same separated-equal obstruction with the same endpoints.

This suggests a two-step cycle:

```text
B G U -> B U G -> B G U
```

or

```text
B G U -> B U G -> U G B.
```

Such a cycle should force one of:

```text
1. the old forbidden hit reappears earlier;
2. a partial sum equality inside G;
3. a midpoint condition at one of the endpoints;
4. direct exchange succeeds or descends.
```

This final rigid-cycle contradiction is not proved here.

---

# 9. Consequence for global acyclicity

A76 sharpens the non-weighted acyclicity gap:

```text
bridge-span monotonicity
  -> equal-span separated bridge return
  -> gap-preserving separated recurrence
  -> rigid separated self-return.
```

Thus the remaining non-weighted tie is no longer a broad recurrence family.  It is a rigid two-step self-return of a separated-equal obstruction.

---

# 10. Target A77

A77 should attack the rigid separated self-return.

Suggested approach:

1. Write the exact partial sums of the two-step cycle:

```text
B G U -> B U G -> B G U
```

and the exchange cycle:

```text
B G U -> B U G -> U G B.
```

2. Impose the recurrent hit equations `H_U` and `H_G`.

3. Impose the A5 blocker equation that reconstructs the same gap endpoints.

4. Show the system forces one of:

```text
G_j=0,
B_i=U_k with smaller support,
2S_y=S_x+S_v midpoint,
earler f-hit,
zero-composite inside B/G/U.
```

---

## Current status

Proved here:

1. U-hit and G-hit A5 pullback formulas for gap-after recurrence;
2. internal blocker cases descend or route to known classes;
3. endpoint cases route to midpoint/external recurrence;
4. gap preservation forces reuse of the whole old gap;
5. gap-preserving separated recurrence reduces to rigid separated self-return.

Not proved here:

1. rigid separated self-return contradiction;
2. weighted cut-selection;
3. final endpoint avoidance theorem.
