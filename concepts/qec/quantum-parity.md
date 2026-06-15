---
type: concept
name: Quantum parity code (QPC)
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Subspace Shor code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ampdamp
- concepts/qec/bacon-shor
- concepts/qec/constant-excitation
- concepts/qec/generalized-shor
- concepts/qec/group-quantum-parity
- concepts/qec/majorana-stab
- concepts/qec/quantum-lego
- concepts/qec/rbh
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_parity
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_parity
---

# Quantum parity code (QPC)

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_parity) (`code_id: quantum_parity`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $⟦m_1 m_2,1,\min(m_1,m_2)⟧$ CSS code family obtained from concatenating an $m_1$-qubit bit-flip repetition code with an $m_2$-qubit phase-flip repetition code.

A set of logical codewords is
\begin{align}
\begin{split}
|\overline{0}\rangle&=\frac{1}{2^{m_2/2}}\left(|0\rangle^{\otimes m_1}+|1\rangle^{\otimes m_1}\right)^{\otimes m_2}\\
|\overline{1}\rangle&=\frac{1}{2^{m_2/2}}\left(|0\rangle^{\otimes m_1}-|1\rangle^{\otimes m_1}\right)^{\otimes m_2}~.
\end{split}
\end{align}

(source: raw/error-correction-zoo.md)

## Protection

Has distance $d=\min(m_1,m_2)$.

## Encoders

- Encoders for a recursively concatenated QPCs are related to *quantum trees*  ([arXiv:2305.03694](https://arxiv.org/abs/2305.03694), [arXiv:2306.14294](https://arxiv.org/abs/2306.14294), [arXiv:2409.13801](https://arxiv.org/abs/2409.13801)) and tree tensor networks  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).
- Linear-optical encoding  ([arXiv:0707.0903](https://arxiv.org/abs/0707.0903)).

## Decoders

- Teleportation-based QEC  ([arXiv:1310.5291](https://arxiv.org/abs/1310.5291)).

## Threshold

- All optical scheme using QPCs concatenated with either Steane or Golay codes  ([arXiv:0908.3932](https://arxiv.org/abs/0908.3932)).

## Realizations

- The $⟦m^2,1,m⟧$ codes for $m\leq 7$ have been realized in trapped-ion quantum devices  ([arXiv:2104.01205](https://arxiv.org/abs/2104.01205)).
- QPCs have been discussed independently in the context of superconducting circuits  ([arXiv:cond-mat/0403712](https://arxiv.org/abs/cond-mat/0403712)) ([doi:10.1088/0034-4885/75/7/072001](https://doi.org/10.1088/0034-4885/75/7/072001)), and aspects of such designs have been realized in experiments  ([arXiv:0802.2295](https://arxiv.org/abs/0802.2295)).

## Relations

- _parent_: [[concepts/qec/generalized-shor]]
- _parent_: [[concepts/qec/group-quantum-parity]] — A $⟦m_1 m_2,1,\min(m_1,m_2)⟧_G$ group-based QPC reduces to a QPC for $G=\mathbb{Z}_2$.
- _cousin_: [[concepts/qec/quantum-lego]] — Encoders for a recursively concatenated QPCs are related to *quantum trees*  ([arXiv:2305.03694](https://arxiv.org/abs/2305.03694), [arXiv:2306.14294](https://arxiv.org/abs/2306.14294)) and tree tensor networks  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).
- _cousin_: [[concepts/qec/bacon-shor]] — Bacon-Shor codes reduce to QPCs when all $X$-type gauge generators are fixed  ([arXiv:1809.01193](https://arxiv.org/abs/1809.01193)).
- _cousin_: [[concepts/qec/majorana-stab]] — QPCs for $m_1=m_2$ can be conveniently expressed in terms of mutually commuting Majorana operators  ([arXiv:quant-ph/0003137](https://arxiv.org/abs/quant-ph/0003137)).
- _cousin_: [[concepts/qec/constant-excitation]] — QPCs for even $m_1$ can be made into CE codes by a Pauli transformation (e.g., $XIXI\cdots XI$) applied to each block of $m_1$ qubits.
- _cousin_: [[concepts/qec/ampdamp]] — An $⟦8,1,2⟧$ QPC correcting a single AD error is equivalent to a concatenation of the $\{|\overline{01}\rangle,|\overline{11}\rangle\}$ (constant-excitation) subcode of the $⟦4,2,2⟧$ code with the dual-rail code  ([arXiv:quant-ph/0103042](https://arxiv.org/abs/quant-ph/0103042), [arXiv:quant-ph/0501184](https://arxiv.org/abs/quant-ph/0501184), [arXiv:2010.00538](https://arxiv.org/abs/2010.00538)). More generally, an $⟦m^2,1,m⟧$ QPC corrects $m-1$ AD errors  ([arXiv:1001.2356](https://arxiv.org/abs/1001.2356)).
- _cousin_: [[concepts/qec/rbh]] — QPCs can be concatenated with RBH codes  ([arXiv:2207.06805](https://arxiv.org/abs/2207.06805)).

## Notes

- Non-deterministic linear-optical encoding  ([arXiv:quant-ph/0501184](https://arxiv.org/abs/quant-ph/0501184)) whose success probability $P_{E}$ is determined by the efficiency $\eta$ of the photonic encoding circuit. A threshold $\eta > 0.82 $ exists for the efficiency, above which $P_{E}\to 1$ as $m_1\to\infty$ given particular $m_2$.
