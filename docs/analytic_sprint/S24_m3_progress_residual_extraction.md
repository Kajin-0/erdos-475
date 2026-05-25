# S24. m=3 progress residual extraction status

This file records the output of `scripts/extract_m3_progress_residuals.py` after S23.

The one-sided right-long-terminal branch has now compressed into:

```text
1. D_short descent by finite block permutation;
2. D_short-neutral rightward terminal progress;
3. small residual: neutral without rightward progress + worse-only.
```

## p=17 extraction

Input:

```text
logs/one_sided_terminal_block_perms_p17.jsonl
```

Command:

```bash
python3 scripts/extract_m3_progress_residuals.py \
  logs/one_sided_terminal_block_perms_p17.jsonl \
  --out logs/m3_progress_residuals_p17.jsonl \
  --summary-out logs/summary_m3_progress_residuals_p17.json
```

Observed summary:

```text
input_records = 852
kept_records  = 68
```

Label counts over all classified one-sided records:

```text
other                           = 583
neutral_with_rightward_progress = 201
neutral_no_rightward_progress   =  19
worse_only                      =  49
```

Thus the unhandled kept residual is:

```text
68 / 852 ≈ 7.98%
```

The handled part is:

```text
(583 + 201) / 852 = 784 / 852 ≈ 92.02%
```

Support lengths:

```text
2: 224
3: 211
4: 217
5: 200
```

Additional flags in the full classified population:

```text
DISTRIBUTED_BRIDGE      =  209
SIGNED_INTERVAL         =   99
LONG_TERMINAL_BRIDGE    = 1527
RIGHT_TERMINAL_BRIDGE   = 1527
```

## p=23 extraction

Input:

```text
logs/one_sided_terminal_block_perms_p23.jsonl
```

Command:

```bash
python3 scripts/extract_m3_progress_residuals.py \
  logs/one_sided_terminal_block_perms_p23.jsonl \
  --out logs/m3_progress_residuals_p23.jsonl \
  --summary-out logs/summary_m3_progress_residuals_p23.json
```

Observed summary:

```text
input_records = 756
kept_records  = 122
```

Label counts over all classified one-sided records:

```text
other                           = 369
neutral_with_rightward_progress = 265
neutral_no_rightward_progress   =  37
worse_only                      =  85
```

Thus the unhandled kept residual is:

```text
122 / 756 ≈ 16.14%
```

The handled part is:

```text
(369 + 265) / 756 = 634 / 756 ≈ 83.86%
```

Support lengths:

```text
2: 171
3: 117
4: 112
5:  93
6:  91
7: 101
8:  71
```

Additional flags in the full classified population:

```text
DISTRIBUTED_BRIDGE      =  288
SIGNED_INTERVAL         =   59
LONG_TERMINAL_BRIDGE    = 1462
RIGHT_TERMINAL_BRIDGE   = 1462
```

## Current reduction status

For the right-one-sided long-terminal branch:

```text
p=17: handled 92.02%, residual 7.98%
p=23: handled 83.86%, residual 16.14%
```

Handled means:

```text
D_short descent
or
D_short-neutral rightward terminal progress.
```

The remaining residual is:

```text
neutral_no_rightward_progress
or
worse_only.
```

## Interpretation

The residual is now small enough to attack directly.

The next split should be:

```text
1. neutral_no_rightward_progress
   - likely same-position moves only;
   - should require a secondary tie-break such as support length, atom multiset, or local pattern rank.

2. worse_only
   - no local permutation preserves or improves the refined order;
   - likely routes to distributed/signed obstructions or requires a special m=3 algebraic contradiction.
```

## Important observation

The retained residual still has nontrivial overlap with already-reduced branches:

```text
DISTRIBUTED_BRIDGE
SIGNED_INTERVAL
```

Therefore some kept records may already be reducible by earlier routes. The residual extractor intentionally keeps them because it is focused on local terminal progress only.

## Next script

Proceed to:

```text
scripts/summarize_m3_progress_residual_details.py
```

Target outputs from:

```text
logs/m3_progress_residuals_p17.jsonl
logs/m3_progress_residuals_p23.jsonl
```

should include:

```text
label counts
support histograms by label
attempt flags by label
best permutation histograms by label
worse new_defect histograms
neutral same-position / leftward-regress counts
whether residual has distributed or signed flags
compact examples for each residual label
```

## Proof priority

The next proof target should be one of:

```text
A. eliminate residuals that already contain distributed/signed flags;
B. prove a same-position neutral tie-break lemma;
C. prove a worse-only m=3 algebraic contradiction.
```

The detail summarizer decides which is highest leverage.

## Status

```text
Residual extracted.
Remaining right-one-sided m=3 terminal set is small.
Next: split kept residual by mechanism.
```
