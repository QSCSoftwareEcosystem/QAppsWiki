---
type: concept
name: Approximate secret-sharing code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/galois-css
- concepts/qec/galois-polynomial
- concepts/qec/purity-testing
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_secret_sharing
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_secret_sharing
---

# Approximate secret-sharing code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_secret_sharing) (`code_id: quantum_secret_sharing`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A family of $ ⟦n,k,d⟧_q $ CSS codes approximately correcting errors on up to $\lfloor (n-1)/2 \rfloor$ Galois qudits, i.e., with approximate distance approaching the no-cloning bound $n/2$. Constructed using a non-degenerate CSS code, such as a polynomial quantum code, and a classical authentication scheme. The code can be viewed as a $t$-error-tolerant secret sharing scheme. Since the code yields a small logical subspace using large registers that contain both classical and quantum information, it is not useful for practical error correction problems, but instead demonstrates the power of approximate quantum error correction.

(source: raw/error-correction-zoo.md)

## Protection

Corrects up to $\lfloor (n-1)/2 \rfloor$ errors with fidelity exponentially close to 1.

## Encoders

- Uses a quantum authentication scheme, which is a keyed system in which a valid state has high fidelity, and a classical secret-sharing scheme.

## Decoders

- Decoding is analogous to reconstruction in a secret sharing scheme and is done in polynomial time. The only required operations are verification of quantum authentication, which is a pair of polynomial-time quantum algorithms that check if the fidelity of the received state is close to 1, and erasure correction for a stabilizer code, which involves solving a system of linear equations.

## Relations

- _parent_: [[concepts/qec/galois-css]] — The code required to construct this code must be a non-degenerate Galois-qudit CSS code.
- _cousin_: [[concepts/qec/approximate-qecc]] — Secret-sharing codes approximately correct errors on up to $\lfloor (n-1)/2 \rfloor$ errors.
- _cousin_: [[concepts/qec/galois-polynomial]] — Polynomial codes can be used for a specific construction of this code.
- _cousin_: [`reed_solomon`](https://errorcorrectionzoo.org/c/reed_solomon) — The classical information in this code is encoded using an RS code.
- _cousin_: [[concepts/qec/purity-testing]] — The purity-testing protocol of Ref.  ([arXiv:quant-ph/0205128](https://arxiv.org/abs/quant-ph/0205128)) can be improved using approximate codes similar to the approximate secret-sharing codes  ([arXiv:0801.1544](https://arxiv.org/abs/0801.1544)).
