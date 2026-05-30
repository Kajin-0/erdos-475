# Insertion block analyzer runbook

This runbook explains how to use

```text
scripts/analyze_insertion_blocks.py
```

to connect finite witness data with the analytic insertion/cut-cover proof program.

## 1. Direct single-instance mode

Use this mode when you want to analyze a specific valid ordering `C` and candidate inserted element `x`.

Example:

```bash
python scripts/analyze_insertion_blocks.py \
  --p 5 \
  --order 1,2 \
  --x 3
```

The script prints:

```text
blocked_count
unblocked_count
blocked_cuts
unblocked_cuts
endpoint_blocked_cuts
crossing_intervals
cut_multiplicities
```

Interpretation:

```text
unblocked_count > 0
```

means at least one insertion cut produces a Graham-valid ordering after inserting `x`.

```text
unblocked_count = 0
```

means the chosen ordering `C` is fully blocked for that particular `x`.  This does not prove a counterexample, because a different valid ordering of `A\{x}` may have an unblocked cut.

## 2. Witness JSONL deletion mode

Use this mode on minimal witness files with rows of the form:

```json
{"p":29,"B":[1,2,5],"final_order":[...]}
```

For each row, the script deletes each element `x` from `final_order`.  If the remaining order is still Graham-valid, it analyzes insertion of `x` back into that deletion order.

Example:

```bash
python scripts/analyze_insertion_blocks.py \
  --witness-jsonl certificates/minimal_witnesses.jsonl \
  --limit 1000 \
  --jsonl-out logs/insertion_block_sample.jsonl
```

The summary reports:

```text
records
valid_deletion_orders
invalid_deletion_orders
fully_blocked_valid_deletions
min_unblocked
max_blocked
max_crossing_intervals
max_cut_multiplicity
```

## 3. What to look for

The most important diagnostic is:

```text
fully_blocked_valid_deletions
```

If this is zero across many witnesses, the insertion strategy has strong empirical support: deleting an element from known witnesses often leaves a valid ordering with at least one way to reinsert the element.

If this is nonzero, those cases are valuable.  They are not failures.  They are model obstruction cases for the analytic proof.

For each fully blocked case, inspect:

```text
endpoint_count
crossing_interval_count
total_crossing_length
max_cut_multiplicity
unblocked_cuts
```

A difficult obstruction signature would have:

```text
unblocked_cuts = []
high crossing_interval_count
high total_crossing_length
high max_cut_multiplicity
```

## 4. Suggested local runs

After `certificates/minimal_witnesses.jsonl` exists, run:

```bash
python scripts/analyze_insertion_blocks.py \
  --witness-jsonl certificates/minimal_witnesses.jsonl \
  --limit 10000 \
  --jsonl-out logs/insertion_block_sample_10k.jsonl
```

Then inspect worst cases:

```bash
python - <<'PY'
import json
from pathlib import Path
rows = [json.loads(x) for x in Path('logs/insertion_block_sample_10k.jsonl').read_text().splitlines() if x.strip()]
valid = [r for r in rows if r.get('deleted_order_valid')]
print('valid rows:', len(valid))
print('fully blocked:', sum(1 for r in valid if r.get('unblocked_count') == 0))
for key in ['blocked_count','crossing_interval_count','total_crossing_length','max_cut_multiplicity']:
    worst = sorted(valid, key=lambda r: r.get(key, -1), reverse=True)[:10]
    print('\nWORST', key)
    for r in worst:
        print({k:r.get(k) for k in ['p','B','x','blocked_count','unblocked_count','crossing_interval_count','total_crossing_length','max_cut_multiplicity']})
PY
```

## 5. Proof relevance

The analytic target is not merely to find one good insertion for one known witness.  The target is stronger:

```text
In every minimal counterexample A, there exists x in A and a valid ordering C
of A\{x} with at least one unblocked insertion cut.
```

The analyzer helps identify which obstruction patterns actually occur in finite data and which local surgery moves are likely to be useful.

## 6. Next planned extension

A later version should search over multiple valid orderings of `A\{x}` and minimize:

```text
M(C,x) = (
  |Block(C,x)|,
  total_blocking_multiplicity,
  crossing_interval_count,
  total_crossing_length,
  endpoint_obstruction_count
).
```

That would directly test the descent-measure strategy described in:

```text
docs/INSERTION_CUT_COVER_PROGRAM.md
```
