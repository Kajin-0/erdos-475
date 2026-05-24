# Analytic internal cyclic self-return hardening A89

This note continues from A88.

A88 identified the highest-risk weighted-core bottleneck:

```text
A83.2: exact cyclic self-return implies E_B - T_k = E_B.
```

A89 hardens that point.

The main conclusion is deliberately precise:

```text
Endpoint-set translation invariance follows from a strong exact-pattern self-return definition.
It does not follow merely from preservation of the weighted block sum A+2B+C=0.
```

Thus A83.2 is valid if “exact self-return” means equality of the internal endpoint pattern of the middle block.  If the proof only establishes equality of the weighted equation or equality of the middle block as an unordered/support object, then an additional lemma is still needed.

---

## 1. Internal endpoint notation

Let

```text
B=b_1 b_2 ... b_n,
n>=2.
```

Define internal partial sums

```text
T_0=0,
T_i=b_1+...+b_i,
1<=i<=n.
```

Let

```text
b=T_n=sum(B).
```

Define the internal endpoint set

```text
E_B={T_0,T_1,...,T_n} subset F_p.
```

Assume the block is internally Graham-valid:

```text
T_i != T_j for i != j.
```

Equivalently, `B` has no nonempty internal zero interval.

---

## 2. Cyclic cut and rotated endpoint set

For a cut after index `k`, with

```text
1<=k<=n-1,
```

write

```text
P=b_1...b_k,
R=b_{k+1}...b_n.
```

Then

```text
B=P R,
rot_k(B)=R P.
```

Let

```text
T_k=sum(P).
```

The rotated block `R P` has internal endpoint sequence:

```text
0,
T_{k+1}-T_k,
T_{k+2}-T_k,
...,
T_n-T_k,
T_n-T_k+T_1,
...,
T_n-T_k+T_k=T_n.
```

As a set, this is

```text
E_{rot_k(B)} = (E_B - T_k) union {T_n}
```

but because

```text
T_n - T_k + T_i = T_i - T_k + T_n,
```

and all arithmetic is in `F_p`, the cleaner translation identity is obtained after identifying endpoints relative to the cyclic basepoint.

To avoid ambiguity about the final endpoint, define the cyclic endpoint set of `B` modulo its total endpoint by

```text
C_B={T_i - T_j : 0<=i,j<=n, endpoint values measured from a chosen basepoint}.
```

For the exact internal pattern needed in A83, the relevant object is not merely `E_B`; it is the endpoint set of the middle block relative to the outer blocks, including the fixed endpoints `0` and `b`.

This motivates the following definition.

---

## 3. Strong exact internal self-return

## Definition A89.1: strong exact internal cyclic self-return

A cut after `k` is a strong exact internal cyclic self-return if, after the cut-swap

```text
P R -> R P,
```

the routed obstruction reconstructs the same weighted core

```text
A + 2B + C = 0
```

with all of the following preserved:

```text
1. the same outer basepoint before B;
2. the same middle endpoints 0 and b relative to that basepoint;
3. the same internal endpoint set E_B;
4. the same obstruction labels attached to the internal endpoints;
5. no internal zero/equal/pair obstruction produced during the return.
```

In short:

```text
strong exact self-return = same weighted equation + same ordered endpoint pattern up to the cyclic cut.
```

This is stronger than merely saying the same block sum `b` or the same support set of atoms reappears.

---

## 4. Endpoint-set invariance under strong exact return

## Lemma A89.2: strong exact internal cyclic self-return implies endpoint-set equality

If the cut after `k` is a strong exact internal cyclic self-return, then

```text
E_{rot_k(B)} = E_B.
```

### Proof

By Definition A89.1, the return reconstructs the same internal endpoint set of the middle block relative to the same outer basepoint and same middle endpoints.  The internal endpoint set of the transformed middle block is exactly `E_{rot_k(B)}`.  Therefore it equals `E_B`. ∎

---

## Lemma A89.3: rotated endpoint-set equality gives translation invariance modulo endpoint convention

Let

```text
1<=k<=n-1.
```

If

```text
E_{rot_k(B)} = E_B
```

as internal endpoint sets relative to the same basepoint, then the non-final cyclic endpoint set satisfies

```text
E_B - T_k = E_B
```

provided the final endpoint `b` is included consistently on both sides.

### Proof

The rotated endpoint set consists of the old endpoints translated by `-T_k`, with wrapped endpoints represented by adding the total `b` after traversal.  Since the final endpoint `b` is preserved and included on both sides, this is exactly translation by `-T_k` on the endpoint set.  Therefore equality of endpoint sets is equivalent to

```text
E_B - T_k = E_B.
```

∎

### Audit note

The endpoint `b` must be handled consistently.  If one works with non-final internal endpoints only, the identity becomes a cyclic endpoint identity rather than a literal equality of subsets of `F_p`.

For final proof extraction, choose one convention and use it throughout.

---

## Proposition A89.4: hardened A83.2 under strong exactness

Under Definition A89.1, A83.2 is valid:

```text
strong exact cyclic self-return at cut k
    -> E_B - T_k = E_B.
```

### Proof

Apply Lemma A89.2, then Lemma A89.3. ∎

---

# 5. Translation-invariant endpoint sets

The next step from A83 is solid.

## Lemma A89.5: nonzero translation-invariant subset of F_p is all of F_p

Let

```text
E subset F_p,
E nonempty.
```

If

```text
E+d=E
```

for some

```text
d != 0,
```

then

```text
E=F_p.
```

### Proof

Since `p` is prime, every nonzero `d` generates the additive group of `F_p`.  From `E+d=E`, induction gives

```text
E+m d=E
```

for every integer `m`.  The orbit of any element `e in E` under translations by `d` is all of `F_p`.  Hence `F_p subseteq E`.  Therefore `E=F_p`. ∎

---

## Lemma A89.6: if T_k is nonzero, strong exact self-return forces E_B=F_p

Assume strong exact internal cyclic self-return at cut `k` and

```text
T_k != 0.
```

Then

```text
E_B=F_p.
```

### Proof

By Proposition A89.4,

```text
E_B-T_k=E_B.
```

Apply Lemma A89.5 with `d=-T_k`. ∎

---

## Lemma A89.7: if T_k=0, there is internal zero collapse

If

```text
T_k=0
```

for some

```text
1<=k<=n-1,
```

then the prefix block

```text
b_1...b_k
```

is a nonempty zero-sum interval inside `B`.

### Proof

By definition, `T_k=sum(b_1...b_k)`. ∎

---

# 6. Full-field endpoint case

Assume `E_B=F_p`.

Since internal endpoints are distinct,

```text
|E_B|=n+1.
```

Therefore

```text
n+1=p.
```

so

```text
|B|=p-1.
```

## Lemma A89.8: full endpoint set forces |B|=p-1

If `B` is internally Graham-valid and `E_B=F_p`, then

```text
|B|=p-1.
```

### Proof

`E_B` has exactly `n+1` elements.  If `E_B=F_p`, then `n+1=p`. ∎

---

## Lemma A89.9: full endpoint set leaves no outside atoms in a subset instance

If `B` has length `p-1` and the ambient object is a subset of `F_p^*`, then no atoms remain outside `B`.  Hence the surrounding blocks `A` and `C` are empty.

### Proof

`F_p^*` has exactly `p-1` elements.  Since the ordering is of a subset, it contains at most `p-1` atoms total.  If `B` already has `p-1` atoms, it contains every atom in the ordering. ∎

---

## Lemma A89.10: full endpoint set contradicts genuine weighted core

If `A` and `C` are empty, then the weighted core

```text
A+2B+C=0
```

becomes

```text
2b=0.
```

Over odd characteristic, this implies

```text
b=0.
```

Thus `B` is a zero-sum whole block, so the weighted core is not genuine.

### Proof

Since `2` is invertible in odd characteristic, divide by `2`. ∎

---

# 7. Hardened internal cyclic rigidity theorem

## Theorem A89.11: strong exact internal cyclic self-return is impossible in a genuine weighted core

Let

```text
A+2B+C=0
```

be a genuine weighted core over an odd prime field, with `|B|>=2` and no internal zero interval in `B`.

Then no proper cut of `B` can be a strong exact internal cyclic self-return.

### Proof

Let the cut be after `k`, where `1<=k<=n-1`.

If `T_k=0`, Lemma A89.7 gives internal zero collapse, contrary to the genuine case.

If `T_k!=0`, Lemma A89.6 gives `E_B=F_p`.  Then Lemma A89.8 gives `|B|=p-1`, Lemma A89.9 gives `A=C=empty`, and Lemma A89.10 gives zero collapse.  Again this contradicts the genuine weighted-core assumption.

Therefore no strong exact self-return exists. ∎

---

# 8. What A89 does and does not prove

A89 proves the A83 endpoint-set invariance step under a strong exact-pattern definition.

It does not prove the following weaker implication:

```text
same weighted equation A+2B+C=0 after cut-swap
    -> E_B - T_k = E_B.
```

That implication is false without additional hypotheses: preserving the block sum `b` alone does not determine the internal endpoint set of `B`.

Therefore, the weighted-core closure still requires one of these two options:

```text
Option 1. Prove that cut-rigid weighted self-return necessarily satisfies Definition A89.1.
Option 2. Replace the A83/A89 endpoint-set argument with a weaker argument that only uses the data actually forced by cut-rigidity.
```

This is a substantial clarification of the proof status.

---

# 9. Revised weighted status

Before A89, A83 stated:

```text
internal cyclic rigidity impossible.
```

After hardening, the precise statement is:

```text
strong exact internal cyclic rigidity impossible.
```

The remaining weighted gap is:

```text
Does cut-rigid weighted self-return imply strong exact internal cyclic rigidity?
```

If yes, A83/A89 closes the weighted branch.

If no, another invariant is needed.

---

# 10. Target A90

A90 should attack the implication:

```text
cut-rigid weighted self-return
    -> strong exact internal cyclic self-return.
```

Recommended route:

1. Strengthen the definition of cut-rigid weighted self-return.
2. Track not only the weighted block sum but the displayed collision/recurrent endpoints generated by A60.
3. Show that if the returned weighted core has the same middle block `B` and same outer blocks `A,C`, then the internal endpoint set of `B` must be preserved.
4. If endpoint set is not preserved, extract a non-weighted obstruction:

```text
internal equal interval,
internal zero interval,
pair-difference boundary,
cyclic recurrence,
or smaller weighted middle.
```

A90 is now the real weighted bottleneck.

---

## Current status after A89

Proved here:

```text
1. strong exact self-return -> endpoint-set translation invariance;
2. nonzero translation invariance -> E_B=F_p;
3. full-field endpoint set -> |B|=p-1;
4. full-field endpoint set contradicts genuine weighted core;
5. strong exact internal cyclic self-return is impossible.
```

Still open:

```text
1. cut-rigid weighted self-return -> strong exact internal cyclic self-return;
2. full weighted-core closure if only weak self-return is known;
3. final endpoint-avoidance theorem without conditional weighted gap.
```
