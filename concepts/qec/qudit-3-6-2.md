---
type: concept
name: $((3,6,2))_{\mathbb{Z}_6}$ Euler code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ame
- concepts/qec/qudits-into-qudits
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_3_6_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_3_6_2
---

# $((3,6,2))_{\mathbb{Z}_6}$ Euler code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_3_6_2) (`code_id: qudit_3_6_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Three-qudit error-detecting code with logical dimension $K=6$ that is obtained from a particular AME state that serves as a solution of a quantum analogue of the classical problem of 36 officers of Euler.
The code is obtained from a $((4,1,3))_{\mathbb{Z}_6}$ code.

(source: raw/error-correction-zoo.md)

## Encoders

- Quantum circuit encoding the state into a qubit system  ([arXiv:2504.05394](https://arxiv.org/abs/2504.05394)).

## Relations

- _parent_: [[concepts/qec/qudits-into-qudits]]
- _parent_: [[concepts/qec/ame]] — The $((3,6,2))_{\mathbb{Z}_6}$ Euler code is an example of a non-stabilizer perfect-tensor code  ([arXiv:2104.05122](https://arxiv.org/abs/2104.05122)).
- _parent_: [[concepts/qec/small-distance-quantum]]

## Notes

- Popular summary in [Quanta Magazine](https://www.quantamagazine.org/eulers-243-year-old-impossible-puzzle-gets-a-quantum-solution-20220110/).
