---
type: concept
name: Operator-algebra (OA) qubit stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Hybrid subsystem qubit stabilizer code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/oa-qubits-into-qubits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qubit_stabilizer_oaqecc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qubit_stabilizer_oaqecc
---

# Operator-algebra (OA) qubit stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qubit_stabilizer_oaqecc) (`code_id: qubit_stabilizer_oaqecc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An OAQECC in which the commutant $\mathcal{A}'$ of the logical algebra $\mathcal{A}$ arises as the group algebra of a subgroup $\mathsf{G}$ of the $n$-qubit Pauli group $\mathsf{P}_n$.

The stabilizer $\mathsf{S}$ is the center of $\mathsf{G}$ modulo factors of $i I$.
The quotient $\mathsf{P}_n / \mathsf{N(S)}$, where $\mathsf{N(S)}$ is the normalizer of $\mathsf{S}$, is in bijective correspondence with the factors of the logical algebra $\mathcal{A}$.

(source: raw/error-correction-zoo.md)

## Protection

Specialized conditions for the correctability of $\mathcal{A}$ with respect to an error operation $\mathcal{E}$ with operation elements $\{E_j\}_j$ can be given in group theoretic terms.
Indeed, $\mathcal{A}$ is correctable for $\mathcal{E}$ if, for all $j,k$,
\begin{align}
E_{j}^{\dagger}E_{k}&\notin(\mathsf{N(S)}-\mathsf{G})\cup\\&
\,\,\,\,\,\,\,\,\,\,\,\,\,\cup\left(\bigcup_{\tau,\sigma:\tau\mathsf{N(S)}\neq\sigma\mathsf{N(S)}}\tau\mathsf{N(S)}\sigma\right)~.
\end{align}

## Relations

- _parent_: [[concepts/qec/oa-qubits-into-qubits]]
