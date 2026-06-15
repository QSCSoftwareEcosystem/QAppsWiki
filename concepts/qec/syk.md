---
type: concept
name: SYK code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/fermions
- concepts/qec/hamiltonian
- concepts/qec/holographic
- concepts/qec/kpt
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/syk
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: syk
---

# SYK code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/syk) (`code_id: syk`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Approximate $n$-fermionic code whose codewords are low-energy states of the Sachdev-Ye-Kitaev (SYK) Hamiltonian  ([arXiv:cond-mat/9212030](https://arxiv.org/abs/cond-mat/9212030)) or other low-rank SYK models  ([arXiv:1910.10173](https://arxiv.org/abs/1910.10173), [arXiv:2010.10545](https://arxiv.org/abs/2010.10545)).

(source: raw/error-correction-zoo.md)

## Rate

SYK codes can have a constant rate and distance scaling as $n^c$ for some power $c$  ([arXiv:2310.07770](https://arxiv.org/abs/2310.07770)).

## Threshold

- The coherent information of noise channels that either break or conserve fermion parity has been calculated for the SYK thermofield double state  ([arXiv:2410.24225](https://arxiv.org/abs/2410.24225)).

## Relations

- _parent_: [[concepts/qec/fermions]]
- _parent_: [[concepts/qec/approximate-qecc]] — SYK codes are approximately error correcting in that they satisfy certain error-correction conditions based on mutual information  ([arXiv:2310.07770](https://arxiv.org/abs/2310.07770)).
- _parent_: [[concepts/qec/hamiltonian]] — The SYK code Hamiltonian is constructed out of non-commuting few-site terms, and every fermion participates in many interactions.
- _parent_: [[concepts/qec/holographic]] — In a holographic model  ([arXiv:2310.07770](https://arxiv.org/abs/2310.07770)), the large distance of these codes can be interpreted as being due to the emergence of a wormhole.
- _cousin_: [[concepts/qec/kpt]] — The Brownian SYK model can be used to demonstrate the complexity-based error-correction of KPT codes  ([arXiv:2003.05451](https://arxiv.org/abs/2003.05451)).
