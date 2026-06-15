---
type: concept
name: Quantum spatially coupled (SC-QLDPC) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qldpc
- concepts/qec/translationally-invariant-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/sc_qldpc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: sc_qldpc
---

# Quantum spatially coupled (SC-QLDPC) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/sc_qldpc) (`code_id: sc_qldpc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

QLDPC code whose stabilizer generator matrix resembles the parity-check matrix of SC-LDPC codes.
There exist CSS  ([arXiv:1102.3181](https://arxiv.org/abs/1102.3181)) and stabilizer constructions  ([arXiv:2305.00137](https://arxiv.org/abs/2305.00137)).
In either case, the stabilizer generator matrix is constructed by "spatially" coupling sub-matrix blocks in chain-like fashion (or, more generally, in grid-like fashion) to yield a band matrix.
The sub-matrix blocks have to satisfy certain conditions amongst themselves so that the resulting band matrix is a stabilizer generator matrix.
Matrices corresponding to translationally invariant chains are called *time-invariant*, and otherwise are called *time-varying*.

A finite-length chain is then capped by imposing either open boundary conditions (yielding *non-tail-biting* SC-QLDPC codes) or periodic boundary conditions (yielding *tail-biting* SC-QLDPC codes).
Both constructions  ([arXiv:1102.3181](https://arxiv.org/abs/1102.3181), [arXiv:2305.00137](https://arxiv.org/abs/2305.00137)) are tail-biting.

In the stabilizer construction  ([arXiv:2305.00137](https://arxiv.org/abs/2305.00137)), the structure of the band matrix allows codes to be concisely defined in terms of *characteristic polynomials*, whose coefficients are the sub-matrix blocks and which resemble the Pauli-to-polynomial mapping associated with translationally invariant stabilizer codes.
Some CSS code constructions can be used to define sub-matrix blocks, yielding spatially coupled (i.e., translationally invariant) extensions of such codes.

For example, the $3\times 3$ toric code can be expressed as an SC-QLDPC code with stabilizer generator matrix given in \ref{figure:sc-qldpc-3toric-stabilizer-generators}.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/translationally-invariant-stabilizer]] — Stabilizer generator matrices of SC-QLDPC codes on infinite-length chains or grids define a class of lattice stabilizer codes.
- _cousin_: [`sc_ldpc`](https://errorcorrectionzoo.org/c/sc_ldpc) — SC-QLDPC code stabilizer-generator matrices have similar block form as the parity-check matrices of SC-LDPC codes.
