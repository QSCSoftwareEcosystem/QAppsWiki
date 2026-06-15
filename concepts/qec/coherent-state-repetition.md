---
type: concept
name: Coherent-state repetition code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cat-concatenated
- concepts/qec/cat-repetition
- concepts/qec/quantum-repetition
- concepts/qec/tiger
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/coherent_state_repetition
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: coherent_state_repetition
---

# Coherent-state repetition code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/coherent_state_repetition) (`code_id: coherent_state_repetition`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A concatenated qubit-into-$n$-mode code (for odd $n$) whose inner code is a quantum repetition code and whose outer code is the two-component cat code in its coherent-state basis. 

A basis of codewords is
\begin{align}
  |\overline{\pm}\rangle\propto\left|\pm\alpha\right\rangle ^{\otimes n}
\end{align}
for $|\alpha| > 0$.

(source: raw/error-correction-zoo.md)

## Protection

For odd $n$, the code has $d_X=1$ and minimum Euclidean distance $d_Z = 4n$  ([arXiv:2411.09668](https://arxiv.org/abs/2411.09668)), so it does not protect against losses but suppresses dephasing exponentially in $n|\alpha|^2$.

## Encoders

- Lindbladian-based dissipative encoding with dissipators $\hat{a}_j \hat{a}_k - \alpha^2$ for neighboring modes $j,k$ on a 1D line as well as local dissipators $\hat{a}_j^2 - \alpha^2$. Encoding passively protects against cavity dephasing.

## Relations

- _parent_: [[concepts/qec/cat-concatenated]] — The coherent-state repetition code is a concatenation whose outer code is the cat code in its coherent-state basis.
- _parent_: [[concepts/qec/tiger]] — For odd $n$, the coherent-state repetition code is a tiger code whose matrix $G$ is the cyclic repetition generator matrix over the integers and whose matrix $H$ is zero  ([arXiv:2411.09668](https://arxiv.org/abs/2411.09668)). For even $n$, or after removing the last row to impose open boundaries, the construction yields a logical-rotor variant instead of a logical qubit.
- _cousin_: [[concepts/qec/cat-repetition]] — The cat (coherent-state) repetition code is a concatenation whose outer code is the (two-component) cat code in its cat (coherent-state) basis. For the two-component case, both reduce to the two-component cat code at $n=1$.
- _cousin_: [[concepts/qec/quantum-repetition]] — Two-component cat codes in the coherent-state basis have been concatenated with quantum repetition codes  ([arXiv:quant-ph/0109077](https://arxiv.org/abs/quant-ph/0109077), [arXiv:quant-ph/0306004](https://arxiv.org/abs/quant-ph/0306004)).
