# Analytic rigid separated self-return A77

This note continues from A76.

A76 reduced the remaining non-weighted bridge/gap tie to a very rigid case:

```text
B G U,
sum(B)=sum(U)=a,
G nonempty,
```

where the gap-after move

```text
B G U -> B U G
```

is Graham-valid but recurrent, and the A5 blocker pullback recreates a separated-equal bridge with the same gap endpoints and equal-block endpoints.

This note derives the exact rigid self-return constraints.

The result is partial but useful:

```text
1. exact same-orientation self-return is impossible unless there is zero collapse;
2. exact exchange-orientation self-return reduces to a symmetric two-cycle;
3. the symmetric two-cycle forces endpoint equations that route to midpoint/direct-exchange recurrence;
4. the only remaining non-weighted tie is this symmetric two-cycle modulo A34/global termination.
```

No complete endpoint-avoidance proof is claimed.

---

## 1. Standing setup

Let the original local segment be

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

The original displayed partial sums are

```text
B-family: x+B_i,
G-family: x+a+G_j,
U-family: x+a+g+U_k,
Y-family: x+2a+g+Y_m.
```

The gap-after move gives

```text
X B U G Y
```

with displayed partial sums

```text
B-family: x+B_i,
U-family: x+a+U_k,
G-family: x+2a+G_j,
Y-family: x+2a+g+Y_m.
```

Only the `U` and `G` families move.

---

## 2. Recurrent hit types

By A76, a new forbidden hit after the gap-after move is either

```text
H_U(k): x+a+U_k=f,
```

or

```text
H_G(j): x+2a+G_j=f.
```

Endpoint cases were already routed:

```text
H_U(|U|) -> adjacent equal-block / midpoint boundary;
H_G(|G|) -> post-segment/external recurrence.
```

So the only rigid self-return case has proper prefixes:

```text
0<k<|U|,
0<j<|G|,
```

unless it routes to midpoint/external recurrence.

---

# 3. What rigid return means

A76 showed that preserving the same gap length forces reuse of the whole old gap `G` and hence reuse of the old gap endpoints.

There are two possible rigid returns.

## Definition A77.1: same-orientation rigid return

The A5 blocker pullback recreates the same separated-equal obstruction

```text
B G U.
```

That means the returned equal intervals are exactly `B` and `U`, with `G` between them in the same order.

## Definition A77.2: exchange-orientation rigid return

The A5 blocker pullback recreates the exchanged separated-equal obstruction

```text
U G B.
```

That means the returned equal intervals are exactly `U` and `B`, with the same gap `G` between them but in the exchanged order.

---

# 4. Same-orientation self-return

A same-orientation return requires that the A5 blocker relation after the moved order `B U G` reconstructs equal blocks whose endpoints are the original endpoints of `B` and `U` in `B G U`.

But in the moved order, `B` and `U` are adjacent.  The old gap `G` lies after `U`, not between `B` and `U`.

Therefore the blocker pullback must cross `G` and then place it back between `B` and `U`.

---

## Lemma A77.3: same-orientation rigid return must use an endpoint G-hit

If the A5 pullback from the moved order `B U G` reconstructs the exact original orientation `B G U`, then the recurrent hit must occur in the moved `G` family, not in a proper prefix of `U`.

### Proof sketch

A proper U-hit has local endpoint after `B K`, with `K` a proper prefix of `U`.  Its A5 pullback intervals are built from suffixes/prefixes of `B`, `K`, and the following tail of `U`; the old gap `G` lies strictly after the hit.  Any pullback that includes the whole old gap must also include the remaining tail of `U`, forcing a proper use of `U` and hence changing the endpoint of the returned equal interval.  Thus it cannot reconstruct the exact full block `U` with `G` before it unless the hit is already beyond all of `U`, i.e. a G-family hit. ∎

### Status

This removes proper U-hits from exact same-orientation self-return.  Proper U-hits either decrease support/gap or route to bridge/equal interval as in A76.

---

## Lemma A77.4: same-orientation G-hit self-return is endpoint/external recurrence

If a G-hit reconstructs the exact original orientation `B G U`, then the A5 blocker must use all of `G`.  Therefore the G-hit is at the endpoint of `G` or its blocker uses the endpoint after all of `G`.

This is the endpoint G-hit branch from A76.13 and routes to post-segment/external/cyclic recurrence.

### Proof sketch

Exact reuse of the whole gap requires both boundaries of `G`.  A proper G-prefix hit uses only a prefix `H` of `G`, and A76.14 shows any such use shortens the gap.  Therefore exact same-orientation preservation requires the full `G`, which is the endpoint branch. ∎

---

## Proposition A77.5: exact same-orientation rigid self-return is not a new tie

A same-orientation rigid return either:

```text
1. uses a proper U/G prefix and hence decreases gap/support by A76;
2. uses endpoint U and routes to midpoint A55;
3. uses endpoint G and routes to external/cyclic recurrence A62/A71;
4. or produces zero collapse inside G.
```

Thus it does not remain as a distinct non-weighted tie.

### Proof

Combine Lemmas A77.3--A77.4 with A76.12--A76.14. ∎

---

# 5. Exchange-orientation self-return

The only rigid possibility left is the exchanged orientation:

```text
B G U -> B U G -> U G B.
```

This is more subtle because it agrees with the direct exchange of the original separated-equal pair.

Recall the direct exchange move from A36:

```text
B G U -> U G B.
```

Therefore an exchange-orientation self-return means:

```text
gap-after recurrence + A5 pullback reconstructs the same obstruction that direct exchange would test directly.
```

---

## Lemma A77.6: exchange-orientation self-return factors through direct exchange

If a rigid return produces `U G B`, then the returned separated-equal obstruction is exactly the direct-exchange target of the original separated-equal branch.

### Proof

The original separated-equal branch is `B G U`.  Its direct exchange is by definition `U G B`.  A rigid exchanged return has the same endpoints and the same gap `G`, hence it is exactly this direct-exchange target. ∎

---

## Lemma A77.7: if direct exchange succeeds, exchange-orientation self-return is impossible

If

```text
B G U -> U G B
```

is Graham-valid and avoids `f`, then the original minimal counterexample is contradicted.  Therefore an exchange-orientation self-return can occur only if direct exchange has a collision or forbidden recurrence.

### Proof

A successful direct exchange gives an endpoint-avoiding Graham-valid ordering, contrary to the assumed counterexample. ∎

---

## Lemma A77.8: direct-exchange collision in the exchange self-return routes by A36--A54

If direct exchange is blocked by a collision, then the collision is one of D1--D5 and routes to:

```text
equal-interval descent,
zero-composite surgery,
two-piece zero,
three-piece zero,
zero collapse,
or D2 zero-composite controlled modulo recurrence.
```

Thus collision-blocked exchange self-return leaves the rigid tie.

### Proof

This is the direct-exchange routing table A36--A54 with `A=B` and `C=U`. ∎

---

## Proposition A77.9: exchange-orientation self-return reduces to direct-exchange forbidden recurrence

The only exchange-orientation rigid self-return not already routed is the case where direct exchange

```text
B G U -> U G B
```

is Graham-valid but recurrent.

### Proof

By Lemma A77.6, the exchange return is the direct-exchange target.  If direct exchange succeeds, contradiction by Lemma A77.7.  If it collides, routing by Lemma A77.8.  Hence only Graham-valid recurrent direct exchange remains. ∎

---

# 6. Direct-exchange recurrence constraints

Direct exchange moves displayed families as in A36.

Original:

```text
x+B_i,
x+a+G_j,
x+a+g+U_k,
x+2a+g+Y_m.
```

After direct exchange `U G B`:

```text
x+U_k,
x+a+G_j,
x+a+g+B_i,
x+2a+g+Y_m.
```

The `G` and post-segment families are unchanged; the `B` and `U` families move.

Thus direct-exchange recurrence can occur only through:

```text
R_U(k): x+U_k=f,
R_B(i): x+a+g+B_i=f.
```

---

## Lemma A77.10: direct-exchange recurrence has only U-family or B-family moved hits

In the direct exchange `B G U -> U G B`, the only new forbidden hits are:

```text
x+U_k=f,
x+a+g+B_i=f.
```

### Proof

The `G` and post-segment families are unchanged; only the translated equal-block prefix families move. ∎

---

## Lemma A77.11: endpoint moved hits route to midpoint/external recurrence

If `k=|U|`, then `x+U=f` is the endpoint after the first equal block in the exchanged order.  Since `sum(U)=sum(B)=a`, this is an adjacent-equal/midpoint boundary relative to the original equal pair.

If `i=|B|`, then `x+a+g+B=x+2a+g`, the full displayed endpoint before `Y`, hence a post-segment/external recurrence.

### Proof

Substitute endpoint sums. ∎

---

## Lemma A77.12: proper moved hits in direct exchange are singleton-prefix recurrence branches

If `0<k<|U|`, then

```text
x+U_k=f
```

is a singleton/prefix recurrence of the form A70.

If `0<i<|B|`, then

```text
x+a+g+B_i=f
```

is also a moved-prefix recurrence based at `x+a+g`.

Therefore proper direct-exchange recurrence routes by A70.

### Proof

Both equations have the form basepoint plus moved prefix equals `f`. ∎

---

# 7. Rigid self-return theorem

## Theorem A77.13: rigid separated self-return reduces to known recurrence mechanisms

Every rigid separated self-return from A76 is one of:

```text
1. same-orientation endpoint/external recurrence;
2. same-orientation midpoint recurrence;
3. same-orientation gap/support descent;
4. exchange-orientation direct-exchange collision routed by A36--A54;
5. exchange-orientation direct-exchange forbidden recurrence routed by A70/A71;
6. zero collapse inside B, G, or U.
```

Thus rigid separated self-return introduces no new local algebraic species.

### Proof

Same-orientation is Proposition A77.5.  Exchange-orientation is Proposition A77.9 plus Lemmas A77.10--A77.12. ∎

---

# 8. Consequence for non-weighted acyclicity

Combining A74--A77:

```text
bridge-span monotonicity
  -> equal-span separated bridge return
  -> gap-preserving separated recurrence
  -> rigid separated self-return
  -> known recurrence mechanisms.
```

Therefore the non-weighted graph is now locally routed.  What remains is not a new branch, but a final global acyclicity statement assembling the routed recurrence mechanisms.

---

# 9. Remaining gaps after A77

The remaining proof obligations are now:

```text
1. weighted core cut-selection theorem;
2. final global acyclicity assembly using the measure from A73/A74;
3. finite verification / exceptional characteristic bridge;
4. final endpoint-avoidance theorem assembly.
```

The non-weighted obstruction tree has no currently isolated local branch left outside the routed graph.

---

# 10. Target A78

A78 should state the non-weighted acyclicity theorem conditional only on the recurrence-routing lemmas already proved and excluding `WEIGHTED_CORE`.

Expected theorem:

> In the obstruction dependency graph with `WEIGHTED_CORE` removed, every infinite path either reaches `SUCCESS`, reaches `CONTRADICTION`, or strictly decreases the global measure `M_NW`.  Therefore no non-weighted minimal counterexample exists.

Then the only substantive remaining analytic gap is weighted core cut-selection.

---

## Current status

Proved here:

1. same-orientation rigid return routes to endpoint/external/midpoint/descent cases;
2. exchange-orientation rigid return factors through direct exchange;
3. direct-exchange collision and recurrence are already routed;
4. rigid separated self-return introduces no new local species.

Not proved here:

1. final global acyclicity theorem;
2. weighted core cut-selection;
3. endpoint avoidance theorem.
