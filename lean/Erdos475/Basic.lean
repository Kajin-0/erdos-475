/-
Lean skeleton for Erdős 475 / Graham's rearrangement problem.

This file is intentionally a semantic scaffold, not a completed formal proof.
It should compile only after a Lake/mathlib project is added around it and the
necessary imports are selected.

The trusted finite certificate route should eventually formalize:

  * a finite field model, preferably `ZMod p` with `Fact p.Prime`;
  * subset/complement semantics;
  * permutation/order witness semantics;
  * pairwise distinct nonempty partial sums;
  * a theorem that checked JSONL witnesses imply the finite residue statement,
    or a direct generated Lean proof for each finite witness.
-/

namespace Erdos475

/-- Placeholder for a residue class modulo a prime `p`.

A production file should replace this with `ZMod p` and import mathlib. -/
abbrev Residue (p : Nat) := Nat

/-- Nonempty partial sums of an order, reduced modulo `p`.

This definition uses `Nat` placeholders.  It is only a project scaffold. -/
def partialSumsNat (p : Nat) : List Nat -> List Nat
  | [] => []
  | x :: xs =>
      let tail := partialSumsNat p xs
      match tail with
      | [] => [x % p]
      | y :: _ => (x % p) :: tail

/-- Placeholder predicate: `order` is a permutation/listing of the finite set `A`.

In the production formalization, `A` should be a `Finset (ZMod p)` and this should
be stated as `order.toFinset = A` plus nodup. -/
def ListsSetExactly (_p : Nat) (_A : List Nat) (_order : List Nat) : Prop :=
  True

/-- Placeholder predicate: all nonempty partial sums are pairwise distinct. -/
def PairwiseDistinctPartialSums (p : Nat) (order : List Nat) : Prop :=
  (partialSumsNat p order).Nodup

/-- Placeholder Graham-valid ordering predicate. -/
def GrahamValidOrder (p : Nat) (A : List Nat) (order : List Nat) : Prop :=
  ListsSetExactly p A order ∧ PairwiseDistinctPartialSums p order

/-- Placeholder statement for Erdős 475 over a prime modulus. -/
def Erdos475Statement (p : Nat) : Prop :=
  ∀ A : List Nat, ∃ order : List Nat, GrahamValidOrder p A order

/-- Placeholder finite certificate record.

Production version should include:
  * primality proof or prime tag;
  * complement `B`;
  * final ordering of `F_p^* \ B`;
  * canonical-scaling data, if coverage is modulo scaling;
  * proof that the order is valid. -/
structure FiniteWitness where
  p : Nat
  B : List Nat
  finalOrder : List Nat

/-- Placeholder certificate validity predicate. -/
def FiniteWitness.Valid (w : FiniteWitness) : Prop :=
  PairwiseDistinctPartialSums w.p w.finalOrder

/-- Target theorem shape for a single checked witness.

This is deliberately left as `sorry` because the file is a scaffold. -/
theorem witness_implies_valid_order_placeholder (w : FiniteWitness) :
    w.Valid -> PairwiseDistinctPartialSums w.p w.finalOrder := by
  intro h
  exact h

end Erdos475
