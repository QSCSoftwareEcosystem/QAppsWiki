---
type: concept
name: Concatenated GKP code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/488-color
- concepts/qec/abelian-lifted-product
- concepts/qec/cluster-state
- concepts/qec/multimodegkp
- concepts/qec/oscillators-concatenated
- concepts/qec/quantum-parity
- concepts/qec/quantum-polar
- concepts/qec/quantum-repetition
- concepts/qec/stab-4-2-2
- concepts/qec/stab-5-1-3
- concepts/qec/stab-6-2-2
- concepts/qec/stabilizer-over-gfqsq
- concepts/qec/triangular-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/gkp_concatenated
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: gkp_concatenated
---

# Concatenated GKP code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/gkp_concatenated) (`code_id: gkp_concatenated`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A concatenated code whose outer code is a GKP code. In other words, a bosonic code that can be thought of as a concatenation of an arbitrary inner code and another bosonic outer code. Most examples encode physical qubits of an inner stabilizer code into the square-lattice GKP code.

(source: raw/error-correction-zoo.md)

## Protection

The analog syndrome information of the outer GKP code can improve protection of the inner code. As an example, concatenating a three-qubit quantum repetition code with GKP codes can correct some two-bit-flip errors  ([arXiv:1706.03011](https://arxiv.org/abs/1706.03011)).

## Rate

Recursively concatenating the $C_6$ and $⟦4,2,2⟧$ codes with GKP codes achieves the hashing bound of the displacement channel  ([arXiv:1706.03011](https://arxiv.org/abs/1706.03011)). 
Concatenating Abelian LP codes with GKP codes can surpass the CSS Hamming bound  ([arXiv:2111.07029](https://arxiv.org/abs/2111.07029)). 
Particular families of GKP codes achieve the capacity of AD and amplification channels for some loss rates  ([arXiv:2412.06715](https://arxiv.org/abs/2412.06715)). 
Concatenations of square-lattice GKP codes with Hermitian Galois-qudit codes achieve the capacity for all loss rates  ([arXiv:2505.10499](https://arxiv.org/abs/2505.10499)). 
Concatenation of GKP codes with quantum polar codes achieves a rate against the displacement channel  ([arXiv:2505.10499](https://arxiv.org/abs/2505.10499)).

## General gates

- Linear-optical computation  ([arXiv:2408.04126](https://arxiv.org/abs/2408.04126)).

## Decoders

- Circuit-level soft information decoder  ([arXiv:2505.06385](https://arxiv.org/abs/2505.06385)).

## Code capacity threshold

- $0.599$ threshold displacement standard deviation for GKP-repetition code  ([arXiv:2212.11397](https://arxiv.org/abs/2212.11397)).
- $0.59$ threshold displacement standard deviation for GKP-color code  ([arXiv:2112.14447](https://arxiv.org/abs/2112.14447)).
- A concatenated threshold with GKP codes on the lowest level exists for general Markovian noise  ([arXiv:2410.12365](https://arxiv.org/abs/2410.12365)).
- There is an upper bound on the threshold under local update recovery that is derived via quantum optimal transport  ([arXiv:2309.16241](https://arxiv.org/abs/2309.16241)).

## Relations

- _parent_: [[concepts/qec/multimodegkp]]
- _parent_: [[concepts/qec/oscillators-concatenated]]
- _cousin_: [[concepts/qec/cluster-state]] — GKP codes have been concatenated with cluster-state codes  ([arXiv:1712.00294](https://arxiv.org/abs/1712.00294)).
- _cousin_: [[concepts/qec/quantum-repetition]] — Concatenating a three-qubit quantum repetition code with GKP codes can correct some two-bit-flip errors  ([arXiv:1706.03011](https://arxiv.org/abs/1706.03011)) (see also  ([arXiv:2212.11397](https://arxiv.org/abs/2212.11397))).
- _cousin_: [[concepts/qec/stab-4-2-2]] — Recursively concatenating the $C_6$ and $⟦4,2,2⟧$ codes with GKP codes achieves the hashing bound of the displacement channel  ([arXiv:1706.03011](https://arxiv.org/abs/1706.03011)).
- _cousin_: [[concepts/qec/stab-6-2-2]] — Recursively concatenating the $C_6$ and $⟦4,2,2⟧$ codes with GKP codes achieves the hashing bound of the displacement channel  ([arXiv:1706.03011](https://arxiv.org/abs/1706.03011)).
- _cousin_: [[concepts/qec/abelian-lifted-product]] — GKP codes have been concatenated with Abelian LP codes  ([arXiv:2111.07029](https://arxiv.org/abs/2111.07029)) that are in turn based on QC-LDPC codes  ([doi:10.1109/TIT.2004.831841](https://doi.org/10.1109/TIT.2004.831841)). Concatenating Abelian LP codes with GKP codes can surpass the CSS Hamming bound  ([arXiv:2111.07029](https://arxiv.org/abs/2111.07029)).
- _cousin_: [[concepts/qec/quantum-parity]] — GKP codes have been concatenated with QPCs  ([arXiv:2102.01374](https://arxiv.org/abs/2102.01374)).
- _cousin_: [[concepts/qec/488-color]] — GKP codes have been concatenated with 4.8.8 color codes  ([arXiv:2112.14447](https://arxiv.org/abs/2112.14447)).
- _cousin_: [[concepts/qec/triangular-color]] — GKP codes have been concatenated with the 6.6.6 color code  ([arXiv:2411.04277](https://arxiv.org/abs/2411.04277)).
- _cousin_: [[concepts/qec/stab-5-1-3]] — GKP codes have been concatenated with the five-qubit code  ([arXiv:2411.04277](https://arxiv.org/abs/2411.04277)).
- _cousin_: [[concepts/qec/quantum-polar]] — Concatenation of GKP codes with quantum polar codes achieves a rate against the displacement channel  ([arXiv:2505.10499](https://arxiv.org/abs/2505.10499)).
- _cousin_: [[concepts/qec/stabilizer-over-gfqsq]] — Concatenations of square-lattice GKP codes with Hermitian Galois-qudit codes achieve the capacity for all loss rates  ([arXiv:2505.10499](https://arxiv.org/abs/2505.10499)).

## Notes

- Bosonic Pauli+ model is a numerical simulation tool for concatenated GKP codes  ([arXiv:2402.09333](https://arxiv.org/abs/2402.09333)).
