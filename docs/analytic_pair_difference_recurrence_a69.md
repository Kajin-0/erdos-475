# Analytic pair-difference recurrence A69

This note continues from A68.

A68 marked atom-insertion recurrence H1/H2 as routed modulo existing global mechanisms. The next A34 recurrence source is the A33 Q2 pair-swap forbidden recurrence.

The goal of this note is to put pair-difference recurrence into the same form as A65--A67:

```text
apply A5 to the recurrent transformed ordering;
pull the blocker back through the pair swap;
prove non-crossing blockers descend;
route crossing blockers to known global mechanisms.
```

Correction status:

```text
This version incorporates the endpoint-convention audit from:

docs/analytic_f7_pair_difference_endpoint_audit.md
```

The key correction is analogous to the H2 correction in A67. If the recurrent hit occurs after

```text
P b a U
```

and

```text
U = U^- u_*,
```

then A5 uses the endpoint immediately before `u_*`. Therefore left-blocker pullbacks use `U^-`, not full `U`.

This note is a routing result, not a complete termination theorem.

---

## 1. Standing pair-difference setup

Consider a local segment

```text
X P a b Y
```

where `a` and `b` are atoms and `P` is a block. The pair-difference boundary has the form

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

Since the final endpoint is not forbidden in endpoint avoidance, `H` is non-final. Applying A5 to `R'` gives a blocker index `j'` such that

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

As in A64, bounded nearest blockers descend. This note handles the long-blocker pullbacks.

---

## 3. Recurrence hit inside the post-pair tail

The main pair-swap recurrence has the forbidden hit inside the tail `Y`.

Write:

```text
Y=U V.
```

If `U` is nonempty, write:

```text
U=U^- u_*.
```

If `V` is nonempty, write:

```text
V=v_1 V^+.
```

The recurrent hit occurs after

```text
P b a U.
```

If `U` is nonempty, this is after

```text
P b a U^- u_*.
```

The atom immediately after the hit is the first atom of `V`, denoted:

```text
v_1.
```

If `V` is empty, the endpoint case is treated separately in Section 7.

The transformed forbidden-hit endpoint is

```text
x+p+b+a+sum(U).
```

Since the pair swap preserves the total of `a+b`, the total endpoint after `P a b U` in the original ordering is the same. The recurrence is therefore a post-local forbidden landing; the pair-swap does not change the final level, only internal levels near the pair.

---

# 4. Non-endpoint case A: U nonempty and V nonempty

Assume:

```text
U=U^-u_*,
V=v_1V^+.
```

Let `H` be the endpoint after:

```text
P b a U^-u_*.
```

Then:

```text
S'_H=S'_{H-1}+u_*.
```

A5 gives:

```text
S'_{H-1}+v_1=S'_{j'}.
```

Thus left-blocker intervals stop before `u_*`, while right-blocker intervals compare `v_1` against `u_*`.

---

## Lemma A69.1: left blocker inside U^- gives suffix-zero descent

If the blocker lies inside `U^-`, then the pullback is

```text
sum(tail(U^- from blocker))+v_1=0.
```

If the blocker is the endpoint immediately before `u_*`, the relation is:

```text
v_1=0,
```

which is impossible because atoms lie in `F_p^*`.

### Proof

For a left blocker, A64.2 gives:

```text
sum'(j',H-1]+v_1=0.
```

Since `H-1` is before `u_*`, the interval ending at `H-1` contains only a suffix of `U^-`, not `u_*`. ∎

---

## Lemma A69.2: left blocker inside P gives a zero-composite descent

If the blocker lies inside `P`, then the pullback is

```text
sum(tail(P from blocker))+b+a+U^-+v_1=0.
```

Since `a+b` is a two-atom block and the tail of `P` is proper, this is a zero-composite branch with smaller active support unless it is an endpoint boundary tie.

### Proof

The transformed interval from the blocker to `H-1` runs through a suffix of `P`, then through `b a`, then through `U^-`. Add `v_1`. ∎

---

## Lemma A69.3: left blocker before P gives a bridge crossing relation

If the blocker lies before `P`, then the pullback is

```text
L+P+b+a+U^-+v_1=0,
```

where `L` is the external bridge ending at the start of `P`.

Using the pair-difference identity `p+b-a=0`, this may be rewritten in signed-correction form. Since:

```text
P+b=a,
```

we get:

```text
L+2a+U^-+v_1=0.
```

Equivalently, using `P-a=-b`, one may rewrite as a signed pair-correction involving `b`.

### Proof

The interval includes the bridge, all of `P`, the swapped pair `b a`, and all of `U^-`, plus the A5 atom `v_1`. The alternative forms follow from `a-b=p`. ∎

### Status

This is a crossing bridge branch. It routes to signed/equal interval or weighted normal-form machinery, not a new recurrence species.

---

# 5. Blockers inside the swapped-pair neighborhood

The pair neighborhood in the transformed order is

```text
b a.
```

There are only endpoint positions around these atoms.

---

## Lemma A69.4: blocker at the endpoint after P gives a zero-composite branch

If the blocker is the endpoint after `P`, then the left-blocker relation reads

```text
b+a+U^-+v_1=0
```

in Case A.

If `U^-` is empty this reduces to

```text
b+a+v_1=0,
```

a three-atom zero branch. If `U^-` is nonempty, it is a zero-composite branch inside the post-pair region.

### Proof

The interval from after `P` to `H-1` is `b a U^-`. Add `v_1`. ∎

---

## Lemma A69.5: blocker at the endpoint after P b gives a zero-composite branch

If the blocker is the endpoint after `P b`, then the left-blocker relation is

```text
a+U^-+v_1=0.
```

If `U^-` is empty, this is a two-atom zero branch `a+v_1=0`. If `U^-` is nonempty, it is a zero-composite branch that can be attacked by A28--A33.

### Proof

The interval from after `P b` to `H-1` is `a U^-`. Add `v_1`. ∎

---

# 6. Right blockers in Case A

Now suppose the A5 blocker lies to the right of the recurrent hit. The interval from the hit to the blocker starts inside `V`.

Let `V_r` be the prefix of `V` ending at the blocker if the blocker lies inside `V`.

---

## Lemma A69.6: right blocker inside proper V-prefix gives zero/pair prefix descent

If the right blocker lies inside a prefix `V_r` of `V`, then the pullback relation has the form

```text
V_r = v_1-u_*.
```

where `u_*` is the last atom before the recurrent hit. Equivalently,

```text
u_*-v_1+V_r=0.
```

Endpoint refinements:

```text
V_r=v_1:
  u_*=0, contradiction.

V_r=v_1W with W a proper prefix of V^+:
  u_*+W=0,
  proper zero-composite descent.

V_r=V:
  V+u_*-v_1=0,
  equivalently V^+ + u_*=0.
```

Thus even the all-of-`V` case is a proper zero-composite or zero-atom contradiction under the corrected endpoint convention.

### Proof

This is the same A5 right-blocker calculation as corrected A67. The hit-boundary atom is `u_*`, and the next atom is `v_1`. ∎

---

## Lemma A69.7: right blocker beyond V gives a bridge zero/signed composite

If the right blocker lies after `V`, then the pullback is

```text
R+V+u_*-v_1=0,
```

where `R` is the external bridge after `V` to the blocker.

Since `V=v_1+V^+`, this reduces to:

```text
R+V^+ + u_*=0.
```

This is a bridge zero-composite crossing the right boundary.

### Proof

The interval from the recurrent hit to the blocker contains all of `V` and the right external bridge. Compare with the A5 atom substitution `v_1-u_*`. ∎

---

# 7. Endpoint case B: U empty, V nonempty

If `U` is empty, the recurrent hit occurs after:

```text
P b a.
```

The hit-boundary atom is:

```text
a.
```

Then:

```text
S'_H=S'_{H-1}+a,
```

and A5 gives:

```text
S'_{H-1}+v_1=S'_{j'}.
```

where `S'_{H-1}` is the endpoint after `P b`.

---

## Lemma A69.8: U-empty left blockers route to zero-composite or bridge classes

For a left blocker,

```text
sum'(j',H-1]+v_1=0.
```

Endpoint table:

```text
at endpoint immediately before a, i.e. after P b:
  v_1=0, contradiction.

after P:
  b+v_1=0.

inside P:
  tail(P)+b+v_1=0.

before P:
  L+P+b+v_1=0.
```

Using `P+b=a`, the bridge branch can also be written:

```text
L+a+v_1=0.
```

All branches route to zero-atom contradiction, proper zero-composite descent, or external bridge routing.

### Proof

When `U` is empty, `H-1` is after `P b`. The left blocker interval is computed directly from that endpoint and then `v_1` is added. ∎

---

## Lemma A69.9: U-empty right blockers route to zero-composite or bridge classes

For a right blocker,

```text
S'_{j'}-S'_H=v_1-a.
```

If `V_r` is a prefix of `V`, then:

```text
V_r=v_1-a,
```

or:

```text
a-v_1+V_r=0.
```

Endpoint table:

```text
immediate first endpoint V_r=v_1:
  a=0, contradiction.

proper prefix V_r=v_1W, W proper in V^+:
  a+W=0,
  proper zero-composite descent.

all of V:
  V+a-v_1=0,
  equivalently V^+ + a=0.

beyond V with bridge R:
  R+V+a-v_1=0,
  equivalently R+V^+ + a=0.
```

All branches route to zero-atom contradiction, proper zero-composite descent, or external bridge routing.

### Proof

The hit-boundary atom is `a`, and the next atom is `v_1`. Apply the right-blocker equation from F7/A5. ∎

---

# 8. Endpoint case C: no post-tail V

If no atom exists after the recurrent hit, then A5 cannot be applied at that hit.

In endpoint avoidance, this case is impossible in a recurrence branch if the recurrent hit is the final endpoint, because:

```text
sigma(S) != f.
```

If a normalization treats the branch as an endpoint immediately after the swapped pair but with additional context elsewhere, the landing is:

```text
x+p+a+b=f.
```

Using:

```text
p=a-b,
```

this becomes:

```text
x+2a=f.
```

This is a scalar/singleton-prefix landing and routes to:

```text
SINGLETON_RECURRENCE / scalar endpoint routing.
```

It is not a new pair-difference recurrence species.

---

# 9. Non-crossing descent theorem

Call a blocker non-crossing if it lies inside:

```text
P,
U^-,
or a proper prefix of V.
```

in Case A, with the `U=empty` endpoint table handled separately.

Call it crossing if it reaches before `P`, beyond `V`, or creates a full-tail bridge branch.

## Proposition A69.10: non-crossing pair-swap recurrence descends

For A33 pair-swap recurrence, every non-crossing transformed A5 blocker pulls back to a smaller zero-composite, suffix-zero, or pair-difference prefix obstruction.

### Proof

Inside-`U^-` blockers descend by Lemma A69.1. Inside-`P` blockers route to smaller zero-composite branches by Lemma A69.2. Inside proper `V` blockers descend by Lemma A69.6 or Lemma A69.9 depending on whether `U` is nonempty. ∎

---

# 10. Crossing routing theorem

## Proposition A69.11: crossing pair-swap recurrence routes to existing mechanisms

Every crossing pair-swap recurrence routes to one of:

```text
bridge signed/equal interval;
zero-composite bridge;
proper zero-composite descent;
singleton/scalar-prefix recurrence;
zero-atom collapse.
```

### Proof

Left bridge crossings are Lemma A69.3 in Case A and Lemma A69.8 in Case B. Pair-neighborhood endpoints are Lemmas A69.4--A69.5 and A69.8. Right endpoint and right bridge crossings are Lemmas A69.6--A69.7 in Case A and Lemma A69.9 in Case B. Endpoint recurrence is Section 8. ∎

---

# 11. Pair-difference recurrence conclusion

Combining Propositions A69.10 and A69.11:

```text
A33 pair-swap recurrence introduces no new local algebraic species.
```

It is routed modulo:

```text
zero-composite descent,
equal/signed interval geometry,
bridge zero-composite machinery,
singleton recurrence,
scalar endpoint routing,
A34 global termination.
```

Thus A34 obligation R3 is no longer standalone.

---

# 12. Remaining recurrence sources

After A69, the remaining recurrence source from A34 is:

```text
R5. cyclic-cut recurrence.
```

Singleton-prefix recurrence R4 has a separate endpoint audit in:

```text
docs/analytic_f7_singleton_endpoint_audit.md
```

and is summarized in F7.

---

## Target A70/A71

A70 analyzes singleton-prefix recurrence.

A71 analyzes cyclic-cut recurrence.

At this stage, the most natural next target is cyclic-cut midpoint characteristic audit, because singleton-prefix atom endpoints have already been packaged in:

```text
docs/analytic_f7_singleton_endpoint_audit.md
```

---

## Current status

Proved here:

```text
1. corrected pair-swap recurrence A5 pullback formulas using U^- / u_*;
2. explicit pair-difference endpoint table for U nonempty and U empty;
3. non-crossing pair-swap blockers descend;
4. crossing blockers route to existing mechanisms;
5. R3 pair-swap recurrence is not a standalone A34 gap.
```

Not proved here:

```text
1. cyclic-cut recurrence;
2. weighted cut-selection;
3. full F9 termination;
4. final endpoint avoidance theorem.
```
