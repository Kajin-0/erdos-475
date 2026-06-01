# Analytic Audit: F7 Pair-Difference Recurrence Endpoint Table

This note audits the pair-difference recurrence source A69 and supplies the explicit endpoint table requested by F7.

Claim boundary:

```text
This is a recurrence-routing audit note.
It is not a complete proof of Erdős 475.
It does not prove full F9 termination.
```

---

## Source files

Primary source:

```text
docs/analytic_pair_difference_recurrence_a69.md
```

F7 theorem:

```text
docs/final/F07_recurrence_routing_theorem.md
```

Related correction:

```text
docs/analytic_f7_h1_h2_sign_audit.md
```

The same endpoint convention used to correct H2 also applies here.

---

## Pair-difference recurrence setup

Start with local segment:

```text
X P a b Y
```

with pair-difference relation:

```text
sum(P)=p=a-b.
```

Equivalently:

```text
p+b-a=0.
```

The pair-swap move is:

```text
X P a b Y -> X P b a Y.
```

Let the recurrent forbidden hit in the transformed ordering occur after:

```text
P b a U.
```

Write:

```text
Y=U V.
```

If `V` is nonempty, write:

```text
V=v_1 V^+.
```

There are two endpoint regimes:

```text
Case A: U is nonempty, U=U^- u_*.
Case B: U is empty, so the hit-boundary atom is a.
```

This distinction is necessary because A5 uses the endpoint before the hit-boundary atom.

---

# Case A: U nonempty

Assume:

```text
U=U^-u_*,
V=v_1V^+.
```

The recurrent hit is after:

```text
P b a U^- u_*.
```

Let `H` be that hit endpoint. Then:

```text
S'_H=S'_{H-1}+u_*.
```

A5 gives:

```text
S'_{H-1}+v_1=S'_{j'}.
```

Therefore left-blocker pullbacks end before `u_*` and use `U^-`, not full `U`.

---

## A-left blockers

For a left blocker:

```text
j'<H,
```

A5 gives:

```text
sum'(j',H-1]+v_1=0.
```

The endpoint table is:

```text
inside U^-:
  suffix(U^-)+v_1=0.

at endpoint immediately before u_*:
  v_1=0, contradiction.

after P b:
  a+U^-+v_1=0.

after P:
  b+a+U^-+v_1=0.

inside P:
  tail(P)+b+a+U^-+v_1=0.

before P:
  L+P+b+a+U^-+v_1=0.
```

The first is suffix-zero descent. The second is zero-atom contradiction. The middle pair-neighborhood endpoint cases are zero-composite branches. The last two are zero-composite or external bridge branches.

Using:

```text
p+b-a=0,
```

the left bridge branch can be rewritten as:

```text
L+P+b+a+U^-+v_1=0
```

with either atom eliminated if useful:

```text
P+b=a,
```

so:

```text
L+a+a+U^-+v_1=0,
```

or:

```text
P-a=-b.
```

These are signed-correction forms, not new recurrence species.

---

## A-right blockers

For a right blocker:

```text
j'>H,
```

subtract the hit endpoint:

```text
S'_{j'}-S'_H=v_1-u_*.
```

If `V_r` is the prefix of `V` ending at the blocker, then:

```text
V_r=v_1-u_*.
```

Equivalently:

```text
u_* - v_1 + V_r=0.
```

Endpoint table:

```text
immediate first endpoint V_r=v_1:
  u_*=0, contradiction.

proper prefix V_r=v_1W, W proper in V^+:
  u_*+W=0,
  proper zero-composite descent.

all of V:
  V+u_*-v_1=0,
  equivalently V^+ + u_*=0.

beyond V with bridge R:
  R+V+u_*-v_1=0,
  equivalently R+V^+ + u_*=0.
```

Thus the all-of-`V` endpoint case is not an independent pair-difference species under the corrected endpoint convention. It is a proper zero-composite or zero-atom contradiction.

---

# Case B: U empty

If `U` is empty, the recurrent hit occurs after:

```text
P b a.
```

The hit-boundary atom is:

```text
a.
```

Thus:

```text
S'_H=S'_{H-1}+a,
```

and A5 gives:

```text
S'_{H-1}+v_1=S'_{j'}.
```

where `S'_{H-1}` is the endpoint after `P b`.

---

## B-left blockers

For a left blocker:

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

The after-`P` case is a two-atom zero branch. The inside-`P` case descends by proper suffix support. The before-`P` case is a left bridge zero/signed composite.

Using `P+b=a`, the bridge branch can also be written:

```text
L+a+v_1=0.
```

---

## B-right blockers

For a right blocker:

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

Again, the all-of-`V` endpoint case is a zero-composite or zero-atom contradiction, not a new pair-difference recurrence species.

---

# Case C: no post-tail V

If no atom exists after the recurrent hit, then A5 cannot be applied at that hit.

In endpoint avoidance, this case should be impossible in the recurrence branch because the final endpoint is not the forbidden value:

```text
sigma(S) != f.
```

If the model normalizes the branch as an endpoint immediately after the swapped pair with further context elsewhere, then the landing is:

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

## Pair-Difference Endpoint Table Lemma

### Statement

Every endpoint or near-endpoint A5 blocker case in pair-difference recurrence routes to one of:

```text
1. zero-atom contradiction;
2. suffix-zero or proper zero-composite descent;
3. pair-neighborhood zero-composite branch;
4. signed/equal external bridge branch;
5. singleton/scalar-prefix recurrence when the recurrent hit is an endpoint landing;
6. F6/F8/F9 global routing.
```

No endpoint case produces a new pair-difference recurrence species outside the existing F3/F9 class universe.

### Proof

The case tables above exhaust left and right A5 blocker positions for both `U` nonempty and `U` empty. Each displayed equality is either a zero atom, a proper subinterval zero-composite, a bridge signed/zero composite, or a scalar/singleton landing. ∎

---

## Required source correction

The source note:

```text
docs/analytic_pair_difference_recurrence_a69.md
```

currently writes several left-blocker formulas using full `U`.

For final use, those should be corrected to use:

```text
U=U^-u_*
```

when the recurrent hit occurs after `P b a U` with `U` nonempty.

Specifically, replace schematic formulas of the form:

```text
... + U + v_1 = 0
```

by:

```text
... + U^- + v_1 = 0
```

and treat the `U=empty` case separately with hit-boundary atom `a`.

---

## F7 impact

This audit addresses the F7 risk:

```text
Pair-difference recurrence endpoint cases require explicit table.
```

The pair-difference recurrence branch still inherits global routing obligations through:

```text
F4 zero-composite descent,
F6 external collision,
F8 bridge/gap descent,
F9 non-weighted termination,
F10/F11 weighted exits if a signed correction becomes weighted-core.
```

But there is no remaining endpoint-table ambiguity.

---

## Significant status

Pair-difference endpoint cases are now explicitly classified.

A69 should be patched next to incorporate the corrected `U^- / u_*` convention, analogous to the H2 correction in A67.
