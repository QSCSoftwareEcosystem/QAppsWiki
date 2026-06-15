---
type: concept
name: Single-shot code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/block-quantum
- concepts/qec/hypergraph-product
- concepts/qec/qecc-finite
- concepts/qec/self-correct
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/single_shot
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: single_shot
---

# Single-shot code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/single_shot) (`code_id: single_shot`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Block quantum qudit code whose error-syndrome weights increase linearly with the distance of the error state to the code space.

Measurement errors during decoding can yield the wrong syndrome outcome, which can cause error correction to fail even against correctable data errors.
A single-shot code is a block quantum code admitting a fault-tolerant error-correcting protocol that does not "fail too badly" when faced with noisy syndrome measurements.

The property typically implies that a sufficiently large number of error-correction rounds will keep both (sufficiently low-weight) data and measurement errors bounded, as opposed to yielding eventually uncorrectable residual errors.
The property is sufficient (but not necessary  ([arXiv:2002.05180](https://arxiv.org/abs/2002.05180))) to reduce the number of error-correction rounds required for fault-tolerant error correction.
The word "single" refers to the ability to decode well using syndrome data from only one measurement round, i.e., without using syndrome data from previous rounds.

In the loosest form of the single-shot property for qubit, modular-qudit, or Galois-qudit codes, given some data error $e$, ideal data error syndrome $s$, and measurement error $m$, there exists an error-correction protocol that outputs a correction $f$ such that the Hamming weight of the *residual error* $e-f$ is *polynomial* in the weight of $m$.
Note that the *stabilizer-reduced weight*  ([arXiv:1805.09271](https://arxiv.org/abs/1805.09271)) of $e$ is often used instead of the weight of $e$, with the justification that many decoders are designed to obtain the minimum-weight error representative.

A related property is *linear confinement*, which states that low-weight errors cause low-weight syndromes.
A code admits $(\gamma,\alpha)$ linear confinement if the (stabilizer-reduced) weight of the syndrome is proportional to the (stabilizer-reduced) weight of the data error (for data errors of weight less than $\gamma$) with proportionality constant $\alpha$.
Linear confinement is sufficient for being single shot against local stochastic noise, and more general notions of confinement are sufficient for being single shot against adversarial noise  ([arXiv:2009.11790](https://arxiv.org/abs/2009.11790)).

Under adversarial noise, good soundness of the measurement checks is a sufficient condition for the single-shot property, although it is not known to be necessary in general  ([arXiv:1805.09271](https://arxiv.org/abs/1805.09271)).

(source: raw/error-correction-zoo.md)

## Protection

A *single-shot distance* $d_{\text{ss}}$ can be defined to quantify syndrome errors, and single-shot codes have $d_{\text{ss}} = \infty$  ([arXiv:1805.09271](https://arxiv.org/abs/1805.09271)).

## Threshold

- Residual errors do not become unwieldy after some system-size-independent number of cycles of faulty syndrome measurements, and a perfect decoder would be able to recover the information if the final residual error is correctable.
Consider acting on a state $\rho$ with a noise channel $\mathcal N$ with noise rate $p$, followed by $t$ rounds of faulty syndrome measurements $\mathcal R$ with noise rate $\eta$ and one perfect recovery (which can be substituted with destructive physical-qubit measurements in practice).
The failure probability of a single-shot code should decrease exponentially with the distance of the code,
\begin{align}
  p_{\text{fail}}&=1-F\left(\mathcal{R}[\mathcal{R}_{\eta}\mathcal{N}_{p}]^{t}(\rho),\rho\right)\\&=t\left(p/p_{\star}\right)^{d}~,
\end{align}
where $F$ is a state fidelity, and where $p_{\star}$ is called the *sustainable threshold*  ([arXiv:2009.11790](https://arxiv.org/abs/2009.11790)).
For any $p$ below this threshold, some maximum measurement noise $\eta_{\star}>0$ can be tolerated after sufficiently large $t$.

The final ideal decoding step $\mathcal{R}$ cannot be done non-destructively in practice due to noisy syndrome measurements, but information can still be recovered by measuring all logical qubits in the computational basis and correcting the outcomes.
If the code is single-shot, then such a procedure will output the correct logical information.

## Relations

- _parent_: [[concepts/qec/block-quantum]]
- _parent_: [[concepts/qec/qecc-finite]]
- _cousin_: [[concepts/qec/self-correct]] — The presence of an energy barrier (i.e., confinement) is sufficient for a code to be single shot, and is also conjectured to be necessary for a code to be a self-correcting memory. Linear confinement of QLDPC (LDPC) codes implies (classical) self-correction  ([arXiv:2403.10599](https://arxiv.org/abs/2403.10599)).
- _cousin_: [[concepts/qec/hypergraph-product]] — Two-fold application of the hypergraph product to a pair of binary linear codes yields single-shot QLDPC codes that exploit redundancy in their stabilizer generators  ([arXiv:1805.09271](https://arxiv.org/abs/1805.09271)).
