---
type: concept
name: $⟦3,1,2⟧_4$ three-Galois-quartrit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/carbon
- concepts/qec/galois-polynomial
- concepts/qec/galois-quad-residue
- concepts/qec/quantum-mds
- concepts/qec/small-distance-quantum
- concepts/qec/stab-6-2-2
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_3_1_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_3_1_2
---

# $⟦3,1,2⟧_4$ three-Galois-quartrit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_3_1_2) (`code_id: galois_3_1_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Three-Galois-qudit CSS code over $\mathbb{F}_4=\{0,1,\omega,\omega^2\}$ that encodes one logical Galois qudit and detects a single-qudit error.

Its $X$- and $Z$-type stabilizer check matrices are both
\begin{align}
  H_X=H_Z=\begin{pmatrix}1&\omega&\omega^2\end{pmatrix}~.
\end{align}
Since the code is a true stabilizer code, multiplication of this row by $\omega$ or $\omega^2$ also yields stabilizers  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).

(source: raw/error-correction-zoo.md)

## Protection

Detects a single Galois-qudit error. It is a quantum MDS code, saturating the quantum Singleton bound.

## Relations

- _parent_: [[concepts/qec/galois-polynomial]] — The $⟦3,1,2⟧_4$ code is constructed from the shortened RS$_4$ code  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- _parent_: [[concepts/qec/galois-quad-residue]] — The $⟦3,1,2⟧_4$ code is constructed from the shortened RS$_4$ code  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- _parent_: [[concepts/qec/quantum-mds]] — The $⟦3,1,2⟧_4$ code saturates the quantum Singleton bound.
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [`reed_solomon_4`](https://errorcorrectionzoo.org/c/reed_solomon_4) — The $⟦3,1,2⟧_4$ code is constructed from the shortened RS$_4$ code  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- _cousin_: [[concepts/qec/stab-6-2-2]] — Binarizing the $⟦3,1,2⟧_4$ code in the self-dual normal basis $\{\omega,\omega^2\}$ yields a $⟦6,2,2⟧$ qubit CSS code equivalent to the $C_6$ code after the qubit relabeling $(2\,3\,4\,5\,6)$  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- _cousin_: [[concepts/qec/carbon]] — Binarizing this code and concatenating each qubit pair with the $⟦4,2,2⟧$ code yields the $⟦12,2,4⟧$ carbon code  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
