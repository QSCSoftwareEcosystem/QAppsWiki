---
type: concept
name: Bosonic quantum Fourier code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-representation
- concepts/qec/pauli-qsc
- concepts/qec/qsc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/fourier_bosonic
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: fourier_bosonic
---

# Bosonic quantum Fourier code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/fourier_bosonic) (`code_id: fourier_bosonic`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Two-mode non-uniform QSC encoding two logical qubits whose projection is onto a copy of an irreducible representation of the single-qubit Pauli group.
This code is an extension of the single-logical-qubit code in  ([arXiv:2306.11621](https://arxiv.org/abs/2306.11621)), storing an extra logical qubit in the multiplicity space of the Pauli group.

The code admits the following basis of codewords for complex $\alpha > 0$, up to normalization:
\begin{align}
\begin{split}
|\overline{0,0}\rangle&\propto\left(\left|\alpha\right\rangle -\left|-\alpha\right\rangle \right)\left(\left|i\alpha\right\rangle +\left|-i\alpha\right\rangle \right)\\
|\overline{0,1}\rangle&\propto\left(\left|i\alpha\right\rangle -\left|-i\alpha\right\rangle \right)\left(\left|\alpha\right\rangle +\left|-\alpha\right\rangle \right)\\
|\overline{1,0}\rangle&\propto\left(\left|i\alpha\right\rangle +\left|-i\alpha\right\rangle \right)\left(\left|\alpha\right\rangle -\left|-\alpha\right\rangle \right)\\
|\overline{1,1}\rangle&\propto\left(\left|\alpha\right\rangle +\left|-\alpha\right\rangle \right)\left(\left|i\alpha\right\rangle -\left|-i\alpha\right\rangle \right)
\end{split}
\end{align}

(source: raw/error-correction-zoo.md)

## General gates

- The single-qubit Pauli group can be realized via Gaussian rotations  ([arXiv:2505.16618](https://arxiv.org/abs/2505.16618)).
- Kerr interactions yield some Clifford gates. There is a Hadamard gate, up to a global rotation  ([arXiv:2505.16618](https://arxiv.org/abs/2505.16618)).
- A logical $ZZ$-gate can be performed using squeezing operators and quantum Zeno effect  ([arXiv:2505.16618](https://arxiv.org/abs/2505.16618)).

## Decoders

- The code is stabilized by the two-mode parity operator and annihilated by the operators $\hat{a}_1^4 - \alpha^4$ and $\hat{a}_1^2 \hat{a}_2^2 + \alpha^4$  ([arXiv:2505.16618](https://arxiv.org/abs/2505.16618)).

## Relations

- _parent_: [[concepts/qec/qsc]] — The bosonic quantum Fourier code has non-uniform $\pm 1$ coefficients.
- _parent_: [[concepts/qec/group-representation]] — The bosonic quantum Fourier code is a group-representation code with $G$ being the single-qubit Pauli group.
- _cousin_: [[concepts/qec/pauli-qsc]] — The bosonic quantum Fourier code and the Pauli group-representation QSC are both group-representation codes with $G$ being the single-qubit Pauli group.
