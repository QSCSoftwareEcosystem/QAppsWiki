---
type: concept
name: EA QLDPC code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/eastab
- concepts/qec/qldpc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ea_qldpc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ea_qldpc
---

# EA QLDPC code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ea_qldpc) (`code_id: ea_qldpc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

EA qubit stabilizer code for which the number of sites participating in each stabilizer generator and the number of stabilizer generators that each site participates in are both bounded by a constant $w$ as $n\to\infty$.

(source: raw/error-correction-zoo.md)

## Encoders

- Encoder adapted for an all-optical implementation  ([doi:10.1364/OL.35.001464](https://doi.org/10.1364/OL.35.001464)).

## Decoders

- Decoder adapted for an all-optical implementation  ([doi:10.1364/OL.35.001464](https://doi.org/10.1364/OL.35.001464)).

## Relations

- _parent_: [[concepts/qec/eastab]]
- _cousin_: [[concepts/qec/qldpc]] — EA QLDPC codes utilize additional ancillary qubits in a pre-shared entangled state, but reduce to qubit QLDPC codes when said qubits are interpreted as noiseless physical qubits.
- _cousin_: [`ldpc`](https://errorcorrectionzoo.org/c/ldpc) — There exist necessary and sufficient conditions for an EA QLDPC code consuming $e=1$ ebit that is obtainable from a pair of LDPC codes  ([arXiv:1108.0679](https://arxiv.org/abs/1108.0679)).

## Notes

- Review of EA QLDPC codes provided in Ref.  ([doi:10.1109/ACCESS.2015.2503267](https://doi.org/10.1109/ACCESS.2015.2503267)).
