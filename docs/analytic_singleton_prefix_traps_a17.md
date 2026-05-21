# Analytic singleton-prefix traps A17: first-atom interleaving tests

This note continues from A14--A16.

A14 reduced the equal-sum branches to proper-prefix interleavings.  A16 pruned many impossible equations.  The smallest possible proper-prefix move is to move a single first atom of the movable block.

This note records the exact singleton-prefix obstruction systems.  These systems are useful because the same atom is usually the adjacent atom `b=r_{h+1}` that appears in the local right-swap obstruction from A5.

The note is still conservative: it does not claim that the singleton-prefix move always succeeds.  It proves that if the singleton-prefix move fails, the first atom must satisfy a short explicit list of equations.

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

Choose `R` so that its unique forbidden hit occurs as early as possible:

```text
S_h=f.
```

Write

```text
a=r_h,
b=r_{h+1},
P=S_{h-1}.
```

Thus

```text
P+a=f.
```

By A5, the right-adjacent swap of `a,b` is blocked, so there exists `j != h` with

```text
P+b=S_j.
```

---

# 1. FIRST branch singleton-prefix test

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

Choose `alpha` minimal among indices `>h` with `S_alpha=2f`.

Let

```text
U=(b,Y),
```

so the singleton proper prefix is

```text
X=(b),
x=b.
```

The singleton-prefix interleaving is

```text
L b Y V  ->  b L Y V.
```

---

## Lemma A17.1: FIRST singleton partial sums

The nonempty partial sums of

```text
b L Y V
```

are

```text
b,
b+L_i                    for 1 <= i <= h,
b+f+Y_k                  for 1 <= k <= |Y|,
2f+V_m                   for 1 <= m <= |V|.
```

### Proof

This is Lemma A14.1 with `X=(b)` and `x=b`.  ∎

---

## Lemma A17.2: FIRST singleton forbidden-hit obstructions

Under the minimal choice of `alpha`, the singleton interleaving can hit `f` only through

```text
b+L_i=f
```

for some `1 <= i <= h`.

Equivalently,

```text
b=f-L_i.
```

All other forbidden-hit mechanisms from A14/A16 are impossible.

### Proof

From Lemma A17.1, a forbidden hit could occur through:

```text
b=f,
b+L_i=f,
b+f+Y_k=f,
2f+V_m=f.
```

The equation `b=f` is impossible under the minimal FIRST choice.  Indeed, `b` is the first proper prefix sum of `U`; if `b=f`, then

```text
S_{h+1}=S_h+b=f+f=2f,
```

which would force the minimal `2f` index `alpha` to be `h+1`.  But then `U` has length one and there is no nonempty proper prefix for the present singleton-prefix move.  In the setting of this move, `Y` is nonempty, hence `alpha>h+1`, contradiction.

The equation `b+f+Y_k=f` is equivalent to `Y_k=-b`, which is impossible by Lemma A16.1.

The equation `2f+V_m=f` is equivalent to `V_m=-f`, impossible by Lemma A16.3.

Thus only `b+L_i=f` remains.  ∎

---

## Lemma A17.3: FIRST singleton Graham-collision obstructions

The singleton interleaving `bLYV` can fail Graham-validity only through one of the following equations:

```text
b = b+L_i,
b = f+U_s,                 2 <= s <= |U|,
b = 2f+V_m,
b+L_i = f+U_s,             2 <= s <= |U|,
b+L_i = 2f+V_m.
```

The equation

```text
b+f+Y_k = 2f+V_m
```

has already been eliminated by Lemma A16.2, and internal collisions within each family are old collisions or impossible.

The first displayed equation `b=b+L_i` is equivalent to

```text
L_i=0.
```

If `i<h`, it would give an old prefix zero before the forbidden hit; this is allowed by Graham-validity because `S_0=0` is not in the list.  If `i=h`, it says `f=0`, which is possible only in the zero-forbidden strong nonzero-sum application.  Therefore this equation must be retained, not discarded.

### Proof

This is the FIRST pruned system from A16 with `q=1` and `U_q=b`.  The family `f+U_s=2f+V_m` was eliminated in A16.  ∎

---

## Lemma A17.4: FIRST singleton failure gives a short trap list for `b`

If the singleton-prefix interleaving

```text
L b Y V -> b L Y V
```

fails to produce a Graham-valid ordering avoiding `f`, then `b` satisfies at least one equation in the following list:

```text
b = f-L_i,
L_i=0,
b = f+U_s,
b = 2f+V_m,
b = f+U_s-L_i,
b = 2f+V_m-L_i,
```

with the indicated index ranges

```text
1 <= i <= h,
2 <= s <= |U|,
1 <= m <= |V|.
```

### Proof

Move all terms not involving `b` to the right-hand side in Lemmas A17.2 and A17.3.  ∎

---

# 2. SECOND branch singleton-prefix test

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

Split

```text
C=(b,Y),
```

so the singleton proper prefix is

```text
X=(b),
x=b.
```

The singleton-prefix interleaving is

```text
A B b Y  ->  A b B Y.
```

Let

```text
sA=S_beta=2f-sigma.
```

---

## Lemma A17.5: SECOND singleton partial sums

The nonempty partial sums of

```text
A b B Y
```

are

```text
A_i,
sA+b,
sA+b+B_k,
f+b+Y_m.
```

### Proof

This is Lemma A14.4 with `X=(b)` and `x=b`.  ∎

---

## Lemma A17.6: SECOND singleton forbidden-hit obstructions

Away from the boundary case `beta=h`, the singleton interleaving can hit `f` only through

```text
sA+b+B_k=f.
```

Equivalently,

```text
b=sigma-f-B_k.
```

The other forbidden-hit mechanisms are impossible.

### Proof

From Lemma A17.5, a forbidden hit could occur through:

```text
A_i=f,
sA+b=f,
sA+b+B_k=f,
f+b+Y_m=f.
```

Away from `beta=h`, the block `A` does not contain the original forbidden hit, so `A_i=f` is impossible.

The equation `sA+b=f` is equivalent to

```text
b=f-sA=sigma-f.
```

This would mean the first proper prefix of the tail block `C` has sum `sigma-f`, impossible by Lemma A15.3 unless `C` has length one.  The singleton-prefix move requires `Y` nonempty, so `C` has length at least two.

The equation `f+b+Y_m=f` is equivalent to `Y_m=-b`, impossible by Lemma A16.4.

Thus only `sA+b+B_k=f` remains.  ∎

---

## Lemma A17.7: SECOND singleton Graham-collision obstructions

Away from `beta=h`, the singleton interleaving `AbBY` can fail Graham-validity only through one of the following equations:

```text
A_i = sA+b,
A_i = sA+b+B_k,
sA+b = f+C_s,              2 <= s <= |C|,
sA+b+B_k = f+C_s,          2 <= s <= |C|.
```

The old-collision family

```text
A_i=f+C_s
```

was eliminated by Lemma A16.5.  Internal collisions are old collisions or impossible.

### Proof

This is the SECOND pruned system from A16 with `q=1` and `C_q=b`.  ∎

---

## Lemma A17.8: SECOND singleton failure gives a short trap list for `b`

Away from `beta=h`, if the singleton-prefix interleaving

```text
A B b Y -> A b B Y
```

fails to produce a Graham-valid ordering avoiding `f`, then `b` satisfies at least one equation in the following list:

```text
b = sigma-f-B_k,
b = A_i-sA,
b = A_i-sA-B_k,
b = f+C_s-sA,
b = f+C_s-sA-B_k,
```

with index ranges

```text
1 <= i <= |A|,
1 <= k <= |B|,
2 <= s <= |C|.
```

The boundary case `beta=h` is excluded here because it is already a pair-trap boundary: `A` itself ends at the original forbidden hit.

### Proof

Move all terms not involving `b` to the right-hand side in Lemmas A17.6 and A17.7.  ∎

---

# 3. Relation to the local right-swap obstruction

A5 gives the independent local relation

```text
P+b=S_j,
```

or

```text
b=S_j-P.
```

Therefore, in every equal-sum branch, if the singleton-prefix move fails, then `b` has at least two descriptions:

```text
b = S_j-P
```

and

```text
b in a short trap list from A17.4 or A17.8.
```

Equating these descriptions gives explicit relations among old partial sums.  Many of these relations should either be old Graham collisions, zero-sum bypass intervals, or short pair traps.

This is the next reduction target.

---

# 4. Target A18: local/singleton trap collision

Prove that the local relation

```text
b=S_j-P
```

cannot coexist with the singleton-prefix trap list unless one of the already classified outcomes occurs:

```text
1. backward or forward bypass zero block from A5/A9;
2. boundary pair trap beta=h;
3. old Graham collision;
4. old second f-hit;
5. shorter forbidden-hit ordering.
```

This target is now finite and explicit: substitute `b=S_j-P` into each line of A17.4 and A17.8 and simplify.

---

## Current status

Proved here:

1. FIRST singleton-prefix partial-sum and forbidden/collision trap list;
2. SECOND singleton-prefix partial-sum and forbidden/collision trap list;
3. failure of the singleton-prefix move forces `b` into an explicit short trap list;
4. combining with A5 gives a finite list of old-partial-sum equations to analyze next.

Not proved here:

1. coexistence impossibility with the A5 local relation;
2. full equal-sum branch elimination;
3. endpoint avoidance theorem.
