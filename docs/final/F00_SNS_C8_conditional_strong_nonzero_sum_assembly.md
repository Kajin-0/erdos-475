# F00.SNS.C8 conditional strong nonzero-sum assembly

This file assembles the current non-circular strong nonzero-sum route.

The earlier endpoint-avoidance extraction exposed a circular input:

```text
Input G: at least one Graham-valid ordering exists.
```

The SNS repair path replaces that with an arbitrary-ordering collision-defect minimization strategy.  The goal is now:

```text
prove strong nonzero-sum for sigma(S) != 0;
derive Erdős 475 by append-one-atom;
then use F12 to strengthen Graham-valid existence to endpoint avoidance.
```

This file does not claim a completed proof.  It states the conditional theorem and names the remaining hardening lemmas exactly.

---

## C8.1. Target theorem

Let `p` be prime and let

```text
S subset F_p^*
```

be finite with

```text
sigma(S) != 0.
```

The strong nonzero-sum theorem asserts that there exists an ordering

```text
R=(r_1,...,r_t)
```

such that the extended partial sums

```text
S_0=0,S_1,...,S_t=sigma(S)
```

are pairwise distinct.

Equivalently, the ordering has no nonempty zero-sum interval.

---

## C8.2. Defect-minimal start

Use the refined collision-defect vector from C1:

```text
D_SNS^*(R)=(P_col(R),L_col^*(R),boundary_rank(R)).
```

where:

```text
P_col(R)=(N_1(R),...,N_t(R));
N_s(R)=number of endpoint collisions of span s;
L_col^*(R)=(t+1-i,t+1-j)
```

for the lexicographically first shortest collision `(i,j)`.

Because `S` is finite, a `D_SNS^*`-minimal ordering exists.

If `P_col(R)=0`, then the ordering is strong nonzero-sum.

If `P_col(R) != 0`, choose the active shortest zero interval

```text
Z=r_{i+1}...r_j,
sum(Z)=0.
```

Since `sigma(S) != 0`, `Z` is not the whole ordering, so an adjacent outside atom `q` exists.

---

## C8.3. q-through-Z repair mechanism

Move the adjacent outside atom `q` into useful interior positions of `Z`.

For a right-adjacent atom:

```text
R=X z_1...z_m q Y,
```

use insertions

```text
R^{(k)}=X z_1...z_k q z_{k+1}...z_m Y,
1<=k<m.
```

Useful insertions destroy the active contiguous zero block `Z`.

The local endpoint formulas are:

```text
E_k={T_0,...,T_k} union {q+T_k,...,q+T_m},
T_s=z_1+...+z_s,
T_m=0.
```

Cross-side collisions have form:

```text
T_a=q+T_b,
```

which gives signed interval data involving `q`.

---

## C8.4. Strongly clean insertion

A useful insertion is strongly clean if it:

```text
1. destroys the active collision interval Z;
2. creates no collision of smaller span;
3. creates no same-span collision at or before the old active location;
4. does not worsen boundary rank.
```

C1 proves:

```text
strongly clean insertion -> D_SNS^* strictly decreases.
```

Thus a defect-minimal ordering cannot admit a strongly clean useful insertion.

---

## C8.5. Obstructed insertion

If no useful insertion is strongly clean, C2 shows that a useful insertion produces one of:

```text
local moved collision;
external moved collision;
signed/equal/pair interval relation;
weighted normal form;
boundary degeneracy.
```

C3--C6 reinterpret these outputs in ARBITRARY phase:

```text
zero intervals are repair defects, not contradictions;
forbidden-hit recurrence is disabled;
collision pullback replaces forbidden recurrence;
weighted outputs are treated as phase-aware repair states.
```

---

## C8.6. Phase-aware state machine

The phase-aware state is

```text
Omega=(R,I,C,E,M,tag,phase),
phase in {ARBITRARY,COLLISION_FREE}.
```

In `ARBITRARY` phase:

```text
zero interval = collision defect;
terminal success = collision-free ordering;
measure = D_SNS^* plus local repair coordinates.
```

In `COLLISION_FREE` phase:

```text
zero interval = contradiction;
strong nonzero-sum has already succeeded.
```

---

## C8.7. Conditional strong nonzero-sum theorem

## Theorem C8.1: conditional strong nonzero-sum assembly

Assume the following hardening lemmas:

```text
H1. Strong-clean insertion descent C1.
H2. q-through-zero-interval obstruction theorem C2.
H3. phase-aware state machine C3.
H4. SNS collision-pullback theorem C4.
H5. phase-aware local/external/bridge descent C5.
H6. phase-aware weighted repair theorem C6.
H7. phase-aware weak cut-rigidity theorem C7.
H8. phase-aware global termination: every ARBITRARY-phase branch either decreases D_SNS^*, reaches COLLISION_FREE, or exits to a smaller weighted/local measure under fixed D_SNS^*.
```

Then strong nonzero-sum holds for every finite `S subset F_p^*` with `sigma(S) != 0`.

### Proof

Choose a `D_SNS^*`-minimal ordering `R`.

If `R` is collision-free, it is a strong nonzero-sum ordering.

Otherwise, let `Z` be the active shortest zero interval.  Since `sigma(S) != 0`, `Z` is not the whole ordering, so choose an adjacent outside atom `q`.

Move `q` into useful interior positions of `Z`.  If some insertion is strongly clean, H1 gives a strictly smaller `D_SNS^*`, contradicting minimality.

If no insertion is strongly clean, H2 produces a local, external, bridge, or weighted repair obstruction.  H3--H7 route every such obstruction inside the phase-aware state machine.  By H8, the branch either reaches `COLLISION_FREE` success, decreases `D_SNS^*`, or terminates by a subordinate well-founded measure.  A decrease of `D_SNS^*` contradicts minimality.  Terminal contradiction can only violate the assumptions `S subset F_p^*`, distinct atom support, or `sigma(S) != 0`; these are fixed assumptions.

Therefore the assumption that `R` has a collision is impossible.  Hence `R` is collision-free and strong nonzero-sum holds. ∎

---

## C8.8. Deriving Erdős 475 from strong nonzero-sum

Once Theorem C8.1 is unconditional, F13 gives Erdős 475.

For any finite `S subset F_p^*`:

```text
if sigma(S) != 0:
  use strong nonzero-sum directly;

if sigma(S)=0 and S nonempty:
  choose x in S;
  T=S\{x};
  sigma(T)=-x != 0;
  order T strongly;
  append x.
```

The appended ordering is Graham-valid because the strong ordering of `T` has extended partial sums distinct and nonzero, and the final appended sum is `0`.

---

## C8.9. Endpoint avoidance after Erdős 475

After Erdős 475 is established, Input G in F12 is resolved.

Then F12 gives the strengthening:

```text
for every f != sigma(S),
there exists a Graham-valid ordering avoiding f.
```

Thus the final theorem order should be:

```text
1. arbitrary-start SNS proof;
2. Erdős 475 by append-one-atom;
3. endpoint avoidance as strengthening.
```

This avoids the circular endpoint-avoidance-first route.

---

## C8.10. Remaining hardening list

The current proof is not complete.  The following items remain open or only sketched.

### R1. C2 useful-insertion obstruction theorem

Need a fully formal proof that if no useful q-insertion is strongly clean, then an insertion creates a routed local/external/weighted obstruction.

### R2. C4 collision pullback in ARBITRARY phase

Need line-by-line endpoint algebra showing every new collision has one of the stated pullback forms without using forbidden recurrence.

### R3. C5 phase-aware local descent

Need formal inequalities showing local zero/equal/signed outputs decrease `D_SNS^*` or a subordinate measure.

### R4. C6 phase-aware weighted repair

Need full replacement of forbidden recurrence in F10/F11 by collision-pullback logic.

### R5. C7 phase-aware weak cut-rigidity

Need hardening of:

```text
C7.2 collision-profile change compensation;
C7.3 first changed endpoint in SNS mode;
C7.4 support/boundary/label diagnostics.
```

### R6. Global phase-aware termination

Need a final well-founded measure combining:

```text
D_SNS^*,
local span/gap/support,
weighted middle length |B|,
type/boundary ranks.
```

The measure must prove no ARBITRARY-phase branch can cycle at fixed collision profile.

---

## C8.11. Current proof status

Current honest status:

```text
The old Input G gap has been replaced by a non-circular SNS repair program.
The SNS program is conditionally assembled but not fully proved.
The remaining bottleneck is no longer merely starting-ordering existence;
it is phase-aware global termination from arbitrary collision-defect repair.
```

No unconditional proof of Erdős 475 has been obtained yet.

---

## C8.12. Recommended next file

The next useful file should attack R6 directly:

```text
docs/final/F00_SNS_C9_phase_aware_global_measure.md
```

Goal:

```text
Define one global well-founded measure for ARBITRARY-phase SNS repair
and map every C1--C7 branch to strict descent or terminal success.
```

---

## C8.13. Status

```text
Status: conditional assembly draft.
Risk: RED/ORANGE.
Main remaining task: phase-aware global measure and hardening R1--R5.
```
