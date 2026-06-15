---
type: concept
name: Stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stabilizer
---

# Stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stabilizer) (`code_id: stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code whose logical subspace is the joint eigenspace (usually with eigenvalue $+1$) of a set of commuting unitary Pauli-type operators forming the code's stabilizer group.
They can be block codes defined on tensor-product spaces of qubits or qudits, or non-block codes defined on single sufficiently large Hilbert spaces such as bosonic modes or other Abelian group spaces.

The coding theory motivation for stabilizer codes came from linear binary codes, whose codewords form a closed subspace in the space of binary strings.
Stabilizer codes extend this property, in various ways, to quantum error correction.
Stabilizer codes can be defined succinctly using the stabilizer group generators and without explicitly writing out a basis of codewords.

Stabilizer codes were originally defined for qubits, where the relevant commuting operators are tensor products of Pauli matrices.
The Pauli stabilizer structure is useful in providing standardized encoding, gates, decoding, and performance bounds.
Elements of this structure remain in qudit extensions, in particular for prime-dimensional modular qudits and Galois qudits.
Infinite-dimensional Pauli-type bases yield the bosonic stabilizer and rotor stabilizer codes.

One can switch between stabilizer codes by appending another stabilizer group and taking the center of the resulting larger group.
\begin{defterm}{Stabilizer code switching, code deformation, update rule, or code rewiring}
\label{topic:code-switching}
Stabilizer code switching is a map between stabilizer codes that is done using a stabilizer group $\mathsf{F}$,
\begin{align}
\mathsf{S}\to\mathsf{N}_{\left\langle \mathsf{S},\mathsf{F}\right\rangle }\left(\mathsf{F}\right)~,
\end{align}
where $\mathsf{N}$ denotes taking the normalizer of a group (e.g., see  ([doi:10.1017/CBO9780511976667](https://doi.org/10.1017/CBO9780511976667), [arXiv:2402.00145](https://arxiv.org/abs/2402.00145)) for proofs).
Code switching may not preserve the logical information and instead implement logical measurements; conditions on $\mathsf{S}$ and $\mathsf{F}$ such that qubit stabilizer code switching preserves logical information are derived in  ([arXiv:2304.01277](https://arxiv.org/abs/2304.01277)).
The stabilizer rewiring algorithm (SRA) allows for code switching between a pair of compatible stabilizer codes  ([arXiv:1707.09403](https://arxiv.org/abs/1707.09403)) (see also Ref.  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879), [arXiv:1511.02596](https://arxiv.org/abs/1511.02596))), and ancillary qubits may be used to maintain minimum distance of any intermediate codes  ([arXiv:1709.09282](https://arxiv.org/abs/1709.09282)).
Clifford operations and Pauli measurements can be expressed as sequences of code switching  ([arXiv:2401.12017](https://arxiv.org/abs/2401.12017)).
In the context of stabilizer codes realizing Abelian topological phases, code switching implements *anyon condensation* of anyons represented by operators in the group $\mathsf{F}$.
Code switching can be done using only transversal gates for qubit stabilizer codes  ([arXiv:2409.13465](https://arxiv.org/abs/2409.13465)).
\end{defterm}

Extensions of the stabilizer formalism, such as XS and XP stabilizer codes, relax the mutual commutation property.
Other extensions, such as CWS and union stabilizer codes, enlarge the codespace by re-assigning error words as codewords.

(source: raw/error-correction-zoo.md)

## Protection

The group of all Pauli-type operators typically serves as the set of noise operators for stabilizer codes.

## General gates

- A Gottesman-Knill-type theorem exists for qubits, modular qudits, Galois qudits, and rotors  ([arXiv:1210.3637](https://arxiv.org/abs/1210.3637), [arXiv:1409.4800](https://arxiv.org/abs/1409.4800)), as well as oscillators  ([arXiv:quant-ph/0109047](https://arxiv.org/abs/quant-ph/0109047), [arXiv:1210.1783](https://arxiv.org/abs/1210.1783), [arXiv:1208.3660](https://arxiv.org/abs/1208.3660)). Stabilizer codes can be described by quadratic functions over Abelian groups  ([arXiv:2601.15396](https://arxiv.org/abs/2601.15396)).

## Decoders

- The structure of stabilizer codes allows for straightforward syndrome-based decoding because the stabilizer generators serve as the code's check operators, and their eigenvalues serve as the error syndromes. The error correction process involves measuring the stabilizer generators and applying correcting Pauli-type operators based on the measurement outcomes.

## Relations

- _parent_: [`group_quantum`](https://errorcorrectionzoo.org/c/group_quantum) — Stabilizer codes are constructed out of Pauli strings, modular-qudit Pauli strings, Galois-qudit Pauli strings, oscillator displacement operators, or rotor generalized Pauli strings. All of these are examples of the Weyl-Heisenberg group on Manin's quantum plane, which is defined on a configuration space that is generally a free Abelian group  ([doi:10.5802/aif.1117](https://doi.org/10.5802/aif.1117), [doi:10.1143/PTP.102.219](https://doi.org/10.1143/PTP.102.219), [arXiv:math/0307393](https://arxiv.org/abs/math/0307393), [arXiv:math/0402401](https://arxiv.org/abs/math/0402401)).
- _parent_: [`commuting_projector`](https://errorcorrectionzoo.org/c/commuting_projector) — Codespace is the ground-state space of the *code Hamiltonian*, which consists of an equal linear combination of stabilizer generators and which can be made into a frustration-free commuting-projector Hamiltonian.
- _parent_: [`frustration_free`](https://errorcorrectionzoo.org/c/frustration_free) — Codespace is the ground-state space of the *code Hamiltonian*, which consists of an equal linear combination of stabilizer generators and which can be made into a frustration-free commuting-projector Hamiltonian.
- _parent_: [`knill`](https://errorcorrectionzoo.org/c/knill) — Stabilizer codes are Knill codes whose nice error basis is either the Pauli strings, modular-qudit Pauli strings, Galois-qudit Pauli strings, oscillator displacement operators, or rotor generalized Pauli strings.
- _cousin_: [`topological_abelian`](https://errorcorrectionzoo.org/c/topological_abelian) — There is a general correspondence between stabilizer codes and gauge theory, with the stabilizer group playing the role of the gauge group  ([arXiv:2412.15317](https://arxiv.org/abs/2412.15317)).

## Notes

- See  ([arXiv:2605.29137](https://arxiv.org/abs/2605.29137)) for a pedagogical introduction to stabilizer codes.
