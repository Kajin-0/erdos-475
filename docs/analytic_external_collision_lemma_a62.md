# Analytic external-collision lemma A62

This note continues from A61.

Many earlier local moves analyzed collisions only among displayed partial-sum families inside a local segment.  The remaining bookkeeping issue is external collisions: a changed local family may collide with an unchanged partial sum outside the displayed segment.

This note gives a general reduction template for such collisions.

The result is not a complete recurrence theorem.  It shows that external collisions introduce no new algebraic species: they become ordinary interval/signed-interval/zero-composite relations, or they re-enter the transformed-order recurrence framework governed by A34.

---

## Standing setup

Let an ordering be decomposed as

```text
U  W  V
```

where `W` is a displayed local segment on which a block move is performed.  Let

```text
x=sum(U).
```

Suppose a local family inside `W` originally has partial sums

```text
x+F_i
```

and after the move becomes

```text
x+t+F_i.
```

Here `t` is the translation produced by the block move.

An external collision is an equality

```text
x+t+F_i = S_u,
```

where `S_u` is an unchanged partial sum not belonging to the displayed local family being analyzed.

The index `u` may lie:

```text
1. before U ends;
2. inside an unchanged part of W;
3. after W;
4. inside another displayed family already handled separately.
```

Cases of type 4 are not external in practice; they belong to the displayed collision table.  This note addresses cases 1--3.

---

# 1. External collision before the local segment

Assume `S_u` lies before the displayed segment begins.  Then `S_u` is a partial sum inside `U`.

Write

```text
x-S_u = sum(u, start(W)]
```

with the sign convention that this is the sum of the interval from the external endpoint `u` to the start of `W`.

The collision

```text
x+t+F_i=S_u
```

is equivalent to

```text
sum(u,start(W)] + t + F_i = 0.
```

## Lemma A62.1: pre-segment external collisions are zero-composite relations

If a changed local family collides with an external partial sum before the displayed segment, then the collision is equivalent to a zero-composite relation consisting of:

```text
external bridge interval + translation block(s) + local prefix.
```

### Proof

Subtract `S_u` from both sides:

```text
x-S_u + t + F_i=0.
```

The term `x-S_u` is the sum of the bridge interval from the external endpoint to the local base.  The term `t` is itself a sum/difference of blocks moved by the local operation.  Therefore the equality is a zero-composite relation. ∎

### Status

Routed class:

```text
zero-composite / signed interval depending on orientation of t.
```

If `t` is a single block sum or a prefix/tail sum, this routes to A28--A33.  If `t` is a difference of two block sums, it routes to A20 signed-interval geometry and then to the normalized residual classes.

---

# 2. External collision after the local segment

Assume `S_u` lies after the displayed segment.  Let `T` be the total sum of the displayed segment; this total is unchanged by a permutation/block move inside `W`.

Write an after-segment partial sum as

```text
S_u = x + T + H_m,
```

where `H_m` is a prefix of the post-segment tail.

Then the external collision

```text
x+t+F_i = x+T+H_m
```

is equivalent to

```text
t+F_i-T-H_m=0.
```

## Lemma A62.2: post-segment external collisions are signed composite relations

If a changed local family collides with an unchanged post-segment partial sum, then the collision is equivalent to

```text
t + F_i - T - H_m = 0.
```

Equivalently, after replacing `T-F_i` by the complementary tail of the displayed segment when possible, it routes to:

```text
zero-composite,
signed interval,
transported-prefix weighted artifact,
or equal-interval relation.
```

### Proof

Subtract the common base value `x`.  The equality becomes

```text
t+F_i=T+H_m.
```

Move all terms to one side.  If `F_i` is a prefix of the displayed segment under some block decomposition, then `T-F_i` is the corresponding tail plus any moved-block correction.  This gives the stated classes. ∎

### Status

This is the general mechanism behind many earlier equations such as D2, D4, E2, E4, and midpoint post-family collisions.

---

# 3. External collision inside unchanged portions of the displayed segment

Some block moves change only a subfamily while other families inside the same displayed segment remain unchanged.  A collision with one of those unchanged displayed families was usually included in the local table.

If not, it has the form

```text
x+t+F_i=x+G_j+s,
```

where `G_j+s` is an unchanged local family.

## Lemma A62.3: unchanged-displayed collisions are ordinary local table equations

Any collision of a changed family with an unchanged family inside the same displayed segment reduces to

```text
t+F_i=s+G_j.
```

This is exactly the type of equation handled in the local routing tables A36, A49, A55, and A60.

### Proof

Cancel the common base value `x`. ∎

### Status

Such equations should be listed in the local table whenever possible.  If omitted, they are not genuinely external; they should be added to the local branch table.

---

# 4. External collision as equal-interval geometry

The most useful global view is endpoint based.

Let the changed partial sum correspond to an endpoint `r` in the transformed ordering, and let the external unchanged partial sum correspond to endpoint `u`.

A collision

```text
S'_r=S'_u
```

means the interval between endpoints `u` and `r` in the transformed ordering has sum zero.

When pulled back to the original ordering, that interval becomes one of:

```text
1. a contiguous interval;
2. a union of two separated intervals;
3. a signed difference of intervals;
4. a transported-prefix relation.
```

## Lemma A62.4: every external collision pulls back to interval geometry

For any block move preserving the multiset of atoms, a collision between a changed local partial sum and an unchanged external partial sum is equivalent to a zero-sum interval in the transformed ordering.  Pulling this interval back through the block move gives an equal-interval, signed-interval, or zero-composite relation in the original ordering.

### Proof

In the transformed ordering, equality of partial sums is equivalent to the intervening block having total zero.  The inverse block move maps this intervening block to a union/difference of original consecutive blocks.  Such objects are precisely the interval-geometric classes used in A20--A27 and the zero-composite classes used in A28--A33. ∎

---

# 5. External collisions and minimality

If the transformed ordering is not Graham-valid because of an external collision, then the attempted move fails by a collision branch and should be routed by Lemma A62.4.

If the transformed ordering is Graham-valid but hits the forbidden value, then it is not a collision problem.  It is a recurrence problem.

## Lemma A62.5: collision failures and forbidden-hit failures are disjoint branches

For any transformed ordering produced by a local move:

```text
1. if a changed family collides with an external old partial sum, the branch is an interval/composite collision branch;
2. if no collision occurs but the transformed ordering hits f, the branch is a forbidden recurrence branch;
3. if neither occurs, the transformed ordering is a successful endpoint-avoiding move.
```

### Proof

This is an exhaustive trichotomy for the transformed ordering: either the partial sums are not pairwise distinct, or they are pairwise distinct and one equals `f`, or they are pairwise distinct and all avoid `f`. ∎

---

# 6. Routing table

| External event | Algebraic form | Routed class |
|---|---|---|
| changed family hits pre-segment partial sum | bridge + translation + prefix = 0 | zero-composite / signed interval |
| changed family hits post-segment partial sum | translation + prefix = total + post-prefix | signed/composite/equal interval |
| changed family hits unchanged local family | local prefix equation | local routing table |
| transformed ordering valid but hits `f` | forbidden landing | A34 recurrence |
| transformed ordering valid and avoids `f` | none | successful move |

---

# 7. Consequence for previous notes

A62 supplies the missing bookkeeping lemma referenced in:

```text
A55 midpoint external collisions;
A60 weighted cut-swap external collisions;
A61 status update;
separated-equal surgery external transformed collisions.
```

External collisions no longer need to be treated as an unclassified obstruction.  They route into the already developed interval/composite framework, with only the usual A34 recurrence issue left for forbidden landings.

---

# 8. Remaining limitations

A62 is a routing lemma, not a termination theorem.

It does not prove that every external collision descends under the global measure.  It proves only that external collisions belong to known algebraic classes:

```text
equal interval,
signed interval,
zero-composite,
transported-prefix weighted artifact,
A34 recurrence for forbidden landings.
```

Termination still requires:

```text
1. A34 global recurrence theorem;
2. descent/normalization for every interval/composite class;
3. cut-selection for genuine weighted cores.
```

---

# 9. Target A63

After A62, the remaining proof architecture should be summarized in one status note.

A63 should list the current proof obligations as:

```text
1. A34 recurrence theorem;
2. weighted core cut-selection theorem;
3. final descent/termination theorem combining local routing tables;
4. finite verification bridge for small primes / exceptional characteristic cases.
```

This would mark the transition from local algebraic routing to global well-founded descent.

---

## Current status

Proved here:

1. pre-segment external collisions route to zero-composite/signed interval;
2. post-segment external collisions route to signed/composite/equal interval;
3. unchanged-displayed collisions belong in local tables;
4. every external collision pulls back to interval geometry;
5. collision failures and forbidden-hit failures are disjoint branches.

Not proved here:

1. global descent for every external collision;
2. A34 recurrence theorem;
3. weighted cut-selection theorem;
4. endpoint avoidance theorem.
