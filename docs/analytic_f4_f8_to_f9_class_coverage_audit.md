# F4-F8 to F9.3 class coverage audit

## Purpose

Check whether every output class / routing destination produced by F4, F5, F6, F7, and F8 is represented in the F9.3 non-weighted class universe (`docs/final/F09_nonweighted_termination_theorem.md` §F9.3), or is explicitly marked as terminal, weighted exit, or unresolved.

## Claim boundary

This is a proof-audit document only, not a complete proof of Erdős 475. It identifies naming inconsistencies and potential coverage gaps between the F4-F8 routing theorems and the F9.3 class universe. It does not prove global termination or residue inclusion.

## F9.3 class universe

From `docs/final/F09_nonweighted_termination_theorem.md:161-192`:

```text
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
SINGLETON_RECURRENCE,
CYCLIC_RECURRENCE,
FORBIDDEN_RECURRENCE,
EXTERNAL_COLLISION,
BRIDGE_GAP.
```

Terminal states: `SUCCESS, CONTRADICTION`.

The class `WEIGHTED_CORE` is treated as an exit to F10-F11, not a non-weighted cycle node.

**Additional classes in F9.12 tables (not in F9.3):**

The F9.12 class-graph tables use several classes not listed in F9.3:
`PROPER_SUBINTERVAL, TEMPLATE_EXTERNAL_CANCELLATION, WRAPPING_BRIDGE, PAIR_DIFFERENCE_RECURRENCE, A34_RECURRENCE, BOUNDED_BLOCKER, LONG_BLOCKER, WEIGHTED_SIGNED_INTERVAL, CUT_RIGID_RETURN, ZERO_ATOM, DUPLICATE_ATOM, MINIMALITY_VIOLATION, INTERIOR_RELATIVE_ZERO`.

These are refinements or subclasses. The audit below checks F4-F8 outputs against the **F9.3** list, and notes the F9.12 subclasses separately.

## Coverage table

### F4: local descent theorem (`docs/final/F04_local_descent_theorem.md`)

**Theorem F4.10** lists these input classes and their routing destinations:

| Source theorem | Output class / branch                   | Destination in F9.3                                           | Status        | Notes                                                                                                                                                                                                    |
| -------------- | --------------------------------------- | ------------------------------------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| F4             | zero interval → contradiction           | CONTRADICTION                                                 | COVERED       | F4 uses descriptive "zero interval"; F9.3 uses `ZERO_COLLAPSE`. Name mismatch but mapping clear.                                                                                                         |
| F4             | enclosing_span or support_size decrease | PROPER_SUBINTERVAL                                            | UNRESOLVED    | "Measure decrease" is not a class name. The resulting state is a smaller instance of the same or lower class — not captured as a named F9.3 class. F9.12 uses `PROPER_SUBINTERVAL` which is not in F9.3. |
| F4             | routes to separated-equal/midpoint F5   | SEPARATED_EQUAL, MIDPOINT                                     | COVERED       | Explicit in F9.3.                                                                                                                                                                                        |
| F4             | routes to recurrence F7                 | SINGLETON_RECURRENCE, CYCLIC_RECURRENCE, FORBIDDEN_RECURRENCE | COVERED       | Explicit in F9.3.                                                                                                                                                                                        |
| F4             | routes to external/bridge F6/F8         | EXTERNAL_COLLISION, BRIDGE_GAP                                | COVERED       | Explicit in F9.3.                                                                                                                                                                                        |
| F4             | routes to weighted core F10/F11         | WEIGHTED_CORE                                                 | WEIGHTED_EXIT | Explicitly outside non-weighted universe.                                                                                                                                                                |

**F4 input classes and their F9.3 correspondence:**

| F4 name                     | F9.3 class            | Status         | Notes                                                                                                       |
| --------------------------- | --------------------- | -------------- | ----------------------------------------------------------------------------------------------------------- |
| zero interval               | ZERO_COLLAPSE         | AMBIGUOUS_NAME | F4 uses "zero interval → contradiction" while F9.3 has `ZERO_COLLAPSE`. Semantically same but names differ. |
| two-piece zero              | TWO_PIECE_ZERO        | COVERED        | Direct match.                                                                                               |
| higher zero-composite       | HIGHER_ZERO_COMPOSITE | COVERED        | Direct match. Also covers three-piece zero (F4.2 mentions it).                                              |
| equal interval              | EQUAL_INTERVAL        | COVERED        | Direct match.                                                                                               |
| signed interval             | SIGNED_INTERVAL       | COVERED        | Direct match.                                                                                               |
| pair-difference boundary    | PAIR_DIFFERENCE       | COVERED        | Direct match.                                                                                               |
| transported-prefix relation | TRANSPORTED_PREFIX    | COVERED        | Direct match.                                                                                               |

**F4 classes NOT in F9.3:**

| F4 concept                                                                               | Missing F9.3 class     | Status         | Notes                                                                                                            |
| ---------------------------------------------------------------------------------------- | ---------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------- |
| PREFIX_ZERO is in F9.3 but F4 never uses the name                                        | PREFIX_ZERO            | AMBIGUOUS_NAME | F4 doesn't list PREFIX_ZERO as a separate class. Could be covered by "zero interval at prefix position".         |
| ZERO_COMPOSITE_SURGERY is in F9.3 but F4 never uses the name                             | ZERO_COMPOSITE_SURGERY | AMBIGUOUS_NAME | F4 covers zero-composite surgery in Lemmas F4.2-F4.3 but doesn't use the F9.3 name.                              |
| THREE_PIECE_ZERO is in F9.3 but F4.10 only lists "two-piece zero, higher zero-composite" | THREE_PIECE_ZERO       | COVERED        | F4.2 explicitly defines three-piece zero. Absent from F4.10 list but covered by "higher zero-composite" concept. |

---

### F5: separated-equal and midpoint routing (`docs/final/F05_separated_equal_midpoint_routing.md`)

**Theorem F5.10** routing destinations:

| Source theorem | Output class / branch                   | Destination in F9.3                                            | Status        | Notes                                                          |
| -------------- | --------------------------------------- | -------------------------------------------------------------- | ------------- | -------------------------------------------------------------- |
| F5             | success by direct exchange or gap-after | SUCCESS                                                        | COVERED       | Terminal.                                                      |
| F5             | strict gap/support/span descent         | PROPER_SUBINTERVAL                                             | UNRESOLVED    | Same issue as F4 — measure decrease is not a named F9.3 class. |
| F5             | zero-composite/equal/signed interval F4 | ZERO_COLLAPSE, TWO_PIECE_ZERO, EQUAL_INTERVAL, SIGNED_INTERVAL | COVERED       | Routes to F4 which then maps to F9.3 classes.                  |
| F5             | external collision F6                   | EXTERNAL_COLLISION                                             | COVERED       | Explicit in F9.3.                                              |
| F5             | recurrence F7                           | SINGLETON_RECURRENCE, CYCLIC_RECURRENCE, FORBIDDEN_RECURRENCE  | COVERED       | Routes to F7 which then maps to F9.3 classes.                  |
| F5             | bridge/gap descent F8                   | BRIDGE_GAP                                                     | COVERED       | Explicit in F9.3.                                              |
| F5             | weighted-core candidate F10/F11         | WEIGHTED_CORE                                                  | WEIGHTED_EXIT | Explicitly outside non-weighted universe.                      |
| F5             | collapse or minimality contradiction    | CONTRADICTION                                                  | COVERED       | Terminal.                                                      |

---

### F6: external collision theorem (`docs/final/F06_external_collision_theorem.md`)

**Theorem F6.7** routing destinations (with F6.10 measure-effect mapping):

| Source theorem | Output class / branch                | Destination in F9.3             | Status        | Notes                                                                |
| -------------- | ------------------------------------ | ------------------------------- | ------------- | -------------------------------------------------------------------- |
| F6             | bridge zero-composite → F8           | BRIDGE_GAP                      | COVERED       | Mapped through F8. F6 uses descriptive name; F9.3 uses `BRIDGE_GAP`. |
| F6             | signed bridge composite → F8         | BRIDGE_GAP                      | COVERED       | Same BRIDGE_GAP class.                                               |
| F6             | equal/separated interval → F4/F5     | EQUAL_INTERVAL, SEPARATED_EQUAL | COVERED       | Explicit in F9.3.                                                    |
| F6             | transported-prefix relation → F10/F4 | TRANSPORTED_PREFIX              | COVERED       | Explicit in F9.3.                                                    |
| F6             | pair-difference boundary → F4/F7     | PAIR_DIFFERENCE                 | COVERED       | Explicit in F9.3.                                                    |
| F6             | cyclic-cut branch → F7               | CYCLIC_RECURRENCE               | COVERED       | Explicit in F9.3.                                                    |
| F6             | singleton/prefix recurrence → F7     | SINGLETON_RECURRENCE            | COVERED       | Explicit in F9.3.                                                    |
| F6             | weighted-core normal form → F10/F11  | WEIGHTED_CORE                   | WEIGHTED_EXIT | Explicitly outside non-weighted universe.                            |
| F6             | collapse or minimality contradiction | CONTRADICTION                   | COVERED       | Terminal.                                                            |

---

### F7: recurrence routing theorem (`docs/final/F07_recurrence_routing_theorem.md`)

**Theorem F7.8** routing destinations:

| Source theorem | Output class / branch                     | Destination in F9.3                                            | Status        | Notes                                                                                     |
| -------------- | ----------------------------------------- | -------------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------- |
| F7             | strict M_NW^\* descent by bounded blocker | PROPER_SUBINTERVAL                                             | UNRESOLVED    | Measure decrease; same issue as F4/F5. F9.12 uses `BOUNDED_BLOCKER` which is not in F9.3. |
| F7             | zero-composite/equal/signed interval → F4 | ZERO_COLLAPSE, TWO_PIECE_ZERO, EQUAL_INTERVAL, SIGNED_INTERVAL | COVERED       | Routes to F4.                                                                             |
| F7             | pair-difference machinery                 | PAIR_DIFFERENCE                                                | COVERED       | Explicit in F9.3.                                                                         |
| F7             | singleton-prefix recurrence               | SINGLETON_RECURRENCE                                           | COVERED       | Explicit in F9.3.                                                                         |
| F7             | cyclic-cut recurrence                     | CYCLIC_RECURRENCE                                              | COVERED       | Explicit in F9.3.                                                                         |
| F7             | external bridge branch → F6/F8            | EXTERNAL_COLLISION, BRIDGE_GAP                                 | COVERED       | Explicit in F9.3.                                                                         |
| F7             | weighted-core branch → F10/F11            | WEIGHTED_CORE                                                  | WEIGHTED_EXIT | Explicitly outside non-weighted universe.                                                 |
| F7             | collapse or minimality contradiction      | CONTRADICTION                                                  | COVERED       | Terminal.                                                                                 |

**Additional F7 subclasses (from lemmas F7.4-F7.7):**

| Source lemma                     | Output class / branch                                                                                                     | Destination in F9.3               | Status  | Notes                                                                                 |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ------- | ------------------------------------------------------------------------------------- |
| F7.4 H1/H2 long blocker          | suffix-zero, zero-composite, pair-difference, signed/equal interval, bridge zero-composite, endpoint singleton recurrence | various F9.3 classes              | COVERED | All sub-routes map to existing F9.3 classes. F9.12 uses `LONG_BLOCKER`.               |
| F7.5 pair-difference recurrence  | pair-difference, zero-composite, signed/equal bridge, singleton/scalar-prefix recurrence                                  | PAIR_DIFFERENCE, etc.             | COVERED | All sub-routes map to existing F9.3 classes. F9.12 uses `PAIR_DIFFERENCE_RECURRENCE`. |
| F7.6 singleton-prefix recurrence | suffix-zero, pair-difference, external bridge, cyclic recurrence                                                          | SINGLETON_RECURRENCE, etc.        | COVERED | All sub-routes map to existing F9.3 classes.                                          |
| F7.7 cyclic-cut recurrence       | midpoint boundary, zero-composite, wrapping bridge, singleton-prefix, pair-difference                                     | MIDPOINT, CYCLIC_RECURRENCE, etc. | COVERED | All sub-routes map to existing F9.3 classes.                                          |

---

### F8: bridge/gap descent theorem (`docs/final/F08_bridge_gap_descent_theorem.md`)

**Theorem F8.11** routing destinations:

| Source theorem | Output class / branch                                   | Destination in F9.3                                            | Status        | Notes                                                 |
| -------------- | ------------------------------------------------------- | -------------------------------------------------------------- | ------------- | ----------------------------------------------------- |
| F8             | enclosing_span decrease by proper-overlap               | PROPER_SUBINTERVAL                                             | UNRESOLVED    | Measure decrease; same issue.                         |
| F8             | support_size decrease by proper-containment             | PROPER_SUBINTERVAL                                             | UNRESOLVED    | Measure decrease; same issue.                         |
| F8             | bridge gap decrease (gap-after / proper-gap recurrence) | measure coordinate                                             | COVERED       | Gap decrease is a coordinate change, not a new class. |
| F8             | zero-composite/equal/signed interval → F4               | ZERO_COLLAPSE, TWO_PIECE_ZERO, EQUAL_INTERVAL, SIGNED_INTERVAL | COVERED       | Routes to F4.                                         |
| F8             | recurrence → F7                                         | SINGLETON_RECURRENCE, CYCLIC_RECURRENCE, FORBIDDEN_RECURRENCE  | COVERED       | Routes to F7.                                         |
| F8             | external collision → F6                                 | EXTERNAL_COLLISION                                             | COVERED       | Explicit in F9.3.                                     |
| F8             | midpoint/adjacent-equal → F5                            | MIDPOINT, SEPARATED_EQUAL                                      | COVERED       | Routes through F5.                                    |
| F8             | direct exchange → separated-equal tables                | SEPARATED_EQUAL                                                | COVERED       | Routes through F5.                                    |
| F8             | weighted-core exit → F10/F11                            | WEIGHTED_CORE                                                  | WEIGHTED_EXIT | Explicitly outside non-weighted universe.             |
| F8             | collapse or success                                     | SUCCESS, CONTRADICTION                                         | COVERED       | Terminal.                                             |

## Summary table

| Source | Total outputs               | COVERED | UNRESOLVED | AMBIGUOUS_NAME | WEIGHTED_EXIT | TERMINAL |
| ------ | --------------------------- | ------- | ---------- | -------------- | ------------- | -------- |
| F4     | 6 routing + 7 class entries | 10      | 1          | 4              | 1             | 1        |
| F5     | 8                           | 6       | 1          | 0              | 1             | 0        |
| F6     | 9                           | 8       | 0          | 0              | 1             | 0        |
| F7     | 8                           | 7       | 1          | 0              | 1             | 0        |
| F8     | 10                          | 8       | 2          | 0              | 1             | 0        |

## Findings

### All covered classes

Every named routing destination from F4-F8 maps to an existing F9.3 class:

- `ZERO_COLLAPSE`, `TWO_PIECE_ZERO`, `HIGHER_ZERO_COMPOSITE`, `EQUAL_INTERVAL`, `SIGNED_INTERVAL`, `PAIR_DIFFERENCE`, `TRANSPORTED_PREFIX` (F4)
- `SEPARATED_EQUAL`, `MIDPOINT` (F5)
- `EXTERNAL_COLLISION` (F6)
- `SINGLETON_RECURRENCE`, `CYCLIC_RECURRENCE`, `FORBIDDEN_RECURRENCE` (F7, F8)
- `BRIDGE_GAP` (F8, F6)
- `SUCCESS`, `CONTRADICTION` (terminal)

### Unresolved items

1. **PROPER_SUBINTERVAL is not in F9.3** — Every theorem (F4-F8) routes "measure decrease" (enclosing_span or support_size decrease) as a non-terminal output. This "decrease to a smaller instance" is captured in F9.12 as `PROPER_SUBINTERVAL`, but this class name does not appear in the F9.3 class universe. The F9.3 universe has `PREFIX_ZERO` and `TWO_PIECE_ZERO` which cover some subinterval cases, but a generic "strict decrease → smaller instance" is not an explicit F9.3 class.

2. **Class name mismatches** — F4 uses descriptive names ("zero interval", "two-piece zero") while F9.3 uses enum-style names (`ZERO_COLLAPSE`, `TWO_PIECE_ZERO`). These are semantically identical but the naming convention differs.

3. **PREFIX_ZERO and ZERO_COMPOSITE_SURGERY in F9.3, absent from F4** — These classes exist in the F9.3 universe but F4 does not explicitly list them as input classes. `PREFIX_ZERO` is a zero interval at a prefix position; F4 covers this conceptually under "zero interval." `ZERO_COMPOSITE_SURGERY` arises from zero-composite uncrossing; F4 covers this under Lemmas F4.2-F4.3 without using the F9.3 name.

### No missing class gaps

No F4-F8 theorem produces an output that routes to a completely uncovered obstruction class. All routing destinations land in the F9.3 set, terminal, or weighted exit.

### Named subclasses in F9.12 not in F9.3

The F9.12 class-graph tables introduce subclasses (`PROPER_SUBINTERVAL`, `TEMPLATE_EXTERNAL_CANCELLATION`, `WRAPPING_BRIDGE`, `PAIR_DIFFERENCE_RECURRENCE`, `A34_RECURRENCE`, `BOUNDED_BLOCKER`, `LONG_BLOCKER`, `ZERO_ATOM`, `DUPLICATE_ATOM`, `MINIMALITY_VIOLATION`, `INTERIOR_RELATIVE_ZERO`, `WEIGHTED_SIGNED_INTERVAL`, `CUT_RIGID_RETURN`) that are not part of the F9.3 class universe. These are refinement classes used for routing precision, not new obstruction species. The F9.3 universe and the F9.12 tables should be synchronized: either F9.3 should include the F9.12 classes, or F9.12 should explicitly note they are subclasses of F9.3 classes.

## Required follow-up

One targeted task: Add `PROPER_SUBINTERVAL` and the other F9.12-defined subclasses to the F9.3 class universe (with a note that they are refinement classes), or explicitly document in F9.3 that the class universe is a "core" set and subclasses are in F9.12. Then mark R4 resolved.
