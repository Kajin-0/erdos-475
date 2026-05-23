# Analytic recurrence theorem attempt A64

This note starts the direct attack on the A34 global recurrence theorem.

A63 identified the main remaining bottleneck as recurrence:

```text
A local move produces a new Graham-valid ordering R'
that still hits the forbidden value f,
and the new first hit is not earlier than the old minimal hit.
```

A34 proposed a global measure.  This note turns that framework into a more concrete recurrence analysis.

The result is partial.  It proves descent in the bounded-blocker cases and isolates the precise remaining tie: a non-earlier recurrence whose new A5 blocker lies outside the support scale of the obstruction that generated the recurrence.

No complete proof is claimed here.

---

## 1. Standing minimal-counterexample setup

Assume endpoint avoidance fails.

Choose a Graham-valid ordering

```text
R=(r_1,...,r_t)
```

with partial sums

```text
S_i=r_1+...+r_i
```

such that

```text
S_h=f
```

and `h` is minimal among all Graham-valid orderings that hit `f`.

Let an active obstruction state be

```text
O=(R,h,type,support,span,pieces,boundary_rank).
```

Use the robust A34 measure

```text
M*(O)=(h, span, pieces, type_rank, boundary_rank).
```

---

## 2. Recurrence event

A local move transforms `R` into a new ordering `R'`.

The recurrence case is:

```text
R' is Graham-valid,
R' hits f,
first_f_hit(R')=h' >= h.
```

If `h'<h`, minimality gives an immediate contradiction.  Thus only `h'>=h` requires work.

Let the move that produced `R'` have active source obstruction support span

```text
s = span(O).
```

The transformed ordering `R'` has a first forbidden hit at index `h'`.

---

# 3. Re-entering the A5 local-blocker framework

If `h'<t`, then the right-adjacent swap at `h'` in `R'` cannot be a successful endpoint-avoiding move.  Since `R'` is Graham-valid and `S'_{h'}=f`, swapping `r'_{h'}` and `r'_{h'+1}` would move the forbidden partial sum away from index `h'`.  If the swap remained Graham-valid and did not create an earlier/new forbidden hit, it would contradict minimality.

The standard A5 obstruction gives a blocker.

---

## Lemma A64.1: every non-final recurrence has an A5 blocker in the transformed ordering

Assume `R'` is Graham-valid, its first forbidden hit is `h'`, and `h'<t`.  Then the right-adjacent swap at `h'` is blocked by a collision.  Hence there exists an index

```text
j' != h'
```

such that

```text
S'_{h'-1}+r'_{h'+1}=S'_{j'}.
```

### Proof

This is A5 applied to the transformed ordering `R'`.  If the adjacent swap were Graham-valid and avoided `f`, it would be a successful endpoint-avoiding ordering.  Since endpoint avoidance is assumed impossible, the swap must be blocked; the displayed equation is exactly the collision criterion for the adjacent swap. ∎

---

## Lemma A64.2: a transformed A5 blocker is a zero-composite obstruction

Let `j'` be an A5 blocker from Lemma A64.1.

If

```text
j'<h',
```

then

```text
sum(j',h'-1] + r'_{h'+1}=0.
```

If

```text
j'>h',
```

then

```text
sum(h',j'] - r'_{h'+1}=0,
```

or equivalently a signed interval/atom obstruction.

### Proof

From

```text
S'_{h'-1}+r'_{h'+1}=S'_{j'}.
```

If `j'<h'`, subtract `S'_{j'}`:

```text
S'_{h'-1}-S'_{j'}+r'_{h'+1}=0,
```

which is `sum(j',h'-1]+r'_{h'+1}=0`.

If `j'>h'`, rearrange:

```text
S'_{j'}-S'_{h'-1}=r'_{h'+1}.
```

The left side is the sum over `(h'-1,j']`, which contains `r'_{h'}` and may be written as a signed interval/atom obstruction relative to `r'_{h'+1}`. ∎

---

# 4. Nearest-blocker normalization

There may be several blockers `j'`.  Choose a nearest blocker:

```text
j_* = argmin_{j' != h'} |j'-h'|.
```

Define the transformed blocker span

```text
b = |j_*-h'|+1.
```

The `+1` includes the adjacent atom `r'_{h'+1}` in the local obstruction scale.

---

## Lemma A64.3: bounded nearest blocker gives recurrence descent

Let `O` be the active obstruction that produced `R'`, with span `s=span(O)`.

If the nearest transformed A5 blocker satisfies

```text
b < s,
```

then the recurrence branch produces a new active obstruction `O'` with

```text
span(O') < span(O).
```

Hence

```text
M*(O') < M*(O)
```

provided the first-hit index coordinate is the same or not larger.

### Proof

By Lemma A64.2, the transformed blocker is a zero-composite/signed-interval obstruction supported inside a window of scale `b`.  Define `O'` to be that blocker obstruction.  If `b<s`, the span coordinate strictly decreases.  The robust measure `M*` is span-first after the first-hit coordinate, so this is descent when `h' = h`.  If `h'>h`, see Lemma A64.5 below for the need to normalize the first-hit coordinate. ∎

### Interpretation

This is the first concrete recurrence descent theorem: recurrence is controlled whenever the new local blocker is shorter than the obstruction that generated the recurrence.

---

# 5. Final-endpoint recurrence

The A5 right-swap blocker requires `h'<t`.  If the transformed first forbidden hit occurs at the final endpoint, then

```text
S'_t=sigma(A).
```

But the endpoint-avoidance target assumes

```text
f != sigma(A).
```

Therefore the final endpoint cannot be the first forbidden hit.

## Lemma A64.4: recurrence hits are non-final

In the endpoint-avoidance setup with `f != sigma(A)`, any forbidden hit in any ordering occurs at an index

```text
h'<t.
```

### Proof

The final partial sum is independent of ordering and equals `sigma(A)`.  Since `f != sigma(A)`, the final partial sum is not `f`. ∎

### Consequence

A5 always applies to a recurrence ordering.

---

# 6. First-hit index normalization

The original minimality choice gives no Graham-valid ordering with first forbidden hit index `<h`.  Therefore any recurrence ordering has

```text
h' >= h.
```

If the global measure uses `h` as its first coordinate with ordinary order, then `h'>h` is not descent even if the obstruction span decreases.

This means the A34 measure must be interpreted carefully.

---

## Lemma A64.5: recurrence descent should be measured at fixed minimal first-hit level

Since `h` is globally minimal, no recurrence branch can have `h'<h`.  Therefore the first coordinate of the recurrence measure should be treated as fixed at the minimal value `h`, and descent should be measured by secondary obstruction complexity among orderings whose first hit is at least `h`.

Equivalently, define the recurrence measure as

```text
M_rec(O)=(span,pieces,type_rank,boundary_rank,h_excess)
```

where

```text
h_excess=h'-h >= 0
```

is placed after the structural coordinates, not before them.

### Proof/Reason

If `h` remains the leading coordinate with ordinary order, then a transformed ordering with `h'>h` and much smaller obstruction support would not count as descent.  But such a branch is structurally simpler and should not be blocked by a later forbidden hit index.  Minimality only forbids `h'<h`; it does not imply that larger `h'` is worse for the obstruction descent.  Thus the first-hit coordinate should be used as a hard lower-bound filter, not as the primary recurrence complexity coordinate. ∎

### Consequence

A64 modifies A34's robust measure for recurrence branches:

```text
M_rec(O)=(span,pieces,type_rank,boundary_rank,h_excess).
```

This is a correction to the earlier A34 ordering.

---

# 7. Main partial recurrence theorem

## Proposition A64.6: bounded-blocker recurrence is controlled

Let a local move from active obstruction `O` produce a Graham-valid ordering `R'` with first forbidden hit `h' >= h`.  Let `j_*` be a nearest A5 blocker for `R'` at `h'`, and let

```text
b=|j_*-h'|+1.
```

If

```text
b < span(O),
```

then the recurrence branch descends under

```text
M_rec=(span,pieces,type_rank,boundary_rank,h_excess).
```

### Proof

By Lemmas A64.1--A64.4, the recurrence produces a transformed A5 blocker.  By Lemma A64.2, that blocker is a zero-composite/signed interval obstruction.  By the nearest-blocker choice, its active support span is at most `b`.  If `b<span(O)`, the span coordinate of `M_rec` strictly decreases. ∎

---

# 8. The remaining tie case

The bounded-blocker theorem leaves the following case:

```text
b >= span(O).
```

This means every A5 blocker for the recurrent transformed ordering lies at distance at least the support scale of the obstruction that generated the recurrence.

Call this a long-blocker recurrence.

## Definition A64.7: long-blocker recurrence

A recurrence branch is a long-blocker recurrence if the transformed ordering `R'` has first forbidden hit `h'` and every A5 blocker `j'` at `h'` satisfies

```text
|j'-h'|+1 >= span(O).
```

where `O` is the active obstruction that produced `R'`.

---

## Lemma A64.8: long-blocker recurrence is the only obstruction to the bounded recurrence theorem

Every recurrence branch either:

```text
1. descends by Proposition A64.6; or
2. is a long-blocker recurrence.
```

### Proof

Immediate dichotomy from whether the nearest blocker span `b` is less than `span(O)` or not. ∎

---

# 9. Structure of long-blocker recurrence

Long-blocker recurrence is not arbitrary.  It says a local move generated a forbidden hit, but all adjacent-swap blockers of that new hit are far away.

This has two important consequences.

## Lemma A64.9: long-blocker recurrence creates a large zero-composite bridge

If `j'<h'` is a long blocker, then

```text
sum(j',h'-1]+r'_{h'+1}=0
```

has support length at least `span(O)`.

If `j'>h'`, the corresponding signed interval/atom obstruction also has support length at least `span(O)`.

### Proof

This is Lemma A64.2 plus the long-blocker inequality. ∎

### Interpretation

The recurrence tie is not a small local obstruction.  It forces a large zero-composite bridge.  This suggests an uncrossing argument: the large bridge should cross or contain the original local support, producing either a smaller overlap obstruction or a separated equal interval already routed.

---

# 10. Target long-blocker uncrossing theorem

The next theorem needed is not a generic recurrence theorem but a specific uncrossing statement.

## Target A64.LB

Let a local obstruction `O` of span `s` produce a recurrence ordering `R'`.  Suppose every transformed A5 blocker at the new first forbidden hit has span at least `s`.

Then the blocker interval must cross the transported image of `support(O)` in such a way that pulling it back to the original ordering produces one of:

```text
1. a proper-overlap equal interval with strict span descent;
2. a two-piece zero composite with strict support descent;
3. a separated equal interval already routed modulo A34;
4. a weighted cut-swap branch with smaller middle block;
5. a contradiction to Graham-validity.
```

This is not proved here.

---

# 11. Consequence for A34

A64 reduces A34.R to a sharper statement:

```text
A34.R = bounded-blocker descent + long-blocker uncrossing.
```

The bounded-blocker part is Proposition A64.6.

The remaining work is A64.LB.

This is progress because the recurrence problem is no longer an abstract measure assertion.  It is now a geometric statement about far A5 blockers crossing the support of the move that created the recurrence.

---

# 12. Target A65

A65 should attack long-blocker uncrossing.

Start with the simplest recurrence source:

```text
atom insertion H1: T_y+q=f.
```

Let the transformed A5 blocker be on the left:

```text
j'<h'.
```

Pull back the blocker zero relation through the atom insertion and compare its interval with the original zero block support.

Expected outcomes:

```text
proper overlap descent,
two-piece zero descent,
pair trap,
forbidden recurrence with smaller span,
or contradiction.
```

---

## Current status

Proved here:

1. every recurrence hit is non-final;
2. every recurrence re-enters A5 and has a transformed blocker;
3. transformed blockers are zero-composite/signed interval obstructions;
4. bounded nearest blockers give strict recurrence descent;
5. the recurrence measure should be span-first with `h_excess` last;
6. the only remaining recurrence tie is long-blocker recurrence.

Not proved here:

1. long-blocker uncrossing;
2. full A34 recurrence theorem;
3. weighted cut-selection theorem;
4. endpoint avoidance theorem.
