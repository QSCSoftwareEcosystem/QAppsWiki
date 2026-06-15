---
type: concept
name: High-dimensional expander (HDX) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/distance-balanced
- concepts/qec/freedman-meyer-luo
- concepts/qec/homological-product
- concepts/qec/hypergraph-product
- concepts/qec/iterated-ramanujan
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ramanujan_tensor_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ramanujan_tensor_product
---

# High-dimensional expander (HDX) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ramanujan_tensor_product) (`code_id: ramanujan_tensor_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

CSS code obtained by applying the generalized distance-balancing/product construction of Ref.  ([arXiv:2004.07935](https://arxiv.org/abs/2004.07935)) to a Ramanujan-complex quantum code and an asymptotically good classical LDPC code.

Ramanujan quantum codes are defined using LSV Ramanujan complexes, which are simplicial complexes that generalize Ramanujan graphs  ([doi:10.1007/BF02126799](https://doi.org/10.1007/BF02126799), [doi:10.1017/CBO9780511615825](https://doi.org/10.1017/CBO9780511615825)).
The auxiliary classical code is viewed as a 1-dimensional chain complex, and the output code is defined on the co-complex of the product of the two co-complexes.
Using a 2D LSV complex yields a QLDPC family with $K=\Omega(\sqrt{n/\log n})$ and $D=\Omega(\sqrt{n \log n})$, while using a 3D LSV complex yields $K=\Omega(\sqrt{n}/\log n)$ and $D=\Omega(\sqrt{n}\log n)$.

(source: raw/error-correction-zoo.md)

## Protection

The unbalanced component code from a 2D LSV complex can have $d_X=\Omega(\log n)$ and $d_Z=\Omega(n)$, while one from a 3D LSV complex can have $d_X=\Omega(\log^2 n)$ and $d_Z=\Omega(n)$  ([arXiv:2004.07935](https://arxiv.org/abs/2004.07935)). After distance balancing, the resulting HDX family has minimum distance $D=\Omega(\sqrt{n \log n})$ in the 2D case and $D=\Omega(\sqrt{n}\log n)$ in the 3D case.

## Rate

For 2D LSV complexes, the rate is of order $\Omega(1/\sqrt{n \log n})$, with minimum distance $D=\Omega(\sqrt{n \log n})$. For 3D LSV complexes, the rate is $\Omega( 1/(\sqrt{n}\log n) )$, with minimum distance $D=\Omega(\sqrt{n}\log n)$.

## Decoders

- For HDX codes built from 2D LSV complexes, $X$-error decoding reduces to polynomial-time cycle-code decoding on the 1-skeleton together with decoding of the auxiliary classical LDPC code  ([arXiv:2004.07935](https://arxiv.org/abs/2004.07935)).
- For the 2D construction, $Z$-errors of linear weight admit a local decoder based on coboundary expansion; replacing the component complex by the 2-skeleton of a 3D LSV complex preserves 2D-type asymptotic parameters while giving linear-time $Z$-decoding with unit-weight local corrections  ([arXiv:2004.07935](https://arxiv.org/abs/2004.07935)).

## Relations

- _parent_: [[concepts/qec/homological-product]] — Ramanujan codes result from a tensor product of a classical-code and a quantum-code chain complex.
- _parent_: [[concepts/qec/iterated-ramanujan]] — Ramanujan codes result from a tensor product of a classical-code and a quantum-code chain complex.
- _cousin_: [[concepts/qec/distance-balanced]] — Ramanujan tensor-product constructions use distance balancing to increase distance.
- _cousin_: [[concepts/qec/hypergraph-product]] — Ramanujan codes utilize the hypergraph product with a twist, which is an automorphism on one of the complexes in the tensor product, in order to increase distance  ([arXiv:2103.06309](https://arxiv.org/abs/2103.06309)).
- _cousin_: [[concepts/qec/freedman-meyer-luo]] — Ramanujan codes broke 20-year record on minimum code distance set by Freedman-Meyer-Luo codes.

## Notes

- Codes were first to break a 20-year record set by the Freedman-Meyer-Luo code for the lower bound on scaling of the minimum distance  ([arXiv:2103.06309](https://arxiv.org/abs/2103.06309)).
