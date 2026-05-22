# Analytic balanced-transfer search A42

This note documents the finite-search tool:

```text
scripts/search_balanced_transfer_walks.py
```

It targets the residual injective endpoint-avoiding difference-walk branch from A41.

---

## A41 residual model

In the balanced D2 branch, we have two equal-length blocks

```text
K=(c_1,...,c_k),
M=(y_1,...,y_k).
```

Define

```text
D_r = (c_1+...+c_r) - (y_1+...+y_r).
```

A41 showed that the non-descending residual case has:

```text
D_0=0,
D_k=T,
D_1,...,D_{k-1} avoid 0 and T,
D_0,...,D_k pairwise distinct,
c_r-y_r != 0,
```

where

```text
T=2a+g.
```

If there is an intermediate `D_r=0`, `D_r=T`, or repeated value `D_r=D_s`, the branch descends to a smaller equal-interval or shorter balanced-transfer object.

---

## What the tool searches

The script searches for local residual witnesses over `F_p` satisfying:

```text
1. C and Y are ordered k-tuples of nonzero residues;
2. all atoms in C and Y are distinct;
3. increments c_r-y_r are nonzero;
4. D_0,...,D_k are pairwise distinct;
5. D_1,...,D_{k-1} avoid 0 and target;
6. D_k=target.
```

This is a local model.  It does not enforce every global Graham-validity or endpoint-avoidance constraint from the original theorem.

A found example means:

```text
this local residual walk is not impossible by the A41 conditions alone.
```

It is not a counterexample to the theorem.

---

## Usage

Single case:

```bash
python3 scripts/search_balanced_transfer_walks.py \
  --single --p 11 --k 3 --limit 5
```

Single case with fixed target:

```bash
python3 scripts/search_balanced_transfer_walks.py \
  --single --p 11 --k 3 --target 4 --limit 5
```

Sweep:

```bash
python3 scripts/search_balanced_transfer_walks.py \
  --sweep --max-p 17 --max-k 4 --limit 3 --json
```

---

## Interpretation

If residual walks exist freely in this local model, then the analytic proof cannot eliminate A41 using only the difference-walk endpoint-avoidance conditions.

One must use additional global structure, for example:

```text
1. K and M sit inside a larger Graham-valid ordering;
2. K is a prefix of C and M is a prefix of Y specifically;
3. the D2 equation came from separated equal-interval exchange;
4. other A36 collision equations must be absent simultaneously;
5. forbidden-hit recurrences must satisfy A34 measure constraints.
```

---

## Current status

Implemented:

1. local residual balanced-transfer walk checker;
2. single-case search;
3. sweep over small primes and k;
4. JSON output.

Not implemented:

1. global Graham-validity constraints;
2. simultaneous absence of all other separated-equal surgery obstructions;
3. integration with the full A19/A24 symbolic state;
4. endpoint avoidance theorem.
