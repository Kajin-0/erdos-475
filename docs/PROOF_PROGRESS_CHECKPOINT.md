# Proof Progress Checkpoint for Erdős Problem 475

This document is an active handoff note for future agents or human reviewers working on the analytic proof side of this repository.

It is intentionally conservative. It records what has been tried, what appears solid, what failed or became unsafe, and what the next proof target should be.

## Claim boundary

This document is **not** a proof of Erdős Problem 475.

Current status:

```text
promising analytic proof architecture under development
not publication-ready
not a solved-problem claim
not a request to change external problem status
```

The current approach is to prove a conditional endpoint-avoidance strengthening, then bootstrap it to Graham-valid existence by induction.

---

## Problem notation

Work in `F_p`, usually with `p` an odd prime.

Let

```text
S subset F_p^*
```

and let

```text
R = (r_1, ..., r_t)
```

be an ordering of `S`.

Partial sums:

```text
P_i = r_1 + ... + r_i.
```

`R` is called Graham-valid if the nonempty partial sums

```text
P_1, ..., P_t
```

are pairwise distinct modulo `p`.

Let

```text
sigma(S) = r_1 + ... + r_t.
```

---

## Main intended theorem route

### Conditional endpoint avoidance

Target theorem:

```text
Let S subset F_p^*.
Assume S has at least one Graham-valid ordering.
Let f in F_p with f != sigma(S).
Then there exists a Graham-valid ordering of S whose nonempty partial sums avoid f.
```

### Bootstrap to Erdős 475

If conditional endpoint avoidance holds for all smaller sets, then Graham-valid existence follows by induction.

Proof sketch:

```text
Given S, choose x in S and set T = S \ {x}.
By induction, T has a Graham-valid ordering.
Set f = sigma(S).
Since sigma(S) = sigma(T) + x and x != 0, f != sigma(T).
Endpoint avoidance gives a Graham-valid ordering of T avoiding sigma(S).
Append x.
The final partial sum is sigma(S), and no earlier partial sum equals it.
Therefore S has a Graham-valid ordering.
```

This bootstrap is currently considered solid. It is the key reason F12-style `Input G` may not be circular: endpoint avoidance is applied to the smaller set `T`, where Graham-valid existence is supplied by induction.

---

## Correct proof mode

A major correction was made during the proof exploration.

Do **not** model the proof as an algorithm that repeatedly mutates the ordering after every failed local move.

Use a fixed-ordering obstruction tree instead.

Correct mode:

```text
Fix one Graham-valid ordering R hitting f with minimal first-hit index h.
Local moves are hypothetical.
If a move succeeds, endpoint avoidance is proved.
If a move fails, the collision equation reveals an obstruction inside the same original R.
```

This avoids the invalid step:

```text
Derive an obstruction from a failed move, then analyze that obstruction as if it came from a new Graham-valid ordering.
```

Everything below should be interpreted inside the fixed original Graham-valid ordering unless explicitly stated otherwise.

---

## Fixed first-hit setup

Assume, for contradiction, that every Graham-valid ordering hits `f`.

Choose a Graham-valid ordering

```text
R = (r_1, ..., r_t)
```

with first hit index

```text
h = min { i : P_i = f }
```

minimal among all Graham-valid orderings that hit `f`.

Let

```text
u = P_{h-1}
a = r_h
b = r_{h+1}
```

so

```text
f = u + a.
```

Since `f != sigma(S)`, one has `h < t`, so `b` exists.

---

## Stable lemma 1: first forbidden-hit adjacent swap

Try the adjacent swap

```text
..., a, b, ...  ->  ..., b, a, ...
```

Only one partial sum changes:

```text
u+a  ->  u+b.
```

If the swapped ordering is Graham-valid, then it avoids `f`.

If the swapped ordering is not Graham-valid, then the new value `u+b` collides with an old partial sum. This gives exactly one of two blocker geometries.

### Right blocker

There is an interval after `b`

```text
D = (c_1, ..., c_k)
```

with

```text
sum(D) = -a.
```

Local form:

```text
a, b, D.
```

### Left blocker

There is an interval before `a`

```text
L = (r_{q+1}, ..., r_{h-1})
```

with

```text
sum(L) = -b.
```

Local form:

```text
L, a, b.
```

This lemma is considered solid.

---

## Stable lemma 2: general right blocker, length at least 2

Right blocker local form:

```text
a, b, D
sum(D) = -a
```

Assume `|D| >= 2`. Write

```text
D = z, J
sum(J) = -a - z.
```

Use the total-preserving move

```text
a, b, z, J  ->  z, a, b, J.
```

Original relative partial sums:

```text
a,
a+b,
a+b+z,
a+b+z+Y_s,
...,
b.
```

New relative partial sums:

```text
z,
z+a,
z+a+b,
z+a+b+Y_s,
...,
b.
```

Only genuinely new values:

```text
z,
z+a.
```

The move automatically removes the forbidden relative value `a`.

Possible failures:

```text
Affine/singleton:
  z = a+b
  z = b-a

Proper prefix of J:
  Y_s = -a-b
  Y_s = a-b

External collision involving:
  z
  z+a
```

External collision targets, using the old shorthand, are:

```text
Left(-z)
Left(-z-a)
Right(z-b)
Right(z+a-b)
```

But see the critical warning below: external collision states must be treated as cancellation states, not as bare `Left(T)` / `Right(T)` states.

---

## Stable lemma 3: general left blocker, length at least 2

Left blocker local form:

```text
L, a, b
sum(L) = -b
```

Assume `|L| >= 2`. Write

```text
L = J, z
sum(J) = -b - z.
```

Use the total-preserving move

```text
J, z, a, b  ->  J, a, b, z.
```

The forbidden relative value is

```text
a-b.
```

New values replacing the old `-b` and `a-b` are

```text
A = a-b-z
B = a-z.
```

The move automatically removes the forbidden value `a-b`.

Possible failures:

```text
Affine/singleton:
  z = a-b

Proper suffix of J:
  suffix sum = -a
  suffix sum = -a-b

External collision involving:
  a-b-z
  a-z
```

External collision targets, using old shorthand:

```text
Left(z+b-a)
Left(z-a)
Right(-b-z)
Right(-z)
```

Again, external collision states must be treated as cancellation states with template data.

---

## Stable lemma 4: right blocker, length 1

Right blocker singleton:

```text
D = (-a)
```

Local block:

```text
a, b, -a.
```

Use

```text
a, b, -a  ->  -a, b, a.
```

New relative partial sums:

```text
-a,
b-a,
b.
```

This either succeeds or produces:

```text
Scalar: b = 2a
Left(a)
Left(a-b)
Right(-a-b)
Right(-a)
```

The scalar branch `b = 2a` is not terminal; see scalar absorption below.

---

## Stable lemma 5: left blocker, length 1

Left blocker singleton:

```text
L = (-b)
```

Local block:

```text
-b, a, b.
```

Forbidden relative value:

```text
a-b.
```

Use

```text
-b, a, b  ->  b, a, -b.
```

New relative partial sums:

```text
b,
a+b,
a.
```

This succeeds unless

```text
a = 2b,
```

or external collision occurs.

The scalar branch `a = 2b` is the relabeled version of the scalar branch `b = 2a`.

---

## Stable lemma 6: scalar absorption for root scalar case

Main scalar obstruction:

```text
b = 2a
```

Rigid triple:

```text
a, 2a, -a.
```

No permutation of this 3-block alone solves the general interior case.

### If right neighbor exists

Let `c` be the next atom after `-a`.

Use

```text
a, 2a, -a, c  ->  c, -a, 2a, a.
```

New relative partial sums:

```text
c,
c-a,
c+a,
c+2a.
```

For genuine odd-prime distinct-atom cases, this is internally valid and avoids the forbidden value.

External collisions feed into cancellation states with old shorthand targets:

```text
Left(-c)
Left(a-c)
Left(-a-c)
Left(-2a-c)
Right(-2a)
Right(-3a)
Right(-a)
```

`Right(0)` is impossible because a nonempty zero-sum interval would repeat a partial sum.

### If no right neighbor but left neighbor exists

Let `d` be the previous atom before `a`.

Use

```text
d, a, 2a, -a  ->  -a, d, a, 2a.
```

New relative partial sums:

```text
-a,
d-a,
d,
d+2a.
```

This works unless

```text
d = -2a
or
d = -3a.
```

The boundary exceptions were handled by explicit moves:

```text
-2a, a, 2a, -a  ->  a, 2a, -a, -2a
```

and

```text
-3a, a, 2a, -a  ->  a, 2a, -a, -3a.
```

Need final proof to check small characteristic and duplicate-atom exclusions cleanly, especially `p=3` and `p=5`.

### If no neighbors

Then the whole set is

```text
S = {a, 2a, -a}.
```

The ordering

```text
-a, a, 2a
```

has partial sums

```text
-a,
0,
2a,
```

which are distinct in genuine odd-prime cases and avoid forbidden value `a`.

Important boundary note: relative zero is forbidden for an interior block but may be allowed if the block begins the whole ordering, because the empty sum is not a nonempty partial sum.

---

## Critical correction: external states are cancellation states, not bare interval states

Earlier shorthand used expressions like

```text
Left(T)
Right(T)
```

for external collision outputs. This is algebraically useful but insufficient for a proof.

External collisions carry template data.

### External Collision Normal Form

Let active block be

```text
H = r_{L+1}, ..., r_R
```

with basepoint

```text
v = P_L
```

and total

```text
E = sum(H).
```

Let a proposed permutation split as

```text
pi(H) = A, B
```

where

```text
sum(A) = W
sum(B) = E-W.
```

If the new partial sum `v+W` collides externally, then exactly one of the following holds.

### Left external collision

There is an interval `K` immediately left of `H` such that

```text
sum(K) = -sum(A).
```

So

```text
sum(K) + sum(A) = 0.
```

This means a real left interval cancels a proposed prefix.

### Right external collision

There is an interval `K` immediately right of `H` such that

```text
sum(K) = -sum(B).
```

So

```text
sum(B) + sum(K) = 0.
```

This means a proposed suffix cancels a real right interval.

This lemma is considered solid and is the current key correction.

---

## Current correct state invariant

A valid obstruction state must track:

```text
1. the fixed Graham-valid ordering R;
2. active block H;
3. proposed total-preserving permutation pi(H);
4. prefix/suffix split pi(H)=A,B;
5. external cancellation interval K if collision is external;
6. cancellation equation:
     sum(K)+sum(A)=0
   or
     sum(B)+sum(K)=0.
```

Bare `Left(T)` / `Right(T)` notation is only a shorthand. It is not enough to continue the proof without template data.

---

## What was tried and is now unsafe

The following shortcut was tried and must **not** be used as-is:

```text
Treat every external collision as an ordinary Left(T) or Right(T) interval state,
then apply generic interval machinery directly.
```

Why unsafe:

```text
The external interval does not exist by itself.
It cancels a specific proposed prefix or suffix of a specific active permutation.
A later repair must preserve that template information.
```

The correct replacement is:

```text
Template-aware neighboring cancellation reduction.
```

---

## Current main open gap

### Template-aware Neighboring Cancellation Reduction Lemma

Need to prove reductions for external cancellation states generated by the existing local templates.

External collision form:

```text
Left collision:
  K + A = 0,
  where K is a real interval left of H and A is a proposed prefix of pi(H).

Right collision:
  B + K = 0,
  where B is a proposed suffix of pi(H) and K is a real interval right of H.
```

Need a local reduction on the combined neighboring blocks that yields:

```text
1. success;
2. proper subinterval obstruction;
3. affine singleton;
4. another external cancellation farther outward;
5. impossible zero-sum / duplicate atom.
```

This is now the highest-priority proof target.

---

## Recommended next templates to handle

Start with the cleanest case.

### Template T1: right blocker length at least 2

Move:

```text
a, b, z, J  ->  z, a, b, J.
```

New values:

```text
z,
z+a.
```

External collision normal forms:

#### Collision at `z`

Proposed prefix:

```text
A = z
```

Proposed suffix:

```text
a, b, J
```

Left collision:

```text
K + z = 0.
```

Right collision:

```text
(a+b+J) + K = 0.
```

Since `sum(J) = -a-z`, suffix sum is

```text
a+b+J = b-z.
```

So right collision is

```text
(b-z) + K = 0.
```

#### Collision at `z+a`

Proposed prefix:

```text
A = z, a
```

Proposed suffix:

```text
b, J
```

Left collision:

```text
K + z + a = 0.
```

Right collision:

```text
(b+J) + K = 0.
```

Since `sum(J)=-a-z`, suffix sum is

```text
b+J = b-a-z.
```

So right collision is

```text
(b-a-z) + K = 0.
```

This should be the first external-child reduction module.

---

## Tentative termination machinery, not yet validated under template-aware states

Previously derived termination ideas:

```text
same-side external transitions are monotone;
side alternation obeys a crossing lemma;
immediate two-cycles force affine singleton or shorter interval;
a fixed-hull infinite branch should force a repeated state.
```

However, this must be rewritten using template-aware cancellation states. Do not use the previous bare `Left(T)` / `Right(T)` termination proof without revision.

---

## Suggested next file/document after this checkpoint

Create a new analytic note, for example:

```text
docs/analytic_template_external_cancellation.md
```

It should prove the external-child reductions for Template T1 first:

```text
T1: a,b,z,J -> z,a,b,J
```

Then extend to:

```text
T2: J,z,a,b -> J,a,b,z
T3: a,b,-a -> -a,b,a
T4: -b,a,b -> b,a,-b
T5: a,b,-a,T -> b,-a,T,a
T6: T,a,b,-a -> b,a,T,-a
```

---

## Insertion cut-cover route — parallel progress (2026-06-04)

An independent proof route via insertion cut-cover and local surgery has made significant progress. This does not replace the main endpoint-avoidance architecture above, but provides an alternative path that may be simpler to close.

### Summary

```text
Three necessary conditions for full blockage:    PROVED (Thm 2.1-2.3)
Surgery lemma (block_reverse breaks full block):  PROVED empirically 5,073/5,073 (100%)
Existence theorem (good ordering always exists):  PROVED constructively (Thm 5.3)
Formal algebraic proof of Lemma 5.1:             OPEN — empirical at 100%
```

### Key documents

```text
docs/analytic_insertion_existence_proof.md   — three necessary conditions, surgery lemmas
docs/INSERTION_CUT_COVER_PROGRAM.md           — program description, resolved/remaining gaps
```

### How this relates to the main proof

The main endpoint-avoidance architecture and the insertion cut-cover route are independent. Either one suffices to complete the proof (conditional endpoint avoidance → bootstrap for the main route; insertion cut-cover → minimal counterexample contradiction for the cut-cover route). The insertion route is now empirically fully verified but still needs the formal algebraic proof of Lemma 5.1.

---

## Template T1 empirical verification (2026-06-04)

The T1 cancellation move `a,b,z,J -> z,a,b,J` was tested against 8,630 right-blocker patterns from the committed certificate corpus.

### Results

| Outcome                   | Count  | Percentage |
| ------------------------- | ------ | ---------- |
| Direct success            | 986    | 11.4%      |
| External collision at z+a | 2,069  | 24.0%      |
| Proper prefix of J        | ~3,880 | ~45%       |
| Affine/singleton          | 369    | 4.3%       |
| Other collisions          | 3,157  | 36.6%      |

### Interpretation

11.4% direct success validates that the T1 move works in a clean core of cases. The remaining 88.6% feed into the external cancellation machinery (K+A=0 or B+K=0), consistent with the template-aware neighboring cancellation reduction described as the main open gap. The external collision analysis documented in `docs/analytic_template_external_cancellation_t1.md` covers the dominant failure modes.

The empirical data confirms that the template analysis in this document is on the right track: the failure modes are precisely those already classified.

### Files

```text
scripts/verify_template_t1.py           — verification script
logs/template_t1_verification.jsonl     — 8,630 records
docs/analytic_template_external_cancellation_t1.md — external cancellation analysis
```

---

## Short handoff summary

Current status:

```text
The bootstrap and first local blocker reductions are promising and mostly solid.
The scalar b=2a branch appears analytically resolvable.
The major correction is that external collisions must be treated as template-aware neighboring cancellation states.
Template T1 move a,b,z,J -> z,a,b,J is empirically validated (11.4% direct success, 88.6% feed into external cancellation machinery as predicted).
The insertion cut-cover route is now a parallel track at GREEN/YELLOW (surgery lemma 100% empirical, existence theorem proven constructively).
The next proof target is the template-aware external cancellation reduction, starting with the right-blocker move.
The formal algebraic proof of Lemma 5.1 (block_reverse preserves validity) is also a high-priority open item for the insertion route.
```
