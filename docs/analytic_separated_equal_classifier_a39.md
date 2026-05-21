# Analytic separated equal classifier A39

This note documents the separated-equal surgery classifier:

```text
scripts/classify_separated_equal_surgery.py
```

It encodes the branch routing from:

```text
docs/analytic_separated_equal_interval_surgery_a36.md
docs/analytic_d1_d5_span_descent_a37.md
docs/analytic_weighted_transported_prefix_a38.md
```

---

## Setup

The separated equal-interval residual has the form:

```text
X A G C Y
```

with

```text
sum(A)=sum(C)=a.
```

The direct exchange is:

```text
X A G C Y -> X C G A Y.
```

A36 gives five possible collision branches:

```text
D1: C_k = a + G_j
D2: C_k = 2a + g + Y_m
D3: A_i = G_j - g
D4: A_i = a + Y_m
D5: C_k = a + g + A_i
```

A39 classifies these branches by positional parameters.

---

## Usage

### D1 example

```bash
python3 scripts/classify_separated_equal_surgery.py \
  --branch D1 --A 5 --G 4 --C 6 --j 2 --k 3
```

### D5 proper-interior example

```bash
python3 scripts/classify_separated_equal_surgery.py \
  --branch D5 --A 5 --G 4 --C 6 --i 2 --k 3
```

JSON output:

```bash
python3 scripts/classify_separated_equal_surgery.py \
  --branch D5 --A 5 --G 4 --C 6 --i 2 --k 3 --json
```

---

## Output classes

The classifier returns classes such as:

```text
equal_interval_descent
zero_collapse
two_piece_zero
three_piece_zero
three_piece_zero_strict_span
```

and a status such as:

```text
controlled_descent
controlled_composite_zero
closed_or_prefix_zero
composite_zero_descent_accounting_needed
```

---

## Branch routing

### D1

```text
C_k = a + G_j
```

Routes to:

```text
k=|C|      -> G_j=0, zero collapse
k<|C|      -> equal interval descent
```

### D2

```text
C_k = 2a + g + Y_m
```

Routes to:

```text
k=|C|      -> two-piece zero: sum(AG)+Y_m=0
k<|C|      -> three-piece zero: sum(AG)+tail(C)+Y_m=0
```

The `k<|C|` case needs descent accounting because the added `Y_m` support can offset the removed `C_k` support.

### D3

```text
A_i = G_j - g
```

Routes to:

```text
j=|G|      -> A_i=0, zero collapse
j<|G|      -> two-piece zero: A_i+tail(G)=0
```

### D4

```text
A_i = a + Y_m
```

Routes to:

```text
i=|A|      -> Y_m=0, zero collapse
i<|A|      -> two-piece zero: tail(A)+Y_m=0
```

### D5

```text
C_k = a + g + A_i
```

Routes to:

```text
i=|A|, k=|C|  -> two-piece/zero: sum(AG)=0
i=|A|         -> two-piece zero: sum(AG)+tail(C)=0
k=|C|         -> two-piece zero: prefix(A)+sum(G)=0
proper case   -> strict-span three-piece zero: prefix(A)+G+tail(C)=0
```

---

## Significance

Before A38/A39, D5 looked like a hard weighted transported-prefix branch.  The classifier now encodes the corrected routing:

```text
D5 proper-interior -> strict-span three-piece zero composite
```

Thus direct-exchange collision branches for separated equal intervals are no longer unclassified.

The remaining hard issues are:

```text
1. composite-zero descent accounting, especially D2 with long Y_m;
2. forbidden-hit recurrences from direct exchange;
3. gap-after move obstruction equations;
4. global recurrence descent from A34.
```

---

## Current status

Implemented:

1. D1--D5 positional routing;
2. endpoint collapse detection;
3. strict-span D5 proper-interior classification;
4. JSON output for audits.

Not implemented:

1. batch sweeps over separated-equal surgery parameters;
2. field-realizability checks;
3. recurrence-descent verification;
4. endpoint avoidance theorem.
