---
type: concept
name: $\chi^{(2)}$ code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fock-state
- concepts/qec/tiger
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/chi2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: chi2
---

# $\chi^{(2)}$ code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/chi2) (`code_id: chi2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $3n$-mode bosonic Fock-state code that requires only linear optics and the $\chi^{(2)}$ optical nonlinear interaction for encoding, decoding, and logical gates.
Codewords lie in Fock-state subspaces that are invariant under Hermitian combinations of the $\chi^{(2)}$ nonlinearities $abc^\dagger$ and $i abc^\dagger$, where $a$, $b$, and $c$ are lowering operators acting on one of the $n$ triples of modes on which the codes are defined.
Codewords are also $+1$ eigenstates of stabilizer-like *symmetry operators*, and photon parities are error syndromes.

(source: raw/error-correction-zoo.md)

## Protection

Codes protect against loss, gain, and dephasing errors conditional on the knowledge of the total number of photons lost.

## Encoders

- Linear optics and $\chi^{(2)}$ interactions.

## Decoders

- Linear optics and $\chi^{(2)}$ interactions.

## General gates

- Linear optics and $\chi^{(2)}$ interactions yield a universal set of gates.

## Relations

- _parent_: [[concepts/qec/fock-state]]
- _cousin_: [[concepts/qec/tiger]] — A three-mode tiger code with $G=(2,2,-2)$, $H=\left(\begin{smallmatrix}0&1&1\\1&0&1\end{smallmatrix}\right)$, and equal syndrome parameters has the same Fock-state support as one of the $\chi^{(2)}$ codes  ([arXiv:2411.09668](https://arxiv.org/abs/2411.09668)).
