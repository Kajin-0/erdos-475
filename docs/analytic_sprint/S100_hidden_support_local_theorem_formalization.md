# S100. Hidden-support local theorem formalization

This note converts the S98-S99 branch closure into a proof-facing theorem/lemma package.

The goal is to make the local hidden-support result ready to migrate into a formal proof document while preserving the safe claim boundary:

```text
Local hidden-support branch: certified closed in the analyzed finite domain.
Full Erdős 475 theorem: not closed until the global analytic residue inclusion is proved.
```

## Objects

Let `R` be a certified pure worse-only `m=3` right-terminal residual with local symbolic order

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0.
```

The base defect is

```text
D_short(R) = (E, L_min, N_min, M),
```

where:

```text
E      = partial-sum collision excess,
L_min  = minimum zero-block length,
N_min  = number of zero blocks of length L_min,
M      = repeated partial-sum multiplicity profile.
```

For equality branches, define the refined defect

```text
D_ref(R) = (D_short(R), S_tail(R)).
```

If the extracted support tail is `T`, then

```text
S_tail(R) = span_gap_R({q} union T).
```

Here

```text
span_gap_R(U) = max_position_R(U) - min_position_R(U) + 1 - |U|.
```

Thus `S_tail=0` exactly when `{q} union T` is contiguous.

## Lemma A. Hidden-support extraction

### Statement

Every certified pure worse-only `m=3` right-terminal residual satisfying the above structural hypotheses yields one of the four reduced hidden-support families:

```text
1. B_tail + q = 0,
2. B_tail + q + Y_prefix = 0,
3. B_tail + q = A_complement,
4. B_prefix = q.
```

### Current status

```text
certificate-backed in the analyzed records;
requires symbolic extraction proof for publication-grade closure.
```

### Proof role

Lemma A is the branching lemma.  It reduces the residual to either:

```text
zero-sum family:  cases 1-2,
equality family:  cases 3-4.
```

## Lemma Z. Zero-sum routing

### Statement

If Lemma A returns either zero-sum family

```text
B_tail + q = 0
```

or

```text
B_tail + q + Y_prefix = 0,
```

then the residual triggers at least one already-closed route mechanism:

```text
CLEAN_DESCENT,
SIGNED_INTERVAL,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
terminal bridge.
```

Therefore the zero-sum families are not primitive obstructions.

### Certified evidence

From S97:

```text
Record-level route coverage:
  83/83 routed.

Representative route examples:
  24/24 extracted.

Attempt-level witnesses:
  24/24 matched.
```

Family split:

```text
B_tail+q:
  p=17: 23/23 routed
  p=23: 20/20 routed
  combined: 43/43 routed

B_tail+q+Y_prefix:
  p=17: 8/8 routed
  p=23: 32/32 routed
  combined: 40/40 routed
```

### Proof role

Lemma Z exits the zero-sum branch.  In a symbolic proof, its core should be written as:

```text
Bq_zero or BqY_zero creates a repeated partial-sum relation.
That relation is one of the existing route types.
```

The route types should be defined directly by partial-sum equalities and endpoint positions.

## Lemma C. Corrected equality tie-break

### Statement

Suppose Lemma A returns an equality family:

```text
B_tail + q = A_complement
```

or

```text
B_prefix = q.
```

For the support-tail equality case, write

```text
B = P T M,
T = B_tail.
```

The old local order is

```text
old: q | P | T | M.
```

Consider the two localizations:

```text
primary:  P | q | T | M,
fallback: q | T | P | M.
```

Then at least one localization preserves `D_short` and sends

```text
S_tail -> 0.
```

Therefore the equality branch strictly descends in

```text
D_ref = (D_short, S_tail).
```

### Corrected primary-failure mechanism

The primary localization can fail only by creating a new shortest block of form

```text
P_suffix + q = 0.
```

This supersedes the earlier incorrect hypothesis

```text
T_prefix + q = 0.
```

When the primary move fails, the fallback

```text
q | T | P | M
```

removes the `P|q` adjacency, creates no new shortest block, and satisfies

```text
D_short(fallback) = D_short(old),
S_tail(fallback) = 0 < S_tail(old).
```

### Certified evidence

From S85:

```text
p=17:
  B_tail+q=A_complement: 4/4 tiebroken

p=23:
  B_tail+q=A_complement: 5/5 tiebroken
  B_prefix=q:            2/2 tiebroken

Total:
  11/11 equality records tiebroken.
```

From S84:

```text
primary_failure_rows = 2
rows_with_only_Pq_new_short = 2
rows_with_non_Pq_new_short = 0
```

From S80:

```text
fallback_new_short_total = 0
fallback_new_short_symbols = {}
fallback_new_zone_histogram = {}
```

### Proof role

Lemma C exits the equality branch by refined descent.

## Theorem H. Local hidden-support branch closure

### Statement

For every certified pure worse-only `m=3` right-terminal residual satisfying Lemma A, one of the following occurs:

```text
1. zero-sum route exit;
2. equality refined-defect descent.
```

Equivalently:

```text
B_tail + q = 0                  -> zero_sum_routed,
B_tail + q + Y_prefix = 0       -> zero_sum_routed,
B_tail + q = A_complement       -> equality_tiebroken,
B_prefix = q                    -> equality_tiebroken.
```

Therefore no certified hidden-support residual remains primitive after applying Lemma Z and Lemma C.

### Certified coverage

```text
zero_sum records: 83/83 covered
equality records: 11/11 covered
combined hidden-support records: 94/94 covered
```

### Proof

Apply Lemma A.

If the resulting family is zero-sum, apply Lemma Z.  The residual exits through an already-routed branch mechanism.

If the resulting family is equality, apply Lemma C.  The residual admits a local rearrangement preserving `D_short` and strictly decreasing `S_tail`, hence decreasing `D_ref`.

This exhausts the four Lemma A families.

## Proof insertion outline

A proof document can use the following order:

```text
Definition 1. D_short.
Definition 2. S_tail and D_ref.
Lemma A. Hidden-support extraction.
Lemma Z. Zero-sum routing.
Lemma C. Corrected equality tie-break.
Theorem H. Hidden-support branch closure.
```

## What is fully certified now

```text
Zero-sum branch:
  83/83 routed;
  24/24 route examples;
  24/24 attempt witnesses.

Equality branch:
  11/11 tiebroken;
  2/2 primary failures corrected to P_suffix+q;
  fallback creates no new shortest block.

Combined local branch:
  94/94 covered.
```

## What remains symbolic

The following must still be converted from certificate-backed evidence to symbolic proof:

```text
1. Lemma A extraction into four families.
2. Lemma Z route classification by partial-sum equalities.
3. Lemma C endpoint proof of P_suffix+q-only failure and clean fallback.
4. Well-foundedness and compatibility of D_ref with the induction scheme.
```

## What remains global

The following are outside the local hidden-support theorem:

```text
1. docs/VERIFIED_DOMAIN.md as the single source of truth.
2. MANIFEST.sha256 for critical artifacts.
3. CI checks for certificate presence/staleness.
4. analytic residue subset certified finite domain.
5. claim synchronization across README, proof.tex, and theorem docs.
```

## Safe claim statement

The strongest safe statement after S100 is:

```text
The pure worse-only m=3 hidden-support branch is certified closed in the analyzed finite domain, with complete zero-sum routing and corrected equality tie-break coverage.
```

The full theorem statement remains conditional until:

```text
analytic residue subset certified finite domain
```

is proved and synchronized with the verified artifact ledger.

## Status

```text
Proof-facing hidden-support theorem formalization assembled.
Next recommended step: translate Lemma Z route labels into symbolic partial-sum cases using the 24 rich attempt witnesses.
```
