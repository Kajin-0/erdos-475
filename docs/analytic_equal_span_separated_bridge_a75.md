# Analytic equal-span separated bridge returns A75

This note continues from A74.

A74 proved bridge-span monotonicity except for one specific tie case:

```text
equal-span separated bridge return.
```

This occurs when a bridge interval `B` outside the source support and an internal/source interval `U` are disjoint, separated by a nonempty gap `G`, and satisfy

```text
sum(B)=sum(U),
```

while the enclosing span does not decrease.

A74 showed this is not a generic bridge problem.  It is a separated-equal interval problem with an additional gap parameter.  This note analyzes that separated-equal return.

The result is partial but sharper: all collision branches route as in A36--A54, and the only remaining non-descending tie is a gap-preserving forbidden recurrence.  Thus the remaining non-weighted global gap becomes a very specific recurrence/gap monotonicity statement.

---

## 1. Standing setup

Let the equal-span bridge return have the form

```text
B G U
```

where:

```text
B = external bridge interval,
G = nonempty gap,
U = internal/source interval,
sum(B)=sum(U)=a.
```

Let

```text
g=sum(G).
```

This is exactly the separated-equal setup with names

```text
A=B,
G=G,
C=U.
```

The enclosing bridge-return span is

```text
span(B G U)=|B|+|G|+|U|.
```

The gap coordinate is

```text
gap_length=|G|.
```

A75 uses the lexicographic bridge-return measure

```text
M_ESB=(enclosing_span, gap_length, support_size, recurrence_depth, boundary_rank).
```

---

# 2. Separated-equal moves available

For

```text
B G U,
sum(B)=sum(U),
```

there are two standard moves from A36--A54:

```text
direct exchange: B G U -> U G B;
gap-after move: B G U -> B U G.
```

A36--A54 routed the displayed collision equations for these moves.

The key new point in A75 is to track `gap_length`.

---

## Lemma A75.1: direct exchange preserves the gap length

The direct exchange

```text
B G U -> U G B
```

keeps the gap block `G` between the equal-sum intervals.  Therefore it preserves

```text
gap_length=|G|.
```

### Proof

The middle block remains `G`.  Only the equal blocks `B` and `U` are exchanged. ∎

### Status

Direct exchange can still be useful because its collisions route to descent/zero-composite classes, but a successful direct exchange does not by itself reduce the separated gap.

---

## Lemma A75.2: gap-after move moves the gap to the right and creates an adjacent equal-block boundary

The gap-after move

```text
B G U -> B U G
```

makes `B` and `U` adjacent.  Thus the separated gap between the equal-sum intervals becomes zero.

### Proof

In the new order, the equal blocks are consecutive as `B U`; the old gap `G` lies after them. ∎

### Consequence

If the gap-after move succeeds, the equal-span separated bridge return leaves the separated-equal class and enters the midpoint/adjacent-equal boundary A55, which is already locally routed modulo A34.

In terms of `M_ESB`, the gap coordinate strictly decreases:

```text
|G| -> 0.
```

---

# 3. Gap-after collision routing decreases class complexity

A49 already routed the gap-after collision equations:

```text
E1: U_k = B_i - a
E2: U_k = a + g + Y_m
E3: G_j = B_i - 2a
E4: G_j = g + Y_m
E5: U_k = a + G_j
```

in generic notation.

In the bridge-return setting, these become:

```text
E1 -> prefix(U)+tail(B)=0;
E2 -> G+tail(U)+prefix(Y)=0;
E3 -> U+tail(B)+prefix(G)=0;
E4 -> tail(G)+prefix(Y)=0;
E5 -> B+prefix(G)=prefix(U).
```

---

## Lemma A75.3: every gap-after collision leaves the equal-span separated bridge class

For an equal-span separated bridge return, any displayed collision of the gap-after move routes to one of:

```text
two-piece zero,
three-piece zero,
equal-interval descent,
zero collapse.
```

Thus it does not return to the same equal-span separated bridge state.

### Proof

This is A49 with `A=B` and `C=U`.  None of the routed forms is again the original separated pair `B G U` with the same gap. ∎

### Measure effect

Each collision branch either collapses or enters zero-composite/equal-interval machinery with strictly lower `type_rank`.  If it later returns to separated-equal, the return is through a bridge branch already measured by A74/A75.

---

# 4. Gap-after forbidden recurrence

The gap-after move can be Graham-valid but still hit the forbidden value.  These forbidden-hit equations have form

```text
x+a+U_k=f,
x+2a+G_j=f.
```

A49 routed these to A34 recurrence.

In A75 terms, this is the only way the gap-after attempt can fail without immediate collision routing.

## Lemma A75.4: non-collision failure of gap-after is forbidden recurrence

If

```text
B G U -> B U G
```

has no Graham collision and does not succeed in avoiding `f`, then it is a forbidden recurrence branch.

### Proof

The transformed ordering is either non-Graham, Graham-valid and avoiding `f`, or Graham-valid and hitting `f`.  The first case is Lemma A75.3; the second succeeds; the third is exactly forbidden recurrence. ∎

---

# 5. Direct exchange collision routing

Direct exchange

```text
B G U -> U G B
```

has D1--D5 collision branches.

A36--A54 show:

```text
D1 -> equal-interval descent / zero collapse;
D2 -> strict descent if m<k, else zero-composite controlled modulo A34;
D3 -> two-piece zero / zero collapse;
D4 -> two-piece zero / zero collapse;
D5 -> strict-span three-piece zero or endpoint two-piece zero.
```

---

## Lemma A75.5: direct-exchange collisions do not preserve the same bridge-return state

Every displayed collision of the direct exchange leaves the original equal-span separated bridge return.  It routes to:

```text
equal-interval descent,
zero-composite surgery,
two-piece zero,
three-piece zero,
zero collapse,
A34 recurrence through D2 zero-composite routing.
```

### Proof

This is the A36--A54 direct-exchange routing table with `A=B` and `C=U`.  D2 can be support-neutral or support-increasing before surgery, but A52--A53 route it to zero-composite surgery modulo A34, not to an unchanged separated bridge state. ∎

---

# 6. Gap monotonicity alternative

For an equal-span separated bridge return, gap-after is the preferred move because it strictly reduces the separated gap if successful.

If gap-after collides, the branch leaves the class by Lemma A75.3.

If gap-after is Graham-valid and avoids `f`, the proof succeeds.

If gap-after is Graham-valid and hits `f`, the only remaining case is forbidden recurrence.

---

## Proposition A75.6: equal-span separated bridge returns reduce gap unless they produce forbidden recurrence

Let

```text
B G U,
sum(B)=sum(U),
G nonempty,
```

be an equal-span separated bridge return.

Apply the gap-after move

```text
B G U -> B U G.
```

Then exactly one of the following occurs:

```text
1. the transformed ordering succeeds;
2. a displayed or external collision occurs and routes out of the equal-span separated bridge class;
3. the transformed ordering is Graham-valid but hits f, giving forbidden recurrence;
4. the separated gap length decreases from |G| to 0, entering the adjacent midpoint boundary if one continues local analysis.
```

In all non-recurrence cases, the bridge-return measure decreases or exits the bridge-return class.

### Proof

Success/collision/forbidden recurrence is exhaustive.  Displayed collisions are Lemma A75.3; external collisions route by A62 and A74.  If the move is collision-free as a block rearrangement, the separated gap between `B` and `U` is zero by Lemma A75.2. ∎

---

# 7. Remaining tie: gap-preserving recurrence

A75 reduces equal-span separated bridge returns to forbidden recurrence from the gap-after move.

This recurrence is not arbitrary: it occurs after a move that would have reduced the gap to zero.  Therefore any transformed A5 blocker produced by A64 should either:

```text
1. have bounded span and descend by A64;
2. cross the old gap G, producing a smaller bridge/equal interval;
3. preserve the old gap only by recreating the same separated-equal pair after a cyclic/external bridge return.
```

The last case is the real tie.

## Definition A75.7: gap-preserving separated recurrence

A gap-preserving separated recurrence is a forbidden recurrence produced by

```text
B G U -> B U G
```

such that subsequent A5 blocker pullback returns to a separated-equal bridge state with the same enclosing span and the same gap length `|G|`.

This is the remaining non-weighted tie after A75.

---

## Lemma A75.8: any non-identical return lowers the bridge-return measure

If the recurrence produced by gap-after returns to a separated-equal bridge state with either:

```text
smaller enclosing span,
smaller gap length,
smaller support size,
or lower boundary rank,
```

then `M_ESB` decreases.

### Proof

This is immediate from the lexicographic definition of `M_ESB`. ∎

---

# 8. Partial theorem for equal-span separated bridge returns

## Theorem A75.9: equal-span separated bridge returns terminate modulo gap-preserving recurrence

Every equal-span separated bridge return either:

```text
1. succeeds;
2. collides and routes to zero-composite/equal-interval machinery;
3. decreases the separated gap to zero and enters midpoint/adjacent-equal routing;
4. produces forbidden recurrence;
5. or enters the gap-preserving separated recurrence tie of Definition A75.7.
```

Thus the only non-weighted bridge tie remaining after A75 is gap-preserving separated recurrence.

### Proof

Apply Proposition A75.6 and Lemma A75.8. ∎

---

# 9. Consequence for global acyclicity

A74 reduced bridge monotonicity to equal-span separated bridge returns.

A75 reduces equal-span separated bridge returns to gap-preserving separated recurrence.

Therefore the remaining non-weighted global acyclicity problem is now:

```text
prove gap-preserving separated recurrence cannot repeat indefinitely.
```

This is narrower than the original A34 recurrence theorem.

---

# 10. Target A76

A76 should attack gap-preserving separated recurrence directly.

Starting point:

```text
B G U -> B U G
```

is Graham-valid and recurrent.

Apply A5 at the new forbidden hit.  Pull the blocker back through the gap-after move.  Show that if the pullback recreates a separated-equal bridge with the same gap, then one of the following must hold:

```text
1. the same endpoints are reused, forcing a cycle of order 2 and hence an earlier hit;
2. the bridge shifts inward, decreasing gap length;
3. a midpoint boundary occurs;
4. a zero-composite appears inside G or at one edge;
5. a cyclic-cut recurrence occurs with smaller bridge span.
```

---

## Current status

Proved here:

1. equal-span separated bridge returns are exactly separated-equal branches;
2. gap-after move reduces the separated gap to zero if successful;
3. gap-after collisions leave the bridge-return class;
4. direct-exchange collisions also leave the unchanged bridge-return state;
5. equal-span separated bridge returns terminate modulo gap-preserving separated recurrence.

Not proved here:

1. gap-preserving separated recurrence elimination;
2. weighted core cut-selection;
3. final endpoint avoidance theorem.
