# F00.SNS.C11 local rank-descent verification

This file continues the strong nonzero-sum repair path.

C10 supplied finite rank tables for the phase-aware global measure:

```text
M_phase=(D_SNS^*, phase_rank, M_loc, M_w, transition_budget).
```

C11 verifies the non-weighted local rank rows first:

```text
ZERO_DEFECT,
LOCAL_ZERO_COMPOSITE,
EQUAL_INTERVAL,
SIGNED_INTERVAL,
PAIR_DIFFERENCE,
SEPARATED_EQUAL,
MIDPOINT_ADJACENT.
```

The goal is to show that these rows either decrease the global collision profile, decrease local span/gap/support, lower type rank, consume finite transition budget, or route to already named phase-aware branches.

Status: verification draft.  Weighted repair is not handled here.

---

## C11.1. Standing phase-aware convention

Work in `ARBITRARY` phase unless explicitly stated otherwise.

A nonempty zero interval is not a contradiction.  It is a collision defect measured by

```text
D_SNS^*(R)=(P_col(R),L_col^*(R),boundary_rank(R)).
```

Let the active shortest zero interval have span

```text
m.
```

A produced zero interval of span `m'` is compared to `m` and to the active location.

---

## C11.2. ZERO_DEFECT row

## Lemma C11.1: zero defect is controlled by collision profile

A produced zero interval `Z'` of span `m'` satisfies exactly one of:

```text
1. m'<m: impossible by minimality of the active shortest collision;
2. m'=m and location earlier than active: impossible by active-location choice;
3. m'=m and location equal to active: no repair occurred;
4. m'=m and location later: active-location coordinate improves after active repair;
5. m'>m: lower-priority defect, subordinate to active repair.
```

### Proof

A zero interval is exactly an endpoint collision.  The collision profile orders collisions first by span and then the active location tie-breaker.  The listed cases exhaust comparisons of `m'` with `m` and the location order. ∎

### Verification status

The row is verified once every transition producing a zero interval identifies its span and location.

Remaining obligation:

```text
Each local table must annotate the produced zero interval span/location.
```

---

## C11.3. LOCAL_ZERO_COMPOSITE row

A local zero-composite has form

```text
U_1+...+U_r=0,
r>=2.
```

where the `U_i` are displayed intervals or bounded atom corrections.

## Lemma C11.2: overlapping zero-composite pieces reduce support/span

If two pieces in a local zero-composite overlap or one contains the other, uncrossing produces a zero/equal/signed relation with strictly smaller local support or enclosing span.

### Proof

For overlap, cancel the common interval.  For containment, subtract the contained interval from the containing interval.  In both cases at least one atom is removed from the active support.  Therefore either `enclosing_span` or `support_size` in `M_loc` decreases. ∎

## Lemma C11.3: separated zero-composites route to bridge/gap or separated-equal rows

If all zero-composite pieces are disjoint after uncrossing, then the relation is separated.  It routes to either:

```text
SEPARATED_EQUAL,
BRIDGE_GAP,
SIGNED_INTERVAL,
or ZERO_DEFECT with controlled span.
```

### Proof

Disjoint zero-composite pieces form separated interval relations.  If two sides have equal total they are separated-equal.  If one side lies outside the active window, it is bridge/gap.  Bounded corrections give signed interval.  If pieces merge into one interval, it is a zero defect. ∎

### Verification status

LOCAL_ZERO_COMPOSITE is verified modulo the explicit zero-composite uncrossing table.

---

## C11.4. EQUAL_INTERVAL row

An equal-interval relation has form

```text
sum(U)=sum(V).
```

## Lemma C11.4: proper-overlap equal intervals decrease enclosing span

If `U` and `V` properly overlap, then uncrossing removes the nonempty overlap and gives a smaller equal/zero relation.

### Proof

Write

```text
U=U_0 O,
V=O V_1
```

with nonempty overlap `O`.  Equality gives `sum(U_0)=sum(V_1)`.  The active enclosure is strictly smaller because `O` is removed. ∎

## Lemma C11.5: proper-containment equal intervals decrease support

If one equal interval properly contains the other, subtracting the contained interval leaves a complement zero-composite with strictly smaller support.

### Proof

If `U=L V R` and `sum(U)=sum(V)`, then `sum(L)+sum(R)=0`.  The contained block `V` is removed from active support. ∎

## Lemma C11.6: disjoint equal intervals route to SEPARATED_EQUAL

If `U` and `V` are disjoint, the relation is separated-equal or midpoint-adjacent depending on whether the gap is nonempty.

### Proof

Disjoint displayed intervals have form `U G V` or `V G U`.  If `G` is nonempty, the type is `SEPARATED_EQUAL`; if `G` is empty, it is `MIDPOINT_ADJACENT`. ∎

### Verification status

EQUAL_INTERVAL row is verified.

---

## C11.5. SIGNED_INTERVAL and PAIR_DIFFERENCE rows

A signed interval has form

```text
sum(U)-sum(V)+E=0
```

where `E` is supported on one or two boundary atoms.

A pair-difference has form

```text
alpha-beta+P=0.
```

## Lemma C11.7: empty pair-difference collapses to atom equality

If `alpha-beta=0`, then either the two atom labels are identical or the subset contains duplicate atom values.

### Proof

The field equality gives `alpha=beta`.  Since `S` is a subset, distinct atoms cannot share the same value. ∎

## Lemma C11.8: bounded signed corrections route to local or weighted repair

A signed interval or pair-difference relation either:

```text
1. absorbs a boundary atom and becomes ZERO_DEFECT or LOCAL_ZERO_COMPOSITE;
2. uncrosses to EQUAL_INTERVAL;
3. routes to EXTERNAL_COLLISION/BRIDGE_GAP if the correction crosses the active window;
4. routes to WEIGHTED_REPAIR only if a genuine coefficient-2 pattern survives all transported-prefix reductions.
```

### Proof

The correction support has size at most two.  If it is adjacent to an interval, absorb it into the interval.  If two interval representations overlap, uncross them.  If the correction lies outside the active local window, the relation is external/bridge.  If after all cancellations one interval remains doubled, the result is a weighted repair candidate. ∎

### Verification status

SIGNED_INTERVAL and PAIR_DIFFERENCE rows are verified modulo explicit endpoint-sign tables.

Remaining obligation:

```text
List all sign conventions in an appendix table.
```

---

## C11.6. SEPARATED_EQUAL row

A separated-equal branch has form

```text
B G U,
sum(B)=sum(U),
G nonempty.
```

The two finite tests are:

```text
direct exchange: B G U -> U G B;
gap-after move:  B G U -> B U G.
```

## Lemma C11.9: successful gap-after decreases gap

If `B G U -> B U G` produces no new collision, then the active separated gap decreases from `|G|` to `0`.

### Proof

After the move, `B` and `U` are adjacent.  The separating gap is empty. ∎

## Lemma C11.10: gap-after collision routes to verified local rows

Any displayed collision in the gap-after table routes to:

```text
ZERO_DEFECT,
LOCAL_ZERO_COMPOSITE,
EQUAL_INTERVAL,
SIGNED_INTERVAL,
PAIR_DIFFERENCE,
EXTERNAL_COLLISION.
```

The first five are verified above; `EXTERNAL_COLLISION` is handled by the bridge/external verification file.

### Proof

The endpoint equations are the standard gap-after forms:

```text
prefix(U)+tail(B)=0,
G+tail(U)+prefix(Y)=0,
U+tail(B)+prefix(G)=0,
tail(G)+prefix(Y)=0,
B+prefix(G)=prefix(U).
```

These are zero-composite, equal-interval, or external forms. ∎

## Lemma C11.11: direct exchange is finite-budget controlled

The direct exchange table has finitely many displayed moved-family comparisons.  If none succeeds, each failure is classified into a verified local row, external row, or weighted row.

### Proof

There are finitely many moved endpoint families in `B` and `U`.  Pairwise comparison gives a finite displayed collision table.  Each equation is zero/equal/signed/pair/weighted or external. ∎

### Verification status

SEPARATED_EQUAL is verified modulo:

```text
1. explicit D-table endpoint cases;
2. external collision row;
3. weighted row.
```

---

## C11.7. MIDPOINT_ADJACENT row

Adjacent equal blocks have form

```text
B U,
sum(B)=sum(U).
```

For odd `p`, the middle endpoint is the midpoint of the enclosing endpoints.

## Lemma C11.12: midpoint-adjacent branch routes to local rows or success

The midpoint-adjacent row routes to:

```text
ZERO_DEFECT,
EQUAL_INTERVAL,
PAIR_DIFFERENCE,
SIGNED_INTERVAL,
SEPARATED_EQUAL after expansion,
SUCCESS if collision-free.
```

### Proof

Adjacent equal blocks either remain adjacent and give midpoint structure, or an attempted local exchange creates displayed collision algebra.  Degenerate atom-level cases are pair/signed relations. ∎

### Characteristic note

The midpoint interpretation uses odd characteristic.  The strong nonzero-sum proof for `p=2` is direct.

---

## C11.8. Local rank-descent theorem

## Theorem C11.13: non-weighted local rank rows are verified modulo external/weighted rows

The rows

```text
ZERO_DEFECT,
LOCAL_ZERO_COMPOSITE,
EQUAL_INTERVAL,
SIGNED_INTERVAL,
PAIR_DIFFERENCE,
SEPARATED_EQUAL,
MIDPOINT_ADJACENT
```

either:

```text
1. decrease D_SNS^*;
2. decrease local span/gap/support;
3. lower type rank;
4. consume finite transition budget;
5. route to EXTERNAL_COLLISION/BRIDGE_GAP;
6. route to WEIGHTED_REPAIR;
7. reach SNS success or atom/subset contradiction.
```

### Proof

ZERO_DEFECT is Lemma C11.1.  LOCAL_ZERO_COMPOSITE is Lemmas C11.2--C11.3.  EQUAL_INTERVAL is Lemmas C11.4--C11.6.  SIGNED_INTERVAL and PAIR_DIFFERENCE are Lemmas C11.7--C11.8.  SEPARATED_EQUAL is Lemmas C11.9--C11.11.  MIDPOINT_ADJACENT is Lemma C11.12. ∎

---

## C11.9. Remaining obligations after C11

C11 reduces the non-weighted local verification to three remaining categories:

```text
1. EXTERNAL_COLLISION / BRIDGE_GAP rank-descent verification;
2. WEIGHTED_REPAIR rank-descent verification;
3. explicit appendix tables for signs and endpoints.
```

---

## C11.10. Recommended next file

The next file should verify external and bridge/gap rank descent:

```text
docs/final/F00_SNS_C12_external_bridge_rank_descent.md
```

Goal:

```text
Check EXTERNAL_COLLISION and BRIDGE_GAP rows under ARBITRARY-phase zero-defect interpretation.
```

---

## C11.11. Status

```text
Status: local rank-descent verification draft.
Risk: ORANGE.
Remaining gap: external/bridge and weighted row verification.
```
