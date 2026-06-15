---
type: concept
name: Numerically optimized bosonic code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/multimodegkp
- concepts/qec/oscillators
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/numopt
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: numopt
---

# Numerically optimized bosonic code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/numopt) (`code_id: numopt`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Bosonic Fock-state code obtained from a numerical minimization procedure, e.g., from enforcing error-correction criteria against some number of losses while minimizing average occupation number. Useful single-mode codes can be determined using basic numerical optimization  ([arXiv:1602.00008](https://arxiv.org/abs/1602.00008), [arXiv:1708.05010](https://arxiv.org/abs/1708.05010)), semidefinite-program recovery/encoding optimization  ([arXiv:1801.07271](https://arxiv.org/abs/1801.07271), [arXiv:2205.00341](https://arxiv.org/abs/2205.00341)), or reinforcement learning  ([arXiv:2108.02766](https://arxiv.org/abs/2108.02766), [arXiv:2212.11651](https://arxiv.org/abs/2212.11651)).

The smallest numerically optimized Fock-state code protecting against a single loss error is the $\sqrt(17)$ code  ([arXiv:1602.00008](https://arxiv.org/abs/1602.00008)),
\begin{align}
\begin{split}
|\overline{0}\rangle&=\frac{1}{\sqrt{6}}\left(\sqrt{7-\sqrt{17}}|0\rangle+\sqrt{\sqrt{17}-1}|3\rangle\right)\\
|\overline{1}\rangle&=\frac{1}{\sqrt{6}}\left(\sqrt{9-\sqrt{17}}|1\rangle-\sqrt{\sqrt{17}-3}|4\rangle\right)~,
\end{split}
\end{align}
correcting a single loss error. The average occupation number of the codewords is $\approx 1.6$, which is $0.4$ photons lower than that of the smallest binomial code with the same level of protection.

(source: raw/error-correction-zoo.md)

## Protection

Numerically optimized bosonic codes can be designed to protect against a finite number of loss events while minimizing resources such as the average occupation number. Many such codes are approximate QECCs.

## Relations

- _parent_: [[concepts/qec/oscillators]]
- _cousin_: [[concepts/qec/multimodegkp]] — Numerically optimizing GKP code lattices yields codes for three, seven, and nine modes with larger distances and fidelities than known GKP codes  ([arXiv:2303.04702](https://arxiv.org/abs/2303.04702)). Neural networks can be used to optimize approximate GKP states  ([arXiv:2411.01265](https://arxiv.org/abs/2411.01265)).
- _cousin_: [[concepts/qec/approximate-qecc]] — Numerically optimized codes arising from optimization routines are often approximate QECCs.
