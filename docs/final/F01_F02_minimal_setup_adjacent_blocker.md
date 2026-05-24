# F1--F2 minimal counterexample setup and adjacent blocker lemma

This file continues the final-proof extraction phase.

F1 and F2 provide the starting point for the endpoint-avoidance proof.  They extract the minimal-counterexample setup and the first local obstruction from:

```text
A4--A5   adjacent forbidden-hit obstruction
A34      recurrence/minimality status
A84      endpoint-avoidance assembly
F3       obstruction state machine
F7       recurrence routing theorem
F9       non-weighted termination theorem
```

This is an extracted draft, not yet the final manuscript version.  The main remaining risk is ensuring the existence of the starting Graham-valid ordering is stated correctly.

---

## F1.1. Endpoint-avoidance setting

Let `p` be an odd prime.  Let

```text
S subset F_p^*
```

be finite, and let

```text
sigma=sum(S).
```

Let

```text
f in F_p,
f != sigma.
```

Endpoint avoidance asks for an ordering

```text
R=(r_1,...,r_t)
```

of `S` such that:

```text
1. the nonempty partial sums S_1,...,S_t are pairwise distinct;
2. no nonempty partial sum equals f.
```

Here

```text
S_i=r_1+...+r_i.
```

The final endpoint is never the forbidden endpoint because

```text
S_t=sigma != f.
```

---

## F1.2. Graham-valid starting ordering

The local obstruction program assumes a Graham-valid ordering exists.  This is the classical Graham rearrangement target and is also the final Erdős 475 conclusion.

For endpoint avoidance, the intended minimal-counterexample method is:

```text
Among all Graham-valid orderings of S, choose one with the earliest possible first forbidden hit.
```

Thus the proof requires one of the following inputs:

```text
Input G. Graham-valid ordering exists independently;
```

or a preliminary reduction that constructs one before endpoint avoidance begins.

In the full theorem chain, endpoint avoidance is stronger than Graham-validity.  Therefore the final proof must not circularly assume Erdős 475 unless the endpoint-avoidance theorem is explicitly conditional on Graham-valid existence.

---

## Audit flag F1.G

This is a critical audit flag:

```text
The final manuscript must justify the existence of at least one Graham-valid ordering before minimizing the forbidden hit.
```

Possible resolutions:

```text
1. prove a weak Graham-valid existence lemma separately;
2. run the same obstruction argument from an arbitrary ordering using first collision/forbidden obstruction;
3. state endpoint avoidance as strengthening conditional on Graham-valid existence, then combine with an independent argument.
```

Until this is resolved, F1 is an extracted draft, not final.

---

## F1.3. Minimal first-hit ordering

Assume a Graham-valid ordering exists.

Suppose endpoint avoidance fails.  Then every Graham-valid ordering of `S` has at least one nonempty partial sum equal to `f`.

Choose a Graham-valid ordering

```text
R=(r_1,...,r_t)
```

such that the first forbidden-hit index

```text
h=min{i : S_i=f}
```

is minimal among all Graham-valid orderings.

Since

```text
S_t=sigma != f,
```

we have

```text
1 <= h < t.
```

Let the atom after the forbidden hit be

```text
z=r_{h+1}.
```

---

## Lemma F1.1: minimal first-hit ordering has a next atom

In the minimal first-hit setup, the forbidden hit is not final, so `r_{h+1}` exists.

### Proof

The final partial sum is `S_t=sigma`, and `sigma != f`.  Therefore the first index `h` with `S_h=f` satisfies `h<t`. ∎

---

# F2. Adjacent blocker lemma

The first local move is the adjacent swap at the forbidden hit:

```text
... r_h r_{h+1} ...  ->  ... r_{h+1} r_h ...
```

Let

```text
y=r_h,
z=r_{h+1}.
```

The original local endpoints are:

```text
S_{h-1},
S_h=S_{h-1}+y=f,
S_{h+1}=S_{h-1}+y+z.
```

After swapping `y` and `z`, the transformed local endpoints are:

```text
S'_{h-1}=S_{h-1},
S'_h=S_{h-1}+z,
S'_{h+1}=S_{h-1}+z+y=S_{h+1}.
```

All endpoints after both atoms are unchanged.

---

## Lemma F2.1: adjacent swap either succeeds, collides, or recurs

Apply the adjacent swap at the first forbidden hit.  The transformed ordering is exactly one of:

```text
1. Graham-valid and avoids f;
2. not Graham-valid, hence has a collision involving the moved endpoint S_{h-1}+z;
3. Graham-valid but recurrent, with first forbidden hit at some transformed endpoint.
```

### Proof

The transformed ordering either has pairwise distinct nonempty partial sums or does not.  If it does and avoids `f`, it succeeds.  If it does and hits `f`, it is recurrent.  If it does not, it has a collision.  Since all endpoints except the moved local endpoint are unchanged, any new collision must involve the moved endpoint. ∎

---

## Lemma F2.2: adjacent collision gives the blocker equation

If the adjacent swap is not Graham-valid, then there exists an index `j` such that

```text
S_{h-1}+z = S_j.
```

Equivalently,

```text
S_{h-1}+r_{h+1}=S_j.
```

This is the adjacent blocker equation.

### Proof

The only new endpoint value created by the adjacent swap is `S_{h-1}+z`.  Since the transformed ordering is not Graham-valid and the original ordering was Graham-valid, this new endpoint must equal some old endpoint `S_j`. ∎

---

## Lemma F2.3: adjacent recurrence gives an earlier-hit contradiction unless routed through a moved endpoint

If the adjacent swap is Graham-valid but recurrent, then the new forbidden hit must occur at the moved endpoint

```text
S_{h-1}+z=f
```

or at an endpoint whose value changed because of the move.  In the adjacent swap, this is only the moved endpoint.

If the recurrent hit occurs at an unchanged endpoint, then the old ordering already had the same forbidden hit.  If its index is earlier than `h`, this contradicts minimality.  If it is at or after `h`, the branch is a recurrence state routed by F7.

### Proof

All endpoints except the moved endpoint and the unchanged post-pair endpoint retain their values.  The post-pair endpoint was already present in the original ordering.  Therefore a genuinely new forbidden hit must occur at the moved endpoint.  Unchanged forbidden hits are handled by minimality or recurrence bookkeeping. ∎

---

## Lemma F2.4: first local obstruction exists

Assume endpoint avoidance fails for the chosen minimal first-hit ordering.  Then the adjacent swap at the first forbidden hit produces either:

```text
1. success, contradicting failure of endpoint avoidance;
2. a collision blocker equation S_{h-1}+r_{h+1}=S_j;
3. a recurrence state routed by F7.
```

Thus a non-successful minimal counterexample produces an initial obstruction state in the F3 state machine.

### Proof

By Lemma F2.1, the adjacent swap either succeeds, collides, or recurs.  Success contradicts the assumption that no Graham-valid ordering avoids `f`.  Collision gives Lemma F2.2.  Recurrence gives Lemma F2.3 and is routed by F7. ∎

---

## F2.5. Blocker geometry

From the blocker equation

```text
S_{h-1}+z=S_j,
```

there are two basic geometries.

### Left blocker: `j<h-1`

Then

```text
S_{h-1}-S_j+z=0.
```

The interval from `j+1` to `h-1`, together with atom `z`, gives a zero-composite relation.

### Right blocker: `j>h-1`

Using `S_h=S_{h-1}+y=f`, the equation gives signed pair data of the form

```text
y-z+sum(h,j]=0
```

or an equivalent right-blocker pair-difference relation, depending on the endpoint convention.

These are precisely the inputs routed by F4 and F7.

---

## Lemma F2.5: blocker geometry enters known classes

Every adjacent blocker equation routes to one of:

```text
zero-composite,
pair-difference boundary,
signed interval,
external collision if the blocker lies outside the displayed local window,
recurrence if generated by a transformed forbidden hit,
weighted-core normal form if coefficient-2 data later survives normalization.
```

### Proof

Left blockers give zero-composite equations.  Right blockers give pair-difference/signed interval equations after subtracting the hit endpoint.  If the blocker lies outside the current displayed window, F6 external-collision routing applies.  If the blocker arises after a transformed forbidden hit, F7 recurrence routing applies.  Any later coefficient-2 normal form is handled by F10/F11. ∎

---

## F1--F2.6. Interface with F12

F12 will use F1--F2 as follows:

```text
1. assume endpoint avoidance fails;
2. choose minimal first-hit Graham-valid ordering;
3. perform adjacent swap at first forbidden hit;
4. if success, contradiction;
5. otherwise obtain initial obstruction state;
6. apply F9/F11 termination to force success or contradiction.
```

---

## F1--F2.7. Remaining extraction risks

Before final manuscript status:

```text
R1. Resolve the Graham-valid starting-ordering issue F1.G.
R2. State endpoint cases h=0, h=t clearly. Here h>=1 and h<t.
R3. Check collision index j cannot equal h in a way that forces z=0 or y=z degeneracy.
R4. Align right-blocker sign conventions with F7.
R5. Decide whether adjacent recurrence should be routed immediately by F7 or included in the initial obstruction class table.
```

---

## F1--F2.8. Extraction status

```text
Status: extracted draft.
Risk: ORANGE because of F1.G.
Next recommended extraction: F12 endpoint avoidance theorem, with F1.G explicitly marked.
```
