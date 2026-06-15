---
type: concept
name: Qubit BCH code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-bch
- concepts/qec/qubit-css
- concepts/qec/qubit-stabilizer
- concepts/qec/stabilizer-over-gf4
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_bch
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_bch
---

# Qubit BCH code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_bch) (`code_id: quantum_bch`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit stabilizer code constructed from a self-orthogonal binary BCH code via the CSS construction, from a Hermitian self-orthogonal quaternary BCH code via the Hermitian construction, or by taking a Euclidean self-orthogonal BCH code over $\mathbb{F}_{2^m}$, converting it to a binary code, and applying the CSS construction.

(source: raw/error-correction-zoo.md)

## General gates

- Magic-state distillation protocols  ([arXiv:1709.02789](https://arxiv.org/abs/1709.02789)).

## Threshold

- Semi-analytical estimates of concatenated thresholds were given in  ([arXiv:quant-ph/0207119](https://arxiv.org/abs/quant-ph/0207119)). In the broader comparative study of Ref.  ([arXiv:0711.1556](https://arxiv.org/abs/0711.1556)), BCH codes larger than $⟦47,1,11⟧$ were not simulated because encoded-CNOT ex-Recs became impractical; although their large $t/n$ suggests potentially good thresholds, the resulting overhead was argued to limit their usefulness as bottom codes.

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]]
- _parent_: [[concepts/qec/galois-bch]] — Galois-qudit BCH codes for $q=2$ reduce to qubit BCH codes.
- _cousin_: [`bch`](https://errorcorrectionzoo.org/c/bch) — Binary BCH codes are used to construct a subset of qubit BCH codes via the CSS construction.
- _cousin_: [`q-ary_bch`](https://errorcorrectionzoo.org/c/q-ary_bch) — BCH codes are used to construct qubit BCH codes via the CSS construction or the Hermitian construction.
- _cousin_: [[concepts/qec/qubit-css]] — Some qubit BCH codes are CSS.
- _cousin_: [[concepts/qec/stabilizer-over-gf4]] — Hermitian self-orthogonal quaternary BCH codes are used to construct a subset of qubit BCH codes via the Hermitian construction.

## Notes

- Qubit BCH codes for small $n$ are tabulated in Ref.  ([arXiv:quant-ph/9910060](https://arxiv.org/abs/quant-ph/9910060)).
