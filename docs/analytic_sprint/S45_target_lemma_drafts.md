# S45. Target lemma drafts after v2 certificate

This note turns the v2 certificate table into explicit proof targets.

## Certificate table used

The proof-focused certificate is:

```text
logs/pure_worse_certificate_table_v2.md
```

It records the current branch split:

| family | status |
| --- | --- |
| `B_tail+q` | zero-sum classified by `Bq_zero` |
| `B_tail+q+Y_prefix` | zero-sum classified by `BqY_zero` |
| `B_tail+q=A_complement` | equality tie-break needed |
| `B_prefix=q` | equality tie-break needed |

The target coverage is complete in the observed certificate:

```text
p=17:
  B_tail+q              -> Bq_zero   23/23
  B_tail+q+Y_prefix     -> BqY_zero   8/8
  equality branches     -> neutral    4/4

p=23:
  B_tail+q              -> Bq_zero   20/20
  B_tail+q+Y_prefix     -> BqY_zero  32/32
  equality branches     -> neutral    7/7
```

## Lemma 1. Hidden-support extraction lemma

### Statement

Let

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0,
D_short(R) = (1,3,1,[2]).
```

Assume `R` lies in the pure worse-only `m=3` right-terminal branch. Under the permutation

```text
A z q B -> B z q A,
```

the new order contains a non-tautological zero interval that reduces to exactly one of:

```text
1. B_tail + q = 0,
2. B_tail + q + Y_prefix = 0,
3. B_tail + q = A_complement,
4. B_prefix = q.
```

### Proof idea

The permutation `B z q A` preserves the two tautological terminal relations in rearranged form, but because the branch is pure worse-only, it must introduce at least one additional collision. The interval endpoints in `B z q A` force any non-tautological interval crossing the central `z q` boundary to be one of:

```text
B_tail + z + q + A1 + A2 + Y_prefix = 0,
B_tail + z + q + A_i + Y_prefix = 0,
B_tail + z + q = 0.
```

These reduce respectively to:

```text
B_tail + q + Y_prefix = 0,
B_tail + q + Y_prefix = A_complement,
B_prefix = q.
```

### Remaining formal gap

The empirical certificate proves this for the sampled records. The formal proof still needs an endpoint-exclusion argument showing that all other non-tautological interval shapes are impossible in a pure worse-only minimal residual.

Required subclaims:

```text
1. Intervals wholly inside A,z or B,z are tautological and already accounted for.
2. Intervals wholly inside X or Y would be external collisions, contradicting the pure branch.
3. Intervals crossing X into the active window route to the external-bridge branch.
4. Intervals crossing only A/B without zq route to the signed/distributed branch.
5. Therefore a genuinely new pure-worse collision under B z q A must cross zq and has one of the listed tail-core forms.
```

## Lemma 2. Zero-sum Bq/BqY secondary-obstruction lemma

### Statement

Under the hypotheses of Lemma 1, suppose the hidden support equation is zero-sum:

```text
B_tail + q = 0
```

or

```text
B_tail + q + Y_prefix = 0.
```

Then every best bridge realization of that hidden equation either gives a descent in `D_short` or exposes a genuine secondary obstruction of the corresponding type:

```text
B_tail + q = 0              -> Bq_zero,
B_tail + q + Y_prefix = 0   -> BqY_zero.
```

### Certificate support

```text
B_tail+q -> Bq_zero:
  p=17: 23/23
  p=23: 20/20

B_tail+q+Y_prefix -> BqY_zero:
  p=17:  8/8
  p=23: 32/32
```

### Proof idea

A bridge realization attempts to make the hidden zero-sum block contiguous:

```text
q B_tail
```

or

```text
q B_tail Y_prefix.
```

If this does not decrease `D_short`, the newly created zero interval persists as a short collision. After removing expected intervals:

```text
A1 A2 z,
B z,
q B_tail (+Y_prefix),
```

the best failed bridge move still contains a genuine shortest zero interval involving `q` and a support/exterior block.

### Remaining formal gap

The empirical certificate identifies the secondary interval, but the formal proof must show that this interval is structurally forced. A possible route is to track partial sums before and after moving the `q`-tail block.

Required subclaims:

```text
1. The hidden zero-sum block creates a repeated partial sum pair after the bridge move.
2. If this repeated pair is not a descent, the multiplicity pattern forces an additional repeated pair sharing q.
3. That additional repeated pair corresponds to Bq_zero or BqY_zero.
4. The secondary obstruction is not tautological and is not the original terminal block.
```

## Lemma 3. Bq/BqY obstruction routing lemma

### Statement

A genuine secondary obstruction of type

```text
Bq_zero
```

or

```text
BqY_zero
```

routes to an earlier known branch or defines a new reducible branch.

Candidate routing targets:

```text
SIGNED_INTERVAL,
EXTERNAL_BRIDGE,
DISTRIBUTED_BRIDGE,
PAIR_TRAP,
support-tail trap.
```

### Proof idea

The obstruction has the same algebraic signature as a support-tail bridge involving the separator `q`. It should be incompatible with pure terminal minimality unless it is already classified as a signed or exterior bridge.

### Remaining formal gap

This is now the most important mathematical gap. It requires either:

```text
A. identify Bq/BqY as an existing branch in earlier classifiers;
```

or:

```text
B. promote Bq/BqY to a named branch lemma with its own descent/tie-break.
```

## Lemma 4. Equality branch tie-break lemma

### Statement

If the hidden support equation is an equality type,

```text
B_tail + q = A_complement
```

or

```text
B_prefix = q,
```

then the tested bridge moves preserve `D_short` but should decrease a refined tie-break rank.

Observed certificate:

```text
p=17:
  B_tail+q=A_complement -> neutral 4/4

p=23:
  B_tail+q=A_complement -> neutral 5/5
  B_prefix=q            -> neutral 2/2
```

### Candidate refined defect

Define

```text
D_ref = (D_short, T_pos, C_rank, S_rank),
```

where:

```text
T_pos  = terminal position rank of the unique length-3 zero interval,
C_rank = cyclic rank of the ordered triple (A1,A2,z),
S_rank = support-rank measuring q relative to B_prefix/B_tail.
```

For a right-terminal residual, `T_pos` should prefer rightward motion of the unique zero triple. For equality branches where `T_pos` is unchanged, use `C_rank` or `S_rank`.

### Remaining formal gap

Need to define `S_rank` precisely. Two candidates:

```text
S_rank_1 = length of B_prefix needed to equal q;
S_rank_2 = lexicographic position of q relative to the shortest prefix/tail relation.
```

The equality branch data should be rechecked under both ranks.

## Recommended next proof action

The next highest-value mathematical target is Lemma 3:

```text
Bq/BqY obstruction routing lemma.
```

The equality tie-break branch is small and isolated. The zero-sum branch is larger and already fully classified; routing `Bq_zero` and `BqY_zero` would likely close the largest remaining pure worse-only subcase.

## Status

```text
The proof task has been narrowed from broad search to four explicit lemmas.
The largest remaining gap is routing Bq/BqY secondary obstructions.
```
