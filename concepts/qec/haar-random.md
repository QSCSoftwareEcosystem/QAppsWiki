---
type: concept
name: Haar-random qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/local-haar-random
- concepts/qec/qubits-into-qubits
- concepts/qec/random-circuit
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/haar_random
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: haar_random
---

# Haar-random qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/haar_random) (`code_id: haar_random`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Haar-random codewords are generated in a process involving averaging over unitary operations distributed according to the Haar measure. Haar-random codes are used to prove statements about the capacity of a quantum channel to transmit quantum information  ([arXiv:1106.1445](https://arxiv.org/abs/1106.1445)), but encoding and decoding in such $n$-qubit codes quickly becomes impractical as $n\to\infty$.

There are different approaches to create Haar-random codewords. In the construction of Ref.  ([arXiv:quant-ph/0702005](https://arxiv.org/abs/quant-ph/0702005)), codewords are produced by performing a unitarily covariant projective measurement on a *typical* subspace of a tensor-power state. Reference  ([arXiv:quant-ph/0702005](https://arxiv.org/abs/quant-ph/0702005)) showed that coherent-information rates are achievable by encoding in such Haar-random codes. In particular, Haar-random codes achieve asymptotically vanishing decoding error in the $n\to\infty$ limit by proving that the encoded information becomes decoupled from the environment. This is a necessary and sufficient condition for successful decoding since measurements of the environment should never reveal the encoded information  ([arXiv:quant-ph/9604022](https://arxiv.org/abs/quant-ph/9604022)).

Intuitively, coupling with the environment can be decreased by projecting the system onto a random codespace. The more qubits that are randomly discarded, the more the codespace is decoupled from the environment. One may ask what is the least amount of qubits that can be discarded, i.e. the largest remaining codespace, that still achieves decoupling. It can be shown through the decoupling inequality  ([arXiv:quant-ph/0512247](https://arxiv.org/abs/quant-ph/0512247)) that the largest possible dimension of the random codespace that achieves arbitrarily large decoupling is exponential in the coherent information of the channel. Therefore, there exist codes that can transmit information at rates governed by coherent information. Furthermore, these codes can be constructed with high probability by performing a Haar-random isometry embedding $k$ logical qubits into an $n$-qubit physical space. Such an isometry can be produced by QR decomposition of a Gaussian random matrix  ([doi:10.1137/0717034](https://doi.org/10.1137/0717034)).

(source: raw/error-correction-zoo.md)

## Rate

Haar-random qubit codes attain the regularized coherent information of certain noise channels in the limit of large $n$  ([arXiv:quant-ph/0701102](https://arxiv.org/abs/quant-ph/0701102)).

## Threshold

- Haar-random qubit codes have a measurement threshold of one  ([arXiv:2402.00145](https://arxiv.org/abs/2402.00145)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/random-circuit]]
- _cousin_: [[concepts/qec/local-haar-random]] — Approximating the random projections through $t$-designs is necessary in order to make the Haar-random qubit protocol practical. Replacing with random Clifford gates is especially convenient since the Clifford group forms a unitary 2-design and produces stabilizer codes.
- _cousin_: [`clifford_group`](https://errorcorrectionzoo.org/c/clifford_group) — Approximating the random projections through $t$-designs is necessary in order to make the Haar-random qubit protocol practical. Replacing with random Clifford gates is especially convenient since the Clifford group forms a unitary 2-design and produces stabilizer codes.
