---
type: concept
name: Singleton-bound approaching AQECC
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/galois-css
- concepts/qec/galois-fqrs
- concepts/qec/quantum-mds
- concepts/qec/quantum-secret-sharing
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_singleton
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_singleton
---

# Singleton-bound approaching AQECC

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_singleton) (`code_id: quantum_singleton`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A member of an approximate quantum code family of rate $R$ that can tolerate adversarial errors nearly saturating the quantum Singleton bound of $(1-R)/2$.
The formulation of such codes relies on a notion of *quantum list decoding*  ([arXiv:quant-ph/0605086](https://arxiv.org/abs/quant-ph/0605086), [arXiv:2212.09935](https://arxiv.org/abs/2212.09935)).

One construction first builds constant-alphabet quantum list-decodable CSS codes from folded quantum Reed-Solomon outer codes, random CSS inner codes, and quantum Alon-Edmonds-Luby distance amplification/alphabet reduction, and then compiles them into AQECCs using purity-testing codes and robust secret sharing  ([arXiv:2212.09935](https://arxiv.org/abs/2212.09935)).
The resulting codes are efficiently encodable and decodable, and descriptions of the codes can be sampled by an efficient randomized algorithm with $2^{-\Omega(n)}$ failure probability.

(source: raw/error-correction-zoo.md)

## Protection

For any $\gamma>0$ and rate $0<R<1$, these approximate quantum $⟦n,R \cdot n⟧_q$ codes have constant Galois-qudit dimension $q=2^{O(1/\gamma^5)}$ and correct errors acting on $(1-R-\gamma) \cdot n/2$ registers, up to a recovery error of $2^{-\Omega(n)}$  ([arXiv:2212.09935](https://arxiv.org/abs/2212.09935)).

## Rate

For any target rate $R\in(0,1)$, codes can tolerate adversarial errors on nearly a $(1-R)/2$ fraction of registers while keeping constant alphabet size  ([arXiv:2212.09935](https://arxiv.org/abs/2212.09935)).

## Encoders

- Efficient encoding.

## Decoders

- Efficient decoder based on quantum list decoding together with purity-testing and robust-secret-sharing post-processing  ([arXiv:2212.09935](https://arxiv.org/abs/2212.09935)).

## Relations

- _parent_: [[concepts/qec/galois-css]]
- _parent_: [[concepts/qec/approximate-qecc]]
- _cousin_: [[concepts/qec/quantum-mds]] — Singleton-bound approaching AQECCs asymptotically approach the quantum Singleton bound, rather than exactly saturating it at finite blocklength.
- _cousin_: [[concepts/qec/galois-fqrs]] — Singleton-bound approaching AQECCs are built using folded quantum Reed-Solomon (FQRS) codes  ([arXiv:2212.09935](https://arxiv.org/abs/2212.09935)).
- _cousin_: [[concepts/qec/quantum-secret-sharing]] — Quantum secret-sharing codes have asymptotically decaying rate and require qudit dimension to increase exponentially with $n$, while Singleton-bound approaching AQECCs have constant rate and qudit dimension.
