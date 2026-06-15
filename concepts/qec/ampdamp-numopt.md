---
type: concept
name: Numerically optimized four-qubit AD code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ampdamp
- concepts/qec/css-4-1-2
- concepts/qec/numopt
- concepts/qec/qubits-into-qubits
- concepts/qec/reinforcement-learning
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ampdamp_numopt
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ampdamp_numopt
---

# Numerically optimized four-qubit AD code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ampdamp_numopt) (`code_id: ampdamp_numopt`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

One of several four-qubit codes that can (approximately) correct a single AD error with higher fidelity than the $⟦4,1,2⟧$ subcodes of the $⟦4,2,2⟧$ code.

A code obtained by a biconvex optimization of the entanglement fidelity admits a codeword basis of  ([arXiv:2411.12952](https://arxiv.org/abs/2411.12952))
\begin{align}
\begin{split}
|\overline{0}\rangle&=\sqrt{1-\frac{1}{2(1-\gamma)^{2}}}|0000\rangle+\frac{1}{\sqrt{2}(1-\gamma)}|1111\rangle\\
|\overline{1}\rangle&=\frac{1}{2}(|0011\rangle+|0101\rangle-|1010\rangle+|1100\rangle)
\end{split}
\end{align}
for AD error rate $\gamma$.
Another code, obtained from a machine-learning optimization  ([arXiv:2503.11783](https://arxiv.org/abs/2503.11783)), admits a codeword basis of
\begin{align}
\begin{split}
|\bar{0}\rangle&=\sqrt{\frac{1}{1+(1-\gamma)^{-4}}}\left(|0000\rangle+(1-\gamma)^{-2}|1111\rangle\right)\\
|\bar{1}\rangle&=\sqrt{\frac{1}{2}}\left(|0011\rangle+|1100\rangle\right).
\end{split}
\end{align}

(source: raw/error-correction-zoo.md)

## Encoders

- Analytical encoding channel  ([arXiv:2411.12952](https://arxiv.org/abs/2411.12952)).

## Decoders

- Analytical recovery channel  ([arXiv:2411.12952](https://arxiv.org/abs/2411.12952)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/ampdamp]]
- _parent_: [[concepts/qec/numopt]] — Numerically optimized four-qubit AD codes can be obtained from a biconvex optimization of the entanglement fidelity  ([arXiv:2411.12952](https://arxiv.org/abs/2411.12952)).
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/css-4-1-2]] — The numerically optimized four-qubit AD code can correct a single AD error with higher entanglement fidelity than the $⟦4,1,2⟧$ LNCY code  ([arXiv:quant-ph/9704002](https://arxiv.org/abs/quant-ph/9704002)).
- _cousin_: [[concepts/qec/reinforcement-learning]] — Numerically optimized four-qubit AD codes can be obtained from a machine-learning optimization  ([arXiv:2503.11783](https://arxiv.org/abs/2503.11783)).
