# F5 separated-equal and midpoint routing theorem

This file continues the final-proof extraction phase.

F5 extracts the separated-equal and midpoint routing machinery used by F4, F8, and F9.  It is mainly backed by:

```text
A36--A48  direct exchange separated-equal table
A49--A54  gap-after separated-equal table
A55       midpoint boundary / adjacent-equal branch
A75--A77  separated bridge recurrence and rigid self-return routing
A98       bridge/gap hardening interface
```

F5 is an extracted draft, not yet the final manuscript version.  The remaining risks are the D/E collision-table endpoint cases and the midpoint characteristic audit.

---

## F5.1. Separated-equal setup

A separated-equal obstruction has displayed form

```text
B G U
```

where:

```text
B, U nonempty;
G may be empty or nonempty depending on the branch;
sum(B)=sum(U).
```

If `G` is empty, the equal blocks are adjacent and the branch is an adjacent-equal / midpoint branch.

If `G` is nonempty, the branch is a separated-equal branch.

The two main moves are:

```text
direct exchange:  B G U -> U G B;
gap-after move:   B G U -> B U G.
```

---

## F5.2. Direct exchange

The direct exchange tests whether the two equal-sum blocks can be swapped across the same gap:

```text
B G U -> U G B.
```

Since `sum(B)=sum(U)`, the total displayed segment sum is preserved.

## Lemma F5.1: direct exchange has only success, collision, or recurrence outcomes

The direct exchange either:

```text
1. gives a Graham-valid ordering avoiding f, hence success;
2. creates a displayed or external collision;
3. gives a Graham-valid ordering with a new forbidden hit, hence recurrence.
```

### Proof

The transformed ordering is either Graham-valid or not.  If Graham-valid, it either avoids `f` or hits `f`.  External collisions are handled by F6; displayed collisions are classified by the direct-exchange table. ∎

---

## F5.3. Direct-exchange collision table

In the direct exchange

```text
B G U -> U G B,
```

the moved endpoint families are those inside `B` and `U`; the gap endpoints and post-segment endpoints are unchanged as total endpoint values.

## Lemma F5.2: displayed direct-exchange collisions route to local non-weighted classes

Every displayed collision from the direct exchange routes to one of:

```text
two-piece zero,
three-piece zero,
equal interval,
signed interval,
pair-difference boundary,
zero collapse,
transported-prefix / weighted-normal-form candidate only if coefficient-2 data survives.
```

### Extracted proof

The direct-exchange collision equations are the D-branches from A36--A48.  After subtracting the colliding endpoint expressions, each equation has one of the schematic forms:

```text
tail(B)+prefix(U)=0,
B_tail+G+U_prefix=0,
U_tail+G+B_prefix=0,
prefix(B)=prefix(U),
B+correction=U+correction.
```

The first three are zero-composite or zero-collapse branches.  Prefix equality gives equal-interval or separated-equal descent after uncrossing.  Boundary-corrected equations give signed interval or pair-difference branches.  If a coefficient-2 pattern survives all transported-prefix and easy reductions, it is passed to F10/F11 as a weighted-core candidate.

External collisions are not part of the displayed table and are handled by F6. ∎

### Audit flags

```text
The final manuscript should include the full D1--D5 table from A36--A48.
The historically risky D2 branch requires explicit endpoint cases.
```

---

## F5.4. Direct-exchange recurrence

A direct exchange can be Graham-valid but recurrent.  In that case a new forbidden hit occurs in a moved block family.

## Lemma F5.3: direct-exchange recurrence routes through F7

Every direct-exchange recurrence is a moved-prefix recurrence and is routed by F7.

### Proof

The only endpoint families whose values change under direct exchange are the moved `B` and `U` prefix families.  Therefore a new forbidden hit must occur in one of those moved families.  Applying the adjacent-blocker lemma gives a recurrence branch of the type handled by F7. ∎

---

## F5.5. Gap-after move

The gap-after move is

```text
B G U -> B U G.
```

It makes the equal blocks adjacent and moves the gap after them.

## Lemma F5.4: successful gap-after move reduces the separated gap

If the gap-after move is Graham-valid and avoids `f`, then the separated-equal gap drops from `|G|` to `0`.

### Proof

Before the move, `G` lies between `B` and `U`.  After the move, the equal-sum blocks are adjacent as `B U`. ∎

---

## F5.6. Gap-after collision table

## Lemma F5.5: displayed gap-after collisions route to local non-weighted classes

Every displayed collision from

```text
B G U -> B U G
```

routes to one of:

```text
two-piece zero,
three-piece zero,
equal interval,
pair-difference boundary,
zero collapse,
external collision handled by F6.
```

### Extracted proof

The gap-after collision equations are the E-branches from A49--A54.  They reduce to forms such as:

```text
prefix(U)+tail(B)=0,
G+tail(U)+prefix(Y)=0,
U+tail(B)+prefix(G)=0,
tail(G)+prefix(Y)=0,
B+prefix(G)=prefix(U).
```

The first four are zero-composite or collapse branches.  The last is an equal-interval or pair-difference branch after uncrossing.  External endpoint collisions are handled by F6. ∎

### Audit flags

```text
The final manuscript should include full E1--E5 endpoint cases.
```

---

## F5.7. Gap-after recurrence and rigid separated return

If the gap-after move is recurrent, F7 applies.  The only non-descending tie is when the A5 blocker pullback reconstructs a separated-equal branch with the same full gap.

## Lemma F5.6: gap-preserving separated recurrence is rigid

If a gap-after recurrence returns to a separated-equal branch with the same gap length, then the old gap `G` is reused with the same endpoints.  The returned branch is either

```text
B G U
```

or

```text
U G B.
```

### Proof

If the recurrent pullback uses a proper prefix or tail of `G`, the gap length decreases.  If it moves either gap endpoint outward, the enclosing span increases or an external bridge is introduced, routed by F6/F8.  Therefore same-gap preservation forces full endpoint alignment. ∎

---

## Lemma F5.7: rigid same-orientation return routes out or descends

A rigid return to

```text
B G U
```

with the same orientation either:

```text
1. uses a proper prefix/tail and decreases support or gap;
2. uses an endpoint and routes to midpoint/adjacent-equal or cyclic recurrence;
3. creates zero collapse inside G;
4. routes through F6/F7/F8.
```

### Proof

Proper-prefix or proper-tail use gives strict support/gap decrease.  Endpoint use either places equal blocks adjacent or crosses the end of the gap, which is midpoint/cyclic/external routing.  A zero interval inside `G` is terminal contradiction. ∎

---

## Lemma F5.8: rigid exchange-orientation return factors through direct exchange

A rigid return to

```text
U G B
```

is exactly the direct-exchange target of the original separated-equal branch.

Therefore it is handled by the direct-exchange trichotomy:

```text
success;
displayed/external collision;
recurrence.
```

### Proof

The exchanged orientation `U G B` is definitionally the direct exchange of `B G U`.  Apply Lemmas F5.1--F5.3. ∎

---

## F5.8. Adjacent-equal and midpoint branch

When `G` is empty, the separated-equal branch becomes adjacent equal blocks:

```text
B U,
sum(B)=sum(U).
```

Over odd characteristic, equality of adjacent block sums is equivalent to a midpoint relation between the endpoints of the combined block.

## Lemma F5.9: adjacent equal blocks route to midpoint or zero-composite machinery

If adjacent nonempty blocks `B,U` have equal sum, then the branch routes to:

```text
midpoint boundary,
zero-composite if one side degenerates,
pair-difference boundary if produced by atom-level swap,
recurrence if the midpoint move hits f,
collapse if an internal zero interval appears.
```

### Proof

Let the endpoint before `B` be `s`.  The endpoint after `B` is `s+b`; the endpoint after `BU` is `s+2b`.  Since `p` is odd, `s+b` is the midpoint of `s` and `s+2b`.  This is the midpoint boundary branch.  Degenerate or atom-level cases reduce to zero-composite or pair-difference branches.  If the transformed midpoint move is recurrent, F7 applies. ∎

### Characteristic audit

This lemma uses division by `2` only in the midpoint interpretation.  The adjacent-equal identity itself is valid in every characteristic.  The final proof handles `p=2` separately in F13.

---

## F5.9. Separated-equal and midpoint routing theorem

## Theorem F5.10: separated-equal/midpoint routing theorem

Every separated-equal or adjacent-equal obstruction routes to one of:

```text
1. success by direct exchange or gap-after move;
2. strict gap/support/span descent;
3. zero-composite/equal/signed interval machinery F4;
4. external collision machinery F6;
5. recurrence machinery F7;
6. bridge/gap descent machinery F8;
7. weighted-core candidate F10/F11 if a genuine coefficient-2 normal form survives;
8. collapse or minimality contradiction.
```

No separated-equal/midpoint branch introduces a new obstruction species.

### Proof

For separated nonempty gap, use direct exchange and gap-after moves.  Direct exchange is Lemmas F5.1--F5.3.  Gap-after move is Lemmas F5.4--F5.6.  Rigid same-gap returns are Lemmas F5.7--F5.8.  For zero gap, use the adjacent-equal/midpoint branch Lemma F5.9.  The listed exits exhaust the success/collision/recurrence trichotomy for the two moves and the gap-preserving recurrence cases. ∎

---

## F5.10. Interface with F9

F5 supplies F9 with the fact that separated-equal and midpoint branches cannot cycle independently:

```text
successful gap-after reduces gap;
proper-gap recurrence reduces gap;
same-gap recurrence is rigid and routes through direct exchange/midpoint/recurrence;
adjacent equal blocks route to midpoint or local descent.
```

---

## F5.11. Remaining extraction risks

Before final manuscript status:

```text
R1. Include full D1--D5 direct-exchange collision table.
R2. Include full E1--E5 gap-after collision table.
R3. Harden D2 equal/separated subbranch.
R4. Check endpoint cases where B, U, or G subpieces become empty.
R5. Check midpoint branch for odd-characteristic assumptions.
R6. Ensure all external collisions point to F6 and all recurrence to F7.
```

---

## F5.12. Extraction status

```text
Status: extracted draft.
Risk: ORANGE.
Next recommended extraction: F3 state machine or F9 non-weighted termination.
```
