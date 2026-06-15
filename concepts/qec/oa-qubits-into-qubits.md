---
type: concept
name: OA qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Hybrid subsystem qubit code
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/oa_qubits_into_qubits
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: oa_qubits_into_qubits
---

# OA qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/oa_qubits_into_qubits) (`code_id: oa_qubits_into_qubits`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An OAQECC family that encompasses ordinary (i.e., subspace) qubit codes, subsystem qubit codes, and hybrid qubit codes using an operator-algebraic framework.

A simple example encompassing elements of all three subfamilies encodes a single logical qubit and a single classical bit into a direct sum of two subsystem qubit codes.
A quantum subsystem code $\mathsf{A}_j\otimes\mathsf{B}_j$, with $\mathsf{A}_j$ the logical qubit factor, and $\mathsf{B}_j$ the gauge qubit factor, is associated with each of the two classical-bit values, labeled by $j\in\{1,2\}$.
The corresponding decomposition of the Hilbert space $\mathsf{H}$ is
\begin{align}
  \mathsf{H}=(\mathsf{A}_{1}\otimes\mathsf{B}_{1})\oplus(\mathsf{A}_{2}\otimes\mathsf{B}_{2})\oplus\mathsf{C}^{\perp}~,
\end{align}
where $\mathsf{C}^\perp$ is the combined error space of both codes.
The above code reduces to a subsystem code when $\mathsf{A}_{2}\otimes\mathsf{B}_{2}$ is trivial, reduces to a hybrid code when $\mathsf{B}_{1,2}$ are both trivial, and reduces to an ordinary (i.e., subspace) qubit code when $\mathsf{B}_{1}$ and $\mathsf{A}_{2}\otimes\mathsf{B}_{2}$ are both trivial.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [`oaecc`](https://errorcorrectionzoo.org/c/oaecc) — An OAQECC defined over qubits is an OA qubit code.
