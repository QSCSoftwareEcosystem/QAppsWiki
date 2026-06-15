---
type: concept
name: Brown-Fawzi Clifford-circuit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-stabilizer
- concepts/qec/random-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/nonlocal_lowdepth
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: nonlocal_lowdepth
---

# Brown-Fawzi Clifford-circuit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/nonlocal_lowdepth) (`code_id: nonlocal_lowdepth`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $⟦n,k⟧$ stabilizer code whose encoder is a random Clifford circuit of depth of order $O(\log^3 n)$.

An $n$-qubit quantum encoding circuit with $O(n^2 \log n)$ random two-qubit Clifford gates applied to pairs of randomly chosen qubits yields a code with distance $d$ with probability $1 - \Omega(1/n^8)$, provided that \begin{equation}
  \frac{k}{n} < 1 - \frac{d}{n}\log_2 3 - h\left(\frac{d}{n}\right)~,
\end{equation}
where $h$ is the entropy function.
Since two gates acting on disjoint qubits can be executed simultaneously, the depth of a circuit of this size is typically of order $O(\log^3 n)$.

(source: raw/error-correction-zoo.md)

## Rate

The achievable distance of these codes is asymptotically the same as a code whose encoder is a random (not necessarily log-depth) general Clifford unitary  ([arXiv:1312.7646](https://arxiv.org/abs/1312.7646)).

## Encoders

- Random $\log^3$-depth Clifford circuit.

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]]
- _parent_: [[concepts/qec/random-stabilizer]]
