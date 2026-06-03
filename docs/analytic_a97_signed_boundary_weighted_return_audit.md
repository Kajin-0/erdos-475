# Analytic Audit: A97 Signed-Boundary Weighted-Return Channel

This note audits the remaining A97/F11 weighted-return channel:

```text
moved P against old R -> signed cut-boundary relation.
```

Claim boundary:

```text
This is a local algebra and routing audit.
It is not a proof of Erdős 475.
It narrows the weighted-return channel but does not by itself close F11.
```

---

## Source files

Primary source:

```text
docs/analytic_weighted_cut_swap_table_hardening_a97.md
```

Weighted closure checkpoints:

```text
docs/analytic_f10_f11_weighted_core_closure_checkpoint.md
docs/analytic_f9_f11_mutual_induction_convention.md
docs/final/F11_weighted_cut_selection_extraction.md
```

---

## Setup

Start with a genuine weighted core:

```text
A + 2B + C = 0,
B=P R,
P,R nonempty.
```

Write sums:

```text
a=sum(A),
p=sum(P),
r=sum(R),
c=sum(C),
b=p+r.
```

The weighted cut-swap is:

```text
A P R C -> A R P C.
```

A97 shows that direct displayed collisions of moved families with `A`, `C`, or each other route to zero-composite/equal/signed non-weighted classes.

The only possible weighted-return channel is the old/new cut-boundary comparison:

```text
x+a+r+P_j = x+a+p+R_k.
```

A97 records this as:

```text
r + P_j - p - R_k = 0.
```

---

## Prefix-tail decomposition

Let:

```text
P = P_j P_j^+,
R = R_k R_k^+,
```

where `P_j` and `R_k` are prefixes and `P_j^+`, `R_k^+` are the corresponding tails.

Then:

```text
p=P_j+P_j^+,
r=R_k+R_k^+.
```

Substitute into the signed boundary equation:

```text
r + P_j - p - R_k = 0.
```

This gives:

```text
(R_k+R_k^+) + P_j - (P_j+P_j^+) - R_k = 0.
```

Cancelling equal terms:

```text
R_k^+ - P_j^+ = 0.
```

Therefore:

```text
R_k^+ = P_j^+.
```

---

## Consequence

Under ordinary prefix-tail decomposition, the signed boundary channel is not itself a new weighted core. It is an equal-tail relation between a suffix of `R` and a suffix of `P`.

This routes to:

```text
EQUAL_INTERVAL,
SEPARATED_EQUAL,
ZERO_COLLAPSE,
PROPER_SUBINTERVAL,
BRIDGE_GAP if the equal tails are separated by a nonempty gap,
F5/F8/F9 machinery.
```

The only way it can contribute to a genuine weighted return is indirectly:

```text
same or related equal-tail relations persist across all proper cuts,
prevent every cut-swap from descending,
and thereby form the weak cut-rigid situation handled by A90--A94.
```

Thus a single A97.8 signed-boundary equation does not by itself preserve a weighted core with the same middle length.

---

## Endpoint cases

### Case 1: `P_j=P`

Then:

```text
P_j^+=empty.
```

The relation gives:

```text
R_k^+=0.
```

If `R_k^+` is nonempty, this is a zero-sum suffix of `R`, hence a zero-composite/collapse branch.

If `R_k^+` is empty, then `R_k=R`, and the equality is tautological at the full boundary. It gives no new obstruction and cannot be used as a nontrivial weighted-return certificate.

### Case 2: `R_k=R`

Then:

```text
R_k^+=empty.
```

The relation gives:

```text
P_j^+=0.
```

If `P_j^+` is nonempty, this is a zero-sum suffix of `P`.

If `P_j^+` is empty, it is the full-boundary tautology.

### Case 3: both tails nonempty

Then:

```text
R_k^+=P_j^+
```

is a proper equal-interval relation supported strictly inside `B`.

The support is contained in:

```text
P_j^+ R_k^+ subset B.
```

It is therefore a non-weighted internal obstruction, not a full weighted return.

### Case 4: one prefix empty

If empty prefixes are explicitly allowed in the boundary comparison, the same decomposition applies:

```text
P_j=empty -> P_j^+=P,
R_k=empty -> R_k^+=R.
```

The equation is still an equal-tail/equal-block relation:

```text
R_k^+=P_j^+.
```

It routes to equal/separated interval machinery unless it is the full equality `R=P`, in which case it is a separated-equal/direct-exchange branch, not a weighted-core relation.

---

## Comparison with moved R against old P

A97.7 gives:

```text
R_k=P_j.
```

This is an equal-prefix relation.

A97.8 gives:

```text
R_k^+=P_j^+.
```

This is an equal-tail relation.

Together, if both occur for compatible `j,k`, they can force stronger internal symmetry of the cut pieces `P` and `R`. But that is precisely a cut-rigid/pattern-rigid scenario, not a single local weighted return.

The persistence of such symmetries over all proper cuts belongs to:

```text
A90--A94 weak-to-pattern-rigid reduction,
A89 strong exact self-return impossibility.
```

---

## Signed-Boundary Audit Lemma

### Statement

For the weighted cut-swap:

```text
A P R C -> A R P C,
```

the A97 signed-boundary relation:

```text
r+P_j-p-R_k=0
```

is equivalent to the equal-tail relation:

```text
R_k^+=P_j^+.
```

Therefore a single signed-boundary relation routes to non-weighted equal-interval/separated-equal/zero-composite machinery, except for tautological full-boundary cases. It does not by itself produce a genuine weighted-core return.

A genuine same-length weighted return can only arise from persistent signed-boundary rigidity across cuts, which is the weak cut-rigid/pattern-rigid branch handled by A90--A94 and A89.

### Proof

The equality follows by substituting:

```text
p=P_j+P_j^+,
r=R_k+R_k^+.
```

into:

```text
r+P_j-p-R_k=0.
```

Endpoint cases are exactly the cases where one or both tails are empty. Nonempty tails give equal-interval machinery; zero tails give zero-collapse or tautology. ∎

---

## Impact on F11 blocker W4

This audit reduces:

```text
W4. A97 signed boundary weighted-return channel signs/endpoints.
```

to:

```text
single signed-boundary equation -> non-weighted equal-tail relation;
persistent signed-boundary across all cuts -> weak cut-rigid branch A90--A94/A89.
```

Thus W4 is no longer a free algebraic weighted-return channel.

Remaining requirement:

```text
The final F11 proof must state that weighted return through A97.8 means persistent cut-rigidity, not an isolated equation.
```

---

## Mutual-induction relevance

For the F9/F11 mutual-induction convention, an isolated A97.8 exit gives:

```text
W(m) -> NW_1
```

where `NW_1` is an equal-tail/equal-interval obstruction supported inside the original weighted middle `B`.

Expected decrease:

```text
support_size decreases
```

or, when the equal tails are separated inside `B`,

```text
enclosing_span <= |B| < enclosing_span(A B C)
```

relative to the full weighted entry support.

This still needs to be included in the final W-to-NW exit decrease table, but the likely decreasing coordinate is now explicit.

---

## Patch recommendation

Patch A97 Lemma A97.8 to replace the ambiguous line:

```text
R^+_k + P_j = P^+_j + R_k depending on tail decomposition
```

with the direct simplification:

```text
R_k^+ = P_j^+.
```

Patch F11 to cite this audit and downgrade W4 from broad weighted-return risk to:

```text
signed-boundary persistence / cut-rigidity risk.
```

---

## Current status

Closed here:

```text
1. algebra of the A97.8 signed boundary equation;
2. endpoint/full-prefix cases for that equation;
3. classification of isolated signed-boundary exits as non-weighted equal-tail relations.
```

Still open:

```text
1. persistent signed-boundary rigidity across all cuts;
2. final W-to-NW exit decrease table;
3. A56 transported-prefix/tail exhaustiveness;
4. final mutual-induction implementation in F9/F11.
```
