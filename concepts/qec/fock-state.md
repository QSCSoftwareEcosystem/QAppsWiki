---
type: concept
name: Fock-state bosonic code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ampdamp
- concepts/qec/qudits-into-oscillators
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/fock_state
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: fock_state
---

# Fock-state bosonic code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/fock_state) (`code_id: fock_state`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qudit-into-oscillator code whose protection against AD noise (i.e., photon loss) stems from the use of disjoint sets of Fock states for the construction of each code basis state. The simplest example is the dual-rail code, which has codewords consisting of single Fock states $|10\rangle$ and $|01\rangle$. This code can detect a single loss error since a loss operator in either mode maps one of the codewords to a different Fock state $|00\rangle$. More involved codewords consist of several well-separated Fock states such that multiple loss events can be detected and corrected.

(source: raw/error-correction-zoo.md)

## Protection

Code distance $d$ is the minimum distance (assuming some metric) between any two labels of Fock states corresponding to different code basis states. For a single mode, $d$ is the minimum absolute value of the difference between any two Fock-state labels; such codes can detect up to $d-1$ loss events. Multimode distances can be defined analogously; see, e.g., Chuang-Leung-Yamamoto codes. There are tradeoffs in how well a Fock-state code protects against loss/gain errors and dephasing noise  ([arXiv:2008.12576](https://arxiv.org/abs/2008.12576)).

## Rate

For every $K,t \geq 2$, there are explicitly constructible $K$-dimensional Fock-state codes with $q=N=(K-1)t(t+1)$ modes, total excitation $N$, and bosonic distance $t+1$; there also exist families with logical dimension $K = o(2^N)$ and distance of order $o(N/\log N)$  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).

## Relations

- _parent_: [[concepts/qec/qudits-into-oscillators]]
- _parent_: [[concepts/qec/ampdamp]] — Fock-state codes are designed to protect against bosonic AD noise.
- _cousin_: [`bits_into_bits`](https://errorcorrectionzoo.org/c/bits_into_bits) — Fock-state code distance is a natural extension of Hamming distance between binary strings.
