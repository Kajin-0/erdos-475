# S77. Pure worse-only reduction theorem skeleton

This note consolidates S50-S76 into a single theorem-level proof skeleton for the pure worse-only `m=3` right-terminal branch.

## Theorem. Pure worse-only `m=3` branch reduction

### Informal statement

Let

```text
R = X A z q B Y
```

be a pure worse-only `m=3` right-terminal residual in `Z/pZ`, with

```text
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0,
D_short(R) = (1,3,1,[2]).
```

Then `R` is not a terminal obstruction.  It reduces by one of the following mechanisms:

```text
1. zero-sum hidden support routes to existing branch machinery;
2. equality hidden support decreases the refined support-localization rank.
```

Therefore the branch descends under a refined defect order.

## Refined defect

Use

```text
D_ref(R) = (D_short(R), S_tail(R))
```

where `S_tail` is only needed in equality branches:

```text
S_tail(R) = span_gap_R({q} union B_tail).
```

Here

```text
span_gap_R(U) = max_position_R(U) - min_position_R(U) + 1 - |U|.
```

The order is lexicographic:

```text
D_ref(R') < D_ref(R)
```

if either:

```text
D_short(R') < D_short(R),
```

or:

```text
D_short(R') = D_short(R)
and
S_tail(R') < S_tail(R).
```

## Proof skeleton

### Step 1. Hidden-support extraction

Apply the local permutation

```text
A z q B -> B z q A.
```

By Lemma A, assembled in S61, the moved order exposes one of four reduced hidden-support families:

```text
B_tail + q = 0,
B_tail + q + Y_prefix = 0,
B_tail + q = A_complement,
B_prefix = q.
```

This extraction follows from endpoint-zone enumeration in

```text
X | B | z | q | A | Y
```

plus the endpoint-exclusion sublemmas:

```text
E1. Proper sub-terminal support interval exclusion.
E2. Exterior crossing interval routes to external bridge.
E3. Local q/A or A/B zero interval routes to signed/distributed branch.
E4. Pure worse-only excludes already-routed branches.
```

The empirical endpoint-taxonomy certificate supports:

```text
p=17: target hidden-support present in 35/35 records.
p=23: target hidden-support present in 59/59 records.
```

### Step 2. Zero-sum branch routing

If the extracted family is

```text
B_tail + q = 0,
```

then it is a `Bq_zero` obstruction and routes through existing branch machinery.

Certified coverage:

```text
p=17: 23/23 target, 23/23 routed.
p=23: 20/20 target, 20/20 routed.
```

If the extracted family is

```text
B_tail + q + Y_prefix = 0,
```

then it is a `BqY_zero` obstruction and routes through existing branch machinery.

Certified coverage:

```text
p=17: 8/8 target, 8/8 routed.
p=23: 32/32 target, 32/32 routed.
```

The route labels are among:

```text
CLEAN_DESCENT,
SIGNED_INTERVAL,
EXTERNAL_BRIDGE,
DISTRIBUTED_BRIDGE,
LEFT_TERMINAL_BRIDGE,
RIGHT_TERMINAL_BRIDGE,
SHORT_TERMINAL_BRIDGE,
LONG_TERMINAL_BRIDGE.
```

Thus the zero-sum branch is not primitive.

### Step 3. Equality branch tie-break

If the extracted family is

```text
B_tail + q = A_complement,
```

or

```text
B_prefix = q,
```

write

```text
B = P T M,
T = B_tail.
```

The old local order is

```text
A z q P T M.
```

Use the primary/fallback localization rule from S72:

```text
Primary:  A z q P T M -> A z P q T M
Fallback: A z q P T M -> A z q T P M
```

Both moves place `q` adjacent to `T`, so

```text
S_tail(new) = 0.
```

Since old order has `P` separating `q` from `T`,

```text
S_tail(old) = |P| > 0.
```

Therefore any `D_short`-neutral localization gives

```text
D_ref(new) < D_ref(old).
```

The fallback implication verified in S71 and sharpened in S75 is:

```text
Primary worse -> Fallback neutral and no new shortest blocks.
```

Certified evidence:

```text
p=17:
  equality records = 4
  primary worse = 1
  fallback rescues = 1
  failures = 0

p=23:
  equality records = 7
  primary worse = 1
  fallback rescues = 1
  failures = 0
```

Thus every equality record has a refined descent.

### Step 4. Combine cases

Every pure worse-only residual enters exactly one extracted family.

The zero-sum families route to already-closed branch machinery.

The equality families descend by

```text
D_ref = (D_short, S_tail).
```

Therefore the pure worse-only `m=3` right-terminal branch is reduced.

## Final certificate table

The v4 certificate table was:

```text
| p | family | records | mode | verified_total | best_bridge_class | target | target_coverage | route_coverage | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 17 | B_tail+q | 23 | zero_sum | 35/35 | worse:23 | Bq_zero | 23/23 | 23/23 | zero_sum_routed |
| 17 | B_tail+q+Y_prefix | 8 | zero_sum | 35/35 | worse:8 | BqY_zero | 8/8 | 8/8 | zero_sum_routed |
| 17 | B_tail+q=A_complement | 4 | equality | 35/35 | neutral:4 | q_tail_span_gap | 4/4 | not_applicable | equality_tiebroken |
| 23 | B_tail+q | 20 | zero_sum | 59/59 | worse:20 | Bq_zero | 20/20 | 20/20 | zero_sum_routed |
| 23 | B_tail+q+Y_prefix | 32 | zero_sum | 59/59 | worse:32 | BqY_zero | 32/32 | 32/32 | zero_sum_routed |
| 23 | B_tail+q=A_complement | 5 | equality | 59/59 | neutral:5 | q_tail_span_gap | 5/5 | not_applicable | equality_tiebroken |
| 23 | B_prefix=q | 2 | equality | 59/59 | neutral:2 | q_tail_span_gap | 2/2 | not_applicable | equality_tiebroken |
```

This table is the empirical certificate for the theorem skeleton.

## Formal dependencies still requiring proof

The theorem skeleton is not a completed publication proof.  The remaining formal dependencies are:

```text
A. Hidden-support extraction endpoint enumeration.
B. Zero-sum Bq/BqY routing lemma.
C. Equality fallback implication.
```

### Dependency A

Mostly drafted in S55-S61.  Remaining work:

```text
1. define pure worse-only rigorously;
2. define support-minimality rigorously;
3. convert E2/E3 route vocabulary into formal partial-sum lemmas.
```

### Dependency B

Empirically closed by route tables.  Remaining work:

```text
prove Bq_zero/BqY_zero force one of the existing route labels.
```

### Dependency C

Reduced to the local block claim in S76:

```text
If P q T M is worse because it creates q + T_prefix = 0,
then q T P M is neutral and creates no new shortest block.
```

This is the sharpest remaining equality-branch gap.

## Recommended next target

The best next formal target is Dependency C because it is now local and finite:

```text
Blocks: q, P, T, M.
Claim: primary failure forces q+T_prefix, and fallback has no new shortest block.
```

After C, the equality branch becomes fully proof-ready.  Then the remaining heavy work is the zero-sum routing lemma.

## Status

```text
Pure worse-only m=3 right-terminal branch has a coherent theorem-level skeleton.
All empirical branches are closed.
Remaining work is formalizing three named dependencies, with equality fallback as the narrowest target.
```
