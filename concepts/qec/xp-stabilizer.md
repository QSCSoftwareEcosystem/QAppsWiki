---
type: concept
name: XP stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Weighted hypergraph code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/clifford-hierarchy
- concepts/qec/cubic-theory
- concepts/qec/cws
- concepts/qec/invertible
- concepts/qec/quantum-lego
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/xp_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: xp_stabilizer
---

# XP stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/xp_stabilizer) (`code_id: xp_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

The XP Stabilizer formalism is a generalization of the XS and Pauli stabilizer formalisms, with stabilizer generators taken from the group $ \mathsf{BD}_{2N}^{\otimes n} = \langle\omega I, X, P\rangle^{\otimes n} $, which is the tensor product of the binary dihedral group of order $8N$.
Here, $N$ is called the *precision*, $ \omega $ is a $ 2N $th root of unity, and $ P = \text{diag} ( 1, \omega^2) $.
The codespace is a $+1$ eigenspace of a set of XP stabilizer generators, which need not commute to define a valid codespace.

XP stabilizer states are in one-to-one correspondence with weighted hypergraph states  ([arXiv:2203.00103](https://arxiv.org/abs/2203.00103)), which generalize both weighted graph states  ([arXiv:quant-ph/0407075](https://arxiv.org/abs/quant-ph/0407075), [arXiv:quant-ph/0602096](https://arxiv.org/abs/quant-ph/0602096), [arXiv:quant-ph/0602230](https://arxiv.org/abs/quant-ph/0602230)) and hypergraph states  ([arXiv:1211.5554](https://arxiv.org/abs/1211.5554), [arXiv:1404.6492](https://arxiv.org/abs/1404.6492), [arXiv:1410.3904](https://arxiv.org/abs/1410.3904)).
XP stabilizer codes are classified into XP-regular and XP-non-regular, where the former admits logical dimension $K=2^k$ (for some integer $k$) and can be mapped to a CSS code with the same diagonal logical operators and similar non-diagonal logical operators, while the latter can have arbitrary dimension, are non-additive, and resemble CWS codes  ([arXiv:2203.00103](https://arxiv.org/abs/2203.00103)).
Measurement of diagonal Pauli operators can be classically simulated efficiently on any XP code, but estimating outcome probabilities for general precision-$4$ XP operators is NP-complete and measurement can take one outside the XP formalism  ([arXiv:2203.00103](https://arxiv.org/abs/2203.00103)).

(source: raw/error-correction-zoo.md)

## Encoders

- Initialization of all qubits in the $|+\rangle$ state and action of generalized controlled $Z$ gates on multi-edges of the underlying hypergraph  ([arXiv:2203.00103](https://arxiv.org/abs/2203.00103)).

## Relations

- _parent_: [[concepts/qec/clifford-hierarchy]] — XP stabilizer codes are joint eigenspaces of operators in the binary dihedral group, a subgroup consisting of Pauli strings and elements of a level of the Clifford hierarchy.
- _cousin_: [[concepts/qec/qubit-css]] — Each XP-regular code can be mapped to a CSS code with the same diagonal logical operators and similar non-diagonal logical operators  ([arXiv:2203.00103](https://arxiv.org/abs/2203.00103)).
- _cousin_: [[concepts/qec/cws]] — The orbit representatives of XP codes play a similar role to the word operators of CWS codes, and non-XP-regular codes have a similar structure  ([arXiv:2203.00103](https://arxiv.org/abs/2203.00103)).
- _cousin_: [[concepts/qec/quantum-lego]] — XP stabilizer codes can be understood through the Quantum Lego formalism  ([arXiv:2310.19538](https://arxiv.org/abs/2310.19538)).
- _cousin_: [[concepts/qec/cubic-theory]] — The cubic theory code can be embedded into a larger codespace such that all diagonal logical operators are represented by XP operators  ([arXiv:2303.15615](https://arxiv.org/abs/2303.15615)).
- _cousin_: [[concepts/qec/invertible]] — The Chen-Hsin invertible-order code can be embedded into a larger codespace such that all diagonal logical operators are represented by XP operators  ([arXiv:2303.15615](https://arxiv.org/abs/2303.15615)).
