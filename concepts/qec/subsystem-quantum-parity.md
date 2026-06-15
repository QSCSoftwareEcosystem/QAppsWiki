---
type: concept
name: Subsystem hypergraph product (SHP) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Subsystem generalized Shor code
- Bacon-Casaccino subsystem code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-shor
- concepts/qec/hybridqecc
- concepts/qec/hypergraph-product
- concepts/qec/subsystem-lifted-product
- concepts/qec/subsystem-product
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/subsystem_quantum_parity
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: subsystem_quantum_parity
---

# Subsystem hypergraph product (SHP) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/subsystem_quantum_parity) (`code_id: subsystem_quantum_parity`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A CSS subsystem version of the generalized Shor code that has the same parameters as the subspace version, but requires fewer stabilizer measurements, resulting in a simpler error recovery routine.
The code can also be thought of as a subsystem version of an HGP code because two such codes reduce to an HGP code upon gauge fixing  ([arXiv:2002.06257](https://arxiv.org/abs/2002.06257)).
The code can be obtained from a generalized Shor code by removing certain stabilizers that do not affect the code distance.

The $X$- and $Z$-type gauge generators of this CSS $⟦n_1n_2,k_1k_2,\min(d_1,d_2)⟧$ code correspond to rows of the following two respective matrices,
\begin{align}
\begin{split}
G_{X}&=H_{1}\otimes I_{n_{2}}\\
G_{Z}&=I_{n_{1}}\otimes H_{2}~,
\end{split}
\end{align}
where $H_{1,2}$ are the parity-check matrices of two binary linear codes, $C_1 = [n_1, k_1, d_1]$ and $C_2 = [n_2, k_2, d_2]$
 ([arXiv:2002.06257](https://arxiv.org/abs/2002.06257)).

(source: raw/error-correction-zoo.md)

## Decoders

- Efficient decoder  ([doi:10.1109/ISIT.2009.5205650](https://doi.org/10.1109/ISIT.2009.5205650)).

## Relations

- _parent_: [[concepts/qec/subsystem-lifted-product]] — SLP codes reduce to SHP codes when the lift is trivial.
- _parent_: [[concepts/qec/subsystem-product]] — SP codes reduce to SHP codes when constructed from two classical codes instead of quantum CSS codes  ([arXiv:2007.12152](https://arxiv.org/abs/2007.12152)).
- _cousin_: [[concepts/qec/hypergraph-product]] — Two SHP codes can be gauge-fixed to yield an HGP code  ([arXiv:2002.06257](https://arxiv.org/abs/2002.06257)). The SHP and HGP code constructions yield the same dimension and minimum distance, but the former does not yield QLDPC codes; see  ([arXiv:0903.0566](https://arxiv.org/abs/0903.0566)).
- _cousin_: [[concepts/qec/generalized-shor]] — In a $⟦n_1n_2, k_1k_2, min(d_1, d_2)⟧$ generalized Shor code, error correction is achieved by measuring $(n_1−k_1)n_2+k_1(n_2−k_2)$ stabilizer generators  ([arXiv:quant-ph/0508131](https://arxiv.org/abs/quant-ph/0508131)). The SHP code achieves the same degree of correctability, but requires only $(n_1−k_1)k_2+k_1(n_2−k_2)$ stabilizer measurements.
- _cousin_: [[concepts/qec/hybridqecc]] — Classical information can also be encoded in subsystem codes using their gauge qubits  ([arXiv:2012.05896](https://arxiv.org/abs/2012.05896)).
