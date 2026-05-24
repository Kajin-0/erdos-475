# F13 endpoint avoidance, strong nonzero-sum, and Erdős 475 dependency

This file completes the first pass of final-proof extraction.

F13 extracts the theorem-level dependency chain from:

```text
A1--A3   early theorem reductions
A85      theorem dependency audit
A86      finite and exceptional cases
F12      endpoint avoidance theorem extraction
```

The purpose is to separate two different statements:

```text
1. Clean implication chain:
   endpoint avoidance -> strong nonzero-sum -> Erdős 475.

2. Current extracted proof status:
   F12 endpoint avoidance is conditional on Input G, so the present extracted package is not yet an unconditional proof of Erdős 475.
```

This distinction is essential.

---

## F13.1. Graham-valid ordering

Let `S subset F_p^*` be finite, and let

```text
R=(r_1,...,r_t)
```

be an ordering of `S`.

Write partial sums:

```text
S_i(R)=r_1+...+r_i,
S_0(R)=0.
```

An ordering is Graham-valid if the nonempty partial sums

```text
S_1(R),...,S_t(R)
```

are pairwise distinct.

Erdős 475 / Graham's rearrangement problem asks for a Graham-valid ordering for every finite subset `S subset F_p^*`.

---

## F13.2. Endpoint avoidance

Endpoint avoidance says:

For every forbidden value

```text
f != sigma(S),
```

there exists a Graham-valid ordering `R` of `S` such that

```text
f notin {S_1(R),...,S_t(R)}.
```

The condition `f != sigma(S)` is necessary because the final nonempty partial sum is always

```text
S_t(R)=sigma(S).
```

---

## F13.3. Strong nonzero-sum theorem

The strong nonzero-sum theorem says:

If

```text
sigma(S) != 0,
```

then there exists an ordering `R` of `S` such that

```text
S_0(R),S_1(R),...,S_t(R)
```

are pairwise distinct.

Equivalently:

```text
1. R is Graham-valid;
2. no nonempty partial sum equals 0.
```

---

# 2. Clean theorem implications

## Proposition F13.1: endpoint avoidance implies strong nonzero-sum

Assume endpoint avoidance holds for `F_p`.  Then the strong nonzero-sum theorem holds for `F_p`.

### Proof

Let `S subset F_p^*` satisfy

```text
sigma(S) != 0.
```

Apply endpoint avoidance with forbidden value

```text
f=0.
```

This is valid because `0 != sigma(S)`.  Endpoint avoidance gives a Graham-valid ordering `R` whose nonempty partial sums avoid `0`.

Therefore the list

```text
S_0(R)=0,S_1(R),...,S_t(R)
```

is pairwise distinct: the nonempty partial sums are pairwise distinct by Graham-validity, and none of them equals `0`.  This is the strong nonzero-sum theorem. ∎

---

## Proposition F13.2: strong nonzero-sum implies Erdős 475

Assume the strong nonzero-sum theorem holds for all finite subsets of `F_p^*`.  Then Erdős 475 holds over `F_p`.

### Proof

Let

```text
S subset F_p^*
```

be finite.

There are two cases.

### Case 1: `sigma(S) != 0`

Apply the strong nonzero-sum theorem directly to `S`.  It gives an ordering whose extended partial sums

```text
S_0,S_1,...,S_t
```

are pairwise distinct.  In particular, the nonempty partial sums are pairwise distinct, so the ordering is Graham-valid.

### Case 2: `sigma(S)=0`

If `S` is empty, the empty ordering is Graham-valid.

If `S` is nonempty, choose an atom

```text
x in S
```

and set

```text
T=S\{x}.
```

Then

```text
sigma(T)=sigma(S)-x=-x != 0,
```

because `x in F_p^*`.

Apply the strong nonzero-sum theorem to `T`.  There is an ordering

```text
t_1,...,t_m
```

such that

```text
0,T_1,...,T_m
```

are pairwise distinct.

Append `x` at the end:

```text
t_1,...,t_m,x.
```

The nonempty partial sums are

```text
T_1,...,T_m,T_m+x.
```

Since

```text
T_m=sigma(T)=-x,
```

the final partial sum is

```text
T_m+x=0.
```

The values `T_1,...,T_m` are pairwise distinct and none is zero.  Therefore

```text
T_1,...,T_m,0
```

are pairwise distinct.  Hence the appended ordering is Graham-valid for `S`. ∎

---

## Corollary F13.3: endpoint avoidance implies Erdős 475

Endpoint avoidance implies Erdős 475 over `F_p`.

### Proof

Endpoint avoidance implies strong nonzero-sum by Proposition F13.1.  Strong nonzero-sum implies Erdős 475 by Proposition F13.2. ∎

---

# 3. Exceptional case p=2

For `p=2`,

```text
F_2^*={1}.
```

The only subsets are:

```text
empty set,
{1}.
```

The empty set has the empty ordering.  The set `{1}` has ordering `(1)`, with one nonempty partial sum, hence pairwise distinct.

## Lemma F13.4: Erdős 475 holds for p=2

Erdős 475 is true over `F_2`.

### Proof

Direct enumeration as above. ∎

---

## Lemma F13.5: endpoint avoidance also holds for p=2

The endpoint-avoidance statement holds over `F_2`.

### Proof

For `S=empty`, `sigma=0`, and the only admissible forbidden value is `f=1`; there are no nonempty partial sums.

For `S={1}`, `sigma=1`, and the only admissible forbidden value is `f=0`; the only nonempty partial sum is `1`, which avoids `0`. ∎

---

# 4. Current extracted proof status

F12 currently proves endpoint avoidance only under:

```text
Input G: at least one Graham-valid ordering of S exists.
```

Therefore the extracted proof currently gives the conditional strengthening:

```text
Graham-valid existence for S
  -> endpoint avoidance for S and every f != sigma(S)
  -> strong nonzero-sum for nonzero-total S.
```

But it does not yet give an unconditional proof of Erdős 475, because using Graham-valid existence as input is circular for proving Graham-valid existence.

---

## Theorem F13.6: current conditional strengthening theorem

Assume:

```text
1. p is odd;
2. final lemmas F1--F12 are valid;
3. Input G holds for S.
```

Then endpoint avoidance holds for `S`.  Consequently, if `sigma(S) != 0`, then `S` has a strong nonzero-sum ordering.

### Proof

Endpoint avoidance follows from F12.  Strong nonzero-sum follows from Proposition F13.1. ∎

---

## Not-yet-theorem F13.X: unconditional Erdős 475

The statement

```text
F1--F12 imply Erdős 475 for all prime fields
```

is not currently justified, because F12 depends on Input G.

To turn the extracted proof into an unconditional proof of Erdős 475, one must remove or independently prove Input G without using Erdős 475.

---

# 5. Required repair for unconditional proof

The recommended repair is to replace Input G by a simultaneous defect-minimization setup.

## Route C: simultaneous minimization

Minimize over all orderings of `S` a defect vector such as:

```text
D(R)=(
  collision_count,
  first_collision_span,
  first_forbidden_hit_index,
  active_obstruction_span,
  active_obstruction_type_rank
).
```

Then prove that the first local move either:

```text
1. decreases D(R);
2. enters the same F3 obstruction state machine;
3. reaches a Graham-valid f-avoiding ordering;
4. reaches contradiction.
```

This would start the proof from an arbitrary ordering, not from an already Graham-valid ordering.

If successful, F12 becomes unconditional and Corollary F13.3 gives Erdős 475.

---

## F13.7. Final proof-status statement

Current status of the extracted proof package:

```text
F3--F11: obstruction-routing and termination engine, extracted but still requiring sign/endpoint audit.
F12: endpoint avoidance conditional on Graham-valid existence.
F13: theorem implication chain clean, but unconditional Erdős 475 not yet established.
```

The honest current claim is:

```text
If the routing lemmas are hardened and Input G is resolved,
then endpoint avoidance follows;
then strong nonzero-sum follows;
then Erdős 475 follows.
```

---

## F13.8. Remaining extraction risks

Before any public proof claim:

```text
R1. Resolve Input G / starting-ordering gap.
R2. Harden F11 weighted termination.
R3. Harden F9 non-weighted measure/rank table.
R4. Complete sign and endpoint audit in F4--F8 and F10--F11.
R5. Optionally add finite verification certificates, clearly marked as advisory unless required.
```

---

## F13.9. Recommended next file

The next useful file should directly attack the starting-ordering gap:

```text
docs/final/F00_arbitrary_ordering_defect_start.md
```

Goal:

```text
Replace Input G by a defect-minimization starting theorem over all orderings.
```

Minimum contents:

```text
1. define defect vector D(R);
2. prove minimizer exists;
3. show if D(R)=0, endpoint avoidance succeeds;
4. analyze first defect if D(R)>0;
5. connect first defect to F3 obstruction state machine.
```

---

## F13.10. Extraction status

```text
Status: extracted theorem-dependency draft.
Risk: GREEN for implication chain.
Risk: RED for unconditional Erdős 475 until Input G is resolved.
```
