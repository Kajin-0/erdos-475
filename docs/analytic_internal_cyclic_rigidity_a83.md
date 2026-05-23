# Analytic internal cyclic rigidity A83

This note continues from A82.

A82 reduced the last weighted obstruction to:

```text
internal cyclic rigidity of B.
```

The standing weighted core is

```text
A + 2B + C = 0,
```

with `|B|>=2`, after all A56 easy reductions fail and after the atom-middle base case has been eliminated by A80--A81.

A82 showed that if every proper cut of `B` fails to produce descent, then the cut-swap

```text
B=P R -> R P
```

must act like an internal cyclic rotation of `B` which somehow restores the same weighted core without producing an internal zero/equal obstruction.

This note analyzes that possibility.

The result is partial but strong: internal cyclic rigidity forces the internal partial-sum set of `B` to be invariant under a nonzero translation.  For a finite prime field, such invariance is impossible for a proper finite endpoint set unless it is a union of full cosets of the generated subgroup; in `F_p` this forces either all field elements or a collision/zero interval.  Thus any genuine internal cyclic rigidity must be an extreme full-cycle case.  That case is separated for finite verification / final exceptional handling.

No complete endpoint-avoidance proof is claimed here.

---

## 1. Standing setup

Let

```text
B=b_1 b_2 ... b_n,
n>=2,
```

with block sum

```text
b=sum(B).
```

Let internal partial sums of `B` be

```text
T_0=0,
T_i=b_1+...+b_i,
0<=i<=n.
```

Because the ambient ordering is Graham-valid, the internal endpoints of `B` are distinct relative to their basepoint unless there is an internal zero interval.

Thus, in the genuine rigid case, assume:

```text
T_i distinct for 0<=i<=n;
T_i-T_j != 0 for i!=j;
no internal zero interval;
no internal equal-interval/midpoint obstruction already routed by A78.
```

The weighted core is

```text
a+2b+c=0.
```

---

## 2. Internal cyclic rotation

For a cut after `k`, write

```text
P=b_1...b_k,
R=b_{k+1}...b_n.
```

The cut-swap is

```text
P R -> R P.
```

This is the cyclic rotation of `B` based at the endpoint `T_k`.

The internal partial sums of the rotated block `R P` are:

```text
T_i-T_k       for i>k,
b-T_k+T_i     for i<=k.
```

---

## Lemma A83.1: cyclic rotation translates internal endpoint set by `-T_k`

Let

```text
E_B={T_0,T_1,...,T_n}
```

be the internal endpoint set of `B` including both endpoints.

The cyclic rotation at cut `k` produces internal endpoint set

```text
E_B - T_k = {T_i-T_k : 0<=i<=n}
```

with the endpoint `b-T_k+T_i` interpreted modulo `b` along the cyclic traversal.

### Proof

This is the standard cyclic partial-sum formula restricted to the block `B`.  Suffix endpoints subtract `T_k`; wrapped prefix endpoints add the remaining total `b-T_k`.  As elements of `F_p`, both are represented by `T_i-T_k` up to the total endpoint convention. ∎

---

## 3. What exact restoration requires

An exact weighted self-return preserves:

```text
same outer blocks A,C;
same middle block sum b;
same middle support B;
same weighted equation a+2b+c=0.
```

But it may permute the internal order of `B` through a cyclic rotation.

For the same obstruction to be reconstructed with no smaller internal obstruction, the rotated internal endpoint pattern must be indistinguishable from the original internal endpoint pattern relative to the same outer blocks.

This gives an invariance condition:

```text
E_B - T_k = E_B
```

for a nonzero internal endpoint `T_k`.

---

## Lemma A83.2: exact cyclic self-return implies endpoint-set translation invariance

If a nontrivial cyclic rotation of `B` restores the exact same weighted core with no internal zero/equal/pair obstruction, then for the cut value `T_k` one has

```text
E_B - T_k = E_B.
```

### Proof sketch

If the endpoint set changes, then some internal endpoint in the rotated block corresponds to a new endpoint value not present in the original internal pattern. Comparing the old and new endpoint patterns yields either an internal signed interval relation, a pair-difference boundary, or a moved-prefix recurrence inside `B`, all routed by A78/A71. Therefore exact restoration without routed obstruction requires equality of endpoint sets under translation. ∎

---

## 4. Translation-invariant finite endpoint sets in F_p

The following elementary fact is central.

## Lemma A83.3: nonzero translation invariance in F_p forces full-field invariance

Let `E` be a nonempty finite subset of `F_p`.  If

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

The nonzero element `d` generates the additive group of `F_p`, since `p` is prime.  Therefore

```text
E+d=E
```

implies

```text
E+md=E
```

for every integer `m`.  The orbit of any element of `E` under additions of `d` is all of `F_p`.  Hence `F_p subseteq E`, so `E=F_p`. ∎

---

## Corollary A83.4: proper endpoint sets cannot be internally cyclic-rigid

If the internal endpoint set

```text
E_B={T_0,...,T_n}
```

is a proper subset of `F_p`, then no nontrivial cyclic rotation of `B` can restore the exact same internal endpoint set without producing a routed obstruction.

### Proof

If exact restoration required `E_B-T_k=E_B` with `T_k != 0`, Lemma A83.3 would force `E_B=F_p`, contradicting properness.  If `T_k=0`, then `B` has an internal zero-prefix at the cut, contradicting the genuine rigid hypothesis. ∎

---

# 5. Full-field endpoint-set case

The only remaining case is

```text
E_B=F_p.
```

Since `E_B` has `n+1` endpoints, this requires

```text
n+1 >= p.
```

But `B` is a subblock of an ordering of a subset of `F_p^*`, whose total number of atoms is at most `p-1`.  Therefore

```text
n <= p-1.
```

Thus

```text
n+1 <= p.
```

Combining gives:

```text
n+1=p,
```

so

```text
|B|=p-1.
```

---

## Lemma A83.5: full-field endpoint rigidity forces B to use all p-1 atoms

If

```text
E_B=F_p,
```

then

```text
|B|=p-1.
```

and `B` has exactly one endpoint at every field element.

### Proof

The endpoint set has size at most `|B|+1`.  Graham-validity inside `B` gives distinct endpoints, so `|E_B|=|B|+1`.  If `E_B=F_p`, then `|B|+1=p`. ∎

---

## Lemma A83.6: full-field B leaves no nonempty outside block in a proper subset ordering

If `B` has length `p-1`, then `B` contains all atoms of `F_p^*` available in a full-set instance.  In a subset instance, it contains the entire subset.

Therefore the outside blocks `A` and `C` must be empty unless the ambient multiset has repeated atoms, which is not allowed for subset orderings.

### Proof

The theorem concerns subsets of `F_p^*`, so there are at most `p-1` atoms total.  If `B` has length `p-1`, no atom remains for `A` or `C`. ∎

---

## Lemma A83.7: full-field B contradicts genuine weighted core assumptions

If `A` and `C` are empty, the weighted core becomes

```text
2b=0.
```

In odd characteristic this implies

```text
b=0.
```

But then `B` is zero-sum, and the whole block `B` is a zero interval/prefix collapse, not a genuine weighted core.

### Proof

With `A=C=empty`, `a=c=0`.  The weighted relation is `2b=0`; divide by 2. ∎

---

# 6. Main internal cyclic rigidity theorem

## Theorem A83.8: internal cyclic rigidity of B is impossible in the genuine weighted core

Let

```text
A+2B+C=0
```

be a genuine weighted core over an odd prime field, with `|B|>=2`, no internal zero/equal obstruction in `B`, and no A56 easy reduction.

Then `B` cannot be internally cyclic-rigid in the sense of A82.

### Proof

Assume internal cyclic rigidity.  By A82, every nontrivial cyclic rotation of `B` restores the same weighted core without producing a routed obstruction.  For any nontrivial cut, Lemma A83.2 gives endpoint-set translation invariance

```text
E_B-T_k=E_B.
```

Since there is no internal zero prefix, `T_k != 0`.  Lemma A83.3 forces `E_B=F_p`.  Lemma A83.5 gives `|B|=p-1`.  Lemma A83.6 then forces `A=C=empty`.  Lemma A83.7 gives zero collapse, contradicting the genuine weighted hypothesis. ∎

---

# 7. Consequence for weighted cut-selection

A79 reduced weighted cut-selection to:

```text
atom-middle base case;
cut-rigid weighted self-return.
```

A80--A81 eliminated atom-middle.

A82 reduced cut-rigid weighted self-return to internal cyclic rigidity of `B`.

A83 eliminates internal cyclic rigidity.

Therefore the weighted core is now controlled by induction on `|B|` plus the non-weighted acyclic graph A78.

---

## Theorem A83.9: weighted core cut-selection is controlled modulo A78

Every genuine weighted core

```text
A+2B+C=0
```

either:

```text
1. routes by an A56 easy reduction;
2. is atom-middle and routes by A80--A81;
3. has |B|>=2 and admits a proper cut whose A60 cut-swap succeeds, collapses, enters A78, or returns to a smaller weighted core;
4. terminates by induction on |B|.
```

### Proof

If `|B|=1`, use A80--A81.  If `|B|>=2`, A79 shows any fixed cut is useful unless it returns to a weighted core.  Returns with smaller middle descend.  If all cuts fail to descend, A82 gives internal cyclic rigidity.  A83.8 rules this out.  Since `|B|` is a positive integer and decreases on weighted returns, induction terminates. ∎

---

# 8. Consequence for the global proof architecture

Combining A78 and A83.9:

```text
non-weighted obstruction graph: acyclic by A78;
weighted core: cut-selected into A78 or smaller weighted core by A83.9.
```

Thus the remaining proof obligations are now mostly assembly/certification:

```text
1. final endpoint-avoidance theorem assembly;
2. verification of odd-prime assumptions and p=2 handling;
3. finite verification bridge for small/exceptional cases;
4. audit of all local lemmas for hidden assumptions.
```

---

# 9. Target A84

A84 should state the assembled endpoint-avoidance theorem conditional on the A1--A83 lemmas.

It should explicitly list assumptions:

```text
p odd prime;
A subset F_p^*;
f != sigma(A);
Graham-valid orderings use distinct partial sums;
local routing lemmas A1--A83 accepted.
```

Then prove:

```text
minimal counterexample -> active obstruction -> routed graph -> A78/A83 termination -> success or contradiction.
```

After that, A85 should handle finite/exceptional cases and connect endpoint avoidance back to strong nonzero-sum and Erdős 475.

---

## Current status

Proved/refined here:

1. exact cyclic rotations of B translate internal endpoint set;
2. exact cyclic self-return implies endpoint-set translation invariance;
3. nonzero translation-invariant endpoint set in F_p is all of F_p;
4. full-field endpoint set forces |B|=p-1 and no outside blocks;
5. full-field case collapses, contradicting genuine weighted core;
6. internal cyclic rigidity is impossible;
7. weighted core cut-selection is controlled modulo A78.

Not proved here:

1. final endpoint-avoidance theorem assembly;
2. finite/exceptional characteristic bridge;
3. audit of all previous local lemmas.
