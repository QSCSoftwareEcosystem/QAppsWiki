---
type: concept
name: Subsystem homological product code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/homological-product
- concepts/qec/multisector-hypergraph
- concepts/qec/qubit-concatenated
- concepts/qec/qubit-subsystem-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/subsystem_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: subsystem_product
---

# Subsystem homological product code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/subsystem_product) (`code_id: subsystem_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A CSS subsystem code constructed from a product of two (subspace) CSS codes.
The case for qubits is formulated below, but these codes have also been extended to Galois qudits  ([arXiv:2007.12152](https://arxiv.org/abs/2007.12152)).

Denote the two CSS codes' parity-check matrix blocks as $H_X^i, H_Z^i$ for $i \in \{A, B\}$.
SP codes can be constructed by the following gauge generating matrices
\begin{align}
\begin{split}
  \label{sub:gauge}
    G_X=\left(\begin{array}{c}H_X^A \otimes I \\ I \otimes
              H_X^B \end{array}\right)
    G_Z=\left(\begin{array}{c}H_Z^A \otimes I \\ I \otimes
              H_Z^B \end{array}\right)~,
\end{split}
\end{align}
where $I$ is the identity matrix with size chosen to match the dimensions.

A stabilizer generator matrix can be written in terms of
the codes' generating matrices, $L_X^i, L_Z^i$ for $i \in \{A, B\}$:
\begin{align}
\begin{split}
  \label{sub:stabilizer}
    H_X=\left(\begin{array}{c}H_X^A \otimes H_X^B \\
              H_X^A \otimes L_X^B \\
              L_X^A \otimes H_X^B \end{array}\right),
    H_Z=\left(\begin{array}{c}H_Z^A \otimes H_Z^B \\
              H_Z^A \otimes L_Z^B \\
              L_Z^A \otimes H_Z^B \end{array}\right)~.
\end{split}
\end{align}
The null space of $G$ excluding $H$ gives logical generating matrices in canonical pairs
\begin{align}
\begin{split}
  L_{X}&=\left(L_{X}^{A}\otimes L_{X}^{B}\right)\\
  L_{Z}&=\left(L_{Z}^{A}\otimes L_{Z}^{B}\right)~,
\end{split}
\end{align}
which satisfy $L_{X}L_{Z}^{T}=I$.

(source: raw/error-correction-zoo.md)

## Protection

If the CSS codes have parameters $⟦n_i,k_i,d_{i},d_{i}⟧$ and sparsity $\{r_i,c_i\}$, for $i=A,B$ respectively,
the SP code has parameters $⟦n_An_B,k_Ak_B,d\leq d_Ad_B⟧$ and sparsity $\{\max (r_A,r_B), c_A+c_B\}$.
Note the distance relation holds for both $X$ and $Z$, hence we omit the $X/Z$ subscript.

## Relations

- _parent_: [[concepts/qec/qubit-subsystem-css]]
- _cousin_: [[concepts/qec/homological-product]] — SP codes reduce to homological product codes when there are no gauge qubits  ([arXiv:2007.12152](https://arxiv.org/abs/2007.12152)).
- _cousin_: [[concepts/qec/multisector-hypergraph]] — SP codes are projected higher-dimensional HGP codes  ([arXiv:2007.12152](https://arxiv.org/abs/2007.12152)).
- _cousin_: [[concepts/qec/qubit-concatenated]] — Concatenated CSS stabilizer codes are gauge-fixed SP codes  ([arXiv:2007.12152](https://arxiv.org/abs/2007.12152)).
