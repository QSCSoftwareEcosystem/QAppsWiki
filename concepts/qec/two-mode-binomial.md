---
type: concept
name: Two-mode binomial code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/binomial
- concepts/qec/chi2
- concepts/qec/chuang-leung-yamamoto
- concepts/qec/group-representation
- concepts/qec/oscillators-concatenated
- concepts/qec/quantum-parity
- concepts/qec/tiger
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/two-mode_binomial
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: two-mode_binomial
---

# Two-mode binomial code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/two-mode_binomial) (`code_id: two-mode_binomial`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Two-mode constant-energy CLY code whose coefficients are square-roots of binomial coefficients.

The simplest two-mode $S=1$ code is an analogue of the "0-2-4" single-mode binomial code  ([arXiv:quant-ph/9811011](https://arxiv.org/abs/quant-ph/9811011)), with codewords
\begin{align}
\begin{split}
  |\overline{0}\rangle&=\frac{1}{\sqrt{2}}\left(|40\rangle+|04\rangle\right)\\
  |\overline{1}\rangle&=|22\rangle~.
\end{split}
\end{align}

An alternative basis for general codewords is
\begin{align}
  |\overline{\mu}\rangle=\frac{1}{2^{J}}\sum_{m=0}^{2J}\left(-1\right)^{\mu m}\sqrt{{2J \choose m}}\left|2J-(S+1)m,(S+1)m\right\rangle~,
\end{align}
with spacing $S$ and dephasing error parameter $N$ such that $J = \frac{1}{2}(N+1)(S+1)$  ([arXiv:1602.00008](https://arxiv.org/abs/1602.00008)).
The $S=0$ version can be obtained by applying a $50:50$ beamsplitter to the highest-weight Fock states $|2J,0\rangle$ and $|0,2J\rangle$  ([arXiv:1512.07605](https://arxiv.org/abs/1512.07605)); in this case, codewords are two-mode binomial coherent states  ([doi:10.1088/0305-4470/4/3/009](https://doi.org/10.1088/0305-4470/4/3/009), [doi:10.1103/PhysRevA.6.2211](https://doi.org/10.1103/PhysRevA.6.2211), [arXiv:2104.10581](https://arxiv.org/abs/2104.10581)).

(source: raw/error-correction-zoo.md)

## Protection

The code exactly detects dephasing errors $\hat{\mathbf{a}}^{\dagger \mathbf{p}}\hat{\mathbf{a}}^{\mathbf{p}}$ whenever $p_1+p_2<\Delta$  ([arXiv:2411.09668](https://arxiv.org/abs/2411.09668)).
It also detects $p_1$ photon loss errors $\hat{\mathbf{a}}^{\mathbf{p}}$ and $p_2$ photon gain errors $\hat{\mathbf{a}}^{\dagger \mathbf{p}}$ whenever $p_1+p_2\leq S$  ([arXiv:2411.09668](https://arxiv.org/abs/2411.09668)).

## General gates

- A beamsplitter is a logical operation for the $S=0$ two-mode binomial code  ([arXiv:2411.09668](https://arxiv.org/abs/2411.09668)).

## Relations

- _parent_: [[concepts/qec/chuang-leung-yamamoto]]
- _cousin_: [[concepts/qec/tiger]] — The two-mode binomial code for $S=0$ is a tiger code with $G = (2,-2)$ and $H = (1,1)$  ([arXiv:2411.09668](https://arxiv.org/abs/2411.09668)). It generalizes to the multinomial code, an $n$-mode tiger code encoding a qu$n$it in generalized $SU(n)$ coherent states  ([arXiv:2411.09668](https://arxiv.org/abs/2411.09668), [doi:10.1088/0305-4470/26/2/018](https://doi.org/10.1088/0305-4470/26/2/018)).
- _cousin_: [[concepts/qec/binomial]] — Two-mode binomial codes are two-mode analogues of binomial codes.
- _cousin_: [[concepts/qec/chi2]] — Two-mode binomial codes  ([arXiv:1709.05302](https://arxiv.org/abs/1709.05302)) are closely related to three-mode $\chi^2$ binomial codes  ([arXiv:1709.05302](https://arxiv.org/abs/1709.05302)).
- _cousin_: [[concepts/qec/oscillators-concatenated]] — Two-mode binomial codes can be concatenated with repetition codes to yield bosonic analogues of QPCs  ([arXiv:1512.07605](https://arxiv.org/abs/1512.07605)).
- _cousin_: [[concepts/qec/quantum-parity]] — Two-mode binomial codes can be concatenated with repetition codes to yield bosonic analogues of QPCs  ([arXiv:1512.07605](https://arxiv.org/abs/1512.07605)).
- _cousin_: [[concepts/qec/group-representation]] — An application of the group-representation encoding construction  ([arXiv:2306.11621](https://arxiv.org/abs/2306.11621)) yields a family of two-mode codes that closely resemble the two-mode binomial codes  ([arXiv:2508.20647](https://arxiv.org/abs/2508.20647)).
