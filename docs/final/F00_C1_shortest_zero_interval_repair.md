# F00.C1 shortest zero-interval defect repair

This file continues the repair of the starting-ordering gap identified in F00.

F00 reduced the circular Input G problem to one sharper missing theorem:

```text
F00.C1 shortest zero-interval defect repair.
```

The issue is simple but fundamental.  In the previous obstruction engine, a nonempty zero interval is a contradiction only after the ordering is already Graham-valid.  In an arbitrary starting ordering, a zero interval is not a contradiction; it is the defect that must be repaired.

This file attacks that repair problem.

Status: repair draft, not complete proof.

---

## C1.1. Setup

Let

```text
R=(r_1,...,r_t)
```

be a defect-minimal ordering under the F00 defect vector.

Assume the first active defect is a shortest collision:

```text
S_i=S_j,
0<=i<j<=t.
```

Let

```text
Z=r_{i+1}...r_j.
```

Then

```text
sum(Z)=0.
```

By shortest-span minimality, `Z` has no proper nonempty zero subinterval.

Write

```text
Z=z_1 z_2 ... z_m,
m=j-i>=1.
```

Thus:

```text
z_1+...+z_m=0,
```

and every proper nonempty interval of `Z` has nonzero sum.

---

## C1.2. Immediate cases

## Lemma C1.1: singleton zero interval is impossible

If `m=1`, then `z_1=0`, contradicting `S subset F_p^*`.

### Proof

`sum(Z)=z_1=0`, but every atom lies in `F_p^*`. ∎

Thus the shortest zero interval has length

```text
m>=2.
```

---

## Lemma C1.2: whole-ordering zero interval is the zero-total case

If `Z` is the whole ordering, then

```text
sigma(S)=0.
```

### Proof

The sum of the whole ordering is `sigma(S)`, and `sum(Z)=0`. ∎

### Consequence

The full-ordering zero-total case cannot be repaired by choosing an outside atom adjacent to `Z`, because no outside atom exists.  It must be handled separately, probably by the append-one-atom reduction used in F13 after proving the nonzero-total strong theorem.

This file focuses first on the non-full case.

---

## C1.3. Choose an outside adjacent atom

Assume `Z` is not the whole ordering.  Then at least one adjacent outside atom exists:

```text
left atom  q_L = r_i       if i>=1,
right atom q_R = r_{j+1}   if j<t.
```

Choose one adjacent outside atom `q`.  For definiteness, suppose a right adjacent atom exists:

```text
R = X Z q Y.
```

The left-adjacent case is symmetric:

```text
R = X q Z Y.
```

Since `q in F_p^*`,

```text
q != 0.
```

---

## C1.4. Moving q through Z

Consider moving `q` leftward through `Z` one adjacent swap at a time:

```text
X z_1 z_2 ... z_m q Y
X z_1 z_2 ... z_{m-1} q z_m Y
X z_1 z_2 ... q z_{m-1} z_m Y
...
X q z_1 z_2 ... z_m Y.
```

Let the state after moving `q` left across the suffix

```text
z_{k+1}...z_m
```

be denoted `R_k`, so:

```text
R_m = X Z q Y,
R_0 = X q Z Y.
```

The total sum of the block `Z q` is always

```text
q.
```

The internal zero interval `Z` is destroyed as a contiguous block except at the initial and final positions where the original `Z` remains contiguous after or before `q`.

---

## C1.5. Prefix-sum effect of inserting q into Z

Place `q` after the prefix

```text
Z_k=z_1...z_k.
```

The local block becomes

```text
z_1...z_k q z_{k+1}...z_m.
```

Relative to the basepoint before `Z`, the internal endpoints are:

```text
T_0=0,
T_1,...,T_k,
T_k+q,
T_k+q+z_{k+1},
...,
T_k+q+z_{k+1}+...+z_m.
```

Since

```text
z_{k+1}+...+z_m = -T_k,
```

the final endpoint after `Z q` is

```text
q.
```

The old zero endpoint after `Z` at value `0` is replaced, inside the local block, by endpoint values shifted by `q` on the suffix side.

---

## Lemma C1.3: internal collisions during q-insertion produce handled obstructions

If inserting `q` into `Z` creates an internal collision inside the displayed block `Z q`, then the collision gives one of:

```text
proper zero subinterval of Z;
zero interval containing q;
equal interval between a prefix and shifted suffix;
pair-difference relation involving q;
```

and hence enters the F3 state machine through F4/F5/F7.

### Proof

Every internal collision is equality of two local endpoint expressions from C1.5.  If both endpoints lie on the old `Z` side, the collision is a proper zero subinterval of `Z`, impossible by shortestness unless it is the whole `Z`.  If one endpoint lies before `q` and the other after `q`, subtracting gives an interval relation containing `q` and a suffix/prefix of `Z`.  This is a zero-composite or pair-difference/signed interval with bounded atom correction `q`.  If both endpoints lie on the shifted suffix side, subtracting cancels `q` and gives a proper zero subinterval of `Z`. ∎

---

## Lemma C1.4: external collisions during q-insertion enter F6/F8

If inserting `q` into `Z` creates a collision with an endpoint outside the local block `Z q`, then it is an external collision in the sense of F6 and routes through F6/F8.

### Proof

The local move replaces one ordering of the same atom window `Z q` by another.  Any collision with an endpoint in `X` or `Y`, or with an unchanged displayed endpoint outside the moving window, is exactly an external collision.  F6 applies. ∎

---

## C1.6. Forbidden hits during q-insertion

If an intermediate insertion of `q` into `Z` is collision-free but creates a forbidden endpoint `f`, then the ordering is Graham-valid up to the local collision defect repair and enters the recurrence machinery.

## Lemma C1.5: forbidden hits during q-insertion route to F7

A forbidden hit created during the movement of `q` through `Z` is a moved-prefix recurrence and routes through F7.

### Proof

Only endpoints in the moving local window change.  A new forbidden hit must occur at one of these moved endpoint values.  Applying the adjacent blocker lemma produces a recurrence branch.  By construction the move is an adjacent atom insertion/swap, hence it is one of the recurrence sources routed by F7. ∎

---

## C1.7. The desired repair conclusion

If there exists an insertion position for `q` inside `Z` such that:

```text
1. no internal collision occurs;
2. no external collision occurs;
3. no forbidden hit occurs;
```

then the local ordering has repaired the active zero interval `Z`.

The defect vector improves if the total number of collisions decreases, or if the same number of collisions remains but the shortest collision span increases.

---

## Lemma C1.6: clean q-insertion improves the shortest collision defect unless another shortest collision remains elsewhere

If inserting `q` into `Z` destroys the zero interval `Z` and creates no new collision involving the local window, then either:

```text
1. collision_count decreases; or
2. another shortest collision of the same span exists outside the local window.
```

### Proof

The selected collision `S_i=S_j` corresponding to `Z` no longer exists as the same contiguous zero interval because `q` interrupts `Z`.  By hypothesis, no new collision involving the local window is created.  All collisions entirely outside the local window are unchanged.  Therefore either the total number of collisions decreases, or an unchanged collision elsewhere remains with the same minimal span. ∎

### Problem

The second alternative prevents immediate contradiction to defect minimality unless the defect vector also tracks the location or multiplicity of shortest collisions more finely.

---

## C1.8. Strengthened defect vector needed

To make Lemma C1.6 usable, refine the defect vector from F00.

Replace

```text
collision_count,
first_collision_span
```

with a sorted multiset of collision spans or with:

```text
N_minspan = number of collisions attaining the minimum collision span.
```

A stronger vector is:

```text
D^+(R)=(
  min_collision_span,
  N_minspan,
  total_collision_count,
  first_forbidden_index,
  active_defect_span,
  active_defect_type_rank,
  boundary_rank
).
```

But this must be ordered carefully.  To prefer eliminating shortest collisions, use:

```text
D^+(R)=(
  min_collision_span,
  -N_minspan,
  total_collision_count,
  ...
)
```

is not allowed in nonnegative lexicographic descent.  Instead use:

```text
D^+(R)=(
  t+1-min_collision_span,
  N_minspan,
  total_collision_count,
  ...
)
```

so increasing the shortest collision span decreases the first coordinate.

---

## Lemma C1.7: refined defect vector can detect shortest-collision repair

With

```text
D^+(R)=(t+1-min_collision_span, N_minspan, total_collision_count, ...),
```

any clean q-insertion that destroys one shortest collision and creates no new collision of the same or smaller span decreases `D^+(R)`.

### Proof

If the minimum collision span increases, then `t+1-min_collision_span` decreases.  If the minimum span is unchanged but one selected shortest collision is removed and no new same-span collision is created, then `N_minspan` decreases.  If all shortest-span counts are unchanged but a longer collision is removed, then `total_collision_count` decreases. ∎

---

## C1.9. All q-insertions obstructed

The hard case is when every insertion position of `q` through `Z` is obstructed by:

```text
internal collision;
external collision;
forbidden hit;
no defect decrease.
```

Internal collisions route to F4/F5/F7 by Lemma C1.3.  External collisions route to F6/F8 by Lemma C1.4.  Forbidden hits route to F7 by Lemma C1.5.

The only not-yet-controlled obstruction is:

```text
clean insertion but no defect decrease because another shortest collision remains elsewhere.
```

This suggests the defect-minimality argument should choose not merely one shortest zero interval, but a lexicographically earliest shortest zero interval, and move an adjacent atom so that the location of the first shortest collision improves.

---

## C1.10. Location refinement

Define collision intervals by pairs `(i,j)`.  Order them lexicographically by:

```text
span=j-i,
left endpoint i,
right endpoint j.
```

Let the active collision be the lexicographically first shortest collision.

Add to the defect vector:

```text
active_collision_left=i,
active_collision_right=j.
```

or transformed nonnegative coordinates:

```text
i,
j.
```

Then cleanly destroying the active collision while creating no earlier/equal collision improves the defect vector.

---

## Needed Lemma C1.8: clean q-insertion does not create earlier shortest collision

For the location-refined defect vector, a clean insertion of adjacent `q` into the active shortest zero interval `Z` should not create an earlier shortest collision unless that collision involves the local window.  But local-window collisions were excluded by cleanliness.

### Status

Plausible but not fully proved.  This is now the main technical sublemma for completing F00.C1.

---

## C1.11. Candidate repair theorem

## Theorem C1.9: shortest zero-interval repair, conditional form

Assume the location-refined defect vector and Lemma C1.8.  Let `R` be a defect-minimal ordering with active shortest zero interval `Z` that is not the whole ordering.  Then moving an adjacent outside atom `q` through `Z` either:

```text
1. decreases the refined defect vector;
2. creates an internal obstruction routed by F4/F5/F7;
3. creates an external obstruction routed by F6/F8;
4. creates a recurrence routed by F7;
5. reaches endpoint avoidance.
```

### Proof

Move `q` through all insertion positions in `Z`.  If any insertion is clean, Lemmas C1.7 and C1.8 give defect decrease.  If none is clean, each failed insertion is obstructed.  Internal collisions are Lemma C1.3, external collisions are Lemma C1.4, and forbidden hits are Lemma C1.5. ∎

---

## C1.12. Full-ordering zero-total case

If the active shortest zero interval is the entire ordering, then

```text
sigma(S)=0.
```

For Erdős 475, F13 handles zero-total sets by removing one atom:

```text
T=S\{x},
sigma(T)=-x != 0.
```

Thus a proof of strong nonzero-sum for nonzero-total subsets would imply Erdős 475 for zero-total subsets by appending `x`.

For endpoint avoidance, the full-ordering zero-total case is subtler because the forbidden value `f` may be nonzero and endpoint avoidance is stronger than Graham-validity.

Potential route:

```text
First prove strong nonzero-sum for sigma != 0 by defect repair.
Then use F12 as a conditional strengthening theorem once Graham-valid existence is obtained.
```

This suggests the arbitrary-ordering repair should target strong nonzero-sum first, not full endpoint avoidance.

---

## C1.13. Revised strategic conclusion

The cleanest non-circular path now appears to be:

```text
1. Prove strong nonzero-sum for sigma(S) != 0 using arbitrary-ordering collision-defect minimization.
2. Derive Erdős 475 by the F13 append-one-atom reduction.
3. Then use F12 to strengthen Graham-valid existence to endpoint avoidance.
```

This avoids needing to prove endpoint avoidance directly from arbitrary orderings.

---

## C1.14. Current status

F00.C1 is not fully proved yet.

Progress made:

```text
1. shortest zero interval has no internal zero subinterval;
2. q-through-Z insertion gives explicit endpoint formulas;
3. internal collisions route to F4/F5/F7;
4. external collisions route to F6/F8;
5. forbidden hits route to F7;
6. clean q-insertion requires refined defect-vector bookkeeping;
7. full-ordering zero-total case suggests proving strong nonzero-sum first.
```

Remaining open sublemma:

```text
C1.8 clean q-insertion does not create earlier shortest collision under location-refined defect order.
```

Strategic remaining gap:

```text
Decide whether to prove endpoint avoidance directly or first prove strong nonzero-sum.
```

---

## C1.15. Recommended next file

The next file should pivot to the strong nonzero-sum version:

```text
docs/final/F00_SNS_arbitrary_collision_defect.md
```

Goal:

```text
Prove or formulate strong nonzero-sum from arbitrary-ordering collision-defect minimization for sigma(S) != 0.
```

This may be the non-circular route into Erdős 475.

---

## C1.16. Status

```text
Status: repair draft.
Risk: RED.
Main result: Input G reduced further to location-refined shortest zero-interval repair, and strategy suggests proving strong nonzero-sum first.
```
