# S33. Universal B z q A tail-core status

This note records the corrected record-level family coverage for the pure worse-only `m=3` terminal residual.

## Inputs

The relevant outputs are:

```text
logs/summary_pure_worse_family_coverage_p17_v2.json
logs/summary_pure_worse_family_coverage_p23_v2.json
```

produced by:

```bash
python3 scripts/summarize_pure_worse_family_coverage.py \
  logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl \
  --pretty \
  --out logs/summary_pure_worse_family_coverage_p17_v2.json

python3 scripts/summarize_pure_worse_family_coverage.py \
  logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl \
  --pretty \
  --out logs/summary_pure_worse_family_coverage_p23_v2.json
```

## Main result

For both p=17 and p=23, the permutation

```text
B z q A
```

has universal meta-family coverage:

```text
B_TAIL_WITH_A_CORE
B_TAIL_ZQ_A_CORE
```

Specifically:

```text
p=17: 35 / 35 pure_worse_only records
p=23: 59 / 59 pure_worse_only records
```

For p=17, the lower-level family is already universal:

```text
B z q A -> B_tail+zq+A
```

For p=23, no single lower-level symbolic family is universal, but the meta-family is universal:

```text
B z q A -> B_TAIL_ZQ_A_CORE
```

This means every pure worse-only residual has a non-tautological zero block of the form:

```text
B_tail + z + q + A + optional exterior terms = 0.
```

## Algebraic reduction

Recall the pure residual normal form:

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) = A1 + A2 = -z.
```

Therefore:

```text
z + A = 0.
```

So a zero block of type

```text
B_tail + z + q + A = 0
```

reduces immediately to:

```text
B_tail + q = 0.
```

If the symbolic block includes a right exterior prefix, then it reduces to:

```text
B_tail + q + Y_prefix = 0.
```

This is the hidden equation the pure worse-only branch exposes.

## Interpretation

The pure worse-only branch is no longer opaque.  It universally implies a tail equation under the single permutation:

```text
B z q A.
```

The branch can now be attacked by proving that a pure terminal residual cannot also contain this hidden tail equation without triggering one of the already-reduced branches:

```text
SIGNED_INTERVAL
DISTRIBUTED_BRIDGE
terminal-tail bridge
right-exterior bridge
```

## Next script

Add:

```text
scripts/extract_bzqa_tail_core_equations.py
```

Input:

```text
logs/analyze_pure_m3_terminal_structure_p17_v2.jsonl
logs/analyze_pure_m3_terminal_structure_p23_v2.jsonl
```

Target output:

```text
1. one B z q A tail-core equation per pure_worse_only record;
2. symbolic block;
3. reduced equation after removing z+A;
4. B_tail start index;
5. B_tail length;
6. Y_prefix length;
7. support-length histogram;
8. reduced-equation family histogram:
   B_tail+q
   B_tail+q+Y_prefix
   mixed_X_or_other
```

## Candidate lemma

Let `R` be a pure worse-only m=3 right-terminal residual.  Then under the move

```text
B z q A
```

there exists a zero block whose reduction by `z+A=0` gives

```text
B_tail + q + Y_prefix = 0
```

with `B_tail` nonempty.

If `Y_prefix` is empty, this is a hidden signed/terminal-tail relation:

```text
B_tail + q = 0.
```

If `Y_prefix` is nonempty, this is a right-exterior bridge and should be reducible by an exterior-bridge route.

## Status

```text
Universal pure worse-only mechanism found:
  B z q A -> B_tail + z + q + A + optional Y_prefix = 0.
Next:
  extract exact reduced tail equations record-by-record.
```
