---
type: concept
name: Quantum code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_into_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_into_quantum
---

# Quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_into_quantum) (`code_id: quantum_into_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code designed for transmission of quantum and/or classical information through a quantum channel for the purposes of robust storage, communication, or sensing. 
Transmission can be performed with side information or entanglement.

While codewords $c$ of an ECC are elements of some alphabet $\Sigma$, quantum codewords are $L^2$-normalizable complex functions on $\Sigma$.
Put differently, the configuration space of the canonical (a.k.a. computational) basis states $|c\rangle$ of a quantum system is the classical alphabet $\Sigma$.
The table below lists the most common alphabets used in quantum codes, along with names of the corresponding systems.
  \begin{table}
    \begin{cells}
    \celldata<c H, c H>{alphabet $\Sigma$ & system $L^2(\Sigma)$}
    \celldata<c, c>{
    $\mathbb{Z}_{2}=\mathbb{F}_2$ & qubit
        \\
    $\mathbb{F}_q$ & Galois qudit
        \\
    $\mathbb{Z}_{q}$ & modular qudit
        \\
    $\mathbb{R}$ & bosonic mode
        \\
    $G$ & group-valued qudit
        \\
    $G/H$ & coset-valued qudit
        \\
    $\mathcal{C}$ & category-valued qudit
    }
    \end{cells}
    \caption{Table listing the most common alphabets (a.k.a. configuration spaces) used in quantum codes. Here, $\mathbb{F}_q$ is a finite field, $G$ is a group, $H$ is a subgroup of $G$, and $\mathcal{C}$ is a category.}
    \label{table:quantum-alphabets}
  \end{table}

(source: raw/error-correction-zoo.md)
