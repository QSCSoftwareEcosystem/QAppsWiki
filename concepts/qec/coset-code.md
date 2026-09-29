---
type: concept
name: Coset-based quantum LDPC code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/general-qldpc
- concepts/qec/two-block-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/coset_code
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: coset_code
---

# Coset-based quantum LDPC code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/coset_code) (`code_id: coset_code`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A two-block CSS code $Q_G^H(a,b)$ built from the action of a finite group $G$ on the left cosets $G/H$ of a subgroup $H$, generalizing 2BGA codes to a much larger family of quantum LDPC codes. The length $n=2[G:H]$ is even, being twice the index of $H$ in $G$.

The building blocks are permutation matrices $\mathbf{L}(g)$ and $\mathbf{R}(g)$ representing, respectively, the left action of $G$ and the right action of the normalizer $N_G(H)$ on the $m=[G:H]$ cosets.
These two actions commute, so for group algebra elements $a\in\mathbb{F}_q[G]$ and $b\in\mathbb{F}_q[N_G(H)]$ the matrices $\mathbf{L}(a)$ and $\mathbf{R}(b)$ commute and yield a valid CSS code with parity-check matrices
\begin{align}
  H_X=[\mathbf{L}(a)\mid \mathbf{R}(b)]~,\qquad H_Z=[-\mathbf{R}(b)^T\mid \mathbf{L}(a)^T]
\end{align}
on $n=2m$ qudits, with stabilizer generators of weight at most $w_a+w_b$, where $w_a$ and $w_b$ are the weights of $a$ and $b$  ([arXiv:2606.17268](https://arxiv.org/abs/2606.17268)).

A computer search over non-abelian groups and their non-normal subgroups yields new weight-six codes $⟦48,8,6⟧$, $⟦96,8,10⟧$, and $⟦224,12,16⟧$, and weight-eight codes $⟦84,16,8⟧$, $⟦112,16,10⟧$, $⟦128,16,12⟧$, and $⟦168,16,15⟧$  ([arXiv:2606.17268](https://arxiv.org/abs/2606.17268)).

(source: raw/error-correction-zoo.md)

## Decoders

- BP-OSD decoding; performance under several decoders is compared in Ref.  ([arXiv:2606.17268](https://arxiv.org/abs/2606.17268)).
- A maximally packed syndrome-extraction circuit of depth $w+2$, including state initialization and measurement, exists for any code of maximum stabilizer weight $w$, generalizing the depth-eight bivariate bicycle schedule  ([arXiv:2606.17268](https://arxiv.org/abs/2606.17268)).

## Threshold

- Circuit-level noise thresholds of $\approx 0.65\%$ for the weight-six family and $\approx 0.35\%$ for the weight-eight family under BP-OSD decoding  ([arXiv:2606.17268](https://arxiv.org/abs/2606.17268)).

## Relations

- _parent_: [[concepts/qec/two-block-quantum]] — Coset-based codes are two-block CSS codes whose commuting blocks $\mathbf{L}(a)$ and $\mathbf{R}(b)$ are the matrices of a group acting on the left and right of the cosets of a subgroup  ([arXiv:2606.17268](https://arxiv.org/abs/2606.17268)).
- _parent_: [[concepts/qec/general-qldpc]] — A coset-based code $Q_G^H(a,b)$ has stabilizer generators of weight at most $w_a+w_b$, so it is a quantum LDPC code when $a$ and $b$ have bounded weight  ([arXiv:2606.17268](https://arxiv.org/abs/2606.17268)).
