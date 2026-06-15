---
type: concept
name: NTRU-GKP code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/multimodegkp
- concepts/qec/quantum-random
- concepts/qec/qudits-into-oscillators
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ntru_gkp
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ntru_gkp
---

# NTRU-GKP code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ntru_gkp) (`code_id: ntru_gkp`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Multi-mode GKP code whose underlying lattice is utilized in variations of the NTRU cryptosystem  ([doi:10.1007/BFb0054868](https://doi.org/10.1007/BFb0054868)).
Randomized constructions yield constant-rate GKP code families whose largest decodable displacement length scales as $O(\sqrt{n})$ with high probability.

The integer-valued $q$-symplectic Gram matrix for an $n$-mode $k$-qubit good NTRU-GKP code is
\begin{align}
  A = \sqrt{\frac{2}{q}}\begin{pmatrix}I & Q\\
  0 & qI
  \end{pmatrix}~,
\end{align}
where $Q$ is a circulant matrix constructed from coefficients of a cyclic polynomial used in the NTRU cryptosystem, and $I$ is the $n$-dimensional identity matrix  ([arXiv:2303.02432](https://arxiv.org/abs/2303.02432)).

(source: raw/error-correction-zoo.md)

## Rate

Randomized constructions yield constant-rate GKP code families whose largest decodable displacement length scales as $O(\sqrt{n})$ with high probability.

## Decoders

- Babai's nearest plane algorithm  ([doi:10.1007/bf02579403](https://doi.org/10.1007/bf02579403)) can be used for bounded-distance decoding.
- An NTRU-based decoder against stochastic displacement noise is efficient because the decoding problem is equivalent to decrypting the NTRU cryptosystem with knowledge of the encoder.

## Code capacity threshold

- A lower bound on the threshold for displacement noise can be formulated in terms of code parameters  ([arXiv:2303.02432](https://arxiv.org/abs/2303.02432)).

## Realizations

- Public-key NTRU-based quantum communication protocol  ([arXiv:2303.02432](https://arxiv.org/abs/2303.02432)).

## Relations

- _parent_: [[concepts/qec/multimodegkp]]
- _parent_: [[concepts/qec/qudits-into-oscillators]]
- _cousin_: [[concepts/qec/quantum-random]] — Several NTRU lattices come from randomized constructions, yielding constant-rate GKP code families whose largest decodable displacement length scales as $O(\sqrt{n})$ with high probability.
