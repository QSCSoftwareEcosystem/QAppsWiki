---
type: concept
name: 2D lattice stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/holographic
- concepts/qec/qldpc
- concepts/qec/quantum-double-abelian
- concepts/qec/surface
- concepts/qec/translationally-invariant-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/2d_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 2d_stabilizer
---

# 2D lattice stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/2d_stabilizer) (`code_id: 2d_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Lattice stabilizer code in two Euclidean dimensions, using either the ordinary block notion of locality or the fermionic/Majorana notion of locality.

Any translation-invariant 2D prime-qudit lattice stabilizer code can be converted to several copies of the prime-qudit 2D surface code along with some trivial codes  ([arXiv:1812.11193](https://arxiv.org/abs/1812.11193)).
Any 2D topological order requires weight-four Hamiltonian terms, i.e., it cannot be stabilized via weight-two or weight-three terms on 2D lattices of qubits or qutrits  ([arXiv:quant-ph/0308021](https://arxiv.org/abs/quant-ph/0308021), [arXiv:1102.0770](https://arxiv.org/abs/1102.0770), [arXiv:1803.02213](https://arxiv.org/abs/1803.02213)).

Translation-invariant 2D prime-qudit lattice stabilizer codes are equivalent to several copies of the prime-qudit surface code and a trivial code via a local constant-depth Clifford circuit  ([arXiv:1812.11193](https://arxiv.org/abs/1812.11193)).
There are algorithms which determine the fusion and braiding rules  ([arXiv:2312.11170](https://arxiv.org/abs/2312.11170)) as well as boundaries and twist defects  ([arXiv:2410.11942](https://arxiv.org/abs/2410.11942)) of a 2D translationally invariant modular-qudit stabilizer code for any qudit dimension.

(source: raw/error-correction-zoo.md)

## Encoders

- The geometric entanglement measure of a 2D stabilizer codeword with sufficiently high distance $d$ scales as order $\Omega(d^2)$  ([arXiv:2405.07970](https://arxiv.org/abs/2405.07970)).

## Decoders

- Renormalization group (RG) decoder  ([arXiv:1006.1362](https://arxiv.org/abs/1006.1362)).
- Tensor-network based decoder for 2D codes subject to correlated noise  ([arXiv:1809.10704](https://arxiv.org/abs/1809.10704)).
- Standard stabilizer-based error correction can be performed even in the presence of perturbations to the codespace  ([arXiv:2211.09803](https://arxiv.org/abs/2211.09803), [arXiv:2401.06300](https://arxiv.org/abs/2401.06300), [arXiv:2402.14906](https://arxiv.org/abs/2402.14906)); see also Refs.  ([arXiv:0807.0287](https://arxiv.org/abs/0807.0287), [arXiv:0911.3843](https://arxiv.org/abs/0911.3843), [arXiv:1107.3940](https://arxiv.org/abs/1107.3940)).
- Real-time geometrically local decoder based on introducing an ancillary buffer and confining spacetime interactions between anyons   ([arXiv:2510.08056](https://arxiv.org/abs/2510.08056)).

## Code capacity threshold

- Noise thresholds can be formulated as anyon condensation transitions in a topological field theory  ([arXiv:2301.05687](https://arxiv.org/abs/2301.05687)), generalizing the mapping of the effect of noise on a code state to a statistical mechanical model  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:1208.2317](https://arxiv.org/abs/1208.2317), [arXiv:1311.7688](https://arxiv.org/abs/1311.7688), [arXiv:1809.10704](https://arxiv.org/abs/1809.10704)). Namely, the noise threshold for a noise channel $\cal{E}$ acting on a 2D stabilizer state $|\psi\rangle$ can be obtained from the properties of the resulting (mixed) state $\mathcal{E}(|\psi\rangle\langle\psi|)$  ([arXiv:2301.05238](https://arxiv.org/abs/2301.05238), [arXiv:2301.05687](https://arxiv.org/abs/2301.05687), [arXiv:2301.05689](https://arxiv.org/abs/2301.05689), [arXiv:2309.11879](https://arxiv.org/abs/2309.11879), [arXiv:2401.17359](https://arxiv.org/abs/2401.17359)).

## Relations

- _parent_: [[concepts/qec/translationally-invariant-stabilizer]]
- _cousin_: [[concepts/qec/surface]] — Translation-invariant 2D qubit lattice stabilizer codes are equivalent to several copies of the Kitaev surface code via a local constant-depth qudit Clifford circuit  ([arXiv:1103.4606](https://arxiv.org/abs/1103.4606), [arXiv:1107.2707](https://arxiv.org/abs/1107.2707), [arXiv:1607.01387](https://arxiv.org/abs/1607.01387)).
- _cousin_: [[concepts/qec/quantum-double-abelian]] — Translation-invariant 2D prime-qudit lattice stabilizer codes are equivalent to several copies of the prime-qudit surface code and a trivial code via a local constant-depth qudit Clifford circuit  ([arXiv:1812.11193](https://arxiv.org/abs/1812.11193)).
- _cousin_: [[concepts/qec/holographic]] — 2D lattice stabilizer codes admit a bulk-boundary correspondence similar to that of holographic codes, namely, the boundary Hilbert space of the former cannot be realized via local degrees of freedom  ([arXiv:2312.04617](https://arxiv.org/abs/2312.04617)).
- _cousin_: [[concepts/qec/qldpc]] — Chain complexes describing qubit QLDPC codes can be converted to 2D lattice stabilizer codes  ([arXiv:2408.01769](https://arxiv.org/abs/2408.01769)).
