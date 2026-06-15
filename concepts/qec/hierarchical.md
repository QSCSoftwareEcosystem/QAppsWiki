---
type: concept
name: Hierarchical code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qldpc
- concepts/qec/qubit-concatenated
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hierarchical
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hierarchical
---

# Hierarchical code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hierarchical) (`code_id: hierarchical`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of $⟦n,k,d⟧$ qubit stabilizer codes resulting from a concatenation of a constant-rate QLDPC code with a rotated surface code.
Concatenation allows for syndrome extraction to be performed on a 2D geometry while maintaining a threshold at the expense of a logarithmically vanishing rate.
The growing syndrome extraction circuit depth allows known bounds in the literature to be weakened  ([arXiv:2109.14599](https://arxiv.org/abs/2109.14599), [arXiv:2302.04317](https://arxiv.org/abs/2302.04317)).

(source: raw/error-correction-zoo.md)

## Rate

Rate scales as $\Omega(1/\log(n)^2)$.

## Decoders

- Decoding is performed as in a standard concatenated code using decoders for the inner and outer codes. The syndrome extraction circuit depth for the outer code is optimized using a permutation routing algorithm  ([doi:10.1145/97444.97707](https://doi.org/10.1145/97444.97707)). The bilayer architecture allows for logical entangling gates between logical surface-code patches.
- Soft output decoding  ([arXiv:2405.07433](https://arxiv.org/abs/2405.07433)).

## Threshold

- Threshold exists for the locally decaying error model; see  ([arXiv:2303.04798](https://arxiv.org/abs/2303.04798)). However, the logical error rate below threshold falls super-polynomially (as opposed to exponentially) with the code distance. The code family possesses a threshold equal to that of surface codes given by tuning the inner code size for any fixed physical error rate.

## Fault tolerance

- 2D geometrically local syndrome extraction circuits of depth of order $O(\sqrt{n}/R)$ that utilize Clifford and SWAP gates of range $R$ and that require order $O(n)$ data and ancilla qubits. Such parameters (including a range of one) are possible while maintaining a threshold because of the concatenation step. This reduces the noise that would otherwise accumulate within a growing-depth syndrome extraction circuit. A key idea is that constant-depth syndrome extraction is not a necessary condition for fault-tolerance.

## Relations

- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/qubit-concatenated]] — Using the concatenation convention of the Zoo, hierarchical codes are concatenations of constant-rate QLDPC (inner) codes with rotated surface (outer) codes. The cited paper  ([arXiv:2303.04798](https://arxiv.org/abs/2303.04798)) uses the opposite inner/outer terminology. The block length of the outer code is picked to grow logarithmically with the block length of the inner code.
