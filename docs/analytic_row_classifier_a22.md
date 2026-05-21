# Analytic row classifier A22: orientation-correct residual classifier

This note documents the row-specific residual classifier:

```text
scripts/classify_a19_residual_row.py
```

It builds on:

```text
scripts/classify_interval_traps.py
```

and applies it to the residual families from A19.

---

## Orientation correction

A19 informally wrote the local blocker relation as an interval relation

```text
b = S_j - S_{h-1} = sum(h-1,j].
```

This is only literally a forward interval when

```text
j > h-1.
```

If

```text
j < h-1,
```

then

```text
b = S_j-S_{h-1} = -sum(j,h-1].
```

The A22 classifier handles this automatically by representing every difference

```text
S_r-S_l
```

as an oriented interval:

```text
+sum(l,r]    if r>l,
-sum(r,l]    if r<l.
```

This correction matters because it changes whether the final interval relation is equal or signed-equal.

---

## Tool usage

Example:

```bash
python3 scripts/classify_a19_residual_row.py \
  --family F1r --t 30 --h 10 --j 14 --i 4
```

This means:

```text
local:    b = S_j - S_{h-1}
F1r:      b = S_h - S_i
```

The tool normalizes both sides to oriented intervals and calls the A21 classifier.

For JSON output:

```bash
python3 scripts/classify_a19_residual_row.py \
  --family S5r --t 40 --h 15 --j 9 --beta 5 --k 3 --s 10 --json
```

---

## Supported residual families

```text
F1r, F2r, F3r, F4r, F5r, F6r,
S1r, S2r, S3r, S4r, S5r
```

`F2r` is special because it is already the prefix-zero branch:

```text
S_i=0.
```

The classifier rejects it as not an atom-equals-interval row.

---

## Residual family mappings

### FIRST branch

```text
F1r: b = S_h - S_i
F3r: b = S_{h+s} - S_0
F4r: b = S_{alpha+m} - S_0
F5r: b = S_{h+s} - S_i
F6r: b = S_{alpha+m} - S_i
```

### SECOND branch

```text
S1r: b = S_h - S_{beta+k}
S2r: b = S_i - S_beta
S3r: b = S_i - S_{beta+k}
S4r: b = S_{h+s} - S_beta
S5r: b = S_{h+s} - S_{beta+k}
```

The local blocker is always:

```text
local: b = S_j - S_{h-1}.
```

The tool compares the local oriented interval with the residual oriented interval.

---

## Output interpretation

The classifier outputs:

```text
local_oriented_interval
residual_oriented_interval
relation_sign
normalized_relation
geometry_class
derived
reason
```

For example, if both oriented intervals have positive sign, the relation is equal:

```text
sum(I)=sum(J).
```

If the signs differ, the relation is signed-equal:

```text
sum(I)=-sum(J).
```

The geometry class is inherited from A21, e.g.

```text
collapse_old_collision
collapse_prefix_zero
collapse_interior_zero
reduction_equal_outer_pieces
residual_two_piece_zero
residual_midpoint
residual_separated_equal
residual_separated_signed
residual_signed_overlap_weighted
```

---

## Current status

Implemented:

1. row-specific mapping for all A19 residual families except prefix-zero F2r;
2. orientation-correct normalization of `S_r-S_l` differences;
3. automatic reduction to A21 interval geometry classes;
4. JSON output for future batch classification.

Not implemented:

1. automatic generation of all branch-valid index ranges;
2. inequality-aware collapse using facts like `j<h` or `alpha>=2h`;
3. final mathematical elimination of residual classes;
4. endpoint avoidance theorem.
