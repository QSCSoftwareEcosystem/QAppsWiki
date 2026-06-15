---
type: concept
name: Random quantum code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/quantum-perfect
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_random
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_random
---

# Random quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_random) (`code_id: quantum_random`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Quantum code whose construction is non-deterministic in some way, i.e., codes that utilize an element of randomness somewhere in their construction. Members of this class range from fully non-deterministic codes (e.g., random-circuit codes), to codes whose multi-step construction is deterministic with the exception of a single step (e.g., expander lifted-product codes).

(source: raw/error-correction-zoo.md)

## Protection

Certain random codes have nontrivial codespace complexity  ([arXiv:2310.04710](https://arxiv.org/abs/2310.04710)).

## Rate

Haar random codes achieve the quantum Hamming bound  ([arXiv:2510.07158](https://arxiv.org/abs/2510.07158)).

## Relations

- _parent_: [[concepts/qec/approximate-qecc]] — Random codes typically correct errors on average.
- _cousin_: [`random`](https://errorcorrectionzoo.org/c/random) — Random quantum codes are quantum analogues of random classical codes.
- _cousin_: [[concepts/qec/quantum-perfect]] — Haar random codes achieve the quantum Hamming bound  ([arXiv:2510.07158](https://arxiv.org/abs/2510.07158)).
