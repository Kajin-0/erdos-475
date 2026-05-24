# F12 endpoint avoidance theorem

This file continues the final-proof extraction phase.

F12 extracts the endpoint-avoidance assembly theorem from the proof program, backed mainly by:

```text
F1--F2  minimal setup and adjacent blocker lemma
F3      obstruction state machine
F4      local zero/equal/pair descent
F5      separated-equal and midpoint routing
F6      external collision theorem
F7      recurrence routing theorem
F8      bridge/gap descent theorem
F9      non-weighted termination theorem
F10     weighted normal form and cut-swap theorem
F11     weighted cut-selection and termination theorem
A84     endpoint-avoidance assembly
```

This is an extracted draft, not a final manuscript theorem.  It is explicitly conditional on the starting Graham-valid ordering issue identified in F1.

---

## F12.1. Endpoint-avoidance statement

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

The endpoint-avoidance theorem states that there exists an ordering

```text
R=(r_1,...,r_t)
```

of `S` such that:

```text
1. the nonempty partial sums S_1,...,S_t are pairwise distinct;
2. no nonempty partial sum equals f.
```

---

## F12.2. Required starting input

The extracted proof currently requires the following input.

## Input G: Graham-valid starting ordering

There exists at least one ordering of `S` whose nonempty partial sums are pairwise distinct.

This input is not harmless: it is essentially the Graham/Erdős 475 existence conclusion.  Therefore the endpoint-avoidance proof, as currently extracted, is conditional unless Input G is proved independently or the minimal-counterexample setup is modified to start from an arbitrary ordering.

---

## F12.3. Conditional endpoint-avoidance theorem

## Theorem F12.1: conditional endpoint avoidance from Graham-valid existence

Assume:

```text
1. p is an odd prime;
2. S subset F_p^* is finite;
3. f != sigma(S);
4. Input G holds for S;
5. final lemmas F1--F11 are valid.
```

Then there exists a Graham-valid ordering of `S` whose nonempty partial sums avoid `f`.

### Proof

Assume endpoint avoidance fails.  By Input G, the set of Graham-valid orderings of `S` is nonempty.  Since endpoint avoidance fails, every Graham-valid ordering has at least one nonempty partial sum equal to `f`.

Choose a Graham-valid ordering

```text
R=(r_1,...,r_t)
```

whose first forbidden-hit index

```text
h=min{i : S_i=f}
```

is minimal among all Graham-valid orderings.

Because `S_t=sigma(S)` and `f != sigma(S)`, the first forbidden hit is not final.  Thus `h<t`, and the atom `r_{h+1}` exists.

Apply the adjacent swap at the first forbidden hit:

```text
... r_h r_{h+1} ... -> ... r_{h+1} r_h ...
```

By F2, the transformed ordering either:

```text
1. is Graham-valid and avoids f;
2. creates a collision blocker equation;
3. is Graham-valid but recurrent.
```

Case 1 contradicts the assumption that endpoint avoidance fails.

In Cases 2 and 3, F2 produces an initial obstruction state in the F3 state machine.  Starting from that obstruction state, apply the termination theorem F9, with weighted exits handled by F10--F11.  The obstruction path cannot continue indefinitely.  It must eventually reach one of:

```text
SUCCESS,
CONTRADICTION.
```

If it reaches `SUCCESS`, a Graham-valid ordering avoiding `f` exists, contradicting endpoint-avoidance failure.

If it reaches `CONTRADICTION`, then the assumed minimal first-hit counterexample violates at least one of:

```text
Graham-validity;
minimality of h;
nonzero atom status;
distinct subset atom status;
f != sigma(S).
```

This also contradicts the setup.

Therefore endpoint avoidance holds under Input G. ∎

---

## F12.4. Unconditional endpoint-avoidance gap

The preceding theorem is conditional because of Input G.

To obtain an unconditional endpoint-avoidance theorem, one must resolve the starting-ordering issue in one of the following ways.

### Route A: independent Graham-valid existence

Prove Erdős 475 or a weak Graham-valid existence theorem independently, then use F12.1 to strengthen it to endpoint avoidance.

Problem:

```text
If the independent theorem is already Erdős 475, then F12 no longer proves Erdős 475; it proves the stronger endpoint-avoidance refinement conditional on Erdős 475.
```

### Route B: arbitrary-ordering obstruction start

Modify F1/F2 so the proof starts from an arbitrary ordering and handles the first obstruction, whether it is:

```text
1. repeated partial sum collision;
2. forbidden hit f;
3. zero interval;
4. endpoint degeneracy.
```

This would remove the need for Input G.

### Route C: simultaneous minimization

Minimize a combined defect measure over all orderings:

```text
(number of repeated partial-sum collisions,
 first forbidden-hit index,
 collision span,
 obstruction complexity).
```

Then show the first local move decreases the combined defect unless it enters the same obstruction state machine.

This may be the most direct route to an unconditional endpoint-avoidance theorem.

---

## F12.5. Endpoint avoidance as a strengthening theorem

Even with Input G, F12.1 is useful as a strengthening theorem:

```text
Graham-valid existence for S
  -> endpoint avoidance for every f != sigma(S).
```

This is stronger than the original Graham-validity statement, but it cannot by itself prove Graham-validity.

---

## F12.6. Interface with F13

F13 proves:

```text
endpoint avoidance -> strong nonzero-sum -> Erdős 475.
```

However, if F12 endpoint avoidance is conditional on Input G, then the full chain becomes circular for proving Erdős 475 unless Input G is independently resolved.

Therefore F13 must state two versions:

```text
1. conditional strengthening version: Graham-valid existence + F12 -> endpoint avoidance -> strong nonzero-sum;
2. unconditional Erdős 475 version: valid only after Input G is removed or independently proved without using Erdős 475.
```

---

## F12.7. Current proof status

The obstruction-routing engine F3--F11 is now extracted as a conditional termination machine.  The remaining global issue is not local algebra; it is the starting-ordering foundation.

Current status:

```text
Endpoint avoidance is extracted conditional on Input G.
Unconditional endpoint avoidance requires a new or modified F1/F2 setup.
```

---

## F12.8. Remaining extraction risks

Before final manuscript status:

```text
R1. Resolve Input G or explicitly state F12 as a conditional strengthening theorem.
R2. Ensure F9 termination theorem is fully hardened.
R3. Ensure F11 weighted termination is fully hardened.
R4. Clarify exactly which contradiction outcomes are terminal in the endpoint-avoidance setup.
R5. Decide whether the public proof aims to prove endpoint avoidance unconditionally or only as a strengthening conditional on Graham-validity.
```

---

## F12.9. Recommended next file

The next extraction should be:

```text
docs/final/F13_erdos475_dependency.md
```

It should state the theorem chain in two forms:

```text
A. clean implication: endpoint avoidance -> strong nonzero-sum -> Erdős 475;
B. current extracted status: F12 is conditional on Input G, so the chain is not yet an unconditional proof of Erdős 475.
```

---

## F12.10. Extraction status

```text
Status: extracted draft.
Risk: RED for unconditional endpoint avoidance because of Input G.
Risk: YELLOW as a conditional strengthening theorem.
```
