# Analytic zero-block breaking A29: why internal rotation is insufficient and how to insert a gap

This note continues from A28.

A28 showed that a two-piece-zero composite

```text
A G C,   sum(A)+sum(C)=0
```

can be contiguized by moving the gap:

```text
A G C -> A C G.
```

The resulting block

```text
Z=A C
```

is a contiguous zero-sum block.  This note records the next necessary step: a contiguous zero block cannot be repaired by merely reordering its internal entries.  To break the endpoint collision, one must insert material from outside the zero block into its interior, or move a proper subblock out.

This is a structural fact.  It prevents a false proof shortcut.

---

## Standing notation

Let an ordering contain a displayed segment

```text
X Z Y
```

where

```text
sum(Z)=0.
```

Write

```text
x=sum(X).
```

If `Z=(z_1,...,z_n)`, write internal prefix sums

```text
Z_k=z_1+...+z_k.
```

---

# 1. Internal reorder cannot remove the endpoint collision

## Lemma A29.1: internal reorder of a zero block preserves the zero-block endpoint collision

Let `Z'` be any reordering of the entries of `Z`.  Then

```text
sum(Z')=0.
```

Therefore in the ordering

```text
X Z' Y
```

the running sum immediately before `Z'` and immediately after `Z'` is the same value `x`.

Consequently, if the index before `Z` corresponds to a nonempty partial sum, then every internal reordering of `Z` still has a Graham collision between the partial sum before `Z'` and the partial sum after `Z'`.

If the index before `Z` is the basepoint, then every internal reordering of `Z` still has a prefix-zero endpoint.

### Proof

Reordering does not change total sum.  Since `sum(Z)=0`, every reordering `Z'` also has sum zero.  Thus the running sum before `Z'` is `x`, and the running sum after `Z'` is `x+sum(Z')=x`.  This is exactly the endpoint collision or prefix-zero endpoint.  ∎

### Consequence

A zero-block repair must change the boundary structure of the zero block.  It is not enough to cyclically rotate or permute the entries inside `Z`.

The repair must do one of the following:

```text
1. insert an outside atom/block into the middle of Z;
2. move a proper nonzero-sum subblock of Z outside the block;
3. merge Z with an adjacent block so the old zero endpoint is no longer an endpoint.
```

---

# 2. Standard insertion move

The most direct zero-block breaking move inserts the adjacent gap `G` into the zero block.

Let a displayed segment be

```text
X A B G Y
```

with

```text
sum(A)+sum(B)=0.
```

Thus `Z=A B` is a contiguous zero block.  Let

```text
a=sum(A),
b=sum(B)=-a,
g=sum(G).
```

The insertion move is

```text
X A B G Y  ->  X A G B Y.
```

This inserts `G` between `A` and `B`, breaking the contiguity of the zero block `AB`.

---

## Lemma A29.2: insertion partial-sum formula

Let internal prefix sums be

```text
A_i,
B_j,
G_k,
Y_m.
```

In the original ordering `XABGY`, the displayed-region partial sums are

```text
x+A_i,
x+a+B_j,
x+G_k,
x+g+Y_m.
```

In the insertion ordering `XAGBY`, they are

```text
x+A_i,
x+a+G_k,
x+a+g+B_j,
x+g+Y_m.
```

Therefore:

1. the `A` family is unchanged;
2. the post-region `Y` family is unchanged;
3. the `G` family is translated by `+a` relative to its old position;
4. the `B` family is translated by `+g` relative to its old position after `A`.

### Proof

Original `XABGY`:

- after `A_i`: `x+A_i`;
- after `A B_j`: `x+a+B_j`;
- after all of `AB` and then `G_k`: since `a+b=0`, the value is `x+G_k`;
- after `ABG` and then `Y_m`: `x+g+Y_m`.

New `XAGBY`:

- after `A_i`: `x+A_i`;
- after `A G_k`: `x+a+G_k`;
- after `AGB_j`: `x+a+g+B_j`;
- after `AGB` and then `Y_m`: since `a+g+b=g`, the value is `x+g+Y_m`.

This gives all formulas.  ∎

---

## Lemma A29.3: insertion removes the zero-block endpoint collision if `g != 0`

In `XABGY`, the endpoint after `AB` has running value

```text
x.
```

In `XAGBY`, the endpoint after `AGB` has running value

```text
x+g.
```

Thus the old zero-block endpoint value is not repeated at the end of the moved block provided

```text
g != 0.
```

### Proof

In the new order, the total displayed block `AGB` has sum

```text
a+g+b=g.
```

So the endpoint value is `x+g`.  If `g != 0`, this differs from `x`.  ∎

### Note

If `G` is a nonempty block with total zero, insertion of the whole block does not break the endpoint collision.  In that case one should use a proper nonzero-sum prefix of `G`, or treat `G` itself as a zero-block/prefix-zero branch.

---

# 3. Insertion obstruction equations

## Lemma A29.4: exact Graham-collision obstruction list for insertion

Assume the original ordering `XABGY` is Graham-valid except for the exposed zero-block endpoint issue being studied in an auxiliary ordering.  Then the insertion ordering `XAGBY` can have a new collision only through equations involving one of the changed families

```text
x+a+G_k,
x+a+g+B_j.
```

The full list of possible new cross-collisions is:

### New G-family against unchanged families

```text
x+a+G_k = x+A_i,
x+a+G_k = x+g+Y_m.
```

Equivalently:

```text
G_k=A_i-a,
G_k=g-a+Y_m.
```

### New B-family against unchanged families

```text
x+a+g+B_j = x+A_i,
x+a+g+B_j = x+g+Y_m.
```

Equivalently:

```text
B_j=A_i-a-g,
B_j=Y_m-a.
```

### New G-family against new B-family

```text
x+a+G_k = x+a+g+B_j,
```

or

```text
G_k=g+B_j.
```

Internal collisions within the translated `G` or `B` families are inherited from internal prefix collisions of those blocks.

### Proof

By Lemma A29.2, only the `G` and `B` families change.  Any new collision must involve at least one changed family.  Listing pairings of the changed families with unchanged `A`, unchanged `Y`, and with each other gives the displayed equations.  ∎

---

## Lemma A29.5: exact forbidden-hit obstruction list for insertion

Let `f` be the forbidden value.  If unchanged families avoid `f`, then the insertion ordering `XAGBY` can hit `f` only if

```text
x+a+G_k=f,
x+a+g+B_j=f.
```

Equivalently:

```text
G_k=f-x-a,
B_j=f-x-a-g.
```

### Proof

Only the `G` and `B` families change, by Lemma A29.2.  ∎

---

# 4. Atom insertion as the minimal case

The most important special case is when `G` is a single atom `q`.

Then `g=q`, and there are no proper internal `G_k` except the endpoint `q` itself.

## Lemma A29.6: atom insertion formulas

For

```text
X A B q Y -> X A q B Y,
```

where

```text
sum(A)+sum(B)=0,
q != 0,
```

the old zero-block endpoint collision is broken.  The changed partial sums are:

```text
x+a+q,
x+a+q+B_j.
```

The possible new collision equations are:

```text
x+a+q = x+A_i,
x+a+q = x+q+Y_m,
x+a+q+B_j = x+A_i,
x+a+q+B_j = x+q+Y_m,
x+a+q = x+a+q+B_j.
```

Equivalently:

```text
q=A_i-a,
q=Y_m-a,
B_j=A_i-a-q,
B_j=Y_m-a,
B_j=0.
```

The equation `B_j=0` is an internal zero-prefix of `B`; depending on position, it is either an exposed interior zero branch or a prefix-zero branch.

### Proof

Specialize Lemmas A29.2--A29.4 to `G=(q)`.  ∎

---

# 5. Relation to the endpoint-avoidance proof tree

A28 converts two-piece zero composites into exposed zero blocks.

A29 says:

```text
exposed zero block + outside gap/atom
    -> insert outside material into the block
    -> either break the endpoint collision
    -> or satisfy explicit translated-prefix obstruction equations.
```

This parallels earlier stages:

```text
A5 right-swap obstruction
A9 zero-block relocation
A14 proper-prefix interleaving
A28 two-piece-zero contiguization
```

All reduce failure to explicit finite equations among translated prefix families.

---

## Target A30

The next useful step is to connect A29 insertion obstructions back to the A20/A21 interval classes.

Specifically:

1. translate each obstruction equation in Lemma A29.4 into an equal-interval, signed-equal-interval, prefix-zero, or pair-trap relation;
2. prove that obstruction equations either reduce total span or return to an already classified residual class;
3. use this to make two-piece-zero composites a controlled reduction class rather than a terminal obstruction.

---

## Current status

Proved here:

1. internal reorder of a zero block cannot remove its endpoint collision;
2. insertion move partial-sum formula;
3. insertion breaks the zero endpoint if the inserted block has nonzero total;
4. exact Graham-collision obstruction equations for insertion;
5. exact forbidden-hit obstruction equations for insertion;
6. atom-insertion special case.

Not proved here:

1. existence of a successful insertion;
2. reduction of all insertion obstructions to known residual classes;
3. endpoint avoidance theorem.
