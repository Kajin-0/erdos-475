# F3 obstruction state machine and transition classes

This file continues the final-proof extraction phase.

F3 extracts the state-machine framework used by the final proof.  It is mainly backed by:

```text
A72  obstruction dependency graph
A78  non-weighted obstruction measure
A87  local lemma audit checklist
A88  formal dependency table
A92  finite return-path formalization
A93  state-machine coverage table
A94  strict progress lemma
A99  augmented recurrence span convention
```

F3 is used by:

```text
F4  local descent theorem
F5  separated-equal/midpoint routing
F6  external collision theorem
F7  recurrence routing theorem
F8  bridge/gap descent theorem
F9  non-weighted termination theorem
F10 weighted normal form and cut-swap theorem
F11 weighted cut-selection theorem
F12 endpoint avoidance theorem
```

This is an extracted draft, not yet the final manuscript version.

---

## F3.1. Obstruction state

An obstruction state is a tuple

```text
Omega=(R,I,C,E,M,tag)
```

where:

```text
R    = current ordering of the same subset S subset F_p^*;
I    = active displayed interval/window in R;
C    = obstruction class;
E    = endpoint/block data attached to I;
M    = active measure tuple;
tag  = provenance label recording how the state was produced.
```

The endpoint/block data `E` includes, as needed:

```text
basepoint before the active window;
left and right boundary endpoints;
internal partial-sum list;
internal endpoint set;
forbidden-hit index;
A5 blocker index;
block decomposition labels;
block sums;
next atom after a recurrent hit;
external bridge data.
```

---

## F3.2. Obstruction classes

The obstruction class `C` belongs to the following universe:

```text
SUCCESS,
CONTRADICTION,
ZERO_COLLAPSE,
PREFIX_ZERO,
TWO_PIECE_ZERO,
THREE_PIECE_ZERO,
HIGHER_ZERO_COMPOSITE,
ZERO_COMPOSITE_SURGERY,
EQUAL_INTERVAL,
SIGNED_INTERVAL,
SEPARATED_EQUAL,
MIDPOINT,
PAIR_DIFFERENCE,
TRANSPORTED_PREFIX,
WEIGHTED_CORE,
SINGLETON_RECURRENCE,
CYCLIC_RECURRENCE,
FORBIDDEN_RECURRENCE,
EXTERNAL_COLLISION,
BRIDGE_GAP.
```

Some labels are bookkeeping labels rather than final theorem statements.  In the final manuscript, they may be grouped as:

```text
local interval classes:        ZERO, EQUAL, SIGNED, PAIR;
separated classes:            SEPARATED_EQUAL, MIDPOINT, BRIDGE_GAP;
recurrence classes:           SINGLETON, CYCLIC, FORBIDDEN;
weighted class:               WEIGHTED_CORE;
terminal classes:             SUCCESS, CONTRADICTION.
```

---

## F3.3. Terminal states

A state is terminal-success if the current ordering `R` is Graham-valid and avoids the forbidden value `f`.

A state is terminal-contradiction if it forces one of:

```text
nonempty zero interval;
zero atom;
repeated partial sums in a claimed Graham-valid ordering;
earlier forbidden hit than the chosen minimal hit;
violation of subset/distinct-atom assumptions;
forbidden final endpoint despite f != sigma(S).
```

---

## F3.4. Non-weighted measure

Use the non-weighted measure

```text
M_NW^* = (
  enclosing_span,
  gap_length,
  support_size,
  recurrence_depth,
  pair_depth,
  separated_depth,
  bridge_depth,
  type_rank,
  boundary_rank,
  h_excess
).
```

All coordinates are nonnegative integers.

Definitions:

```text
enclosing_span   = length of the smallest atom interval containing active support;
gap_length       = separated/bridge gap length when present, otherwise 0;
support_size     = number of participating atoms;
recurrence_depth = consecutive recurrence returns since last strict descent;
pair_depth       = consecutive pair-difference routings since last local descent;
separated_depth  = consecutive separated-equal routings since last gap/span descent;
bridge_depth     = consecutive bridge returns since last bridge/gap descent;
type_rank        = finite rank of obstruction class;
boundary_rank    = finite rank of endpoint degeneracy;
h_excess         = recurrent hit index minus the globally minimal first-hit index.
```

The order is lexicographic.

Important convention:

```text
h_excess is last.
```

Minimality forbids an earlier forbidden hit, but later hits do not dominate the geometric descent coordinates.

---

## F3.5. Weighted measure

For weighted states, use

```text
M_W=(|B|,M_NW^*)
```

where `B` is the doubled middle block in the weighted core

```text
A+2B+C=0.
```

The leading coordinate `|B|` is a positive integer.  Weighted induction in F11 uses strict decrease of this coordinate.

---

## F3.6. Transition types

Every nonterminal state transition in the final proof must be one of the following.

### T1. Adjacent swap

Swap adjacent atoms or adjacent local blocks:

```text
L M -> M L.
```

Used by adjacent blocker arguments, pair swaps, atom-middle swaps, and local exchange moves.

### T2. Block exchange

Exchange two displayed blocks, usually equal or signed-related:

```text
B G U -> U G B.
```

Used by separated-equal direct exchange.

### T3. Gap-after move

Move a separating gap after equal blocks:

```text
B G U -> B U G.
```

Used by separated-equal gap reduction.

### T4. Weighted cut-swap

For a weighted core with `B=P R`, apply

```text
A P R C -> A R P C.
```

Used by F10/F11.

### T5. Cyclic cut

Rotate an active block or ordering around a cut endpoint:

```text
P R -> R P.
```

Used by cyclic recurrence and internal cyclic self-return arguments.

### T6. Atom-insertion normalization

Move an atom into or out of a zero-composite or atom-insertion window:

```text
P Q q -> P q Q
```

or the reverse orientation.

Used by H1/H2 recurrence routing.

### T7. A5 blocker pullback

At a recurrent forbidden hit, apply the blocker equation

```text
S'_{H-1}+z=S'_j
```

and pull it back to the pre-move ordering.

Used by all recurrence routing.

### T8. External collision pullback

If a transformed moved endpoint collides with an endpoint outside the displayed table, pull the collision back to bridge/external interval data.

Used by F6.

### T9. Normal-form rewrite

Rewrite an algebraic obstruction without changing the ordering, such as:

```text
transported-prefix -> zero-composite;
weighted easy reduction -> non-weighted class;
proper-overlap equal interval -> smaller equal interval;
proper-containment equal interval -> zero-composite;
midpoint relation -> adjacent equal branch.
```

---

## F3.7. Transition outcome trichotomy

For an ordering-changing transition, exactly one of the following occurs:

```text
1. the transformed ordering is Graham-valid and avoids f;
2. the transformed ordering is not Graham-valid;
3. the transformed ordering is Graham-valid but recurrent, i.e. hits f.
```

These correspond to:

```text
SUCCESS,
COLLISION,
RECURRENCE.
```

Non-ordering-changing transitions are normal-form rewrites and must either:

```text
1. strictly decrease the active measure;
2. lower the finite type/boundary rank;
3. enter a named terminating subroutine;
4. enter the weighted branch with smaller |B|;
5. reach success or contradiction.
```

---

## F3.8. Finite return path

A finite return path is a sequence

```text
Omega_0 -> Omega_1 -> ... -> Omega_N
```

where every arrow is one of the transition types T1--T9.

A weighted self-return is a finite return path with

```text
Omega_0.C = WEIGHTED_CORE,
Omega_N.C = WEIGHTED_CORE.
```

It is non-descending if the returned weighted middle length is not smaller than the original middle length.

---

## F3.9. First changed endpoint principle

Let a finite return path preserve the same outer blocks and same middle support `B`, but change the internal endpoint set of `B`.

Define

```text
s_* = min{s : E_B(Omega_s) != E_B(Omega_0)}.
```

The first changed endpoint occurs in a single transition T1--T9.

If that transition is obstructed, it creates a named obstruction class.  If it is unobstructed, then in a minimal non-descending self-return path it gives a shorter return path or progress, contradicting minimality.

This is the state-machine form of the A91--A94 first-changed-endpoint machinery.

---

## F3.10. State-machine coverage theorem

## Theorem F3.1: all final routing steps fit the obstruction state machine

Every local routing operation used in F4--F11 is one of the transition types T1--T9.

### Proof

The coverage is as follows:

```text
adjacent swaps                 -> T1;
separated direct exchange      -> T2;
gap-after moves                -> T3;
weighted proper cut swaps      -> T4;
cyclic rotations               -> T5;
atom-insertion normalizations  -> T6;
recurrent blocker pullbacks    -> T7;
external collisions            -> T8;
algebraic normal-form rewrites -> T9.
```

These categories exhaust the local moves used in the extracted final lemmas F4--F11. ∎

---

## F3.11. Measure discipline theorem

## Theorem F3.2: every nonterminal transition must descend or enter a named branch

In the final proof, every nonterminal state transition must satisfy one of:

```text
1. it reaches terminal success;
2. it reaches terminal contradiction;
3. it strictly decreases M_NW^*;
4. it enters a named branch F4--F8;
5. it enters the weighted branch F10--F11;
6. it strictly decreases |B| inside the weighted branch.
```

### Proof

This is not an independent algebraic theorem; it is the organizing rule enforced by the extracted lemmas.  F4 handles local zero/equal/pair branches.  F5 handles separated-equal/midpoint branches.  F6 handles external collisions.  F7 handles recurrence.  F8 handles bridge/gap returns.  F10 handles fixed weighted cut-swaps.  F11 handles weighted cut-selection and weighted termination. ∎

---

## F3.12. Interface with F9

F9 will use F3 as follows:

```text
1. every obstruction state belongs to the F3 class universe;
2. every transition belongs to T1--T9;
3. every transition either descends, exits to a named branch, enters weighted induction, or terminates;
4. the non-weighted class graph has no infinite path once weighted states are excluded;
5. weighted states terminate by F11.
```

---

## F3.13. Remaining extraction risks

Before final manuscript status:

```text
R1. Define type_rank and boundary_rank explicitly or avoid using them in the main text.
R2. Ensure M_NW^* coordinate order matches F9 exactly.
R3. Ensure F6--F11 use T1--T9 terminology consistently.
R4. Formalize first-changed-endpoint minimality only if needed in F11 main text.
R5. Avoid overloading R as both ordering and right block in final manuscript.
```

---

## F3.14. Extraction status

```text
Status: extracted draft.
Risk: YELLOW.
Next recommended extraction: F9 non-weighted termination theorem.
```
