# Analytic Note: T3 Right Singleton Blocker

This note packages the right singleton blocker template from the first forbidden-hit adjacent swap.

Claim boundary:

```text
This is a local template note, not a complete proof of Erdős 475.
The external children of T3 are explicitly classified, but not all are fully reduced here.
```

---

## Parent situation

The first forbidden-hit adjacent swap produced a right blocker of length one.

Local block:

```text
a,b,-a
```

Original relative partial sums:

```text
a,
a+b,
b.
```

The forbidden relative value is

```text
a.
```

The active block total is

```text
E=b.
```

The T3 repair is

```text
a,b,-a  ->  -a,b,a.
```

New relative partial sums:

```text
-a,
b-a,
b.
```

The endpoint `b` is unchanged.

Thus the genuinely new values are

```text
W_1=-a,
W_2=b-a.
```

---

## Internal classification

### Forbidden hits

The new values hit the forbidden value `a` only if

```text
-a = a       -> 2a=0,
b-a = a     -> b=2a.
```

For odd prime `p`, `2a=0` is impossible because `a != 0`.

So the only genuine scalar obstruction is

```text
b=2a.
```

This scalar branch is routed to scalar absorption.

### Zero hits

```text
-a=0        impossible,
b-a=0      -> b=a, duplicate atom.
```

### Internal collisions

```text
-a=b-a     -> b=0, impossible,
-a=b       -> b=-a, duplicate atom because `-a` is already in the block,
b-a=b      -> a=0, impossible.
```

Therefore, outside the scalar branch `b=2a`, the T3 repair is internally Graham-valid and removes the forbidden relative value.

---

## External collision normal forms

Even when internally valid, the T3 repair can fail by external collision involving one of

```text
W_1=-a,
W_2=b-a.
```

Use the template-aware external collision normal form.

---

## External branch at W_1=-a

At

```text
W_1=-a,
```

the proposed permutation splits as

```text
pi(H)=A,B=(-a),(b,a).
```

The prefix has sum

```text
sum(A)=-a.
```

The suffix has sum

```text
sum(B)=a+b.
```

### Left external collision

A left interval `K` immediately before the active block satisfies

```text
sum(K)+sum(A)=0,
```

so

```text
sum(K)=a.
```

Old shorthand:

```text
Left(a).
```

Template-aware meaning:

```text
K + (-a) = 0.
```

### Right external collision

A right interval `K` immediately after the active block satisfies

```text
sum(B)+sum(K)=0,
```

so

```text
sum(K)=-a-b.
```

Old shorthand:

```text
Right(-a-b).
```

Template-aware meaning:

```text
(b,a) + K = 0.
```

---

## External branch at W_2=b-a

At

```text
W_2=b-a,
```

the proposed permutation splits as

```text
pi(H)=A,B=(-a,b),(a).
```

The prefix has sum

```text
sum(A)=b-a.
```

The suffix has sum

```text
sum(B)=a.
```

### Left external collision

A left interval `K` immediately before the active block satisfies

```text
sum(K)=a-b.
```

Old shorthand:

```text
Left(a-b).
```

Template-aware meaning:

```text
K + (-a,b) = 0.
```

### Right external collision

A right interval `K` immediately after the active block satisfies

```text
sum(K)=-a.
```

Old shorthand:

```text
Right(-a).
```

Template-aware meaning:

```text
(a) + K = 0.
```

---

## T3 local theorem

### Statement

For the right singleton blocker template

```text
a,b,-a  ->  -a,b,a,
```

every failure is one of:

```text
1. scalar branch b=2a;
2. template-aware left cancellation K+(-a)=0 with sum(K)=a;
3. template-aware right cancellation (b,a)+K=0 with sum(K)=-a-b;
4. template-aware left cancellation K+(-a,b)=0 with sum(K)=a-b;
5. template-aware right cancellation (a)+K=0 with sum(K)=-a;
6. impossible nonzero or duplicate-atom condition.
```

The scalar branch is already routed to scalar absorption.

The external branches are exactly the four primitive interval labels previously observed:

```text
Left(a),
Left(a-b),
Right(-a-b),
Right(-a),
```

but they must be treated as template-aware cancellation states.

---

## Significance

This note cleanly separates the T3 singleton blocker into:

```text
scalar absorption branch,
four template-aware external cancellation branches.
```

It also corrects the earlier shorthand by recording the exact prefix/suffix pieces canceled in each external branch.

---

## Remaining work for T3

This note does not yet reduce the four T3 external branches through all lengths of the canceling interval.

Needed next:

```text
T3-E1: K+(-a)=0, sum(K)=a.
T3-E2: (b,a)+K=0, sum(K)=-a-b.
T3-E3: K+(-a,b)=0, sum(K)=a-b.
T3-E4: (a)+K=0, sum(K)=-a.
```

Some of these should overlap with T1/T2-style cancellation reductions or scalar absorption, but they need explicit template-aware routing before T3 can be considered fully packaged.

---

## Current status

T3 is locally classified but not globally closed.

The next proof target should be one of:

```text
1. reduce the four T3 external branches explicitly;
2. prove a small singleton-cancellation theorem covering all four at once;
3. route them to T1/T2 or bridge/gap states by a formal lemma.
```
