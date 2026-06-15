---
type: concept
name: $((n,2,2))$ Bravyi-Lee-Li-Yoshida PI code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/movassagh-ouyang
- concepts/qec/qubit-concatenated
- concepts/qec/qubit-permutation-invariant
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/unentangled_permutation_invariant
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: unentangled_permutation_invariant
---

# $((n,2,2))$ Bravyi-Lee-Li-Yoshida PI code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/unentangled_permutation_invariant) (`code_id: unentangled_permutation_invariant`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

PI distance-two code on $n\geq4$ qubits whose degree of entanglement vanishes asymptotically with $n$  ([arXiv:2405.01332](https://arxiv.org/abs/2405.01332)) (cf.  ([arXiv:0704.0251](https://arxiv.org/abs/0704.0251))).

In terms of Dicke states, the codewords are
\begin{align}
  \begin{split}
    |0_{L}\rangle&=\sqrt{1-\frac{2}{n}}|D_{0}^{n}\rangle+\sqrt{\frac{2}{n}}|D_{n}^{n}\rangle\\
    |1_{L}\rangle&=|D_{2}^{n}\rangle~.
  \end{split}
\end{align}

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qubit-permutation-invariant]]
- _parent_: [[concepts/qec/movassagh-ouyang]] — The $((n,2,2))$ PI code is a Movassagh-Ouyang Hamiltonian code constructed from a binary code consisting of all codewords of weight 0, 2, or $n$  ([arXiv:2405.01332](https://arxiv.org/abs/2405.01332)).
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/qubit-concatenated]] — The Bravyi-Lee-Li-Yoshida PI code can be concatenated to yield codes that have higher distance and that admit codewords with vanishing entanglement  ([arXiv:2405.01332](https://arxiv.org/abs/2405.01332)) (cf.  ([arXiv:0704.0251](https://arxiv.org/abs/0704.0251))).
