---
type: concept
name: BPSK c-q modulation format
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- BPSK c-q modulation code
- BPSK c-q modulation scheme
- BPSK c-q signaling format
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-hadamard-bpsk
- concepts/qec/quantum-psk
- concepts/qec/squeezed-coherent-bpsk
- concepts/qec/two-legged-cat
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_bpsk
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_bpsk
---

# BPSK c-q modulation format

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_bpsk) (`code_id: quantum_bpsk`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Coherent-state c-q binary code encoding into two coherent states $|\pm\alpha\rangle$ for complex $\alpha$. A shifted version, with codewords $\{|0\rangle,|\alpha\rangle\}$, is called binary amplitude modulation (BAM), The three-state subcode $\{|\alpha,\alpha\rangle,|-\alpha,\alpha\rangle,|\alpha,-\alpha\rangle\}$ of two-mode BPSK is called the *single-degeneracy code*  ([arXiv:1101.1550](https://arxiv.org/abs/1101.1550)).

(source: raw/error-correction-zoo.md)

## Rate

The single-degeneracy code yields an improved PIE by $2.8\%$ over BPSK  ([doi:10.1103/PhysRevA.61.032309](https://doi.org/10.1103/PhysRevA.61.032309)) (see  ([arXiv:1101.1550](https://arxiv.org/abs/1101.1550))).

## Decoders

- Linear-optical quantum receiver  ([arXiv:1103.5592](https://arxiv.org/abs/1103.5592)).
- Kennedy receiver  ([arXiv:0706.1038](https://arxiv.org/abs/0706.1038)).
- Photon-number resolving detector  ([arXiv:1807.05199](https://arxiv.org/abs/1807.05199)).
- Non-Gaussian near-optimal receiver  ([arXiv:0706.1038](https://arxiv.org/abs/0706.1038)).
- Multi-stage quantum receiver  ([arXiv:1404.5033](https://arxiv.org/abs/1404.5033)).
- Quantum receiver attaining the Helstrom bound in the low-photon regime  ([arXiv:2410.21800](https://arxiv.org/abs/2410.21800)).
- Green machine receiver  ([arXiv:2310.05889](https://arxiv.org/abs/2310.05889)).

## Realizations

- Linear-optical quantum receiver  ([arXiv:1103.5592](https://arxiv.org/abs/1103.5592)).
- Homodyne receiver  ([arXiv:0809.4953](https://arxiv.org/abs/0809.4953)).
- Kennedy receiver  ([arXiv:0809.4953](https://arxiv.org/abs/0809.4953), [arXiv:1911.08932](https://arxiv.org/abs/1911.08932)).
- Photon-number resolving detector  ([arXiv:1807.05199](https://arxiv.org/abs/1807.05199)).
- Communication over dephasing  ([arXiv:1907.12515](https://arxiv.org/abs/1907.12515)), time-varying phase-noise  ([doi:10.1103/PhysRevResearch.2.023384](https://doi.org/10.1103/PhysRevResearch.2.023384)), and thermal-noise  ([arXiv:2007.11109](https://arxiv.org/abs/2007.11109)) channels.
- Adaptive decoder using displacements and photon detection  ([arXiv:2207.12234](https://arxiv.org/abs/2207.12234)).
- BPQM detector on a BPSK-modulated tree code  ([arXiv:2102.13052](https://arxiv.org/abs/2102.13052)).
- Superadditivity of the green machine receiver has been demonstrated in the photon starved regime  ([arXiv:2310.05889](https://arxiv.org/abs/2310.05889)).

## Relations

- _parent_: [[concepts/qec/quantum-psk]]
- _parent_: [[concepts/qec/quantum-hadamard-bpsk]]
- _parent_: [[concepts/qec/squeezed-coherent-bpsk]] — Squeezed-coherent BPSK c-q modulation reduces to coherent-state BPSK c-q modulation when the squeezing parameter is zero.
- _cousin_: [`bpsk`](https://errorcorrectionzoo.org/c/bpsk) — BPSK (BPSK c-q) codes are used to transmit classical information using antipodal coherent states over classical (quantum) channels.
- _cousin_: [[concepts/qec/two-legged-cat]] — BPSK c-q (two-component cat) codes are used to transmit classical (quantum) information using (superpositions of) antipodal coherent states over quantum channels.
