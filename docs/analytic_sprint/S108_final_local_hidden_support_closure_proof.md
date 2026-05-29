# S108. Final local hidden-support closure proof

This note integrates the two local branch proofs into one final proof-facing closure for the certified pure worse-only `m=3` hidden-support branch.

It combines:

```text
S105: Lemma Z, zero-sum routing final draft
S106: Lemma C, corrected equality tie-break endpoint proof
S107: equality tie-break symbolic gap closure draft
```

The purpose is to give a single local theorem proof that can later be migrated into `proof.tex` or a finite-domain theorem document.

## Safe claim boundary

This note proves only the local certified branch closure:

```text
The pure worse-only m=3 hidden-support branch is certified closed in the analyzed finite domain.
```

It does not prove the full Erdős 475 theorem.  The global theorem still requires:

```text
analytic residue subset certified finite domain.
```

## Local residual form

Let `R` be a certified pure worse-only `m=3` right-terminal residual with local symbolic order:

```text
R = X A z q B Y,
A = A1 A2,
A1 + A2 + z = 0,
sum(B) + z = 0.
```

The branch is called `pure worse-only` because the direct hidden-support localization attempts do not immediately give a base `D_short` descent.

## Defects

The base short defect is:

```text
D_short(R) = (E, L_min, N_min, M),
```

where:

```text
E      = partial-sum collision excess,
L_min  = minimum zero-block length,
N_min  = number of shortest zero blocks,
M      = repeated partial-sum multiplicity profile.
```

For equality branches, define:

```text
D_ref(R) = (D_short(R), S(R)),
```

where `S(R)` is the span gap of the extracted support segment with `q`:

```text
S(R) = span_gap_R({q} union T).
```

Here:

```text
span_gap_R(U) = max_position_R(U) - min_position_R(U) + 1 - |U|.
```

## Lemma A. Hidden-support extraction

The hidden-support extraction reduces every certified pure worse-only residual to exactly one of four families:

```text
1. B_tail + q = 0,
2. B_tail + q + Y_prefix = 0,
3. B_tail + q = A_complement,
4. B_prefix = q.
```

The first two are zero-sum families.  The last two are equality families.

In the current sprint this extraction is certificate-backed in the analyzed records and still requires a publication-grade symbolic extraction proof.

## Lemma Z. Zero-sum routing

If Lemma A returns either:

```text
B_tail + q = 0
```

or:

```text
B_tail + q + Y_prefix = 0,
```

then the residual routes through at least one already-closed branch mechanism:

```text
CLEAN_DESCENT,
SIGNED_INTERVAL,
DISTRIBUTED_BRIDGE,
EXTERNAL_BRIDGE,
TERMINAL_BRIDGE.
```

Therefore the zero-sum families are not primitive obstructions.

### Proof basis

S105 decomposes the proof into:

```text
1. endpoint mapping for Bq/BqY zero relations;
2. exposing-cut existence;
3. endpoint exhaustion into clean, signed, distributed, external, or terminal routes.
```

The endpoint split is:

```text
D_short improves       -> CLEAN_DESCENT,
both endpoints internal -> SIGNED_INTERVAL,
exterior endpoint       -> bridge.
```

Bridge endpoints split exhaustively as:

```text
multiple bridge depths -> DISTRIBUTED_BRIDGE,
single nonterminal     -> EXTERNAL_BRIDGE,
single terminal        -> TERMINAL_BRIDGE.
```

`MIXED` is not primitive; it means at least one closed route flag occurs and can be selected.

### Certified coverage

```text
B_tail+q:
  p=17: 23/23 routed
  p=23: 20/20 routed
  combined: 43/43 routed

B_tail+q+Y_prefix:
  p=17: 8/8 routed
  p=23: 32/32 routed
  combined: 40/40 routed

Total zero-sum:
  83/83 routed
```

Rich witness coverage:

```text
route examples:      24/24
attempt witnesses:   24/24
```

## Lemma C. Corrected equality tie-break

If Lemma A returns either:

```text
B_tail + q = A_complement
```

or:

```text
B_prefix = q,
```

then the residual admits a local move preserving `D_short` and strictly decreasing the relevant support-span gap `S`.

Therefore the equality family descends in:

```text
D_ref = (D_short, S).
```

### Support-tail equality

For:

```text
B_tail + q = A_complement,
```

write:

```text
B = P T M,
T = B_tail.
```

The local orders are:

```text
old:      q | P | T | M,
primary:  P | q | T | M,
fallback: q | T | P | M.
```

In the old order:

```text
S(old) = |P|.
```

Both primary and fallback make `{q} union T` contiguous:

```text
S(primary) = 0,
S(fallback) = 0.
```

If primary is `D_short`-neutral, then:

```text
D_ref(primary) < D_ref(old).
```

If primary is `D_short`-worse, S106-S107 identify the corrected obstruction:

```text
P_suffix + q = 0.
```

The fallback order removes the `P|q` adjacency responsible for this obstruction:

```text
fallback: q | T | P | M.
```

S107 rules out primitive new fallback obstructions at `q|T` or `T|P`; such obstructions either route by Lemma Z/signed-support machinery or are old/non-worsening.

Therefore:

```text
D_short(fallback) = D_short(old),
S(fallback) = 0 < S(old),
D_ref(fallback) < D_ref(old).
```

### Prefix equality

For:

```text
B_prefix = q,
```

let `T=B_prefix` and use the same extracted-segment span gap:

```text
S_prefix = span_gap({q} union T).
```

The certified records are handled by primary-neutral equality tie-break:

```text
p=23: 2/2 records.
```

This is the prefix-normal form of the same refined-defect descent.

### Certified equality coverage

```text
p=17:
  B_tail+q=A_complement: 4/4 tiebroken

p=23:
  B_tail+q=A_complement: 5/5 tiebroken
  B_prefix=q:            2/2 tiebroken

Total equality:
  11/11 tiebroken
```

Primary-failure shape:

```text
primary_failure_rows = 2
rows_with_only_Pq_new_short = 2
rows_with_non_Pq_new_short = 0
```

Fallback cleanliness:

```text
fallback_new_short_total = 0
fallback_new_short_symbols = {}
fallback_new_zone_histogram = {}
```

## Theorem H. Local hidden-support branch closure

### Statement

For every certified pure worse-only `m=3` right-terminal residual satisfying Lemma A, no primitive hidden-support obstruction remains.

More explicitly, the four Lemma A families close as follows:

```text
B_tail + q = 0                  -> zero_sum_routed,
B_tail + q + Y_prefix = 0       -> zero_sum_routed,
B_tail + q = A_complement       -> equality_tiebroken,
B_prefix = q                    -> equality_tiebroken.
```

### Proof

Apply Lemma A.

If the extracted family is:

```text
B_tail + q = 0
```

or:

```text
B_tail + q + Y_prefix = 0,
```

apply Lemma Z.  The residual routes through a closed zero-sum mechanism and is not primitive.

If the extracted family is:

```text
B_tail + q = A_complement
```

or:

```text
B_prefix = q,
```

apply Lemma C.  The residual admits a move preserving `D_short` and strictly decreasing the refined span-gap defect.

The four cases exhaust Lemma A.

Therefore no certified hidden-support residual remains primitive in the analyzed finite domain.

## Certified theorem coverage

Zero-sum:

```text
83/83 routed
```

Equality:

```text
11/11 tiebroken
```

Combined:

```text
94/94 hidden-support records covered
```

## Proof dependencies still requiring publication-grade symbolic form

The local theorem currently depends on certificate-backed lemmas.  The remaining local symbolic work is:

```text
1. Lemma A: prove hidden-support extraction into four families.
2. Lemma Z: complete the endpoint-exhaustion proof without classifier language.
3. Lemma C: formalize the C1-C4 sublemmas from S107.
4. Prove well-foundedness and induction compatibility of D_ref.
```

## Global dependencies outside this local theorem

The full theorem still requires:

```text
1. docs/VERIFIED_DOMAIN.md as a single source of truth.
2. MANIFEST.sha256 for critical artifacts.
3. CI checks for certificate presence/staleness.
4. Analytic residue subset certified finite domain.
5. Claim synchronization across README, proof.tex, theorem notes, and sprint docs.
```

## Safe conclusion

The strongest safe conclusion at this point is:

```text
The pure worse-only m=3 hidden-support branch is certified closed in the analyzed finite domain, with zero-sum routing and corrected equality tie-break coverage.
```

The full Erdős 475 theorem remains conditional on the global analytic residue and verified-domain bridge.

## Status

```text
Final local hidden-support closure proof assembled.
Next recommended repo-level task: create docs/VERIFIED_DOMAIN.md and begin artifact manifest hardening.
```
