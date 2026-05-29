# S57. E1 proper sub-terminal support interval exclusion

This note formalizes E1 from S56.

## Purpose

In the endpoint-zone proof for the moved order

```text
R' = X B z q A Y,
```

we must dispose of zero intervals contained entirely in the terminal support block

```text
B z.
```

The only allowed such interval in the pure terminal branch is the full tautological block

```text
sum(B) + z = 0.
```

Every proper zero sub-block of `B z` either contradicts support minimality or routes to a prior support/terminal branch.

## Setup

Let

```text
B = b_1 b_2 ... b_s
```

be the support block attached to the terminal element `z`, with

```text
b_1 + b_2 + ... + b_s + z = 0.        (1)
```

Assume the terminal support block is chosen minimally in the sense that no proper contiguous sub-block of `B z` already gives an allowed terminal/support zero relation in the residual branch.

The block `B z` in the moved order is:

```text
b_1 b_2 ... b_s z.
```

A contiguous interval contained in `B z` has one of two forms:

```text
Type I:  b_i + b_{i+1} + ... + b_j = 0,              1 <= i <= j <= s.
Type II: b_i + b_{i+1} + ... + b_s + z = 0,          1 <= i <= s.
```

The full terminal tautology is Type II with `i=1`:

```text
b_1 + ... + b_s + z = 0.
```

## Lemma E1

### Statement

Let `I` be a zero interval contained in `B z`.  If `I` is not the full block `B z`, then `I` implies the existence of a proper support zero relation inside `B`:

```text
b_i + ... + b_j = 0
```

or

```text
b_1 + ... + b_{i-1} = 0.
```

Consequently, `I` is incompatible with the pure minimal terminal residual unless the branch has already routed to a support/terminal obstruction.

## Proof

There are two cases.

### Case 1. The interval does not include z

Then the interval has the form

```text
I = b_i + b_{i+1} + ... + b_j = 0,
```

with

```text
1 <= i <= j <= s.
```

This is directly a zero sub-block inside `B`.

If `i=1` and `j=s`, then `sum(B)=0`.  Combining this with (1) gives

```text
z = 0,
```

which is impossible in the usual nonzero sequence setting, or is an immediate degenerate terminal case excluded from the residual branch.

If the interval is proper, it is an internal support collision.  Such a collision is a prior support branch, not a new pure worse-only case.

Thus Type I intervals are excluded from the pure residual.

### Case 2. The interval includes z

Then the interval has the form

```text
I = b_i + b_{i+1} + ... + b_s + z = 0.          (2)
```

If `i=1`, then (2) is exactly the full terminal tautology (1).  This is allowed but ignored because it is not a new obstruction.

Suppose now that `i>1`.  Subtract (2) from (1):

```text
(b_1 + ... + b_s + z) - (b_i + ... + b_s + z) = 0 - 0.
```

Therefore

```text
b_1 + b_2 + ... + b_{i-1} = 0.                 (3)
```

Equation (3) is a proper zero prefix of `B`.  Hence a proper support sub-block is zero.

This is a prior support/terminal obstruction, contradicting the assumption that we remain in the pure minimal terminal residual.

Thus Type II intervals other than the full `B z` tautology are excluded.

## Conclusion

The only zero interval contained in `B z` that can remain in the pure terminal branch is

```text
B + z = 0.
```

All other contained intervals imply a proper support zero relation and are therefore already-routed or excluded.

## Role in Lemma A

In the endpoint-zone enumeration of

```text
X | B | z | q | A | Y,
```

E1 handles the case:

```text
I subset B z.
```

It proves that this case contributes only the tautological class:

```text
tautology_terminal_zB.
```

Therefore any non-tautological interval relevant to hidden-support extraction must cross beyond `B z`, specifically through the separator `z q` into `A` and possibly `Y`.

## Empirical support

The endpoint taxonomy saw exactly this behavior:

```text
p=17: tautology_terminal_zB = 35, no other Bz-contained non-target class.
p=23: tautology_terminal_zB = 59, no other Bz-contained non-target class.
```

## Formal dependency remaining

To use E1 in a final proof, define the support-minimality assumption precisely.  A clean formulation is:

```text
B is chosen as a minimal contiguous support block satisfying sum(B)+z=0.
```

Under that definition, E1 is fully algebraic.
