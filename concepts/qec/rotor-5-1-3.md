---
type: concept
name: $⟦5,1,3⟧_{\mathbb{Z}}$ Five-rotor code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ame
- concepts/qec/covariant
- concepts/qec/quantum-cyclic
- concepts/qec/qudit-5-1-3
- concepts/qec/rotor-stabilizer
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/rotor_5_1_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: rotor_5_1_3
---

# $⟦5,1,3⟧_{\mathbb{Z}}$ Five-rotor code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/rotor_5_1_3) (`code_id: rotor_5_1_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Extension of the five-qubit stabilizer code to the integer alphabet, i.e., the angular momentum states of a rotor. The code is $U(1)$-covariant and ideal codewords are not normalizable.

(source: raw/error-correction-zoo.md)

## Protection

Normalized codewords approximately protect against erasure while maintaining covariance  ([arXiv:1902.07714](https://arxiv.org/abs/1902.07714)).
For smooth cutoff width $w$ and logical charge range $2h+1$, the worst-case entanglement infidelity scales as $O(h/w)$ for a known single erasure and for any known two-subsystem erasure  ([arXiv:1902.07714](https://arxiv.org/abs/1902.07714)).

## Relations

- _parent_: [[concepts/qec/rotor-stabilizer]]
- _parent_: [[concepts/qec/ame]] — Five-rotor codewords are CV AME  ([arXiv:2503.15698](https://arxiv.org/abs/2503.15698)).
- _parent_: [[concepts/qec/quantum-cyclic]]
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/covariant]] — The five-rotor code is $U(1)$-covariant.
- _cousin_: [[concepts/qec/qudit-5-1-3]] — The five-rotor code is a rotor analogue of the five-qudit code.
