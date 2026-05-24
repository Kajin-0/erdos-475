# Analytic cut-rigid to strong-exact self-return A90

This note continues from A89.

A89 hardened the A83 endpoint-set invariance step and found the precise condition needed:

```text
strong exact internal cyclic self-return
    -> E_B - T_k = E_B.
```

It also clarified that this does **not** follow merely from preserving the weighted equation

```text
A + 2B + C = 0.
```

Therefore the remaining weighted bottleneck is:

```text
cut-rigid weighted self-return
    -> strong exact internal cyclic self-return.
```

A90 analyzes that implication.

The result is diagnostic rather than final: the weak cut-rigid definition from A79--A82 is insufficient to imply strong exactness.  A stronger notion, pattern-rigid weighted self-return, does imply strong exactness and is eliminated by A89.  Thus the remaining weighted gap is narrowed to proving that every weak cut-rigid return is either pattern-rigid or produces a non-weighted obstruction/smaller weighted core.

---

## 1. Standing weighted core

Let

```text
X A B C Y
```

be a genuine weighted core with

```text
a+2b+c=0,
```

where

```text
a=sum(A),
b=sum(B),
c=sum(C),
|B|>=2.
```

Assume A56 easy reductions fail:

```text
b != 0,
a+b != 0,
b+c != 0,
a != c,
no transported-prefix/tail rewrite.
```

For a proper cut

```text
B=P R,
P,R nonempty,
```

the A60 cut-swap is

```text
A P R C -> A R P C.
```

---

## 2. Weak cut-rigid self-return

The weak notion used in A79--A82 can be summarized as follows.

## Definition A90.1: weak cut-rigid weighted self-return

A weighted core is weakly cut-rigid if for every proper cut `B=P R`, the A60 cut-swap and subsequent routing do not produce:

```text
1. success;
2. collapse;
3. non-weighted termination;
4. a returned weighted core with smaller middle length.
```

Instead, the routing returns to a genuine weighted core whose doubled middle has length at least `|B|`.

This definition tracks:

```text
block sums,
weighted-core type,
middle length.
```

It does **not** automatically track:

```text
internal endpoint set of B,
order of internal endpoints,
labels of recurrent/blocker endpoints,
identity of displayed collision families.
```

---

## 3. Strong exact self-return

A89 introduced the stronger condition needed for endpoint-set invariance.

## Definition A90.2: strong exact internal cyclic self-return

A cut after `P` is strong exact if the cut-swap

```text
P R -> R P
```

returns to the same weighted core while preserving:

```text
1. same outer basepoint before B;
2. same middle endpoints 0 and b;
3. same internal endpoint set E_B;
4. same obstruction labels attached to internal endpoints;
5. no internal zero/equal/pair obstruction during the return.
```

By A89:

```text
strong exact self-return -> impossible in a genuine weighted core.
```

---

# 4. Weak rigidity does not imply strong exactness by definition

## Lemma A90.3: weak cut-rigidity lacks endpoint-set data

Weak cut-rigidity does not by itself imply

```text
E_{rot_k(B)}=E_B.
```

### Proof

Definition A90.1 records only that routing returns to some genuine weighted core with middle length not smaller than `|B|`.  It does not state that the returned middle block has the same internal endpoint set as the original `B`.  Two orderings can have the same total block sum and same length but different internal endpoint sets.  Therefore endpoint-set equality is not a logical consequence of weak cut-rigidity alone. ∎

---

## Corollary A90.4: A83/A89 cannot close weak cut-rigidity without an additional lemma

The A89 endpoint-set argument eliminates strong exact self-return, not weak cut-rigid self-return.  Therefore a proof of weighted closure must add a lemma showing that every weak cut-rigid self-return either:

```text
1. is strong exact / pattern-rigid;
2. produces a non-weighted obstruction;
3. produces a smaller weighted core;
4. collapses.
```

### Proof

Immediate from Lemma A90.3 and A89. ∎

---

# 5. Pattern-rigid self-return

The missing intermediate concept is endpoint-pattern preservation.

## Definition A90.5: pattern-rigid weighted self-return

A weak cut-rigid return at cut `B=P R` is pattern-rigid if the returned weighted core has:

```text
1. same outer blocks A and C;
2. same middle support interval B;
3. same total middle sum b;
4. same internal endpoint set E_B relative to the same basepoint;
5. same boundary endpoints between A|B and B|C;
6. no new internal zero/equal/pair obstruction.
```

Pattern-rigid is weaker than preserving the full ordered list of endpoints, but strong enough for A89.

---

## Lemma A90.6: pattern-rigid self-return implies strong exact self-return for A89 purposes

If a cut-rigid return is pattern-rigid in the sense of Definition A90.5, then it satisfies the strong exactness hypotheses needed in A89.

### Proof

A89 requires preservation of the same basepoint, middle endpoints, internal endpoint set, and absence of internal routed obstructions.  These are exactly included in Definition A90.5.  Preservation of obstruction labels is only needed to prevent silent endpoint relabeling; if labels change, the changed labels create a moved-prefix or pair-difference branch, which is non-weighted.  Thus pattern-rigidity is sufficient for the A89 endpoint-set invariance argument. ∎

---

## Proposition A90.7: pattern-rigid weighted self-return is impossible

A genuine weighted core cannot have a pattern-rigid self-return at any proper cut of `B`.

### Proof

By Lemma A90.6, pattern-rigid self-return satisfies A89's strong exactness condition.  A89.11 rules out strong exact internal cyclic self-return in a genuine weighted core. ∎

---

# 6. Non-pattern weak returns

It remains to understand weak cut-rigid returns that are not pattern-rigid.

A non-pattern return must change at least one of:

```text
1. outer blocks A,C;
2. middle support interval B;
3. internal endpoint set E_B;
4. boundary endpoints A|B or B|C;
5. endpoint labels / collision family labels.
```

Each change should create a detectable obstruction.

---

## Lemma A90.8: change of middle support gives smaller/larger-middle alternative

If the returned weighted core does not have the same middle support interval `B`, then either:

```text
1. its doubled middle is contained in P or R, giving smaller middle length;
2. it properly contains B, giving transported-prefix/external-bridge alternatives from A82.4;
3. it overlaps B without equality, giving proper-overlap bridge/equal interval descent by A74;
4. it is disjoint from B, giving separated-equal/external collision routing by A62/A75.
```

### Proof sketch

Compare the returned doubled middle interval `M` with the original `B`.  The possibilities are containment, proper overlap, disjointness, or equality.  Containment inside one cut side gives smaller middle.  Proper containment of `B` by `M` is A82.4.  Proper overlap is an interval-uncrossing branch.  Disjointness is external/separated-equal. ∎

---

## Lemma A90.9: change of outer blocks gives transported-prefix or external collision data

If the returned weighted core has the same middle support `B` but different outer blocks `A',C'`, then subtracting

```text
a+2b+c=0
```

from

```text
a'+2b+c'=0
```

gives

```text
(a'-a)+(c'-c)=0.
```

This is an equal/signed interval or two-piece zero relation involving the changed outer material.

### Proof

Subtract the two weighted equations.  Since the doubled middle is the same, the `2b` terms cancel.  The remaining equation is a zero-composite/signed interval relation in the outer differences. ∎

### Consequence

Changing outer blocks cannot be an invisible weighted self-return.  It exposes a non-weighted obstruction unless the outer changes are empty.

---

## Lemma A90.10: change of internal endpoint set creates an internal moved-prefix obstruction

Assume the returned weighted core has the same outer blocks and same middle support `B`, but the internal endpoint set changes:

```text
E_new != E_B.
```

Then there exists an internal endpoint value appearing in one pattern and not the other.  Comparing the two endpoint patterns produces one of:

```text
1. internal zero interval;
2. internal equal interval;
3. internal pair-difference boundary;
4. internal singleton/prefix recurrence.
```

### Proof sketch

Let `e` be an endpoint value in the symmetric difference of the two internal endpoint sets.  The routed return identifies a weighted core on the same outer endpoints, so the changed endpoint value must be crossed by a collision, forbidden hit, or blocker relation during the return.  The first such event is local inside `B` and has A5/A64 form.  Its pullback is a zero/equal/pair/singleton branch. ∎

### Status

This lemma is the new critical item.  It is plausible and structurally necessary, but it must be hardened with an explicit first-changed-endpoint argument.

---

## Lemma A90.11: change of boundary endpoints gives A56 easy reduction or non-weighted branch

If the returned core has the same internal middle support but different boundary endpoints at `A|B` or `B|C`, then the change is an adjacent transfer of material between `A` and `B` or between `B` and `C`.  Subtracting the weighted equations gives a coefficient-2 boundary relation of A56 type or a two-piece zero relation.

### Proof sketch

Moving a boundary piece `D` from `A` into `B`, or from `B` into `A`, changes the weighted equation by one copy or two copies of `D`.  The difference equation has form

```text
D=0,
A+D=0,
D+C=0,
or transported-prefix/tail coefficient pattern.
```

These are exactly A56 easy reductions or zero-composite branches. ∎

---

## Lemma A90.12: change of endpoint labels gives recurrence routing

If endpoint values are preserved but their obstruction labels change, then some displayed collision/recurrent endpoint has moved from one family to another.  The first such label change is a pair-swap, singleton-prefix, or cyclic-cut recurrence branch already routed by A69--A71.

### Proof sketch

Labels are attached to displayed families: left block, middle prefix, right block, external bridge, etc.  A label change with same endpoint value means the same field value is achieved by two different displayed intervals.  Their difference gives equal interval, pair-difference, or zero-composite data.  If the equality appears only after a transformed Graham-valid ordering, it is a recurrence branch routed by A69--A71. ∎

---

# 7. Weak-to-pattern reduction theorem, conditional

## Theorem A90.13: weak cut-rigid self-return reduces to pattern-rigid or a routed obstruction

Assume Lemma A90.10 is hardened.  Then every weak cut-rigid weighted self-return either:

```text
1. is pattern-rigid;
2. returns to a smaller weighted middle;
3. triggers A56 transported-prefix/easy reduction;
4. produces a non-weighted obstruction handled by A78;
5. collapses.
```

### Proof

If the return is pattern-rigid, done.  If middle support changes, use Lemma A90.8.  If outer blocks change, use Lemma A90.9.  If internal endpoint set changes, use Lemma A90.10.  If boundary endpoints change, use Lemma A90.11.  If only labels change, use Lemma A90.12.  These cases exhaust failure of pattern-rigidity. ∎

---

## Corollary A90.14: weighted closure follows from hardening Lemma A90.10

If Lemma A90.10 is proved in full detail, then the weighted core branch closes:

```text
weak cut-rigid return
  -> pattern-rigid or routed obstruction
  -> pattern-rigid impossible by A89
  -> routed obstruction handled by A78/A56/smaller weighted induction.
```

### Proof

Combine Theorem A90.13 with Proposition A90.7 and the weighted induction framework A79--A83. ∎

---

# 8. Revised bottleneck after A90

A90 reduces the remaining weighted problem to one precise local hardening task:

```text
A90.10 first-changed-endpoint lemma.
```

That lemma must prove:

```text
same outer blocks + same middle support + changed internal endpoint set
    -> internal non-weighted obstruction or smaller weighted core.
```

This is a better target than the earlier broad phrase “cut-rigid implies strong exact.”

---

# 9. Target A91

A91 should harden Lemma A90.10.

Suggested title:

```text
First-changed-endpoint lemma for weighted self-return A91
```

Required structure:

1. Define two internal endpoint sequences for `B` and `rot_k(B)`:

```text
E_old=(T_0,...,T_n),
E_new=(T'_0,...,T'_n).
```

2. Assume same outer blocks and same middle support, but `E_new != E_old`.

3. Let `r` be the first index where the endpoint value/family differs.

4. Show the first difference creates one of:

```text
old endpoint = new endpoint with different interval -> equal interval;
new endpoint collides with old external endpoint -> external collision A62;
new endpoint is forbidden -> recurrence A64/A69--A71;
new endpoint is novel and no collision/forbidden -> transformed ordering progresses, contradicting self-return minimality.
```

5. Conclude changed endpoint pattern cannot be invisible.

---

## Current status after A90

Proved here:

```text
1. weak cut-rigidity alone does not imply endpoint-set invariance;
2. pattern-rigid self-return implies strong exact self-return;
3. pattern-rigid self-return is impossible by A89;
4. weak non-pattern returns reduce to explicit change cases;
5. the remaining weighted bottleneck is the first-changed-endpoint lemma A90.10.
```

Still open:

```text
1. hard proof of A90.10;
2. full weighted closure after A91;
3. final endpoint-avoidance theorem without conditional weighted gap.
```
