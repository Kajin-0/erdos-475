# S104. Zero-sum exposing-cut existence lemma

S103 drafted the endpoint mapping lemma:

```text
B_tail + q = 0                  -> signed or bridge endpoint form,
B_tail + q + Y_prefix = 0       -> signed or bridge endpoint form.
```

The remaining local sublemma was:

```text
M3. Exposing-cut existence.
```

This note drafts that sublemma.

## Goal

Show that for every zero-sum hidden-support family

```text
B_tail + q = 0
```

or

```text
B_tail + q + Y_prefix = 0,
```

there is a local candidate move/cut that exposes the repeated partial-sum endpoints from S103 as either:

```text
T_a = q + T_b
```

or:

```text
base + q + T_b = P_e,  e in Ext.
```

Once exposed, S102 gives the route:

```text
CLEAN_DESCENT,
SIGNED_INTERVAL,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
TERMINAL_BRIDGE.
```

## Local geometry

The residual has symbolic order:

```text
R = X A z q B Y.
```

The support block decomposes as:

```text
B = B_prefix B_tail.
```

or, more finely:

```text
B = P T M,
T = extracted support tail.
```

For the zero-sum branch, the extracted relation is one of:

```text
T + q = 0,
T + q + Y_prefix = 0.
```

The issue is that in the raw order, `q` lies before all of `B`:

```text
q B_prefix T M.
```

A move is needed to align `q` with the active interval endpoints used by the signed/bridge classifier.

## Candidate moves

The bridge-move search considers best moves from the hidden-support bridge stage.  Symbolically, these are local rearrangements that place `q` into or next to a support block so that `q` is adjacent to a candidate active interval.

For proof purposes, we need only the following abstraction:

```text
An exposing cut is a cut k in an active shortest interval Z such that inserting q at k places the zero-sum support-tail endpoint on one side of q and the complementary active/exterior endpoint on the other side.
```

In classifier notation, the move produces one of:

```text
new_order = Z_prefix(k) q Z_suffix(k)
```

or the left-reversal analogue.

## Lemma M3. Exposing-cut existence

### Statement

Let `R` be a certified pure worse-only `m=3` right-terminal residual in a zero-sum hidden-support family.

If:

```text
B_tail + q = 0
```

or:

```text
B_tail + q + Y_prefix = 0,
```

then at least one best hidden-support bridge move exposes the zero-sum relation to the active-window classifier.  Equivalently, there exists an active shortest interval `Z` and insertion cut `k` such that either:

```text
1. D_short(new_order(k)) < D_short(old_order),
```

or the zero-sum relation appears as:

```text
2. T_a = q + T_b,
```

or:

```text
3. base + q + T_b = P_e, e in Ext.
```

### Certified evidence

This is exactly what the rich zero-sum route certificate verifies at record level:

```text
B_tail+q:
  p=17: 23/23 route_success=yes
  p=23: 20/20 route_success=yes
  combined: 43/43

B_tail+q+Y_prefix:
  p=17: 8/8 route_success=yes
  p=23: 32/32 route_success=yes
  combined: 40/40
```

Total:

```text
83/83 zero-sum records expose a route.
```

The rich attempt witness layer further verifies:

```text
24/24 representative route examples have matched route objects,
24/24 representative route examples have matched attempts.
```

Thus there is no remaining empirical exposing-cut gap in the certified domain.

## Proof intuition

The zero-sum relation contains `q` plus a terminal segment of support:

```text
q + T = 0
```

or:

```text
q + T + Y_prefix = 0.
```

The hidden-support bridge moves are generated precisely by moving `q` across candidate support windows.  Since the relation includes `q`, placing `q` at a cut adjacent to the extracted support tail exposes the zero-sum interval endpoint.

There are only two endpoint outcomes:

```text
1. both endpoints are active-window endpoints;
2. one endpoint is exterior.
```

The first gives signed form:

```text
T_a = q + T_b.
```

The second gives bridge form:

```text
base + q + T_b = P_e.
```

If the move already lowers `D_short`, the case exits by clean descent before endpoint classification is needed.

## Bq_zero exposing cut

For:

```text
B_tail + q = 0,
```

choose the cut that places `q` immediately before or inside the active representation of `B_tail`.

The exposed interval has sum:

```text
q + B_tail = 0.
```

If the two interval endpoints lie inside the active window, this is:

```text
T_a = q + T_b.
```

If the far endpoint of `B_tail` is represented by an exterior partial sum, this is:

```text
base + q + T_b = P_e.
```

Thus Bq_zero is exposed as signed or bridge unless the move is already a clean descent.

## BqY_zero exposing cut

For:

```text
B_tail + q + Y_prefix = 0,
```

choose the cut that places `q` adjacent to the active representation of `B_tail`, while the endpoint after `Y_prefix` is treated as right exterior unless it collapses internally.

The exposed interval has sum:

```text
q + B_tail + Y_prefix = 0.
```

If `Y_prefix` is externally visible, the endpoint after `Y_prefix` is an exterior partial sum:

```text
P_e, e in Ext.
```

so the relation becomes:

```text
base + q + T_b = P_e.
```

If the `Y_prefix` contribution is empty or absorbed into the active window, the relation is internal and becomes signed:

```text
T_a = q + T_b.
```

Thus BqY_zero is exposed as signed or bridge unless the move is already a clean descent.

## Connection to route labels

Once the exposing cut exists, the S102 endpoint split applies:

```text
clean descent        -> CLEAN_DESCENT,
internal endpoints   -> SIGNED_INTERVAL,
multiple bridge b    -> DISTRIBUTED_BRIDGE,
single nonterminal b -> EXTERNAL_BRIDGE,
single terminal b    -> TERMINAL_BRIDGE.
```

If multiple route flags occur simultaneously, the label is:

```text
MIXED,
```

and any closed route flag may be selected.

## Certificate alignment

The exposing-cut lemma is reflected directly in the route producer:

```text
route_success = bool(useful_route_flags)
```

The rich route rerun gave:

```text
route_success_by_family:
  B_tail+q:          yes 43/43
  B_tail+q+Y_prefix: yes 40/40
```

Thus every certified zero-sum record has at least one exposing move with a useful route flag.

## Remaining formal details

For publication-grade proof, the following still need to be written without computational language:

```text
1. Define the admissible hidden-support bridge moves symbolically.
2. Show that the support-tail endpoint determines an admissible cut k.
3. Show that the selected cut exposes q+B_tail or q+B_tail+Y_prefix as an active or active-exterior endpoint equality.
4. Show that the classifier endpoint split is exhaustive.
```

S102 and S103 cover items 3-4 at proof-skeleton level.  This note supplies the symbolic target for item 2.

## Status

```text
Exposing-cut existence lemma drafted.
Zero-sum Lemma Z now decomposes into:
  M1/M2 endpoint mapping,
  M3 exposing-cut existence,
  S102 endpoint exhaustion.
```
