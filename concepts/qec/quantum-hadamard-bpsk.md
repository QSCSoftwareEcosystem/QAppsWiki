---
type: concept
name: Hadamard BPSK c-q modulation format
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Hadamard BPSK c-q modulation code
- Hadamard BPSK c-q modulation scheme
- Hadamard BPSK c-q signaling format
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/coherent-state-c-q
- concepts/qec/concatenated-c-q
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_hadamard_bpsk
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_hadamard_bpsk
---

# Hadamard BPSK c-q modulation format

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_hadamard_bpsk) (`code_id: quantum_hadamard_bpsk`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Multimode coherent-state c-q code that is a concatenation of a Hadamard code with a BPSK c-q code.
Its codewords are $n$-mode coherent states whose components $\pm\alpha$ are arranged according to rows of a Hadamard matrix.

(source: raw/error-correction-zoo.md)

## Rate

Using a joint-detection receiver, the code exhibits superadditive capacity relative to symbol-by-symbol detection and approaches the Holevo limit in the low-photon regime  ([arXiv:1101.1550](https://arxiv.org/abs/1101.1550)).

## Relations

- _parent_: [[concepts/qec/coherent-state-c-q]]
- _parent_: [[concepts/qec/concatenated-c-q]] — The Hadamard BPSK c-q code can be thought of as a concatenation of the Hadamard binary linear code with BPSK for the purposes of transmission of classical information over quantum channels.
- _cousin_: [`hadamard`](https://errorcorrectionzoo.org/c/hadamard) — The Hadamard BPSK c-q code can be thought of as a concatenation of the Hadamard binary linear code with BPSK for the purposes of transmission of classical information over quantum channels.
- _cousin_: [`bpsk`](https://errorcorrectionzoo.org/c/bpsk) — The Hadamard BPSK c-q code can be thought of as a concatenation of the Hadamard binary linear code with BPSK for the purposes of transmission of classical information over quantum channels.
