---
type: concept
name: Quantum AG code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-true-stabilizer
- concepts/qec/quantum-triorthogonal
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_ag
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_ag
---

# Quantum AG code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_ag) (`code_id: quantum_ag`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

True Galois-qudit stabilizer code constructed from evaluation AG codes via the Galois-qudit Hermitian construction or the Galois-qudit CSS construction.

(source: raw/error-correction-zoo.md)

## Rate

Quantum AG codes can be asymptotically good  ([arXiv:quant-ph/0107102](https://arxiv.org/abs/quant-ph/0107102), [arXiv:quant-ph/0107129](https://arxiv.org/abs/quant-ph/0107129)). There exist three such families  ([arXiv:2408.07764](https://arxiv.org/abs/2408.07764), [arXiv:2408.09254](https://arxiv.org/abs/2408.09254), [arXiv:2408.10140](https://arxiv.org/abs/2408.10140)) that admit a diagonal transversal gate at the third level of the \term{Clifford hierarchy}.

## Magic scaling exponent

By defining a generalization of triorthogonal matrices to Galois qudits of dimension $q=2^m$, one can construct an asymptotically good family of quantum AG codes that admits a diagonal transversal gate at the third level of the \term{Clifford hierarchy} and attains a zero magic-state yield parameter, $\gamma = 0$  ([arXiv:2408.07764](https://arxiv.org/abs/2408.07764)). This code can be treated as a qubit code by decomposing each Galois qudit into a Kronecker product of $m$ qubits; see  ([doi:10.1109/18.959288](https://doi.org/10.1109/18.959288)) ([arXiv:quant-ph/0501074](https://arxiv.org/abs/quant-ph/0501074)) ([arXiv:2408.10140](https://arxiv.org/abs/2408.10140), [arXiv:2408.09254](https://arxiv.org/abs/2408.09254)). Two other asymptotically good families  ([arXiv:2408.09254](https://arxiv.org/abs/2408.09254), [arXiv:2408.10140](https://arxiv.org/abs/2408.10140)) admit a transversal $CCZ$ gate (a different diagonal gate at the third level of the \term{Clifford hierarchy}) and achieve $\gamma \to 0$ with constant alphabet size.

## Encoders

- Encoding defined in Ref.  ([arXiv:quant-ph/0107129](https://arxiv.org/abs/quant-ph/0107129)) uses a technique from Ref.  ([arXiv:quant-ph/0005008](https://arxiv.org/abs/quant-ph/0005008)) to encode quantum stabilizer codes.

## Transversal gates

- There exist three asymptotically good code families  ([arXiv:2408.07764](https://arxiv.org/abs/2408.07764), [arXiv:2408.09254](https://arxiv.org/abs/2408.09254), [arXiv:2408.10140](https://arxiv.org/abs/2408.10140)) that admit a diagonal transversal gate at the third level of the \term{Clifford hierarchy}.
- By decomposing each Galois qudit into a Kronecker product of qubits, the family of Ref.  ([arXiv:2408.10140](https://arxiv.org/abs/2408.10140)) yields an explicit asymptotically good qubit CSS code family with parameters $⟦N,K=\Theta(N),D=\Theta(N)⟧$ on which $\overline{CCZ}^{\otimes K}$ is realized by a transversal application of physical $CCZ$ gates on a constant fraction of qubits.
- There exists an asymptotically good code family that admits three-Galois-qudit non-Clifford gates for any three logical Galois qudits  ([arXiv:2502.01864](https://arxiv.org/abs/2502.01864)).

## Relations

- _parent_: [[concepts/qec/galois-true-stabilizer]] — Quantum AG codes can be constructed via the Galois-qudit CSS construction or the Galois-qudit Hermitian construction.
- _cousin_: [`evaluation`](https://errorcorrectionzoo.org/c/evaluation) — Quantum AG codes are quantum analogues of evaluation AG codes.
- _cousin_: [[concepts/qec/quantum-triorthogonal]] — By defining a generalization of triorthogonal matrices to Galois qudits of dimension $q=2^m$, one can construct an asymptotically good family of quantum AG codes that admits a diagonal transversal gate at the third level of the \term{Clifford hierarchy} and attains a zero magic-state yield parameter, $\gamma = 0$  ([arXiv:2408.07764](https://arxiv.org/abs/2408.07764)). This code can be treated as a qubit code by decomposing each Galois qudit into a Kronecker product of $m$ qubits; see  ([doi:10.1109/18.959288](https://doi.org/10.1109/18.959288)) ([arXiv:quant-ph/0501074](https://arxiv.org/abs/quant-ph/0501074)) ([arXiv:2408.10140](https://arxiv.org/abs/2408.10140), [arXiv:2408.09254](https://arxiv.org/abs/2408.09254)). Two other asymptotically good families  ([arXiv:2408.09254](https://arxiv.org/abs/2408.09254), [arXiv:2408.10140](https://arxiv.org/abs/2408.10140)) admit a transversal $CCZ$ gate (a different diagonal gate at the third level of the \term{Clifford hierarchy}) and achieve $\gamma \to 0$ with constant alphabet size.
- _cousin_: [`shimura`](https://errorcorrectionzoo.org/c/shimura) — The AG codes used in an asymptotically good construction of quantum AG codes with non-Clifford transversal gates  ([arXiv:2408.09254](https://arxiv.org/abs/2408.09254)) are those of the TVZ codes.
- _cousin_: [`elliptic`](https://errorcorrectionzoo.org/c/elliptic) — Elliptic codes can be used to construct quantum AG codes  ([arXiv:2110.00769](https://arxiv.org/abs/2110.00769)).
