# Analytic endpoint-rigid atom-middle self-return A81

This note continues from A80.

A80 reduced the atom-middle weighted core

```text
A + 2q + C = 0
```

where `q` is a single atom, to one remaining rigid case:

```text
endpoint-rigid atom-middle self-return.
```

This version incorporates the finite sign-pattern audit from:

```text
docs/analytic_weighted_atom_middle_a81_sign_audit.md
```

Claim boundary:

```text
This note eliminates the endpoint-rigid atom-middle sign ambiguity modulo non-weighted termination and the F9/F11 mutual-induction interface.
It is not a complete proof of Erdős 475.
```

---

## 1. Standing setup

Let the displayed segment be:

```text
X A q C Y
```

where `q` is a single atom. Write:

```text
a=sum(A),
c=sum(C).
```

The atom-middle weighted core is:

```text
a+2q+c=0.
```

Assume the A56 easy reductions are absent:

```text
q != 0,
a+q != 0,
q+c != 0,
a != c,
no transported-prefix/tail rewrite.
```

Assume first that both `A` and `C` are nonempty. Endpoint-empty cases are recorded separately below.

Write:

```text
A=A^- alpha,
C=gamma C^+,
```

where:

```text
alpha = last atom of A,
gamma = first atom of C.
```

---

## 2. Endpoint-rigid pair traps

A80 showed that a rigid atom-middle self-return can survive only if the adjacent swaps

```text
A^- alpha q C -> A^- q alpha C
```

and

```text
A q gamma C^+ -> A gamma q C^+
```

are both forced into endpoint pair-difference traps.

The canonical orientation is:

```text
q-alpha=a,
gamma-q=c.
```

Other endpoint conventions reverse one or both signs.

---

## 3. Canonical endpoint trap

Assume:

```text
a=q-alpha,
c=gamma-q.
```

Substitute into the weighted core:

```text
(q-alpha)+2q+(gamma-q)=0.
```

Then:

```text
2q-alpha+gamma=0,
```

so:

```text
alpha-gamma=2q.
```

Thus the canonical endpoint-rigid atom trap compresses to a boundary signed midpoint / pair-difference relation supported on:

```text
alpha,q,gamma.
```

---

## 4. Immediate collapses in the canonical row

If:

```text
alpha=gamma,
```

then:

```text
2q=0,
```

so `q=0` in odd characteristic, contradiction.

If:

```text
alpha=-gamma,
```

then:

```text
alpha-gamma=2alpha=2q,
```

so:

```text
q=alpha,
```

which is impossible if `alpha` and `q` are distinct atoms of the set.

---

## 5. Four sign-pattern table

The four endpoint sign patterns are:

```text
(+,+):  a = q-alpha,     c = gamma-q;
(+,-):  a = q-alpha,     c = q-gamma;
(-,+):  a = alpha-q,     c = gamma-q;
(-,-):  a = alpha-q,     c = q-gamma.
```

Substitution into:

```text
a+2q+c=0
```

gives:

| Pattern | Substitution | Simplified relation | Class |
|---|---|---|---|
| `(+,+)` | `(q-alpha)+2q+(gamma-q)=0` | `alpha-gamma=2q` | boundary signed midpoint / pair-difference |
| `(+,-)` | `(q-alpha)+2q+(q-gamma)=0` | `alpha+gamma=4q` | bounded three-atom signed relation |
| `(-,+)` | `(alpha-q)+2q+(gamma-q)=0` | `alpha+gamma=0` | two-atom zero-composite |
| `(-,-)` | `(alpha-q)+2q+(q-gamma)=0` | `alpha-gamma=-2q` | boundary signed midpoint / pair-difference |

Every row is supported only on the boundary triple:

```text
alpha,q,gamma
```

or, in the `(-,+)` row, on the two boundary atoms:

```text
alpha,gamma.
```

No row leaves a full atom-middle weighted core on `A q C`.

---

## 6. Row verification

### `(+,+)`

```text
(q-alpha)+2q+(gamma-q)=0
```

gives:

```text
2q-alpha+gamma=0,
```

hence:

```text
alpha-gamma=2q.
```

### `(+,-)`

```text
(q-alpha)+2q+(q-gamma)=0
```

gives:

```text
4q-alpha-gamma=0,
```

hence:

```text
alpha+gamma=4q.
```

This is a bounded three-atom signed relation. In characteristic 3 it becomes `alpha+gamma=q`; in characteristic 5 it becomes `alpha+gamma=-q`. No new weighted row is created.

### `(-,+)`

```text
(alpha-q)+2q+(gamma-q)=0
```

gives:

```text
alpha+gamma=0.
```

This is a two-atom zero-composite.

### `(-,-)`

```text
(alpha-q)+2q+(q-gamma)=0
```

gives:

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

This corrects the earlier ambiguous placeholder line in this note.

---

## 7. A56-adjacent quantities in the canonical row

Under the canonical traps:

```text
a=q-alpha,
c=gamma-q,
alpha-gamma=2q.
```

Then:

```text
a+q=(q-alpha)+q=2q-alpha=-gamma,
```

and:

```text
q+c=q+(gamma-q)=gamma.
```

Thus the failure of the easy reductions `a+q=0` and `q+c=0` is exactly the nonzero-atom condition:

```text
gamma != 0.
```

This explains why the atom trap is the minimal boundary case after A56 reductions fail.

---

## 8. Endpoint-empty outer blocks

If `A` is empty, the weighted relation becomes:

```text
2q+c=0.
```

If `C` is nonempty, adjacent motion of `q` against the first atom `gamma` of `C` produces equations of the form:

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

If `C` has length one, `2q+gamma=0` is a bounded two-atom midpoint relation, not a full weighted middle interval.

The case `C` empty is symmetric. The relation is:

```text
a+2q=0,
```

and adjacent motion of `q` against the last atom `alpha` of `A` gives the same non-weighted output classes.

Endpoint-empty cases therefore do not create an independent atom-middle weighted obstruction.

---

## 9. Adjacent boundary triple permutations

After endpoint rigidity, the remaining active algebra is supported on the boundary triple:

```text
alpha,q,gamma.
```

Any local permutation of this triple changes only singleton or pair endpoints. A displayed collision or recurrence from such a move has one of the forms:

```text
alpha-gamma=0,
alpha-q+P=0,
gamma-q+P=0,
alpha+gamma+P=0,
```

where `P` is a local prefix/tail or empty endpoint piece.

These are non-weighted classes:

```text
zero collapse,
pair-difference,
signed interval,
zero-composite,
singleton recurrence,
midpoint.
```

No doubled interval block remains.

---

## 10. Endpoint-rigid atom trap theorem

### Theorem A81.1: endpoint-rigid atom-middle trap routes to non-weighted machinery

Every endpoint-rigid atom-middle weighted core:

```text
A+2q+C=0
```

routes to one of:

```text
1. A56 easy reduction;
2. zero collapse;
3. two-atom zero-composite;
4. pair-difference boundary;
5. signed/equal interval;
6. midpoint or singleton recurrence;
7. non-weighted F9 machinery.
```

In particular, the `|B|=1` weighted base case cannot remain as an independent genuine weighted-core obstruction after the endpoint-rigid sign cases are expanded.

### Proof

A80 reduces atom-middle to endpoint-rigid atom traps. The four sign-pattern table above exhausts left/right endpoint conventions. Each row compresses the weighted relation to a boundary relation on `alpha,q,gamma` or to `alpha+gamma=0`. Endpoint-empty cases route to the same non-weighted classes. ∎

---

## 11. Consequence for weighted cut-selection

A79 split the weighted gap into:

```text
W-base: atom-middle weighted core;
W-rigid: cut-rigid weighted self-return for |B|>=2.
```

This note eliminates `W-base` modulo non-weighted F9 termination and the F9/F11 mutual-induction convention.

The remaining weighted gap is:

```text
cut-rigid weighted self-return for |B|>=2.
```

---

## Current status after A81 patch

Proved/recorded here:

```text
1. all four endpoint-rigid sign patterns are computed explicitly;
2. the ambiguous (-,-) sign line is corrected;
3. endpoint-empty outer blocks route to non-weighted classes;
4. atom-middle |B|=1 is not an independent weighted obstruction.
```

Still open outside this note:

```text
1. A56 transported-prefix/tail exhaustiveness;
2. A97 signed boundary weighted-return channel;
3. F9/F11 mutual-induction interface in final F9/F11 drafts;
4. W-to-NW exit decrease table relative to weighted entry.
```
