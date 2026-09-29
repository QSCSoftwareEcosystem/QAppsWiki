---
type: concept
name: Three-block CSS code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/multi-block-quantum
- concepts/qec/two-block-quantum
- concepts/qec/xyz-product
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/three_block_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: three_block_quantum
---

# Three-block CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/three_block_quantum) (`code_id: three_block_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Galois-qudit CSS code constructed from three pairwise commuting square matrices $A$, $B$, and $C$; the case $t=3$ of multi-block CSS codes. The four-term chain complex underlying the code provides a complete set of metachecks in one basis, given by explicit closed-form check matrices.

The complex $\text{mbc}(A,B,C)$ has boundary matrices  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910))
\begin{align}
  Q_1=\left[C \,|\, B \;\, A\right],\quad
  Q_2=\left[
  \begin{array}{cc|c}
    B& A&0\\ \hline -C&0 &A\\ 0& -C& -B
  \end{array}
  \right],\quad
  Q_3=\left[
  \begin{array}{c}
    A\\-B\\ \hline C
  \end{array}
  \right]~,
\end{align}
which satisfy $Q_1 Q_2 = 0$ and $Q_2 Q_3 = 0$ whenever the three blocks commute.
The level-one code $\text{CSS}(Q_1,Q_2^T)$ has $H_X = Q_1$ and $H_Z = Q_2^T$, with qudits arranged in three blocks.
The matrix $M_Z = Q_3^T$ satisfies $M_Z H_Z = 0$ and provides a complete set of $Z$-type metachecks; the mirror level-two code $\text{CSS}(Q_2,Q_3^T)$ instead admits $X$-type metachecks provided by $Q_1$.

For qubit codes, minus signs can be dropped, and the level-one code can be written as  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714))
\begin{align}
  H_X = \left[A^T\, B^T\, C^T\right],\quad
  H_Z = \left[
  \begin{array}{ccc}
    C&0&A\\ 0&C&B\\ B&A&0
  \end{array}
  \right],\quad
  H_{\text{meta}} = \left[B\, A\, C\right]~,
\end{align}
with metachecks satisfying $H_{\text{meta}} H_Z = 0$.
There is one block of $X$-type checks and three blocks of $Z$-type checks, so only the $Z$-type checks are redundant; the codes can admit single-shot decoding in the $Z$ basis but not, in general, in the $X$ basis.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/multi-block-quantum]] — Three-block CSS codes are multi-block CSS codes with $t=3$.
- _cousin_: [[concepts/qec/two-block-quantum]] — Three-block (two-block) CSS codes are constructed from three (two) commuting square matrices.
- _cousin_: [[concepts/qec/xyz-product]] — The XYZ product yields non-CSS codes from a three-fold product of three classical codes, while three-block CSS codes arise from a three-fold product of two-term chain complexes defined by three commuting square matrices.
