# Analytic state-machine coverage table A93

This note continues from A92.

A92 defined an obstruction state machine with allowed transition types:

```text
T-adjacent-swap
T-block-exchange
T-cut-swap
T-cyclic-cut
T-atom-insertion-normalization
T-A5-blocker-pullback
T-external-collision-pullback
T-normal-form-rewrite
```

A93 maps the analytic notes A1--A92 into these transition types.  The purpose is to identify whether any routing step used in the proof program lies outside the state-machine model.

Main conclusion:

```text
Most routing steps fit the A92 transition list.
The uncovered pieces are not new move types; they are proof obligations about progress/descent and exhaustive coverage.
```

The two remaining formal issues are:

```text
1. strict progress lemma for unobstructed first endpoint changes;
2. exhaustive verification that universal delegators A62, A64, and A60 cover all external/recurrence/cut-swap cases.
```

---

## 1. Transition type reference

Use these abbreviations.

| Code | Transition type |
|---|---|
| TAS | T-adjacent-swap |
| TBX | T-block-exchange |
| TCS | T-cut-swap |
| TCC | T-cyclic-cut |
| TAIN | T-atom-insertion-normalization |
| TA5 | T-A5-blocker-pullback |
| TEX | T-external-collision-pullback |
| TNF | T-normal-form-rewrite |
| TERM | terminal success/contradiction |
| MEAS | measure-decrease/progress assertion |

---

## 2. Early theorem and setup notes

| Notes | Role | Transition coverage | Status |
|---|---|---|---|
| A1--A3 | theorem reductions and endpoint-avoidance framing | not state-machine moves | clean theorem layer |
| A4--A5 | first forbidden hit and adjacent blocker | TAS + TA5 | needs final hardening of blocker equation |
| A6--A19 | early exploratory/structural setup if present | TNF / definitions | audit for obsolete content |

Coverage issue:

```text
A5 must be extracted as the first final local lemma.
```

Required final form:

```text
If adjacent swap at first forbidden hit does not succeed, then either collision or recurrence produces an A5 blocker equation.
```

---

## 3. Zero-composite and interval setup

| Notes | Role | Transition coverage | Status |
|---|---|---|---|
| A20--A27 | interval/signed interval algebra | TNF + TBX | covered, but sign audit required |
| A28--A33 | zero-composite surgery / atom insertion | TAIN + TNF + TAS | covered, endpoint audit required |
| A34--A35 | recurrence status and obstruction classes | TA5 + TNF | covered as status layer |

Coverage issue:

```text
Atom insertion is explicitly covered by TAIN, but every H1/H2 forbidden hit must then enter TA5.
```

---

## 4. Separated-equal and midpoint notes

| Notes | Role | Transition coverage | Status |
|---|---|---|---|
| A36--A48 | direct exchange D-branch analysis | TBX + TNF | covered, table must be hardened |
| A49--A54 | gap-after E-branch analysis | TBX + TNF | covered, endpoint cases required |
| A55 | midpoint boundary / adjacent equal | TNF + TBX | covered, odd-characteristic audit required |

Coverage issue:

```text
D2 and gap-after recurrence branches must be linked explicitly to TA5 or recurrence-state transitions.
```

No new transition type needed.

---

## 5. Weighted and external-collision setup

| Notes | Role | Transition coverage | Status |
|---|---|---|---|
| A56 | weighted normal forms / transported-prefix | TNF | covered, exhaustiveness high-risk |
| A58 | nested zero-composite rewrite | TNF | covered |
| A59 | static cut insufficiency | advisory / DROP candidate | not needed as transition |
| A60 | fixed weighted cut-swap | TCS + TNF + TA5 | covered, high-risk table |
| A61 | status after cut-swap | status layer | merge/drop after hardening |
| A62 | external collision pullback | TEX | covered, high-risk universal delegator |
| A63 | obstruction class status | TNF/status | covered |

Coverage issue:

```text
A62 must prove all external collisions enter TEX outputs.
A60 must prove all displayed cut-swap collisions are TBX/TCS/TNF-compatible.
```

No new transition type needed.

---

## 6. Recurrence routing notes

| Notes | Role | Transition coverage | Status |
|---|---|---|---|
| A64 | bounded-blocker recurrence descent | TA5 + MEAS | covered, strict measure proof needed |
| A65 | H1 long-blocker non-crossing | TAIN + TA5 + TNF | covered |
| A66 | H1 crossing cases | TAIN + TA5 + TEX + TNF | covered, bridge signs audit |
| A67 | H2 long-blocker | TAIN + TA5 + TEX + TNF | covered, right-blocker audit |
| A68 | recurrence status map | status layer | merge into final recurrence theorem |
| A69 | pair-swap recurrence | TAS + TA5 + TNF | covered |
| A70 | singleton-prefix recurrence | TA5 + TNF | covered |
| A71 | cyclic-cut recurrence | TCC + TA5 + TNF | covered |

Coverage issue:

```text
A64's bounded-blocker descent is not a new transition, but it must be a formal MEAS assertion under the final measure.
```

No new transition type needed.

---

## 7. Dependency graph and non-weighted acyclicity

| Notes | Role | Transition coverage | Status |
|---|---|---|---|
| A72 | obstruction dependency graph | graph over transition outputs | covered as meta-layer |
| A73 | global acyclicity attempt | MEAS | proof sketch, superseded by A78/A87/A88 audit |
| A74 | bridge-span monotonicity | TEX + TBX + TNF + MEAS | covered, harden |
| A75 | equal-span separated bridge | TBX + TA5 + TNF + MEAS | covered |
| A76 | gap-preserving separated recurrence | TBX + TA5 + TEX + MEAS | covered |
| A77 | rigid separated self-return | TBX + TA5 + TCC + TNF | covered |
| A78 | non-weighted acyclicity theorem | MEAS over graph | covered, conditional on hardening |

Coverage issue:

```text
A74--A77 contain the bridge/gap chain.  All moves fit the state machine, but the measure-decrease claims must be converted from sketches to explicit inequalities.
```

No new transition type needed.

---

## 8. Weighted cut-selection and closure notes

| Notes | Role | Transition coverage | Status |
|---|---|---|---|
| A79 | weighted cut-selection split | TCS + TNF + MEAS | covered, weak rigidity issue noted later |
| A80 | atom-middle weighted core | TAS + TNF + TA5 | covered |
| A81 | endpoint-rigid atom-middle | TNF + TAS | covered, sign audit required |
| A82 | cut-rigid weighted self-return | TCS + TCC + TNF + MEAS | covered, weakened by A89/A90 |
| A83 | internal cyclic rigidity | TCC + TNF | covered only under strong-exact assumption |
| A89 | strong exact cyclic self-return hardening | TCC + TNF | covered |
| A90 | weak-to-pattern diagnostic | TNF + MEAS + state-data comparison | covered, introduces A90.10 |
| A91 | first-changed-endpoint lemma | all transition types + MEAS | covered, conditional on finite path/progress |
| A92 | state-machine formalization | meta-layer | current model |

Coverage issue:

```text
A79--A83 originally assumed too much about exact self-return.
A89--A92 repair this by requiring pattern-rigidity or first-changed-endpoint/progress analysis.
```

No new transition type needed, but strict progress remains open.

---

## 9. Assembly, theorem dependency, and audit notes

| Notes | Role | Transition coverage | Status |
|---|---|---|---|
| A84 | endpoint-avoidance assembly | theorem layer | conditional |
| A85 | theorem dependency audit | theorem layer | clean |
| A86 | finite/exceptional cases | theorem/certification layer | p=2 clean; computation advisory |
| A87 | local lemma audit checklist | audit layer | active |
| A88 | formal dependency table | audit/extraction layer | active |

These are not local move transitions.  They depend on the state-machine coverage and strict progress lemma.

---

## 10. Transition coverage summary

Every major move used in the A-notes is covered by one of the A92 transition types.

```text
Adjacent swaps                 -> TAS
Separated equal exchanges      -> TBX
Gap-after moves                -> TBX
Weighted proper cut swaps      -> TCS
Cyclic rotations               -> TCC
Atom-insertion normalizations  -> TAIN
Recurrent blocker pullbacks    -> TA5
External collisions            -> TEX
Algebraic rewrites             -> TNF
```

No additional transition type is currently required.

---

## 11. Uncovered proof obligations

Although transition-type coverage is adequate, several proof obligations remain uncovered.

### U1. Strict progress lemma

Needed from A91/A92:

```text
An unobstructed first endpoint-pattern change strictly decreases a formal measure or produces success.
```

Current status:

```text
not fully proved.
```

---

### U2. Universal external-collision classification

Needed from A62:

```text
Every external collision pulled back from any local move is TEX and lands in a named class with non-increasing measure.
```

Current status:

```text
covered conceptually, needs exhaustive proof.
```

---

### U3. Recurrence bounded-blocker measure

Needed from A64:

```text
Bounded blockers strictly decrease the final global measure.
```

Current status:

```text
covered conceptually, needs final measure verification.
```

---

### U4. Cut-swap displayed collision table

Needed from A60:

```text
All displayed cut-swap collision equations route to covered transition outputs.
```

Current status:

```text
covered conceptually, high-risk sign/endpoint audit.
```

---

### U5. Bridge/gap measure inequalities

Needed from A74--A77:

```text
All bridge/gap returns either decrease span/gap/support or enter a covered recurrence/normal-form branch.
```

Current status:

```text
covered conceptually, proof sketches need hardening.
```

---

## 12. State-machine coverage theorem

## Theorem A93.1: A1--A92 routing uses no move outside the A92 state machine

Every local move or routing operation used in A1--A92 is represented by one of the transition types:

```text
TAS, TBX, TCS, TCC, TAIN, TA5, TEX, TNF.
```

### Proof

The coverage tables in Sections 2--9 assign each note cluster to transition types.  The assignment covers adjacent swaps, block exchanges, weighted cut-swaps, cyclic cuts, atom insertion, A5 recurrence pullbacks, external collision pullbacks, and normal-form rewrites.  These exhaust the local operations used in the analytic notes. ∎

### Status

This theorem is a coverage assertion.  It does not prove each transition's algebra or measure effect.  Those are U1--U5.

---

## 13. Consequence for A91/A92

A91's first-changed-endpoint lemma can now be stated against the A92 state machine because every prior routing operation fits the transition list.

The only remaining point is not coverage but strict progress:

```text
unobstructed first endpoint change -> measure descent or success.
```

Thus the next target should be U1.

---

## 14. Target A94

A94 should prove the strict progress lemma.

Suggested title:

```text
Strict progress lemma for unobstructed endpoint changes A94
```

Minimum statement:

Let an obstruction path in a minimal counterexample have a first endpoint-pattern change.  If the changed endpoint does not collide, does not hit `f`, does not create a weighted self-return with the same measure, and does not increase the active measure, then the path has made strict progress.  Formalize progress as a decrease of:

```text
M_progress=(
  unresolved_endpoint_changes,
  active_obstruction_measure,
  transition_depth
)
```

or replace it with direct success/descent.

---

## Current status after A93

Proved/recorded here:

```text
1. transition coverage table for A1--A92;
2. no new transition type appears necessary;
3. remaining proof obligations U1--U5 isolated;
4. U1 strict progress lemma is the next bottleneck.
```

Still open:

```text
1. strict progress lemma;
2. hardening A62, A64, A60, A74--A77;
3. final unconditional proof extraction.
```
