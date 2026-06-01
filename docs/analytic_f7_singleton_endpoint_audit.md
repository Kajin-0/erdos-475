# Analytic Audit: F7 Singleton-Prefix Endpoint Cases

This note audits the remaining F7 singleton-prefix endpoint flag:

```text
A70 atom-singleton endpoint cases need explicit final text.
```

Claim boundary:

```text
This is an audit note for F7 singleton-prefix recurrence.
It is not a complete proof of Erdős 475.
It does not prove full F9 termination.
```

---

## Source files

Primary source:

```text
docs/analytic_singleton_prefix_recurrence_a70.md
```

Global recurrence theorem:

```text
docs/final/F07_recurrence_routing_theorem.md
```

Related routing notes:

```text
docs/analytic_singleton_routing_theorem.md
docs/analytic_f6_edge_compatibility_audit.md
docs/analytic_fixed_ordering_formalism_lemma.md
```

---

## Singleton-prefix recurrence setup

A singleton-prefix recurrence has a recurrent forbidden hit:

```text
x+B_i=f,
```

where `B_i` is a moved prefix. The atom-singleton case is:

```text
B_i=q,
x+q=f.
```

Let the atom immediately after the recurrent hit be:

```text
b_+.
```

In the general prefix case, write:

```text
B_i = B_i^- b_-
```

where `b_-` is the last atom of `B_i`.

For the atom-singleton case:

```text
b_- = q,
B_i^- = empty.
```

A5 gives a blocker endpoint `j'` satisfying:

```text
S'_{H-1}+b_+ = S'_{j'}.
```

The audit splits by blocker position.

---

## Case 1: left blocker inside B_i

In the atom-singleton case:

```text
B_i=q
```

has no nonempty proper interior before the final atom.

Therefore:

```text
left blocker inside B_i does not exist.
```

Route:

```text
empty case, no obstruction edge.
```

---

## Case 2: left blocker at the base of B_i

A70 gives:

```text
B_i^- + b_+ = 0.
```

For the atom-singleton case:

```text
B_i^- = empty.
```

Thus:

```text
b_+=0.
```

But atoms lie in:

```text
F_p^*.
```

Therefore:

```text
left-base blocker in the atom-singleton case is terminal contradiction.
```

Global class:

```text
CONTRADICTION / ZERO_ATOM.
```

---

## Case 3: left blocker before the base

A70 gives the bridge relation:

```text
L+B_i^-+b_+=0.
```

For the atom-singleton case:

```text
B_i^- = empty,
```

so:

```text
L+b_+=0.
```

Here `L` is a left external bridge ending at the base of the moved singleton.

Route:

```text
F6.1 left external collision / F8 bridge-gap descent.
```

Global classes:

```text
EXTERNAL_COLLISION,
BRIDGE_GAP,
ZERO_COMPOSITE.
```

Measure obligation:

```text
Handled by F6/F8/F9: bridge span/gap/support descent or controlled bridge recurrence.
```

This is not a new singleton endpoint species.

---

## Case 4: right blocker at the immediate next atom

A70 right-blocker formula gives, for a right prefix `C_r` after the recurrent hit:

```text
C_r = b_+ - b_-.
```

If the blocker is at the immediate next atom, then:

```text
C_r=b_+.
```

Therefore:

```text
b_+=b_+-b_-.
```

So:

```text
b_-=0.
```

In the atom-singleton case:

```text
b_-=q.
```

Thus:

```text
q=0,
```

contradicting `q in F_p^*`.

Route:

```text
CONTRADICTION / ZERO_ATOM.
```

---

## Case 5: right blocker inside a proper following prefix

If the right blocker lies inside a proper nontrivial following prefix `C_r`, A70 gives:

```text
C_r = b_+ - b_-.
```

Equivalently:

```text
b_- - b_+ + C_r = 0.
```

For the atom-singleton case:

```text
b_-=q.
```

Thus:

```text
q-b_+ + C_r=0.
```

Route:

```text
PAIR_DIFFERENCE / proper prefix descent.
```

If `C_r` is a proper prefix of the following tail, the support is smaller than the source augmented support, unless it reaches a boundary case already covered below.

Global classes:

```text
PAIR_DIFFERENCE,
TRANSPORTED_PREFIX,
PROPER_SUBINTERVAL.
```

---

## Case 6: right blocker using the full local tail

If the blocker uses the full local tail `C`, A70 gives:

```text
C = b_+ - b_-.
```

Equivalently:

```text
b_- - b_+ + C = 0.
```

For the atom-singleton case:

```text
q-b_+ + C=0.
```

Route:

```text
PAIR_DIFFERENCE boundary.
```

This is not terminal by itself, but it is already one of F7's known recurrence output classes.

Global classes:

```text
PAIR_DIFFERENCE,
BOUNDARY_PAIR,
TRANSPORTED_PREFIX.
```

Measure obligation:

```text
Consumed by pair-difference recurrence routing and then F9.
```

---

## Case 7: right blocker beyond the local tail

If the right blocker lies beyond the local tail, A70 gives:

```text
C+R+b_- - b_+=0,
```

where `R` is the external bridge after the local tail.

For the atom-singleton case:

```text
C+R+q-b_+=0.
```

Route:

```text
F6.3 signed external collision / signed bridge composite.
```

Global classes:

```text
SIGNED_INTERVAL,
PAIR_DIFFERENCE,
BRIDGE_GAP,
EXTERNAL_COLLISION,
WEIGHTED_CORE if required by signed-normal-form routing.
```

Measure obligation:

```text
F6/F8/F10/F11/F9 handle the signed bridge exit.
```

This is not a new singleton endpoint species.

---

## Atom-Singleton Endpoint Audit Lemma

### Statement

In the atom-singleton recurrence case:

```text
x+q=f,
```

every A5 blocker endpoint case routes to one of:

```text
1. impossible zero atom;
2. left bridge zero-composite;
3. proper pair-difference prefix descent;
4. pair-difference boundary branch;
5. right signed bridge composite;
6. F6/F8/F10/F11/F9 global routing.
```

No atom-singleton endpoint case introduces a new recurrence species.

### Proof

The case split above exhausts possible A5 blocker positions relative to the atom `q` and the following tail:

```text
left inside q: impossible empty case;
left at base: b_+=0;
left before base: L+b_+=0;
right immediate: q=0;
right proper prefix: q-b_+ + C_r=0;
right full tail: q-b_+ + C=0;
right beyond tail: C+R+q-b_+=0.
```

Each equation is either terminal contradiction or one of F7's listed output classes. ∎

---

## General singleton-prefix endpoint consequence

For general `B_i` of length at least two, A70 already records:

```text
left inside B_i -> suffix-zero descent;
left at base -> prefix-zero/two-piece zero;
left before base -> bridge zero-composite;
right proper prefix -> pair-difference prefix descent;
right full tail -> pair-difference boundary;
right beyond tail -> bridge signed composite.
```

The only endpoint ambiguity was the atom case where suffixes could become empty. This audit shows the empty-suffix cases become zero-atom contradictions.

---

## Consequence for F7

The F7 audit flag:

```text
A70 atom-singleton endpoint cases need explicit final text.
```

is addressed by this note.

Remaining F7 risks still include:

```text
H1/H2 sign audit,
pair-difference endpoint table,
cyclic-cut midpoint equations,
augmented span convention checks.
```

But the endpoint-branch-specific singleton-prefix gap is now reduced to known F7/F9 classes.

---

## Consequence for endpoint-branch proof program

After this note, the remaining high-level gap for the endpoint-avoidance branch is no longer class coverage. The main remaining gap is:

```text
Full F9 edge-by-edge measure descent proof.
```

---

## Significant status

The endpoint-branch singleton-prefix recurrence gap is now routed.

The proof effort should next focus on the F9 measure audit rather than more local endpoint algebra.
