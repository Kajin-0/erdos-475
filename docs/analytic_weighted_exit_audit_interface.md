# Weighted-exit audit: every WEIGHTED_EXIT from F9/F4-F8, entry points, measure decrease, and interface status

## Claim boundary

This is a proof-audit document mapping every WEIGHTED_EXIT in the F4-F9 theorem suite to its F10/F11 entry, the exit-back measure conditions, and whether the F9/F11 mutual-induction interface is closed. It does not prove new F11 machinery. It records what each theorem currently claims and what is missing.

## Mutual Induction Interface (from docs/analytic_f9_f11_mutual_induction_convention.md)

Pattern: NW0 -> W(m) -> { terminal, W(m') with m'<m, NW1 with M_NW^_(NW1)<M_NW^_(NW0), or NW1 with no-reentry certificate }.

Every WEIGHTED_EXIT from a non-weighted lemma must eventually satisfy one of:

1. terminal (SUCCESS, CONTRADICTION, collapse);
2. strict M_NW^\* decrease relative to the non-weighted parent NW0 that entered the weighted branch;
3. return to W(m') with strictly smaller |B|;
4. no-reentry certificate forbidding W(j), j >= m, at equal-or-larger M_NW^\*.

---

## Table: every WEIGHTED_EXIT, entry, exit measure, and interface status

| #   | Source theorem | Entry condition into F10/F11                                                                 | Exit-back from weighted branch                            | Decreasing coordinate on exit (as claimed)     | Allowed return paths | Interface closed?                                         | Key unresolved dependency                                                                                          |
| --- | -------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------- | -------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| W1  | F4.10(6)       | transported-prefix relation where coefficient-2 survives all easy reductions                 | handed to F10/F11 per F4.9                                | NOT SPECIFIED at F4 level — delegated entirely | delegated to F11     | OPEN                                                      | F4 does not track NW0 measure; F11 must prove decrease relative to NW0                                             |
| W2  | F5.10(7)       | genuine coefficient-2 normal form surviving direct-exchange or gap-after collision table     | handed to F10/F11 per F5.2, F5.6                          | NOT SPECIFIED at F5 level — delegated entirely | delegated to F11     | OPEN                                                      | F5 does not track NW0 measure; F11 must prove decrease relative to NW0                                             |
| W3  | F6.7(8)        | weighted-core normal form from signed external collision where coefficient-2/core remains    | handed to F10/F11 per F6.3, F6.9                          | NOT SPECIFIED at F6 level — routed out         | delegated to F11     | OPEN                                                      | F6 does not track NW0 measure; F6.10 says "routed to F10/F11" with no decrease condition                           |
| W4  | F7.8(7)        | weighted-core branch from recurrence (signed/crossing blocker where weighted output appears) | handed to F10/F11 per F7.4-F7.7                           | NOT SPECIFIED at F7 level — delegated          | delegated to F11     | OPEN                                                      | F7 does not track NW0 measure; F7.8(7) says "handled by F10/F11" without mutual-induction condition                |
| W5  | F8.11(9)       | irreducible signed correction (coefficient-2/core) from bridge/gap descent                   | handed to F10/F11 per F8.7                                | NOT SPECIFIED at F8 level — delegated          | delegated to F11     | OPEN - RED inherited                                      | F8.11 explicitly says "high-risk inherited dependency because F10/F11 weighted-core termination is not yet closed" |
| W6  | F9.6           | any non-weighted state entering WEIGHTED_CORE                                                | F10/F11 returns: success, collapse, NW machinery, smaller | B                                              | , or induction       | F9 claims "F10-F11 ensure the weighted branch" terminates | OPEN - inherits F11 risk                                                                                           | F9.6 audit flag: "inherits the risk status of F11. In the final manuscript, F11 must be fully hardened before F9 can be considered final." |

---

## Detail: what F10/F11 claim about each exit

### F10 easy reductions (Lemma F10.1, Theorem F10.5)

| A56/NW exit                           | F10 claim                                             | Exit-back condition           | Interface status                               |
| ------------------------------------- | ----------------------------------------------------- | ----------------------------- | ---------------------------------------------- |
| B=0 -> ZERO_COLLAPSE                  | terminal                                              | terminal                      | CLOSED if B genuinely nonempty in genuine core |
| A+B=0 -> TWO_PIECE_ZERO               | "non-weighted, exits to F4-F9 under mutual induction" | NOT SPECIFIED relative to NW0 | OPEN — F10 does not track NW0 measure          |
| B+C=0 -> TWO_PIECE_ZERO               | same                                                  | NOT SPECIFIED relative to NW0 | OPEN                                           |
| A=C -> EQUAL_INTERVAL/SEPARATED_EQUAL | same                                                  | NOT SPECIFIED relative to NW0 | OPEN                                           |
| transported-prefix/tail               | same                                                  | NOT SPECIFIED relative to NW0 | OPEN                                           |

### F10 cut-swap displayed collisions (Lemma F10.3, A97 rows)

| A97/NW exit                                               | F10 claim                          | Exit-back condition                    | Interface status |
| --------------------------------------------------------- | ---------------------------------- | -------------------------------------- | ---------------- |
| zero-composite / two-piece zero / equal-prefix/equal-tail | "routes to non-weighted machinery" | NOT SPECIFIED relative to NW0          | OPEN             |
| forbidden recurrence (E20-E21)                            | "routed by F7"                     | depends on F7 bounded-blocker decrease | OPEN             |
| external collision (E22)                                  | "routed by F6"                     | depends on F6/F8/F9 finite-budget      | OPEN             |

### F11 atom-middle (Lemma F11.2)

| Exit                              | F11 claim                       | Exit-back condition                      | Interface status                            |
| --------------------------------- | ------------------------------- | ---------------------------------------- | ------------------------------------------- |
| A56 easy reduction                | NW1 satisfying mutual induction | CLAIMED but NOT PROVED for every subcase | OPEN — remaining: parent-support annotation |
| zero collapse / two-atom zero     | terminal                        | terminal                                 | CLOSED                                      |
| pair-difference / signed interval | non-weighted                    | NOT SPECIFIED relative to NW0            | OPEN                                        |
| midpoint / singleton recurrence   | non-weighted, F7                | depends on F7 decrease                   | OPEN                                        |

### F11 proper-middle cut-swap (Lemma F11.3)

| Exit                                                 | F11 claim      | Exit-back condition                                | Interface status                    |
| ---------------------------------------------------- | -------------- | -------------------------------------------------- | ----------------------------------- |
| success                                              | terminal       | CLOSED                                             |
| displayed collision routed to zero/equal/signed/pair | "non-weighted" | NOT SPECIFIED relative to NW0                      | OPEN                                |
| external collision via F6                            | "routed"       | depends on F6/F8/F9 finite-budget                  | OPEN                                |
| recurrence via F7                                    | "routed"       | depends on F7 bounded-blocker decrease             | OPEN                                |
| isolated signed-boundary equal-prefix/equal-tail     | "non-weighted" | NOT SPECIFIED relative to NW0                      | OPEN                                |
| persistent cut-rigidity                              | to F11.6/F11.7 | pattern-rigid impossible (F11.7) or routed (F11.6) | ORANGE — A90-A94 not yet formalized |

---

## W-to-NW exit decrease table (docs/analytic_weighted_to_nonweighted_exit_decrease_table.md) status

22 rows enumerated. Only 2 GREEN (E1, E9). 19 YELLOW. 1 ORANGE (E4, A=C equal-outer).
0 RED. But YELLOW means "locally classified but needing final lexicographic edge verification."

Key shortfall: the table compares NW1 against the weighted window Wwin, not against NW0. The mutual induction interface requires comparison against NW0. The table acknowledges this:

> "A local support-size decrease is not automatically a final lexicographic decrease unless earlier coordinates of M_NW^\* are also shown not to increase."
> "Final mutual induction needs comparison against NW_0, not only Wwin."

---

## Summary

| Aspect                                        | Status                                                                                                                 |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Every WEIGHTED_EXIT from F4-F9 identified     | YES — all 6 source theorems have explicit WEIGHTED_EXIT branches                                                       |
| Entry point into F10/F11 described            | YES — each theorem describes the entry condition (coefficient-2 survival, signed correction, etc.)                     |
| Measure decrease on exit back to NW           | NO — neither F4, F5, F6, F7, nor F8 specifies the decrease condition relative to NW0                                   |
| F9.6 claims weighted exits terminate          | YES — but explicitly inherits F11 risk                                                                                 |
| F10 easy reductions track NW0 measure         | NO — F10.1 says "exits under mutual induction" without computing decrease                                              |
| F11 atom-middle tracks NW0 measure            | NO — cites parent-support annotations as remaining work                                                                |
| F11 proper-middle cut-swap tracks NW0 measure | NO — delegates to W-to-NW table which acknowledges the gap                                                             |
| W-to-NW exit table compares against NW0       | NO — compares against Wwin; acknowledges NW0 comparison is still needed                                                |
| A90-A94 formalized                            | NO — still needed for weak-to-pattern-rigidity reduction                                                               |
| F9/F11 mutual-induction interface             | OPEN — the interface convention document exists but no theorem pair currently satisfies it without additional auditing |

## Conclusion

The F9/F11 mutual-induction interface is **OPEN**. Every WEIGHTED_EXIT in F4-F9 successfully routes to F10/F11 as a destination, but neither the source theorems nor F10/F11 currently prove that the exit-back condition (M_NW^_(NW1) < M_NW^_(NW0)) holds. The W-to-NW exit table enumerates all 22 exit types and gives local decrease candidates relative to the weighted window, but the parent-relative comparison is not yet certified. F11.1 (controlled-exit theorem) states the required condition but the proof currently depends on parent-support annotations and A90-A94 formalization that do not exist in final form.
