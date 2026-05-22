# Analytic separated-equal D2 search A44

This note documents the stronger finite-search model:

```text
scripts/search_separated_equal_d2_model.py
```

A43 showed that the local A41 balanced-transfer difference-walk conditions are insufficient by themselves.  A44 strengthens the model by including the surrounding separated-equal structure.

---

## Setup modeled

The script models blocks

```text
X A G C Y
```

but searches only the local algebraic block data

```text
A,G,C,Y
```

with nonzero distinct atoms in `F_p^*`.

It enforces:

```text
sum(A)=sum(C).
```

The direct exchange under study is:

```text
X A G C Y -> X C G A Y.
```

---

## D2 active condition

The D2 branch from A36 is:

```text
D2: C_k = 2a + g + Y_m,
```

where

```text
a=sum(A)=sum(C),
g=sum(G).
```

The script searches for configurations where D2 occurs.

Optional flag:

```text
--require-balanced
```

restricts to the balanced-transfer case:

```text
m=k.
```

and also checks the A41 residual difference-walk conditions.

---

## Simultaneous absence of other direct-exchange collisions

A44 also requires the other A36 direct-exchange collision equations to be absent:

```text
D1: C_k = a + G_j
D3: A_i = G_j - g
D4: A_i = a + Y_m
D5: C_k = a + g + A_i
```

for all valid internal prefix indices.

This is the key strengthening over A42.

---

## Optional local Graham condition

The flag

```text
--require-local-graham
```

requires the concatenated local segment

```text
A G C Y
```

to have pairwise distinct nonempty partial sums.

This is still weaker than the full global Graham-validity condition because the external block `X` and the rest of the ordering are omitted.

---

## Usage

Single case:

```bash
python3 scripts/search_separated_equal_d2_model.py \
  --single --p 11 --A 2 --G 1 --C 2 --Y 2 --limit 5
```

Balanced only:

```bash
python3 scripts/search_separated_equal_d2_model.py \
  --single --p 11 --A 2 --G 1 --C 2 --Y 2 \
  --require-balanced --limit 5
```

Balanced plus local Graham:

```bash
python3 scripts/search_separated_equal_d2_model.py \
  --single --p 11 --A 2 --G 1 --C 2 --Y 2 \
  --require-balanced --require-local-graham --limit 5
```

Sweep:

```bash
python3 scripts/search_separated_equal_d2_model.py \
  --sweep --max-p 11 --max-len 3 \
  --require-balanced --require-local-graham --limit 3
```

---

## Interpretation

A surviving example means:

```text
The separated-equal D2 branch survives the local algebraic constraints,
absence of D1/D3/D4/D5,
and optional local Graham distinctness.
```

It still does not imply a theorem counterexample because it does not enforce:

```text
1. full global Graham-validity including X and external blocks;
2. endpoint-avoidance minimality;
3. forbidden-hit recurrence constraints from A34;
4. simultaneous absence of gap-after move obstructions;
5. cyclic/local obstruction compatibility.
```

---

## Current status

Implemented:

1. local A,G,C,Y model;
2. `sum(A)=sum(C)` enforcement;
3. D2 detection;
4. absence of D1/D3/D4/D5;
5. optional balanced-transfer restriction;
6. optional local Graham distinctness;
7. single-case and sweep modes.

Not yet done:

1. run and log sweeps;
2. integrate gap-after obstruction absence;
3. enforce full global ordering constraints;
4. endpoint avoidance theorem.
