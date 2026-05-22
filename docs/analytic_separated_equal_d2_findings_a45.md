# Analytic separated-equal D2 findings A45

This note records the result of the stronger A44 search.

Log:

```text
logs/a44_separated_equal_d2_search_summary.txt
```

Tool:

```text
scripts/search_separated_equal_d2_model.py
```

---

## Main finding

The stronger local model still admits balanced D2 survivors.

The model enforced:

```text
1. distinct nonzero atoms in A,G,C,Y;
2. sum(A)=sum(C);
3. active D2: C_k=2a+g+Y_m;
4. balanced transfer: m=k;
5. A41 residual difference-walk condition;
6. absence of D1/D3/D4/D5 for all prefixes;
7. local Graham distinctness of A G C Y.
```

Even with these constraints, survivors occur for small fields.

---

## Representative survivor

Over `F_7`:

```text
A=[1]
G=[3]
C=[2,6]
Y=[4]
```

Then:

```text
sum(A)=1,
sum(C)=2+6=1 mod 7,
g=3.
```

D2 with `k=m=1` says:

```text
C_1 = 2a+g+Y_1.
```

Check:

```text
2 = 2*1 + 3 + 4 = 9 = 2 mod 7.
```

The local partial sums of `A G C Y` are:

```text
[1,4,6,5,2],
```

which are distinct modulo `7`.

---

## Consequence

Balanced D2 cannot be eliminated using only:

```text
local A,G,C,Y algebra,
D1/D3/D4/D5 absence,
local Graham distinctness,
A41 difference-walk endpoint avoidance.
```

Additional global structure is required.

---

## Structural observation

The first surviving examples are dominated by the boundary case:

```text
k=m=1.
```

This case has no intermediate difference-walk values.  Therefore the A41 mechanisms based on:

```text
intermediate D_r=0,
intermediate D_r=target,
repeated D_r=D_s
```

cannot apply.

So the balanced branch should split into:

```text
1. atom-balanced D2 boundary: k=m=1;
2. proper balanced D2: k=m>=2.
```

---

## Atom-balanced D2 boundary

When `k=m=1`, D2 reads:

```text
c_1 = 2a+g+y_1.
```

Using `C=c_1 L` with `sum(C)=a`, this becomes:

```text
sum(A G L y_1)=0.
```

This is the D2 composite-zero relation from A38/A40, but with the shortest possible transfer length.

There is no shorter balanced transfer prefix.

Thus any descent must come from:

```text
1. pair moves involving c_1 and y_1;
2. zero-composite surgery on A G L y_1;
3. global recurrence/minimality constraints;
4. compatibility with local/cyclic first-hit obstructions.
```

---

## Target A46

Analyze the atom-balanced D2 boundary:

```text
k=m=1,
C_1=2a+g+Y_1.
```

Suggested move:

Compare the atoms `c_1` and `y_1` directly.

Since

```text
c_1-y_1=2a+g=sum(A G C)-a? 
```

and

```text
sum(A G tail_1(C) y_1)=0,
```

one should try the pair swap or insertion involving `c_1` and `y_1`, analogous to the Q2 pair-difference analysis in A33.

Expected outcomes:

```text
1. strict support descent;
2. pair trap;
3. zero-prefix/interior-zero collapse;
4. forbidden-hit recurrence controlled by A34.
```

---

## Current status

Observed here:

1. A44 stronger local model has survivors;
2. survivors occur already at `k=m=1`;
3. local constraints still insufficient;
4. atom-balanced D2 boundary is now the next branch to analyze.

Not proved:

1. atom-balanced D2 elimination;
2. proper balanced D2 elimination for `k>=2`;
3. endpoint avoidance theorem.
