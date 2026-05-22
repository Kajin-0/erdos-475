# Analytic balanced-transfer findings A43

This note records the result of the A42 local search.

Log:

```text
logs/a42_balanced_transfer_search_summary.txt
```

Tool:

```text
scripts/search_balanced_transfer_walks.py
```

---

## Main finding

The local A41 residual difference-walk conditions are not sufficient to eliminate the balanced-transfer branch.

Residual walks exist in small finite fields.

Examples include:

```text
p=5, k=2
p=7, k=3
p=11, k=4
p=13, k=4
p=17, k=4
```

---

## Representative example

For

```text
p=7,
k=3,
target=1,
```

one local residual witness is:

```text
C = [3, 6, 2]
Y = [1, 5, 4]
```

Then the increments are:

```text
c_r-y_r = [2, 1, 5]
```

and the difference walk is:

```text
D = [0, 2, 3, 1].
```

This satisfies:

```text
D_0=0,
D_3=1,
D_1,D_2 avoid 0 and 1,
D_0,D_1,D_2,D_3 are pairwise distinct,
all increments are nonzero,
all C/Y atoms are nonzero and pairwise distinct.
```

---

## Consequence

A41 cannot be closed by a lemma of the form:

> Every injective endpoint-avoiding difference walk is impossible.

That statement is false in the local model.

Therefore, a proof must use additional global constraints.

---

## Additional constraints that remain unused by A42

The local search does not enforce:

```text
1. the full original ordering is Graham-valid;
2. K is a prefix of C and M is a prefix of Y inside X A G C Y;
3. sum(A)=sum(C) in the larger separated-equal setup;
4. D2 came specifically from the direct exchange XAGCY -> XCGAY;
5. all other D1, D3, D4, D5 collision equations are absent simultaneously;
6. direct exchange forbidden-hit equations are absent or controlled by A34;
7. endpoint avoidance failure is globally minimal.
```

These constraints are likely necessary.

---

## Target A44

The next useful step is to strengthen the search model by enforcing simultaneous absence of all other direct-exchange obstruction equations from A36.

For the separated-equal setup:

```text
X A G C Y,
sum(A)=sum(C),
```

D2 is only relevant as the active obstruction if the other direct-exchange collision branches are absent:

```text
D1: C_k = a + G_j,
D3: A_i = G_j - g,
D4: A_i = a + Y_m,
D5: C_k = a + g + A_i.
```

A44 should implement a stronger finite search that models blocks `A,G,C,Y`, enforces `sum(A)=sum(C)`, triggers D2, and checks whether D1/D3/D4/D5 are all absent.

If no examples survive this stronger model for small fields, that gives evidence for an analytic simultaneous-obstruction lemma.

---

## Current status

Proved/observed here:

1. local balanced-transfer residual walks exist;
2. A41 endpoint/injectivity conditions alone are insufficient;
3. the next proof must use simultaneous separated-equal structure.

Not proved:

1. simultaneous-obstruction elimination;
2. global recurrence descent;
3. endpoint avoidance theorem.
