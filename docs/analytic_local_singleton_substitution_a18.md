# Analytic local/singleton substitution A18: finite residual case ledger

This note continues from A17.

A17 showed that if a singleton-prefix interleaving fails in an equal-sum branch, the adjacent atom

```text
b = r_{h+1}
```

lies in a short trap list.  Independently, the local right-swap obstruction from A5 gives

```text
S_{h-1}+b=S_j,
```

for some `j != h`.  Equivalently,

```text
b=S_j-S_{h-1}.
```

This note substitutes the local expression for `b` into the A17 singleton trap lists and records which cases collapse immediately and which remain as genuine residual algebraic cases.

The note is a ledger, not a complete proof.  Its purpose is to prevent rechecking the same easy cases and to isolate the remaining finite symbolic cases.

---

## Standing setup

Let

```text
R=(r_1,...,r_t)
```

be a Graham-valid ordering of `A subset F_p^*`, with

```text
S_0=0,
S_i=r_1+...+r_i,
sigma=S_t.
```

Assume endpoint avoidance fails for `(A,f)`, where

```text
f != sigma.
```

Choose `R` so that the unique forbidden hit occurs as early as possible:

```text
S_h=f.
```

Write

```text
a=r_h,
b=r_{h+1},
P=S_{h-1}.
```

Then

```text
P+a=f.
```

The A5 local right-swap obstruction gives

```text
P+b=S_j
```

for some

```text
j != h.
```

Thus

```text
b=S_j-P.
```

Since `A` is a set of nonzero residues,

```text
a != b,
a != 0,
b != 0.
```

---

# 1. FIRST singleton branch substitution

Assume the FIRST equal-sum branch:

```text
R=LUV,
sum(L)=sum(U)=f,
```

where

```text
L=(r_1,...,r_h),
U=(r_{h+1},...,r_alpha),
V=(r_{alpha+1},...,r_t),
S_alpha=2f.
```

Let `U_s` denote prefix sums of `U`, with

```text
U_1=b,
U_|U|=f.
```

Let `L_i=S_i` for `1<=i<=h` and `V_m` denote prefix sums of `V`.

A17 showed that if the FIRST singleton interleaving

```text
L b Y V -> b L Y V
```

fails, then at least one of the following holds:

```text
(F1) b = f-L_i,
(F2) L_i=0,
(F3) b = f+U_s,                  2 <= s <= |U|,
(F4) b = 2f+V_m,
(F5) b = f+U_s-L_i,              2 <= s <= |U|,
(F6) b = 2f+V_m-L_i.
```

This section combines these with

```text
b=S_j-P.
```

---

## Lemma A18.1: FIRST case F1 has two immediate boundary collapses

In case `(F1)`:

```text
b=f-L_i.
```

The subcase `i=h` is impossible, and the subcase `i=h-1` is impossible.

### Proof

If `i=h`, then `L_i=f`, so

```text
b=f-L_h=f-f=0,
```

contradicting `b in F_p^*`.

If `i=h-1`, then `L_i=P`, so

```text
b=f-P=a,
```

contradicting `a != b`.  Equivalently, `P+b=f=S_h`, so the local blocker would have `j=h`, which is excluded by A5.  ∎

### Residual F1 cases

Only

```text
1 <= i <= h-2
```

remain.  In those cases, substituting `b=S_j-P` gives

```text
S_j = P+f-L_i.
```

Using `f=P+a`, this is

```text
S_j = 2P+a-L_i.
```

No immediate contradiction follows without additional interval information.

---

## Lemma A18.2: FIRST case F5 collapses when `i=h`

In case `(F5)`:

```text
b=f+U_s-L_i,        2 <= s <= |U|.
```

The subcase `i=h` is impossible.

### Proof

If `i=h`, then `L_i=f`, so `(F5)` gives

```text
b=U_s.
```

But `U_1=b`.  Since `s>=2`, this gives

```text
U_s=U_1.
```

In the original ordering, the corresponding partial sums are

```text
S_{h+s}=f+U_s,
S_{h+1}=f+U_1.
```

Thus `S_{h+s}=S_{h+1}` with distinct indices, contradicting Graham-validity.  ∎

### Residual F5 cases

Only

```text
1 <= i <= h-1
```

remain for F5.  Substituting `b=S_j-P` gives

```text
S_j = P+f+U_s-L_i.
```

---

## Lemma A18.3: FIRST case F2 is not automatically contradictory

Case `(F2)` says

```text
L_i=0.
```

This is allowed by Graham-validity when `i<h`, because `S_0=0` is not included among the nonempty partial sums in Graham's condition.  The subcase `i=h` says `f=0`, which is also possible in the strong nonzero-sum application.

Therefore F2 must remain as a genuine residual branch.

### Interpretation

F2 is a prefix-zero branch.  It may be useful rather than harmful: if a prefix sums to zero, cutting after that prefix can sometimes shorten the first forbidden-hit index.  This requires a separate cyclic-cut argument and is not disposed of here.

---

## FIRST residual ledger after immediate collapses

After Lemmas A18.1--A18.3, the FIRST singleton failure is reduced to the following residual cases:

```text
(F1r) b=f-L_i,              1 <= i <= h-2,
(F2r) L_i=0,                1 <= i <= h,
(F3r) b=f+U_s,              2 <= s <= |U|,
(F4r) b=2f+V_m,
(F5r) b=f+U_s-L_i,          2 <= s <= |U|, 1 <= i <= h-1,
(F6r) b=2f+V_m-L_i.
```

Together with the local relation, each residual gives an equation for the blocker partial sum:

```text
S_j = P + RHS.
```

The next elimination step should translate each residual equation into an interval-sum relation and test whether it is:

```text
1. an old Graham collision;
2. an old second f-hit;
3. a local zero-sum bypass;
4. a prefix-zero/cyclic-cut branch;
5. a genuine unresolved atom.
```

---

# 2. SECOND singleton branch substitution

Assume the SECOND equal-sum branch:

```text
R=ABC,
sum(B)=sum(C)=sigma-f,
```

where

```text
A=(r_1,...,r_beta),
B=(r_{beta+1},...,r_h),
C=(r_{h+1},...,r_t),
S_beta=2f-sigma.
```

Let

```text
sA=S_beta=2f-sigma.
```

Let `C_s` denote prefix sums of `C`, with

```text
C_1=b,
C_|C|=sigma-f.
```

Away from the boundary case `beta=h`, A17 showed that if the SECOND singleton interleaving

```text
A B b Y -> A b B Y
```

fails, then at least one of the following holds:

```text
(S1) b = sigma-f-B_k,
(S2) b = A_i-sA,
(S3) b = A_i-sA-B_k,
(S4) b = f+C_s-sA,             2 <= s <= |C|,
(S5) b = f+C_s-sA-B_k,         2 <= s <= |C|.
```

The boundary case `beta=h` is excluded here because it is already a pair-trap boundary in A11/A15.

---

## Lemma A18.4: SECOND case S1 collapses at the endpoint of B

In case `(S1)`:

```text
b=sigma-f-B_k.
```

The subcase `k=|B|` is impossible.

### Proof

Since `sum(B)=sigma-f`, if `k=|B|`, then `B_k=sigma-f`, and `(S1)` gives

```text
b=0,
```

contradicting `b in F_p^*`.  ∎

### Residual S1 cases

Only

```text
1 <= k < |B|
```

remain.

---

## Lemma A18.5: SECOND case S2 collapses at the endpoint of A

In case `(S2)`:

```text
b=A_i-sA.
```

The subcase `i=|A|=beta` is impossible.

### Proof

At `i=beta`, one has

```text
A_i=sA.
```

Thus `(S2)` gives

```text
b=0,
```

contradicting `b in F_p^*`.  ∎

### Residual S2 cases

Only

```text
1 <= i < beta
```

remain.

---

## Lemma A18.6: SECOND case S4 has an endpoint form but does not collapse automatically

In case `(S4)`:

```text
b=f+C_s-sA.
```

Using `f-sA=sigma-f`, this is

```text
b=sigma-f+C_s.
```

If `s=|C|`, then `C_s=sigma-f`, so

```text
b=2(sigma-f).
```

This is not automatically contradictory in `F_p`.  Therefore the endpoint subcase of S4 remains residual.

---

## SECOND residual ledger after immediate collapses

Away from `beta=h`, the SECOND singleton failure is reduced to:

```text
(S1r) b=sigma-f-B_k,            1 <= k < |B|,
(S2r) b=A_i-sA,                 1 <= i < beta,
(S3r) b=A_i-sA-B_k,
(S4r) b=f+C_s-sA,               2 <= s <= |C|,
(S5r) b=f+C_s-sA-B_k,           2 <= s <= |C|.
```

Together with the local relation `b=S_j-P`, each gives a blocker equation

```text
S_j = P + RHS.
```

---

# 3. The finite residual problem

The equal-sum singleton-prefix branch is now reduced to a finite symbolic residual problem.

## FIRST residual count

The FIRST singleton branch has six residual families after immediate collapses:

```text
F1r, F2r, F3r, F4r, F5r, F6r.
```

## SECOND residual count

The SECOND singleton branch has five residual families away from the boundary pair-trap case:

```text
S1r, S2r, S3r, S4r, S5r.
```

The boundary case

```text
beta=h
```

is separated as a pair-trap branch.

## Target A19

For each residual family, substitute

```text
P=S_{h-1},
f=P+a,
b=S_j-P,
```

and rewrite the equation as an interval-sum identity.  Then prove that every identity gives one of:

```text
1. old Graham collision;
2. old second f-hit;
3. A5 forward/backward bypass zero block;
4. A8 cyclic zero block;
5. A11 boundary pair-trap;
6. prefix-zero branch that allows a cut reducing the first-hit index.
```

A19 should be written as a table of interval identities, one row per residual family.

---

## Current status

Proved here:

1. F1 boundary subcases `i=h` and `i=h-1` collapse;
2. F5 subcase `i=h` collapses by old Graham collision;
3. F2 prefix-zero branch must remain residual;
4. S1 endpoint `k=|B|` collapses;
5. S2 endpoint `i=beta` collapses;
6. S4 endpoint does not collapse automatically;
7. the equal-sum singleton branch is reduced to explicit residual families.

Not proved here:

1. elimination of all residual families;
2. prefix-zero cut reduction;
3. boundary pair-trap repair;
4. endpoint avoidance theorem.
