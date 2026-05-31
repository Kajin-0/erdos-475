# Analytic Theorem Note: Scalar Absorption Branches

This note packages the scalar branches produced by the singleton blocker templates.

Claim boundary:

```text
This is a local scalar-branch routing theorem note, not a complete proof of Erdős 475.
The global obstruction-tree termination theorem remains open.
```

---

## Purpose

The singleton blocker templates produce scalar branches:

```text
T3 right singleton blocker:
  a,b,-a -> -a,b,a
  scalar branch b=2a.

T4 left singleton blocker:
  -b,a,b -> b,a,-b
  scalar branch a=2b.
```

This note records the scalar absorption repairs for `b=2a` and routes the mirror case `a=2b` by relabeling/reversal.

---

# Scalar branch S1: b=2a

## Setup

The right singleton blocker scalar branch is:

```text
b=2a.
```

The local triple is

```text
a,2a,-a.
```

The forbidden relative value is

```text
a.
```

Original relative partial sums:

```text
a,
3a,
2a.
```

No purely internal permutation of the three-block should be used as a universal interior repair, because relative zero and forbidden-value collisions occur in some permutations.

The correct strategy is scalar absorption: adjoin a neighboring atom if available.

---

## S1-A: right-neighbor absorption

Assume a right neighbor exists after the scalar triple:

```text
c.
```

Use the four-block repair:

```text
a,2a,-a,c
  ->
c,-a,2a,a.
```

The total is preserved:

```text
a+2a-a+c = 2a+c,
```

and

```text
c-a+2a+a = c+2a.
```

New relative partial sums:

```text
c,
c-a,
c+a,
c+2a.
```

### Forbidden value check

The new values hit `a` only if:

```text
c=a        duplicate atom,
c-a=a      c=2a, duplicate atom,
c+a=a      c=0, impossible,
c+2a=a     c=-a, duplicate atom.
```

Thus the forbidden value is avoided for any genuine distinct nonzero right neighbor.

### Internal collision check

Pairwise collisions among

```text
c,
c-a,
c+a,
c+2a
```

force one of:

```text
a=0,
2a=0,
3a=0.
```

For a genuine distinct scalar triple over an odd prime, these do not produce a valid obstruction:

```text
p=3 gives 2a=-a, so the triple is not distinct.
p>=5 gives 3a != 0.
```

Thus the right-neighbor absorption is internally valid in all genuine odd-prime distinct cases.

### External outputs

External collision can occur at:

```text
c,
c-a,
c+a,
c+2a.
```

Using old shorthand, the external targets are:

```text
Left(-c),
Left(a-c),
Left(-a-c),
Left(-2a-c),
Right(-2a),
Right(-3a),
Right(-a),
Right(0).
```

The `Right(0)` branch is impossible because it would be a nonempty zero-sum right interval, hence a repeated partial sum.

All other external outputs are template-aware cancellation states and route to the generic/duplicate interval modules or bridge/gap framework as appropriate.

---

## S1-B: no right neighbor, left neighbor available

Assume the scalar triple is at the right end of the ordering but has a left neighbor:

```text
d.
```

The four-block is

```text
d,a,2a,-a.
```

The forbidden relative value is

```text
d+a.
```

Use the repair:

```text
d,a,2a,-a
  ->
-a,d,a,2a.
```

The total is preserved:

```text
d+a+2a-a = d+2a,
```

and

```text
-a+d+a+2a = d+2a.
```

New relative partial sums:

```text
-a,
d-a,
d,
d+2a.
```

### Forbidden-value check

The new values hit `d+a` only if:

```text
-a = d+a      -> d=-2a,
d-a = d+a     -> 2a=0, impossible for odd p,
d = d+a       -> a=0, impossible,
d+2a = d+a    -> a=0, impossible.
```

So the only forbidden-hit scalar exception is:

```text
d=-2a.
```

### Internal collision check

The new values collide only if:

```text
d=-a        duplicate atom,
d=-3a,
3a=0,
```

besides impossible nonzero cases.

The duplicate case is impossible. The condition `3a=0` degenerates the original triple at `p=3`.

So the only genuine internal scalar exception is:

```text
d=-3a.
```

Therefore, if

```text
d notin {-2a,-3a},
```

the left-neighbor absorption is internally valid and avoids the forbidden value. External failures are template-aware cancellation states involving:

```text
-a,
d-a,
d,
d+2a.
```

---

## S1-C: exceptional left-neighbor case d=-2a

If

```text
d=-2a,
```

the four-block is

```text
-2a,a,2a,-a.
```

Its total is

```text
-2a+a+2a-a=0.
```

If this four-block is strictly interior with a previous nonempty partial sum before it, the total zero would repeat the base partial sum and contradict Graham-validity.

Thus this case can only survive as a beginning-boundary case, where relative zero at the final partial sum of the active block is not automatically a repeated nonempty partial sum.

In the beginning-boundary case, use:

```text
-2a,a,2a,-a
  ->
a,2a,-a,-2a.
```

New partial sums:

```text
a,
3a,
2a,
0.
```

The original forbidden value for this boundary block is

```text
-a.
```

For genuine odd-prime distinct cases, these partial sums are distinct and avoid `-a`, except for small-characteristic degeneracies that already collapse atom distinctness.

---

## S1-D: exceptional left-neighbor case d=-3a

If

```text
d=-3a,
```

the four-block is

```text
-3a,a,2a,-a.
```

The forbidden relative value is

```text
-2a.
```

Use:

```text
-3a,a,2a,-a
  ->
a,2a,-a,-3a.
```

The total is preserved:

```text
-3a+a+2a-a=-a,
```

and

```text
a+2a-a-3a=-a.
```

New relative partial sums:

```text
a,
3a,
2a,
-a.
```

These avoid the forbidden value `-2a` unless one of:

```text
3a=0,
5a=0,
4a=0,
a=0.
```

The `p=3` case degenerates the original triple. In `p=5`, the condition `-3a=2a` means `d` duplicates the local atom `2a`, so the case is impossible in a set. Other odd-prime cases are nondegenerate.

Thus the `d=-3a` branch is resolved in genuine distinct cases.

---

## S1-E: no neighbors

If the scalar triple has no left or right neighbor, then

```text
S={a,2a,-a}.
```

Use the ordering:

```text
-a,a,2a.
```

Nonempty partial sums:

```text
-a,
0,
2a.
```

For genuine odd-prime distinct cases, these are pairwise distinct and avoid the forbidden value `a`.

Again, relative zero is allowed here because the block begins the whole ordering; the empty sum is not one of the nonempty partial sums.

---

## S1 scalar absorption theorem

### Statement

In the scalar branch

```text
b=2a,
```

with local triple

```text
a,2a,-a,
```

every genuine odd-prime distinct case is resolved by one of:

```text
1. right-neighbor absorption if a right neighbor exists;
2. left-neighbor absorption if no right neighbor exists and d notin {-2a,-3a};
3. explicit boundary repair for d=-2a;
4. explicit repair for d=-3a;
5. explicit whole-set ordering if no neighbors exist.
```

Any external failure produced by a successful absorption move is a template-aware cancellation state and routes through the already packaged interval/bridge framework.

Thus the scalar branch `b=2a` introduces no new terminal obstruction type.

---

# Mirror scalar branch S2: a=2b

The left singleton blocker scalar branch is:

```text
a=2b.
```

It is the mirror of S1 under the relabeling

```text
a_S1 = b,
```

so that

```text
2a_S1 = 2b = a.
```

Equivalently, apply reversal and exchange the roles of the left/right singleton blocker templates.

Thus every case above has a mirror:

```text
right-neighbor absorption <-> left-neighbor absorption,
left boundary repair      <-> right boundary repair,
b=2a                     <-> a=2b.
```

The same small-characteristic exclusions apply, with `a` and `b` interchanged.

---

## Scalar Absorption Theorem

### Statement

The scalar branches produced by the singleton blocker templates,

```text
b=2a,
a=2b,
```

introduce no new terminal obstruction class.

Each branch is resolved by scalar absorption, explicit boundary repair, whole-set repair, or routes any remaining external failure to a template-aware cancellation state handled by the interval/bridge framework.

### Proof

The branch `b=2a` is handled by S1-A through S1-E above.

The branch `a=2b` follows by mirror symmetry, reversing the local ordering and relabeling `a_S1=b`.

Thus both scalar branches close. ∎

---

## Significance

This completes packaging of the remaining local scalar branch from the first-blocker system.

The first-blocker local modules now consist of:

```text
T1: right blocker, length >= 2.
T2: left blocker, length >= 2.
T3: right singleton blocker.
T4: left singleton blocker.
GEN-L1 / GEN-R1.
GEN-L>=2 / GEN-R>=2.
DUP-L / DUP-R.
Scalar absorption.
```

All now have durable notes.

---

## Remaining proof work

The next work is global, not local:

```text
1. define a final obstruction-tree state object using template-aware cancellation data;
2. define a well-founded measure that handles:
   - proper subinterval descent,
   - affine/singleton routing,
   - bridge/gap smaller enclosure,
   - further external cancellation recurrence,
   - boundary-sensitive zero cases;
3. prove the global termination theorem;
4. derive conditional endpoint avoidance;
5. apply the bootstrap to Erdős 475.
```
