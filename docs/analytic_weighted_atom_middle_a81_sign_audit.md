# Analytic Audit: Weighted Atom-Middle A81 Sign Patterns

This note audits the atom-middle weighted-core base case from:

```text
docs/analytic_atom_middle_weighted_core_a80.md
docs/analytic_endpoint_rigid_atom_middle_a81.md
docs/final/F11_weighted_cut_selection_extraction.md
```

Claim boundary:

```text
This is a finite algebra audit for the |B|=1 weighted base case.
It is not a proof of Erdős 475.
It closes the A81 sign-pattern ambiguity modulo non-weighted termination and the F9/F11 mutual-induction interface.
```

---

## Purpose

F11 listed the atom-middle base case as a risk:

```text
A81 sign-pattern algebra must be checked line by line.
Endpoint-empty cases A=empty or C=empty must be explicitly included in the final manuscript.
```

A81 already sketches the four sign patterns, but one displayed proof line contains an ambiguous placeholder:

```text
alpha+2q? - gamma = 0
```

This audit recomputes all four cases cleanly.

---

## Standing atom-middle setup

The atom-middle weighted core is:

```text
A + 2q + C = 0,
```

with:

```text
a=sum(A),
c=sum(C),
q in F_p^*.
```

Thus:

```text
a + 2q + c = 0.
```

Assume the genuine weighted-core easy reductions fail:

```text
q != 0,
a+q != 0,
q+c != 0,
a != c,
no transported-prefix/tail rewrite.
```

When both outer blocks are nonempty, write:

```text
A=A^- alpha,
C=gamma C^+,
```

where:

```text
alpha = last atom of A,
gamma = first atom of C.
```

Endpoint-rigid atom-middle traps reduce to left/right boundary pair equations with one of four sign patterns.

---

## Four endpoint sign patterns

The four sign patterns are:

```text
(+,+):  a = q-alpha,     c = gamma-q;
(+,-):  a = q-alpha,     c = q-gamma;
(-,+):  a = alpha-q,     c = gamma-q;
(-,-):  a = alpha-q,     c = q-gamma.
```

Each is substituted into:

```text
a+2q+c=0.
```

---

## Table: exact algebra

| Pattern | Substitution into `a+2q+c=0` | Simplified boundary relation | Class |
|---|---|---|---|
| `(+,+)` | `(q-alpha)+2q+(gamma-q)=0` | `alpha-gamma=2q` | boundary signed midpoint / pair-difference |
| `(+,-)` | `(q-alpha)+2q+(q-gamma)=0` | `alpha+gamma=4q` | bounded three-atom signed relation |
| `(-,+)` | `(alpha-q)+2q+(gamma-q)=0` | `alpha+gamma=0` | two-atom zero-composite |
| `(-,-)` | `(alpha-q)+2q+(q-gamma)=0` | `alpha-gamma=-2q` | boundary signed midpoint / pair-difference |

No row leaves a genuine full atom-middle weighted core on `A q C`.

Every row is supported only on the boundary triple:

```text
alpha, q, gamma.
```

or, in the `(-,+)` row, on the two boundary atoms:

```text
alpha, gamma.
```

---

## Row verification

### Pattern `(+,+)`

Assume:

```text
a=q-alpha,
c=gamma-q.
```

Then:

```text
(q-alpha)+2q+(gamma-q)=0
```

so:

```text
2q-alpha+gamma=0,
```

hence:

```text
alpha-gamma=2q.
```

This is the canonical A81 relation.

---

### Pattern `(+,-)`

Assume:

```text
a=q-alpha,
c=q-gamma.
```

Then:

```text
(q-alpha)+2q+(q-gamma)=0,
```

so:

```text
4q-alpha-gamma=0,
```

hence:

```text
alpha+gamma=4q.
```

This is a bounded three-atom signed relation. It is not a weighted core with a nontrivial doubled interval. It routes to signed interval / pair-difference / midpoint machinery on the boundary triple.

Characteristic note:

```text
p=3: 4q=q, so alpha+gamma=q.
p=5: 4q=-q, so alpha+gamma=-q.
```

No division by 3 or 5 is used.

---

### Pattern `(-,+)`

Assume:

```text
a=alpha-q,
c=gamma-q.
```

Then:

```text
(alpha-q)+2q+(gamma-q)=0,
```

so:

```text
alpha+gamma=0.
```

This is a two-atom zero-composite:

```text
alpha + gamma = 0.
```

It is terminal or routes to zero-composite machinery. It is not a genuine weighted atom-middle core.

---

### Pattern `(-,-)`

Assume:

```text
a=alpha-q,
c=q-gamma.
```

Then:

```text
(alpha-q)+2q+(q-gamma)=0,
```

so:

```text
alpha+2q-gamma=0.
```

Therefore:

```text
gamma-alpha=2q,
```

or equivalently:

```text
alpha-gamma=-2q.
```

This is the sign reverse of the canonical `(+,+)` boundary signed midpoint relation.

This row corrects the ambiguous A81 placeholder line.

---

## Endpoint-empty outer blocks

A80.6 treats cases where one outer block is empty.

### Case `A=empty`

The weighted relation is:

```text
2q+c=0.
```

If `C` is nonempty, write:

```text
C=gamma C^+.
```

Adjacent motion of `q` against `gamma` gives displayed equations of the form:

```text
gamma-q+P=0,
q-gamma+P=0,
P=0,
```

where `P` is a local prefix/tail of `C`.

These route to:

```text
pair-difference,
signed interval,
zero-composite,
singleton recurrence.
```

If `C` has length one, then:

```text
2q+gamma=0
```

is a bounded two-atom midpoint relation, not a full weighted middle interval.

### Case `C=empty`

Symmetrically, the weighted relation is:

```text
a+2q=0.
```

Adjacent motion of `q` against the last atom `alpha` of `A` gives:

```text
alpha-q+P=0,
q-alpha+P=0,
P=0,
```

routing to the same non-weighted classes.

Endpoint-empty cases therefore do not create an independent atom-middle weighted obstruction.

---

## Characteristic audit

The atom-middle sign audit uses only addition/subtraction and, in two optional collapse observations, invertibility of `2`.

Since Erdős 475 is over odd prime fields in the relevant branch:

```text
2 != 0.
```

The following collapses are valid:

```text
alpha=gamma and alpha-gamma=2q -> q=0, contradiction;
alpha=-gamma and alpha-gamma=2q -> q=alpha, duplicate if alpha and q are distinct atoms.
```

No division by 3 is used.

Small-characteristic notes:

```text
p=3 changes numeric coefficients such as 4q=q, but does not create a new weighted-core row.
p=5 changes 4q=-q, but again creates only a bounded boundary relation.
```

---

## Atom-Middle Sign Audit Lemma

### Statement

Every endpoint-rigid atom-middle sign pattern for:

```text
A+2q+C=0
```

compresses to a bounded boundary relation supported on:

```text
alpha,q,gamma
```

or to a two-atom zero relation:

```text
alpha+gamma=0.
```

Consequently, the atom-middle base case `|B|=1` cannot remain as a genuine weighted-core obstruction after endpoint-rigid signs are expanded.

It exits to:

```text
zero-composite,
pair-difference,
signed interval,
midpoint,
singleton/prefix recurrence,
non-weighted F9 machinery,
terminal contradiction.
```

### Proof

The four-row table exhausts left/right sign conventions for the endpoint traps. Direct substitution into `a+2q+c=0` gives only boundary atom relations. Endpoint-empty cases are handled by adjacent motion of `q` against the nonempty outer block and produce the same non-weighted classes. ∎

---

## Consequence for F11

This audit reduces F11 weighted blocker W2:

```text
A81 atom-middle sign-pattern algebra.
```

New status:

```text
W2 is finite-algebra closed modulo non-weighted F9 termination and the F9/F11 mutual-induction interface.
```

Remaining weighted blockers:

```text
W1. F9/F11 mutual dependency must be patched into F9/F11.
W3. A56 transported-prefix/tail exhaustiveness.
W4. A97 signed boundary weighted-return channel.
W6. W-to-NW exit decrease table relative to weighted entry.
```

---

## Patch recommendation

Patch:

```text
docs/analytic_endpoint_rigid_atom_middle_a81.md
```

at Lemma A81.10 to replace the ambiguous proof line:

```text
alpha+2q? - gamma = 0
```

with:

```text
alpha+2q-gamma=0,
```

hence:

```text
alpha-gamma=-2q.
```

Patch F11 to cite this audit and downgrade the atom-middle sign algebra risk.
