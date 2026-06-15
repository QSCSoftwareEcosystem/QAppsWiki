---
type: concept
name: Magnon code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/eth
- concepts/qec/frustration-free
- concepts/qec/spins-into-spins
- concepts/qec/spt
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/mps
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: mps
---

# Magnon code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/mps) (`code_id: mps`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $n$-spin approximate code whose codespace of $k=\Omega(\log n)$ qubits is efficiently described in terms of particular matrix product states or Bethe ansatz tensor networks.
Magnon codewords are low-energy excited states of the frustration-free Heisenberg-XXX model Hamiltonian  ([arXiv:1902.02115](https://arxiv.org/abs/1902.02115)).

(source: raw/error-correction-zoo.md)

## Protection

Distance $d=\Omega(n^{1-\nu})$ for any $\nu\in(0,1)$.

## Relations

- _parent_: [[concepts/qec/spins-into-spins]] — Magnon codewords are low-energy excited states of the frustration-free Heisenberg-XXX model Hamiltonian  ([arXiv:1902.02115](https://arxiv.org/abs/1902.02115)).
- _parent_: [[concepts/qec/frustration-free]] — Magnon codewords are low-energy excited states of the frustration-free Heisenberg-XXX model Hamiltonian  ([arXiv:1902.02115](https://arxiv.org/abs/1902.02115)).
- _parent_: [[concepts/qec/approximate-qecc]] — Magnon codes approximately protect against erasures in the thermodynamic limit.
- _cousin_: [[concepts/qec/eth]] — Magnon codes have been shown to protect against non-geometrically local noise, while ETH codes protect only against erasures on geometrically local patches.
- _cousin_: [[concepts/qec/spt]] — Magnon codewords  ([arXiv:1902.02115](https://arxiv.org/abs/1902.02115)) are associated with 1D SPT orders  ([arXiv:1008.3745](https://arxiv.org/abs/1008.3745), [arXiv:1010.3732](https://arxiv.org/abs/1010.3732), [arXiv:1103.3323](https://arxiv.org/abs/1103.3323), [arXiv:1106.4772](https://arxiv.org/abs/1106.4772)).
