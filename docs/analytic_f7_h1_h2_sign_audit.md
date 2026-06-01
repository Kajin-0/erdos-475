# Analytic Audit: F7 H1/H2 Sign and Endpoint Conventions

This note audits the H1/H2 atom-insertion recurrence signs used by F7.

Claim boundary:

```text
This is a sign/endpoint audit note for F7 recurrence routing.
It is not a complete proof of Erdős 475.
```

---

## Source files

Primary source notes:

```text
docs/analytic_long_blocker_uncrossing_h1_a65.md
docs/analytic_long_blocker_crossing_h1_a66.md
docs/analytic_long_blocker_uncrossing_h2_a67.md
docs/final/F07_recurrence_routing_theorem.md
```

This audit has two outcomes:

```text
1. H1 signs are internally consistent.
2. H2 needs a correction: left-blocker pullbacks must use U^- rather than full U, because A5 applies at the endpoint before the last atom of U.
```

---

# Part I: H1 sign audit

## H1 setup

Start with a zero block:

```text
P Q,
```

with:

```text
sum(P)+sum(Q)=0.
```

Let:

```text
pP = sum(P),
Q = q1 Q^+,
q = inserted atom.
```

Then:

```text
sum(Q)=-pP.
```

The H1 insertion is:

```text
X P Q q Y -> X P q Q Y.
```

The H1 recurrent hit occurs after:

```text
P q.
```

The next atom is:

```text
q1.
```

A5 gives:

```text
S'_{H-1}+q1=S'_{j'}.
```

Since the hit atom is `q`,

```text
S'_H=S'_{H-1}+q.
```

---

## H1 left blocker

If:

```text
j'<H,
```

then:

```text
sum'(j',H-1]+q1=0.
```

Cases:

```text
inside P:
  tail(P)+q1=0.

before P:
  L+P+q1=0.
```

These match A65.

---

## H1 right blocker

If:

```text
j'>H,
```

then:

```text
S'_{j'}-S'_H=q1-q.
```

Cases:

```text
inside Q prefix Q_r:
  Q_r=q1-q,
  equivalently q-q1+Q_r=0.

all of Q:
  Q=q1-q.
```

Since:

```text
sum(Q)=-pP,
```

the all-Q endpoint gives:

```text
-pP=q1-q,
```

or:

```text
pP+q1-q=0.
```

Beyond Q with right bridge `R`:

```text
Q+R=q1-q,
```

so:

```text
R-pP+q-q1=0.
```

These match A65.

---

## H1 crossing cases

A66 lists:

```text
C1: L+P+q1=0.
C2: R-P+q-q1=0.
C3: P+q1-q=0.
```

Using:

```text
P+Q=0,
Q=q1+Q^+,
```

C1 implies:

```text
L=Q^+.
```

Proof:

```text
P+q1+Q^+=0,
L+P+q1=0,
subtract -> L-Q^+=0.
```

C2 implies:

```text
R+Q^+ + q=0.
```

Proof:

```text
R-P+q-q1=0,
P=-(q1+Q^+),
so R+q1+Q^+ + q - q1=0.
```

C3 is:

```text
P+q1-q=0,
```

or:

```text
q-q1=P.
```

This is the pair-difference boundary branch.

### H1 audit conclusion

The H1 sign table in A65--A66 is consistent.

H1 routes to:

```text
non-crossing zero/pair descent,
C1 equal interval L=Q^+,
C2 zero composite R+Q^+ + q=0,
C3 pair-difference boundary P+q1-q=0.
```

No H1 sign correction is required.

---

# Part II: H2 sign audit and correction

## H2 setup

Start with:

```text
P Q,
sum(P)+sum(Q)=0.
```

Insert atom `q`:

```text
X P Q q Y -> X P q Q Y.
```

Decompose:

```text
Q = U V,
U = U^- u_*,
V = v1 V^+,
```

where:

```text
u_* = last atom of U,
v1  = first atom of V.
```

The non-endpoint H2 recurrent hit occurs after:

```text
P q U = P q U^- u_*.
```

The next atom is:

```text
v1.
```

Let:

```text
H = endpoint after P q U.
```

Then:

```text
S'_H = S'_{H-1}+u_*.
```

A5 gives:

```text
S'_{H-1}+v1=S'_{j'}.
```

Therefore the interval ending at `H-1` ends before the last atom `u_*` of `U`.

This is the source of the correction.

---

## Corrected H2 left blocker formulas

If:

```text
j'<H,
```

then:

```text
sum'(j',H-1]+v1=0.
```

Since `H-1` is before `u_*`, the pullback uses `U^-`, not full `U`.

Correct cases:

```text
inside U^-:
  suffix(U^-)+v1=0.

at the endpoint immediately before u_*:
  v1=0,
  contradiction.

inside P:
  tail(P)+q+U^-+v1=0.

before P:
  L+P+q+U^-+v1=0.
```

### Correction to A67

A67 currently phrases some H2 left-blocker pullbacks using full `U`:

```text
L+P+q+U+v1=0
```

and related formulas.

The corrected formula is:

```text
L+P+q+U^-+v1=0.
```

The missing atom is `u_*`; it belongs to the hit endpoint, not to the A5 pre-hit endpoint.

---

## Corrected H2 right blocker formulas

If:

```text
j'>H,
```

then:

```text
S'_{j'}-S'_H=v1-u_*.
```

For a prefix `V_r` of `V` ending at the blocker:

```text
V_r=v1-u_*.
```

Equivalently:

```text
u_* - v1 + V_r=0.
```

Cases:

```text
immediate first endpoint V_r=v1:
  u_*=0,
  contradiction.

proper prefix V_r=v1 W with W proper in V^+:
  u_* + W=0,
  proper zero-composite descent.

all of V:
  V+u_*-v1=0,
  equivalently V^+ + u_*=0.

beyond V with right bridge R:
  R+V+u_*-v1=0,
  equivalently R+V^+ + u_*=0.
```

These formulas refine A67's right-blocker signs and show that the all-of-V endpoint case is often a smaller two-piece zero composite rather than only a pair-difference boundary.

---

## Corrected H2 crossing cases

The corrected non-endpoint crossing cases are:

```text
D1. left bridge before P:
    L+P+q+U^-+v1=0.

D2. right bridge after V:
    R+V+u_*-v1=0,
    equivalently R+V^+ + u_*=0.

D3. right blocker uses all V:
    V+u_*-v1=0,
    equivalently V^+ + u_*=0.
```

Use the original zero relation:

```text
P+U^-+u_*+v1+V^+=0.
```

For D1, subtract the zero relation from the D1 equation:

```text
(L+P+q+U^-+v1) - (P+U^-+u_*+v1+V^+) = 0.
```

This gives:

```text
L+q-u_*-V^+=0.
```

or equivalently:

```text
V^+ = L+q-u_*.
```

Thus D1 is a signed/equal relation involving the left bridge, the inserted atom, the hit atom, and the tail after `v1`.

For D2:

```text
R+V+u_*-v1=0
```

and `V=v1+V^+`, so:

```text
R+V^+ + u_*=0.
```

For D3:

```text
V+u_*-v1=0
```

so:

```text
V^+ + u_*=0.
```

This is a proper zero composite unless `V^+` is empty, in which case it forces:

```text
u_*=0,
```

contradiction.

---

## Endpoint H2 case V empty

If:

```text
V=empty,
```

then the H2 hit occurs after:

```text
P q Q.
```

Since:

```text
P+Q=0,
```

the hit value is:

```text
x+q=f.
```

So endpoint H2 is exactly an atom-singleton recurrence.

Route:

```text
docs/analytic_f7_singleton_endpoint_audit.md
```

No additional H2 endpoint species is created.

---

## H2 corrected routing theorem

### Statement

With the corrected endpoint convention `U=U^-u_*`, every H2 non-endpoint long-blocker pullback routes to one of:

```text
1. suffix-zero or zero-composite descent inside U^-, P, or V^+;
2. zero-atom contradiction for immediate endpoint blockers;
3. signed/equal relation D1: L+q-u_*-V^+=0;
4. zero composite D2: R+V^+ + u_*=0;
5. zero composite D3: V^+ + u_*=0;
6. endpoint H2 atom-singleton recurrence if V is empty.
```

Therefore H2 still introduces no new local algebraic species, but the formulas in A67 should be corrected before final manuscript use.

### Proof

The proof is the A5 endpoint calculation above. The key identity is:

```text
S'_H=S'_{H-1}+u_*.
```

A5 uses:

```text
S'_{H-1}+v1,
```

so left-blocker intervals stop before `u_*`. Right-blocker intervals are measured from the hit endpoint and therefore compare `v1` against `u_*`. The displayed formulas follow by subtracting endpoints and using:

```text
P+U^-+u_*+v1+V^+=0.
```

∎

---

## Impact on F7 and F9

### Positive impact

The corrected H2 formulas improve the routing:

```text
D3 all-of-V endpoint -> V^+ + u_*=0,
```

which is a proper zero-composite or zero-atom contradiction, not merely an unresolved pair-difference boundary.

D2 also simplifies to:

```text
R+V^+ + u_*=0.
```

### Required patch

Before final manuscript status, update:

```text
docs/analytic_long_blocker_uncrossing_h2_a67.md
docs/final/F07_recurrence_routing_theorem.md
```

to use `U^-`/`u_*` notation in H2.

### F9 compatibility

All corrected H2 outputs still land in the existing F9 class universe:

```text
ZERO_COLLAPSE,
TWO_PIECE_ZERO,
HIGHER_ZERO_COMPOSITE,
SIGNED_INTERVAL,
EQUAL_INTERVAL,
PAIR_DIFFERENCE,
SINGLETON_RECURRENCE,
EXTERNAL_COLLISION,
BRIDGE_GAP.
```

No new F9 class is needed.

---

## Significant status

H1 sign audit: passed.

H2 sign audit: found and corrected an endpoint convention error.

The correction strengthens the H2 routing, but the source notes and F7 final theorem should be patched before any final-proof claim.
