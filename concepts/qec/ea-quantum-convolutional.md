---
type: concept
name: EA quantum convolutional code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/eastab
- concepts/qec/quantum-convolutional
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ea_quantum_convolutional
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ea_quantum_convolutional
---

# EA quantum convolutional code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ea_quantum_convolutional) (`code_id: ea_quantum_convolutional`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A quantum convolutional code designed to utilize pre-shared entanglement between sender and receiver  ([arXiv:0712.2223](https://arxiv.org/abs/0712.2223), [arXiv:0806.4214](https://arxiv.org/abs/0806.4214), [arXiv:0807.3803](https://arxiv.org/abs/0807.3803)).
Entanglement assistance removes the self-orthogonality constraint that ordinary quantum convolutional codes inherit from the stabilizer formalism, allowing arbitrary classical convolutional codes to be imported into quantum ones  ([arXiv:0807.3803](https://arxiv.org/abs/0807.3803)).
In some constructions, the additional ebits also reduce the memory requirements of the encoding circuit  ([arXiv:0812.4449](https://arxiv.org/abs/0812.4449)).

(source: raw/error-correction-zoo.md)

## Encoders

- Importing arbitrary classical quaternary convolutional codes into entanglement-assisted quantum convolutional encoders  ([arXiv:0712.2223](https://arxiv.org/abs/0712.2223), [arXiv:0807.3803](https://arxiv.org/abs/0807.3803)).

## Relations

- _parent_: [[concepts/qec/eastab]]
- _cousin_: [`convolutional`](https://errorcorrectionzoo.org/c/convolutional) — EA quantum convolutional codes are entanglement-assisted quantum analogues of convolutional codes.
- _cousin_: [[concepts/qec/quantum-convolutional]] — EA quantum convolutional codes are entanglement-assisted versions of quantum convolutional codes.
