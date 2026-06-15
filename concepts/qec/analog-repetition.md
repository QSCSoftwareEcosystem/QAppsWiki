---
type: concept
name: Analog repetition code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Gaussian repetition code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/1d-stabilizer
- concepts/qec/ame
- concepts/qec/analog-stabilizer
- concepts/qec/group-quantum-repetition
- concepts/qec/niset-andersen-cerf
- concepts/qec/oscillator-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/analog_repetition
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: analog_repetition
---

# Analog repetition code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/analog_repetition) (`code_id: analog_repetition`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $⟦n,1⟧_{\mathbb{R}}$ analog stabilizer version of the quantum repetition code, encoding the position states of one mode into an odd number $n$ of modes.

There are two variants, a bit- and a phase-flip code, whose encoding for $n=3$ is
\begin{align}
  |\overline{x}_{\text{bit}}\rangle&\rightarrow|x,x,x\rangle\\
  |\overline{x}_{\text{phase}}\rangle&\rightarrow \int dx_{1}dx_{2}dx_{3}\delta(x_{1}+x_{2}+x_{3}-x)|x_{1},x_{2},x_{3}\rangle~.
\end{align}

Nullifiers for the bit-flip analog repetition code are differences $\hat{x}_{j+1} - \hat{x}_{j}$.
Bit-flip codewords can be superposed to yield the logical momentum basis of *analog GHZ states*
\begin{align}
  |\overline{p}\rangle=\int dx e^{ipx}|x\rangle^{\otimes n}~,
\end{align}
a bosonic version of GHZ states.
At $p=0$, the above is an analog stabilizer state nullified by the bit-flip nullifiers and the total momentum operator $\hat{p}_1+\hat{p}_2+\cdots+\hat{p}_n$  ([doi:10.1002/1521-3978(200212)50:12<1177::AID-PROP1177>3.0.CO;2-T](https://doi.org/10.1002/1521-3978(200212)50:12<1177::AID-PROP1177>3.0.CO;2-T)).
For $n=2$, this state is known as an *EPR pair*  ([doi:10.1103/PhysRev.47.777](https://doi.org/10.1103/PhysRev.47.777)), an infinitely squeezed version of the two-mode squeezed (TMS) a.k.a. twin-beam state.

(source: raw/error-correction-zoo.md)

## Realizations

- Quantum teleportation  ([doi:10.1038/nature02858](https://doi.org/10.1038/nature02858)), secret sharing  ([arXiv:quant-ph/0311015](https://arxiv.org/abs/quant-ph/0311015)), and superdense coding  ([arXiv:quant-ph/0210132](https://arxiv.org/abs/quant-ph/0210132)) protocols have been realized with analog GHZ states for $n=2,3$.

## Relations

- _parent_: [[concepts/qec/analog-stabilizer]]
- _parent_: [[concepts/qec/oscillator-css]]
- _parent_: [[concepts/qec/1d-stabilizer]]
- _parent_: [[concepts/qec/group-quantum-repetition]] — Group-based quantum repetition codes reduce to analog repetition codes for $G = \mathbb{R}$.
- _cousin_: [[concepts/qec/niset-andersen-cerf]] — EPR pairs are used in an encoding of the Niset-Andersen-Cerf code  ([arXiv:0710.4858](https://arxiv.org/abs/0710.4858)).
- _cousin_: [[concepts/qec/ame]] — Analog GHZ states are $1$-uniform for all $n$ and CV AME for $n=2,3$  ([arXiv:0901.1488](https://arxiv.org/abs/0901.1488), [arXiv:2503.15698](https://arxiv.org/abs/2503.15698)).

## Notes

- Analog GHZ states are useful for quantum teleportation  ([arXiv:quant-ph/9906021](https://arxiv.org/abs/quant-ph/9906021)).
