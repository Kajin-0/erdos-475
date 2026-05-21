# Analytic atom-insertion obstruction table A30

This note continues from A29.

A29 showed that an exposed zero block cannot be repaired by internal reordering alone.  The minimal repair is to insert an outside atom into the zero block.

This note translates the atom-insertion obstruction equations from A29 into interval language.  The result is a finite table showing that each atom-insertion failure is either:

```text
1. an atom-plus-interval zero relation;
2. an equal-interval relation;
3. a two-piece zero composite;
4. a prefix/interior zero branch;
5. a forbidden-hit equation with the same structure.
```

This is not a complete proof.  It is the next bookkeeping reduction needed to make two-piece-zero cases controlled.

---

## Standing setup

Work in an auxiliary ordering containing a displayed segment

```text
X A B q Y
```

where `q` is a single atom and

```text
sum(A)+sum(B)=0.
```

Write endpoints in the auxiliary ordering as

```text
x = endpoint after X,
y = endpoint after XA,
z = endpoint after XAB,
z+1 = endpoint after XABq.
```

Thus:

```text
A=(x,y],
B=(y,z],
q=r_{z+1},
Y begins after z+1.
```

Let the auxiliary partial sums be denoted by `T_i`.

The zero-block condition is

```text
T_z-T_x = sum(A)+sum(B)=0,
```

so

```text
T_z=T_x.
```

The atom insertion move is

```text
X A B q Y  ->  X A q B Y.
```

A29 showed that this breaks the zero-block endpoint collision because `q != 0`.

---

## Prefix notation inside the displayed segment

For `1 <= i <= |A|`, write

```text
A_i = T_{x+i}-T_x.
```

For `1 <= j <= |B|`, write

```text
B_j = T_{y+j}-T_y.
```

For `1 <= m <= |Y|`, write

```text
Y_m = T_{z+1+m}-T_{z+1}.
```

Let

```text
a=sum(A)=T_y-T_x.
```

Since `sum(A)+sum(B)=0`,

```text
sum(B)=-a.
```

---

# 1. A29 atom-insertion obstruction equations

A29 gave the following possible Graham-collision obstruction equations for the atom insertion:

```text
(Q1) q=A_i-a,
(Q2) q=Y_m-a,
(Q3) B_j=A_i-a-q,
(Q4) B_j=Y_m-a,
(Q5) B_j=0.
```

A29 also gave forbidden-hit equations of the same translated-prefix type.  Those are treated after the collision table.

---

# 2. Collision obstruction table

## Lemma A30.1: Q1 is an atom-plus-tail-zero relation

Equation `(Q1)`

```text
q=A_i-a
```

is equivalent to

```text
q + sum(x+i,y] = 0.
```

### Proof

Since

```text
A_i=T_{x+i}-T_x,
a=T_y-T_x,
```

we have

```text
A_i-a = T_{x+i}-T_y = -sum(x+i,y].
```

Thus `q=A_i-a` is equivalent to

```text
q=-sum(x+i,y],
```

or

```text
q+sum(x+i,y]=0.
```

∎

### Status

This is a two-piece zero composite consisting of the atom `q` and the tail of `A` after the internal cut `i`.

---

## Lemma A30.2: Q2 is an equal-interval relation

Equation `(Q2)`

```text
q=Y_m-a
```

is equivalent to

```text
sum(x,y] + q = Y_m.
```

In endpoint form:

```text
T_y-T_x + (T_{z+1}-T_z) = T_{z+1+m}-T_{z+1}.
```

Because `T_z=T_x`, this can also be written as

```text
T_y + T_{z+1} - 2T_x = T_{z+1+m}-T_{z+1}.
```

### Proof

The equation `q=Y_m-a` rearranges immediately to

```text
a+q=Y_m.
```

Since `a=sum(x,y]`, the claim follows.  ∎

### Status

This is not generally a zero interval.  It is an equal-sum relation between the composite interval `Aq` and a prefix of `Y`.  It should be routed to equal-interval/midpoint machinery after making `Aq` contiguous in the relevant moved ordering.

---

## Lemma A30.3: Q3 is an atom-plus-B-prefix equals negative A-tail relation

Equation `(Q3)`

```text
B_j=A_i-a-q
```

is equivalent to

```text
q + B_j + sum(x+i,y] = 0.
```

### Proof

As in Lemma A30.1,

```text
A_i-a=-sum(x+i,y].
```

Therefore

```text
B_j=-sum(x+i,y]-q,
```

which rearranges to

```text
q+B_j+sum(x+i,y]=0.
```

∎

### Status

This is a three-piece zero composite: atom `q`, a prefix of `B`, and a tail of `A`.  Since `A` and `B` are adjacent around the internal cut, moving `q` or rotating the subblocks can potentially contiguize two of the three pieces.

---

## Lemma A30.4: Q4 is an equal-interval relation between `A+B_j` and a prefix of `Y`

Equation `(Q4)`

```text
B_j=Y_m-a
```

is equivalent to

```text
sum(A)+B_j=Y_m.
```

In interval notation:

```text
sum(x,y+j]=Y_m.
```

where `(x,y+j]` consists of all of `A` followed by the first `j` entries of `B`.

### Proof

Rearrange `B_j=Y_m-a` to

```text
a+B_j=Y_m.
```

But `a+B_j=sum(x,y+j]`.  ∎

### Status

This is an equal-interval relation.  It routes to A20/A26 equal-interval reduction machinery.

---

## Lemma A30.5: Q5 is a zero-prefix inside `B`

Equation `(Q5)`

```text
B_j=0
```

is equivalent to

```text
sum(y,y+j]=0.
```

If the starting endpoint `y` is a nonbase nonempty partial-sum index in the auxiliary ordering, this is an interior zero interval.  If `y=0`, this is a prefix-zero branch.

### Proof

This is the definition of `B_j`.  ∎

---

# 3. Forbidden-hit obstruction table

In the atom-insertion setting, A29 gives possible forbidden-hit equations from the changed values:

```text
(H1) x+a+q=f,
(H2) x+a+q+B_j=f.
```

Here `x` denotes the running sum value before `A`, not the endpoint index.  In endpoint-index notation the running value is `T_x`.

## Lemma A30.6: H1 is a single landing equation for the inserted atom

Equation `(H1)` is

```text
T_y+q=f.
```

Thus the atom `q` inserted after `A` lands directly on the forbidden value.

### Status

This is exactly the same type of single-atom forbidden landing equation studied in the A5/A17 local obstruction layers.

---

## Lemma A30.7: H2 is a forbidden landing after a B-prefix

Equation `(H2)` is

```text
T_y+q+B_j=f.
```

Equivalently,

```text
q+B_j=f-T_y.
```

This is an atom-plus-prefix landing equation.

### Status

If this equation blocks every possible atom insertion, the blocker set is a translated prefix family.  This should be handled by the same prefix-trap method used in A14--A17.

---

# 4. Routing summary

Every atom-insertion obstruction routes to an already named class.

| Case | Equation | Routed class |
|---|---|---|
| Q1 | `q+tail(A)=0` | two-piece zero composite |
| Q2 | `A+q=prefix(Y)` | equal-interval / midpoint branch |
| Q3 | `q+B_prefix+tail(A)=0` | three-piece zero composite |
| Q4 | `A+B_prefix=prefix(Y)` | equal-interval branch |
| Q5 | `B_prefix=0` | interior-zero or prefix-zero branch |
| H1 | `T_y+q=f` | atom forbidden landing |
| H2 | `T_y+q+B_prefix=f` | atom-plus-prefix forbidden landing |

Thus atom insertion does not introduce an unstructured obstruction.  It returns to the same family of interval and prefix-trap objects already present earlier in the proof tree.

---

# 5. Target A31: descent for atom-insertion obstruction graph

The remaining task is to prove that this routing is a **descent**, not merely a recurrence.

A natural measure is a tuple such as

```text
(total span of zero composite,
number of pieces in the composite,
distance of inserted atom from the zero block,
first forbidden-hit index)
```

The desired theorem is:

> Every atom-insertion obstruction from A30 either collapses immediately or produces a residual object with strictly smaller measure than the two-piece-zero object that led to the insertion attempt.

If this is proved, then `residual_two_piece_zero` and `residual_separated_signed` become controlled finite-descent classes.

---

## Current status

Proved here:

1. Q1 routes to atom-plus-tail zero;
2. Q2 routes to equal-interval/midpoint structure;
3. Q3 routes to a three-piece zero composite;
4. Q4 routes to equal-interval structure;
5. Q5 routes to interior-zero/prefix-zero;
6. forbidden-hit equations route to atom/prefix landing equations.

Not proved here:

1. strict descent for every routed obstruction;
2. successful atom insertion existence;
3. endpoint avoidance theorem.
