# Analytic pair-difference recurrence A69

This note continues from A68.

A68 marked atom-insertion recurrence H1/H2 as routed modulo existing global mechanisms.  The next A34 recurrence source is the A33 Q2 pair-swap forbidden recurrence.

The goal of this note is to put pair-difference recurrence into the same form as A65--A67:

```text
apply A5 to the recurrent transformed ordering;
pull the blocker back through the pair swap;
prove non-crossing blockers descend;
route crossing blockers to known global mechanisms.
```

This note is a routing result, not a complete termination theorem.

---

## 1. Standing pair-difference setup

Consider a local segment

```text
X P a b Y
```

where `a` and `b` are atoms and `P` is a block.  The pair-difference boundary has the form

```text
a-b=sum(P)=p.
```

Equivalently,

```text
p+b-a=0.
```

The pair-swap move is

```text
X P a b Y -> X P b a Y.
```

Let

```text
x=sum(X).
```

After the swap, the endpoint after `P b` has value

```text
x+p+b.
```

Using `a-b=p`, this is

```text
x+a.
```

Thus the pair-swap transports the atom `a` to an earlier endpoint level.

The A33 recurrence branch has schematic form

```text
x+Y_m=f
```

or, depending on the local normalization, a forbidden landing in the post-pair family after the pair swap.

For this note, model the recurrent forbidden hit as an endpoint `H` in the transformed ordering after the swapped pair, with first forbidden hit not earlier than the global minimal index.

---

## 2. Transformed A5 blocker

Let the transformed ordering be

```text
R' = X P b a Y.
```

Let `H` be the first forbidden-hit endpoint in `R'` created by the pair-swap recurrence.

Since the final endpoint is not forbidden in endpoint avoidance, `H` is non-final.  Applying A5 to `R'` gives a blocker index `j'` such that

```text
S'_{H-1}+r'_{H+1}=S'_{j'}.
```

The blocker is classified by its position relative to the swapped-pair neighborhood:

```text
left of P,
inside P,
at/around b,a,
inside Y before H,
after H.
```

As in A64, bounded nearest blockers descend.  This note handles the long-blocker pullbacks.

---

## 3. Recurrence hit inside the post-pair tail

The most important pair-swap recurrence has the forbidden hit inside the tail `Y`.  Write

```text
Y=U V,
```

where the forbidden hit occurs after

```text
P b a U.
```

Let

```text
u=sum(U),
v=sum(V).
```

The transformed forbidden-hit endpoint is

```text
x+p+a+b+u.
```

Since the pair swap preserves the total of `a+b`, the total endpoint after `P a b U` in the original ordering is the same.  The recurrence is therefore a post-local forbidden landing; the pair-swap does not change the final level, only internal levels near the pair.

The atom immediately after the hit is the first atom of `V`, call it

```text
v_1.
```

If `V` is empty, the endpoint case is treated in Section 7.

---

# 4. Left blockers

Assume first that the A5 blocker lies to the left of the recurrent hit.

Then A64.2 gives

```text
sum'(j',H-1]+v_1=0.
```

We pull this interval back through the pair swap.

---

## Lemma A69.1: left blocker inside U gives suffix-zero descent

If the blocker lies inside `U`, then the pullback is

```text
sum(tail(U from blocker))+v_1=0.
```

This is a two-piece zero composite supported inside `Y`, strictly smaller than the pair-difference source plus tail context.

### Proof

The interval from the blocker to `H-1` is a suffix of `U`.  Add the A5 atom `v_1`. ∎

---

## Lemma A69.2: left blocker inside P gives a zero-composite descent

If the blocker lies inside `P`, then the pullback is

```text
sum(tail(P from blocker))+b+a+U+v_1=0.
```

Since `a+b` is a two-atom block and the tail of `P` is proper, this is a zero-composite branch with smaller active support unless it is an endpoint boundary tie.

### Proof

The transformed interval from the blocker to `H-1` runs through a suffix of `P`, then through `b a`, then through `U`.  Add `v_1`. ∎

---

## Lemma A69.3: left blocker before P gives a bridge crossing relation

If the blocker lies before `P`, then the pullback is

```text
L+P+b+a+U+v_1=0,
```

where `L` is the external bridge ending at the start of `P`.

Using the pair-difference identity `p+b-a=0`, this may be rewritten as

```text
L+2a+U+v_1=0
```

or

```text
L+P+2b+U+v_1=0,
```

depending on which atom is eliminated.

### Proof

The interval includes the bridge, all of `P`, the swapped pair `b a`, and all of `U`, plus the A5 atom `v_1`.  The alternative forms follow from `a-b=p`. ∎

### Status

This is a crossing bridge branch.  It routes to signed/equal interval or weighted normal-form machinery, not a new recurrence species.

---

# 5. Blockers inside the swapped-pair neighborhood

The pair neighborhood in the transformed order is

```text
b a.
```

There are only endpoint positions around these atoms.

---

## Lemma A69.4: blocker at the endpoint after P gives the original pair-difference relation

If the blocker is the endpoint after `P`, then the left-blocker relation reads

```text
b+a+U+v_1=0
```

for a post-pair recurrence hit after `U`.  If `U` is empty this reduces to

```text
b+a+v_1=0,
```

a three-atom zero branch.  If `U` is nonempty, it is a zero-composite branch inside the post-pair region.

### Proof

The interval from after `P` to `H-1` is `b a U`.  Add `v_1`. ∎

---

## Lemma A69.5: blocker at the endpoint after P b gives a pair-difference boundary

If the blocker is the endpoint after `P b`, then the left-blocker relation is

```text
a+U+v_1=0.
```

If `U` is empty, this is a two-atom zero branch `a+v_1=0`.  If `U` is nonempty, it is a zero-composite branch that can be attacked by A28--A33.

### Proof

The interval from after `P b` to `H-1` is `a U`.  Add `v_1`. ∎

---

# 6. Right blockers

Now suppose the A5 blocker lies to the right of the recurrent hit.  The interval from the hit to the blocker starts inside `V`.

Let `V_r` be the prefix of `V` ending at the blocker if the blocker lies inside `V`.

---

## Lemma A69.6: right blocker inside proper V-prefix gives pair-difference prefix descent

If the right blocker lies inside a proper prefix `V_r` of `V`, then the pullback relation has the form

```text
V_r = v_1 - u_last,
```

where `u_last` is the last atom before the recurrent hit.  Equivalently,

```text
u_last-v_1+V_r=0.
```

This is a smaller pair-difference/prefix obstruction.

### Proof

This is the same A5 right-blocker calculation as A67.5, with `U` now the prefix before the recurrent hit in the post-pair tail. ∎

---

## Lemma A69.7: right blocker using all of V is a pair-difference endpoint branch

If the right blocker uses all of `V`, then

```text
V+u_last-v_1=0,
```

or

```text
v_1-u_last=sum(V).
```

This is an A33-type pair-difference boundary.

### Proof

Endpoint case of Lemma A69.6. ∎

---

## Lemma A69.8: right blocker beyond V gives a bridge zero/signed composite

If the right blocker lies after `V`, then the pullback is

```text
R+V+u_last-v_1=0,
```

where `R` is the external bridge after `V` to the blocker.

This is a signed zero-composite crossing the right boundary.

### Proof

The interval from the recurrent hit to the blocker contains all of `V` and the right external bridge.  Compare with the A5 atom substitution `v_1-u_last`. ∎

---

# 7. Endpoint recurrence

If the forbidden hit occurs at the endpoint immediately after the swapped-pair region, then no post-tail `V` exists in the local model.  The recurrence reduces to an atom or pair landing depending on normalization.

## Lemma A69.9: endpoint pair-swap recurrence routes to singleton or pair-difference recurrence

If the pair-swap recurrence occurs at the endpoint immediately after `P b a`, then the forbidden landing is

```text
x+p+a+b=f.
```

Using `a-b=p`, this can be rewritten as

```text
x+2a=f
```

or

```text
x+p+a+b=f.
```

Thus the endpoint case is a singleton/pair landing branch, not a new pair-swap recurrence species.

### Proof

Substitute `p=a-b`. ∎

### Status

This branch belongs with singleton-prefix recurrence R4 and midpoint-type atom landing if division by 2 is invoked.

---

# 8. Non-crossing descent theorem

Call a blocker non-crossing if it lies inside:

```text
P,
U,
or a proper prefix of V.
```

Call it crossing if it reaches before `P`, beyond `V`, or uses all of `V` in the endpoint pair-difference case.

## Proposition A69.10: non-crossing pair-swap recurrence descends

For A33 pair-swap recurrence, every non-crossing transformed A5 blocker pulls back to a smaller zero-composite, suffix-zero, or pair-difference prefix obstruction.

### Proof

Inside-`U` blockers descend by Lemma A69.1.  Inside-`P` blockers route to smaller zero-composite branches by Lemma A69.2.  Inside proper `V` blockers descend by Lemma A69.6. ∎

---

# 9. Crossing routing theorem

## Proposition A69.11: crossing pair-swap recurrence routes to existing mechanisms

Every crossing pair-swap recurrence routes to one of:

```text
bridge signed/equal interval;
zero-composite bridge;
pair-difference endpoint branch;
singleton/midpoint recurrence.
```

### Proof

Left bridge crossings are Lemma A69.3.  Pair-neighborhood endpoints are Lemmas A69.4--A69.5.  Right endpoint and right bridge crossings are Lemmas A69.7--A69.8.  Endpoint recurrence is Lemma A69.9. ∎

---

# 10. Pair-difference recurrence conclusion

Combining Propositions A69.10 and A69.11:

```text
A33 pair-swap recurrence introduces no new local algebraic species.
```

It is routed modulo:

```text
zero-composite descent,
equal/signed interval geometry,
pair-difference boundary machinery,
singleton recurrence,
A34 global termination.
```

Thus A34 obligation R3 is no longer standalone.

---

# 11. Remaining recurrence sources

After A69, the remaining recurrence sources from A34 are:

```text
R4. singleton-prefix recurrence;
R5. cyclic-cut recurrence.
```

The next target should be singleton-prefix recurrence because endpoint cases from H2 and pair-swap recurrence route into it.

---

## Target A70

Analyze singleton-prefix recurrence.

Schematic branch:

```text
x+q=f
```

or

```text
x+B_i=f
```

after a local move.

Apply A5 at the singleton/prefix hit and pull blockers back.  Expected outcomes:

```text
zero-composite suffix descent;
equal/signed bridge interval;
pair-difference endpoint;
cyclic-cut recurrence;
A34 termination.
```

---

## Current status

Proved here:

1. pair-swap recurrence A5 pullback formulas;
2. non-crossing pair-swap blockers descend;
3. crossing blockers route to existing mechanisms;
4. R3 pair-swap recurrence is not a standalone A34 gap.

Not proved here:

1. singleton-prefix recurrence;
2. cyclic-cut recurrence;
3. weighted cut-selection;
4. final endpoint avoidance theorem.
