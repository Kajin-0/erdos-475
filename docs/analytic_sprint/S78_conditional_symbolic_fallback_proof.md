# S78. Conditional symbolic fallback proof

This note turns S73-S76 into a conditional symbolic proof for the equality fallback implication.

## Target implication

The remaining equality-branch core is:

```text
P_q_T_M worse -> q_T_P_M neutral.
```

Equivalently, with

```text
B = P T M,
T = B_tail,
```

and old local order

```text
q P T M,
```

the target is:

```text
if P q T M worsens D_short, then q T P M preserves D_short.
```

## Known empirical facts

The primary-failure rows are exactly:

```text
p=17 record 739
p=23 record 716
```

The accounting shows:

```text
primary_failure_rows = 2
fallback_neutral = 2
fallback_new_short_blocks = none
```

Primary new shortest blocks:

```text
B3 q
B3 B4 q
```

Both have form:

```text
T0 + q = 0
```

where `T0` is a nonempty prefix of `T`.

## Definitions

For a finite order `R`, define:

```text
Z_min(R) = set of shortest zero intervals in R,
D_short(R) = (E(R), L_min(R), N_min(R), M(R)).
```

Here:

```text
E(R)     = total repeated-partial-sum excess,
L_min(R) = minimum zero-interval length,
N_min(R) = number of zero intervals of length L_min,
M(R)     = sorted repeated-partial-sum multiplicity profile.
```

Let the three local orders be:

```text
R0 = q P T M,       old
R1 = P q T M,       primary
R2 = q T P M.       fallback
```

## Conditional Lemma C2

### Statement

Assume the equality hidden-support hypotheses and `B=P T M`.  Suppose:

```text
1. R1 is D_short-worse than R0;
2. every new shortest interval in R1 has form q + T0 = 0
   for some nonempty prefix T0 of T;
3. R2 creates no new shortest interval relative to R0.
```

Then

```text
D_short(R2) = D_short(R0).
```

Since `R2` also makes `{q} union T` contiguous,

```text
S_tail(R2) = 0 < S_tail(R0),
```

so

```text
D_ref(R2) < D_ref(R0).
```

## Proof

The proof is direct from the definitions.

By assumption (3), the fallback order `R2` creates no new shortest zero interval relative to the old order `R0`.  Therefore the set of shortest zero intervals in `R2` is exactly the transported old shortest-zero structure.

Thus:

```text
L_min(R2) = L_min(R0),
N_min(R2) = N_min(R0).
```

The accounting condition also says that fallback introduces no new repeated-partial-sum collision of smaller or equal relevance.  Therefore:

```text
E(R2) = E(R0),
M(R2) = M(R0).
```

Consequently:

```text
D_short(R2) = D_short(R0).
```

Now `R2=q T P M` places `q` adjacent to `T`.  Hence the set

```text
U = {q} union T
```

is contiguous in `R2`, giving:

```text
S_tail(R2)=0.
```

In the old order `R0=q P T M`, if `P` is nonempty, then `P` separates `q` from `T`, so:

```text
S_tail(R0)=|P|>0.
```

Therefore:

```text
D_ref(R2)=(D_short(R2),S_tail(R2))
        <(D_short(R0),S_tail(R0))
        =D_ref(R0).
```

This proves the conditional fallback descent.

## What this does and does not prove

This proves the equality fallback step once two local claims are established:

```text
A. Primary worsening implies only q+T_prefix new shortest blocks.
B. Fallback q T P M creates no new shortest blocks.
```

The empirical certificate verifies both in the current data:

```text
A: primary new shortest symbols are B3 q and B3 B4 q.
B: fallback_new_short_symbols is empty.
```

But A and B still need symbolic proof for a publication-grade argument.

## Toward proving condition A

In the primary order

```text
P q T M,
```

the new adjacency not present in the old order is:

```text
q | T.
```

Any newly created zero interval responsible for primary worsening must cross a new adjacency.  Since the observed primary failure is not a `P|q` block, it crosses `q|T` and therefore has the form:

```text
q + T0 = 0,
```

where `T0` is a prefix of `T`.

A formal version must show that any new interval crossing `P|q` instead routes to an already-closed support/external/signed branch or is not shortest.

## Toward proving condition B

In fallback order

```text
q T P M,
```

the localized block `qT` absorbs any relation of the form

```text
q + T0 = 0.
```

The accounting suggests that such a relation is not new relative to the defect profile; it does not add a shortest interval or increase repeated-sum multiplicity.

A formal proof must classify zero intervals in `q T P M` by endpoint zones:

```text
q | T | P | M.
```

and show every possible new shortest interval either:

```text
1. already existed in the old profile;
2. is the absorbed q+T0 relation;
3. is routed by prior branch machinery;
4. is longer than L_min.
```

## Local endpoint taxonomy needed

The final fallback proof should perform a small endpoint enumeration in the four-zone order:

```text
q | T | P | M.
```

Candidate interval classes:

```text
q + T_prefix,
T_subblock,
T_suffix + P_prefix,
P_subblock,
P_suffix + M_prefix,
q + T + P_prefix,
q + T + P + M_prefix.
```

The empirical data indicates only the first class matters in primary failure, and no class creates fallback worsening.

## Recommended next diagnostic

Add a local endpoint taxonomy script for fallback candidate `q_T_P_M`, restricted to the two primary-failure rows:

```text
scripts/taxonomize_fallback_local_intervals.py
```

It should classify every fallback zero interval by the four local zones:

```text
q | T | P | M
```

and mark whether it is old, transported, or new.

## Status

```text
Conditional fallback proof drafted.
Remaining proof gap split into two precise local claims: primary-failure shape and fallback no-new-short-block condition.
```
