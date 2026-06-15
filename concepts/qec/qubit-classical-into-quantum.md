---
type: concept
name: Qubit c-q code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/classical-into-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qubit_classical_into_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qubit_classical_into_quantum
---

# Qubit c-q code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qubit_classical_into_quantum) (`code_id: qubit_classical_into_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A qubit code designed for transmission of classical information in the form of bits through non-classical channels.

(source: raw/error-correction-zoo.md)

## Protection

Performance of a linear binary code over a channel is dual to the performance of its dual over a particular dual channel  ([arXiv:1701.05583](https://arxiv.org/abs/1701.05583)).

## Decoders

- Belief propagation with quantum messages (BPQM) decoder for c-q channel communication  ([arXiv:1607.04833](https://arxiv.org/abs/1607.04833)).
The original BPQM proposal used quantum messages to decode pure-state c-q channels, had c-q polar codes in mind, and yielded explicit capacity-achieving decoders for non-Pauli channels  ([arXiv:1607.04833](https://arxiv.org/abs/1607.04833)).
BPQM was analyzed for a BPSK-modulated pure-loss channel and shown to be optimal for small tree codes  ([arXiv:2003.04356](https://arxiv.org/abs/2003.04356)).
A later quantum message-passing formulation proved optimality of BPQM for any binary linear code with a tree Tanner graph, and proposed an extension to factor graphs with cycles using approximate cloning  ([arXiv:2109.08170](https://arxiv.org/abs/2109.08170)).
BPQM has also been extended to symmetric classical-quantum channels using paired measurements  ([arXiv:2207.04984](https://arxiv.org/abs/2207.04984)).

## Realizations

- Quantum enhancement was demonstrated using a polarization-based non-error-correcting c-q encoding  ([arXiv:1704.07036](https://arxiv.org/abs/1704.07036)).

## Relations

- _parent_: [[concepts/qec/classical-into-quantum]]
