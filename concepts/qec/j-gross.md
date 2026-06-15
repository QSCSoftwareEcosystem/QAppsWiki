---
type: concept
name: Clifford-group spin code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-representation
- concepts/qec/qubit-permutation-invariant
- concepts/qec/single-spin
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/j_gross
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: j_gross
---

# Clifford-group spin code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/j_gross) (`code_id: j_gross`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A single-spin code designed to realize a discrete group of gates using $SU(2)$ rotations.
Codewords are subspaces of a spin's Hilbert space that house irreducible representations (irreps) of a discrete subgroup of $SU(2)$.

The first realization  ([arXiv:2005.10910](https://arxiv.org/abs/2005.10910)) used the single-qubit Clifford group (effectively, the binary octahedral, or $2O$ subgroup of $SU(2)$).
Code construction is done by restricting the $SU(2)$ irrep to $2O$, and determining the carrier spaces of any nontrivial irreps of $2O$. Since irreps of $2O$ do not appear in integer spins, half-integer spins are used.

A simple example of a codespace is a projection onto an instance of a particular irrep of $2O$, referred to as either $ \varrho_4 $ or $ \varrho_5 $.
In the case of only one instance of the desired irrep present in the spin, the projection is created as follows:
\begin{align}
  P_\varrho = \frac{\text{dim} \varrho}{|2O|} \sum_{g \in 2O} \chi_\varrho (g)^* D(g)~,
\end{align}
where $D(g)$ is the $SU(2)$ Wigner matrix corresponding to group element $g$, and the character $\chi_\varrho (g) = \text{tr}(\varrho(g) )$ is the trace of the matrix of the desired irrep evaluated at a group element.
In cases where multiple copies of the irrep are present, one can try to optimize the distance of the code inside the multiplicity space.

Logical Pauli matrices $\overline{\sigma}_w$ are defined using the above projection and the angular momentum operators:
\begin{align}
  \overline{\sigma}_w = i P_\varrho e^{-i \pi J_w} P_\varrho~.
\end{align}
Finally, $|\overline{0} \rangle$ is defined as the $+1$ eigenvalue of $\overline{\sigma}_z$ and $|\overline{1} \rangle = \overline{\sigma}_x |\overline{0} \rangle $.

(source: raw/error-correction-zoo.md)

## Encoders

- Encoder for a modified code that protects against electric and magnetic field fluctuations  ([arXiv:2503.12142](https://arxiv.org/abs/2503.12142)).

## General gates

- Universal computation results from being able to prepare a single logical state, perform one measurement, and the following logical gates: the phase gate ($ \overline{S} $), the Hadamard gate ($\overline{H}$), the conditional phase gate ($\overline{CZ}$), and the square root of the phase gate ($\overline{T}$). Single-qubit Cliffords can be generated using $\overline{S}$ and $\overline{H}$, the extension to multiple-qubit Cliffords is done using $\overline{CZ}$, and $\overline{T}$ is to transform to non-Clifford states. Together these gates can be used to create all logical unitaries, while preparation and measurement complete universal quantum computation.

## Relations

- _parent_: [[concepts/qec/single-spin]]
- _parent_: [[concepts/qec/group-representation]] — Clifford-group spin codes are group-representation codes with $G$ being a subgroup of $SU(2)$  ([arXiv:2005.10910](https://arxiv.org/abs/2005.10910), [arXiv:2304.08611](https://arxiv.org/abs/2304.08611)).
- _cousin_: [[concepts/qec/qubit-permutation-invariant]] — Clifford codes for spins housing representations of $SU(2)$ yield PI qubit codes with non-trivial distance when the single spin-$n/2$ is treated as the permutationally invariant subspace of $n$ qubits via the Dicke-state mapping. The subgroup of gates of a Clifford-group spin code is implemented transversally via this mapping  ([arXiv:2304.08611](https://arxiv.org/abs/2304.08611)).
