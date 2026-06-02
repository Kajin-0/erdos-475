# Analytic Checkpoint: F10/F11 Weighted-Core Closure

This checkpoint audits the current status of the weighted-core branch after the recent F6/F7/F8/F9 hardening work.

Claim boundary:

```text
This file is not a proof of Erdős 475.
It is a weighted-core proof-status checkpoint.
It records what is closed, what is conditional, and what remains a theorem blocker.
```

---

## Why this checkpoint exists

The global proof currently depends on the following interface:

```text
F9 non-weighted termination delegates genuine weighted-core exits to F10/F11.
F11 weighted-core termination delegates routed non-weighted exits back to F9.
```

This is acceptable only if the final proof is written as a well-founded mutual induction or as a single combined-measure theorem.

Otherwise, the F9/F11 interface is circular.

This checkpoint makes that explicit.

---

## Source files

Weighted final drafts:

```text
docs/final/F10_weighted_normal_form_cut_swap.md
docs/final/F11_weighted_cut_selection_extraction.md
```

Core A-note chain:

```text
docs/analytic_internal_cyclic_self_return_hardening_a89.md
docs/analytic_cut_rigid_to_strong_exact_a90.md
docs/analytic_first_changed_endpoint_a91.md
docs/analytic_finite_return_path_formalization_a92.md
docs/analytic_state_machine_coverage_a93.md
docs/analytic_strict_progress_endpoint_change_a94.md
docs/analytic_weighted_cut_swap_table_hardening_a97.md
docs/analytic_bridge_gap_measure_hardening_a98.md
```

Recent global hardening:

```text
docs/final/F06_external_collision_theorem.md
docs/final/F07_recurrence_routing_theorem.md
docs/final/F08_bridge_gap_descent_theorem.md
docs/final/F09_nonweighted_termination_theorem.md
docs/analytic_mbg_to_mnw_subrank_convention.md
```

---

## Weighted branch setup

A weighted core has displayed form:

```text
A + 2B + C = 0.
```

It is genuine if the easy reductions fail:

```text
B != 0,
A+B != 0,
B+C != 0,
A != C,
no transported-prefix/tail rewrite applies.
```

F10 handles a chosen proper cut:

```text
B = P R,
A P R C -> A R P C.
```

F11 must prove that either:

```text
1. the weighted branch exits to non-weighted machinery;
2. succeeds;
3. collapses;
4. or returns to a weighted core with strictly smaller |B|.
```

---

## What is substantially hardened

### H1. Strong exact self-return impossibility

A89 proves:

```text
strong exact internal cyclic self-return -> impossible in a genuine weighted core.
```

Key logic:

```text
strong exact return -> E_B - T_k = E_B;
T_k != 0 -> E_B = F_p;
E_B = F_p -> |B| = p-1;
|B| = p-1 -> A=C=empty;
A+2B+C=0 -> 2B=0 -> B=0 in odd characteristic;
contradiction to genuine weighted core.
```

Status:

```text
Closed under the strong exact-pattern hypothesis.
```

Important limitation:

```text
A89 does not prove weak cut-rigid return -> strong exact return.
```

---

### H2. Weak-to-pattern reduction

A90 shows weak cut-rigidity alone is insufficient, then introduces pattern-rigidity.

A90 reduces the problem to:

```text
same outer blocks + same middle support + changed internal endpoint set
  -> internal non-weighted obstruction or smaller weighted core.
```

A91 supplies the first-changed-endpoint analysis.

A92 supplies the finite return-path state-machine model.

A93 supplies the transition coverage table.

A94 supplies the strict-progress/minimal-self-return principle.

Status:

```text
Conceptually routed, but still proof-architecture-sensitive.
```

The final proof must define the self-return path and minimality convention carefully enough that A94's remove-change/undo argument is legal.

---

### H3. Weighted cut-swap displayed collision table

A97 hardens the A60 cut-swap table for:

```text
A P R C -> A R P C.
```

The moved endpoint families are:

```text
R_k' = x+a+R_k,
P_j' = x+a+r+P_j.
```

A97 classifies displayed collisions into:

```text
zero-composite,
two-piece zero,
equal/separated interval,
signed interval / transported-prefix candidate,
weighted-core return through signed boundary relation,
forbidden recurrence,
endpoint zero-collapse.
```

A97 also isolates the only weighted-return channel:

```text
signed boundary relation comparing moved P/R data.
```

Status:

```text
Table architecture hardened.
Final proof still needs a compact endpoint table and sign convention check for the signed boundary relation.
```

---

### H4. External, recurrence, and bridge dependencies

Older A94/F11 risks included:

```text
A62 external collision,
A64 recurrence bounded-blocker measure,
A74--A77 bridge/gap inequalities.
```

Recent final drafts and checkpoints substantially harden these:

```text
F6 / A95: external collision class routing;
F7 / A64--A71: recurrence routing, with H1/H2, pair, singleton, cyclic audits;
F8 / A98: bridge/gap class routing and measure convention;
F9: global non-weighted measure framework.
```

Status:

```text
Class-routed and mostly hardened, but final edge-by-edge F9 rank table still required.
```

---

## Current weighted-core blocker map

| Blocker | Description | Current status | Severity |
|---|---|---|---|
| W1 | F9/F11 mutual dependency | not yet formalized as mutual induction | RED |
| W2 | A81 atom-middle sign-pattern algebra | not recently audited | ORANGE/RED |
| W3 | A56 transported-prefix/tail exhaustiveness | still a key F10 risk | ORANGE |
| W4 | A97 signed boundary channel sign/endpoints | table exists, final sign audit needed | ORANGE |
| W5 | A94 minimal self-return progress principle | conceptually proved, needs final formalization | ORANGE |
| W6 | F9 final edge-by-edge rank table | not complete | ORANGE |
| W7 | Tiered exits from F10/F11 to F6--F9 | class-routed, needs exact final cross-references | YELLOW/ORANGE |

---

## Most important structural issue: F9/F11 circularity

F9 currently says:

```text
Non-weighted paths terminate if weighted exits terminate by F11.
```

F11 currently says:

```text
Weighted paths terminate if routed non-weighted exits terminate by F9.
```

This is not automatically invalid, but it must be made non-circular.

### Required final formulation

Use a combined global measure such as:

```text
M_total = (
  weighted_flag_or_middle_length,
  M_NW^*,
  return_path_depth,
  local_subrank
).
```

Better:

```text
M_total = (
  weighted_middle_length_or_infinity_class,
  phase_rank,
  M_NW^*,
  return_path_depth
).
```

But the final proof must be precise.

A clean option is mutual induction:

```text
Induct on |B| for weighted cores.
For fixed |B|, non-weighted exits terminate by F9 restricted to weighted exits of smaller |B| or terminal exits.
```

The key rule must be:

```text
A non-weighted path may enter WEIGHTED_CORE only if the weighted branch either:
  1. exits terminally;
  2. returns to non-weighted with strictly smaller M_NW^*;
  3. or returns to weighted with strictly smaller |B|.
```

If a weighted branch exits to non-weighted at the same `M_NW^*` and can later re-enter a weighted core with the same `|B|`, the proof is circular.

This exact edge must be audited.

---

## Weighted branch progress theorem needed

The final F11 theorem should prove the stronger statement:

```text
Starting from a genuine weighted core with middle length m,
every branch either:
  - succeeds;
  - collapses;
  - exits to a non-weighted obstruction with strictly smaller global measure;
  - exits to a non-weighted obstruction that cannot re-enter a weighted core of length >= m;
  - or returns to a genuine weighted core with middle length < m.
```

Current F11 proves a weaker routed statement:

```text
weighted exits to non-weighted machinery handled by F9.
```

That is insufficient unless F9/F11 are jointly ordered.

---

## Atom-middle risk W2

F11 atom-middle base case depends on A80--A81.

The draft compresses endpoint-rigid traps to boundary atom relations such as:

```text
q-alpha=a,
gamma-q=c,
alpha-gamma=2q.
```

Risk:

```text
A81 sign-pattern algebra must be audited line by line.
Endpoint-empty cases A=empty or C=empty must be explicit.
```

This is a finite algebra table and is probably tractable.

Recommended next local task:

```text
Create docs/analytic_weighted_atom_middle_a81_audit.md
```

---

## Transported-prefix risk W3

F10 and F11 both depend on A56 easy reductions.

Current easy reductions:

```text
B=0,
A+B=0,
B+C=0,
A=C,
transported-prefix/tail rewrite.
```

Risk:

```text
The transported-prefix/tail hypotheses must be stated explicitly and proven exhaustive.
```

Recommended task:

```text
Audit A56 and extract exact transported-prefix/tail conditions.
```

---

## Signed boundary channel W4

A97 shows the only displayed weighted return comes through signed cut-boundary relations, especially:

```text
r + P_j - p - R_k = 0.
```

Risk:

```text
Need final sign/endpoints audit proving this either:
  1. is A56 reducible;
  2. routes to nonweighted signed/equal/pair machinery;
  3. or returns with smaller weighted middle;
  4. or is the weak cut-rigid case handled by A90--A94.
```

This is probably the highest-value weighted algebra audit after atom-middle.

---

## Current weighted closure status

The weighted branch is no longer a completely broad unknown. It is concentrated into:

```text
1. non-circular F9/F11 mutual induction;
2. A81 atom-middle sign/endpoint table;
3. A56 transported-prefix/tail exhaustiveness;
4. A97 signed boundary return channel;
5. final edge-by-edge rank table for exits.
```

---

## Recommended next steps

Do not continue adding broad weighted overview notes after this checkpoint.

Next analytic actions should be concrete:

```text
1. Create A81 atom-middle sign-pattern audit.
2. Create A97 signed-boundary channel audit.
3. Create F9/F11 mutual-induction convention note.
4. Patch F11 to replace stale broad risks with the exact W1--W7 blocker map.
```

---

## One-line status

```text
F10/F11 are not closed, but the weighted bottleneck is now sharply localized.
The most serious issue is the non-circular F9/F11 induction interface.
```
